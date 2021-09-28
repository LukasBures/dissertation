# A set of standard configurations that can be directly selected from the command
# line using their name. Each is a dictionary with the following entries:
#     - output: the name of the feature file that will be generated.
#     - model: the model configuration, as passed to a feature extractor.
#     - preprocessing: how to preprocess the images read from disk.

feature_configs = {
    "superpoint_7scenes": {
        "output": "feats-superpoint-n4096-r1024",
        "model": {
            "name": "superpoint",
            "nms_radius": 3,
            "max_keypoints": 4096,
        },
        "preprocessing": {
            "globs": ["*.color.png"],
            "grayscale": True,
            "resize_max": 1024,
        },
    },
}

# A set of standard configurations that can be directly selected from the command
# line using their name. Each is a dictionary with the following entries:
#     - output: the name of the match file that will be generated.
#     - model: the model configuration, as passed to a feature matcher.
matcher_configs = {
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
