from pathlib import Path
import argparse
import sys
import os

from configs import feature_configs, matcher_configs

sys.path.append("/home/lukas/PycharmProjects/dissertation/Hierarchical-Localization")
try:
    user_paths = os.environ["PYTHONPATH"].split(os.pathsep)
except KeyError:
    pass
else:
    print(f"__PYTHONPATH: {user_paths}")

from hloc import extract_features, match_features, pairs_from_poses, triangulation
from utils2 import get_timestamps, delete_unused_images
from utils2 import build_empty_colmap_model

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=Path, default='datasets/4Seasons', help='Path to the dataset, default: %(default)s')
parser.add_argument('--outputs', type=Path, default='outputs/4Seasons', help='Path to the output directory, default: %(default)s')
parser.add_argument("--num_ref", type=int, default=20, help="Number of image pairs for SfM, default: %(default)s")
parser.add_argument("--feature_conf", type=str, help="Feature config")
parser.add_argument("--matcher_conf", type=str, help="Matcher config")
args = parser.parse_args()

ref_dir = args.dataset / 'reference'
assert ref_dir.exists(), f'{ref_dir} does not exist'
ref_images = ref_dir / 'undistorted_images'

output_dir: Path = args.outputs
output_dir.mkdir(exist_ok=True, parents=True)
ref_sfm_empty: Path = output_dir / 'sfm_reference_empty'
ref_sfm: Path = output_dir / 'sfm_superpoint+superglue'

num_ref_pairs: int = args.num_ref
ref_pairs: Path = output_dir / f'pairs-db-dist{num_ref_pairs}.txt'


feature_conf: dict = feature_configs[args.feature_conf]
matcher_conf: dict = matcher_configs[args.matcher_conf]

# Only reference images that have a pose are used in the pipeline.
# To save time in feature extraction, we delete unsused images.
delete_unused_images(ref_images, get_timestamps(ref_dir / 'poses.txt', 0))

# Build an empty COLMAP model containing only camera and images
# from the provided poses and intrinsics.
build_empty_colmap_model(ref_dir, ref_sfm_empty)

# Match reference images that are spatially close.
pairs_from_poses.main(ref_sfm_empty, ref_pairs, num_ref_pairs)

# Extract, match, and triangulate the reference SfM model.
ffile = extract_features.main(feature_conf, ref_images, output_dir)
mfile = match_features.main(matcher_conf, ref_pairs, feature_conf['output'], output_dir)
triangulation.main(ref_sfm, ref_sfm_empty, ref_images, ref_pairs, ffile, mfile)
