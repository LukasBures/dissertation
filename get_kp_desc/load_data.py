#!/usr/bin/env python

import pickle

path = "/home/lukas/PycharmProjects/Dissertation/data/results/get_kp_desc/spring/surf_descs_10.pickle"

output = open(path, "rb")
data = pickle.load(output)
output.close()


print(len(data))

