import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input_path', type=str)
parser.add_argument('output_path', type=str)
parser.add_argument('index_file', type=str)
parser.add_argument('--file_ext', default='.xml', type=str)
args = parser.parse_args()

try:
  os.mkdir(args.output_path)
except:
  pass

files = open(args.index_file).read().splitlines()
for f in files:
  fn = os.path.basename(f)
  os.system('ln -s {} {}/{}.{}'.format(os.path.join(args.input_path, f + '.' + args.file_ext), args.output_path, fn, args.file_ext))
