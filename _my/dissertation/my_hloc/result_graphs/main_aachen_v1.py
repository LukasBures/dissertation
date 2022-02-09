from typing import List

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

run: int = 1
dataset_name: str = "Aachen v1"
print(f"\n{dataset_name} - EXPERIMENT RUN {run}\n")

results_without_dynamic_kp_run1: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "day": "63.0 / 73.4 / 81.4",
        "night": "30.6 / 38.8 / 46.9",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "day": "75.2 / 85.1 / 92.2",
        "night": "56.1 / 68.4 / 85.7",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "day": "81.1 / 89.8 / 95.1",
        "night": "69.4 / 82.7 / 94.9",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "day": "81.8 / 90.9 / 95.8",
        "night": "74.5 / 83.7 / 98.0",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "day": "84.0 / 91.7 / 96.8",
        "night": "76.5 / 88.8 / 99.0",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "day": "83.6 / 92.5 / 97.0",
        "night": "79.6 / 88.8 / 100.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "day": "85.0 / 92.5 / 97.3",
        "night": "81.6 / 90.8 / 100.0",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "day": "84.2 / 92.6 / 97.2",
        "night": "80.6 / 90.8 / 100.0",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "day": "84.7 / 93.7 / 97.5",
        "night": "81.6 / 89.8 / 100.0",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "day": "86.2 / 93.3 / 97.7",
        "night": "78.6 / 92.9 / 100.0",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "day": "86.3 / 94.1 / 97.7",
        "night": "83.7 / 90.8 / 100.0",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "day": "87.0 / 93.6 / 97.6",
        "night": "84.7 / 92.9 / 100.0",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "day": "86.7 / 94.2 / 98.1",
        "night": "83.7 / 92.9 / 100.0",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "day": "86.8 / 94.1 / 97.8",
        "night": "82.7 / 88.8 / 100.0",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "day": "86.7 / 93.9 / 98.1",
        "night": "85.7 / 92.9 / 100.0",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "day": "86.2 / 94.1 / 97.8",
        "night": "84.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "day": "86.9 / 94.8 / 98.2",
        "night": "83.7 / 90.8 / 100.0",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "day": "87.0 / 94.8 / 98.3",
        "night": "84.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "day": "86.8 / 94.9 / 98.3",
        "night": "86.7 / 89.8 / 100.0",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "day": "87.0 / 95.0 / 98.3",
        "night": "85.7 / 90.8 / 100.0",
    },
]
results_with_dynamic_kp_run1: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "day": "62.0 / 72.7 / 82.8",
        "night": "32.7 / 44.9 / 54.1",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "day": "74.0 / 85.6 / 94.1",
        "night": "61.2 / 73.5 / 89.8",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "day": "81.1 / 89.7 / 95.5",
        "night": "71.4 / 82.7 / 95.9",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "day": "82.8 / 90.8 / 96.5",
        "night": "76.5 / 88.8 / 96.9",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "day": "83.1 / 92.1 / 96.8",
        "night": "77.6 / 87.8 / 100.0",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "day": "83.7 / 91.0 / 96.6",
        "night": "82.7 / 89.8 / 100.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "day": "84.2 / 93.1 / 97.1",
        "night": "81.6 / 88.8 / 100.0",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "day": "84.1 / 93.1 / 97.3",
        "night": "81.6 / 87.8 / 100.0",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "day": "85.4 / 93.8 / 97.7",
        "night": "80.6 / 90.8 / 100.0",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "day": "84.2 / 93.4 / 97.6",
        "night": "84.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "day": "86.4 / 93.6 / 97.7",
        "night": "82.7 / 90.8 / 100.0",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "day": "85.7 / 94.1 / 97.7",
        "night": "84.7 / 95.9 / 100.0",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "day": "85.7 / 94.7 / 98.2",
        "night": "83.7 / 90.8 / 100.0",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "day": "87.1 / 94.2 / 97.6",
        "night": "83.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "day": "86.9 / 94.5 / 98.1",
        "night": "85.7 / 92.9 / 100.0",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "day": "85.7 / 94.5 / 98.1",
        "night": "85.7 / 92.9 / 100.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "day": "86.8 / 94.2 / 98.1",
        "night": "83.7 / 90.8 / 100.0",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "day": "86.8 / 94.4 / 98.2",
        "night": "84.7 / 92.9 / 100.0",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "day": "86.9 / 94.4 / 98.2",
        "night": "84.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "day": "87.5 / 94.3 / 98.2",
        "night": "84.7 / 89.8 / 100.0",
    },
]
results_without_dynamic_kp_run2: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "day": "61.2 / 72.3 / 81.8",
        "night": "35.7 / 39.8 / 50.0",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "day": "75.0 / 84.6 / 92.8",
        "night": "61.2 / 71.4 / 87.8",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "day": "79.9 / 89.1 / 95.1",
        "night": "71.4 / 82.7 / 94.9",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "day": "81.8 / 90.8 / 96.5",
        "night": "77.6 / 86.7 / 98.0",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "day": "83.3 / 91.5 / 96.7",
        "night": "77.6 / 87.8 / 99.0",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "day": "84.1 / 91.9 / 97.1",
        "night": "81.6 / 89.8 / 100.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "day": "84.8 / 92.1 / 97.1",
        "night": "80.6 / 90.8 / 100.0",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "day": "85.1 / 92.4 / 97.6",
        "night": "82.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "day": "85.0 / 93.2 / 97.9",
        "night": "79.6 / 92.9 / 100.0",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "day": "85.2 / 94.2 / 97.6",
        "night": "83.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "day": "85.8 / 94.1 / 97.8",
        "night": "83.7 / 89.8 / 100.0",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "day": "86.0 / 93.9 / 97.8",
        "night": "85.7 / 90.8 / 100.0	",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "day": "86.9 / 94.3 / 98.1",
        "night": "84.7 / 90.8 / 100.0",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "day": "85.3 / 94.1 / 97.9",
        "night": "83.7 / 89.8 / 100.0",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "day": "86.2 / 94.5 / 98.3",
        "night": "79.6 / 90.8 / 100.0",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "day": "86.7 / 94.4 / 98.3",
        "night": "82.7 / 89.8 / 100.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "day": "86.5 / 93.3 / 97.8",
        "night": "84.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "day": "87.4 / 94.7 / 98.2",
        "night": "85.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "day": "87.7 / 95.0 / 98.3",
        "night": "82.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "day": "87.4 / 94.9 / 98.3",
        "night": "84.7 / 91.8 / 100.0",
    },
]
results_with_dynamic_kp_run2: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "day": "63.3 / 74.3 / 84.6",
        "night": "32.7 / 43.9 / 54.1",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "day": "74.2 / 85.8 / 93.3",
        "night": "60.2 / 76.5 / 89.8",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "day": "79.6 / 88.8 / 95.4",
        "night": "67.3 / 82.7 / 93.9",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "day": "82.6 / 90.7 / 96.2",
        "night": "76.5 / 83.7 / 98.0",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "day": "83.1 / 91.3 / 96.8",
        "night": "75.5 / 88.8 / 99.0",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "day": "83.5 / 90.8 / 96.6",
        "night": "77.6 / 88.8 / 100.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "day": "84.3 / 92.6 / 97.3",
        "night": "82.7 / 90.8 / 100.0",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "day": "86.2 / 93.3 / 97.6",
        "night": "82.7 / 90.8 / 100.0",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "day": "85.2 / 92.7 / 97.3",
        "night": "81.6 / 90.8 / 100.0",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "day": "85.3 / 93.2 / 97.5",
        "night": "81.6 / 92.9 / 100.0",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "day": "85.8 / 93.2 / 97.9",
        "night": "82.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "day": "85.7 / 93.4 / 97.9",
        "night": "83.7 / 90.8 / 100.0",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "day": "86.3 / 94.3 / 98.1",
        "night": "85.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "day": "85.6 / 93.7 / 97.9",
        "night": "83.7 / 91.8 / 100.0",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "day": "86.0 / 94.3 / 98.1",
        "night": "84.7 / 90.8 / 100.0",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "day": "86.5 / 93.8 / 98.3",
        "night": "81.6 / 92.9 / 100.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "day": "86.8 / 94.5 / 98.2",
        "night": "84.7 / 88.8 / 100.0",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "day": "86.4 / 94.7 / 98.2",
        "night": "83.7 / 90.8 / 100.0",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "day": "87.4 / 94.9 / 98.2",
        "night": "83.7 / 89.8 / 100.0",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "day": "86.4 / 94.5 / 98.2",
        "night": "83.7 / 91.8 / 100.0",
    },
]
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
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, 101, 10))
plt.grid(axis="both", color="0.95")
plt.savefig(f"plots/{dataset_name.replace(' ', '_')}_day.pdf")
plt.savefig(f"plots/{dataset_name.replace(' ', '_')}_day.png")
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
    plt.title(f"{dataset_name} day, conditions: {limit}m, {angle}°")
    plt.xlabel("% of kept static keypoints")
    plt.ylabel("% of images from dataset")
    plt.legend(
        [
            f"{limit:2.2f}m, {angle}°, with dynamic KPs",
            f"{limit:2.2f}m, {angle}°, without dynamic KPs",
        ],
        title="Conditions",
    )
    plt.xlim(xmin=0)
    # plt.ylim(ymin=0)
    plt.xticks(np.arange(0, 101, 10))
    # plt.yticks(np.arange(0, 101, 10))
    plt.grid(axis="both", color="0.95")
    plt.savefig(f"plots/{dataset_name.replace(' ', '_')}_{limit:2.2f}m_{angle}.pdf")
    plt.savefig(f"plots/{dataset_name.replace(' ', '_')}_{limit:2.2f}m_{angle}.png")
    plt.show()

print(f"{dataset_name} - DONE")
