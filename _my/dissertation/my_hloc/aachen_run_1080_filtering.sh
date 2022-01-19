# Activate virtual environment.
. /home/lukas/PycharmProjects/dissertation/.venv/bin/activate

# Global settings.
selected_gpu=1  # 1080
output_root_folder=/data512/dissertation_results
project_folder=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc
this_file_name=`basename "$0"`
cd "$project_folder" || exit 1

# Aachen dataset settings.
used_dataset="aachen"
dataset_folder=/data512/datasets/aachen/
segmentations_file=/data512/dissertation_results/aachen_all_v1/segment_nvidia_v01.pkl
pipeline=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/pipelines/Aachen/pipeline_filtering.py
configs=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/pipelines/Aachen/configs.py
feature_filter=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/utils/feature_filter.py
outputs_folder=results

# EXPERIMENTS:
# -----------------------------------------------------------------------------
retrieval_conf="netvlad"
feature_conf="superpoint_aachen"
matcher_conf="superglue"
num_covis=20
num_loc=50
static_from=50
static_to=100
static_step=10
dynamic_from=100
dynamic_to=100
dynamic_step=10
folder_name="$used_dataset"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$output_root_folder"/"$folder_name"/code
cp $pipeline "$output_root_folder"/"$folder_name"/code
cp $configs "$output_root_folder"/"$folder_name"/code
cp $feature_filter "$output_root_folder"/"$folder_name"/code
cp $this_file_name "$output_root_folder"/"$folder_name"/code
cd "$output_root_folder"/"$folder_name"/ || exit 1
time python "$output_root_folder"/"$folder_name"/code/pipeline_filtering.py --dataset $dataset_folder --outputs $outputs_folder --num_covis $num_covis --num_loc $num_loc --retrieval_conf $retrieval_conf --feature_conf $feature_conf --matcher_conf $matcher_conf --gpu_number $selected_gpu --static_from $static_from --static_to $static_to --static_step $static_step --dynamic_from $dynamic_from --dynamic_to $dynamic_to --dynamic_step $dynamic_step --segmentations_file $segmentations_file 2>&1 | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
echo "ALL DONE!"
date
