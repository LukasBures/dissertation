from typing import List

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

run: int = 4
dataset_name: str = "4Seasons, validation"
print(f"\n{dataset_name} - EXPERIMENT RUN {run}\n")

# 4Seasons-2022.02.07_12.04.32
results_without_dynamic_kp_run1: List[dict] = [
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

# 4Seasons-2022.02.08_19.36.08
results_without_dynamic_kp_run2: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "results": "31.283% /  62.566% /  89.347%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "results": "58.140% /  89.347% /  98.500%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "results": "67.442% /  94.599% /  99.250%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "results": "74.644% /  95.874% /  99.625%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "results": "78.545% /  96.174% /  99.700%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "results": "79.220% /  97.524% / 100.000%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "results": "84.021% /  97.749% / 100.000%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "results": "83.571% /  97.899% /  99.925%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "results": "84.171% /  97.674% / 100.000%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "results": "84.921% /  97.899% / 100.000%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "results": "85.671% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "results": "86.947% /  98.125% / 100.000%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "results": "87.772% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "results": "88.372% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "results": "89.122% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "results": "87.622% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "results": "88.672% /  98.200% / 100.000%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "results": "89.422% /  98.500% / 100.000%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "results": "89.872% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "results": "89.422% /  98.500% / 100.000%",
    },
]
results_with_dynamic_kp_run2: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "results": "19.280% /  44.636% /  74.194%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "results": "34.059% /  61.515% /  85.071%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "results": "47.562% /  69.467% /  89.272%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "results": "50.488% /  73.743% /  91.523%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "results": "53.413% /  79.895% /  93.473%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "results": "58.815% /  81.995% /  95.574%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "results": "60.990% /  84.021% /  96.474%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "results": " 61.740% /  86.872% /  97.599%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "results": "65.791% /  88.222% /  98.350%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "results": "67.592% /  89.797% /  98.500%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "results": "69.917% /  90.623% /  98.575%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "results": "71.493% /  92.123% /  98.950%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "results": "72.768% /  93.098% /  99.250%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "results": "75.394% /  94.524% /  99.775%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "results": "77.344% /  94.149% /  99.550%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "results": "78.395% /  95.199% /  99.775%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "results": "78.620% /  95.724% /  99.550%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "results": "80.045% /  96.024% /  99.775%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "results": "80.195% /  96.324% /  99.925%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "results": "81.170% /  96.849% /  99.925%",
    },
]

# 4Seasons-2022.02.09_21.28.45
results_without_dynamic_kp_run3: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "results": "30.083% /  63.091% /  88.972%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "results": "56.489% /  87.547% /  98.950%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "results": "67.892% /  93.848% /  99.475%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "results": "73.218% /  95.274% /  99.625%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "results": "80.120% /  96.249% /  99.925%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "results": "80.570% /  96.699% /  99.925%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "results": "83.421% /  97.299% / 100.000%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "results": "81.620% /  97.449% / 100.000%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "results": "84.396% /  98.050% /  99.850%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "results": "85.896% /  98.275% / 100.000%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "results": "87.472% /  98.125% / 100.000%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "results": "87.097% /  98.125% / 100.000%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "results": "87.922% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "results": "87.997% /  98.275% / 100.000%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "results": "88.447% /  97.974% / 100.000%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "results": "89.797% /  98.425% / 100.000%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "results": "89.647% /  98.200% / 100.000%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "results": "90.173% /  98.500% / 100.000%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "results": "89.347% /  98.425% / 100.000%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "results": "90.173% /  98.350% / 100.000%",
    },
]
results_with_dynamic_kp_run3: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "results": "19.280% /  45.536% /  74.419%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "results": "36.834% /  61.815% /  83.946%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "results": "45.161% /  68.117% /  88.822%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "results": "50.488% /  74.869% /  92.048%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "results": "54.164% /  78.770% /  93.773%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "results": "56.114% /  81.170% /  95.274%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "results": "60.165% /  83.871% /  96.774%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "results": "64.141% /  86.947% /  97.599%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "results": "68.042% /  88.522% /  98.425%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "results": "68.042% /  89.872% /  98.650%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "results": "69.317% /  90.323% /  99.250%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "results": "72.093% /  91.748% /  98.950%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "results": "73.368% /  93.023% /  99.175%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "results": "75.094% /  93.098% /  99.250%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "results": "75.244% /  94.149% /  99.700%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "results": "78.020% /  94.749% /  99.625%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "results": "77.944% /  95.949% /  99.700%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "results": "80.120% /  95.724% /  99.700%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "results": "80.870% /  96.099% /  99.700%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "results": "82.671% /  96.999% /  99.775%",
    },
]

