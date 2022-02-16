from typing import List

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

run: int = 4
dataset_name: str = "4Seasons, training"
print(f"\n{dataset_name} - EXPERIMENT RUN {run}\n")

# 4Seasons-2022.02.07_12.04.32
results_without_dynamic_kp_run1: List[dict] = [
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

# 4Seasons-2022.02.08_19.36.08
results_without_dynamic_kp_run2: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "results": "24.152% /  49.348% /  74.961%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "results": "54.564% /  82.264% /  96.296%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "results": "67.919% /  91.706% /  98.592%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "results": "76.161% /  95.409% /  99.478%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "results": "81.116% /  97.235% /  99.687%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "results": "85.342% /  97.340% /  99.791%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "results": "85.133% /  97.966% /  99.844%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "results": "87.324% /  98.070% /  99.791%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "results": "87.272% /  98.748% /  99.948%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "results": "89.411% /  98.852% / 100.000%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "results": "89.306% /  99.322% / 100.000%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "results": "90.193% /  99.322% /  99.948%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "results": "89.202% /  99.687% / 100.000%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "results": "90.819% /  99.270% /  99.948%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "results": "90.662% /  99.478% / 100.000%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "results": "90.350% /  99.426% / 100.000%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "results": "90.923% /  99.426% / 100.000%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "results": "91.758% /  99.374% / 100.000%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "results": "91.862% /  99.583% / 100.000%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "results": "92.227% /  99.635% / 100.000%",
    },
]
results_with_dynamic_kp_run2: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "results": "26.552% /  51.435% /  73.187%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "results": "48.878% /  72.613% /  86.802%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "results": "60.146% /  79.708% /  91.341%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "results": "65.571% /  83.359% /  93.532%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "results": "69.588% /  86.594% /  95.097%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "results": "72.561% /  89.150% /  95.827%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "results": "76.004% /  90.089% /  96.609%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "results": "77.152% /  91.080% /  96.557%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "results": "78.508% /  92.593% /  97.183%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "results": "80.230% /  93.219% /  97.235%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "results": "81.899% /  94.366% /  97.757%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "results": "82.525% /  94.262% /  97.757%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "results": "83.829% /  95.044% /  98.070%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "results": "83.672% /  95.670% /  98.279%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "results": "85.446% /  95.827% /  98.331%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "results": "86.489% /  96.714% /  98.592%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "results": "87.011% /  96.766% /  98.748%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "results": "86.802% /  97.027% /  98.852%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "results": "87.637% /  97.340% /  98.748%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "results": "88.002% /  97.600% /  98.748%",
    },
]

# 4Seasons-2022.02.09_21.28.45
results_without_dynamic_kp_run3: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "results": "24.726% /  51.330% /  77.882%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "results": "52.947% /  82.316% /  95.253%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "results": "69.275% /  91.132% /  98.905%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "results": "77.726% /  94.627% /  99.322%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "results": "81.168% /  96.453% /  99.478%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "results": "83.829% /  97.548% /  99.583%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "results": "84.768% /  97.966% /  99.948%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "results": "87.376% /  98.852% /  99.896%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "results": "88.002% /  98.487% /  99.948%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "results": "88.889% /  99.322% /  99.948%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "results": "89.411% /  98.957% / 100.000%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "results": "89.254% /  98.957% /  99.948%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "results": "89.724% /  99.478% /  99.948%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "results": "90.871% /  99.791% / 100.000%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "results": "90.089% /  99.531% / 100.000%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "results": "91.862% /  99.687% / 100.000%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "results": "91.706% /  99.687% / 100.000%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "results": "92.019% /  99.583% / 100.000%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "results": "91.288% /  99.844% / 100.000%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "results": "92.123% /  99.844% / 100.000%",
    },
]
results_with_dynamic_kp_run3: List[dict] = [

    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "results": "29.421% /  51.382% /  74.231%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "results": "47.939% /  72.770% /  87.898%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "results": "59.520% /  80.282% /  91.601%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "results": "64.319% /  83.099% /  93.375%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "results": "70.005% /  86.750% /  95.044%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "results": "73.970% /  89.202% /  96.348%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "results": "75.013% /  90.193% /  96.453%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "results": "76.995% /  91.184% /  96.557%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "results": "78.247% /  91.341% /  96.870%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "results": "80.386% /  93.062% /  97.340%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "results": "81.899% /  93.688% /  97.392%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "results": "83.412% /  94.679% /  97.809%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "results": "82.473% /  94.940% /  97.861%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "results": "84.820% /  95.514% /  98.122%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "results": "84.246% /  96.244% /  98.592%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "results": "86.385% /  96.505% /  98.435%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "results": "87.533% /  96.974% /  98.748%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "results": "87.011% /  96.870% /  98.696%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "results": "87.689% /  97.444% /  98.696%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "results": "88.472% /  97.444% /  98.852%",
    },
]

