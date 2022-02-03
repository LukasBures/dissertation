from typing import List

import matplotlib.pyplot as plt
import numpy as np

dataset_name: str = "Aachen v1.1"

results_without_dynamic_kp: List[dict] = [
    {
        "static_percentage": 0,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "day": "62.4 / 73.4 / 82.3",
        "night": "24.1 / 33.0 / 41.9",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "day": "76.5 / 85.4 / 93.2",
        "night": "44.0 / 66.5 / 82.2",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "day": "80.8 / 89.9 / 95.5",
        "night": "64.9 / 80.1 / 92.1",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "day": "82.4 / 90.9 / 96.7",
        "night": "68.1 / 84.3 / 95.8",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "day": "83.1 / 91.7 / 96.4",
        "night": "66.5 / 86.9 / 97.4",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "day": "84.2 / 92.4 / 97.0",
        "night": "67.5 / 85.3 / 97.4",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "day": "83.3 / 92.4 / 97.5",
        "night": "70.7 / 88.0 / 98.4",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "day": "84.6 / 93.2 / 97.1",
        "night": "74.3 / 89.0 / 98.4",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "day": "84.1 / 92.1 / 97.3",
        "night": "67.5 / 88.0 / 98.4",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "day": "85.3 / 93.1 / 97.7",
        "night": "73.8 / 86.9 / 98.4",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "day": "86.7 / 93.9 / 97.8",
        "night": "71.7 / 87.4 / 98.4",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "day": "86.2 / 93.4 / 97.7",
        "night": "73.3 / 88.5 / 98.4",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "day": "85.6 / 93.9 / 98.1",
        "night": "71.2 / 90.1 / 98.4",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "day": "86.2 / 94.5 / 98.1",
        "night": "75.9 / 88.5 / 98.4",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "day": "86.3 / 94.1 / 97.8",
        "night": "73.8 / 89.5 / 98.4",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "day": "86.7 / 94.3 / 97.9",
        "night": "74.3 / 88.0 / 98.4",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "day": "86.9 / 94.7 / 98.4",
        "night": "73.3 / 89.0 / 98.4",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "day": "86.5 / 94.9 / 98.2",
        "night": "73.3 / 89.0 / 98.4",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "day": "86.8 / 95.1 / 98.3",
        "night": "74.3 / 88.5 / 98.4",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "day": "87.0 / 94.5 / 98.3",
        "night": "73.3 / 88.5 / 98.4",
    },
]

results_with_dynamic_kp: List[dict] = [
    # TODO: 0 static, 100 dynamic
    {
        "static_percentage": 0,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "day": "62.1 / 73.1 / 83.5",
        "night": "24.1 / 39.3 / 53.9",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "day": "76.1 / 85.9 / 92.6",
        "night": "56.0 / 70.7 / 85.9",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "day": "79.5 / 88.7 / 95.3",
        "night": "63.4 / 79.6 / 93.2",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "day": "82.2 / 91.1 / 95.9",
        "night": "63.9 / 82.7 / 95.3",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "day": "84.6 / 91.1 / 96.8",
        "night": "70.2 / 85.3 / 97.4",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "day": "85.0 / 91.5 / 97.2",
        "night": "71.7 / 89.0 / 97.4",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "day": "84.8 / 92.2 / 97.1",
        "night": "68.1 / 86.4 / 97.9",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "day": "83.6 / 92.0 / 97.1",
        "night": "72.3 / 88.5 / 97.4",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "day": "84.3 / 92.5 / 97.6",
        "night": "70.7 / 88.0 / 97.9",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "day": "84.8 / 93.3 / 97.6",
        "night": "69.6 / 88.5 / 98.4",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "day": "87.0 / 93.6 / 97.8",
        "night": "70.2 / 89.0 / 98.4",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "day": "85.7 / 93.7 / 98.1",
        "night": "74.9 / 88.5 / 99.0",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "day": "86.5 / 94.1 / 97.9",
        "night": "70.7 / 88.0 / 98.4",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "day": "86.7 / 94.4 / 97.9",
        "night": "72.8 / 88.5 / 98.4",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "day": "86.2 / 93.7 / 98.1",
        "night": "73.3 / 90.1 / 98.4",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "day": "86.3 / 94.3 / 98.2",
        "night": "73.8 / 90.1 / 99.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "day": "86.2 / 94.1 / 98.1",
        "night": "73.8 / 89.5 / 98.4",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "day": "86.5 / 94.5 / 98.2",
        "night": "72.8 / 90.1 / 98.4",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "day": "87.4 / 95.0 / 98.2",
        "night": "73.3 / 88.5 / 98.4",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "day": "86.8 / 94.3 / 98.3",
        "night": "74.3 / 89.0 / 98.4",
    },
]

# Preprocessing the data.
for data in [results_without_dynamic_kp, results_with_dynamic_kp]:
    for r in data:
        r["day"] = r["day"].replace(" ", "").split("/")
        r["night"] = r["night"].replace(" ", "").split("/")
        for idx, ddnn in enumerate(zip(r["day"], r["night"])):
            r["day"][idx] = float(ddnn[0])
            r["night"][idx] = float(ddnn[1])

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
    y_day_with_dynamic_kp.append(r_with_dynamic_kp["day"])
    y_day_without_dynamic_kp.append(r_without_dynamic_kp["day"])

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
    "r^--",
    x_static[offset:],
    y_day_without_dynamic_kp[offset:, 1],
    "g^--",
    x_static[offset:],
    y_day_without_dynamic_kp[offset:, 2],
    "b^--",
)
plt.title(f"{dataset_name}, day.")
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
plt.savefig(f"{dataset_name}_day.pdf")
plt.savefig(f"{dataset_name}_day.png")
plt.show()

print("DONE")
