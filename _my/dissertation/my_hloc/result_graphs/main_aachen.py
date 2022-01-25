from typing import List
import matplotlib.pyplot as plt

dataset_name: str = "Aachen"

results_without_dynamic_kp: List[dict] = [
    {
        "static_percentage": 0,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    }
]

results_with_dynamic_kp: List[dict] = [
    {
        "static_percentage": 0,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "day": [0.0, 0.0, 0.0],
        "night": [0.0, 0.0, 0.0],
    }
]

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

for dataset in datasets:
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
    plt.grid(axis="both", color="0.95")
    name = f"{dataset['dataset_name']}_day.png"
    plt.savefig(name)
    plt.show()

    plt.plot(x_static, y_night, "o-")
    plt.title(f"{dataset['dataset_name']}, night.")
    plt.xlabel("% of kept static keypoints")
    plt.ylabel("% of images from dataset")
    plt.legend(["0.25m, 2°", "0.50m, 5°", "5.00m, 10°"], title="Conditions")
    plt.grid(axis="both", color="0.95")
    name = f"{dataset['dataset_name']}_night.png"
    plt.savefig(name)
    plt.show()

print("DONE")
