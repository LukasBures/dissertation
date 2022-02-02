# Activate virtual environment.
. /home/lukas/PycharmProjects/dissertation/.venv/bin/activate

# Global settings
selected_gpu=1  # 1080
output_root_folder=/data512/dissertation_results
project_folder=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc
this_file_name=`basename "$0"`
cd "$project_folder" || exit 1

# 4Seasons dataset settings.
used_dataset="4Seasons"
dataset_folder=/data512/datasets/4Seasons/
segmentations_file=/data512/dissertation_results/4Seasons/segment_nvidia_v01.h5
pipeline=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/pipelines/4Seasons/pipeline_filtering.py
configs=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/pipelines/4Seasons/configs.py
feature_filter=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/utils/feature_filter.py
utils=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/pipelines/4Seasons/utils2.py
prepare_reference=/home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/pipelines/4Seasons/prepare_reference.py
outputs_folder_0=results_test0
outputs_folder_1=results_test1
outputs_folder_training=results_training
outputs_folder_validation=results_validation

# EXPERIMENTS:
# -----------------------------------------------------------------------------
feature_conf="superpoint_fast"
matcher_conf="superglue_fast"
num_ref=20
num_loc=10
static_from=100
static_to=100
static_step=100
dynamic_from=100
dynamic_to=100
dynamic_step=100
folder_name="$used_dataset"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$output_root_folder"/"$folder_name"/code
cp $pipeline "$output_root_folder"/"$folder_name"/code
cp $configs "$output_root_folder"/"$folder_name"/code
cp $feature_filter "$output_root_folder"/"$folder_name"/code
cp $utils "$output_root_folder"/"$folder_name"/code
cp $prepare_reference "$output_root_folder"/"$folder_name"/code
cp $this_file_name "$output_root_folder"/"$folder_name"/code
cd "$output_root_folder"/"$folder_name"/ || exit 1

# TRAIN
time python "$output_root_folder"/"$folder_name"/code/prepare_reference.py --dataset $dataset_folder --outputs $outputs_folder_training  --num_ref $num_ref --feature_conf $feature_conf --matcher_conf $matcher_conf 2>&1 | tee mylog_reference_train.log
time python "$output_root_folder"/"$folder_name"/code/pipeline_filtering.py --sequence "training" --dataset $dataset_folder --outputs $outputs_folder_training --num_ref $num_ref --num_loc $num_loc --feature_conf $feature_conf --matcher_conf $matcher_conf --gpu_number $selected_gpu --static_from $static_from --static_to $static_to --static_step $static_step --dynamic_from $dynamic_from --dynamic_to $dynamic_to --dynamic_step $dynamic_step --segmentations_file $segmentations_file 2>&1 | tee mylog_training.log

# VALIDATION
time python "$output_root_folder"/"$folder_name"/code/prepare_reference.py --dataset $dataset_folder --outputs $outputs_folder_validation  --num_ref $num_ref --feature_conf $feature_conf --matcher_conf $matcher_conf 2>&1 | tee mylog_reference_validation.log
time python "$output_root_folder"/"$folder_name"/code/pipeline_filtering.py --sequence "validation" --dataset $dataset_folder --outputs $outputs_folder_validation --num_ref $num_ref --num_loc $num_loc --feature_conf $feature_conf --matcher_conf $matcher_conf --gpu_number $selected_gpu --static_from $static_from --static_to $static_to --static_step $static_step --dynamic_from $dynamic_from --dynamic_to $dynamic_to --dynamic_step $dynamic_step --segmentations_file $segmentations_file 2>&1 | tee mylog_validation.log

# TEST 0
# time python "$output_root_folder"/"$folder_name"/code/prepare_reference.py --dataset $dataset_folder --outputs $outputs_folder_0  --num_ref $num_ref --feature_conf $feature_conf --matcher_conf $matcher_conf 2>&1 | tee mylog_reference_test0.log
# time python "$output_root_folder"/"$folder_name"/code/pipeline_filtering.py --sequence "test0" --dataset $dataset_folder --outputs $outputs_folder_0 --num_ref $num_ref --num_loc $num_loc --feature_conf $feature_conf --matcher_conf $matcher_conf --gpu_number $selected_gpu --static_from $static_from --static_to $static_to --static_step $static_step --dynamic_from $dynamic_from --dynamic_to $dynamic_to --dynamic_step $dynamic_step --segmentations_file $segmentations_file 2>&1 | tee mylog_test0.log

# TEST 1
# time python "$output_root_folder"/"$folder_name"/code/prepare_reference.py --dataset $dataset_folder --outputs $outputs_folder_1  --num_ref $num_ref --feature_conf $feature_conf --matcher_conf $matcher_conf 2>&1 | tee mylog_reference_test1.log
# time python "$output_root_folder"/"$folder_name"/code/pipeline_filtering.py --sequence "test1" --dataset $dataset_folder --outputs $outputs_folder_1 --num_ref $num_ref --num_loc $num_loc --feature_conf $feature_conf --matcher_conf $matcher_conf --gpu_number $selected_gpu --static_from $static_from --static_to $static_to --static_step $static_step --dynamic_from $dynamic_from --dynamic_to $dynamic_to --dynamic_step $dynamic_step --segmentations_file $segmentations_file 2>&1 | tee mylog_test1.log

cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
echo "ALL DONE!"
date
