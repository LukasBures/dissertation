#!/usr/bin/env python

import multiprocessing as mp
import time

import cv2
import load_data

season_names = ["spring", "summer", "fall", "winter"]
methods = ["orb", "brisk", "surf", "sift", "kaze", "akaze"]
source_folder = "../data/results/get_kp_desc"
destination_folder = "../data/results/match_desc"


def worker(data):
    start_time = time.monotonic()
    method = data[0]
    from_season = data[1]
    to_seasons = data[2]

    detector = []
    if method == "surf" or method == "sift":
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        matcher = cv2.FlannBasedMatcher(index_params, search_params)
    elif method == "kaze" or method == "akaze":
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    elif method == "orb":
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    elif method == "brisk":
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    load_data.load_all_descs(source_folder, method)

    # matches = matcher.knnMatch(descs1, descs2, k=2)
    #
    #
    #
    #
    #
    # if not detector:
    #     print("{0} unknown method: method {1}, season {2}, exiting ...".format(mp.current_process().name, method, season))
    # else:
    #     print("{0} starting: method {1}, season {2}".format(mp.current_process().name, method, season))
    #     cap = cv2.VideoCapture(file_path)
    #     all_kps = []
    #     all_descs = []
    #     frame_idx = 1
    #     frame_offset = 50
    #     step = 250
    #     total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    #     used_frames = []
    #
    #     while cap.isOpened():
    #         current_frame = ((frame_idx - 1) * step) + frame_offset
    #         if current_frame > total_frames:
    #             break
    #         else:
    #             cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    #             ret, frame = cap.read()
    #             cv2.imshow(mp.current_process().name, frame)
    #             cv2.waitKey(1)
    #             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #             kps, descs = detector.detectAndCompute(gray, None)
    #             all_kps.append(kps)
    #             all_descs.append(descs)
    #             used_frames.append(current_frame)
    #             end_time = time.monotonic()
    #             if frame_idx % 1000 == 0:
    #                 save_data.save_desc(all_descs, "{0}/{1}/{2}_descs_{3}.pickle".format(root_folder, season, method, frame_idx))
    #                 save_data.save_kp(all_kps, "{0}/{1}/{2}_kps_{3}.pickle".format(root_folder, season, method, frame_idx))
    #                 all_kps = []
    #                 all_descs = []
    #             elif (frame_idx - frame_offset) % 100 == 0:
    #                 print("{0} update: method {1}, season {2}, frame {3}, time {4}".format(mp.current_process().name, method, season, frame_idx, timedelta(seconds=end_time - start_time)))
    #         frame_idx += 1
    #
    #     save_data.save_desc(all_descs, "{0}/{1}/{2}_descs_{3}.pickle".format(root_folder, season, method, frame_idx))
    #     save_data.save_kp(all_kps, "{0}/{1}/{2}_kps_{3}.pickle".format(root_folder, season, method, frame_idx))
    #     save_data.save_frame_numbers(used_frames, "{0}/{1}/{2}_frames_{3}.pickle".format(root_folder, season, method, frame_idx))
    #
    #     end_time = time.monotonic()
    #     print("{0} update: method {1}, season {2}, frame {3}, time {4}".format(mp.current_process().name, method, season, frame_idx, timedelta(seconds=end_time - start_time)))
    #


def generate_combinations(methods, seasons):
    combinations = []
    for method in methods:
        for from_season in seasons:
            to_seasons = []
            for to_season in seasons:
                if from_season is not to_season:
                    to_seasons.append(to_season)
            combinations.append([method, from_season, to_seasons])
    return combinations


if __name__ == "__main__":
    combinations = generate_combinations(methods, season_names)
    pool = mp.Pool(processes=1)
    pool.map(worker, combinations)
