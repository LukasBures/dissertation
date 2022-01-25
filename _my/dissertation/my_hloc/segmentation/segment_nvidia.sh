#!/bin/bash

# /bin/bash segment_nvidia.sh | tee segment_nvidia.log
. /home/lukas/PycharmProjects/dissertation/.venv/bin/activate

DATASET_NAME="4Seasons_test0"
PATH_ROOT="/media/lukas/WD_2TB/dissertation/aachen_all_v1/best_images"
DESTINATION_FOLDER="/data512/dissertation_results/4Seasons/"


# ---------------------------------------------------------------------------------
# Segment NVIDIA
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."

# aachen_v1
# python -m runx.runx scripts/aachen_dump_all_v1.yml -i

# aachen_v1_1
# python -m runx.runx scripts/aachen_dump_all_v1_1.yml -i

# 4Seasons test 0
python -m runx.runx scripts/4Seasons_dump_test0.yml -i

# 4Seasons test 1
# python -m runx.runx scripts/4Seasons_dump_test1.yml -i

echo "DONE segmentation: $DATASET_NAME ..."

# ---------------------------------------------------------------------------------
# Create pickle file
echo "Starting creating pickle file plus grouping segmentations ..."
cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/ || exit
python segment.py --dataset_name $DATASET_NAME --path_root $PATH_ROOT --destination_folder $DESTINATION_FOLDER
echo "DONE saved to pickle ..."

# ---------------------------------------------------------------------------------
echo "ALL DONE"
