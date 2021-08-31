from itertools import combinations
import json

if __name__ == "__main__":
    arr = ["human", "nature", "sky", "vehicle"]

    method_name = "superpoint_n2048_r1024_seg_nvidia"

    # Model
    model_name = 'superpoint'
    nms_radius = 3
    keypoint_threshold = 0.02
    max_keypoints = 2048

    # Preprocessing
    grayscale = True
    resize_max = 1024
    resize_force = False  # was True

    # Segmentation
    path_to_segmentations = '/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc/logs/aachen/segment_nvidia/day/segment_nvidia.pkl'

    all_conf = {}
    cnt = 0
    names = []
    for idx in range(1, 5):
        combo = list(combinations(arr, idx))
        for c in combo:
            conf = dict()
            name = f"{method_name}_{''.join([l[0] for l in list(c)])}"
            conf[name] = {'output': f'feats-superpoint-n{max_keypoints}-rmax{resize_max}'}
            conf[name].update({'model': {'name': model_name, 'nms_radius': nms_radius, 'keypoint_threshold': keypoint_threshold, 'max_keypoints': max_keypoints}})
            if resize_force:
                conf[name].update({'preprocessing': {'grayscale': grayscale, 'resize_max': resize_max, 'resize_force': resize_force}})
            else:
                conf[name].update({'preprocessing': {'grayscale': grayscale, 'resize_max': resize_max}})
            conf[name].update({'segmentation': {'path_to_segmentations': path_to_segmentations, 'groups': list(c)}})
            all_conf.update(conf)
            names.append(name)
            cnt += 1
    print(json.dumps(all_conf, indent=4, sort_keys=False).replace(": true", ": True").replace(": false", ": False"))
    print(f"\nNumber of combinations = {cnt}")
    print("\n".join(names))
    print("\nDONE")
