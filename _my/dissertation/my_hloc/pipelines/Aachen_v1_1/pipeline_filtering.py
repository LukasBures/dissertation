import argparse
import itertools
import os
import subprocess
import sys
from pathlib import Path
from pprint import pformat

import pycolmap
import torch
from configs import feature_configs, matcher_configs, retrieval_configs

sys.path.append("/home/lukas/PycharmProjects/dissertation/Hierarchical-Localization")
try:
    user_paths = os.environ["PYTHONPATH"].split(os.pathsep)
except KeyError:
    pass
else:
    print(f"__PYTHONPATH: {user_paths}")

from feature_filter import FeatureFilter
from hloc import (
    colmap_from_nvm,
    extract_features,
    localize_sfm,
    match_features,
    pairs_from_covisibility,
    pairs_from_retrieval,
    triangulation,
)

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

# Configurations.
dataset_name: Path = args.dataset
images_path: Path = dataset_name / "images/images_upright/"
outputs_path: Path = args.outputs  # where everything will be saved
sift_sfm_path: Path = outputs_path / "sfm_sift"  # from which we extract the reference poses
reference_sfm_path: Path = outputs_path / "sfm_superpoint+superglue"  # the SfM model we will build
sfm_pairs_path: Path = outputs_path / f"pairs-db-covis{args.num_covis}.txt"  # top-k most covisible in SIFT model
loc_pairs_path: Path = outputs_path / f"pairs-query-netvlad{args.num_loc}.txt"  # top-k retrieved by NetVLAD
static_from: int = args.static_from
static_to: int = args.static_to
static_step: int = args.static_step
dynamic_from: int = args.dynamic_from
dynamic_to: int = args.dynamic_to
dynamic_step: int = args.dynamic_step
segmentations_file_path: Path = args.segmentations_file

# Test package versions.
print(f"__Python VERSION: {sys.version}")  # 3.6.12 (default, Aug 18 2020, 02:08:22)
print(f"__pycolmap VERSION: {pycolmap.__version__}")  # 0.1.0
print(f"__triangulation.main parameters: {triangulation.main.__code__.co_varnames}")
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
retrieval_conf: dict = retrieval_configs[args.retrieval_conf]
feature_conf: dict = feature_configs[args.feature_conf]
matcher_conf: dict = matcher_configs[args.matcher_conf]

# Print used configs.
print(f"\nSelected retrieval configuration:\n{pformat(retrieval_conf)}")
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

all_features_pth = extract_features.main(conf=feature_conf, image_dir=images_path, export_dir=outputs_path)
colmap_from_nvm.main(
    nvm=dataset_name / "3D-models/aachen_cvpr2018_db.nvm",
    intrinsics=dataset_name / "3D-models/database_intrinsics.txt",
    database=dataset_name / "aachen.db",
    output=sift_sfm_path,
)

pairs_from_covisibility.main(sift_sfm_path, sfm_pairs_path, num_matched=args.num_covis)

for static_percentage in static_percentages:
    for dynamic_percentage in dynamic_percentages:
        filtered_kp_file_prefix: str = f"s{static_percentage}_d{dynamic_percentage}_"

        # Print static and dynamic percentages.
        print("-" * 50)
        print(f"Starting: static: {static_percentage}%, dynamic: {dynamic_percentage}")

        # Filter dynamic / static features.
        pth, nm = os.path.split(os.path.abspath(all_features_pth))
        new_features_pth = Path(os.path.join(pth, filtered_kp_file_prefix + nm))
        ff = FeatureFilter(
            h5_file_path=str(all_features_pth),
            new_h5_file_path=str(new_features_pth),
            segmentation_h5_file_path=str(segmentations_file_path),
        )
        ff.filter_and_update_kp(static_percentage_keep=static_percentage, dynamic_percentage_keep=dynamic_percentage)
        del ff

        sfm_matches = match_features.main(
            conf=matcher_conf,
            pairs=sfm_pairs_path,
            features=filtered_kp_file_prefix + feature_conf["output"],
            export_dir=outputs_path,
        )

        # Triangulation.
        triangulation.main(
            sfm_dir=reference_sfm_path,
            reference_model=sift_sfm_path,
            image_dir=images_path,
            pairs=sfm_pairs_path,
            features=new_features_pth,
            matches=sfm_matches,
            skip_geometric_verification=False,
            verbose=True,
        )

        # Global descriptors, pairs, and local matches.
        global_descriptors = extract_features.main(conf=retrieval_conf, image_dir=images_path, export_dir=outputs_path)
        pairs_from_retrieval.main(
            descriptors=global_descriptors,
            output=loc_pairs_path,
            num_matched=args.num_loc,
            query_prefix="query",
            db_model=reference_sfm_path,
        )
        loc_matches = match_features.main(
            conf=matcher_conf,
            pairs=loc_pairs_path,
            features=filtered_kp_file_prefix + feature_conf["output"],
            export_dir=outputs_path,
        )

        results = (
            outputs_path
            / f"Aachen_hloc-{args.feature_conf.lower()}+{args.matcher_conf.lower()}_netvlad{args.num_loc}+s{static_percentage}_d{dynamic_percentage}.txt"
        )
        localize_sfm.main(
            reference_sfm=reference_sfm_path,
            queries=dataset_name / "queries/*_time_queries_with_intrinsics.txt",
            retrieval=loc_pairs_path,
            features=new_features_pth,
            matches=loc_matches,
            results=results,
            covisibility_clustering=False,
        )

        # Empty space:
        # Delete new features
        if os.path.exists(str(new_features_pth)):
            os.remove(str(new_features_pth))
        else:
            print(f"Can not delete the file as it doesn't exists: {str(new_features_pth)}")

        # Co-visibility db
        covisibility_db_path: Path = outputs_path / f"{filtered_kp_file_prefix}{feature_conf['output']}_{matcher_conf['output']}_pairs-db-covis{args.num_covis}.h5"
        if os.path.exists(str(covisibility_db_path)):
            os.remove(str(covisibility_db_path))
        else:
            print(f"Can not delete the file as it doesn't exists: {str(covisibility_db_path)}")

        # Netvlad query
        netvlad_query_path: Path = outputs_path / f"{filtered_kp_file_prefix}{feature_conf['output']}_{matcher_conf['output']}_pairs-query-netvlad{args.num_loc}.h5"
        if os.path.exists(str(netvlad_query_path)):
            os.remove(str(netvlad_query_path))
        else:
            print(f"Can not delete the file as it doesn't exists: {str(netvlad_query_path)}")
