#!/bin/bash

# /bin/bash segment_deeplab_v3plus.sh | tee segment_deeplab_v3plus.log

# ---------------------------------------------------------------------------------
# segment DeepLab v3+
source /home/lukas/PycharmProjects/Dissertation/venvDissertation/bin/activate
cd /home/lukas/PycharmProjects/Dissertation/_segmentation/tf-models/research/ || exit

# From tensorflow/models/research/
python deeplab/model_test.py

# From tensorflow/models/research/deeplab
# bash local_test.sh