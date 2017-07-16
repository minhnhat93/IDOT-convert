from utils.annotation_parsing import parse_pascal_voc_groundtruth, write_darknet_labels
import os

LABEL_DIR='/home/nhat/darknet-finetune/IDOT_dataset/labels'
IMG_DIR='/home/nhat/darknet-finetune/IDOT_dataset/images'

if LABEL_DIR is None:
    LABEL_DIR = os.getcwd()

frames = parse_pascal_voc_groundtruth('IDOT_dataset/xml')
write_darknet_labels(LABEL_DIR, frames, ['vehicle', 'people'])

train_set = open('IDOT_dataset/train_index.txt').read().splitlines()
test_set = open('IDOT_dataset/test_index.txt').read().splitlines()
f_train = open('IDOT_dataset/train.txt', 'w')
f_test = open('IDOT_dataset/test.txt', 'w')

for fn in train_set:
    f_train.write('{}\n'.format(os.path.join(IMG_DIR, '{}.jpg'.format(fn))))

for fn in test_set:
    f_test.write('{}\n'.format(os.path.join(IMG_DIR, '{}.jpg'.format(fn))))

f_train.close()
f_test.close()
