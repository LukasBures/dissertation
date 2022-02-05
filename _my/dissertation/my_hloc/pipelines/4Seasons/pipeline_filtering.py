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
from utils2 import (
    delete_unused_images,
    evaluate_submission_filtering,
    generate_localization_pairs,
    generate_query_lists,
    get_timestamps,
    prepare_submission,
)

sys.path.append("/home/lukas/PycharmProjects/dissertation/Hierarchical-Localization")
try:
    user_paths = os.environ["PYTHONPATH"].split(os.pathsep)
except KeyError:
    pass
else:
    print(f"__PYTHONPATH: {user_paths}")

from feature_filter import FeatureFilter
from hloc import extract_features, localize_sfm, match_features

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
parser.add_argument("--static_from", type=int, default=100, help="Static from percentage.")
parser.add_argument("--static_to", type=int, default=100, help="Static to percentage (included).")
parser.add_argument("--static_step", type=int, default=10, help="Static percentage step.")
parser.add_argument("--dynamic_from", type=int, default=100, help="Dynamic from percentage.")
parser.add_argument("--dynamic_to", type=int, default=100, help="Dynamic to percentage (included).")
parser.add_argument("--dynamic_step", type=int, default=10, help="Dynamic percentage step.")
parser.add_argument("--segmentations_file", type=Path, help="Path to the file with semantic segmentations.")
args = parser.parse_args()

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

if static_from == static_step == static_to == 0:
    static_percentages: list = [0]
else:
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

sequence: str = args.sequence
data_dir: Path = args.dataset
output_dir: Path = args.outputs
segmentations_file_path: Path = args.segmentations_file
output_dir.mkdir(exist_ok=True, parents=True)

ref_dir: Path = data_dir / "reference"
assert ref_dir.exists(), f"{ref_dir} does not exist"
seq_dir: Path = data_dir / sequence
assert seq_dir.exists(), f"{seq_dir} does not exist"
seq_images: Path = seq_dir / "undistorted_images"
reloc: Path = ref_dir / relocalization_files[sequence]
ref_sfm: Path = output_dir / "sfm_superpoint+superglue"
submission_dir: Path = output_dir / f"submission_superpoint+superglue"
submission_dir.mkdir(exist_ok=True)
query_list: Path = output_dir / f"{sequence}_queries_with_intrinsics.txt"
ref_pairs: Path = output_dir / "pairs-db-dist20.txt"
results_path: Path = output_dir / f"localization_{sequence}_hloc+superglue.txt"
loc_pairs: Path = output_dir / f"pairs-query-{sequence}-dist{num_loc_pairs}.txt"

for static_percentage in static_percentages:
    for dynamic_percentage in dynamic_percentages:
        filtered_kp_file_prefix: str = f"s{static_percentage}_d{dynamic_percentage}_"

        # Print static and dynamic percentages.
        print("-" * 50)
        print(f"Starting: static: {static_percentage}%, dynamic: {dynamic_percentage}")

        # Not all query images that are used for the evaluation.
        # To save time in feature extraction, we delete unused images.
        timestamps = get_timestamps(files=reloc, idx=1)
        delete_unused_images(root=seq_images, timestamps=timestamps)

        # Generate a list of query images with their intrinsics.
        generate_query_lists(timestamps=timestamps, seq_dir=seq_dir, out_path=query_list)

        # Generate the localization pairs from the given reference frames.
        generate_localization_pairs(
            sequence=sequence, reloc=reloc, num=num_loc_pairs, ref_pairs=ref_pairs, out_path=loc_pairs
        )

        # Extract features.
        all_features_pth = extract_features.main(conf=feature_conf, image_dir=seq_images, export_dir=output_dir)

        # Filter dynamic / static features.
        pth, nm = os.path.split(os.path.abspath(all_features_pth))
        new_features_pth: Path = Path(os.path.join(pth, filtered_kp_file_prefix + nm))
        ff: FeatureFilter = FeatureFilter(
            h5_file_path=str(all_features_pth),
            new_h5_file_path=str(new_features_pth),
            segmentation_h5_file_path=str(segmentations_file_path),
            dynamic_group_classes=["human", "vehicle"],
        )
        ff.filter_and_update_kp_4seasons(
            static_percentage_keep=static_percentage, dynamic_percentage_keep=dynamic_percentage
        )
        del ff

        # Match features.
        matches_file = match_features.main(
            conf=matcher_conf,
            pairs=loc_pairs,
            features=filtered_kp_file_prefix + feature_conf["output"],
            export_dir=output_dir,
        )

        # Localize features.
        localize_sfm.main(
            reference_sfm=ref_sfm,
            queries=query_list,
            retrieval=loc_pairs,
            features=new_features_pth,
            matches=matches_file,
            results=results_path,
            covisibility_clustering=False,
        )

        # Convert the absolute poses to relative poses with the reference frames.
        prepare_submission(results=results_path, relocs=reloc, poses_path=ref_dir / "poses.txt", out_dir=submission_dir)

        # If not a test sequence: evaluation the localization accuracy
        if "test" not in sequence:
            print("Evaluating the relocalization submission ...")
            static_dynamic_info = {"static": static_percentage, "dynamic": dynamic_percentage}
            evaluate_submission_filtering(
                submission_dir=submission_dir, relocs=reloc, static_dynamic_info=static_dynamic_info
            )
        else:
            print(f"For sequence '{sequence}' can not evaluate relocalization.")

        # Empty space:
        # Delete new features
        if os.path.exists(str(new_features_pth)):
            os.remove(str(new_features_pth))
            print(f"Removed file: {str(new_features_pth)}")
        else:
            print(f"Can not delete the file as it doesn't exists: {str(new_features_pth)}")

        # Query
        fn_query: str = (
            f"{filtered_kp_file_prefix}{feature_conf['output']}_"
            f"{matcher_conf['output']}_pairs-query-{sequence}-dist{num_loc_pairs}.h5"
        )
        query_path: Path = output_dir / fn_query
        if os.path.exists(str(query_path)):
            os.remove(str(query_path))
            print(f"Removed file: {str(query_path)}")
        else:
            print(f"Can not delete the file as it doesn't exists: {str(query_path)}")
