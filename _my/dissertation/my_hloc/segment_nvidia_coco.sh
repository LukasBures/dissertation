#!/bin/bash

# /bin/bash segment_nvidia_coco.sh | tee segment_nvidia_coco.log


export CUDA_DEVICE_ORDER=PCI_BUS_ID
# 1080 = 0
# 1080Ti = 1
export CUDA_VISIBLE_DEVICES=0

# ---------------------------------------------------------------------------------
# segment NVIDIA
source /home/lukas/PycharmProjects/Dissertation/venvDissertation/bin/activate
cd /home/lukas/PycharmProjects/Dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit 1
export OMP_NUM_THREADS=3
echo "Starting segmentation: coco val"
python -m runx.runx scripts/coco_dump_val.yml -i
echo "Starting segmentation: coco train"
python -m runx.runx scripts/coco_dump_train.yml -i
echo "DONE"
