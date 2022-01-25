import argparse
import itertools
import os
import subprocess
import sys
from pathlib import Path
from pprint import pformat

import pycolmap
import torch
from configs import feature_configs, matcher_configs
from utils2 import get_timestamps, delete_unused_images
from utils2 import generate_query_lists, generate_localization_pairs
from utils2 import prepare_submission, evaluate_submission

sys.path.append("/home/lukas/PycharmProjects/dissertation/Hierarchical-Localization")
try:
    user_paths = os.environ["PYTHONPATH"].split(os.pathsep)
except KeyError:
    pass
else:
    print(f"__PYTHONPATH: {user_paths}")

from feature_filter import FeatureFilter
from hloc import extract_features, match_features, localize_sfm, logger

relocalization_files = {
    'training': 'RelocalizationFilesTrain//relocalizationFile_recording_2020-03-24_17-36-22.txt',
    'validation': 'RelocalizationFilesVal/relocalizationFile_recording_2020-03-03_12-03-23.txt',
    'test0': 'RelocalizationFilesTest/relocalizationFile_recording_2020-03-24_17-45-31_*.txt',
    'test1': 'RelocalizationFilesTest/relocalizationFile_recording_2020-04-23_19-37-00_*.txt',
}

parser = argparse.ArgumentParser()
parser.add_argument('--sequence', type=str, required=True,
                    choices=['training', 'validation', 'test0', 'test1'],
                    help='Sequence to be relocalized.')
parser.add_argument('--dataset', type=Path, default='datasets/4Seasons',
                    help='Path to the dataset, default: %(default)s')
parser.add_argument('--outputs', type=Path, default='outputs/4Seasons',
                    help='Path to the output directory, default: %(default)s')
parser.add_argument("--num_ref", type=int, default=20, help="Number of image pairs for SfM, default: %(default)s")
parser.add_argument("--num_loc", type=int, default=10, help="Number of image pairs for loc, default: %(default)s")
parser.add_argument("--feature_conf", type=str, help="Feature config")
parser.add_argument("--matcher_conf", type=str, help="Matcher config")
parser.add_argument("--gpu_number", type=int, default=0, help="active GPU")
parser.add_argument("--static_from", type=int, default=100, help="Static from percentage.")
parser.add_argument("--static_to", type=int, default=100, help="Static to percentage (included).")
parser.add_argument("--static_step", type=int, default=10, help="Static percentage step.")
parser.add_argument("--dynamic_from", type=int, default=100, help="Dynamic from percentage.")
parser.add_argument("--dynamic_to", type=int, default=100, help="Dynamic to percentage (included).")
parser.add_argument("--dynamic_step", type=int, default=10, help="Dynamic percentage step.")
parser.add_argument("--segmentations_file", type=Path, help="Path to the file with semantic segmentations.")
args = parser.parse_args()

sequence = args.sequence
static_from: int = args.static_from
static_to: int = args.static_to
static_step: int = args.static_step
dynamic_from: int = args.dynamic_from
dynamic_to: int = args.dynamic_to
dynamic_step: int = args.dynamic_step
num_ref_pairs: int = args.num_ref
num_loc_pairs: int = args.num_loc

# Test package versions
print(f"__Python VERSION: {sys.version}")  # 3.6.12 (default, Aug 18 2020, 02:08:22)
print(f"__pycolmap VERSION: {pycolmap.__version__}")  # 0.1.0
print(f"__pyTorch VERSION: {torch.__version__}")  # 1.7.0+cu101
tmp_output = subprocess.check_output(["nvcc", "--version"])
tmp_output = tmp_output.decode("utf-8")
print(f"__CUDA VERSION: \n{tmp_output.rstrip()}")  # release 10.1, V10.1.243
print(f"__CUDNN VERSION: {torch.backends.cudnn.version()}")  # 7603
print(f"__Number CUDA Devices: {torch.cuda.device_count()}")
tmp_output = subprocess.check_output(
    ["nvidia-smi", "--format=csv", "--query-gpu=index,name,driver_version,memory.total,memory.used,memory.free"]
)
tmp_output = tmp_output.decode("utf-8")
print(f"__CUDA Devices: \n{tmp_output.rstrip()}")
print(f"__Available Devices: {torch.cuda.device_count()}")
print(f"__Current CUDA Device: {torch.cuda.get_device_name(torch.cuda.current_device())}")
torch.cuda.set_device(args.gpu_number)
print(f"__CUDA Device Changed To: {torch.cuda.get_device_name(torch.cuda.current_device())}")

