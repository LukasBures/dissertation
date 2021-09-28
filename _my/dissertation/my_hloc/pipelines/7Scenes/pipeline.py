import argparse
import logging
import subprocess
import sys
from pathlib import Path
from pprint import pformat

import torch
from configs import feature_configs, matcher_configs
from hloc import extract_features, localize_sfm, match_features, pairs_from_covisibility, triangulation

from .cambridge_utils import create_query_list_with_intrinsics, evaluate
from .create_gt_sfm import correct_sfm_with_gt_depth
from .utils import create_reference_sfm

SCENES = ["chess", "fire", "heads", "office", "pumpkin", "redkitchen", "stairs"]


def run_scene(
    images, gt_dir, retrieval, outputs, results, num_covis, use_dense_depth, feature_conf, matcher_conf, depth_dir=None
):
    outputs.mkdir(exist_ok=True, parents=True)
    ref_sfm_sift = outputs / "sfm_sift"
    ref_sfm = outputs / "sfm_superpoint+superglue"
    query_list = outputs / "query_list_with_intrinsics.txt"

    # TODO: for every experiment?
    # feature_conf = superpoint_7scenes
    # matcher_conf = match_features.confs["superglue"]
    matcher_conf["model"]["sinkhorn_iterations"] = 5

    test_list = gt_dir / "list_test.txt"
    create_reference_sfm(gt_dir, ref_sfm_sift, test_list)
    create_query_list_with_intrinsics(gt_dir, query_list, test_list)

    features = extract_features.main(feature_conf, images, outputs, as_half=True)

    sfm_pairs = outputs / f"pairs-db-covis{num_covis}.txt"
    pairs_from_covisibility.main(ref_sfm_sift, sfm_pairs, num_matched=num_covis)
    sfm_matches = match_features.main(matcher_conf, sfm_pairs, feature_conf["output"], outputs)
    if not (use_dense_depth and ref_sfm.exists()):
        triangulation.main(ref_sfm, ref_sfm_sift, images, sfm_pairs, features, sfm_matches, colmap_path="colmap")

    if use_dense_depth:
        assert depth_dir is not None
        ref_sfm_fix = outputs / "sfm_superpoint+superglue+depth"
        correct_sfm_with_gt_depth(ref_sfm, depth_dir, ref_sfm_fix)
        ref_sfm = ref_sfm_fix

    loc_matches = match_features.main(matcher_conf, retrieval, feature_conf["output"], outputs)

    localize_sfm.main(
        ref_sfm,
        query_list,
        retrieval,
        features,
        loc_matches,
        results,
        covisibility_clustering=False,
        prepend_camera_name=True,
    )


# parameters
parser = argparse.ArgumentParser()
parser.add_argument("--scenes", default=SCENES, choices=SCENES, nargs="+")
parser.add_argument("--overwrite", action="store_true")
parser.add_argument(
    "--dataset", type=Path, default="datasets/7scenes", help="Path to the dataset, default: %(default)s"
)
parser.add_argument(
    "--outputs", type=Path, default="outputs/7scenes", help="Path to the output directory, default: %(default)s"
)
parser.add_argument("--use_dense_depth", action="store_true")
parser.add_argument("--num_covis", type=int, default=30, help="Number of image pairs for SfM, default: %(default)s")
parser.add_argument("--gpu_number", type=int, default=0, help="active GPU")
parser.add_argument("--feature_conf", type=str, help="Feature config")
parser.add_argument("--matcher_conf", type=str, help="Matcher config")
# parser.add_argument("--retrieval_conf", type=str, help="Retrieval config")
args = parser.parse_args()

# Setup the paths
gt_dirs = args.dataset / "7scenes_sfm_triangulated/{scene}/triangulated"
retrieval_dirs = args.dataset / "7scenes_densevlad_retrieval_top_10"

# configs
outputs = args.outputs  # where everything will be saved
dataset = args.dataset
scenes = args.scenes
overwrite = args.overwrite
use_dense_depth = args.use_dense_depth
num_covis = args.num_covis


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

# pick one of the configurations for extraction and matching
# retrieval_conf = retrieval_configs[args.retrieval_conf]
feature_conf = feature_configs[args.feature_conf]
matcher_conf = matcher_configs[args.matcher_conf]

# Print used configs
# print(f"\nSelected retrieval configuration:\n{pformat(retrieval_conf)}")
print(f"\nSelected feature configuration:\n{pformat(feature_conf)}")
print(f"\nSelected matcher configuration:\n{pformat(matcher_conf)}")
print("\n")


all_results = {}
for scene in scenes:
    logging.info(f"Working on scene '{scene}'.")
    results = outputs / scene / "results_{}.txt".format("dense" if use_dense_depth else "sparse")
    if overwrite or not results.exists():
        run_scene(
            dataset / scene,
            Path(str(gt_dirs).format(scene=scene)),
            retrieval_dirs / f"{scene}_top10.txt",
            outputs / scene,
            results,
            num_covis,
            use_dense_depth,
            feature_conf,
            matcher_conf,
            depth_dir=dataset / f"depth/7scenes_{scene}/train/depth",
        )
    all_results[scene] = results

for scene in scenes:
    logging.info(f"Evaluate scene '{scene}'.")
    gt_dir = Path(str(gt_dirs).format(scene=scene))
    evaluate(gt_dir, all_results[scene], gt_dir / "list_test.txt")
