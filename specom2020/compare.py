#!/usr/bin/env python
import multiprocessing as mp
import numpy as np
import time
from datetime import timedelta
import cv2
import myutils

seasons = ["spring", "fall", "winter"]
# methods = ["orb", "brisk", "surf", "sift", "kaze", "akaze"]
methods = ["surf", "sift", "akaze"]
Hs_out_folder = "../datasets/results/specom2020/homographies/"


def load_data_to_compare(from_season, method, to_season="summer"):
    from_season_path = "../datasets/results/specom2020/" + from_season + "/" + method + "_kp_desc_3578.pickle"
    from_season_path_frames = "../datasets/results/specom2020/" + from_season + "/" + method + "_frames_3578.pickle"
    from_season_kps, from_season_descs, from_season_frames = myutils.load_data.load_kp_desc(from_season_path, from_season_path_frames)

    to_season_path = "../datasets/results/specom2020/" + to_season + "/" + method + "_kp_desc_3578.pickle"
    to_season_path_frames = "../datasets/results/specom2020/" + to_season + "/" + method + "_frames_3578.pickle"
    to_season_kps, to_season_descs, to_season_frames = myutils.load_data.load_kp_desc(to_season_path, to_season_path_frames)

    return from_season_kps, from_season_descs, from_season_frames, to_season_kps, to_season_descs, to_season_frames


def load_data_to_compare_GAN(from_season, method, to_season="summer"):
    from_season_path = "../datasets/results/specom2020/GAN/" + from_season + "_to_summer_GAN_" + method + "_kp_desc_3578.pickle"
    from_season_path_frames = "../datasets/results/specom2020/GAN/" + from_season + "_to_summer_GAN_" + method + "_frames_3578.pickle"
    from_season_kps, from_season_descs, from_season_frames = myutils.load_data.load_kp_desc(from_season_path, from_season_path_frames)

    # to_season_path = "../datasets/results/specom2020/" + to_season + "/" + method + "_kp_desc_3578.pickle"
    # to_season_path_frames = "../datasets/results/specom2020/" + to_season + "/" + method + "_frames_3578.pickle"
    # to_season_kps, to_season_descs, to_season_frames = myutils.load_data.load_kp_desc(to_season_path, to_season_path_frames)

    # return from_season_kps, from_season_descs, from_season_frames, to_season_kps, to_season_descs, to_season_frames
    return from_season_kps, from_season_descs, from_season_frames