# 4Seasons-2022.02.12_15.28.29 - Sinkhorn iteration = 50
results_without_dynamic_kp_run4: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "results": "53.263% /  83.196% /  95.724%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "results": "76.294% /  93.998% /  99.850%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "results": "82.146% /  97.674% /  99.925%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "results": "85.446% /  97.899% /  99.925%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "results": "86.647% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "results": "87.847% /  97.974% / 100.000%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "results": "88.672% /  98.425% /  99.925%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "results": "89.947% /  98.500% / 100.000%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "results": "89.272% /  98.425% / 100.000%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "results": "90.023% /  98.425% / 100.000%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "results": "90.698% /  98.275% / 100.000%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "results": "90.248% /  98.575% / 100.000%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "results": "91.373% /  98.500% / 100.000%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "results": "90.923% /  98.350% / 100.000%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "results": "91.148% /  98.800% / 100.000%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "results": "91.298% /  98.425% / 100.000%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "results": "91.148% /  98.500% / 100.000%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "results": "91.148% /  98.575% / 100.000%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "results": "91.898% /  98.500% / 100.000%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "results": "91.823% /  98.500% / 100.000%",
    },
]
results_with_dynamic_kp_run4: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "results": "34.584% /  59.490% /  82.971%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "results": "48.387% /  71.418% /  89.872%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "results": "54.089% /  77.944% /  92.873%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "results": "62.491% /  83.121% /  95.949%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "results": "65.191% /  86.497% /  96.699%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "results": "69.917% /  89.797% /  97.299%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "results": "74.644% /  91.823% /  98.650%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "results": "76.744% /  92.948% /  99.100%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "results": "78.470% /  94.224% /  99.400%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "results": "81.995% /  94.824% /  99.550%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "results": "82.446% /  95.499% /  99.700%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "results": "83.871% /  95.274% /  99.700%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "results": "85.071% /  96.249% /  99.925%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "results": "86.272% /  96.699% / 100.000%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "results": "86.122% /  96.924% / 100.000%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "results": "88.072% /  96.999% / 100.000%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "results": "87.172% /  97.299% / 100.000%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "results": "89.347% /  97.449% / 100.000%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "results": "88.597% /  97.524% / 100.000%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "results": "89.872% /  97.674% / 100.000%",
    },
]

#
results_without_dynamic_kp_run5: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "results": "0.0 / 0.0 / 0.0",
    },
]
results_with_dynamic_kp_run5: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "results": "0.0 / 0.0 / 0.0",
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
elif run == 4:
    results_without_dynamic_kp: List[dict] = results_without_dynamic_kp_run4
    results_with_dynamic_kp: List[dict] = results_with_dynamic_kp_run4
else:
    raise Exception(f"Unknown experiment run (run = {run}).")

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


# Data to pd.DataFrame
data_for_print: dict = {
    "static %": list(),
    "dynamic %": list(),
    "0.10m": list(),
    "0.20m": list(),
    "0.50m": list(),
}
for data in [results_without_dynamic_kp, results_with_dynamic_kp]:
    for d in data:
        data_for_print["static %"].append(d["static_percentage"])
        data_for_print["dynamic %"].append(d["dynamic_percentage"])
        data_for_print["0.10m"].append(d["results"][0])
        data_for_print["0.20m"].append(d["results"][1])
        data_for_print["0.50m"].append(d["results"][2])

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
    y_day_with_dynamic_kp.append(r_with_dynamic_kp["results"])
    y_day_without_dynamic_kp.append(r_without_dynamic_kp["results"])

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
plt.title(f"{dataset_name}")
plt.xlabel("% of kept static keypoints")
plt.ylabel("% of successfully localized images")
plt.legend(
    [
        "0.10m, with dynamic KPs",
        "0.20m, with dynamic KPs",
        "0.50m, with dynamic KPs",
        "0.10m, without dynamic KPs",
        "0.20m, without dynamic KPs",
        "0.50m, without dynamic KPs",
    ],
    title="Conditions:",
    loc=4,
)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, 101, 10))
plt.grid(axis="both", color="0.95")
plt.savefig(f"plots/{dataset_name.replace(' ', '_').replace(',', '')}_run{run}.pdf")
# plt.savefig(f"plots/{dataset_name.replace(' ', '_')}_run{run}.png")
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
    plt.title(f"{dataset_name}, condition: {limit:2.2f}m")
    plt.xlabel("% of kept static keypoints")
    plt.ylabel("% of successfully localized images")
    plt.legend(
        [
            f"{limit:2.2f}m, with dynamic KPs",
            f"{limit:2.2f}m, without dynamic KPs",
        ],
        title="Conditions:",
        loc=4,
    )
    plt.xlim(xmin=0)
    # plt.ylim(ymin=0)
    plt.xticks(np.arange(0, 101, 10))
    # plt.yticks(np.arange(0, 101, 10))
    plt.grid(axis="both", color="0.95")
    plt.savefig(f"plots/{dataset_name.replace(' ', '_').replace(',', '')}_{f'{limit:2.2f}'.replace('.','')}m_run{run}.pdf")
    # plt.savefig(f"plots/{dataset_name.replace(' ', '_')}_{limit}m_run{run}.png")
    plt.show()

print(f"{dataset_name} - DONE")