# 4Seasons-2022.02.12_15.28.29 - Sinkhorn iteration = 50
results_without_dynamic_kp_run4: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 0,
        "results": "45.801% /  70.214% /  86.020%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 0,
        "results": "76.474% /  94.262% /  98.070%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 0,
        "results": "83.985% /  96.922% /  99.374%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 0,
        "results": "86.385% /  97.600% /  99.948%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 0,
        "results": "90.089% /  99.113% /  99.896%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 0,
        "results": "90.245% /  98.748% /  99.948%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 0,
        "results": "91.132% /  99.478% /  99.948%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 0,
        "results": "91.706% /  99.374% / 100.000%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 0,
        "results": "92.280% /  99.322% / 100.000%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 0,
        "results": "92.436% /  99.531% / 100.000%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 0,
        "results": "92.384% /  99.531% /  99.948%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 0,
        "results": "93.219% /  99.478% / 100.000%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 0,
        "results": "93.323% /  99.531% / 100.000%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 0,
        "results": "92.906% /  99.478% / 100.000%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 0,
        "results": "93.010% /  99.687% / 100.000%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 0,
        "results": "93.375% /  99.791% / 100.000%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 0,
        "results": "93.219% /  99.791% / 100.000%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 0,
        "results": "93.532% /  99.687% / 100.000%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 0,
        "results": "93.584% /  99.791% / 100.000%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 0,
        "results": "93.427% /  99.844% / 100.000%",
    },
]
results_with_dynamic_kp_run4: List[dict] = [
    {
        "static_percentage": 5,
        "dynamic_percentage": 100,
        "results": "42.984% /  66.667% /  82.055%",
    },
    {
        "static_percentage": 10,
        "dynamic_percentage": 100,
        "results": "62.963% /  81.481% /  91.132%",
    },
    {
        "static_percentage": 15,
        "dynamic_percentage": 100,
        "results": "70.631% /  85.811% /  94.158%",
    },
    {
        "static_percentage": 20,
        "dynamic_percentage": 100,
        "results": "76.995% /  89.671% /  96.192%",
    },
    {
        "static_percentage": 25,
        "dynamic_percentage": 100,
        "results": "80.021% /  91.341% /  96.974%",
    },
    {
        "static_percentage": 30,
        "dynamic_percentage": 100,
        "results": "80.647% /  92.540% /  97.131%",
    },
    {
        "static_percentage": 35,
        "dynamic_percentage": 100,
        "results": "82.890% /  93.636% /  97.757%",
    },
    {
        "static_percentage": 40,
        "dynamic_percentage": 100,
        "results": "84.403% /  95.357% /  97.757%",
    },
    {
        "static_percentage": 45,
        "dynamic_percentage": 100,
        "results": "85.237% /  95.305% /  97.809%",
    },
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "results": "86.698% /  95.983% /  97.966%",
    },
    {
        "static_percentage": 55,
        "dynamic_percentage": 100,
        "results": "87.376% /  96.140% /  97.966%",
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "results": "87.480% /  96.505% /  98.122%",
    },
    {
        "static_percentage": 65,
        "dynamic_percentage": 100,
        "results": "88.732% /  96.661% /  98.122%",
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "results": "89.671% /  97.287% /  98.383%",
    },
    {
        "static_percentage": 75,
        "dynamic_percentage": 100,
        "results": "89.619% /  97.392% /  98.383%",
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "results": "89.932% /  97.757% /  98.592%",
    },
    {
        "static_percentage": 85,
        "dynamic_percentage": 100,
        "results": "90.297% /  97.757% /  98.539%",
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "results": "90.975% /  97.653% /  98.696%",
    },
    {
        "static_percentage": 95,
        "dynamic_percentage": 100,
        "results": "91.445% /  98.279% /  98.696%",
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "results": "91.601% /  98.592% /  99.113%",
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
df.to_csv(f"csv/{dataset_name.replace(' ', '_').replace(',', '')}_run{run}.csv")
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
