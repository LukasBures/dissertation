# python -m runx.runx scripts/aachen.yml -i -n

selected_gpu=0
root_folder=/home/lukas/PycharmProjects/Dissertation/_my/_dissertation/my_hloc

# foldername="superpoint_aachen-superglue_$(date +%Y.%m.%d_%H.%M.%S)"
# mkdir -p logs/aachen/"$foldername"/code
# cp main.py run_1080Ti.sh logs/aachen/"$foldername"/code
# cp -R runx/ logs/aachen/"$foldername"/code
# # cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$foldername"/code
# cd logs/aachen/"$foldername"/
# # --feature_conf superpoint_aachen --matcher_conf superglue
# python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_aachen --matcher_conf superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
# cd $root_folder

# -----------------------------------------------------------------------------
foldername="superpoint_aachen-my_superglue_$(date +%Y.%m.%d_%H.%M.%S)"
mkdir -p logs/aachen/"$foldername"/code
cp main.py run_1080Ti.sh logs/aachen/"$foldername"/code
cp -R runx/ logs/aachen/"$foldername"/code
# cp -R /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/hloc/ logs/aachen/"$foldername"/code
cd logs/aachen/"$foldername"/
# --outputs results --feature_conf superpoint_aachen --matcher_conf my_superglue
python code/main.py --experiment_name aachen --dataset /home/lukas/PycharmProjects/Dissertation/datasets/aachen/ --images /home/lukas/PycharmProjects/Dissertation/datasets/aachen/images/images_upright/ --pairs /home/lukas/PycharmProjects/Dissertation/HierarchicalLocalization/pairs/aachen/ --outputs results --feature_conf superpoint_aachen --matcher_conf my_superglue --result_dir ./ --gpu_number $selected_gpu | tee mylog.log
cd $root_folder

echo "DONE"
