import glob
import random

combos = ["spring_GAN", "fall_GAN", "winter_GAN", "spring_original", "fall_original", "winter_original"]
summer_paths = sorted(glob.glob("/datasets/specom2020/summer_original/*.jpg"))
texts = []

n_samples = 200
idx = random.sample(range(0, len(summer_paths)), n_samples)
idx = sorted(idx)

with open("/datasets/specom2020/selected_idxs.txt", 'w') as f:
    text = ""
    for id in idx:
        text += str(id) + " - " + summer_paths[id] + "\n"
    f.write(text)

for combo in combos:
    print(combo)
    paths = sorted(glob.glob("/home/lukas/PycharmProjects/Dissertation/_my/datasets/specom2020/" + combo + "/*.jpg"))
    text = ""

    for id in idx:
        summer = summer_paths[id]
        for i in idx:
            season = paths[i]
            text += summer + " " + season + "\n"

    with open("/home/lukas/PycharmProjects/Dissertation/_my/datasets/specom2020/summer_original-" + combo + ".txt", 'w') as f:
        f.write(text)
