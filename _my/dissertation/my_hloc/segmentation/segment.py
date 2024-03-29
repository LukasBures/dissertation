import argparse
import os
from collections import namedtuple

import cv2
import h5py
import numpy as np
from tqdm import tqdm

# Parameters.
parser = argparse.ArgumentParser()
parser.add_argument("--dataset_name", type=str, help="Dataset name.")
parser.add_argument("--path_roots", nargs="+", help="Root folders.")
parser.add_argument("--destination_folder", type=str, help="Dataset name.")
parser.add_argument(
    "--segmentation_classes", nargs="+", help="Segmentation classes.", default=["nature", "sky", "human", "vehicle"]
)
args = parser.parse_args()

print(f"Dataset name: {args.dataset_name}")
print(f"Path roots: {args.path_roots}")
print(f"Destination folder: {args.destination_folder}")
segmentation_classes: list = args.segmentation_classes

filtered_names: list = list()
if "nature" in segmentation_classes:
    filtered_names: list = filtered_names + ["vegetation", "terrain"]
if "sky" in segmentation_classes:
    filtered_names: list = filtered_names + ["sky"]
if "human" in segmentation_classes:
    filtered_names: list = filtered_names + ["person", "rider"]
if "vehicle" in segmentation_classes:
    filtered_names: list = filtered_names + [
        "car",
        "truck",
        "bus",
        "caravan",
        "trailer",
        "train",
        "motorcycle",
        "bicycle",
        "license plate",
    ]
print(f"Filtered names: {filtered_names}")

store_names: list = list()
if "sky" in filtered_names:
    store_names.append("sky")
if "person" in filtered_names:
    store_names.append("human")
if "car" in filtered_names:
    store_names.append("vehicle")
if "vegetation" in filtered_names:
    store_names.append("nature")
store_name = "_".join(store_names)

dataset: str = args.dataset_name
method: str = "segment_nvidia"
version: str = "v01"
DEBUG: bool = False
TEST: bool = False

# ------------------------------------------------------------------------
path_roots: list = args.path_roots
destination_folder: str = args.destination_folder

print(f"Dataset: {dataset}, segmentation method: {method}")
print(f"Image source paths: {path_roots}")
print(f"Segmentation h5 file destination path: {destination_folder}")
os.makedirs(destination_folder, exist_ok=True)

# --------------------------------------------------------------------------------
# Definitions:
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
labels: list = [
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


def mask_it(segmented_img, labels: list, filtered_names: list) -> dict:
    masks: dict = dict()
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


def process_segmentations(
    root_path: str, method: str, labels: list, filtered_names: list, output_file_path: str
) -> None:
    """


    :param root_path:
    :param method:
    :param labels:
    :param filtered_names:
    :return:
    """
    if method == "segment_nvidia":
        with h5py.File(str(output_file_path), "w") as destination_file:
            for file in tqdm(os.listdir(root_path)):
                if file.endswith(".png"):
                    if "_input.png" in file:
                        original_file_name = file.replace("_input.png", "")
                        segmented_img = cv2.imread(
                            os.path.join(root_path, file.replace("_input.png", "_prediction.png"))
                        )
                        masks = mask_it(segmented_img, labels, filtered_names)

                        nature_mask = masks["vegetation"] | masks["terrain"]
                        sky_mask = masks["sky"]
                        human_mask = masks["person"] | masks["rider"]
                        vehicle_mask = (
                            masks["car"]
                            | masks["truck"]
                            | masks["bus"]
                            | masks["caravan"]
                            | masks["trailer"]
                            | masks["train"]
                            | masks["motorcycle"]
                            | masks["bicycle"]
                            | masks["license plate"]
                        )

                        grp = destination_file.create_group(original_file_name)
                        grp.create_dataset("nature", data=nature_mask)
                        grp.create_dataset("sky", data=sky_mask)
                        grp.create_dataset("human", data=human_mask)
                        grp.create_dataset("vehicle", data=vehicle_mask)

                        if DEBUG:
                            original_img = cv2.imread(os.path.join(root_path, file))
                            # masks[f"{original_file_name}.jpg"] = {"original_img": original_img, "segmented_img": segmented_img}
                            # masks[f"{original_file_name}.jpg"].update(masks)
                            cv2.imshow("seg", segmented_img)
                            cv2.imshow("orig", original_img)
                            if cv2.waitKey(0) == ord("n"):
                                print("Next")

                        if TEST:
                            break

                        del segmented_img
                        del masks
                        del nature_mask
                        del sky_mask
                        del human_mask
                        del vehicle_mask
    else:
        raise Exception(f"Unknown method: {method}.")


def process_multiple_segmentations(
    root_paths: list, method: str, labels: list, filtered_names: list, output_file_path: str
) -> None:
    """


    :param root_paths:
    :param method:
    :param labels:
    :param filtered_names:
    :return:
    """
    if method == "segment_nvidia":
        with h5py.File(str(output_file_path), "w") as destination_file:
            for pth in root_paths:
                if "cam0" in pth:
                    cam: str = "cam0"
                elif "cam1" in pth:
                    cam: str = "cam1"
                else:
                    raise Exception(f"Unknown camera: can not get camera number from path: {pth}.")

                # If group does not exist in destination_file - create it
                if cam in destination_file:
                    cam_grp = destination_file[cam]
                else:
                    cam_grp = destination_file.create_group(cam)

                for file in tqdm(os.listdir(pth)):
                    if file.endswith(".png"):
                        if "_input.png" in file:
                            original_file_name = file.replace("_input.png", "")

                            # If group does not exist in destination_file - create it
                            if original_file_name not in cam_grp:
                                segmented_img = cv2.imread(
                                    os.path.join(pth, file.replace("_input.png", "_prediction.png"))
                                )
                                masks = mask_it(segmented_img, labels, filtered_names)
                                grp = cam_grp.create_group(original_file_name)

                                if "nature" in segmentation_classes:
                                    nature_mask = masks["vegetation"] | masks["terrain"]
                                    grp.create_dataset("nature", data=nature_mask)
                                    del nature_mask

                                if "sky" in segmentation_classes:
                                    sky_mask = masks["sky"]
                                    grp.create_dataset("sky", data=sky_mask)
                                    del sky_mask

                                if "human" in segmentation_classes:
                                    human_mask = masks["person"] | masks["rider"]
                                    grp.create_dataset("human", data=human_mask)
                                    del human_mask

                                if "vehicle" in segmentation_classes:
                                    vehicle_mask = (
                                        masks["car"]
                                        | masks["truck"]
                                        | masks["bus"]
                                        | masks["caravan"]
                                        | masks["trailer"]
                                        | masks["train"]
                                        | masks["motorcycle"]
                                        | masks["bicycle"]
                                        | masks["license plate"]
                                    )
                                    grp.create_dataset("vehicle", data=vehicle_mask)
                                    del vehicle_mask

                                del segmented_img
                                del masks

    else:
        raise Exception(f"Unknown method: {method}.")


print("Segmenting ...")
output_file_path: str = f"{destination_folder}/{method}_{dataset}_{version}.h5"
if len(path_roots) == 1:
    process_segmentations(path_roots[0], method, labels, filtered_names, output_file_path)
else:
    process_multiple_segmentations(path_roots, method, labels, filtered_names, output_file_path)

print("DONE segment.py")
