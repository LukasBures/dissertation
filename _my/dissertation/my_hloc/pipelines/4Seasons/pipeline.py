import argparse
import logging
import subprocess
import sys
from pathlib import Path
from pprint import pformat

import torch
from configs import feature_configs, matcher_configs
from hloc import extract_features, localize_sfm, match_features, pairs_from_poses, triangulation
from utils import (
    build_empty_colmap_model,
    delete_unused_images,
    evaluate_submission,
    generate_localization_pairs,
    generate_query_lists,
    get_timestamps,
    prepare_submission,
)

relocalization_files = {
    "training": "RelocalizationFilesTrain/relocalizationFile_recording_2020-03-24_17-36-22.txt",
    "validation": "RelocalizationFilesVal/relocalizationFile_recording_2020-03-03_12-03-23.txt",
    "test0": "RelocalizationFilesTest/relocalizationFile_recording_2020-03-24_17-45-31_*.txt",
    "test1": "RelocalizationFilesTest/relocalizationFile_recording_2020-04-23_19-37-00_*.txt",
}

parser = argparse.ArgumentParser()
parser.add_argument(
    "--sequence",
    type=str,
    required=True,
    choices=["training", "validation", "test0", "test1"],
    help="Sequence to be relocalized.",
)
parser.add_argument(
    "--dataset", type=Path, default="datasets/4Seasons", help="Path to the dataset, default: %(default)s"
)
parser.add_argument(
    "--outputs", type=Path, default="outputs/4Seasons", help="Path to the output directory, default: %(default)s"
)
parser.add_argument("--num_ref", type=int, default=20, help="Number of image pairs for SfM, default: %(default)s")
parser.add_argument("--num_loc", type=int, default=10, help="Number of image pairs for loc, default: %(default)s")
parser.add_argument("--feature_conf", type=str, help="Feature config")
parser.add_argument("--matcher_conf", type=str, help="Matcher config")
parser.add_argument("--gpu_number", type=int, default=0, help="active GPU")
args = parser.parse_args()


num_ref_pairs = args.num_ref
num_loc_pairs = args.num_loc
feature_conf = feature_configs[args.feature_conf]
matcher_conf = matcher_configs[args.matcher_conf]

# Test package versions
print(f"__Python VERSION: {sys.version}")  # 3.6.12 (default, Aug 18 2020, 02:08:22)
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

# Print used configs
print(f"\nSelected feature configuration:\n{pformat(feature_conf)}")
print(f"\nSelected matcher configuration:\n{pformat(matcher_conf)}")
print("\n")


# -----------------------------------------
# prepare reference

ref_dir = args.dataset / "reference"
assert ref_dir.exists(), f"{ref_dir} does not exist"
ref_images = ref_dir / "undistorted_images"

output_dir = args.outputs
output_dir.mkdir(exist_ok=True, parents=True)
ref_sfm_empty = output_dir / "sfm_reference_empty"
ref_sfm = output_dir / "sfm_superpoint+superglue"

ref_pairs = output_dir / f"pairs-db-dist{num_ref_pairs}.txt"

# Only reference images that have a pose are used in the pipeline.
# To save time in feature extraction, we delete unsused images.
delete_unused_images(ref_images, get_timestamps(ref_dir / "poses.txt", 0))

# Build an empty COLMAP model containing only camera and images
# from the provided poses and intrinsics.
build_empty_colmap_model(ref_dir, ref_sfm_empty)

# Match reference images that are spatially close.
pairs_from_poses.main(ref_sfm_empty, ref_pairs, num_ref_pairs)

# Extract, match, and triangulate the reference SfM model.
ffile = extract_features.main(feature_conf, ref_images, output_dir)
mfile = match_features.main(matcher_conf, ref_pairs, feature_conf["output"], output_dir)
triangulation.main(ref_sfm, ref_sfm_empty, ref_images, ref_pairs, ffile, mfile)

# -----------------------------------------
# localize

sequence = args.sequence

data_dir = args.dataset
ref_dir = data_dir / "reference"
assert ref_dir.exists(), f"{ref_dir} does not exist"
seq_dir = data_dir / sequence
assert seq_dir.exists(), f"{seq_dir} does not exist"
seq_images = seq_dir / "undistorted_images"
reloc = ref_dir / relocalization_files[sequence]

output_dir = args.outputs
output_dir.mkdir(exist_ok=True, parents=True)
query_list = output_dir / f"{sequence}_queries_with_intrinsics.txt"
ref_pairs = output_dir / "pairs-db-dist20.txt"
ref_sfm = output_dir / "sfm_superpoint+superglue"
results_path = output_dir / f"localization_{sequence}_hloc+superglue.txt"
submission_dir = output_dir / "submission_hloc+superglue"

loc_pairs = output_dir / f"pairs-query-{sequence}-dist{num_loc_pairs}.txt"

# Not all query images that are used for the evaluation
# To save time in feature extraction, we delete unused images.
timestamps = get_timestamps(reloc, 1)
delete_unused_images(seq_images, timestamps)

# Generate a list of query images with their intrinsics.
generate_query_lists(timestamps, seq_dir, query_list)

# Generate the localization pairs from the given reference frames.
generate_localization_pairs(sequence, reloc, num_loc_pairs, ref_pairs, loc_pairs)

# Extract, match, amd localize.
ffile = extract_features.main(feature_conf, seq_images, output_dir)
mfile = match_features.main(matcher_conf, loc_pairs, feature_conf["output"], output_dir)
localize_sfm.main(ref_sfm, query_list, loc_pairs, ffile, mfile, results_path)

# Convert the absolute poses to relative poses with the reference frames.
submission_dir.mkdir(exist_ok=True)
prepare_submission(results_path, reloc, ref_dir / "poses.txt", submission_dir)

# If not a test sequence: evaluation the localization accuracy
if "test" not in sequence:
    logging.info("Evaluating the relocalization submission...")
    evaluate_submission(submission_dir, reloc)