def calculate_homographies(season, method, from_kps_all, from_descs_all, from_frames, to_kps_all, to_descs_all, to_frames, GAN=False):
    if method == "surf" or method == "sift":
        matcher = cv2.cuda_DescriptorMatcher.createBFMatcher(cv2.NORM_L2)
    elif method == "kaze" or method == "akaze":
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    elif method == "brisk":
        matcher = cv2.cuda_DescriptorMatcher.createBFMatcher(cv2.NORM_HAMMING)
    elif method == "orb":
        matcher = cv2.cuda_DescriptorMatcher.createBFMatcher(cv2.NORM_HAMMING)
        good_match_percent = 0.15
    else:
        assert print(mp.current_process().name + ": unknown method: " + method)
        return 1

    # skip factor - skip first 16 frames because in summer there is not a video - just dark blank screen
    sk = 17
    min_match_count = 10
    min_kp_count = 20
    H_all = []

    from_kps_all = from_kps_all[sk:]
    from_descs_all = from_descs_all[sk:]
    from_frames = from_frames[sk:]
    to_kps_all = to_kps_all[sk:]
    to_descs_all = to_descs_all[sk:]
    to_frames = to_frames[sk:]

    for fr, (from_kps, from_descs, from_frame) in enumerate(zip(from_kps_all, from_descs_all, from_frames)):
        H_tmp = []
        # if fr == 1:
        #     break

        if not method == "akaze":
            cuda_from_descs = cv2.cuda_GpuMat()
            # np_from_descs = np.vstack(from_descs)
            np_from_descs = np.array(from_descs)
            cuda_from_descs.upload(np_from_descs)
        for to_kps, to_descs, to_frame in zip(to_kps_all, to_descs_all, to_frames):
            if len(from_descs) >= min_kp_count and len(to_descs) >= min_kp_count:
                if not method == "akaze":
                    cuda_to_descs = cv2.cuda_GpuMat()
                    # np_to_descs = np.vstack(to_descs)
                    np_to_descs = np.array(to_descs)
                    cuda_to_descs.upload(np_to_descs)
                if method == "surf" or method == "sift":
                    cuda_matches = matcher.knnMatch(cuda_from_descs, cuda_to_descs, 2)
                    # apply Lowe ratio
                    good = []
                    for m, n in cuda_matches:
                        if m.distance < 0.7 * n.distance:
                            good.append(m)
                elif method == "akaze":
                    matches = matcher.knnMatch(np.array(from_descs), np.array(to_descs), 2)
                    good = []
                    for m, n in matches:
                        if m.distance < 0.9 * n.distance:
                            good.append(m)
                elif method == "orb":
                    cuda_matches = matcher.match(cuda_from_descs, cuda_to_descs)
                    # Sort them in the order of their distance.
                    matches = sorted(cuda_matches, key=lambda x: x.distance)
                    good = matches[:int(len(matches) * good_match_percent)]
                else:
                    good = matcher.match(cuda_from_descs, cuda_to_descs)

                if len(good) >= min_match_count:
                    src_pts = np.float32([from_kps[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                    dst_pts = np.float32([to_kps[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
                    H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)
                else:
                    H = -2
            else:
                H = -1
            H_tmp.append([from_frame, to_frame, H])
        H_all.append(H_tmp)
        if GAN:
            print(mp.current_process().name + ": GAN calculating homographies | " + season + " + " + method + " -> " + str(fr) + "/" + str(len(from_frames) - sk))
        else:
            print(mp.current_process().name + ": calculating homographies | " + season + " + " + method + " -> " + str(fr) + "/" + str(len(from_frames) - sk))

    return H_all


def worker(data):
    season = data[0]
    method = data[1]

    # load data
    from_kps, from_descs, from_frames, to_kps, to_descs, to_frames = load_data_to_compare(season, method)
    print(mp.current_process().name + ": loaded -> " + season + " + " + method)
    from_gan_kps, from_gan_descs, from_gan_frames = load_data_to_compare_GAN(season, method)
    print(mp.current_process().name + ": GAN loaded -> " + season + " + " + method)

    # calculate homographies and save
    Hs = calculate_homographies(season, method, from_kps, from_descs, from_frames, to_kps, to_descs, to_frames)
    print(mp.current_process().name + ": homographies calculated -> " + season + " + " + method)
    myutils.save_data.save(Hs, Hs_out_folder + "Hs_" + method + "_from_" + season + "_to_summer.pickle")
    print(mp.current_process().name + ": data saved -> " + season + " + " + method)

    Hs_GAN = calculate_homographies(season, method, from_gan_kps, from_gan_descs, from_gan_frames, to_kps, to_descs, to_frames, GAN=True)
    print(mp.current_process().name + ": GAN homographies calculated -> " + season + " + " + method)
    myutils.save_data.save(Hs_GAN, Hs_out_folder + "Hs_GAN_" + method + "_transformed_from_" + season + "_to_summer-summer.pickle")
    print(mp.current_process().name + ": GAN data saved -> " + season + " + " + method)

    return 0


def generate_combinations(seasons, methods):
    combo = []
    for season in seasons:
        for method in methods:
            combo.append([season, method])
    return combo


if __name__ == '__main__':
    combinations = generate_combinations(seasons, methods)

    TEST = False
    if TEST:
        # for combination in combinations:
        worker(["spring", "sift"])
        worker(["spring", "surf"])
        worker(["spring", "akaze"])
    else:
        pool = mp.Pool()
        pool.map(worker, combinations)


