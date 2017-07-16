import os
import cv2
from os import mkdir


def mkdir_if_not_exist(dn):
  try:
    mkdir(dn)
  except:
    pass


mkdir_if_not_exist('IDOT_dataset/train')
mkdir_if_not_exist('IDOT_dataset/train/images')
mkdir_if_not_exist('IDOT_dataset/train/xml')
mkdir_if_not_exist('IDOT_dataset/test')
mkdir_if_not_exist('IDOT_dataset/test/images')
mkdir_if_not_exist('IDOT_dataset/test/xml')

train_set = open('IDOT_dataset/train_index.txt').read().splitlines()
test_set = open('IDOT_dataset/test_index.txt').read().splitlines()

curr_dir = os.getcwd()
for fn in train_set:
  os.system('ln -s {}/IDOT_dataset/images/{}.jpg IDOT_dataset/train/images/{}.jpg'.format(curr_dir, fn, fn))
  os.system('ln -s {}/IDOT_dataset/xml/{}.xml IDOT_dataset/train/xml/{}.xml'.format(curr_dir, fn, fn))
for fn in test_set:
  os.system('ln -s {}/IDOT_dataset/images/{}.jpg IDOT_dataset/test/images/{}.jpg'.format(curr_dir, fn, fn))
  os.system('ln -s {}/IDOT_dataset/xml/{}.xml IDOT_dataset/test/xml/{}.xml'.format(curr_dir, fn, fn))
