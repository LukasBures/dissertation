#!/usr/bin/env python
import multiprocessing as mp
import numpy as np
import cv2
import myutils

seasons = ["spring", "fall", "winter"]
methods = ["surf", "sift", "akaze"]
Hs_out_folder = "../datasets/results/specom2020/homographies/"
spring_video_path = "/data1/nordlandsbanen.spring.sync.1920x1080.h264.nrk.mp4"
summer_video_path = "/data2/nordlandsbanen.summer.sync.1920x1080.h264.nrk.mp4"
fall_video_path = "/data3/nordlandsbanen.fall.sync.1920x1080.h264.nrk.mp4"
winter_video_path = "/data4/nordlandsbanen.winter.sync.1920x1080.h264.nrk.mp4"

seasons_video_paths = [spring_video_path, fall_video_path, winter_video_path]

def check_h(H):
    if np.linalg.det(H) < 0:
        return False

    N1 = np.sqrt(H[0][0] * H[0][0] + H[1][0] * H[1][0])
    if N1 > 4 or N1 < 0.1:
    # if N1 > 2 or N1 < 0.05:
        return False

    N2 = np.sqrt(H[0][1] * H[0][1] + H[1][1] * H[1][1])
    if N2 > 4 or N2 < 0.1:
    # if N2 > 2 or N2 < 0.05:
        return False

    N3 = np.sqrt(H[2][0] * H[2][0] + H[2][1] * H[2][1])
    if N3 > 0.002:
    # if N3 > 0.001:
        return False
    return True

def calculate_average_Hs(list_list_H):
    average_H = np.zeros(shape=(3, 3))
    count = 0.0
    for list_H in list_list_H:
        for H_data in list_H:
            if H_data[0] == H_data[1]:
                if (not isinstance(H_data[2], int)) and (H_data[2] is not None):
                    w, h = H_data[2].shape
                    if w == h == 3:
                        if check_h(H_data[2]):
                            average_H += H_data[2]
                            count += 1.0
                            break
    average_H /= count
    return average_H


def load_data(season, method):
    Hs = myutils.load_data.load(Hs_out_folder + "Hs_" + method + "_from_" + season + "_to_summer.pickle")
    Hs_GAN = myutils.load_data.load(Hs_out_folder + "Hs_GAN_" + method + "_transformed_from_" + season + "_to_summer-summer.pickle")
    return Hs, Hs_GAN


def worker(combination):
    season = combination[0]
    method = combination[1]
    print(mp.current_process().name + " season = " + season + ", method = " + method)

    Hs, Hs_GAN = load_data(season, method)

    Hs_average = calculate_average_Hs(Hs)
    print(mp.current_process().name + " Hs = ", str(Hs_average))
    # visualize_test(Hs_average, season)
    myutils.save_data.save(Hs_average, Hs_out_folder + "average_H_" + season + "_" + method + ".pickle")

    Hs_GAN_average = calculate_average_Hs(Hs_GAN)
    print(mp.current_process().name + " Hs_GAN = ", str(Hs_GAN_average))
    # visualize_test(Hs_GAN_average, season)
    myutils.save_data.save(Hs_GAN_average, Hs_out_folder + "average_H_GAN_" + season + "_" + method + ".pickle")
    

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
        for combination in combinations:
            worker(combination)
    else:
        # pool = mp.Pool(processes=12)
        pool = mp.Pool()
        pool.map(worker, combinations)
