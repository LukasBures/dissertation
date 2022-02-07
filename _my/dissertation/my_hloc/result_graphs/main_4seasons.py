from typing import List

import matplotlib.pyplot as plt
import numpy as np

dataset_name: str = "4Seasons"

results_without_dynamic_kp_run1: List[dict] = [
    {
        "static_percentage": 0,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "results": "63.0 / 73.4 / 81.4",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "results": "75.2 / 85.1 / 92.2",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "results": "81.1 / 89.8 / 95.1",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "results": "81.8 / 90.9 / 95.8",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "results": "84.0 / 91.7 / 96.8",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "results": "83.6 / 92.5 / 97.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "results": "85.0 / 92.5 / 97.3",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "results": "84.2 / 92.6 / 97.2",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "results": "84.7 / 93.7 / 97.5",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "results": "86.2 / 93.3 / 97.7",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "results": "86.3 / 94.1 / 97.7",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "results": "87.0 / 93.6 / 97.6",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "results": "86.7 / 94.2 / 98.1",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "results": "86.8 / 94.1 / 97.8",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "results": "86.7 / 93.9 / 98.1",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "results": "86.2 / 94.1 / 97.8",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "results": "86.9 / 94.8 / 98.2",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "results": "87.0 / 94.8 / 98.3",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "results": "86.8 / 94.9 / 98.3",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "results": "87.0 / 95.0 / 98.3",
    },
]
results_with_dynamic_kp_run1: List[dict] = [
    {
        "static_percentage": 0,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "results": "63.0 / 73.4 / 81.4",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "results": "75.2 / 85.1 / 92.2",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "results": "81.1 / 89.8 / 95.1",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "results": "81.8 / 90.9 / 95.8",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "results": "84.0 / 91.7 / 96.8",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "results": "83.6 / 92.5 / 97.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "results": "85.0 / 92.5 / 97.3",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "results": "84.2 / 92.6 / 97.2",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "results": "84.7 / 93.7 / 97.5",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "results": "86.2 / 93.3 / 97.7",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "results": "86.3 / 94.1 / 97.7",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "results": "87.0 / 93.6 / 97.6",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "results": "86.7 / 94.2 / 98.1",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "results": "86.8 / 94.1 / 97.8",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "results": "86.7 / 93.9 / 98.1",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "results": "86.2 / 94.1 / 97.8",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "results": "86.9 / 94.8 / 98.2",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "results": "87.0 / 94.8 / 98.3",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "results": "86.8 / 94.9 / 98.3",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "results": " 81.770% /  96.249% /  99.700%",
    },
]
results_without_dynamic_kp_run2: List[dict] = [
    {
        "static_percentage": 0,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "results": "63.0 / 73.4 / 81.4",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "results": "75.2 / 85.1 / 92.2",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "results": "81.1 / 89.8 / 95.1",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "results": "81.8 / 90.9 / 95.8",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "results": "84.0 / 91.7 / 96.8",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "results": "83.6 / 92.5 / 97.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "results": "85.0 / 92.5 / 97.3",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "results": "84.2 / 92.6 / 97.2",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "results": "84.7 / 93.7 / 97.5",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "results": "86.2 / 93.3 / 97.7",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "results": "86.3 / 94.1 / 97.7",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "results": "87.0 / 93.6 / 97.6",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "results": "86.7 / 94.2 / 98.1",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "results": "86.8 / 94.1 / 97.8",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "results": "86.7 / 93.9 / 98.1",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "results": "86.2 / 94.1 / 97.8",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "results": "86.9 / 94.8 / 98.2",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "results": "87.0 / 94.8 / 98.3",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "results": "86.8 / 94.9 / 98.3",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "results": "87.0 / 95.0 / 98.3",
    },
]
results_with_dynamic_kp_run2: List[dict] = [
    {
        "static_percentage": 0,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "results": "63.0 / 73.4 / 81.4",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "results": "75.2 / 85.1 / 92.2",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "results": "81.1 / 89.8 / 95.1",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "results": "81.8 / 90.9 / 95.8",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "results": "84.0 / 91.7 / 96.8",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "results": "83.6 / 92.5 / 97.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "results": "85.0 / 92.5 / 97.3",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "results": "84.2 / 92.6 / 97.2",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "results": "84.7 / 93.7 / 97.5",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "results": "86.2 / 93.3 / 97.7",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "results": "86.3 / 94.1 / 97.7",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "results": "87.0 / 93.6 / 97.6",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "results": "86.7 / 94.2 / 98.1",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "results": "86.8 / 94.1 / 97.8",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "results": "86.7 / 93.9 / 98.1",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "results": "86.2 / 94.1 / 97.8",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "results": "86.9 / 94.8 / 98.2",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "results": "87.0 / 94.8 / 98.3",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "results": "86.8 / 94.9 / 98.3",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "results": "87.0 / 95.0 / 98.3",
    },
]


