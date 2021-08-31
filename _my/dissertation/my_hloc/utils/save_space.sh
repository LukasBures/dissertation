#!/bin/bash
# This script is for cleaning some big unnecessary data and moving results of defined experiments

ROOT_FOLDER="/media/lukas/WD_2TB/dissertation"
TO_FOLDER="/data512/dissertation_results"

cd $ROOT_FOLDER || exit 1
shopt -s dotglob
shopt -s nullglob

array=(*/)
# declare an array variable
# declare -a array=(
#   "superpoint_kp4096_seg_nvidia_n-my_superglue-2021.01.15_21.48.34"
#   )

# check if experiment has finished

# get length of an array
array_length=${#array[@]}

# use for loop to read all values and indexes
for (( i=1; i<array_length+1; i++ )); do
    cd $ROOT_FOLDER || exit 1
    echo "$i" "/" "${array_length}" "Processing: " "${array[$i-1]}"
    FILE="${array[$i-1]}"results/Aachen_hloc_superpoint+superglue_netvlad50.txt

    if test -f "$FILE"; then
        cd "${array[$i-1]}" || exit 1
        cd results/ || exit 1

        rm *.h5
        rm *.pkl
        rm -R sfm*

        cd $ROOT_FOLDER || exit 1
        mv "${array[$i-1]}" $TO_FOLDER
    else
        echo "$FILE does not exist."
    fi
    echo ""
done

echo "DONE"