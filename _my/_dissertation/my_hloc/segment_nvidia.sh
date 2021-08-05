#!/bin/bash

# /bin/bash segment_nvidia.sh | tee segment_nvidia.log

# ---------------------------------------------------------------------------------
# segment NVIDIA
source /home/lukas/PycharmProjects/Dissertation/venvDissertation/bin/activate
cd /home/lukas/PycharmProjects/Dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit
export OMP_NUM_THREADS=3
echo "Starting segmentation: aachen day queries"
python -m runx.runx scripts/aachen_dump_day.yml -i
echo "Starting segmentation: aachen night queries"
python -m runx.runx scripts/aachen_dump_night.yml -i
echo "DONE"
