from tqdm import tqdm
import h5py
import numpy as np
import random
import pickle
from typing import List


class FeatureFilter:
    def __init__(self, h5_file_path: str, new_h5_file_path: str, segmentations_file: str = None) -> None:
        if segmentations_file:
            self._segmentations_file: str = segmentations_file
        else:
            self._segmentations_file: str = "/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/aachen_all_v1/segment_nvidia_v01.pkl"
        with open(self._segmentations_file, "rb") as fl:
            self._segmentation_data = pickle.load(fl)

        self._h5_file_path: str = h5_file_path
        self._new_h5_file_path: str = new_h5_file_path
        self._names: list = self._list_h5_names()

    def _list_h5_names(self) -> list:
        names: list = list()
        with h5py.File(str(self._h5_file_path), 'r') as fd:
            def visit_fn(_, obj):
                if isinstance(obj, h5py.Dataset):
                    names.append(obj.parent.name.strip('/'))

            fd.visititems(visit_fn)
        return list(set(names))

    def _split_keypoints(
            self, keypoints, image_name: str, image_width: int, image_height: int, dynamic_group_classes=None
    ) -> (List[dict], List[dict]):
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
                    dynamic_keypoints.append({
                        "kp": k,
                        "is_dynamic": is_k_dynamic,
                        "idx": idx,
                    })
                    break

            static_keypoints.append({
                "kp": k,
                "is_dynamic": is_k_dynamic,
                "idx": idx,
            })

        return dynamic_keypoints, static_keypoints

    def filter_and_update(self, static_percentage_keep, dynamic_percentage_keep) -> dict:
        # Percentage check
        if static_percentage_keep > 100:
            raise Exception("Static percentage to keep has to be lower or equal to 100%.")
        if dynamic_percentage_keep > 100:
            raise Exception("Dynamic percentage to keep has to be lower or equal to 100%.")

        total_static_kp_count: int = 0
        total_dynamic_kp_count: int = 0
        kept_static_kp_count: int = 0
        kept_dynamic_kp_count: int = 0

        source_file = h5py.File(str(self._h5_file_path), "r")
        destination_file = h5py.File(str(self._new_h5_file_path), "w")
        for image_name in tqdm(self._names):
            keypoints = source_file[image_name]["keypoints"].__array__()
            descriptors = source_file[image_name]["descriptors"].__array__()
            scores = source_file[image_name]["scores"].__array__()
            image_size = source_file[image_name]["image_size"].__array__()

            dynamic, static = self._split_keypoints(
                keypoints, image_name.split("/")[-1], image_width=image_size[0], image_height=image_size[1]
            )

            if static_percentage_keep == 100:
                keep_static = static
            else:
                n = int(static_percentage_keep / 100.0 * len(static))
                keep_static = random.sample(static, n)

            if dynamic_percentage_keep == 100:
                keep_dynamic = dynamic
            else:
                m = int(dynamic_percentage_keep / 100.0 * len(dynamic))
                keep_dynamic = random.sample(dynamic, m)

            kept_static_kp_count += len(keep_static)
            kept_dynamic_kp_count += len(keep_dynamic)
            total_static_kp_count += len(static)
            total_dynamic_kp_count += len(dynamic)

            kp_info: list = keep_static + keep_dynamic
            new_descriptors: list = list()
            new_scores: list = list()
            new_keypoints: list = list()

            for k in kp_info:
                new_descriptors.append(descriptors[:, k["idx"]])
                new_scores.append(scores[k["idx"]])
                new_keypoints.append(keypoints[k["idx"]])

            # Write to new file.
            grp = destination_file.create_group(image_name)
            grp.create_dataset("keypoints", data=new_keypoints)
            grp.create_dataset("descriptors", data=np.asarray(new_descriptors).T)
            grp.create_dataset("scores", data=np.asarray(new_scores))
            grp.create_dataset("image_size", data=image_size)

        source_file.close()
        destination_file.close()

        summary_info: dict = {
            "static_percentage_to_keep": static_percentage_keep,
            "dynamic_percentage_to_keep": dynamic_percentage_keep,
            "total_static_kp_count": total_static_kp_count,
            "total_dynamic_kp_count": total_dynamic_kp_count,
            "kept_static_kp_count": kept_static_kp_count,
            "kept_dynamic_kp_count": kept_dynamic_kp_count,
        }
        return summary_info


if __name__ == "__main__":
    file_name = "/media/lukas/WD_2TB/dissertation/aachen-2021.12.07_07.51.52/results/feats-superpoint-n4096-r1024.h5"
    new_h5_file_path = "/media/lukas/WD_2TB/dissertation/aachen-2021.12.07_07.51.52/results/new_feats-superpoint-n4096-r1024.h5"
    ff = FeatureFilter(h5_file_path=file_name, new_h5_file_path=new_h5_file_path)
    new_kps = ff.filter_and_update(static_percentage_keep=50, dynamic_percentage_keep=100)

    print("DONE filter_features.py")