results_without_dynamic_kp: List[dict] = results_without_dynamic_kp_run2
results_with_dynamic_kp: List[dict] = results_with_dynamic_kp_run2

# Preprocessing the data.
for data in [results_without_dynamic_kp, results_with_dynamic_kp]:
    for r in data:
        r["results"] = r["results"].replace(" ", "").replace("%", "").split("/")
        for idx, d in enumerate(r["results"]):
            r["results"][idx] = float(d)

datasets: List[dict] = [
    {
        "dataset_name": f"{dataset_name} + 100% dynamic KP",
        "results": results_with_dynamic_kp,
    },
    {
        "dataset_name": f"{dataset_name} + 0% dynamic KP",
        "results": results_without_dynamic_kp,
    },
]


x_static: list = list()
y_day_with_dynamic_kp: list = list()
y_day_without_dynamic_kp: list = list()

for items in zip(results_without_dynamic_kp, results_with_dynamic_kp):
    r_without_dynamic_kp = items[0]
    r_with_dynamic_kp = items[1]

    if r_with_dynamic_kp["static_percentage"] != r_without_dynamic_kp["static_percentage"]:
        raise Exception("Static percentages do not match!")

    x_static.append(r_with_dynamic_kp["static_percentage"])
    y_day_with_dynamic_kp.append(r_with_dynamic_kp["results"])
    y_day_without_dynamic_kp.append(r_without_dynamic_kp["results"])

x_static = np.array(x_static)
y_day_with_dynamic_kp = np.array(y_day_with_dynamic_kp)
y_day_without_dynamic_kp = np.array(y_day_without_dynamic_kp)

offset: int = 1
plt.plot(
    x_static[offset:],
    y_day_with_dynamic_kp[offset:, 0],
    "r.-",
    x_static[offset:],
    y_day_with_dynamic_kp[offset:, 1],
    "g.-",
    x_static[offset:],
    y_day_with_dynamic_kp[offset:, 2],
    "b.-",
    x_static[offset:],
    y_day_without_dynamic_kp[offset:, 0],
    "kx--",
    x_static[offset:],
    y_day_without_dynamic_kp[offset:, 1],
    "kx--",
    x_static[offset:],
    y_day_without_dynamic_kp[offset:, 2],
    "kx--",
)
plt.title(f"{dataset_name}")
plt.xlabel("% of kept static keypoints")
plt.ylabel("% of images from dataset")
plt.legend(
    [
        "0.25m, 2°, with dynamic KPs",
        "0.50m, 5°, with dynamic KPs",
        "5.00m, 10°, with dynamic KPs",
        "0.25m, 2°, without dynamic KPs",
        "0.50m, 5°, without dynamic KPs",
        "5.00m, 10°, without dynamic KPs",
    ],
    title="Conditions",
)
plt.grid(axis="both", color="0.95")
plt.savefig(f"{dataset_name}.pdf")
plt.savefig(f"{dataset_name}.png")
plt.show()

print("DONE")
