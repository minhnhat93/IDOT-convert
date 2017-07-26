import matplotlib.pyplot as plt
from utils.annotation_parsing import parse_pascal_voc_groundtruth, convert_ground_truth_to_detection
import numpy as np
from PIL import Image
import cv2
import glob
import os


def read_roi(fn):
  roi = np.asarray(Image.open(fn), dtype=np.int32)
  roi = roi.sum(axis=2)
  roi.setflags(write=1)
  roi[roi <= 100] = 0
  roi[roi > 100] = 1
  return roi


# min y: 29
# points: (x=333, y=84)

for dataset in ['M-30', 'M-30-HD', 'Urban1']:
  roi = read_roi(os.path.join('/home/nhat/engage-project/dataset/GRAM-RTM/GRAM-RTMv4/ROI/', '{}-map.jpg'.format(dataset)))
  roi = np.expand_dims(roi, 2)
  roi = np.repeat(roi, 3, axis=2)
  os.chdir('/home/nhat/engage-project/dataset/GRAM-RTM/GRAM-RTMv4/{}/images/'.format(dataset))
  if not os.path.exists('../images-masked'):
    os.mkdir('../images-masked')
  images = os.listdir('.')
  images = glob.glob(str(images) + '*.jpg')
  for fn in images:
    image = np.asarray(Image.open(fn))
    image = image * roi
    image = Image.fromarray(image.astype(np.uint8))
    image.save(os.path.join('../images-masked', fn))
