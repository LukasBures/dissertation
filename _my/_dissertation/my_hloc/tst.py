import torch
import sys
from subprocess import call
import h5py
import sys
import pickle
sys.path.append('/home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/')
import argparse
import torch


pth = "/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc/logs/aachen/test_top_superpoint_aachen-my_superglue_2020.12.12_14.58.41/results"

# has only db and query image names
# filename = pth + "/feats-superpoint-n4096-r1024.h5"

# filename = pth + "/feats-superpoint-n4096-r1024_matches-superglue_pairs-db-covis20.h5"
filename = "/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc/logs/aachen/extract_features_test/feats-superpoint-n2048-rmax1600.h5"

# filename = pth + "/feats-superpoint-n4096-r1024_matches-superglue_pairs-query-netvlad50.h5"


# with open('/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc/logs/aachen/segment_nvidia/day/segment_nvidia.pkl', 'rb') as file:
#     klk = pickle.load(file)
#
# print("gg")

with h5py.File(filename, "r") as f:
    for key in f.keys():
        print(key)  # Names of the groups in HDF5 file.

    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = f[a_group_key]
    # data2 = f[a_group_key]["matches0"]
    # data3 = f[a_group_key]["matching_scores0"]
    print("a")

#
# with open(pth + '/Aachen_hloc_superpoint+superglue_netvlad50.txt_logs.pkl', 'rb') as file:
#     arr = pickle.load(file)


print("a")