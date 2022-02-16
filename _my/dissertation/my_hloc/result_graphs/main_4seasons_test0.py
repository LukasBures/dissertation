from typing import List
import yaml
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
import os

run: int = 2
dataset_name: str = "4Seasons, test0"
print(f"\n{dataset_name} - EXPERIMENT RUN {run}\n")

# Experiment 1 - 4Seasons-2022.02.09_21.28.45
experiment_1: str = "/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/result_graphs/4Seasons/results_reloc/lukas_bures_exp1/test0_results"

# Experiment 2 - 4Seasons-2022.02.12_15.28.29
experiment_2: str = "/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/result_graphs/4Seasons/results_reloc/lukas_bures_exp2/test0_results"

if run == 1:
    exp_dir: str = experiment_1
elif run == 2:
    exp_dir: str = experiment_2
else:
    raise Exception(f"Unknown experiment run (run = {run}).")

results_without_dynamic_kp: List[dict] = list()
results_with_dynamic_kp: List[dict] = list()

for file in os.listdir(exp_dir):
    if file.endswith(".yaml"):
        with open(os.path.join(exp_dir, file), "r") as stream:
            try:
                data: dict = yaml.safe_load(stream)
                static_percentage: int = int(data["method"].split("_")[0].replace("s", ""))
                dynamic_percentage: int = int(data["method"].split("_")[1].replace("d", ""))
                if dynamic_percentage == 0:
                    results_without_dynamic_kp.append({
                        "static_percentage": static_percentage,
                        "dynamic_percentage": 0,
                        "results": f"{data['recall_at_thrs1']} / {data['recall_at_thrs2']} / {data['recall_at_thrs3']}",
                    })
                else:
                    results_with_dynamic_kp.append({
                        "static_percentage": static_percentage,
                        "dynamic_percentage": 100,
                        "results": f"{data['recall_at_thrs1']} / {data['recall_at_thrs2']} / {data['recall_at_thrs3']}",
                    })
            except yaml.YAMLError as exc:
                print(exc)

# Order list of dictionaries by key.
results_without_dynamic_kp: list = sorted(results_without_dynamic_kp, key=lambda dd: dd['static_percentage'])
results_with_dynamic_kp: list = sorted(results_with_dynamic_kp, key=lambda dd: dd['static_percentage'])

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
