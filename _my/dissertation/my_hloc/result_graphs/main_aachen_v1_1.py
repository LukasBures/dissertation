from typing import List

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

run: int = 1
dataset_name: str = "Aachen v1.1"
print(f"\n{dataset_name} - EXPERIMENT RUN {run}\n")

# 2022.01.19_23.19.29
results_without_dynamic_kp_run1: List[dict] = [
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
results_with_dynamic_kp_run1: List[dict] = [
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

# 2022.01.30_10.12.19
results_without_dynamic_kp_run2: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "day": "61.4 / 74.5 / 83.6",
        "night": "22.5 / 36.1 / 45.0",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "day": "76.7 / 86.3 / 93.3",
        "night": "51.8 / 71.7 / 82.7",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "day": "81.3 / 89.8 / 95.3",
        "night": "64.9 / 79.6 / 93.2",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "day": "82.6 / 90.2 / 96.1",
        "night": "65.4 / 82.7 / 93.7",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "day": "84.3 / 92.4 / 96.6",
        "night": "68.1 / 86.4 / 96.3",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "day": "83.5 / 92.1 / 96.7",
        "night": "69.1 / 85.3 / 96.3",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "day": "85.2 / 93.0 / 97.2",
        "night": "67.5 / 88.0 / 97.9",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "day": "84.8 / 92.5 / 97.1",
        "night": "71.7 / 88.0 / 98.4",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "day": "86.3 / 93.2 / 97.5",
        "night": "71.2 / 87.4 / 97.9",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "day": "85.1 / 93.9 / 97.6",
        "night": "73.3 / 88.5 / 98.4",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "day": "85.7 / 93.6 / 97.6",
        "night": "73.3 / 89.0 / 98.4",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "day": "86.7 / 93.7 / 97.7",
        "night": "71.7 / 87.4 / 99.0",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "day": "86.7 / 94.3 / 97.9",
        "night": "73.3 / 88.0 / 98.4",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "day": "85.7 / 94.2 / 98.1",
        "night": "74.3 / 89.5 / 98.4",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "day": "86.2 / 93.9 / 97.9",
        "night": "73.3 / 88.0 / 99.0",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "day": "86.0 / 93.9 / 98.1",
        "night": "74.3 / 88.5 / 98.4",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "day": "86.4 / 94.4 / 98.2",
        "night": "71.7 / 87.4 / 98.4",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "day": "86.7 / 94.1 / 98.3",
        "night": "71.2 / 90.1 / 98.4",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "day": "86.4 / 94.2 / 98.2",
        "night": "72.8 / 87.4 / 98.4",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "day": "86.4 / 94.5 / 98.4",
        "night": "74.9 / 88.5 / 98.4",
    },
]
results_with_dynamic_kp_run2: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "day": "60.7 / 73.1 / 82.9",
        "night": "29.3 / 37.2 / 48.7",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "day": "75.0 / 85.2 / 93.0",
        "night": "55.0 / 70.7 / 84.3",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "day": "79.7 / 89.3 / 95.4",
        "night": "61.8 / 80.6 / 92.1",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "day": "81.9 / 91.5 / 96.5",
        "night": "67.0 / 83.8 / 95.8",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "day": "83.3 / 92.5 / 97.0",
        "night": "67.0 / 84.3 / 97.4",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "day": "84.3 / 91.7 / 97.1",
        "night": "66.0 / 85.3 / 97.4",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "day": "84.2 / 92.7 / 97.1",
        "night": "69.6 / 85.3 / 98.4",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "day": "84.2 / 92.7 / 97.5",
        "night": "70.2 / 87.4 / 97.4",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "day": "85.2 / 93.3 / 97.7",
        "night": "68.1 / 85.9 / 97.9",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "day": "85.2 / 93.2 / 97.5",
        "night": "69.1 / 90.1 / 98.4",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "day": "85.4 / 92.6 / 97.8",
        "night": "73.3 / 87.4 / 98.4",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "day": "86.7 / 94.1 / 98.1",
        "night": "71.2 / 89.0 / 98.4",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "day": "86.8 / 94.3 / 98.1",
        "night": "72.8 / 88.0 / 98.4",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "day": "86.9 / 93.4 / 98.1",
        "night": "73.3 / 88.0 / 98.4",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "day": "86.4 / 93.8 / 97.9",
        "night": "72.8 / 89.0 / 98.4",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "day": "86.7 / 94.3 / 98.1",
        "night": "73.3 / 89.5 / 99.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "day": "86.9 / 94.7 / 98.3",
        "night": "72.8 / 89.0 / 98.4",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "day": "86.3 / 94.3 / 98.2",
        "night": "73.8 / 88.5 / 98.4",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "day": "87.0 / 94.2 / 98.5",
        "night": "72.8 / 88.0 / 99.0",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "day": "87.3 / 94.5 / 98.3",
        "night": "74.3 / 89.0 / 98.4",
    },
]

