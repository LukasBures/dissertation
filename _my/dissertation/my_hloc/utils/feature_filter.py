import random
from typing import List, Optional

import h5py
import numpy as np


class FeatureFilter:
    """
    Feature filter class.
    """

    def __init__(
        self,
        h5_file_path: str,
        new_h5_file_path: str,
        segmentation_h5_file_path: str,
        dynamic_group_classes: list = None,
    ) -> None:
        """
        Constructor.

        :param h5_file_path: Path to the h5 feature path for filtering.
        :param new_h5_file_path: Path to the new h5 file that will be created.
        :param segmentation_h5_file_path: Path to the h5 file with segmentations.
        :param dynamic_group_classes: List of dynamic group of classes, can contain: vehicle, human, sky, and nature.
        """
        self._h5_file_path: str = str(h5_file_path)
        self._new_h5_file_path: str = str(new_h5_file_path)
        self._segmentation_h5_file_path: str = str(segmentation_h5_file_path)
        if dynamic_group_classes is None:
            self._dynamic_group_classes: list = ["vehicle", "human"]
        else:
            self._dynamic_group_classes: list = dynamic_group_classes
        self._names: list = self._list_h5_names()

    def _list_h5_names(self) -> list:
        """
        List all names in h5 file.

        :return: List of h5 names.
        """
        names: list = list()
        with h5py.File(self._h5_file_path, "r") as fd:

            def visit_fn(_, obj):
                if isinstance(obj, h5py.Dataset):
                    names.append(obj.parent.name.strip("/"))

            fd.visititems(visit_fn)
        return list(set(names))

    @staticmethod
    def _split_keypoints(
        keypoints, segmentations: list, image_width: int, image_height: int
    ) -> (List[dict], List[dict]):
        """
        Split keypoints to static and dynamic lists.

        :param keypoints: Keypoints in the image.
        :param segmentations: Selected segmentations from pre-calculated h5 file.
        :param image_width: Image width.
        :param image_height: Image height.
        :return: Tuple of dynamic and static lists.
        """

        dynamic_keypoints: List[dict] = list()
        static_keypoints: List[dict] = list()
        for idx, k in enumerate(keypoints):
            is_k_dynamic: bool = False
            for segmentation in segmentations:
                # k[0] = x-axis
                # k[1] = y-axis
                x: int = int(round(k[0]))
                y: int = int(round(k[1]))
                x: int = x if x < image_width else image_width - 1
                y: int = y if y < image_height else image_height - 1
                if segmentation[y, x] > 0:
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

    def filter_and_update_kp(self, static_percentage_keep, dynamic_percentage_keep) -> Optional[dict]:  # noqa: C901
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

        with h5py.File(self._h5_file_path, "r") as source_file:
            with h5py.File(self._new_h5_file_path, "w") as destination_file:
                with h5py.File(self._segmentation_h5_file_path, "r") as segmentation_file:
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

                        img_name: str = image_name.split("/")[-1].split(".")[0]
                        segmentations: list = list()
                        for d in self._dynamic_group_classes:
                            segmentations.append(segmentation_file[img_name][d].__array__())
                        dynamic, static = self._split_keypoints(
                            keypoints=keypoints,
                            segmentations=segmentations,
                            image_width=image_size[0],
                            image_height=image_size[1],
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
                                new_descriptors: np.ndarray = np.vstack([new_descriptors, descriptors[:, k["idx"]]])
                            new_scores.append(scores[k["idx"]])
                            new_keypoints.append(keypoints[k["idx"]])

                        if new_descriptors:
                            new_descriptors: np.ndarray = np.swapaxes(new_descriptors, 0, 1)
                        else:
                            new_descriptors: np.ndarray = np.asarray(new_descriptors)

                        # Write to the new file.
                        grp = destination_file.create_group(image_name)
                        grp.create_dataset("keypoints", data=new_keypoints)
                        grp.create_dataset("descriptors", data=new_descriptors)
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
    input_segmentations_file_path = "/data512/dissertation_results/aachen_all_v1/segment_nvidia_v01.h5"
    ff = FeatureFilter(
        h5_file_path=input_file_path,
        new_h5_file_path=output_file_path,
        segmentation_h5_file_path=input_segmentations_file_path,
    )
    ff.filter_and_update_kp(static_percentage_keep=50, dynamic_percentage_keep=100)
    print("DONE feature_filter.py")
