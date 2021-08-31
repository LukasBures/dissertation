# check parameters
# python -m runx.runx scripts/aachen.yml -i -n

# run
# python -m runx.runx scripts/aachen.yml -i

import sys
sys.path.append('/home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/')
import argparse
import torch
import subprocess
from pathlib import Path
from pprint import pformat
from hloc import extract_features, match_features, pairs_from_covisibility
from hloc import colmap_from_nvm, triangulation, localize_sfm
from runx import logx
# from hloc import visualization

# Pipeline for outdoor day-night visual localization

# Setup
# Here we declare the paths to the dataset, the reconstruction and localization outputs,
# and we choose the feature extractor and the matcher. You only need to download the
# [Aachen Day-Night dataset](https://www.visuallocalization.net/datasets/) and
# put it in `datasets/aachen/`, or change the path.

# Argument Parser
parser = argparse.ArgumentParser(description='KP Filtration')
parser.add_argument('--experiment_name', type=str, default='new_experiment')
parser.add_argument('--dataset', type=str, default='/home/lukas/PycharmProjects/Dissertation/datasets/aachen/')
parser.add_argument('--images', type=str,
                    default='/home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/')
parser.add_argument('--pairs', type=str,
                    default='/home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/')
parser.add_argument('--outputs', type=str, default='outputs/aachen/')  # where everything will be saved
parser.add_argument('--feature_conf', type=str, default='superpoint_aachen')
parser.add_argument('--matcher_conf', type=str, default='superglue')
parser.add_argument('--local_rank', default=0, type=int, help='parameter used by apex library')
parser.add_argument('--global_rank', default=0, type=int, help='parameter used by apex library')
# parser.add_argument('--gpu_number', type=int, default=0)
parser.add_argument('--apex', action='store_true', default=False, help='Use Nvidia Apex Distributed Data Parallel')
parser.add_argument('--result_dir', type=str, default='logs', help='where to write log output')
parser.add_argument('--gpu_number', type=int, default=0, help='active GPU')

args = parser.parse_args()
dataset = Path(args.dataset)
pairs = Path(args.pairs)
outputs = Path(args.outputs) 
images = args.images

assert args.result_dir is not None, 'need to define result_dir arg'
logx.logxx.initialize(logdir=args.result_dir,
                      tensorboard=True, hparams=vars(args),
                      global_rank=args.global_rank)

if args.apex:
    logx.logxx.msg(f'Global Rank: {args.global_rank} Local Rank: {args.local_rank}')
    torch.cuda.set_device(args.local_rank)
    torch.distributed.init_process_group(backend='nccl', init_method='env://')

# Test package versions
logx.logxx.msg(f'__Python VERSION: {sys.version}')  # 3.6.12 (default, Aug 18 2020, 02:08:22)
logx.logxx.msg(f'__pyTorch VERSION: {torch.__version__}')  # 1.7.0+cu101
tmp_output = subprocess.check_output(["nvcc", "--version"])
tmp_output = tmp_output.decode("utf-8")
logx.logxx.msg(f'__CUDA VERSION: \n{tmp_output.rstrip()}')  # release 10.1, V10.1.243
logx.logxx.msg(f'__CUDNN VERSION: {torch.backends.cudnn.version()}')  # 7603
logx.logxx.msg(f'__Number CUDA Devices: {torch.cuda.device_count()}')
tmp_output = subprocess.check_output(["nvidia-smi", "--format=csv", "--query-gpu=index,name,driver_version,memory.total,memory.used,memory.free"])
tmp_output = tmp_output.decode("utf-8")
logx.logxx.msg(f'__CUDA Devices: \n{tmp_output.rstrip()}')
logx.logxx.msg(f'__Available Devices: {torch.cuda.device_count()}')
logx.logxx.msg(f'__Current CUDA Device: {torch.cuda.get_device_name(torch.cuda.current_device())}')
torch.cuda.set_device(args.gpu_number)
logx.logxx.msg(f'__CUDA Device Changed To: {torch.cuda.get_device_name(torch.cuda.current_device())}')

