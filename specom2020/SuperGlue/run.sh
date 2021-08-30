#!/usr/bin/env bash

# python3 my_match_pairs.py --input_pairs "./assets/scannet_sample_pairs_with_gt.txt"
python3 my_match_pairs.py --input_pairs "./assets/summer_original-spring_GAN.txt" \
    --output_dir "./dump_summer_original-spring_GAN"  \
    --resize -1 \
    --superglue "outdoor" \
    --max_keypoints -1 \
    --device "cuda:1"

python3 my_match_pairs.py --input_pairs "./assets/summer_original-fall_GAN.txt" \
    --output_dir "./dump_summer_original-fall_GAN"  \
    --resize -1 \
    --superglue "outdoor" \
    --max_keypoints -1 \
    --device "cuda:1"

python3 my_match_pairs.py --input_pairs "./assets/summer_original-winter_GAN.txt" \
    --output_dir "./dump_summer_original-winter_GAN"  \
    --resize -1 \
    --superglue "outdoor" \
    --max_keypoints -1 \
    --device "cuda:1"