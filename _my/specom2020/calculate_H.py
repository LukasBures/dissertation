# !/usr/bin/env python3
import multiprocessing as mp
import numpy as np
import cv2
from pathlib import Path

file_prefix = "dump_summer_original-"
root_folder = "/home/lukas/PycharmProjects/Dissertation/_my/datasets/results/specom2020/"
seasons = ["spring", "fall", "winter"]
methods = ["surf", "sift", "akaze", "superpoint"]


def check_h(H):
    if np.linalg.det(H) < 0:
        return False

    N1 = np.sqrt(H[0][0] * H[0][0] + H[1][0] * H[1][0])
    if N1 > 4 or N1 < 0.1:
        return False

    N2 = np.sqrt(H[0][1] * H[0][1] + H[1][1] * H[1][1])
    if N2 > 4 or N2 < 0.1:
        return False

    N3 = np.sqrt(H[2][0] * H[2][0] + H[2][1] * H[2][1])
    if N3 > 0.002:
        return False
    return True


def load_data(working_folder_path):
    data = []
    for path in Path(working_folder_path).rglob('*.npz'):
        npz_data = np.load(path)
        fr, to = path.name.replace("_matches.npz", "").split("_")
        data.append({"img0": int(fr), "img1": int(to),
                     "keypoints0": npz_data['keypoints0'], "keypoints1": npz_data['keypoints1'],
                     "matches": npz_data['matches'], "confidence": npz_data['match_confidence']})
    return sorted(data, key=lambda k: (k['img0'], k['img1']))


def analyse_data(data, season, transformation, method):
    data = sorted(data, key=lambda k: (k['img0'], k['H_norm']))
    current = data[0]["img0"]
    top_x = 1

    for d in data:
        # if failed to calculate H matrix pass
        if d["H_norm"] == 1e6:
            continue
        else:
            # if img0 has changed
            if current is not d["img0"]:
                current = d["img0"]
                top_x = 1
            if d["img0"] == d["img1"]:
                d.update({"top": top_x})
            top_x += 1

    # statistics
    top1 = 0
    top5 = 0
    top10 = 0
    top20 = 0
    for d in data:
        if "top" in d:
            if d["top"] == 1:
                top1 += 1
            elif 1 < d["top"] <= 5:
                top5 += 1
            elif 5 < d["top"] <= 10:
                top10 += 1
            elif 10 < d["top"] <= 20:
                top20 += 1

    print("{} >> ----------------------------------------------------".format(mp.current_process().name))
    print("{} >> season: {}, transformation: {}, method: {}".format(mp.current_process().name, season, transformation, method))
    print("{} >> top 1: {}, top 5: {}, top 10: {}, top 20: {}".format(mp.current_process().name, top1, top5, top10, top20))
    print("{} >> ----------------------------------------------------".format(mp.current_process().name))
    return data


def process_data(data, H_gt):
    for d in data:
        pts0 = []
        pts1 = []
        H = np.zeros((3, 3), dtype=float)
        H_norm = 1e6
        H_check = False
        for i, m in enumerate(d["matches"]):
            if m > -1:
                pts0.append(d["keypoints0"][i])
                pts1.append(d["keypoints1"][d["matches"][i]])
        if len(pts0) > 4:
            pts0 = np.float32(pts0).reshape(-1, 1, 2)
            pts1 = np.float32(pts1).reshape(-1, 1, 2)
            H, _ = cv2.findHomography(pts0, pts1, cv2.RANSAC)
            if H is not None and H_gt is not None:
                H_norm = np.linalg.norm(np.abs(np.subtract(H, H_gt)))
                H_check = check_h(H)
        d.update({"H": H, "H_norm": H_norm, "H_check": H_check, "H_gt": H_gt})
    return data


def worker(combination):
    working_folder_path = combination[0]
    season = combination[1]
    transformation = combination[2]
    method = combination[3]
    print("{} >> Starting | season: {}, transformation: {}, method: {}".format(mp.current_process().name, season, transformation, method))

    data = load_data(working_folder_path)
    H_gt = np.load(root_folder + "manual_H_summer2" + season + ".npz")["arr_0"]
    processed_data = process_data(data, H_gt)
    analysed_data = analyse_data(processed_data, season, transformation, method)
    np.savez(root_folder + "analysed_data_" + season + "_" + transformation + "_" + method + ".npz", analysed_data)


