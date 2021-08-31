from pathlib import Path
from pprint import pformat
import argparse
import torch
import subprocess
import sys

from hloc import extract_features, match_features, triangulation
from hloc import pairs_from_covisibility, pairs_from_retrieval, localize_sfm
from configs import retrieval_configs, feature_configs, matcher_configs

# parameters
parser = argparse.ArgumentParser()
parser.add_argument("--dataset", type=Path, help="Path to the dataset.")
parser.add_argument("--outputs", type=Path, help="Path to the output directory.")
parser.add_argument("--num_covis", type=int, default=20, help="Number of image pairs for SfM, default: %(default)s")
parser.add_argument("--num_loc", type=int, default=50, help="Number of image pairs for loc, default: %(default)s")
parser.add_argument("--retrieval_conf", type=str, help="Retrieval config")
parser.add_argument("--feature_conf", type=str, help="Feature config")
parser.add_argument("--matcher_conf", type=str, help="Matcher config")
parser.add_argument("--gpu_number", type=int, default=0, help="active GPU")
args = parser.parse_args()

# Setup the paths
dataset = args.dataset
images = dataset/"images/images_upright/"
sift_sfm = dataset/"3D-models/aachen_v_1_1"

outputs = args.outputs  # where everything will be saved
reference_sfm = outputs/"sfm_superpoint+superglue"  # the SfM model we will build
sfm_pairs = outputs/f"pairs-db-covis{args.num_covis}.txt"  # top-k most covisible in SIFT model
loc_pairs = outputs/f"pairs-query-netvlad{args.num_loc}.txt"  # top-k retrieved by NetVLAD
results = outputs/f"Aachen-v1.1_hloc_superpoint+superglue_netvlad{args.num_loc}.txt"

# Test package versions
print(f'__Python VERSION: {sys.version}')  # 3.6.12 (default, Aug 18 2020, 02:08:22)
print(f'__pyTorch VERSION: {torch.__version__}')  # 1.7.0+cu101
tmp_output = subprocess.check_output(["nvcc", "--version"])
tmp_output = tmp_output.decode("utf-8")
print(f'__CUDA VERSION: \n{tmp_output.rstrip()}')  # release 10.1, V10.1.243
print(f'__CUDNN VERSION: {torch.backends.cudnn.version()}')  # 7603
print(f'__Number CUDA Devices: {torch.cuda.device_count()}')
tmp_output = subprocess.check_output(["nvidia-smi", "--format=csv", "--query-gpu=index,name,driver_version,memory.total,memory.used,memory.free"])
tmp_output = tmp_output.decode("utf-8")
print(f'__CUDA Devices: \n{tmp_output.rstrip()}')
print(f'__Available Devices: {torch.cuda.device_count()}')
print(f'__Current CUDA Device: {torch.cuda.get_device_name(torch.cuda.current_device())}')
torch.cuda.set_device(args.gpu_number)
print(f'__CUDA Device Changed To: {torch.cuda.get_device_name(torch.cuda.current_device())}')

# pick one of the configurations for extraction and matching
retrieval_conf = retrieval_configs[args.retrieval_conf]
feature_conf = feature_configs[args.feature_conf]
matcher_conf = matcher_configs[args.matcher_conf]

# Print used configs
print(f"\nSelected retrieval configuration:\n{pformat(retrieval_conf)}")
print(f"\nSelected feature configuration:\n{pformat(feature_conf)}")
print(f"\nSelected matcher configuration:\n{pformat(matcher_conf)}")
print("\n")

features = extract_features.main(feature_conf, images, outputs)

pairs_from_covisibility.main(sift_sfm, sfm_pairs, num_matched=args.num_covis)
sfm_matches = match_features.main(matcher_conf, sfm_pairs, feature_conf["output"], outputs)

triangulation.main(reference_sfm, sift_sfm, images, sfm_pairs, features, sfm_matches, colmap_path="colmap")

global_descriptors = extract_features.main(retrieval_conf, images, outputs)
pairs_from_retrieval.main(global_descriptors, loc_pairs, args.num_loc, query_prefix="query", db_model=reference_sfm)
loc_matches = match_features.main(matcher_conf, loc_pairs, feature_conf["output"], outputs)

# not required with SuperPoint+SuperGlue
localize_sfm.main(reference_sfm, dataset/"queries/*_time_queries_with_intrinsics.txt", loc_pairs, features, loc_matches, results, covisibility_clustering=False)
