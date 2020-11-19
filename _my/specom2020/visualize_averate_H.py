#!/usr/bin/env python
import multiprocessing as mp
import numpy as np
import cv2
import myutils

seasons = ["spring", "fall", "winter"]
methods = ["sift", "surf", "akaze"]
Hs_out_folder = "../datasets/results/specom2020/homographies/"
spring_video_path = "/data1/nordlandsbanen.spring.sync.1920x1080.h264.nrk.mp4"
summer_video_path = "/data2/nordlandsbanen.summer.sync.1920x1080.h264.nrk.mp4"
fall_video_path = "/data3/nordlandsbanen.fall.sync.1920x1080.h264.nrk.mp4"
winter_video_path = "/data4/nordlandsbanen.winter.sync.1920x1080.h264.nrk.mp4"
seasons_video_paths = [spring_video_path, fall_video_path, winter_video_path]
VISUALIZE = True


def check_h(H):
    if np.linalg.det(H) < 0:
        return False

    N1 = np.sqrt(H[0][0] * H[0][0] + H[1][0] * H[1][0])
    # if N1 > 4 or N1 < 0.1:
    if N1 > 2 or N1 < 0.05:
        return False

    N2 = np.sqrt(H[0][1] * H[0][1] + H[1][1] * H[1][1])
    # if N2 > 4 or N2 < 0.1:
    if N2 > 2 or N2 < 0.05:
        return False

    N3 = np.sqrt(H[2][0] * H[2][0] + H[2][1] * H[2][1])
    # if N3 > 0.002:
    if N3 > 0.001:
        return False
    return True


