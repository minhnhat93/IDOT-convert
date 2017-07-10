#!/usr/bin/env bash
git clone https://github.com/thtrieu/darkflow ~/darkflow
cd ~/darkflow
python3 setup.py build_ext --inplace
sudo pip3 install -e .
wget https://pjreddie.com/media/files/yolo.weights -O bin/yolo.weights