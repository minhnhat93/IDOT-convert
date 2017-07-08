#!/usr/bin/env bash
git clone https://github.com/thtrieu/darkflow ~/darkflow
cd ~/darkflow
python3 setup.py build_ext --inplace
sudo pip3 install -e .
