# !/usr/bin/env python
import numpy as np
import cv2
from pathlib import Path

root_folder = "/home/lukas/PycharmProjects/Dissertation/_my/datasets/results/specom2020/"
seasons = ["spring", "fall", "winter"]

# [x, y]
summer2spring_summer = [[261, 31], [330, 46], [281, 86], [183, 109], [201, 112], [119, 110], [243, 149], [229, 117]]
summer2spring_spring = [[269, 27], [333, 43], [282, 83], [181, 105], [200, 109], [117, 108], [245, 147], [229, 113]]
summer2fall_summer = [[259, 47], [213, 108], [208, 137], [102, 147], [151, 103], [130, 125], [143, 106], [203, 174], [152, 105], [163, 99], [185, 67]]
summer2fall_fall = [[255, 48], [211, 106], [206, 134], [100, 143], [149, 100], [126, 117], [141, 99], [206, 173], [157, 103], [168, 94], [191, 61]]
summer2winter_summer = [[235, 164], [299, 118], [312, 149], [263, 155], [108, 113], [203, 63], [106, 66], [329, 114]]
summer2winter_winter = [[240, 163], [308, 117], [321, 149], [270, 154], [101, 105], [201, 52], [99, 54], [327, 109]]

summer2spring_summer = np.float32(summer2spring_summer).reshape(-1, 1, 2)
summer2spring_spring = np.float32(summer2spring_spring).reshape(-1, 1, 2)
summer2fall_summer = np.float32(summer2fall_summer).reshape(-1, 1, 2)
summer2fall_fall = np.float32(summer2fall_fall).reshape(-1, 1, 2)
summer2winter_summer = np.float32(summer2winter_summer).reshape(-1, 1, 2)
summer2winter_winter = np.float32(summer2winter_winter).reshape(-1, 1, 2)


def save_data(path, H):
    np.savez(path, H)


def worker(name, pts0, pts1):
    H, _ = cv2.findHomography(pts0, pts1, cv2.RANSAC)
    print(50 * "-")
    print(name)
    print(H)
    print(50 * "-")
    save_data(root_folder + name, H)


if __name__ == '__main__':
    worker("manual_H_summer2spring", summer2spring_summer, summer2spring_spring)
    worker("manual_H_summer2fall", summer2fall_summer, summer2fall_fall)
    worker("manual_H_summer2winter", summer2winter_summer, summer2winter_winter)
