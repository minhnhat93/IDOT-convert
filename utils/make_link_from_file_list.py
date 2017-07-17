import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input_path', type=str)
parser.add_argument('output_path', type=str)
args = parser.parse_args()

try:
  os.mkdir(args.output_path)
except:
  pass

files = open('IDOT_dataset/test_index.txt').read().splitlines()
for f in files:
  fn = os.path.basename(f)
  os.system('ln -s {} {}/{}'.format(f, args.output_path, fn))
