import matplotlib.pyplot as plt


aachen_test = [
    {
        "static_percentage": 50,
        "dynamic_percentage": 100,
        "day": [89.7, 95.8, 98.7],
        "night": [87.8, 94.9, 100.0],
    },
    {
        "static_percentage": 60,
        "dynamic_percentage": 100,
        "day": [89.7, 95.8, 98.7],
        "night": [87.8, 94.9, 100.0],
    },
    {
        "static_percentage": 70,
        "dynamic_percentage": 100,
        "day": [89.7, 95.8, 98.7],
        "night": [87.8, 94.9, 100.0],
    },
    {
        "static_percentage": 80,
        "dynamic_percentage": 100,
        "day": [89.7, 95.8, 98.7],
        "night": [87.8, 94.9, 100.0],
    },
    {
        "static_percentage": 90,
        "dynamic_percentage": 100,
        "day": [89.7, 95.8, 98.7],
        "night": [87.8, 94.9, 100.0],
    },
    {
        "static_percentage": 100,
        "dynamic_percentage": 100,
        "day": [89.7, 95.8, 98.7],
        "night": [87.8, 94.9, 100.0],
    },
]

aachen = [aachen_test]

for a in aachen:
    x_static: list = list()
    x_dynamic: list = list()
    y_day: list = list()
    y_night: list = list()
    for x in a:
        x_static.append(x["static_percentage"])
        x_dynamic.append(x["dynamic_percentage"])
        y_day.append(x["day"])
        y_night.append(x["night"])

    plt.plot(x_static, y_day)
    plt.title("Static % at day.")
    plt.xlabel("Static keypoints [%].")
    plt.ylabel("Accuracy [%]")
    plt.legend(["0.25m, 2°", "0.50m, 5°", "5.00m, 10°"], title="Conditions")
    plt.show()

    plt.plot(x_static, y_night)
    plt.title("Static % at night.")
    plt.xlabel("Static keypoints [%].")
    plt.ylabel("Accuracy [%].")
    plt.legend(["0.25m, 2°", "0.50m, 5°", "5.00m, 10°"], title="Conditions")
    plt.show()

print("DONE")
