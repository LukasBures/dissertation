import argparse
import subprocess
import sys
from pathlib import Path
from pprint import pformat
import os
import itertools
import h5py

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

outputs = Path("/data512/dissertation_results/aachen-2022.01.12_14.27.51/results")
sift_sfm = outputs / "sfm_sift"  # from which we extract the reference poses
reference_sfm = outputs / "sfm_superpoint+superglue"  # the SfM model we will build
dataset = Path("/data512/datasets/aachen/")
images = dataset / "images/images_upright/"
sfm_pairs = outputs / f"pairs-db-covis20.txt"  # top-k most covisible in SIFT model

all_features_pth = outputs / "feats-superpoint-n4096-r1024.h5"
pth, nm = os.path.split(os.path.abspath(all_features_pth))
new_features_pth = Path(os.path.join(pth, "new_" + nm))

sfm_matches = outputs / "feats-superpoint-n4096-r1024_matches-superglue_pairs-db-covis20.h5"


# colmap matches_importer --database_path /data512/dissertation_results/aachen-2021.12.14_18.04.18/results/sfm_superpoint+superglue/database.db --match_list_path /data512/dissertation_results/aachen-2021.12.14_18.04.18/results/pairs-db-covis20.txt --match_type pairs --SiftMatching.use_gpu 0 --SiftMatching.max_num_trials 20000 --SiftMatching.min_inlier_ratio 0.1

#with h5py.File(str(sfm_matches), 'r') as rrr:
#    print(rrr.keys())

# with h5py.File(str(all_features_pth), 'r') as all:
#    with h5py.File(str(new_features_pth), 'r') as new:
#        print(all.keys())
#        print(new.keys())



# retrieval_conf="netvlad"
# feature_conf="superpoint_fast"
# matcher_conf="superglue_fast"






# sfm_dir, reference_sfm_model, image_dir, pairs, features, matches,
triangulation.main(
    sfm_dir=reference_sfm,
    reference_model=sift_sfm,
    image_dir=images,
    pairs=sfm_pairs,
    features=new_features_pth,
    matches=sfm_matches,
    skip_geometric_verification=False,
    verbose=True
)




