import os
import glob
import xml.etree.ElementTree as ET
import numpy as np
import json
import _pickle

get_fn_without_ext = lambda fn: os.path.splitext(fn)[0]


def parse_pascal_voc_groundtruth(dir_name):
  # FOR ground truth bounding boxes only
  # Each frame K will have its ground truth detection in the file K.xml
  # For pascal voc format see 1.xml
  frames = dict()
  cur_dir = os.getcwd()
  os.chdir(dir_name)
  annotations = os.listdir('.')
  annotations = glob.glob(str(annotations) + '*.xml')

  for file in annotations:
    root = ET.parse(file).getroot()
    frame_id = get_fn_without_ext(file)
    R = dict(
      frame_id=frame_id,
      bboxes=[],
    )
    # actual parsing

    for obj in root.iter('object'):
      xmlbox = obj.find('bndbox')
      xmin = int(float(xmlbox.find('xmin').text))
      xmax = int(float(xmlbox.find('xmax').text))
      ymin = int(float(xmlbox.find('ymin').text))
      ymax = int(float(xmlbox.find('ymax').text))
      R['bboxes'].append([xmin, ymin, xmax, ymax])
    R['bboxes'] = np.asarray(R['bboxes'])
    R['detected'] = [False] * len(R['bboxes'])
    frames[str(frame_id)] = R

  os.chdir(cur_dir)
  return frames


def parse_txt_groundtruth(fn):
  # assume MOT format:
  # frame_id, id, x, y, width, height
  frames = dict()
  data = np.genfromtxt(fn, dtype=str, delimiter=',')
  data = data[:, 0:6].astype(float)
  for entry in data:
    frame_id, _, xmin, ymin, width, height = entry
    frame_id = int(frame_id)
    if str(frame_id) in frames:
      frames[str(frame_id)]['bboxes'].append([xmin, ymin, xmin + width - 1, ymin + height - 1])
      frames[str(frame_id)]['detected'].append(False)
    else:
      frames[str(frame_id)] = dict(
        frame_id=frame_id,
        bboxes=[[xmin, ymin, xmin + width - 1, ymin + height - 1]],
        detected=[False],
      )
  for frame in frames.values():
    frame['bboxes'] = np.asarray(frame['bboxes'])
  return frames


def parse_json_detection(dir_name):
  # For detection only
  # Frame K will have its detection in the file K.json in the folder.
  # Format: Check 1.json
  frames = list()
  cur_dir = os.getcwd()
  os.chdir(dir_name)
  annotations = os.listdir('.')
  annotations = glob.glob(str(annotations) + '*.json')

  for file in annotations:
    frame_id = get_fn_without_ext(file)
    bboxes = json.load(open(file))
    for bbox in bboxes:
      frames.append([int(frame_id), -1, bbox['topleft']['x'], bbox['topleft']['y'], bbox['bottomright']['x'],
                     bbox['bottomright']['y'], bbox['confidence']])

  os.chdir(cur_dir)
  return frames


def parse_txt_detection(fn):
  # assume MOT format:
  # frame_id, id, x, y, width, height, confidence
  data = np.genfromtxt(fn, dtype=str, delimiter=',')
  data = data[:, 0:7].astype(float)
  data[:, 4] = data[:, 2] + data[:, 4] - 1
  data[:, 5] = data[:, 3] + data[:, 5] - 1
  return data


def write_MOT_detection(fn, det, threshold):
  with open(fn, 'w') as f:
    for bbox in sorted(det):
      if bbox[6] > threshold:
        f.write(
          '{}, -1, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, -1, -1, -1\n'.format(bbox[0], bbox[2], bbox[3],
                                                                                bbox[4] - bbox[2] + 1,
                                                                                bbox[5] - bbox[3] + 1, bbox[6]))


def get_precision_recall_at_threshold(fn, confidence_threshold):
  rec, prec, scores = _pickle.load(open(fn, 'rb'))
  loc = (scores > confidence_threshold).astype(int).sum() - 1
  return dict(
    recall=rec[loc],
    precision=prec[loc]
  )
