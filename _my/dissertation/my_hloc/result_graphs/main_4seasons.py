from typing import List

import matplotlib.pyplot as plt
import numpy as np

dataset_name: str = "4Seasons - validation"

results_without_dynamic_kp_run1: List[dict] = [
    {
        "static_percentage": 0,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "results": "28.882% /  59.415% /  86.572%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "results": "56.789% /  86.872% /  98.275%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "results": "68.567% /  93.548% /  99.625%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "results": "74.719% /  95.049% /  99.325%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "results": "79.070% /  96.624% / 100.000%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "results": "80.795% /  96.624% / 100.000%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "results": "82.821% /  96.624% /  99.925%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "results": "84.246% /  97.674% / 100.000%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "results": "84.471% /  97.749% /  99.925%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "results": "86.422% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "results": "85.746% /  98.425% / 100.000%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "results": "87.922% /  98.425% / 100.000%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "results": "87.322% /  98.200% / 100.000%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "results": "87.622% /  98.275% / 100.000%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "results": "88.522% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "results": "89.122% /  98.425% / 100.000%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "results": "88.972% /  98.425% / 100.000%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "results": "89.047% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "results": "89.872% /  98.425% / 100.000%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "results": "89.422% /  98.275% / 100.000%",
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
        "results": "19.355% /  44.786% /  75.169%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "results": "36.009% /  62.416% /  84.921%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "results": "44.261% /  70.443% /  88.747%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "results": "49.212% /  74.269% /  91.373%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "results": "54.914% /  77.869% /  94.374%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "results": "59.415% /  82.446% /  96.099%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "results": "62.191% /  84.396% /  96.774%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "results": "64.216% /  86.422% /  97.674%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "results": "66.917% /  89.122% /  97.824%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "results": "69.542% /  89.797% /  98.650%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "results": "69.617% /  90.323% /  98.725%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "results": " 72.168% /  91.973% /  99.400%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "results": "72.993% /  93.098% /  99.400%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "results": "74.719% /  93.848% /  99.550%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "results": "76.444% /  94.524% /  99.550%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "results": "77.119% /  94.374% /  99.625%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "results": "77.644% /  95.349% /  99.775%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "results": "81.095% /  96.249% /  99.775%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "results": "82.221% /  96.699% /  99.775%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "results": "81.770% /  96.249% /  99.700%",
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
plt.savefig(f"{dataset_name}.pdf")
plt.savefig(f"{dataset_name}.png")
plt.show()

print("DONE")
