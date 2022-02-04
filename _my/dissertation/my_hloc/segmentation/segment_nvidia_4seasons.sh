#!/bin/bash

# /bin/bash segment_nvidia.sh | tee segment_nvidia.log
. /home/lukas/PycharmProjects/dissertation/.venv/bin/activate
HUMAN="human"
VEHICLE="vehicle"

# ---------------------------------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------------------------------
echo "VALIDATION --------------------------------------"
PATH_ROOT_CAM0="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_validation_cam0/best_images/"
PATH_ROOT_CAM1="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_validation_cam1/best_images/"
DESTINATION_FOLDER="/data512/dissertation_results/4Seasons/"

# Segment NVIDIA
DATASET_NAME="4Seasons_validation_cam0"
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit 1
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
# time python -m runx.runx scripts/4Seasons_dump_validation_cam0.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Segment NVIDIA
DATASET_NAME="4Seasons_validation_cam1"
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit 1
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
# time python -m runx.runx scripts/4Seasons_dump_validation_cam1.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Create h5 file
DATASET_NAME="4Seasons_validation"
echo "Starting creating h5 file plus grouping segmentations ..."
cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/ || exit 1
# python segment.py --dataset_name $DATASET_NAME --path_roots $PATH_ROOT_CAM0 $PATH_ROOT_CAM1 --destination_folder $DESTINATION_FOLDER --segmentation_classes $HUMAN $VEHICLE
echo "DONE saved to h5 ..."
echo "-----------------------------------------------"
echo ""

# ---------------------------------------------------------------------------------
# TRAINING
# ---------------------------------------------------------------------------------
echo "TRAINING --------------------------------------"
PATH_ROOT_CAM0="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_training_cam0/best_images/"
PATH_ROOT_CAM1="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_training_cam1/best_images/"
DESTINATION_FOLDER="/data512/dissertation_results/4Seasons/"

# Segment NVIDIA
DATASET_NAME="4Seasons_training_cam0"
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit 1
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
# time python -m runx.runx scripts/4Seasons_dump_training_cam0.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Segment NVIDIA
DATASET_NAME="4Seasons_training_cam1"
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit 1
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
time python -m runx.runx scripts/4Seasons_dump_training_cam1.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Create h5 file
DATASET_NAME="4Seasons_training"
echo "Starting creating h5 file plus grouping segmentations ..."
cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/ || exit 1
python segment.py --dataset_name $DATASET_NAME --path_roots $PATH_ROOT_CAM0 $PATH_ROOT_CAM1 --destination_folder $DESTINATION_FOLDER --segmentation_classes $HUMAN $VEHICLE
echo "DONE saved to h5 ..."
echo "-----------------------------------------------"
echo ""

# ---------------------------------------------------------------------------------
# TEST0
# ---------------------------------------------------------------------------------
echo "TEST0 --------------------------------------"
PATH_ROOT_CAM0="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_test0_cam0/best_images/"
PATH_ROOT_CAM1="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_test0_cam1/best_images/"
DESTINATION_FOLDER="/data512/dissertation_results/4Seasons/"

## Segment NVIDIA
DATASET_NAME="4Seasons_test0_cam0"
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit 1
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
time python -m runx.runx scripts/4Seasons_dump_test0_cam0.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Segment NVIDIA
DATASET_NAME="4Seasons_test0_cam1"
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit 1
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
time python -m runx.runx scripts/4Seasons_dump_test0_cam1.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Create h5 file
DATASET_NAME="4Seasons_test0"
echo "Starting creating h5 file plus grouping segmentations ..."
cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/ || exit 1
python segment.py --dataset_name $DATASET_NAME --path_roots $PATH_ROOT_CAM0 $PATH_ROOT_CAM1 --destination_folder $DESTINATION_FOLDER --segmentation_classes $HUMAN $VEHICLE
echo "DONE saved to h5 ..."
echo "-----------------------------------------------"
echo ""

# ---------------------------------------------------------------------------------
# TEST1
# ---------------------------------------------------------------------------------
echo "TEST1 --------------------------------------"
PATH_ROOT_CAM0="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_test1_cam0/best_images/"
PATH_ROOT_CAM1="/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/4Seasons_test1_cam1/best_images/"
DESTINATION_FOLDER="/data512/dissertation_results/4Seasons/"

## Segment NVIDIA
DATASET_NAME="4Seasons_test1_cam0"
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit 1
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
time python -m runx.runx scripts/4Seasons_dump_test1_cam0.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Segment NVIDIA
DATASET_NAME="4Seasons_test1_cam1"
cd /home/lukas/PycharmProjects/dissertation/_segmentation/semantic_segmentation_NVIDIA/ || exit 1
export OMP_NUM_THREADS=3
echo "Starting segmentation: $DATASET_NAME ..."
time python -m runx.runx scripts/4Seasons_dump_test1_cam1.yml -i
echo "DONE segmentation: $DATASET_NAME ..."

# Create h5 file
DATASET_NAME="4Seasons_test1"
echo "Starting creating h5 file plus grouping segmentations ..."
cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/segmentation/ || exit 1
python segment.py --dataset_name $DATASET_NAME --path_roots $PATH_ROOT_CAM0 $PATH_ROOT_CAM1 --destination_folder $DESTINATION_FOLDER --segmentation_classes $HUMAN $VEHICLE
echo "DONE saved to h5 ..."
echo "-----------------------------------------------"
echo ""

# ---------------------------------------------------------------------------------
echo "ALL DONE"
