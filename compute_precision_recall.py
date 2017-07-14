import numpy as np
import os
import argparse
import _pickle
from utils.io import *


def compute_pre_rec(gt, detection, ovthresh=0.5):
  # detection format:
  # frame_id, id, xmin, ymin, xmax, ymax, confidence
  # ground truth format:
  # dictionary len for each frame id, each elem has bboxes K dictionary
  #  'bboxes' Kx4 ndarray: [xmin, ymin, xmax, ymax]
  #  'detected' K bool
  image_ids = [x[0] for x in detection]
  confidence = np.array([float(x[6]) for x in detection])
  BB = np.array([[float(z) for z in x[2:6]] for x in detection])

  # sort by confidence
  sorted_ind = np.argsort(-confidence)
  sorted_scores = np.sort(-confidence)
  BB = BB[sorted_ind, :]
  image_ids = [int(image_ids[x]) for x in sorted_ind]

  nd = len(image_ids)
  tp = np.zeros(nd)
  fp = np.zeros(nd)

  npos = 0
  for R in gt.values():
    npos += len(R['bboxes'])

  for d in range(nd):
    if str(image_ids[d]) not in gt:
      fp[d] = 1
      continue
    R = gt[str(image_ids[d])]
    BBGT = R['bboxes']
    bb = BB[d, :].astype(float)
    ovmax = -np.inf

    if BBGT.size > 0:
      # compute overlaps
      # intersection
      ixmin = np.maximum(BBGT[:, 0], bb[0])
      iymin = np.maximum(BBGT[:, 1], bb[1])
      ixmax = np.minimum(BBGT[:, 2], bb[2])
      iymax = np.minimum(BBGT[:, 3], bb[3])
      iw = np.maximum(ixmax - ixmin + 1., 0.)
      ih = np.maximum(iymax - iymin + 1., 0.)
      inters = iw * ih

      # union
      uni = ((bb[2] - bb[0] + 1.) * (bb[3] - bb[1] + 1.) +
             (BBGT[:, 2] - BBGT[:, 0] + 1.) *
             (BBGT[:, 3] - BBGT[:, 1] + 1.) - inters)

      overlaps = inters / uni
      ovmax = np.max(overlaps)
      jmax = np.argmax(overlaps)

    if ovmax > ovthresh:
      if not R['detected'][jmax]:
        tp[d] = 1.
        R['detected'][jmax] = 1
      else:
        fp[d] = 1.
    else:
      fp[d] = 1.


  # compute precision recall
  fp = np.cumsum(fp)
  tp = np.cumsum(tp)
  rec = tp / float(npos)
  # avoid divide by zero in case the first detection matches a difficult
  # ground truth
  prec = tp / np.maximum(tp + fp, np.finfo(np.float64).eps)
  return rec, prec, -sorted_scores


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('gt_type', choices=['pascal_voc', 'txt'], type=str)
  parser.add_argument('gt_path', type=str)
  parser.add_argument('detection_type', choices=['json', 'txt'], type=str)
  parser.add_argument('detection_path', type=str)
  parser.add_argument('--ovthresh', default=0.5, type=float)
  parser.add_argument('--output_path', default='rec_prec_scores.pkl', type=str)
  args = parser.parse_args()
  return args


# This cript assume the frame id in both detection and ground truth are the same
# In pascal_voc and json reading the frame id will be deduced from the file names.
if __name__ == '__main__':
  args = parse_args()
  if args.gt_type == 'pascal_voc':
    gt = parse_pascal_voc_groundtruth(args.gt_path)
  elif args.gt_type == 'txt':
    gt = parse_txt_groundtruth(args.gt_path)

  if args.detection_type == 'json':
    detection = parse_json_detection(args.detection_path)
  elif args.detection_type == 'txt':
    detection = parse_txt_detection(args.detection_path)

  rec, prec, scores = compute_pre_rec(gt=gt, detection=detection, ovthresh=args.ovthresh)
  print("Recall: {}".format(rec[-1]))
  print("Precision: {}".format(prec[-1]))
  with open(args.output_path, 'wb') as f:
    _pickle.dump([rec, prec, scores], f)


