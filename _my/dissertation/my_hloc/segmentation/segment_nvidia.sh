#!/bin/bash

# /bin/bash segment_nvidia.sh | tee segment_nvidia.log
. /home/lukas/PycharmProjects/dissertation/.venv/bin/activate

DATASET_NAME="aachen_v1_1"

# ---------------------------------------------------------------------------------
# Segment NVIDIA
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
python -m runx.runx scripts/aachen_dump_all_v1.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# ---------------------------------------------------------------------------------
# Create pickle file
echo "Starting creating pickle file plus grouping segmentations ..."
cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/ || exit
python segment.py
echo "DONE saved to pickle ..."

# ---------------------------------------------------------------------------------
echo "ALL DONE"
