import cv2
import numpy as np
from os.path import join
from os import mkdir
VIDEO_FILES = [
'IDOT_dataset/videos/193402_Main_St_(US_51_Bus)_and_Empire_St_(IL_9)_in_Bloomington_20141023_11am.mp4',
'IDOT_dataset/videos/243948_IL_126_@_Ridge_Rd._001_20150625_10am.mp4',
'IDOT_dataset/videos/245837_FAI-74_E_of_St._Joseph_in_Champaign_County_20150630_09am.mp4',
'IDOT_dataset/videos/251035_Princeton_34_&_26_T_20150812_08am.mp4',
'IDOT_dataset/videos/251950_IL_8_(E.Washington_St)_&_Illini_Dr_-_Farmdale_Rd_20150818_12pm.mp4',
'IDOT_dataset/videos/252707_FAI-74_E_of_Lincoln_Ave_in_Urbana_20150826_09am.mp4',
'IDOT_dataset/videos/20150829_020000DST_ciceroPeterson.avi',
'IDOT_dataset/videos/20150829_020000DST_elstonIrvingPark.avi',
'IDOT_dataset/videos/20150918_150500DST_halsted.avi',
'IDOT_dataset/videos/ILCHI_CHI003_20151010_075033_051.mp4',
'IDOT_dataset/videos/ILCHI_CHI120_20151013_095039_099.mp4',
'IDOT_dataset/videos/ILCHI_CHI164_20150930_125029_234.mp4',
'IDOT_dataset/videos/intersection_4.avi',
]
ANNOTATION_FILES = [
'IDOT_dataset/groundTruth/193402_Main_St_(US_51_Bus)_and_Empire_St_(IL_9)_in_Bloomington_20141023_11am.gt',
'IDOT_dataset/groundTruth/243948_IL_126_@_Ridge_Rd._001_20150625_10am.gt',
'IDOT_dataset/groundTruth/245837_FAI-74_E_of_St._Joseph_in_Champaign_County_20150630_09am.gt',
'IDOT_dataset/groundTruth/251035_Princeton_34_&_26_T_20150812_08am.gt',
'IDOT_dataset/groundTruth/251950_IL_8_(E.Washington_St)_&_Illini_Dr_-_Farmdale_Rd_20150818_12pm.gt',
'IDOT_dataset/groundTruth/252707_FAI-74_E_of_Lincoln_Ave_in_Urbana_20150826_09am.gt',
'IDOT_dataset/groundTruth/20150829_020000DST_ciceroPeterson.gt',
'IDOT_dataset/groundTruth/20150829_020000DST_elstonIrvingPark.gt',
'IDOT_dataset/groundTruth/20150918_150500DST_halsted.gt',
'IDOT_dataset/groundTruth/ILCHI_CHI003_20151010_075033_051.gt',
'IDOT_dataset/groundTruth/ILCHI_CHI120_20151013_095039_099.gt',
'IDOT_dataset/groundTruth/ILCHI_CHI164_20150930_125029_234.gt',
'IDOT_dataset/groundTruth/intersection_4.gt',
]

OUTPUT_DIR = 'IDOT_dataset/frames'

def read_gt(fn, total_frames):
  frame_data = [[]] * total_frames
  raw_data = np.genfromtxt(fn, dtype=str)
  for entry in raw_data:
    # object_id x y width height frame_id if_lost if_occluded if_interpolated label
    # x and y same order in the YOLO9000 train set, no need to change format
    bbox = [int(entry[0]), float(entry[1]), float(entry[2]), float(entry[3]), float(entry[4])]
    frame_id = int(entry[5])
    difficult = int(entry[6])
    name = entry[7]
    frame_data[frame_id].append(dict(
      bbox=bbox[1:5],
      difficult=difficult,
      name=name,
    ))
  return frame_data

try:
  mkdir('IDOT_dataset/frames')
except:
  pass

prev_total_count = 0
for video, annotation in zip(VIDEO_FILES, ANNOTATION_FILES):
  vidcap = cv2.VideoCapture(video)
  frame_index = 1
  success = True
  while success:
    success, image = vidcap.read()
    print('Read a new frame {}: '.format(frame_index), success)
    cv2.imwrite(join(OUTPUT_DIR, "{}.jpg".format(frame_index + prev_total_count)), image)     # save frame as JPEG file
    frame_index += 1
  total_frames_in_this_video = frame_index - 1
