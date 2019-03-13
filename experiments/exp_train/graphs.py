# !/usr/bin/env python

__author__ = "Lukas Bures"
__copyright__ = "Copyright 2016-2018"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Lukas Bures"
__status__ = "Development"
__email__ = "lbures@kky.zcu.cz"

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def getpaths(method):
    prefix = "/Users/lukas/PycharmProjects/Dissertation/experiments/exp_train/"
    files = ["outputs/" + method + "_1_234.txt",
             "outputs/" + method + "_2_134.txt",
             "outputs/" + method + "_3_214.txt",
             "outputs/" + method + "_4_231.txt"]
    paths = [prefix + files[0], prefix + files[1], prefix + files[2], prefix + files[3]]
    return paths


def parse(method):
    paths = getpaths(method)

    all_parsed_data = []
    for p in paths:
        with open(p) as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]
            data = lines[6:-1]
            frame_number = []
            detect1 = []
            detect1_all = []
            detect2 = []
            detect2_all = []
            detect3 = []
            detect3_all = []
            for d in data:
                pd = d.split(",")
                frame_number.append(np.float(pd[0]))
                detect1.append(np.float(pd[1]))
                detect1_all.append(np.float(pd[2]))
                detect2.append(np.float(pd[3]))
                detect2_all.append(np.float(pd[4]))
                detect3.append(np.float(pd[5]))
                detect3_all.append(np.float(pd[6]))

        all_parsed_data.append([frame_number, detect1, detect1_all, detect2, detect2_all, detect3, detect3_all])
    return all_parsed_data


def plot_absolute_counts(data, method, visualize=False):
    seasons_combo1 = ["Spring", "Summer", "Fall", "Winter"]
    seasons_combo2 = ["Summer", "Spring", "Fall", "Winter"]
    seasons_combo3 = ["Fall", "Summer", "Spring", "Winter"]
    seasons_combo4 = ["Winter", "Summer", "Fall", "Spring"]
    seasons = [seasons_combo1, seasons_combo2, seasons_combo3, seasons_combo4]

    i = 0
    idx = [1, 3, 5]
    # 4 combination of seasons
    for d in data:
        # 3 combination, eg: Matching Spring to Summer
        for f in range(0, 3):
            season = seasons[i]
            fig, ax = plt.subplots()
            plt.xlim(0, len(d[0]))
            plt.ylim(0, max(d[idx[f]]))
            ax.plot(d[0], d[idx[f]], "k.")
            ax.set(xlabel='Frame number', ylabel='Count of good matches', title=method + ": Matching " + season[0] + " to " + season[f + 1])
            ax.grid()
            fig.savefig("/Users/lukas/PycharmProjects/Dissertation/experiments/exp_train/outputs_img/abosulute_counts/" + method + "_" + season[0] + "_to_" + season[f + 1] + ".png")
            if visualize:
                plt.show()
        i += 1


def plot_relative_percent(data, method, visualize=False):
    seasons_combo1 = ["Spring", "Summer", "Fall", "Winter"]
    seasons_combo2 = ["Summer", "Spring", "Fall", "Winter"]
    seasons_combo3 = ["Fall", "Summer", "Spring", "Winter"]
    seasons_combo4 = ["Winter", "Summer", "Fall", "Spring"]
    seasons = [seasons_combo1, seasons_combo2, seasons_combo3, seasons_combo4]

    i = 0
    idx = [1, 3, 5]
    # 4 combination of seasons
    for d in data:
        # 3 combination, eg: Matching Spring to Summer
        for f in range(0, 3):
            season = seasons[i]
            fig, ax = plt.subplots()
            plt.xlim(0, len(d[0]))

            # calculate ratio
            ddd = []
            for a, b in zip(d[idx[f]], d[idx[f] + 1]):
                ddd.append(a / b * 100)

            plt.ylim(0, max(ddd))

            ax.plot(d[0], ddd, "k.")
            ax.set(xlabel='Frame number', ylabel='Ratio of good matches [%]', title=method + ": Matching " + season[0] + " to " + season[f + 1])
            ax.grid()

            fig.savefig("/Users/lukas/PycharmProjects/Dissertation/experiments/exp_train/outputs_img/relative_percent/" + method + "_" + season[0] + "_to_" + season[f + 1] + ".png")
            if visualize:
                plt.show()
        i += 1


def calculate_averages(data, method, visualize=True):
    seasons_combo1 = ["Spring", "Summer", "Fall", "Winter"]
    seasons_combo2 = ["Summer", "Spring", "Fall", "Winter"]
    seasons_combo3 = ["Fall", "Summer", "Spring", "Winter"]
    seasons_combo4 = ["Winter", "Summer", "Fall", "Spring"]
    seasons = [seasons_combo1, seasons_combo2, seasons_combo3, seasons_combo4]

    i = 0
    idx = [1, 3, 5]
    # 4 combination of seasons
    for d in data:
        # 3 combination, eg: Matching Spring to Summer
        for f in range(0, 3):
            season = seasons[i]

            if visualize:
                print ""
                print method + ": Matching " + season[0] + " to " + season[f + 1]
                print("Absolute: %.2f" % round(sum(d[idx[f]]) / np.float(len(d[idx[f]])), 2))

                ddd = []
                for a, b in zip(d[idx[f]], d[idx[f] + 1]):
                    ddd.append(a / b * 100)
                print("Relative: %.2f" % round(sum(ddd) / np.float(len(ddd)), 2))
        i += 1


methods = ["SIFT", "SURF", "AKAZE"]
for method in methods:
    print "-" * 60
    print method
    parsed_data = parse(method)
    plot_absolute_counts(parsed_data, method)
    plot_relative_percent(parsed_data, method)
    calculate_averages(parsed_data, method)
