# !/usr/bin/env python

from __future__ import print_function

import time

import cv2
import numpy as np

__author__ = "Lukas Bures"
__copyright__ = "Copyright 2016-2018"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Lukas Bures"
__status__ = "Development"
__email__ = "lbures@kky.zcu.cz"


# ----------------------------------------------------------------------------------------------------------------------
# It draws KP matches.
def draw_matches(img1, kp1, img2, kp2, match):
    # Create a new output image that concatenates the two images together
    # (a.k.a) a montage
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]

    out = np.zeros((max([rows1, rows2]), cols1 + cols2, 3), dtype="uint8")

    # Place the first image to the left
    out[0:rows1, 0:cols1, :] = img1

    # Place the next image to the right of it
    out[0:rows2, cols1 : cols1 + cols2, :] = img2

    # For each pair of points we have between both images draw circles, then connect a line between them
    for mat in match:
        # Get the matching keypoints for each of the images
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        # x - columns
        # y - rows
        (x1, y1) = kp1[img1_idx].pt
        (x2, y2) = kp2[img2_idx].pt

        # Draw a small circle at both co-ordinates
        cv2.circle(out, (int(x1), int(y1)), 10, (255, 0, 0), -1)
        cv2.circle(out, (int(x2) + cols1, int(y2)), 10, (0, 255, 0), -1)

        # Draw a line in between the two points
        cv2.line(out, (int(x1), int(y1)), (int(x2) + cols1, int(y2)), (0, 0, 255), 3)

    return out


def good_match(mode, matcher, template, video):
    goodmatch = []

    if mode is 1 or mode is 2 or mode is 4:
        match = matcher.knnMatch(template, video, k=2)
        # Store all the good matches as per Lowe's ratio test.
        for j, k in match:
            # 0.7
            if j.distance < (0.7 * k.distance):
                goodmatch.append(j)
    else:
        match = matcher.match(template, video)
        match = sorted(match, key=lambda val: val.distance)
        # Consider the best 10% matches to be good matches
        goodmatch = match[: np.int(len(match) / 10)]

    return goodmatch, match


# ----------------------------------------------------------------------------------------------------------------------
# Create one image from two input images.
def side_by_side2(img1, img2):
    # Create a new output image that concatenates the two images together
    # (a.k.a) a montage
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]

    out = np.zeros((max([rows1, rows2]), cols1 + cols2, 3), dtype="uint8")

    # Place the first image to the left
    out[0:rows1, 0:cols1, :] = img1

    # Place the next image to the right of it
    out[0:rows2, cols1 : cols1 + cols2, :] = img2

    return out


# ----------------------------------------------------------------------------------------------------------------------
# Create one image from four input images.
def side_by_side4(img0, img1, img2, img3):
    # Create a new output image that concatenates the two images together
    # (a.k.a) a montage
    rows0 = img0.shape[0]
    cols0 = img0.shape[1]
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]
    rows3 = img3.shape[0]
    cols3 = img3.shape[1]

    out = np.zeros((max([rows0 + rows2, rows1 + rows3]), max([cols0 + cols1, cols2 + cols3]), 3), dtype="uint8")

    # Place the first image to the left top
    out[0:rows0, 0:cols0, :] = img0

    # Place the second image to the right top
    out[0:rows1, cols0 : cols0 + cols1, :] = img1

    # Place the third image to the left bottom
    out[rows0 : rows0 + rows2, 0:cols2, :] = img2

    # Place the fourth image to the right bottom
    out[rows1 : rows1 + rows3, cols2 : cols2 + cols3, :] = img3

    return out


