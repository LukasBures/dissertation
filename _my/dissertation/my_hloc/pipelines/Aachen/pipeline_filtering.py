import argparse
import subprocess
import sys
from pathlib import Path
from pprint import pformat
import os
import itertools

import torch
from configs import feature_configs, matcher_configs, retrieval_configs
from hloc import (
    colmap_from_nvm,
    extract_features,
    localize_sfm,
    match_features,
    pairs_from_covisibility,
    pairs_from_retrieval,
    triangulation,
)
from feature_filter import FeatureFilter


# Parameters.
parser = argparse.ArgumentParser()
parser.add_argument("--dataset", type=Path, help="Path to the dataset.")
parser.add_argument("--outputs", type=Path, help="Path to the output directory.")
parser.add_argument("--num_covis", type=int, default=20, help="Number of image pairs for SfM, default: %(default)s")
parser.add_argument("--num_loc", type=int, default=50, help="Number of image pairs for loc, default: %(default)s")
parser.add_argument("--retrieval_conf", type=str, help="Retrieval config")
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

# Paths.
dataset = args.dataset
images = dataset / "images/images_upright/"

# Configurations.
outputs = args.outputs  # where everything will be saved
sift_sfm = outputs / "sfm_sift"  # from which we extract the reference poses
reference_sfm = outputs / "sfm_superpoint+superglue"  # the SfM model we will build
sfm_pairs = outputs / f"pairs-db-covis{args.num_covis}.txt"  # top-k most covisible in SIFT model
loc_pairs = outputs / f"pairs-query-netvlad{args.num_loc}.txt"  # top-k retrieved by NetVLAD
static_from: int = args.static_from
static_to: int = args.static_to
static_step: int = args.static_step
dynamic_from: int = args.dynamic_from
dynamic_to: int = args.dynamic_to
dynamic_step: int = args.dynamic_step
segmentations_file = args.segmentations_file

# Test package versions.
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

# pick one of the configurations for extraction and matching
retrieval_conf = retrieval_configs[args.retrieval_conf]
feature_conf = feature_configs[args.feature_conf]
matcher_conf = matcher_configs[args.matcher_conf]

# Print used configs.
print(f"\nSelected retrieval configuration:\n{pformat(retrieval_conf)}")
print(f"\nSelected feature configuration:\n{pformat(feature_conf)}")
print(f"\nSelected matcher configuration:\n{pformat(matcher_conf)}")
print("\n")

static_percentages: list = list(range(static_from, static_to + static_step, static_step))
dynamic_percentages: list = list(range(dynamic_from, dynamic_to + dynamic_step, dynamic_step))
static_dynamic_combinations: list = list(itertools.product(static_percentages, dynamic_percentages))
print("Planned static/dynamic percentages:")
for static_dynamic_combination in static_dynamic_combinations:
    print(f"Static = {' ' if static_dynamic_combination[0] < 100 else ''}{static_dynamic_combination[0]}%, dynamic = {' ' if static_dynamic_combination[1] < 100 else ''}{static_dynamic_combination[1]}%")
print("\n")
print("-" * 50)
print("STARTING\n\n")

all_features_pth = extract_features.main(feature_conf, images, outputs)
colmap_from_nvm.main(
    dataset / "3D-models/aachen_cvpr2018_db.nvm",
    dataset / "3D-models/database_intrinsics.txt",
    dataset / "aachen.db",
    sift_sfm,
)

pairs_from_covisibility.main(sift_sfm, sfm_pairs, num_matched=args.num_covis)
sfm_matches = match_features.main(matcher_conf, sfm_pairs, feature_conf["output"], outputs)

for static_percentage in static_percentages:
    for dynamic_percentage in dynamic_percentages:
        # Print static and dynamic percentages.
        print("-" * 50)
        print(f"Starting: static: {static_percentage}%, dynamic: {dynamic_percentage}")

        # Filter dynamic / static features.
        pth, nm = os.path.split(os.path.abspath(all_features_pth))
        new_features_pth = os.path.join(pth, "new_" + nm)
        ff = FeatureFilter(h5_file_path=all_features_pth, new_h5_file_path=new_features_pth, segmentations_file=segmentations_file)
        filter_summary_info = ff.filter_and_update(static_percentage_keep=static_percentage, dynamic_percentage_keep=dynamic_percentage)
        print(f"Filter summary info: {filter_summary_info}.")

        # Triangulation.
        triangulation.main(reference_sfm, sift_sfm, images, sfm_pairs, new_features_pth, sfm_matches, colmap_path="colmap")

        # Global descriptors, pairs, and local matches.
        global_descriptors = extract_features.main(retrieval_conf, images, outputs)
        pairs_from_retrieval.main(global_descriptors, loc_pairs, args.num_loc, query_prefix="query", db_model=reference_sfm)
        loc_matches = match_features.main(matcher_conf, loc_pairs, feature_conf['output'], outputs)

        if "superpoint" in args.feature_conf.lower() and "superglue" in args.matcher_conf.lower():
            # Not required with SuperPoint + SuperGlue.
            covisibility_clustering: bool = False
        else:
            covisibility_clustering: bool = True

        results = outputs / f"Aachen_hloc-{args.feature_conf.lower()}+{args.matcher_conf.lower()}_netvlad{args.num_loc}+static{static_percentage}_dynamic{dynamic_percentage}.txt"
        localize_sfm.main(
            reference_sfm,
            dataset / "queries/*_time_queries_with_intrinsics.txt",
            loc_pairs,
            new_features_pth,
            loc_matches,
            results,
            covisibility_clustering=covisibility_clustering,
        )
