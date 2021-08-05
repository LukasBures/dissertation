#!/bin/bash

# /bin/bash segment_resnest.sh | tee segment_resnest.log

# ---------------------------------------------------------------------------------
# segment ResNeSt https://github.com/zhanghang1989/ResNeSt
# https://hangzhang.org/PyTorch-Encoding/model_zoo/segmentation.html
# PyTorch-Encoding - v projektu

source /home/lukas/PycharmProjects/Dissertation/venvDissertation/bin/activate
cd /home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc/ || exit
python segment_model.py
