#!/usr/bin/env python
import time
from datetime import timedelta
import cv2
import myutils
import multiprocessing as mp
import numpy as np
from pathlib import Path


root_folder = "/home/lukas/PycharmProjects/Dissertation/_my/datasets/specom2020/"
summer_original_spring_GAN = root_folder + "summer_original-spring_GAN.txt"
summer_original_spring_original = root_folder + "summer_original-spring_original.txt"
summer_original_fall_GAN = root_folder + "summer_original-fall_GAN.txt"
summer_original_fall_original = root_folder + "summer_original-fall_original.txt"
summer_original_winter_GAN = root_folder + "summer_original-winter_GAN.txt"
summer_original_winter_original = root_folder + "summer_original-winter_original.txt"

img_paths = [summer_original_spring_GAN, summer_original_spring_original,
             summer_original_fall_GAN, summer_original_fall_original,
             summer_original_winter_GAN, summer_original_winter_original]

out_root_folder = "/home/lukas/PycharmProjects/Dissertation/_my/datasets/results/specom2020/"
output_dirs = [out_root_folder + "dump_summer_original-spring_GAN",
               out_root_folder + "dump_summer_original-spring_original",
               out_root_folder + "dump_summer_original-fall_GAN",
               out_root_folder + "dump_summer_original-fall_original",
               out_root_folder + "dump_summer_original-winter_GAN",
               out_root_folder + "dump_summer_original-winter_original"]

methods = ["surf", "sift", "akaze"]


def load_pairs(path):
    with open(path, 'r') as f:
        pairs = [l.split() for l in f.readlines()]
    return pairs


def worker(data):
    start_time = time.monotonic()
    method = data[0]
    file_path = data[1]
    output_dir = data[2] + "_" + method

    # Create the output directories if they do not exist already.
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    if method == "surf":
        detector = cv2.xfeatures2d.SURF_create()
        matcher = cv2.cuda_DescriptorMatcher.createBFMatcher(cv2.NORM_L2)
    elif method == "sift":
        detector = cv2.xfeatures2d.SIFT_create()
        matcher = cv2.cuda_DescriptorMatcher.createBFMatcher(cv2.NORM_L2)
    elif method == "akaze":
        detector = cv2.AKAZE_create()
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING)

    if not detector:
         print("unknown method: method {0}, exiting ...".format(method))
    else:
        print("starting: method {0}, file {1}".format(method, file_path))

        pairs = load_pairs(file_path)
        for i, pair in enumerate(pairs):
            name0, name1 = pair[:2]
            stem0, stem1 = Path(name0).stem, Path(name1).stem
            matches_path = str(output_dir) + '/{}_{}_matches.npz'.format(stem0, stem1)

            # chache
            if not Path(matches_path).exists():
                gray0 = cv2.imread(pair[0], 0)
                gray1 = cv2.imread(pair[1], 0)

                kps0, descs0 = detector.detectAndCompute(gray0, None)
                kps1, descs1 = detector.detectAndCompute(gray1, None)

                if method == "surf" or method == "sift":
                    cuda_descs0 = cv2.cuda_GpuMat()
                    cuda_descs1 = cv2.cuda_GpuMat()

                    np_descs0 = np.array(descs0)
                    np_descs1 = np.array(descs1)

                    cuda_descs0.upload(np_descs0)
                    cuda_descs1.upload(np_descs1)

                    good_matches = []
                    if descs0 is not None and descs1 is not None:
                        cuda_matches = matcher.knnMatch(cuda_descs0, cuda_descs1, 2)
                        for m, n in cuda_matches:
                            if m.distance < 0.7 * n.distance:
                                good_matches.append(m)

                elif method == "akaze":
                    good_matches = []
                    if descs0 is not None and descs1 is not None:
                        matches = matcher.knnMatch(np.array(descs0), np.array(descs1), 2)
                        if len(matches[0]) == 2:
                            for m, n in matches:
                                if m.distance < 0.7 * n.distance:
                                    good_matches.append(m)

                # Write the matches to disk.
                kps0_out = []
                kps1_out = []
                for kp in kps0:
                    kps0_out.append(kp.pt)
                for kp in kps1:
                    kps1_out.append(kp.pt)
                kps0_out = np.array(kps0_out)
                kps1_out = np.array(kps1_out)

                matches = np.full(len(kps0_out), -1)
                conf = np.full(len(kps0_out), 0.0)

                for match in good_matches:
                    matches[match.queryIdx] = match.trainIdx
                    conf[match.queryIdx] = match.distance

                out_matches = {'keypoints0': kps0_out, 'keypoints1': kps1_out, 'matches': matches, 'match_confidence': conf}
                np.savez(str(matches_path), **out_matches)

                end_time = time.monotonic()
                print("pool {} >> {} - {}/{}, time: {}".format(mp.current_process().name, method, i, len(pairs), timedelta(seconds=end_time - start_time)))

            
def generate_combinations(methods, img_paths, output_dirs):
    combinations = []
    for method in methods:
        for img_path, output_dir in zip(img_paths, output_dirs):
            combinations.append([method, img_path, output_dir])
    return combinations


if __name__ == '__main__':
    # combinations = generate_combinations(methods, img_paths, output_dirs)
    combinations = []
    combinations.append(["sift", summer_original_fall_GAN, output_dirs[2]])
    combinations.append(["akaze", summer_original_spring_GAN, output_dirs[0]])
    combinations.append(["akaze", summer_original_winter_GAN, output_dirs[4]])

    TEST = False

    if TEST:
        worker(combinations[2])
    else:
        pool = mp.Pool()
        pool.map(worker, combinations)