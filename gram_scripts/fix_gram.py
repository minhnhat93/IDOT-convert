from utils.annotation_parsing import fix_GRAM_RTM_annotation
from os.path import join

ANNOTATION_DIR = '/home/nhat/engage-project/dataset/GRAM-RTM/GRAM-RTMv4/Annotations'

fix_GRAM_RTM_annotation(join(ANNOTATION_DIR, 'M-30', 'xml'), join(ANNOTATION_DIR, 'M-30', 'xml-fixed'))
fix_GRAM_RTM_annotation(join(ANNOTATION_DIR, 'M-30-HD', 'xml'), join(ANNOTATION_DIR, 'M-30-HD', 'xml-fixed'))
fix_GRAM_RTM_annotation(join(ANNOTATION_DIR, 'Urban1', 'xml'), join(ANNOTATION_DIR, 'Urban1', 'xml-fixed'))
