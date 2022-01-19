import os
from collections import namedtuple
import pickle
import cv2
import h5py
import numpy as np
from tqdm import tqdm

nature: list = ["vegetation", "terrain"]
sky: list = ["sky"]
human: list = ["person", "rider"]
vehicle: list = ["car", "truck", "bus", "caravan", "trailer", "train", "motorcycle", "bicycle", "license plate"]
filtered_names: list = sky + human + vehicle + nature
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

dataset: str = "aachen"
method: str = "segment_nvidia"
version: str = "v01"
DEBUG: bool = False
TEST: bool = False

# ------------------------------------------------------------------------
# TODO: Implement arg parser.

# aachen
path_root: str = "/media/lukas/WD_2TB/dissertation/aachen_all_v1/best_images"
destination_folder: str = "/data512/dissertation_results/aachen_all_v1"

# aachen v1.1
# path_root: str = (
#     "/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/aachen_all_v1_1/best_images"
# )
# destination_folder: str = "/data512/dissertation_results/aachen_all_v1_1"

print(f"Dataset: {dataset}, segmentation method: {method}")
output_dst_root: str = f"{destination_folder}/{store_name}"
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


def process_segmentations(pth: str, method: str, labels: list, filtered_names: list, output_file_path: str) -> None:
    """


    :param pth:
    :param method:
    :param labels:
    :param filtered_names:
    :return:
    """
    output_data: dict = dict()
    if method is "segment_nvidia":
        with h5py.File(str(output_file_path), "w") as destination_file:
            for file in tqdm(os.listdir(pth)):
                if file.endswith(".png"):
                    if "_input.png" in file:
                        # print("Processing: ", file)
                        original_file_name = file.replace("_input.png", "")
                        segmented_img = cv2.imread(os.path.join(pth, file.replace("_input.png", "_prediction.png")))
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

                        # selected_segmentations: dict = {
                        #     "nature": nature_mask,
                        #     "sky": sky_mask,
                        #     "human": human_mask,
                        #     "vehicle": vehicle_mask,
                        # }
                        # pickle.dump({f"{original_file_name}": selected_segmentations}, flw, pickle.HIGHEST_PROTOCOL)
                        # output_data[f"{original_file_name}.jpg"] = selected_segmentations

                        if DEBUG:
                            original_img = cv2.imread(os.path.join(pth, file))
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
                        # del selected_segmentations
    else:
        raise Exception(f"Unknown method: {method}.")


def save_segmentations(segmentations, pth) -> None:
    """


    :param segmentations:
    :param pth:
    :return:
    """
    for key in segmentations:
        cv2.imwrite(f"{pth}/{key}", segmentations[key]["total_mask"])


def save_segmentations_to_pickle(data: dict, pth: str) -> None:
    """


    :param data:
    :param pth:
    :return:
    """
    with open(pth, "wb") as flw:
        pickle.dump(data, flw)


print("Segmenting ...")
output_file_path: str = f"{destination_folder}/{method}_{version}.h5"
process_segmentations(path_root, method, labels, filtered_names, output_file_path)

# print("Saving ...")
# if to_pickle:
#     save_segmentations_to_pickle(segmentations, f"{pickle_output_dst_root}/{method}_{version}.pkl")
# else:
#     save_segmentations(segmentations, output_dst_root)

print("DONE segment.py")
