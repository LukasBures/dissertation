from pathlib import Path

import h5py
from hloc import triangulation

# fl = "/data512/dissertation_results/4Seasons-2022.02.02_09.14.49/results_validation/feats-superpoint-n1024-r1024.h5"
new_h5_file_path = (
    "/data512/dissertation_results/4Seasons-2022.02.06_16.06.02/results_validation/feats-superpoint-n1024-r1024.h5"
)
segmentations = "/data512/dissertation_results/4Seasons-2022.02.06_16.06.02/results_validation/s65_d100_feats-superpoint-n1024-r1024.h5"
nnn = "/data512/dissertation_results/aachen-2022.02.05_16.35.22/results/global-feats-netvlad.h5"
# 1586247632370009088 - does not exist
# with h5py.File(new_h5_file_path, "w") as destination_file:
#     cam0 = destination_file.create_group("cam0")
#     grp = cam0.create_group("image_sasa")
#     grp.create_dataset("keypoints", data=123)

reference = "/data512/dissertation_results/4Seasons/segment_nvidia_4Seasons_reference_v01.h5"
validation = "/data512/dissertation_results/4Seasons/segment_nvidia_4Seasons_validation_v01.h5"

with h5py.File(str(reference), "r") as ref:
    with h5py.File(str(validation), "r") as val:
        print(val.keys())
        print(ref.keys())
        print("!")



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
