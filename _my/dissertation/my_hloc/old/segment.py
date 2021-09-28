import argparse
import os
import pickle
from collections import namedtuple
from pathlib import Path

import cv2
import h5py
import numpy as np
import torch
from tqdm import tqdm

nature = ["vegetation", "terrain"]
sky = ["sky"]
human = ["person", "rider"]
vehicle = ["car", "truck", "bus", "caravan", "trailer", "train", "motorcycle", "bicycle", "license plate"]
#  sky + human + vehicle + nature
filtered_names = nature
print(f"Filtered names: {filtered_names}")

store_names = []
if "sky" in filtered_names:
    store_names.append("sky")
if "person" in filtered_names:
    store_names.append("human")
if "car" in filtered_names:
    store_names.append("vehicle")
if "vegetation" in filtered_names:
    store_names.append("nature")
store_name = "_".join(store_names)

dataset = "aachen"
method = "segment_nvidia"
day = True
toPickle = False
DEBUG = False
TEST = True
# ------------------------------------------------------------------------

if day:
    dn = "day"
elif not day:
    dn = "night"

if TEST:
    dn = "test"


path_root = (
    f"/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc/logs/{dataset}/{method}/{dn}/best_images"
)
print(f"Dataset: {dataset}, segmentation method:{method}, time: {dn}")
output_dst_root = (
    f"/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc/logs/{dataset}/{method}/{dn}/{store_name}"
)
pickle_output_dst_root = (
    f"/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc/logs/{dataset}/{method}/{dn}"
)
os.makedirs(output_dst_root, exist_ok=True)


# --------------------------------------------------------------------------------
# Definitions
# --------------------------------------------------------------------------------
# a label and all meta information
Label = namedtuple(
    "Label",
    [
        "name",  # The identifier of this label, e.g. 'car', 'person', ... .
        # We use them to uniquely name a class
        "id",  # An integer ID that is associated with this label.
        # The IDs are used to represent the label in ground truth images
        # An ID of -1 means that this label does not have an ID and thus
        # is ignored when creating ground truth images (e.g. license plate).
        # Do not modify these IDs, since exactly these IDs are expected by the
        # evaluation server.
        "trainId",  # Feel free to modify these IDs as suitable for your method. Then create
        # ground truth images with train IDs, using the tools provided in the
        # 'preparation' folder. However, make sure to validate or submit results
        # to our evaluation server using the regular IDs above!
        # For trainIds, multiple labels might have the same ID. Then, these labels
        # are mapped to the same class in the ground truth images. For the inverse
        # mapping, we use the label that is defined first in the list below.
        # For example, mapping all void-type classes to the same ID in training,
        # might make sense for some approaches.
        # Max value is 255!
        "category",  # The name of the category that this label belongs to
        "categoryId",  # The ID of this category. Used to create ground truth images
        # on category level.
        "hasInstances",  # Whether this label distinguishes between single instances or not
        "ignoreInEval",  # Whether pixels having this class as ground truth label are ignored
        # during evaluations or not
        "color",  # The color of this label
    ],
)


# --------------------------------------------------------------------------------
# A list of all labels
# --------------------------------------------------------------------------------

# Please adapt the train IDs as appropriate for your approach.
# Note that you might want to ignore labels with ID 255 during training.
# Further note that the current train IDs are only a suggestion. You can use whatever you like.
# Make sure to provide your results using the original IDs and not the training IDs.
# Note that many IDs are ignored in evaluation and thus you never need to predict these!
labels = [
    #       name                     id    trainId   category            catId     hasInstances   ignoreInEval   color
    Label("unlabeled", 0, 255, "void", 0, False, True, (0, 0, 0)),
    Label("ego vehicle", 1, 255, "void", 0, False, True, (0, 0, 0)),
    Label("rectification border", 2, 255, "void", 0, False, True, (0, 0, 0)),
    Label("out of roi", 3, 255, "void", 0, False, True, (0, 0, 0)),
    Label("static", 4, 255, "void", 0, False, True, (0, 0, 0)),
    Label("dynamic", 5, 255, "void", 0, False, True, (111, 74, 0)),
    Label("ground", 6, 255, "void", 0, False, True, (81, 0, 81)),
    Label("road", 7, 0, "flat", 1, False, False, (128, 64, 128)),
    Label("sidewalk", 8, 1, "flat", 1, False, False, (244, 35, 232)),
    Label("parking", 9, 255, "flat", 1, False, True, (250, 170, 160)),
    Label("rail track", 10, 255, "flat", 1, False, True, (230, 150, 140)),
    Label("building", 11, 2, "construction", 2, False, False, (70, 70, 70)),
    Label("wall", 12, 3, "construction", 2, False, False, (102, 102, 156)),
    Label("fence", 13, 4, "construction", 2, False, False, (190, 153, 153)),
    Label("guard rail", 14, 255, "construction", 2, False, True, (180, 165, 180)),
    Label("bridge", 15, 255, "construction", 2, False, True, (150, 100, 100)),
    Label("tunnel", 16, 255, "construction", 2, False, True, (150, 120, 90)),
    Label("pole", 17, 5, "object", 3, False, False, (153, 153, 153)),
    Label("polegroup", 18, 255, "object", 3, False, True, (153, 153, 153)),
    Label("traffic light", 19, 6, "object", 3, False, False, (250, 170, 30)),
    Label("traffic sign", 20, 7, "object", 3, False, False, (220, 220, 0)),
    Label("vegetation", 21, 8, "nature", 4, False, False, (107, 142, 35)),
    Label("terrain", 22, 9, "nature", 4, False, False, (152, 251, 152)),
    Label("sky", 23, 10, "sky", 5, False, False, (70, 130, 180)),
    Label("person", 24, 11, "human", 6, True, False, (220, 20, 60)),
    Label("rider", 25, 12, "human", 6, True, False, (255, 0, 0)),
    Label("car", 26, 13, "vehicle", 7, True, False, (0, 0, 142)),
    Label("truck", 27, 14, "vehicle", 7, True, False, (0, 0, 70)),
    Label("bus", 28, 15, "vehicle", 7, True, False, (0, 60, 100)),
    Label("caravan", 29, 255, "vehicle", 7, True, True, (0, 0, 90)),
    Label("trailer", 30, 255, "vehicle", 7, True, True, (0, 0, 110)),
    Label("train", 31, 16, "vehicle", 7, True, False, (0, 80, 100)),
    Label("motorcycle", 32, 17, "vehicle", 7, True, False, (0, 0, 230)),
    Label("bicycle", 33, 18, "vehicle", 7, True, False, (119, 11, 32)),
    Label("license plate", -1, -1, "vehicle", 7, False, True, (0, 0, 142)),
]
# ------------------------------------------------------------------------


