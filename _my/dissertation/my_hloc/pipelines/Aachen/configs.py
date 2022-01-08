# A set of standard configurations that can be directly selected from the command
# line using their name. Each is a dictionary with the following entries:
#     - output: the name of the feature file that will be generated.
#     - model: the model configuration, as passed to a feature extractor.
#     - preprocessing: how to preprocess the images read from disk.

retrieval_configs = {
    "netvlad": {
        "output": "global-feats-netvlad",
        "model": {
            "name": "netvlad",
        },
        "preprocessing": {
            "resize_max": 1024,
        },
    },
}

feature_configs = {
    "superpoint_fast": {
        "output": "feats-superpoint-n4096-r1024",
        "model": {
            "name": "superpoint",
            "nms_radius": 3,
            "max_keypoints": 1024,
        },
        "preprocessing": {
            "grayscale": True,
            "resize_max": 1024,
        },
    },
    "superpoint_aachen": {
        "output": "feats-superpoint-n4096-r1024",
        "model": {
            "name": "superpoint",
            "nms_radius": 3,
            "max_keypoints": 4096,
        },
        "preprocessing": {
            "grayscale": True,
            "resize_max": 1024,
        },
    },
    # Resize images to 1600px even if they are originally smaller.
    # Improves the keypoint localization if the images are of good quality.
    "superpoint_max": {
        "output": "feats-superpoint-n4096-rmax1600",
        "model": {
            "name": "superpoint",
            "nms_radius": 3,
            "max_keypoints": 4096,
        },
        "preprocessing": {
            "grayscale": True,
            "resize_max": 1600,
            "resize_force": True,
        },
    },
    "superpoint_inloc": {
        "output": "feats-superpoint-n4096-r1600",
        "model": {
            "name": "superpoint",
            "nms_radius": 4,
            "max_keypoints": 4096,
        },
        "preprocessing": {
            "grayscale": True,
            "resize_max": 1600,
        },
    },
    "d2net-ss": {
        "output": "feats-d2net-ss",
        "model": {
            "name": "d2net",
            "multiscale": False,
        },
        "preprocessing": {
            "grayscale": False,
            "resize_max": 1600,
        },
    },
    "sift": {
        "output": "feats-sift",
        "model": {"name": "sift"},
        "preprocessing": {
            "grayscale": True,
            "resize_max": 1600,
        },
    },
    "dir": {
        "output": "global-feats-dir",
        "model": {
            "name": "dir",
        },
        "preprocessing": {
            "resize_max": 1024,
        },
    },
}


# A set of standard configurations that can be directly selected from the command
# line using their name. Each is a dictionary with the following entries:
#     - output: the name of the match file that will be generated.
#     - model: the model configuration, as passed to a feature matcher.
matcher_configs = {
    "superglue_fast": {
        "output": "matches-superglue",
        "model": {
            "name": "superglue",
            "weights": "outdoor",
            "sinkhorn_iterations": 5,
        },
    },
    "superglue": {
        "output": "matches-superglue",
        "model": {
            "name": "superglue",
            "weights": "outdoor",
            "sinkhorn_iterations": 50,
        },
    },
    "NN-superpoint": {
        "output": "matches-NN-mutual-dist.7",
        "model": {
            "name": "nearest_neighbor",
            "do_mutual_check": True,
            "distance_threshold": 0.7,
        },
    },
    "NN-ratio": {
        "output": "matches-NN-mutual-ratio.8",
        "model": {
            "name": "nearest_neighbor",
            "do_mutual_check": True,
            "ratio_threshold": 0.8,
        },
    },
    "NN-mutual": {
        "output": "matches-NN-mutual",
        "model": {
            "name": "nearest_neighbor",
            "do_mutual_check": True,
        },
    },
}