def generate_combinations(seasons, methods):
    combo = []
    transformed = ["original", "GAN"]
    for season in seasons:
        for t in transformed:
            for method in methods:
                pth = root_folder + file_prefix + season + "_" + t + "_" + method
                combo.append([pth, season, t, method])
    return combo


if __name__ == '__main__':
    combinations = generate_combinations(seasons, methods)

    TEST = False
    if TEST:
        worker(combinations[3])
        worker(combinations[19])
    else:
        pool = mp.Pool()
        pool.map(worker, combinations)

"""
/home/lukas/PycharmProjects/Dissertation/venv/bin/python /home/lukas/PycharmProjects/Dissertation/_my/specom2020/calculate_H.py
ForkPoolWorker-1 >> Starting | season: spring, transformation: original, method: surf
ForkPoolWorker-2 >> Starting | season: spring, transformation: original, method: sift
ForkPoolWorker-3 >> Starting | season: spring, transformation: original, method: akaze
ForkPoolWorker-4 >> Starting | season: spring, transformation: original, method: superpoint
ForkPoolWorker-5 >> Starting | season: spring, transformation: GAN, method: surf
ForkPoolWorker-6 >> Starting | season: spring, transformation: GAN, method: sift
ForkPoolWorker-7 >> Starting | season: spring, transformation: GAN, method: akaze
ForkPoolWorker-8 >> Starting | season: spring, transformation: GAN, method: superpoint
ForkPoolWorker-9 >> Starting | season: fall, transformation: original, method: surf
ForkPoolWorker-10 >> Starting | season: fall, transformation: original, method: sift
ForkPoolWorker-11 >> Starting | season: fall, transformation: original, method: akaze
ForkPoolWorker-12 >> Starting | season: fall, transformation: original, method: superpoint
ForkPoolWorker-11 >> ----------------------------------------------------
ForkPoolWorker-11 >> season: fall, transformation: original, method: akaze
ForkPoolWorker-11 >> top 1: 149, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-11 >> ----------------------------------------------------
ForkPoolWorker-3 >> ----------------------------------------------------
ForkPoolWorker-3 >> season: spring, transformation: original, method: akaze
ForkPoolWorker-3 >> top 1: 81, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-3 >> ----------------------------------------------------
ForkPoolWorker-7 >> ----------------------------------------------------
ForkPoolWorker-7 >> season: spring, transformation: GAN, method: akaze
ForkPoolWorker-7 >> top 1: 75, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-7 >> ----------------------------------------------------
ForkPoolWorker-11 >> Starting | season: fall, transformation: GAN, method: surf
ForkPoolWorker-3 >> Starting | season: fall, transformation: GAN, method: sift
ForkPoolWorker-7 >> Starting | season: fall, transformation: GAN, method: akaze
ForkPoolWorker-6 >> ----------------------------------------------------
ForkPoolWorker-6 >> season: spring, transformation: GAN, method: sift
ForkPoolWorker-6 >> top 1: 140, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-6 >> ----------------------------------------------------
ForkPoolWorker-6 >> Starting | season: fall, transformation: GAN, method: superpoint
ForkPoolWorker-2 >> ----------------------------------------------------
ForkPoolWorker-2 >> season: spring, transformation: original, method: sift
ForkPoolWorker-2 >> top 1: 146, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-2 >> ----------------------------------------------------
ForkPoolWorker-2 >> Starting | season: winter, transformation: original, method: surf
ForkPoolWorker-1 >> ----------------------------------------------------
ForkPoolWorker-1 >> season: spring, transformation: original, method: surf
ForkPoolWorker-1 >> top 1: 175, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-1 >> ----------------------------------------------------
ForkPoolWorker-1 >> Starting | season: winter, transformation: original, method: sift
ForkPoolWorker-10 >> ----------------------------------------------------
ForkPoolWorker-10 >> season: fall, transformation: original, method: sift
ForkPoolWorker-10 >> top 1: 190, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-10 >> ----------------------------------------------------
ForkPoolWorker-10 >> Starting | season: winter, transformation: original, method: akaze
ForkPoolWorker-7 >> ----------------------------------------------------
ForkPoolWorker-7 >> season: fall, transformation: GAN, method: akaze
ForkPoolWorker-7 >> top 1: 149, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-7 >> ----------------------------------------------------
ForkPoolWorker-7 >> Starting | season: winter, transformation: original, method: superpoint
ForkPoolWorker-3 >> ----------------------------------------------------
ForkPoolWorker-3 >> season: fall, transformation: GAN, method: sift
ForkPoolWorker-3 >> top 1: 175, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-3 >> ----------------------------------------------------
ForkPoolWorker-3 >> Starting | season: winter, transformation: GAN, method: surf
ForkPoolWorker-9 >> ----------------------------------------------------
ForkPoolWorker-9 >> season: fall, transformation: original, method: surf
ForkPoolWorker-9 >> top 1: 197, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-9 >> ----------------------------------------------------
ForkPoolWorker-9 >> Starting | season: winter, transformation: GAN, method: sift
ForkPoolWorker-5 >> ----------------------------------------------------
ForkPoolWorker-5 >> season: spring, transformation: GAN, method: surf
ForkPoolWorker-5 >> top 1: 184, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-5 >> ----------------------------------------------------
ForkPoolWorker-5 >> Starting | season: winter, transformation: GAN, method: akaze
ForkPoolWorker-11 >> ----------------------------------------------------
ForkPoolWorker-11 >> season: fall, transformation: GAN, method: surf
ForkPoolWorker-11 >> top 1: 194, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-11 >> ----------------------------------------------------
ForkPoolWorker-11 >> Starting | season: winter, transformation: GAN, method: superpoint
ForkPoolWorker-10 >> ----------------------------------------------------
ForkPoolWorker-10 >> season: winter, transformation: original, method: akaze
ForkPoolWorker-10 >> top 1: 47, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-10 >> ----------------------------------------------------
ForkPoolWorker-1 >> ----------------------------------------------------
ForkPoolWorker-1 >> season: winter, transformation: original, method: sift
ForkPoolWorker-1 >> top 1: 112, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-1 >> ----------------------------------------------------
ForkPoolWorker-5 >> ----------------------------------------------------
ForkPoolWorker-5 >> season: winter, transformation: GAN, method: akaze
ForkPoolWorker-5 >> top 1: 33, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-5 >> ----------------------------------------------------
ForkPoolWorker-9 >> ----------------------------------------------------
ForkPoolWorker-9 >> season: winter, transformation: GAN, method: sift
ForkPoolWorker-9 >> top 1: 84, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-9 >> ----------------------------------------------------
ForkPoolWorker-2 >> ----------------------------------------------------
ForkPoolWorker-2 >> season: winter, transformation: original, method: surf
ForkPoolWorker-2 >> top 1: 145, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-2 >> ----------------------------------------------------
ForkPoolWorker-3 >> ----------------------------------------------------
ForkPoolWorker-3 >> season: winter, transformation: GAN, method: surf
ForkPoolWorker-3 >> top 1: 163, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-3 >> ----------------------------------------------------
ForkPoolWorker-8 >> ----------------------------------------------------
ForkPoolWorker-8 >> sea  son: spring, transformation: GAN, method: superpoint
ForkPoolWorker-8 >> top 1: 200, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-8 >> ----------------------------------------------------
ForkPoolWorker-4 >> ----------------------------------------------------
ForkPoolWorker-4 >> season: spring, transformation: original, method: superpoint
ForkPoolWorker-4 >> top 1: 200, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-4 >> ----------------------------------------------------
ForkPoolWorker-7 >> ----------------------------------------------------
ForkPoolWorker-7 >> season: winter, transformation: original, method: superpoint
ForkPoolWorker-7 >> top 1: 200, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-7 >> ----------------------------------------------------
ForkPoolWorker-12 >> ----------------------------------------------------
ForkPoolWorker-12 >> season: fall, transformation: original, method: superpoint
ForkPoolWorker-12 >> top 1: 200, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-12 >> ----------------------------------------------------
ForkPoolWorker-6 >> ----------------------------------------------------
ForkPoolWorker-6 >> season: fall, transformation: GAN, method: superpoint
ForkPoolWorker-6 >> top 1: 200, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-6 >> ----------------------------------------------------
ForkPoolWorker-11 >> ----------------------------------------------------
ForkPoolWorker-11 >> season: winter, transformation: GAN, method: superpoint
ForkPoolWorker-11 >> top 1: 199, top 5: 0, top 10: 0, top 20: 0
ForkPoolWorker-11 >> ----------------------------------------------------

Process finished with exit code 0

"""