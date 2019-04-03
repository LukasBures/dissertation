#!/usr/bin/env python

import pickle


def save_kp(kps, path):
    pickle_out = open(path, "wb")
    pickle.dump(kps, pickle_out)
    pickle_out.close()


def save_desc(descs, path):
    pickle_out = open(path, "wb")
    pickle.dump(descs, pickle_out)
    pickle_out.close()
