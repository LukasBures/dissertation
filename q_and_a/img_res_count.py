


from PIL import Image
from pprint import pprint

import os
rootdir = "../datasets/aachen/query/day/"

counter = {}
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        pth = os.path.join(subdir, file)

        if not file.endswith("jpg"):
            print(f"Not jpg file: {file}")
            continue

        im = Image.open(pth)
        width, height = im.size

        tag = f"{width}x{height}"
        if tag in counter:
            counter[tag] += 1
        else:
            counter[tag] = 1

pprint(counter)

# only day images
# aachen_v1 = {'1024x768': 255, '1200x1600': 97, '1600x1200': 378, '768x1024': 104}
# all images day + night
# aachen_v1 = {'1024x768': 262, '1200x1600': 110, '1600x1200': 468, '768x1024': 107}

already_at_scale = counter["1200x1600"] + counter["1600x1200"]
will_be_scaled = counter["1024x768"] + counter["768x1024"]

print(f"already_at_scale = {already_at_scale}")
print(f"will_be_scaled = {will_be_scaled}")
print(f"% of already scaled images: {already_at_scale / (already_at_scale + will_be_scaled) * 100:.2f} %")
print(f"% of images that will be scaled: {will_be_scaled / (already_at_scale + will_be_scaled) * 100:.2f} %")




print("*" * 20)
ttl = counter["1200x1600"] + counter["1600x1200"] + counter["1024x768"] + counter["768x1024"]
print(f"total image count: {ttl}, 0.1% = {ttl / 1000.0}")
