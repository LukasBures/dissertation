#!/bin/bash

. /home/lukas/PycharmProjects/dissertation/.venv/bin/activate

cd /home/lukas/PycharmProjects/dissertation/_my/dissertation/my_hloc/result_graphs || exit 1

python main_aachen_v1.py
python main_aachen_v1_1.py
python main_4seasons_validation.py
# python main_4seasons_training.py

echo "ALL DONE"
