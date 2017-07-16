from utils.annotation_parsing import parse_pascal_voc_groundtruth, write_darknet_labels
from os.path import join

DATA_DIR='/home/nhat/engage-project/dataset/GRAM-RTM/GRAM-RTMv4'
for dataset in ['M-30', 'M-30-HD', 'Urban1']:
  annotation_path = join(DATA_DIR, 'Annotations', dataset, 'xml-fixed')
  out_path = join(DATA_DIR, dataset, 'labels')
  frames = parse_pascal_voc_groundtruth(annotation_path)
  write_darknet_labels(out_path, frames, ['vehicle'], '{}.txt')
