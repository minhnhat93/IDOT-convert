from annotation_parsing import parse_json_detection, write_MOT_detection
import argparse
import os

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('input_path', type=str)
  parser.add_argument('output_path', type=str)
  parser.add_argument('--threshold', default=0.0, type=float)
  return parser.parse_args()

args = parse_args()
data = parse_json_detection(args.input_path)

write_MOT_detection(args.output_path, data, args.threshold)
