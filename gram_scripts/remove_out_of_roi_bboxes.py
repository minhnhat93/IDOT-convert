from utils.annotation_parsing import parse_txt_detection, write_MOT_detection
import os
from PIL import Image
import argparse
import numpy as np

def in_roi_check(roi, bbox):
  height, width = roi.shape
  y_min = max(int(bbox[1]) - 1, 0)
  y_max = min(int(bbox[3]) - 1, height)
  x_min = max(int(bbox[0]) - 1, 0)
  x_max = min(int(bbox[2]) - 1, width)
  _bbox = np.zeros_like(roi)
  _bbox[y_min:y_max + 1, x_min:x_max + 1] = 1
  return (_bbox * roi).sum() > 0

def read_roi(fn):
  roi = np.asarray(Image.open(fn), dtype=np.int32)
  roi = roi.sum(axis=2)
  roi.setflags(write=1)
  roi[roi <= 100] = 0
  roi[roi > 100] = 1
  return roi

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
parser.add_argument('output_file', type=str)
parser.add_argument('roi_name', type=str, choices=['M-30', 'M-30-HD', 'Urban1'])
args = parser.parse_args()

roi_path = os.path.join('gram_scripts/rois', '{}-map.jpg'.format(args.roi_name))
roi = read_roi(roi_path)
data = parse_txt_detection(args.input_file)
frames = []
for frame in data:
  bbox = frame[2:6]
  if in_roi_check(roi, bbox):
    frames.append(frame)
  else:
    print("Bounding box removed: ", frame)
write_MOT_detection(args.output_file, frames, 0.0)