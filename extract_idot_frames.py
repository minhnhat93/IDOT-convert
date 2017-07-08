import cv2
import numpy as np
from os.path import join
from os import mkdir
from collections import OrderedDict
import xml.etree.ElementTree as ET

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


if __name__ == '__main__':
  try:
    mkdir('IDOT_dataset/frames')
  except:
    pass

  prev_total_frame = 0
  for video in VIDEO_FILES:
    print(video)
    vidcap = cv2.VideoCapture(video)
    frame_index = 1
    success = True
    width, height = None, None
    while success:
      success, image = vidcap.read()
      cv2.imwrite(join('IDOT_dataset/frames', "{}.jpg".format(frame_index + prev_total_frame)), image)     # save frame as JPEG file
      frame_index += 1
      if width is None:
        width, height, channels = image.shape
    total_frames_in_this_video = frame_index - 1
    prev_total_frame += total_frames_in_this_video
