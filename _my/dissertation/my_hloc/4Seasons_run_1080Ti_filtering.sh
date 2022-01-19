# Activate virtual environment.
source /home/lukas/PycharmProjects/dissertation/.venv/bin/activate

# Global settings.
selected_gpu=0  # 1080Ti
output_root_folder=/data512/dissertation_results
project_folder=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc
this_file_name=`basename "$0"`
cd "$project_folder" || exit 1

# 4Seasons dataset settings.
used_dataset="4Seasons"
dataset_folder=/data512/datasets/4Seasons/
pipeline=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/pipelines/4Seasons/pipeline.py
configs=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/pipelines/4Seasons/configs.py
utils=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/pipelines/4Seasons/utils.py
outputs_folder_0=results_test0
outputs_folder_1=results_test1

# EXPERIMENTS:
# -----------------------------------------------------------------------------
feature_conf="superpoint_max"
matcher_conf="superglue"
num_ref=20
num_loc=10
folder_name="$used_dataset"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$output_root_folder"/"$folder_name"/code
cp $pipeline "$output_root_folder"/"$folder_name"/code
cp $configs "$output_root_folder"/"$folder_name"/code
cp $utils "$output_root_folder"/"$folder_name"/code
cp $this_file_name "$output_root_folder"/"$folder_name"/code
cd "$output_root_folder"/"$folder_name"/ || exit 1
time python "$output_root_folder"/"$folder_name"/code/pipeline.py --sequence "test0" --dataset $dataset_folder --outputs $outputs_folder_0 --num_ref $num_ref --num_loc $num_loc --feature_conf $feature_conf --matcher_conf $matcher_conf --gpu_number $selected_gpu 2>&1 | tee mylog.log
time python "$output_root_folder"/"$folder_name"/code/pipeline.py --sequence "test1" --dataset $dataset_folder --outputs $outputs_folder_1 --num_ref $num_ref --num_loc $num_loc --feature_conf $feature_conf --matcher_conf $matcher_conf --gpu_number $selected_gpu 2>&1 | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
echo "ALL DONE!"
date
