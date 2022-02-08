from typing import List

import matplotlib.pyplot as plt
import numpy as np

dataset_name: str = "4Seasons training"

results_without_dynamic_kp_run1: List[dict] = [
    {
        "static_percentage": 0,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "results": "24.883% /  49.870% /  75.639%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "results": "55.608% /  82.994% /  95.670%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "results": "67.397% /  91.601% /  98.435%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "results": "78.873% /  95.357% /  99.374%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "results": "81.168% /  96.922% /  99.478%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "results": "84.455% /  97.340% /  99.739%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "results": "85.968% /  98.122% /  99.896%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "results": "86.698% /  98.226% /  99.844%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "results": "87.272% /  98.696% /  99.948%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "results": "88.941% /  98.957% / 100.000%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "results": "88.993% /  98.696% / 100.000%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "results": "89.828% /  99.374% / 100.000%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "results": "90.506% /  99.061% /  99.948%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "results": "91.393% /  99.322% / 100.000%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "results": "91.654% /  99.635% / 100.000%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "results": "91.236% /  99.531% / 100.000%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "results": "91.601% /  99.635% / 100.000%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "results": "91.810% /  99.687% / 100.000%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "results": "91.445% /  99.635% / 100.000%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "results": "92.384% /  99.635% / 100.000%",
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
        "results": "26.813% /  51.852% /  71.883%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "results": "48.774% /  72.300% /  88.002%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "results": "57.173% /  80.230% /  91.967%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "results": "65.884% /  83.568% /  94.105%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "results": "70.370% /  86.437% /  95.305%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "results": "73.239% /  88.628% /  95.722%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "results": "76.682% /  89.619% /  96.035%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "results": "76.943% /  90.975% /  96.870%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "results": "78.091% /  91.810% /  97.131%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "results": "78.821% /  92.540% /  97.287%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "results": "82.212% /  93.792% /  97.496%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "results": "81.534% /  93.584% /  97.653%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "results": "82.838% /  94.105% /  97.705%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "results": "83.620% /  94.888% /  98.018%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "results": "85.550% /  95.879% /  98.226%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "results": "86.020% /  95.931% /  98.435%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "results": " 87.011% /  96.714% /  98.644%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "results": "87.428% /  96.870% /  98.592%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "results": "87.898% /  96.818% /  98.696%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "results": "88.263% /  97.653% /  98.905%",
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


results_without_dynamic_kp: List[dict] = results_without_dynamic_kp_run1
results_with_dynamic_kp: List[dict] = results_with_dynamic_kp_run1

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

# MAIN PLOT
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
    "rx--",
    x_static[offset:],
    y_day_without_dynamic_kp[offset:, 1],
    "gx--",
    x_static[offset:],
    y_day_without_dynamic_kp[offset:, 2],
    "bx--",
)
plt.title(f"{dataset_name}")
plt.xlabel("% of kept static keypoints")
plt.ylabel("% of images from dataset")
plt.legend(
    [
        "0.1m, with dynamic KPs",
        "0.2m, with dynamic KPs",
        "0.5m, with dynamic KPs",
        "0.1m, without dynamic KPs",
        "0.2m, without dynamic KPs",
        "0.5m, without dynamic KPs",
    ],
    title="Conditions",
)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, 101, 10))
plt.grid(axis="both", color="0.95")
plt.savefig(f"plots/{dataset_name.replace(' ', '_')}.pdf")
plt.savefig(f"plots/{dataset_name.replace(' ', '_')}.png")
plt.show()

# INDIVIDUAL PLOTS
for i in range(0, 3):
    if i == 0:
        color = "r"
        limit = 0.1
    elif i == 1:
        color = "g"
        limit = 0.2
    else:
        color = "b"
        limit = 0.5

    plt.plot(
        x_static[offset:],
        y_day_with_dynamic_kp[offset:, i],
        f"{color}.-",
        x_static[offset:],
        y_day_without_dynamic_kp[offset:, i],
        f"{color}x--",
    )
    plt.title(f"{dataset_name}, {limit}m")
    plt.xlabel("% of kept static keypoints")
    plt.ylabel("% of images from dataset")
    plt.legend(
        [
            f"{limit}m, with dynamic KPs",
            f"{limit}m, without dynamic KPs",
        ],
        title="Conditions",
    )
    plt.xlim(xmin=0)
    # plt.ylim(ymin=0)
    plt.xticks(np.arange(0, 101, 10))
    # plt.yticks(np.arange(0, 101, 10))
    plt.grid(axis="both", color="0.95")
    plt.savefig(f"plots/{dataset_name.replace(' ', '_')}_{limit}m.pdf")
    plt.savefig(f"plots/{dataset_name.replace(' ', '_')}_{limit}m.png")
    plt.show()

print(f"{dataset_name} - DONE")
