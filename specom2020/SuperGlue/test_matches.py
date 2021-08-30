

import numpy as np

matches_path = "/home/lukas/PycharmProjects/Dissertation/_my/specom2020/SuperGlue/dump_summer_original-spring_original/009874_009874_matches.npz"

try:
    results = np.load(matches_path)
except:
    raise IOError('Cannot load matches .npz file: %s', matches_path)

kpts0, kpts1 = results['keypoints0'], results['keypoints1']
matches, conf = results['matches'], results['match_confidence']



print("afs")