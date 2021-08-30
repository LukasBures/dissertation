#!/usr/bin/env python3
import numpy as np
import pylib as py
import tensorflow as tf
import tf2lib as tl
import module
from imlib import dtype

import cv2
import glob
import os

from_folder = "/home/lukas/PycharmProjects/Dissertation/_my/datasets/nordlandsbanen_imgs/"
to_folder = "/home/lukas/PycharmProjects/Dissertation/_my/datasets/specom2020/"
seasons = ["spring", "summer", "fall", "winter"]
seasons_without_summer = ["spring", "fall", "winter"]
crop_size = 360


def resize_imgs():
    for season in seasons:
        os.chdir(from_folder + season)
        for file in glob.glob("*.jpg"):
            in_path = from_folder + season + "/" + file
            out_path = to_folder + season + "_original/" + file
            img = cv2.imread(in_path, cv2.IMREAD_COLOR)
            img_resized = cv2.resize(img, dsize=(crop_size, crop_size), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(out_path, img_resized)
            print(out_path)


def generate_gan(seasons):
    for season in seasons:
        experiment_dir = "/home/lukas/PycharmProjects/Dissertation/CycleGAN/output/" + season + "2summer_nordlandsbanen_noTunnels"
        G_A2B = module.ResnetGenerator(input_shape=(crop_size, crop_size, 3))
        tl.Checkpoint(dict(G_A2B=G_A2B), py.join(experiment_dir, 'checkpoints')).restore()

        @tf.function
        def sample_A2B(A):
            A2B = G_A2B(A, training=False)
            return A2B

        print("experiment dir: " + experiment_dir)
        os.chdir(to_folder + season + "_original")
        for file in glob.glob("*.jpg"):
            in_path = to_folder + season + "_original/" + file
            out_path = to_folder + season + "_GAN/" + file
            A = cv2.imread(in_path)
            A = np.expand_dims(np.asarray(A).astype(np.float32), axis=0)
            A2B = sample_A2B(A)
            img_out = dtype.im2cv(A2B.numpy()).squeeze(axis=0)
            cv2.imwrite(out_path, img_out)
            print(out_path)

# resize_imgs()
generate_gan(seasons_without_summer)