# Pick one of the configurations for extraction and matching.
feature_conf: dict = feature_configs[args.feature_conf]
matcher_conf: dict = matcher_configs[args.matcher_conf]

# Print used configs
print(f"\nSelected feature configuration:\n{pformat(feature_conf)}")
print(f"\nSelected matcher configuration:\n{pformat(matcher_conf)}")
print("\n")

static_percentages: list = list(range(static_to, static_from - static_step, -static_step))
dynamic_percentages: list = list(range(dynamic_to, dynamic_from - dynamic_step, -dynamic_step))
static_dynamic_combinations: list = list(itertools.product(static_percentages, dynamic_percentages))
print("Planned static/dynamic percentages:")
for static_dynamic_combination in static_dynamic_combinations:
    if static_dynamic_combination[0] < 10:
        static_str_prefix: str = "  "
    elif 10 <= static_dynamic_combination[0] < 100:
        static_str_prefix: str = " "
    else:
        static_str_prefix: str = ""

    if static_dynamic_combination[1] < 10:
        dynamic_str_prefix: str = "  "
    elif 10 <= static_dynamic_combination[1] < 100:
        dynamic_str_prefix: str = " "
    else:
        dynamic_str_prefix: str = ""

    print(
        f"Static = {static_str_prefix}{static_dynamic_combination[0]}%, "
        f"dynamic = {dynamic_str_prefix}{static_dynamic_combination[1]}%"
    )

print("\n")
print("-" * 50)
print("STARTING\n\n")


for static_percentage in static_percentages:
    for dynamic_percentage in dynamic_percentages:
        filtered_kp_file_prefix: str = f"s{static_percentage}_d{dynamic_percentage}_"

        # Print static and dynamic percentages.
        print("-" * 50)
        print(f"Starting: static: {static_percentage}%, dynamic: {dynamic_percentage}")


data_dir = args.dataset
ref_dir = data_dir / 'reference'
assert ref_dir.exists(), f'{ref_dir} does not exist'
seq_dir = data_dir / sequence
assert seq_dir.exists(), f'{seq_dir} does not exist'
seq_images = seq_dir / 'undistorted_images'
reloc = ref_dir / relocalization_files[sequence]

output_dir = args.outputs
output_dir.mkdir(exist_ok=True, parents=True)
query_list = output_dir / f'{sequence}_queries_with_intrinsics.txt'
ref_pairs = output_dir / 'pairs-db-dist20.txt'
ref_sfm = output_dir / 'sfm_superpoint+superglue'
results_path = output_dir / f'localization_{sequence}_hloc+superglue.txt'
submission_dir = output_dir / 'submission_hloc+superglue'

num_loc_pairs = 10
loc_pairs = output_dir / f'pairs-query-{sequence}-dist{num_loc_pairs}.txt'

fconf = extract_features.confs['superpoint_max']
mconf = match_features.confs['superglue']

# Not all query images that are used for the evaluation.
# To save time in feature extraction, we delete unused images.
timestamps = get_timestamps(reloc, 1)
delete_unused_images(seq_images, timestamps)

# Generate a list of query images with their intrinsics.
generate_query_lists(timestamps, seq_dir, query_list)

# Generate the localization pairs from the given reference frames.
generate_localization_pairs(
    sequence, reloc, num_loc_pairs, ref_pairs, loc_pairs)

# Extract, match, and localize.
ffile = extract_features.main(fconf, seq_images, output_dir)
mfile = match_features.main(mconf, loc_pairs, fconf['output'], output_dir)
localize_sfm.main(
    ref_sfm, query_list, loc_pairs, ffile, mfile, results_path)

# Convert the absolute poses to relative poses with the reference frames.
submission_dir.mkdir(exist_ok=True)
prepare_submission(results_path, reloc, ref_dir / 'poses.txt', submission_dir)

# If not a test sequence: evaluation the localization accuracy.
if 'test' not in sequence:
    logger.info('Evaluating the relocalization submission...')
    evaluate_submission(submission_dir, reloc)