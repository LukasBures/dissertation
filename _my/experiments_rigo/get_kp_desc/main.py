#!/usr/bin/env python

import multiprocessing as mp
import time
from datetime import timedelta

import cv2
import save_data

spring_video_path = "/data1/nordlandsbanen.spring.sync.1920x1080.h264.nrk.mp4"
summer_video_path = "/data2/nordlandsbanen.summer.sync.1920x1080.h264.nrk.mp4"
fall_video_path = "/data3/nordlandsbanen.fall.sync.1920x1080.h264.nrk.mp4"
winter_video_path = "/data4/nordlandsbanen.winter.sync.1920x1080.h264.nrk.mp4"
seasons_video_paths = [spring_video_path, summer_video_path, fall_video_path, winter_video_path]
season_names = ["spring", "summer", "fall", "winter"]
methods = ["orb", "brisk", "surf", "sift", "kaze", "akaze"]
root_folder = "../data/results/get_kp_desc"


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
        print(
            "{0} unknown method: method {1}, season {2}, exiting ...".format(mp.current_process().name, method, season)
        )
    else:
        print("{0} starting: method {1}, season {2}".format(mp.current_process().name, method, season))
        cap = cv2.VideoCapture(file_path)
        all_kps = []
        all_descs = []

        frame_idx = 1
        frame_offset = 50
        step = 250
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        current_frame = ((frame_idx - 1) * step) + frame_offset
        used_frames = []

        while cap.isOpened():
            current_frame = ((frame_idx - 1) * step) + frame_offset
            if current_frame > total_frames:
                break
            else:
                cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
                ret, frame = cap.read()
                # cv2.imshow(mp.current_process().name, frame)
                # cv2.waitKey(1)
                # if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                kps, descs = detector.detectAndCompute(gray, None)

                all_kps.append(kps)
                all_descs.append(descs)
                used_frames.append(current_frame)

                end_time = time.monotonic()

                print(
                    "{0} update: method {1}, season {2}, frame {3} - {4}/{5}, time {6}".format(
                        mp.current_process().name,
                        method,
                        season,
                        frame_idx,
                        current_frame,
                        total_frames,
                        timedelta(seconds=end_time - start_time),
                    )
                )
                frame_idx += 1

        save_data.save_desc(all_descs, "{0}/{1}/{2}_descs_{3}.pickle".format(root_folder, season, method, frame_idx))
        save_data.save_kp(all_kps, "{0}/{1}/{2}_kps_{3}.pickle".format(root_folder, season, method, frame_idx))
        save_data.save_frame_numbers(
            used_frames, "{0}/{1}/{2}_frames_{3}.pickle".format(root_folder, season, method, frame_idx)
        )

        end_time = time.monotonic()
        print(
            "{0} update: method {1}, season {2}, frame {3} - {4}/{5}, time {6}".format(
                mp.current_process().name,
                method,
                season,
                frame_idx,
                current_frame,
                total_frames,
                timedelta(seconds=end_time - start_time),
            )
        )


def generate_combinations(methods, seasons, video_paths):
    combinations = []
    for method in methods:
        for i, season in enumerate(seasons):
            combinations.append([method, season, video_paths[i]])
    return combinations


if __name__ == "__main__":
    combinations = generate_combinations(methods, season_names, seasons_video_paths)
    pool = mp.Pool(processes=1)
    pool.map(worker, combinations)
