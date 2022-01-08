#!/bin/bash

# /bin/bash segment_nvidia.sh | tee segment_nvidia.log
. /home/lukas/PycharmProjects/dissertation/.venv/bin/activate

# ---------------------------------------------------------------------------------
# Segment NVIDIA
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit
export OMP_NUM_THREADS=3
echo "Starting segmentation: aachen v1 ..."
python -m runx.runx scripts/aachen_dump_all_v1.yml -i
echo "DONE segmentation ..."

# ---------------------------------------------------------------------------------
# Create pickle file
echo "Starting creating pickle file plus grouping segmentations ..."
cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/ || exit
python segment.py
echo "DONE"