# 2022.02.13_22.09.26
results_without_dynamic_kp_run3: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
]
results_with_dynamic_kp_run3: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
]

#
results_without_dynamic_kp_run4: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
]
results_with_dynamic_kp_run4: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "day": "0.0 / 0.0 / 0.0",
        "night": "0.0 / 0.0 / 0.0",
    },
]

if run == 1:
    results_without_dynamic_kp: List[dict] = results_without_dynamic_kp_run1
    results_with_dynamic_kp: List[dict] = results_with_dynamic_kp_run1
elif run == 2:
    results_without_dynamic_kp: List[dict] = results_without_dynamic_kp_run2
    results_with_dynamic_kp: List[dict] = results_with_dynamic_kp_run2
elif run == 3:
    results_without_dynamic_kp: List[dict] = results_without_dynamic_kp_run3
    results_with_dynamic_kp: List[dict] = results_with_dynamic_kp_run3
else:
    raise Exception(f"Unknown experiment run (run = {run}).")

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

# Data to pd.DataFrame
data_for_print: dict = {
    "static %": list(),
    "dynamic %": list(),
    "day, 0.25m, 2°": list(),
    "day, 0.50m, 5°": list(),
    "day, 5.00m, 10°": list(),
}
for data in [results_without_dynamic_kp, results_with_dynamic_kp]:
    for d in data:
        data_for_print["static %"].append(d["static_percentage"])
        data_for_print["dynamic %"].append(d["dynamic_percentage"])
        data_for_print["day, 0.25m, 2°"].append(d["day"][0])
        data_for_print["day, 0.50m, 5°"].append(d["day"][1])
        data_for_print["day, 5.00m, 10°"].append(d["day"][2])

df: DataFrame = DataFrame(data=data_for_print)
print(df)

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

# MAIN PLOT
offset: int = 0
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
plt.title(f"{dataset_name}, day")
plt.xlabel("% of kept static keypoints")
plt.ylabel("% of successfully localized images")
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
    loc=4,
)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, 101, 10))
plt.grid(axis="both", color="0.95")
plt.savefig(f"plots/{dataset_name.replace(' ', '_').replace(',', '')}_day_run{run}.pdf")
# plt.savefig(f"plots/{dataset_name.replace(' ', '_')}_day_run{run}.png")
plt.show()

# INDIVIDUAL PLOTS
for i in range(0, 3):
    if i == 0:
        color = "r"
        limit = 0.25
        angle = 2
    elif i == 1:
        color = "g"
        limit = 0.50
        angle = 5
    else:
        color = "b"
        limit = 5.00
        angle = 10

    plt.plot(
        x_static[offset:],
        y_day_with_dynamic_kp[offset:, i],
        f"{color}.-",
        x_static[offset:],
        y_day_without_dynamic_kp[offset:, i],
        f"{color}x--",
    )
    plt.title(f"{dataset_name}, day, conditions: {limit:2.2f}m, {angle}°")
    plt.xlabel("% of kept static keypoints")
    plt.ylabel("% of successfully localized images")
    plt.legend(
        [
            f"{limit:2.2f}m, {angle}°, with dynamic KPs",
            f"{limit:2.2f}m, {angle}°, without dynamic KPs",
        ],
        title="Conditions:",
        loc=4,
    )
    plt.xlim(xmin=0)
    # plt.ylim(ymin=0)
    plt.xticks(np.arange(0, 101, 10))
    # plt.yticks(np.arange(0, 101, 10))
    plt.grid(axis="both", color="0.95")
    plt.savefig(f"plots/{dataset_name.replace(' ', '_').replace(',', '')}_{limit:2.2f}m_{angle}_run{run}.pdf")
    # plt.savefig(f"plots/{dataset_name.replace(' ', '_')}_{limit:2.2f}m_{angle}_run{run}.png")
    plt.show()

print(f"{dataset_name} - DONE")
