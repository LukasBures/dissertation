from pathlib import Path

import h5py
from hloc import triangulation

#
#
# root = "/data512/dissertation_results/aachen-2021.12.13_13.47.06/results/"
#
# original = root + "feats-superpoint-n4096-r1024.h5"
#
# new = root + "new_feats-superpoint-n4096-r1024.h5"
#
#
# with h5py.File(str(original), 'r') as fo:
#     with h5py.File(str(new), 'r') as fn:
#         print(fo.keys())
#         print(fn.keys())
#
#
# print("done")
# colmap matches_importer --database_path results/sfm_superpoint+superglue/database.db --match_list_path results/pairs-db-covis20.txt --match_type pairs --SiftMatching.use_gpu 0 --SiftMatching.max_num_trials 20000 --SiftMatching.min_inlier_ratio 0.1


root = "/data512/dissertation_results/aachen-2021.12.13_17.32.10/"
reference_sfm = Path(root + "results/sfm_superpoint+superglue")
sift_sfm = Path(root + "results/sfm_sift")
images = Path("/data512/datasets/aachen/images/images_upright/")
sfm_pairs = Path("/data512/dissertation_results/aachen-2021.12.13_17.32.10/results/pairs-db-covis20.txt")
new_features_pth = Path(
    "/data512/dissertation_results/aachen-2021.12.13_17.32.10/results/new_feats-superpoint-n4096-r1024.h5"
)
sfm_matches = Path(
    "/data512/dissertation_results/aachen-2021.12.13_17.32.10/results/feats-superpoint-n4096-r1024_matches-superglue_pairs-db-covis20.h5"
)

# with h5py.File(str(sfm_matches), 'r') as fo:
#    print(fo.keys())

triangulation.main(
    reference_sfm,
    sift_sfm,
    images,
    sfm_pairs,
    new_features_pth,
    sfm_matches,
    colmap_path="colmap",
    skip_geometric_verification=True,
    verbose=False,
)

print("ALL DONE")