def mask_it(segmented_img, labels, filtered_names):
    masks = {}
    total_mask = None
    for nm in filtered_names:
        for label in labels:
            if label.name is nm:
                clr = np.array(label.color)
                clr = clr[[2, 1, 0]]  # RGB to BGR
                # print(f"was {np.array(label.color)}, new {clr}")
                masks[nm] = cv2.inRange(segmented_img, clr, clr)
                # mask = cv2.inRange(segmented_img, clr, clr)
                # masks[nm] = cv2.bitwise_and(segmented_img, segmented_img, mask=mask)
                # if DEBUG:
                #     cv2.imshow("segmented_img", segmented_img)
                #     cv2.imshow("mask", mask)
                #     cv2.imshow("masked", masks[nm])
                #     if cv2.waitKey(0) == ord('n'):
                #         print("Next")
                break
        if total_mask is None:
            total_mask = masks[nm]
        else:
            total_mask = total_mask | masks[nm]
    masks["total_mask"] = total_mask
    # cv2.imshow("total_mask", cv2.bitwise_and(segmented_img, segmented_img, mask=total_mask))
    # if cv2.waitKey(0) == ord('n'):
    #     pass

    return masks


def load_segmentations(pth, method, labels, filtered_names):
    dts = {}
    if method is "segment_nvidia":
        for file in os.listdir(pth):
            if file.endswith(".png"):
                if "_input.png" in file:
                    print("Processing: ", file)
                    original_file_name = file.replace("_input.png", "")
                    original_img = cv2.imread(os.path.join(pth, file))
                    segmented_img = cv2.imread(os.path.join(pth, file.replace("_input.png", "_prediction.png")))

                    masks = mask_it(segmented_img, labels, filtered_names)
                    dts[f"{original_file_name}.jpg"] = {"original_img": original_img, "segmented_img": segmented_img}
                    dts[f"{original_file_name}.jpg"].update(masks)

                    if toPickle:
                        tmp_dts = dts
                        foo = dict()
                        foo[f"{original_file_name}.jpg"] = {
                            "nature": tmp_dts[f"{original_file_name}.jpg"]["vegetation"]
                            | tmp_dts[f"{original_file_name}.jpg"]["terrain"]
                        }
                        foo[f"{original_file_name}.jpg"].update({"sky": tmp_dts[f"{original_file_name}.jpg"]["sky"]})
                        foo[f"{original_file_name}.jpg"].update(
                            {
                                "human": tmp_dts[f"{original_file_name}.jpg"]["person"]
                                | tmp_dts[f"{original_file_name}.jpg"]["rider"]
                            }
                        )
                        foo[f"{original_file_name}.jpg"].update(
                            {
                                "vehicle": tmp_dts[f"{original_file_name}.jpg"]["car"]
                                | tmp_dts[f"{original_file_name}.jpg"]["truck"]
                                | tmp_dts[f"{original_file_name}.jpg"]["bus"]
                                | tmp_dts[f"{original_file_name}.jpg"]["caravan"]
                                | tmp_dts[f"{original_file_name}.jpg"]["trailer"]
                                | tmp_dts[f"{original_file_name}.jpg"]["train"]
                                | tmp_dts[f"{original_file_name}.jpg"]["motorcycle"]
                                | tmp_dts[f"{original_file_name}.jpg"]["bicycle"]
                                | tmp_dts[f"{original_file_name}.jpg"]["license plate"]
                            }
                        )
                        dts.update(foo)

                    if DEBUG:
                        cv2.imshow("seg", segmented_img)
                        cv2.imshow("orig", original_img)
                        if cv2.waitKey(0) == ord("n"):
                            print("Next")
                    # # todo: remove this break - just for debug purpose
                    # break
    else:
        assert "Unknown method"
    return dts


def save_segmentations(segmentations, pth):
    for key in segmentations:
        cv2.imwrite(f"{pth}/{key}", segmentations[key]["total_mask"])


def save_segmentations_to_pickle(segmentations, pth):
    with open(pth, "wb") as f:
        pickle.dump(segmentations, f)


print("Segmenting")
segmentations = load_segmentations(path_root, method, labels, filtered_names)
print("Saving")
save_segmentations(segmentations, output_dst_root)
save_segmentations_to_pickle(segmentations, f"{pickle_output_dst_root}/{method}.pkl")

print("DONE")