# ----------------------------------------------------------------------------------------------------------------------
def process(mode, output_file, paths, visual=False):
    print(output_file)
    log = open(output_file, "w")

    print(paths[0], file=log)
    print(paths[1], file=log)
    print(paths[2], file=log)
    print(paths[3], file=log)

    frame = 0
    if visual:
        cv2.namedWindow("TEMPLATE | VIDEO", cv2.WINDOW_NORMAL)

    # Load color image and convert it in to the grayscale color
    # Template = cv2.imread("./img/Stock_84.png", cv2.IMREAD_COLOR)
    # TemplateGS = cv2.cvtColor(Template, cv2.COLOR_RGB2GRAY)
    # cap = cv2.VideoCapture("./img/trimmed.avi")

    cap_0 = cv2.VideoCapture(paths[0])
    cap_1 = cv2.VideoCapture(paths[1])
    cap_2 = cv2.VideoCapture(paths[2])
    cap_3 = cv2.VideoCapture(paths[3])

    matcher = []
    sift = []
    surf = []
    orb = []
    akaze = []

    if mode == 1:
        print("mode: SIFT", file=log)
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        matcher = cv2.FlannBasedMatcher(index_params, search_params)
        sift = cv2.xfeatures2d.SIFT_create(0, 3, 0.04, 10, 1.6)

    elif mode == 2:
        print("mode: SURF", file=log)
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        matcher = cv2.FlannBasedMatcher(index_params, search_params)
        surf = cv2.xfeatures2d.SURF_create(400, 3, 3, 1, 1)

    elif mode == 3:
        print("mode: ORB", file=log)
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        orb = cv2.ORB_create(500, 1.2, 8, 31, 0, 2, cv2.ORB_HARRIS_SCORE, 31)

    elif mode == 4:
        print("mode: AKAZE", file=log)
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
        akaze = cv2.AKAZE_create()

    else:
        print("mode: UNKNOWN", file=log)

    print(
        "video_frame,good_matches_1in0,all_matches_1in0,good_matches_2in0,all_matches_2in0,good_matches_3in0,all_matches_3in0",
        file=log,
    )

    # Main loop
    while True:
        start_time = time.time()
        # Capture frame-by-frame
        ret_0, frame_0 = cap_0.read()
        ret_1, frame_1 = cap_1.read()
        ret_2, frame_2 = cap_2.read()
        ret_3, frame_3 = cap_3.read()

        # Exit if video ends
        if (not ret_0) or (not ret_1) or (not ret_2) or (not ret_3):
            break

        # Convert image in to the grayscale color
        frame_0_gs = cv2.cvtColor(frame_0, cv2.COLOR_RGB2GRAY)
        frame_1_gs = cv2.cvtColor(frame_1, cv2.COLOR_RGB2GRAY)
        frame_2_gs = cv2.cvtColor(frame_2, cv2.COLOR_RGB2GRAY)
        frame_3_gs = cv2.cvtColor(frame_3, cv2.COLOR_RGB2GRAY)

        # Detect keypoints and compute descriptors
        if mode == 1:
            frame_0_kp, frame_0_des = sift.detectAndCompute(frame_0_gs, None)
            frame_1_kp, frame_1_des = sift.detectAndCompute(frame_1_gs, None)
            frame_2_kp, frame_2_des = sift.detectAndCompute(frame_2_gs, None)
            frame_3_kp, frame_3_des = sift.detectAndCompute(frame_3_gs, None)
        elif mode == 2:
            frame_0_kp, frame_0_des = surf.detectAndCompute(frame_0_gs, None)
            frame_1_kp, frame_1_des = surf.detectAndCompute(frame_1_gs, None)
            frame_2_kp, frame_2_des = surf.detectAndCompute(frame_2_gs, None)
            frame_3_kp, frame_3_des = surf.detectAndCompute(frame_3_gs, None)
        elif mode == 3:
            frame_0_kp, frame_0_des = orb.detectAndCompute(frame_0_gs, None)
            frame_1_kp, frame_1_des = orb.detectAndCompute(frame_1_gs, None)
            frame_2_kp, frame_2_des = orb.detectAndCompute(frame_2_gs, None)
            frame_3_kp, frame_3_des = orb.detectAndCompute(frame_3_gs, None)
        elif mode == 4:
            frame_0_kp, frame_0_des = akaze.detectAndCompute(frame_0_gs, None)
            frame_1_kp, frame_1_des = akaze.detectAndCompute(frame_1_gs, None)
            frame_2_kp, frame_2_des = akaze.detectAndCompute(frame_2_gs, None)
            frame_3_kp, frame_3_des = akaze.detectAndCompute(frame_3_gs, None)
        else:
            print("Unknown mode.", file=log)
            break

        if frame_0_des is not None:
            # (template, video)
            if frame_1_des is not None:
                good_matches_1in0, all_matches_1in0 = good_match(mode, matcher, frame_1_des, frame_0_des)
            else:
                good_matches_1in0 = list()
                all_matches_1in0 = 0

            if frame_2_des is not None:
                good_matches_2in0, all_matches_2in0 = good_match(mode, matcher, frame_2_des, frame_0_des)
            else:
                good_matches_2in0 = list()
                all_matches_2in0 = 0

            if frame_3_des is not None:
                good_matches_3in0, all_matches_3in0 = good_match(mode, matcher, frame_3_des, frame_0_des)
            else:
                good_matches_3in0 = list()
                all_matches_3in0 = 0

            print(
                str(frame)
                + ","
                + str(len(good_matches_1in0))
                + ","
                + str(len(all_matches_1in0))
                + ","
                + str(len(good_matches_2in0))
                + ","
                + str(len(all_matches_2in0))
                + ","
                + str(len(good_matches_3in0))
                + ","
                + str(len(all_matches_3in0)),
                file=log,
            )
        else:
            print(str(frame) + ",0,0,0,0,0,0", file=log)

        if visual:
            matchesImg = draw_matches(frame_3, frame_3_kp, frame_0, frame_0_kp, good_matches_3in0)
            out = cv2.resize(matchesImg, (1280, 720 / 2))
            cv2.imshow("TEMPLATE | VIDEO", out)
            # ESC key
            if cv2.waitKey(1) == 27:
                break

        if frame % 10 is 0:
            print(frame)
        # 2950 frames (from 0-2949)
        if frame == 2949:
            break
        frame += 1
        print("--- %s seconds ---" % (time.time() - start_time))

    cap_0.release()
    cap_1.release()
    cap_2.release()
    cap_3.release()
    # Destroy all windows
    cv2.destroyAllWindows()


#
# def ivan(paths):
#     cap_0 = cv2.VideoCapture(paths[0])
#     cap_1 = cv2.VideoCapture(paths[1])
#     cap_2 = cv2.VideoCapture(paths[2])
#     cap_3 = cv2.VideoCapture(paths[3])
#
#     while True:
#         # Capture frame-by-frame
#         ret_0, frame_0 = cap_0.read()
#         ret_1, frame_1 = cap_1.read()
#         ret_2, frame_2 = cap_2.read()
#         ret_3, frame_3 = cap_3.read()
#
#         # Exit if video ends
#         if (not ret_0) or (not ret_1) or (not ret_2) or (not ret_3):
#             break
#
#         mimg = side_by_side4(frame_0, frame_1, frame_2, frame_3)
#
#         out = cv2.resize(mimg, (1280, 720))
#         cv2.imshow("TEMPLATE | VIDEO", out)
#         # ESC key
#         if cv2.waitKey(1) == 27:
#             break
