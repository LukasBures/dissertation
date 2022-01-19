import pickle
import random
from typing import List, Optional

import h5py
import numpy as np


class FeatureFilter:
    """
    Feature filter class.
    """

    def __init__(self, h5_file_path: str, new_h5_file_path: str, segmentations_file: str, dataset_name: str) -> None:
        """
        Constructor.

        :param h5_file_path: Path to the h5 feature path for filtering.
        :param new_h5_file_path: Path to the new h5 file that will be created.
        :param segmentations_file: Pickle file with segmentations.
        :param dataset_name: Dataset name, for deciding how to read pickle data.
        """
        self._segmentations_file: str = segmentations_file
        self._segmentation_data: dict = dict()
        if dataset_name == "aachen":
            with open(self._segmentations_file, "rb") as fl:
                self._segmentation_data = pickle.load(fl)
        else:
            with open(self._segmentations_file, "rb") as fl:
                while True:
                    try:
                        data = pickle.load(fl)
                        for d in data:
                            self._segmentation_data[d] = data[d]
                    except EOFError:
                        break

        self._h5_file_path: str = h5_file_path
        self._new_h5_file_path: str = new_h5_file_path
        self._names: list = self._list_h5_names()

    def _list_h5_names(self) -> list:
        """
        List all names in h5 file.

        :return: List of h5 names.
        """
        names: list = list()
        with h5py.File(str(self._h5_file_path), "r") as fd:

            def visit_fn(_, obj):
                if isinstance(obj, h5py.Dataset):
                    names.append(obj.parent.name.strip("/"))

            fd.visititems(visit_fn)
        return list(set(names))

    def _split_keypoints(
        self, keypoints, image_name: str, image_width: int, image_height: int, dynamic_group_classes=None
    ) -> (List[dict], List[dict]):
        """
        Split keypoints to static and dynamic lists.

        :param keypoints:
        :param image_name: Image name.
        :param image_width: Image width.
        :param image_height: Image height.
        :param dynamic_group_classes: List of d
        :return: Tuple of dynamic and static lists.
        """
        if dynamic_group_classes is None:
            dynamic_group_classes: list = ["vehicle", "human"]

        dynamic_keypoints: List[dict] = list()
        static_keypoints: List[dict] = list()
        all_segmentations: dict = self._segmentation_data[image_name]
        for idx, k in enumerate(keypoints):
            is_k_dynamic: bool = False
            for d in dynamic_group_classes:
                # k[0] = x-axis
                # k[1] = y-axis
                x: int = int(round(k[0]))
                y: int = int(round(k[1]))
                x: int = x if x < image_width else image_width - 1
                y: int = y if y < image_height else image_height - 1
                if all_segmentations[d][y, x] > 0:
                    is_k_dynamic: bool = True
                    dynamic_keypoints.append(
                        {
                            "kp": k,
                            "is_dynamic": is_k_dynamic,
                            "idx": idx,
                        }
                    )
                    break

            if not is_k_dynamic:
                static_keypoints.append(
                    {
                        "kp": k,
                        "is_dynamic": is_k_dynamic,
                        "idx": idx,
                    }
                )

        return dynamic_keypoints, static_keypoints

    def filter_and_update_kp(self, static_percentage_keep, dynamic_percentage_keep) -> Optional[dict]:
        """
        Filter and update keypoints -> reduce number of keypoints.

        :param static_percentage_keep: Percentage of static keypoint to keep.
        :param dynamic_percentage_keep: Percentage of dynamic keypoint to keep.
        :return: Optional dictionary with summary info.
        """
        # Percentage check.
        if static_percentage_keep > 100:
            raise Exception("Static percentage to keep has to be lower or equal to 100%.")
        if dynamic_percentage_keep > 100:
            raise Exception("Dynamic percentage to keep has to be lower or equal to 100%.")

        # Variable initialization.
        total_static_kp_count: int = 0
        total_dynamic_kp_count: int = 0
        kept_static_kp_count: int = 0
        kept_dynamic_kp_count: int = 0

        with h5py.File(str(self._h5_file_path), "r") as source_file:
            with h5py.File(str(self._new_h5_file_path), "w") as destination_file:
                for idx, image_name in enumerate(self._names):
                    keypoints = source_file[image_name]["keypoints"].__array__()
                    descriptors = source_file[image_name]["descriptors"].__array__()
                    scores = source_file[image_name]["scores"].__array__()
                    image_size = source_file[image_name]["image_size"].__array__()

                    # If it is db file - ignore it.
                    if "db" == image_name.split("/")[0]:
                        grp = destination_file.create_group(image_name)
                        grp.create_dataset("keypoints", data=keypoints)
                        grp.create_dataset("descriptors", data=descriptors)
                        grp.create_dataset("scores", data=scores)
                        grp.create_dataset("image_size", data=image_size)
                        continue

                    dynamic, static = self._split_keypoints(
                        keypoints, image_name.split("/")[-1], image_width=image_size[0], image_height=image_size[1]
                    )

                    if static_percentage_keep == 100:
                        keep_static: list = static
                    else:
                        if len(static) > 0:
                            n: int = int(static_percentage_keep / 100.0 * len(static))
                            keep_static: list = random.sample(static, n)
                        else:
                            keep_static: list = list()

                    if dynamic_percentage_keep == 100:
                        keep_dynamic: list = dynamic
                    else:
                        if len(dynamic) > 0:
                            m: int = int(dynamic_percentage_keep / 100.0 * len(dynamic))
                            keep_dynamic: list = random.sample(dynamic, m)
                        else:
                            keep_dynamic: list = list()

                    print(
                        f"{idx + 1}/{len(self._names)}) {image_name.split('/')[-1]} - "
                        f"dynamic: {len(keep_dynamic)}, static: {len(keep_static)}, "
                        f"total: {len(keep_static) + len(keep_dynamic)}/{len(keypoints)}"
                    )

                    kept_static_kp_count += len(keep_static)
                    kept_dynamic_kp_count += len(keep_dynamic)
                    total_static_kp_count += len(static)
                    total_dynamic_kp_count += len(dynamic)

                    kp_info_unsorted: list = keep_static + keep_dynamic
                    kp_info: list = sorted(kp_info_unsorted, key=lambda dt: dt["idx"])
                    new_descriptors: list = list()
                    new_scores: list = list()
                    new_keypoints: list = list()

                    for i, k in enumerate(kp_info):
                        if i == 0:
                            new_descriptors = descriptors[:, k["idx"]]
                        else:
                            new_descriptors = np.vstack([new_descriptors, descriptors[:, k["idx"]]])
                        new_scores.append(scores[k["idx"]])
                        new_keypoints.append(keypoints[k["idx"]])

                    # Write to the new file.
                    grp = destination_file.create_group(image_name)
                    grp.create_dataset("keypoints", data=new_keypoints)
                    grp.create_dataset("descriptors", data=np.swapaxes(new_descriptors, 0, 1))
                    grp.create_dataset("scores", data=np.asarray(new_scores))
                    grp.create_dataset("image_size", data=image_size)

        summary_info: dict = {
            "static_percentage_to_keep": static_percentage_keep,
            "dynamic_percentage_to_keep": dynamic_percentage_keep,
            "total_static_kp_count": total_static_kp_count,
            "total_dynamic_kp_count": total_dynamic_kp_count,
            "kept_static_kp_count": kept_static_kp_count,
            "kept_dynamic_kp_count": kept_dynamic_kp_count,
        }
        print(f"Filter summary info: {summary_info}.")
        return summary_info


if __name__ == "__main__":
    input_file_path = "/data512/dissertation_results/aachen-2021.12.14_18.04.18/results/feats-superpoint-n4096-r1024.h5"
    output_file_path = (
        "/data512/dissertation_results/aachen-2021.12.14_18.04.18/results/test2_feats-superpoint-n4096-r1024.h5"
    )
    input_segmentations_path = "/data512/dissertation_results/aachen_all_v1/segment_nvidia_v01.pkl"
    ff = FeatureFilter(
        h5_file_path=input_file_path,
        new_h5_file_path=output_file_path,
        segmentations_file=input_segmentations_path,
        dataset_name="aachen",
    )
    ff.filter_and_update_kp(static_percentage_keep=50, dynamic_percentage_keep=100)
    print("DONE feature_filter.py")
