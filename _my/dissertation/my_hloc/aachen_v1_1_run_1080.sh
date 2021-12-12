# activate venv
source /home/lukas/PycharmProjects/dissertation/.venv/bin/activate

# Global settings
selected_gpu=1  # 1080
output_root_folder=/media/lukas/WD_2TB/dissertation
project_folder=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc
this_file_name=`basename "$0"`
cd "$project_folder" || exit 1

# Aachen v1_1 dataset settings
used_dataset="aachen_v1_1"
dataset_folder=/data512/datasets/aachen_v1_1/
pipeline=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/pipelines/Aachen_v1_1/pipeline.py
configs=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/pipelines/Aachen_v1_1/configs.py
outputs_folder=results

# EXPERIMENTS
# -----------------------------------------------------------------------------
retrieval_conf="netvlad"
feature_conf="superpoint_max"
matcher_conf="superglue"
num_covis=20
num_loc=50
folder_name="$used_dataset"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$output_root_folder"/"$folder_name"/code
cp $pipeline "$output_root_folder"/"$folder_name"/code
cp $configs "$output_root_folder"/"$folder_name"/code
cp $this_file_name "$output_root_folder"/"$folder_name"/code
cd "$output_root_folder"/"$folder_name"/ || exit 1
time python "$output_root_folder"/"$folder_name"/code/pipeline.py --dataset $dataset_folder --outputs $outputs_folder --num_covis $num_covis --num_loc $num_loc --retrieval_conf $retrieval_conf --feature_conf $feature_conf --matcher_conf $matcher_conf --gpu_number $selected_gpu 2>&1 | tee mylog.log
cd "$project_folder" || exit 1






# -----------------------------------------------------------------------------
echo "ALL DONE!"
