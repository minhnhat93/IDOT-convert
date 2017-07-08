import cv2
import numpy as np
from os.path import join
from os import mkdir
from collections import OrderedDict
import xml.etree.ElementTree as ET

VIDEO_FILES = [
  # low res
  'IDOT_dataset/videos/193402_Main_St_(US_51_Bus)_and_Empire_St_(IL_9)_in_Bloomington_20141023_11am.mp4',
  'IDOT_dataset/videos/243948_IL_126_@_Ridge_Rd._001_20150625_10am.mp4',
  'IDOT_dataset/videos/245837_FAI-74_E_of_St._Joseph_in_Champaign_County_20150630_09am.mp4',
  'IDOT_dataset/videos/251035_Princeton_34_&_26_T_20150812_08am.mp4',
  'IDOT_dataset/videos/251950_IL_8_(E.Washington_St)_&_Illini_Dr_-_Farmdale_Rd_20150818_12pm.mp4',
  'IDOT_dataset/videos/252707_FAI-74_E_of_Lincoln_Ave_in_Urbana_20150826_09am.mp4',
  'IDOT_dataset/videos/intersection_4.avi',
  # ----------------------------------------------
  # high res
  'IDOT_dataset/videos/20150829_020000DST_ciceroPeterson.avi',
  'IDOT_dataset/videos/20150829_020000DST_elstonIrvingPark.avi',
  'IDOT_dataset/videos/20150918_150500DST_halsted.avi',
  'IDOT_dataset/videos/ILCHI_CHI003_20151010_075033_051.mp4',
  'IDOT_dataset/videos/ILCHI_CHI120_20151013_095039_099.mp4',
  'IDOT_dataset/videos/ILCHI_CHI164_20150930_125029_234.mp4',
]
ANNOTATION_FILES = [
  'IDOT_dataset/groundTruth/193402_Main_St_(US_51_Bus)_and_Empire_St_(IL_9)_in_Bloomington_20141023_11am.gt',
  'IDOT_dataset/groundTruth/243948_IL_126_@_Ridge_Rd._001_20150625_10am.gt',
  'IDOT_dataset/groundTruth/245837_FAI-74_E_of_St._Joseph_in_Champaign_County_20150630_09am.gt',
  'IDOT_dataset/groundTruth/251035_Princeton_34_&_26_T_20150812_08am.gt',
  'IDOT_dataset/groundTruth/251950_IL_8_(E.Washington_St)_&_Illini_Dr_-_Farmdale_Rd_20150818_12pm.gt',
  'IDOT_dataset/groundTruth/252707_FAI-74_E_of_Lincoln_Ave_in_Urbana_20150826_09am.gt',
  'IDOT_dataset/groundTruth/intersection_4.gt',
  # ----------------------------------------------
  'IDOT_dataset/groundTruth/20150829_020000DST_ciceroPeterson.gt',
  'IDOT_dataset/groundTruth/20150829_020000DST_elstonIrvingPark.gt',
  'IDOT_dataset/groundTruth/20150918_150500DST_halsted.gt',
  'IDOT_dataset/groundTruth/ILCHI_CHI003_20151010_075033_051.gt',
  'IDOT_dataset/groundTruth/ILCHI_CHI120_20151013_095039_099.gt',
  'IDOT_dataset/groundTruth/ILCHI_CHI164_20150930_125029_234.gt',
]


def read_annotation(fn, width, height, total_frames):
  frames_data = []
  for j in range(total_frames):
    frames_data.append(dict(
      frame_id=j,
      width=width,
      height=height,
      bboxes=[],
    ))
  raw_data = np.genfromtxt(fn, dtype=str)
  for entry in raw_data:
    # object_id x y width height frame_id if_lost if_occluded if_interpolated label
    # x and y same order in the YOLO9000 train set, no need to change format
    bbox = [int(entry[0]), int(entry[1]), int(entry[2]), int(entry[3]), int(entry[4])]
    frame_id = int(entry[5])
    difficult = int(entry[6])
    name = entry[7]
    frames_data[frame_id]['bboxes'].append(dict(
      bbox=bbox[1:5],
      difficult=difficult,
      name=name,
    ))
  return frames_data


def save_pascal_voc(fn, width, height, frame):
  annotation = ET.fromstring('<annotation></annotation>')
  ET.SubElement(annotation, 'filename').text = '{}.jpg'.format(frame['frame_id'])
  size = ET.SubElement(annotation, 'size')
  ET.SubElement(size, 'width').text = str(width)
  ET.SubElement(size, 'height').text = str(height)
  ET.SubElement(size, 'depth').text = str(3)
  for object in frame['bboxes']:
    bbox = object['bbox']
    name = object['name']
    xmin = bbox[0]
    ymin = bbox[1]
    xmax = bbox[0] + bbox[2] - 1
    ymax = bbox[1] + bbox[3] - 1
    object_xml = ET.SubElement(annotation, 'object')
    ET.SubElement(object_xml, 'name').text = name
    bndbox_xml = ET.SubElement(object_xml, 'bndbox')
    ET.SubElement(bndbox_xml, 'xmin').text = str(xmin)
    ET.SubElement(bndbox_xml, 'ymin').text = str(ymin)
    ET.SubElement(bndbox_xml, 'xmax').text = str(xmax)
    ET.SubElement(bndbox_xml, 'ymax').text = str(ymax)
  annot_str = ET.tostring(annotation)
  with open(fn, 'wb') as f:
    f.write(annot_str)


if __name__ == '__main__':
  try:
    mkdir('IDOT_dataset/xml')
  except:
    pass

  prev_total_frame = 0
  f_training = open('IDOT_dataset/train.txt', 'wb')
  f_testing = open('IDOT_dataset/test.txt', 'wb')
  for video, annotation in zip(VIDEO_FILES, ANNOTATION_FILES):
    print(annotation)
    vidcap = cv2.VideoCapture(video)
    frame_index = 1
    success = True
    width, height = None, None
    while success:
      success, image = vidcap.read()
      frame_index += 1
      if width is None:
        width, height, channels = image.shape
    total_frames_in_this_video = frame_index - 1
    num_training = int(float(total_frames_in_this_video) / 10.0 * 6)
    for idx in range(total_frames_in_this_video):
      if idx < num_training:
        f_training.write('{}\n'.format(prev_total_frame + idx + 1).encode())
      else:
        f_testing.write('{}\n'.format(prev_total_frame + idx + 1).encode())
    frames_data = read_annotation(annotation, width, height, total_frames_in_this_video)
    for frame_index, frame in enumerate(frames_data):
      save_pascal_voc(join('IDOT_dataset/xml', '{}.xml'.format(prev_total_frame + frame_index + 1)), width, height, frame)
    prev_total_frame += total_frames_in_this_video
  f_training.close()
  f_testing.close()
