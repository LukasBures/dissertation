#!/usr/bin/env python

import pickle
import numpy as np
import re
import os
import multiprocessing as mp
# path = "/home/lukas/PycharmProjects/Dissertation/data/results/get_kp_desc/spring/surf_descs_10.pickle"
path = "/home/lukas/PycharmProjects/Dissertation/data/results/get_kp_desc/spring/akaze_kps_3578.pickle"


def load_all_descs(path, method):
    batches = ["1000", "2000", "3000", "3578"]
    # batches = ["3578"]
    data = {"spring": [], "summer": [], "fall": [], "winter": []}

    for d in data:
        for b in batches:
            full_path = "{0}/{1}/{2}_descs_{3}.pickle".format(path, d, method, b)
            output = open(full_path, "rb")
            data[d].append(pickle.load(output))
            output.close()
        data[d] = np.concatenate(data[d], axis=0)

    return data


output = open(path, "rb")
data = pickle.load(output)
output.close()

print(data)