def visualize_test(H, season, method):
    summer_cap = cv2.VideoCapture(summer_video_path)
    if season == "spring":
        season_cap = cv2.VideoCapture(spring_video_path)
    elif season == "fall":
        season_cap = cv2.VideoCapture(fall_video_path)
    elif season == "winter":
        season_cap = cv2.VideoCapture(winter_video_path)
    else:
        print("BAD SEASON !!!")

    total_frames = int(summer_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_idx = 20
    step = 250
    crop_size = 360
    w = int(summer_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(summer_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    img_sz = 1024
    w_from = int((w / 2) - (img_sz / 2))
    w_to = int((w / 2) + (img_sz / 2))
    h_from = int((h / 2) - (img_sz / 2))
    h_to = int((h / 2) + (img_sz / 2))

    if VISUALIZE:
        cv2.namedWindow("summer_resized")
        cv2.namedWindow(season + "_resized")
        cv2.namedWindow("summer_resized H")
    else:
        count = 0

    for hs in H:
        for hh in hs:
            if hh[0] == hh[1]:
                if (not isinstance(hh[2], int)) and (hh[2] is not None):
                    w, h = hh[2].shape
                    if w == h == 3:
                        if check_h(hh[2]):
                            if VISUALIZE:
                                current_frame = hh[0]
                                if current_frame > total_frames:
                                    print(mp.current_process().name + " BREAK: Total frames: " + str(total_frames) + ", current frame = " + str(current_frame))
                                    break
                                else:
                                    summer_cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
                                    _, summer_frame = summer_cap.read()
                                    summer_center_frame = summer_frame[h_from:h_to, w_from:w_to]
                                    summer_resized = cv2.resize(summer_center_frame, dsize=(crop_size, crop_size), interpolation=cv2.INTER_CUBIC)


                                    season_cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
                                    _, season_frame = season_cap.read()
                                    season_center_frame = season_frame[h_from:h_to, w_from:w_to]
                                    season_resized = cv2.resize(season_center_frame, dsize=(crop_size, crop_size), interpolation=cv2.INTER_CUBIC)

                                    print(current_frame)
                                    cv2.imshow("summer_resized", summer_resized)
                                    cv2.imshow(season + "_resized", season_resized)

                                    h, w, d = season_resized.shape
                                    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                                    dst = cv2.perspectiveTransform(pts, hh[2])
                                    summer_resized = cv2.polylines(summer_resized, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)

                                    cv2.imshow("summer_resized H", summer_resized)

                                    if cv2.waitKey(1) % 256 == 27:
                                        break
                            else:
                                # print(count)
                                count += 1
                                # break
    return count


def load_data(season, method):
    Hs = myutils.load_data.load(Hs_out_folder + "Hs_" + method + "_from_" + season + "_to_summer.pickle")
    Hs_GAN = myutils.load_data.load(Hs_out_folder + "Hs_GAN_" + method + "_transformed_from_" + season + "_to_summer-summer.pickle")
    return Hs, Hs_GAN


def worker(combination):
    season, method = combination
    # H = myutils.load_data.load(Hs_out_folder + "average_H_GAN_" + season + "_" + method + ".pickle")
    Hs, Hs_GAN = load_data(season, method)
    count = visualize_test(Hs, season, method)
    print(mp.current_process().name + " season = " + season + ", method = " + method + ", count = " + str(count))
    count = visualize_test(Hs_GAN, season, method)
    print(mp.current_process().name + " GAN: season = " + season + ", method = " + method + ", count = " + str(count))


def generate_combinations(seasons, methods):
    combo = []
    for season in seasons:
        for method in methods:
            combo.append([season, method])
    return combo


if __name__ == '__main__':
    combinations = generate_combinations(seasons, methods)
    pool = mp.Pool(processes=1)
    pool.map(worker, combinations)
    # worker("winter", "sift")

"""
ForkPoolWorker-2 season = spring, method = sift, count = 1282
ForkPoolWorker-1 season = spring, method = surf, count = 1303
ForkPoolWorker-3 season = spring, method = akaze, count = 1214
ForkPoolWorker-5 season = fall, method = sift, count = 2479
ForkPoolWorker-4 season = fall, method = surf, count = 2486
ForkPoolWorker-6 season = fall, method = akaze, count = 2171
ForkPoolWorker-8 season = winter, method = sift, count = 592
ForkPoolWorker-7 season = winter, method = surf, count = 522
ForkPoolWorker-9 season = winter, method = akaze, count = 590

ForkPoolWorker-2 GAN: season = spring, method = sift, count = 1064
ForkPoolWorker-1 GAN: season = spring, method = surf, count = 1047
ForkPoolWorker-3 GAN: season = spring, method = akaze, count = 1043
ForkPoolWorker-5 GAN: season = fall, method = sift, count = 2152
ForkPoolWorker-4 GAN: season = fall, method = surf, count = 2301
ForkPoolWorker-6 GAN: season = fall, method = akaze, count = 2129
ForkPoolWorker-8 GAN: season = winter, method = sift, count = 270
ForkPoolWorker-7 GAN: season = winter, method = surf, count = 264
ForkPoolWorker-9 GAN: season = winter, method = akaze, count = 496
"""

"""

bez fotka == fotka
ForkPoolWorker-2 season = spring, method = sift, count = 14920
ForkPoolWorker-1 season = spring, method = surf, count = 62233
ForkPoolWorker-3 season = spring, method = akaze, count = 21876
ForkPoolWorker-5 season = fall, method = sift, count = 23055
ForkPoolWorker-4 season = fall, method = surf, count = 78446
ForkPoolWorker-6 season = fall, method = akaze, count = 26253
ForkPoolWorker-8 season = winter, method = sift, count = 2847
ForkPoolWorker-7 season = winter, method = surf, count = 15255
ForkPoolWorker-9 season = winter, method = akaze, count = 11701

ForkPoolWorker-2 GAN: season = spring, method = sift, count = 14321
ForkPoolWorker-1 GAN: season = spring, method = surf, count = 34953
ForkPoolWorker-3 GAN: season = spring, method = akaze, count = 23552
ForkPoolWorker-5 GAN: season = fall, method = sift, count = 30262
ForkPoolWorker-4 GAN: season = fall, method = surf, count = 86936
ForkPoolWorker-6 GAN: season = fall, method = akaze, count = 27936
ForkPoolWorker-8 GAN: season = winter, method = sift, count = 3011
ForkPoolWorker-7 GAN: season = winter, method = surf, count = 15289
ForkPoolWorker-9 GAN: season = winter, method = akaze, count = 10959
"""