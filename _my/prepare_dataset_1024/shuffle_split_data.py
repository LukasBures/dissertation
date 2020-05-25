import json
from sklearn.model_selection import train_test_split
import os
import fnmatch
from datetime import date
import os

data_path = "../datasets/nordlandsbanen_imgs/"
seasons = ["spring", "summer", "fall", "winter"]
split = "split3"
out_path = "../datasets/nordlandsbanen_imgs/" + split

ratio_train = 0.6
ratio_test = 0.2
ratio_val = 0.2
today = date.today()

if not os.path.exists(out_path):
    os.makedirs(out_path)

for s in seasons:
    data = list()
    for file in os.listdir(data_path + s):
        if fnmatch.fnmatch(file, '*.jpg'):
            data.append("/home/lukas/PycharmProjects/Dissertation/_my/datasets/nordlandsbanen_imgs/" + s + "/" + file)

    data.sort()

    data_train, data_tmp = train_test_split(data, train_size=0.6, test_size=0.4, random_state=1, shuffle=True)
    data_test, data_val = train_test_split(data_tmp, train_size=0.5, test_size=0.5, random_state=1, shuffle=True)

    print(s, "train", len(data_train), ", test", len(data_test), ", val", len(data_val))

    json_data = {
        'data_train': data_train,
        'data_test': data_test,
        'data_val': data_val,
        'date': today.strftime("%d/%m/%Y"),
        'ratio_train': ratio_train,
        'ratio_test': ratio_test,
        'ratio_val': ratio_val
    }

    with open(out_path + "/" + s + ".json", 'w') as outfile:
        json.dump(json_data, outfile)


