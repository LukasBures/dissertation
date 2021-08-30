#!/bin/bash
# This script is for cleaning some big unnecessary data and moving results of defined experiments

# declare an array variable
declare -a array=(
  "superpoint_kp4096_seg_nvidia_n-my_superglue-2021.01.15_21.48.34"
  "superpoint_kp4096_seg_nvidia_h-my_superglue-2021.01.15_07.26.01"
  "superpoint_aachen_test_5_seg_nvidia_s-my_superglue-2021.01.29_21.05.45"
  "superpoint_aachen_test_5_seg_nvidia_n-my_superglue-2021.01.29_14.50.43"
  "superpoint_aachen-my_superglue_2020.12.12_14.58.41"
  "superpoint_aachen_test_5_seg_nvidia_h-my_superglue-2021.01.29_08.44.13"
  "superpoint_n4096_r1024_seg_nvidia_hnsv-my_superglue-2021.01.29_00.34.52"
  "superpoint_n4096_r1024_seg_nvidia_nsv-my_superglue-2021.01.28_16.24.21"
  "superpoint_aachen_test_5_noresize-my_superglue-2020.12.31_21.18.21"
  "superpoint_aachen_test_5-my_superglue_2020.12.22_17.07.38"
  "superpoint_n4096_r1024_seg_nvidia_hsv-my_superglue-2021.01.28_07.51.11"
  "superpoint_n4096_r1024_seg_nvidia_hnv-my_superglue-2021.01.27_23.32.25"
  "superpoint_n4096_r1024_seg_nvidia_hns-my_superglue-2021.01.27_15.24.25"
  "superpoint_n4096_r1024_seg_nvidia_sv-my_superglue-2021.01.27_06.44.06"
  "superpoint_n4096_r1024_seg_nvidia_nv-my_superglue-2021.01.26_22.34.14"
  "superpoint_n4096_r1024_seg_nvidia_ns-my_superglue-2021.01.26_14.20.02"
  "superpoint_n4096_r1024_seg_nvidia_hv-my_superglue-2021.01.26_06.02.12"
  "superpoint_n4096_r1024_seg_nvidia_hs-my_superglue-2021.01.25_21.36.59"
  "superpoint_n4096_r1024_seg_nvidia_hn-my_superglue-2021.01.25_13.26.12"
  "superpoint_n4096_r1024_seg_nvidia_v-my_superglue-2021.01.25_05.03.53"
  "superpoint_n4096_r1024_seg_nvidia_s-my_superglue-2021.01.24_20.28.25"
  "superpoint_n4096_r1024_seg_nvidia_n-my_superglue-2021.01.24_12.16.42"
  "superpoint_n4096_r1024_seg_nvidia_h-my_superglue-2021.01.24_03.54.56"
  "superpoint_kp4096_seg_nvidia_hnsv-my_superglue-2021.01.23_13.50.01"
  "superpoint_kp4096_seg_nvidia_nsv-my_superglue-2021.01.22_23.48.54"
  "superpoint_kp4096_seg_nvidia_hsv-my_superglue-2021.01.22_09.28.06"
  "superpoint_kp4096_seg_nvidia_hnv-my_superglue-2021.01.21_19.29.13"
  "superpoint_kp4096_seg_nvidia_hns-my_superglue-2021.01.21_05.25.15"
  "superpoint_kp4096_seg_nvidia_sv-my_superglue-2021.01.20_15.07.54"
  "superpoint_kp4096_seg_nvidia_nv-my_superglue-2021.01.20_00.57.24"
  "superpoint_kp4096_seg_nvidia_ns-my_superglue-2021.01.19_10.56.32"
  "superpoint_kp4096_seg_nvidia_hv-my_superglue-2021.01.18_20.39.16"
  "superpoint_kp4096_seg_nvidia_hs-my_superglue-2021.01.18_06.26.17"
  "superpoint_kp4096_seg_nvidia_hn-my_superglue-2021.01.17_16.23.00"
  "superpoint_kp4096_seg_nvidia_v-my_superglue-2021.01.17_02.10.04"
  "superpoint_kp4096_seg_nvidia_s-my_superglue-2021.01.16_11.53.41"
  "superpoint_n2048_r1024_seg_nvidia_hnsv-my_superglue-2021.01.16_00.46.57"
  "superpoint_n2048_r1024_seg_nvidia_nsv-my_superglue-2021.01.15_17.24.21"
  "superpoint_n2048_r1024_seg_nvidia_hsv-my_superglue-2021.01.15_10.02.54"
  "superpoint_n2048_r1024_seg_nvidia_hnv-my_superglue-2021.01.15_02.35.06"
  "superpoint_kpt015_seg_nvidia_hnsv-my_superglue-2021.01.15_01.09.57"
  "superpoint_n2048_r1024_seg_nvidia_hns-my_superglue-2021.01.14_18.53.37"
  "superpoint_kpt015_seg_nvidia_nsv-my_superglue-2021.01.14_18.51.28"
  "superpoint_kpt015_seg_nvidia_hsv-my_superglue-2021.01.14_12.39.03"
  "superpoint_n2048_r1024_seg_nvidia_sv-my_superglue-2021.01.14_11.17.48"
  "superpoint_kpt015_seg_nvidia_hnv-my_superglue-2021.01.14_06.34.42"
  "superpoint_n2048_r1024_seg_nvidia_nv-my_superglue-2021.01.14_03.57.47"
  "superpoint_kpt015_seg_nvidia_hns-my_superglue-2021.01.14_00.22.49"
  "superpoint_n2048_r1024_seg_nvidia_ns-my_superglue-2021.01.13_20.28.11"
  "superpoint_kpt015_seg_nvidia_sv-my_superglue-2021.01.13_18.18.13"
  "superpoint_n2048_r1024_seg_nvidia_hv-my_superglue-2021.01.13_13.04.03"
  "superpoint_kpt015_seg_nvidia_nv-my_superglue-2021.01.13_12.13.38"
  "superpoint_kpt015_seg_nvidia_ns-my_superglue-2021.01.13_06.06.16"
  "superpoint_n2048_r1024_seg_nvidia_hs-my_superglue-2021.01.13_05.29.35"
  "superpoint_kpt015_seg_nvidia_hv-my_superglue-2021.01.13_00.01.36"
  "superpoint_n2048_r1024_seg_nvidia_hn-my_superglue-2021.01.12_22.13.28"
  "superpoint_kpt015_seg_nvidia_hs-my_superglue-2021.01.12_17.57.12"
  "superpoint_n2048_r1024_seg_nvidia_v-my_superglue-2021.01.12_14.49.38"
  "superpoint_kpt015_seg_nvidia_hn-my_superglue-2021.01.12_11.59.25"
  "superpoint_n2048_r1024_seg_nvidia_s-my_superglue-2021.01.12_07.27.56"
  "superpoint_kpt015_seg_nvidia_v-my_superglue-2021.01.12_05.55.35"
  "superpoint_n2048_r1024_seg_nvidia_n-my_superglue-2021.01.12_00.09.30"
  "superpoint_kpt015_seg_nvidia_s-my_superglue-2021.01.11_23.50.03"
  "superpoint_kpt015_seg_nvidia_n-my_superglue-2021.01.11_17.53.11"
  "superpoint_n2048_r1024_seg_nvidia_h-my_superglue-2021.01.11_16.44.04"
  "superpoint_kpt015_seg_nvidia_h-my_superglue-2021.01.11_11.45.12"
  "superpoint_default_test_2-superglue_default-2021.01.06_05.32.40"
  "superpoint_default_test_2-superglue_recommended-2021.01.06_00.41.47"
  "superpoint_default_test_1-superglue_default-2021.01.05_19.55.16"
  "superpoint_default_test_1-superglue_recommended-2021.01.05_14.58.37"
  "superpoint_recommended_nms5-superglue_recommended-2021.01.02_08.49.49"
  "superpoint_recommended_nms4-superglue_recommended-2021.01.02_04.19.16"
  "superpoint_recommended_nms2-superglue_recommended-2021.01.01_23.48.22"
  "superpoint_recommended-superglue_recommended_2020.12.22_16.58.46"
  )

rootfolder="/media/lukas/WD_2TB/dissertation"
tofolder="/data512/dissertation"

# get length of an array
array_length=${#array[@]}

cd $rootfolder || exit 1

# use for loop to read all values and indexes
for (( i=1; i<array_length+1; i++ )); do
    echo "$i" "/" ${array_length} "Processing: " ${array[$i-1]}

    cd ${array[$i-1]} || exit 1
    cd results/ || exit 1

    rm *.h5
    rm *.pkl
    rm -R sfm*

    cd $rootfolder || exit 1
    mv ${array[$i-1]} $tofolder
done

echo "DONE"