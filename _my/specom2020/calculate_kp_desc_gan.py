#!/usr/bin/env python3
import numpy as np
import pylib as py
import tensorflow as tf
import tf2lib as tl
import module
from imlib import dtype

import multiprocessing as mp
import time
from datetime import timedelta
import cv2
import myutils

spring_video_path = "/data1/nordlandsbanen.spring.sync.1920x1080.h264.nrk.mp4"
fall_video_path = "/data3/nordlandsbanen.fall.sync.1920x1080.h264.nrk.mp4"
winter_video_path = "/data4/nordlandsbanen.winter.sync.1920x1080.h264.nrk.mp4"
seasons_video_paths = [spring_video_path, fall_video_path, winter_video_path]
season_names = ["spring", "fall", "winter"]
methods = ["orb", "brisk", "surf", "sift", "kaze", "akaze"]
root_folder = "../datasets/results/specom2020"


def worker(data):
    start_time = time.monotonic()
    method = data[0]
    season = data[1]
    file_path = data[2]

    detector = []
    if method == "surf":
        detector = cv2.xfeatures2d.SURF_create()
    elif method == "sift":
        detector = cv2.xfeatures2d.SIFT_create()
    elif method == "kaze":
        detector = cv2.KAZE_create()
    elif method == "akaze":
        detector = cv2.AKAZE_create()
    elif method == "orb":
        detector = cv2.ORB_create()
    elif method == "brisk":
        detector = cv2.BRISK_create()

    if not detector:
        # print("{0} unknown method: method {1}, season {2}, exiting ...".format(mp.current_process().name, method, season))
        print("unknown method: method {0}, season {1}, exiting ...".format(method, season))
    else:
        crop_size = 360
        experiment_dir = "../../CycleGAN/output/" + season + "2summer_nordlandsbanen_noTunnels"

        # model
        G_A2B = module.ResnetGenerator(input_shape=(crop_size, crop_size, 3))
        G_B2A = module.ResnetGenerator(input_shape=(crop_size, crop_size, 3))

        # resotre
        tl.Checkpoint(dict(G_A2B=G_A2B, G_B2A=G_B2A), py.join(experiment_dir, 'checkpoints')).restore()


        @tf.function
        def sample_A2B(A):
            A2B = G_A2B(A, training=False)
            A2B2A = G_B2A(A2B, training=False)
            return A2B, A2B2A


        @tf.function
        def sample_B2A(B):
            B2A = G_B2A(B, training=False)
            B2A2B = G_A2B(B2A, training=False)
            return B2A, B2A2B

        print("starting: season {0}".format(season))
        cap = cv2.VideoCapture(file_path)
        all_kp_desc = []

        frame_idx = 1
        frame_offset = 50
        step = 250
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        current_frame = ((frame_idx - 1) * step) + frame_offset
        used_frames = []

        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        img_sz = 1024
        w_from = int((w / 2) - (img_sz / 2))
        w_to = int((w / 2) + (img_sz / 2))
        h_from = int((h / 2) - (img_sz / 2))
        h_to = int((h / 2) + (img_sz / 2))

        while True:
            current_frame = ((frame_idx - 1) * step) + frame_offset
            if current_frame > total_frames:
                print("BREAK: Total frames: " + str(total_frames) + ", current frame = " + str(current_frame))
                break
            else:
                cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
                _, A_cap = cap.read()
                center_frame = A_cap[h_from:h_to, w_from:w_to]
                A_resized = cv2.resize(center_frame, dsize=(crop_size, crop_size), interpolation=cv2.INTER_CUBIC)
                A = np.expand_dims(np.asarray(A_resized).astype(np.float32), axis=0)

                A2B, _ = sample_A2B(A)
                img = dtype.im2cv(A2B.numpy()).squeeze(axis=0)

                # cv2.imshow("a, img", img)
                # cv2.waitKey(1)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                kps, descs = detector.detectAndCompute(gray, None)

                data_kp_desc = []
                if len(kps) > 0:
                    for kp, desc in zip(kps, descs):
                        data_kp_desc.append([kp.pt, kp.size, kp.angle, kp.response, kp.octave, kp.class_id, desc])
                else:
                    data_kp_desc.append([])

                all_kp_desc.append(data_kp_desc)
                used_frames.append(current_frame)

                end_time = time.monotonic()
    
                print("{0} update: method {1}, season {2}, frame {3} - {4}/{5}, time {6}".format("-", method, season, frame_idx, current_frame, total_frames, timedelta(seconds=end_time - start_time)))
                frame_idx += 1

        myutils.save_kp_desc(all_kp_desc, "{0}/{1}/GAN_{2}_kp_desc_{3}.pickle".format(root_folder, season, method, frame_idx))
        myutils.save_frame_numbers(used_frames, "{0}/{1}/GAN_{2}_frames_{3}.pickle".format(root_folder, season, method, frame_idx))

        end_time = time.monotonic()
        print("{0} update: method {1}, season {2}, frame {3} - {4}/{5}, time {6}".format("", method, season, frame_idx, current_frame, total_frames, timedelta(seconds=end_time - start_time)))


def generate_combinations(methods, seasons, video_paths):
    combinations = []
    for method in methods:
        for i, season in enumerate(seasons):
            combinations.append([method, season, video_paths[i]])
    return combinations


if __name__ == '__main__':
    combinations = generate_combinations(methods, season_names, seasons_video_paths)
    for combination in combinations:
        worker(combination)