import matplotlib.pyplot as plt
from typing import List


aachen_results_without_dynamic_kp: List[dict] = [
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "day": [72.7, 80.8, 84.7],
        "night": [66.8, 72.9, 81.2],
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "day": [78.5, 87.3, 93.8],
        "night": [71.4, 78.9, 86.3],
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "day": [80.5, 87.9, 94.2],
        "night": [75.5, 83.7, 88.8],
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "day": [84.6, 92.1, 96.5],
        "night": [82.4, 87.4, 92.9],
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "day": [87.2, 92.9, 96.4],
        "night": [85.8, 92.1, 96.1],
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "day": [89.7, 95.8, 98.7],
        "night": [87.8, 94.9, 100.0],
    },
]

aachen_results_with_dynamic_kp: List[dict] = [
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "day": [64.7, 68.8, 77.5],
        "night": [62.2, 71.5, 79.6],
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "day": [68.5, 74.3, 83.8],
        "night": [68.4, 75.9, 85.3],
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "day": [78.5, 82.9, 87.2],
        "night": [75.5, 82.7, 88.8],
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "day": [85.6, 89.9, 94.9],
        "night": [82.4, 86.4, 92.9],
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "day": [86.2, 90.9, 95.4],
        "night": [85.8, 92.1, 95.9],
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "day": [88.7, 95.8, 98.7],
        "night": [87.8, 94.9, 100.0],
    },
]

aachen_datasets: List[dict] = [
    {
        "dataset_name": "Aachen + 100% dynamic KP",
        "results": aachen_results_with_dynamic_kp,
    },
    {
        "dataset_name": "Aachen + 0% dynamic KP",
        "results": aachen_results_without_dynamic_kp,
    }
]

for dataset in aachen_datasets:
    x_static: list = list()
    x_dynamic: list = list()
    y_day: list = list()
    y_night: list = list()
    for result in dataset["results"]:
        x_static.append(result["static_percentage"])
        x_dynamic.append(result["dynamic_percentage"])
        y_day.append(result["day"])
        y_night.append(result["night"])

    plt.plot(x_static, y_day, "o-")
    plt.title(f"{dataset['dataset_name']}, day.")
    plt.xlabel("% of kept static keypoints")
    plt.ylabel("% of images from dataset")
    plt.legend(["0.25m, 2°", "0.50m, 5°", "5.00m, 10°"], title="Conditions")
    plt.grid(axis="both", color='0.95')
    name = f"{dataset['dataset_name']}_day.png"
    plt.savefig(name)
    plt.show()

    plt.plot(x_static, y_night, "o-")
    plt.title(f"{dataset['dataset_name']}, night.")
    plt.xlabel("% of kept static keypoints")
    plt.ylabel("% of images from dataset")
    plt.legend(["0.25m, 2°", "0.50m, 5°", "5.00m, 10°"], title="Conditions")
    plt.grid(axis="both", color='0.95')
    name = f"{dataset['dataset_name']}_night.png"
    plt.savefig(name)
    plt.show()

print("DONE")
