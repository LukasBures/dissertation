# !/usr/bin/env python

__author__ = "Lukas Bures"
__copyright__ = "Copyright 2016-2018"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Lukas Bures"
__status__ = "Development"
__email__ = "lbures@kky.zcu.cz"


from process import *

prefix = "/Users/lukas/PycharmProjects/Dissertation/experiments/exp_train/"
files = ["data/_1_SPRING.mov", "data/_2_SUMMER.mov", "data/_3_FALL.mov", "data/_4_WINTER.mov"]
paths1 = [prefix + files[0], prefix + files[1], prefix + files[2], prefix + files[3]]
paths2 = [prefix + files[1], prefix + files[0], prefix + files[2], prefix + files[3]]
paths3 = [prefix + files[2], prefix + files[1], prefix + files[0], prefix + files[3]]
paths4 = [prefix + files[3], prefix + files[1], prefix + files[2], prefix + files[0]]

process(4, prefix + "outputs/AKAZE_1_234.txt", paths1, False)
process(4, prefix + "outputs/AKAZE_2_134.txt", paths2, False)
process(4, prefix + "outputs/AKAZE_3_214.txt", paths3, False)
process(4, prefix + "outputs/AKAZE_4_231.txt", paths4, False)

process(2, prefix + "outputs/SURF_1_234.txt", paths1, False)
process(2, prefix + "outputs/SURF_2_134.txt", paths2, False)
process(2, prefix + "outputs/SURF_3_214.txt", paths3, False)
process(2, prefix + "outputs/SURF_4_231.txt", paths4, False)


process(1, prefix + "outputs/SIFT_1_234.txt", paths1, False)
process(1, prefix + "outputs/SIFT_2_134.txt", paths2, False)
process(1, prefix + "outputs/SIFT_3_214.txt", paths3, False)
process(1, prefix + "outputs/SIFT_4_231.txt", paths4, False)


process(3, prefix + "outputs/ORB_1_234.txt", paths1, False)
process(3, prefix + "outputs/ORB_2_134.txt", paths2, False)
process(3, prefix + "outputs/ORB_3_214.txt", paths3, False)
process(3, prefix + "outputs/ORB_4_231.txt", paths4, False)
