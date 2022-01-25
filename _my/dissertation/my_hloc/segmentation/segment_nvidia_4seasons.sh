#!/bin/bash

# /bin/bash segment_nvidia.sh | tee segment_nvidia.log
. /home/lukas/PycharmProjects/dissertation/.venv/bin/activate

# ---------------------------------------------------------------------------------
DATASET_NAME="4Seasons_test0_cam0"
PATH_ROOT="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_test0_cam0/"
DESTINATION_FOLDER="/data512/dissertation_results/4Seasons/"

# Segment NVIDIA
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
python -m runx.runx scripts/4Seasons_dump_test0_cam0.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Create pickle file
echo "Starting creating pickle file plus grouping segmentations ..."
cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/ || exit
python segment.py --dataset_name $DATASET_NAME --path_root $PATH_ROOT --destination_folder $DESTINATION_FOLDER
echo "DONE saved to h5 ..."

# ---------------------------------------------------------------------------------
DATASET_NAME="4Seasons_test0_cam1"
PATH_ROOT="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_test0_cam1/"
DESTINATION_FOLDER="/data512/dissertation_results/4Seasons/"

# Segment NVIDIA
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
python -m runx.runx scripts/4Seasons_dump_test0_cam1.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Create pickle file
echo "Starting creating pickle file plus grouping segmentations ..."
cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/ || exit
python segment.py --dataset_name $DATASET_NAME --path_root $PATH_ROOT --destination_folder $DESTINATION_FOLDER
echo "DONE saved to h5 ..."

# ---------------------------------------------------------------------------------
DATASET_NAME="4Seasons_test1_cam0"
PATH_ROOT="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_test1_cam0/"
DESTINATION_FOLDER="/data512/dissertation_results/4Seasons/"

# Segment NVIDIA
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
python -m runx.runx scripts/4Seasons_dump_test1_cam0.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Create pickle file
echo "Starting creating pickle file plus grouping segmentations ..."
cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/ || exit
python segment.py --dataset_name $DATASET_NAME --path_root $PATH_ROOT --destination_folder $DESTINATION_FOLDER
echo "DONE saved to h5 ..."

# ---------------------------------------------------------------------------------
DATASET_NAME="4Seasons_test1_cam1"
PATH_ROOT="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_test1_cam1/"
DESTINATION_FOLDER="/data512/dissertation_results/4Seasons/"

# Segment NVIDIA
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
python -m runx.runx scripts/4Seasons_dump_test1_cam1.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Create pickle file
echo "Starting creating pickle file plus grouping segmentations ..."
cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/ || exit
python segment.py --dataset_name $DATASET_NAME --path_root $PATH_ROOT --destination_folder $DESTINATION_FOLDER
echo "DONE saved to h5 ..."

# ---------------------------------------------------------------------------------
echo "ALL DONE"
