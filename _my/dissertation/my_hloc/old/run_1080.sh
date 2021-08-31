# PYTHONPATH=logs/aachen/heavy-mussel_2020.12.11_12.57/code
# python -m runx.runx scripts/aachen.yml -i -n

# activate venv
source /home/lukas/PycharmProjects/Dissertation/.venv/bin/activate

selected_gpu=1
project_folder=/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc
root_folder=/media/lukas/WD_2TB/dissertation

# AACHEN
aachen_dataset=/home/lukas/PycharmProjects/Dissertation/datasets/aachen/
aachen_images=/home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/
aachen_pairs=/home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/

# AACHEN 1.1
aachen_11_dataset=/home/lukas/PycharmProjects/Dissertation/datasets/aachen/
aachen_11_images=/home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/
aachen_11_pairs=/home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/

#folder_name="superpoint_max-superglue_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf superpoint_max --matcher_conf superglue
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_max --matcher_conf superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder

# -----------------------------------------------------------------------------
#folder_name="superpoint_max-my_superglue_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf superpoint_max --matcher_conf my_superglue
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_max --matcher_conf my_superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder

# -----------------------------------------------------------------------------
#folder_name="superpoint_max-my_superglue_retest_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf superpoint_max --matcher_conf my_superglue
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_max --matcher_conf my_superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder

## -----------------------------------------------------------------------------
#folder_name="superpoint_aachen-my_superglue_retest_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf superpoint_aachen --matcher_conf my_superglue
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_aachen --matcher_conf my_superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder

## -----------------------------------------------------------------------------
#folder_name="superpoint_aachen-my_superglue_200_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf superpoint_aachen --matcher_conf my_superglue_200
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_aachen --matcher_conf my_superglue_200 --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder

# -----------------------------------------------------------------------------
#folder_name="superpoint_max-my_superglue_retest2_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf superpoint_max --matcher_conf my_superglue
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_max --matcher_conf my_superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder

# -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'_'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log

# -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_6"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'_'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder"

# -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_7"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'_'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder"

# -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_8"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'_'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder"

# -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_9"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'_'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder"

## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-retest_2-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_noresize"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_kp1024"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_kp3072"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_resize2000"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_resize2400"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_resize3200"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="NN"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

## -----------------------------------------------------------------------------
#feature="superpoint_recommended_maxkp_512"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_maxsize_800"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_maxsize_900"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-retest3-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-retest4-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="NN_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu --netvlad 30 --covisibility_clustering true | tee mylog.log
#cd "$project_folder" || exit 1

## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="NN_recommended"
#folder_name="$feature"'-'"$matcher"'-netvlad_20-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu --netvlad 20 --covisibility_clustering true | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="NN_recommended"
#folder_name="$feature"'-'"$matcher"'-netvlad_30-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu --netvlad 30 --covisibility_clustering true | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="NN_recommended"
#folder_name="$feature"'-'"$matcher"'-netvlad_50-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu --netvlad 50 --covisibility_clustering true | tee mylog.log
#cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
#feature="superpoint_max"
#matcher="NN_recommended"
#folder_name="$feature"'-'"$matcher"'-netvlad_30-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu --netvlad 30 --covisibility_clustering true | tee mylog.log
#cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
#feature="superpoint_max"
#matcher="NN_recommended"
#folder_name="$feature"'-'"$matcher"'-netvlad_50-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu --netvlad 50 --covisibility_clustering true | tee mylog.log
#cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_h"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_n"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_s"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_v"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_hn"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_hs"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

# ---------------------------------------------------------------------
# superpoint_aachen_test_5_seg_nvidia ---------------------------------
# ---------------------------------------------------------------------
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_sv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_hns"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_hnv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_hsv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_nsv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_hnsv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1



# ---------------------------------------------------------------------
# superpoint_n2048_r1024_seg_nvidia ---------------------------------
# ---------------------------------------------------------------------
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_h"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_n"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_s"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_v"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_hn"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_hs"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_hv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_ns"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_nv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_sv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_hns"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_hnv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_hsv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_nsv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_n2048_r1024_seg_nvidia_hnsv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

# ---------------------------------------------------------------------
# superpoint_kp4096_seg_nvidia - my_superglue_200 ---------------------
# ---------------------------------------------------------------------

## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_h"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_n"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_s"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_v"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_hn"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_hs"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_hv"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_ns"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_nv"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_sv"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_hns"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_hnv"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_hsv"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_kp4096_seg_nvidia_nsv"
#matcher="my_superglue_200"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_hnsv"
matcher="my_superglue_200"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset $aachen_dataset --images $aachen_images --pairs $aachen_pairs --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1


echo "DONE"
