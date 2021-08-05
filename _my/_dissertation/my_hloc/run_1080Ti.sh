# python -m runx.runx scripts/aachen.yml -i -n

selected_gpu=0
root_folder=/media/lukas/WD_2TB/dissertation
project_folder=/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc

#folder_name="superpoint_aachen-superglue_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080Ti.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf superpoint_aachen --matcher_conf superglue
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_aachen --matcher_conf superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder

# -----------------------------------------------------------------------------
#folder_name="superpoint_aachen-my_superglue_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080Ti.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf superpoint_aachen --matcher_conf my_superglue
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_aachen --matcher_conf my_superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder

## -----------------------------------------------------------------------------
#folder_name="my_superpoint-superglue_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080Ti.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf my_superpoint --matcher_conf superglue
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf my_superpoint --matcher_conf superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder

## -----------------------------------------------------------------------------
#folder_name="my_superpoint-my_superglue_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080Ti.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf my_superpoint --matcher_conf my_superglue
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf my_superpoint --matcher_conf my_superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder

## -----------------------------------------------------------------------------
#folder_name="superpoint_aachen-my_superglue_retest3_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080Ti.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf superpoint_aachen --matcher_conf my_superglue
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_aachen --matcher_conf my_superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder
#
## -----------------------------------------------------------------------------
#folder_name="superpoint_aachen-my_superglue_mt03_$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p logs/aachen/"$folder_name"/code
#cp main.py run_1080Ti.sh logs/aachen/"$folder_name"/code
#cp -R runx/ logs/aachen/"$folder_name"/code
## cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$folder_name"/code
#cd logs/aachen/"$folder_name"/
## --feature_conf superpoint_aachen --matcher_conf my_superglue_mt03
#python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_aachen --matcher_conf my_superglue_mt03 --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd $root_folder

# -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'_'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log

# -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_1"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'_'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log

# -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_2"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'_'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder"

# -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_3"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'_'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder"

# -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_4"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'_'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder"

## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-retest_1-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-retest_1-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-retest_1-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-retest_2-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="superglue_recommended_sinkhorn15"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="superglue_recommended_sinkhorn30"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_nms2"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_nms4"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_nms5"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_maxkp_1536"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_maxkp_2560"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_maxkp_2560"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="superglue_recommended_mt010"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="superglue_recommended_mt015"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="superglue_recommended_mt025"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="superglue_recommended_mt030"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="superglue_recommended_mt035"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

## -----------------------------------------------------------------------------
#feature="superpoint_default_test_1"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_default_test_1"
#matcher="superglue_default"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_default_test_2"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_default_test_2"
#matcher="superglue_default"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_HNSV"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
#feature="superpoint_recommended"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

## -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_hv"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_ns"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_nv"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_sv"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_hns"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_hnv"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_hsv"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_nsv"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_recommended_seg_nvidia_hnsv"
#matcher="superglue_recommended"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1


# ---------------------------------------------------------------------
# superpoint_aachen_test_5_seg_nvidia ---------------------------------
# ---------------------------------------------------------------------

## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_h"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_n"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_s"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_v"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_hn"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_hs"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_hv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_ns"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1
#
## -----------------------------------------------------------------------------
#feature="superpoint_aachen_test_5_seg_nvidia_nv"
#matcher="my_superglue"
#folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
#mkdir -p "$root_folder"/"$folder_name"/code
#cp main.py "$root_folder"/"$folder_name"/code
#cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
#cp -R runx/ "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
#cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
#cd "$root_folder"/"$folder_name"/ || exit 1
#python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
#cd "$project_folder" || exit 1

# ---------------------------------------------------------------------
# superpoint_kpt015_seg_nvidia ---------------------------------
# ---------------------------------------------------------------------

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_h"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_n"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_s"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_v"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_hn"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_hs"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_hv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_ns"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_nv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_sv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_hns"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_hnv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_hsv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_nsv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kpt015_seg_nvidia_hnsv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# ---------------------------------------------------------------------
# superpoint_kp4096_seg_nvidia ---------------------------------
# ---------------------------------------------------------------------

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_h"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_n"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_s"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_v"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_hn"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_hs"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_hv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_ns"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_nv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_sv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_hns"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_hnv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_hsv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_nsv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_kp4096_seg_nvidia_hnsv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# ---------------------------------------------------------------------
# superpoint_n4096_r1024_seg_nvidia ---------------------------------
# ---------------------------------------------------------------------

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_h"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_n"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_s"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_v"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_hn"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_hs"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_hv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_ns"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_nv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_sv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_hns"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_hnv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_hsv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_nsv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_n4096_r1024_seg_nvidia_hnsv"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -------------
# missing calculations
# -------------

# -----------------------------------------------------------------------------
feature="superpoint_aachen_test_5_seg_nvidia_h"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_aachen_test_5_seg_nvidia_n"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1

# -----------------------------------------------------------------------------
feature="superpoint_aachen_test_5_seg_nvidia_s"
matcher="my_superglue"
folder_name="$feature"'-'"$matcher"'-'"$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p "$root_folder"/"$folder_name"/code
cp main.py "$root_folder"/"$folder_name"/code
cp run_1080Ti.sh "$root_folder"/"$folder_name"/code
cp -R runx/ "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/extract_features.py "$root_folder"/"$folder_name"/code
cp /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/match_features.py "$root_folder"/"$folder_name"/code
cd "$root_folder"/"$folder_name"/ || exit 1
python "$root_folder"/"$folder_name"/code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf $feature --matcher_conf $matcher --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd "$project_folder" || exit 1














echo "DONE"