# Config
sfm_pairs = pairs / 'pairs-db-covis20.txt'  # top 20 most covisible in SIFT model
loc_pairs = pairs / 'pairs-query-netvlad50.txt'  # top 50 retrieved by NetVLAD
reference_sfm = outputs / 'sfm_superpoint+superglue'  # the SfM model we will build
results = outputs / 'Aachen_hloc_superpoint+superglue_netvlad50.txt'  # the result file

# List the standard configurations available
print(f'Configs for feature extractors:\n{pformat(extract_features.confs)}')
print(f'Configs for feature matchers:\n{pformat(match_features.confs)}')

# Pick one of the configurations for extraction and matching, you can also simply write your own here!
feature_conf = extract_features.confs[args.feature_conf]
matcher_conf = match_features.confs[args.matcher_conf]

# Extract local features for database and query images
# The function returns the path of the file in which all the extracted features are stored.
feature_path = extract_features.main(feature_conf, images, outputs)




# ---------------------------------------------------------------------------------------------------------------------
# MODEL
# ---------------------------------------------------------------------------------------------------------------------
# Generate pairs for the SfM reconstruction
# Instead of matching all database images exhaustively, we exploit the existing SIFT model to find which image pairs
# are the most covisible. We first convert the SIFT model from the NVM to the COLMAP format, and then do a covisiblity
# search, selecting the top 20 most covisibile neighbors for each image.
# colmap_from_nvm.main(
#     dataset / '3D-models/aachen_cvpr2018_db.nvm',
#     dataset / '3D-models/database_intrinsics.txt',
#     dataset / 'aachen.db',
#     outputs / 'sfm_sift')

# pairs_from_covisibility.main(
#     outputs / 'sfm_sift', sfm_pairs, num_matched=20)

# Match the database images
# The function returns the path of the file in which all the computed matches are stored.
# sfm_match_path = match_features.main(matcher_conf, sfm_pairs, feature_conf['output'], outputs)

# Triangulate a new SfM model from the given poses
# We triangulate the sparse 3D pointcloud given the matches and the reference poses stored in the SIFT COLMAP model.
# triangulation.main(
#     reference_sfm,
#     outputs / 'sfm_sift',
#     images,
#     sfm_pairs,
#     feature_path,
#     sfm_match_path,
#     colmap_path='colmap')  # change if COLMAP is not in your PATH


# ---------------------------------------------------------------------------------------------------------------------
# QUERY
# ---------------------------------------------------------------------------------------------------------------------
# Match the query images
# Here we assume that the localization pairs are already computed using image retrieval (NetVLAD).
# To generate new pairs from your own global descriptors, have a look at `hloc/pairs_from_retrieval.py`.
# These pairs are also used for the localization - see below.
loc_match_path = match_features.main(matcher_conf, loc_pairs, feature_conf['output'], outputs)

# Localize
# Perform hierarchical localization using the precomputed retrieval and matches. The file
# `Aachen_hloc_superpoint+superglue_netvlad50.txt` will contain the estimated query poses. Have a look at
# `Aachen_hloc_superpoint+superglue_netvlad50.txt_logs.pkl` to analyze some statistics and find failure cases.
localize_sfm.main(
    reference_sfm / 'model',
    dataset / 'queries/*_time_queries_with_intrinsics.txt',
    loc_pairs,
    feature_path,
    loc_match_path,
    results,
    covisibility_clustering=False)  # not required with SuperPoint+SuperGlue

# # Visualizing the SfM model
# # We visualize some of the database images with their detected keypoints.
# # Color the keypoints by track length: red keypoints are observed many times, blue keypoints few.
# visualization.visualize_sfm_2d(reference_sfm / 'model', images, n=1, color_by='track_length')
#
# # Color the keypoints by visibility: blue if sucessfully triangulated, red if never matched.
# visualization.visualize_sfm_2d(reference_sfm / 'model', images, n=1, color_by='visibility')
#
# # Color the keypoints by triangulated depth: red keypoints are far away, blue keypoints are closer.
# visualization.visualize_sfm_2d(reference_sfm / 'model', images, n=1, color_by='depth')
#
# # Visualizing the localization
# # We parse the localization logs and for each query image plot matches and inliers with a few database images.
# visualization.visualize_loc(
#     results, images, reference_sfm / 'model', n=1, top_k_db=1, prefix='query/night', seed=2)
