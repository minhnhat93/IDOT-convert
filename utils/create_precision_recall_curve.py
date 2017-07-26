import _pickle
import argparse
import numpy as np

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('fn', type=str)
    return parser.parse_args()

args = parse_arg()

rec, prec, scores = _pickle.load(open(args.fn, 'rb'))

#print('Recall@0.0: {}'.format(rec[-1])
#print('Precision@0.0: {}'.format(rec[-1])
print('Recall and Precision at various threshold: ')
max_threshold = scores.max()
for threshold in np.arange(0.0, max_threshold, 0.05):
    index = (scores > threshold).astype(int).sum() - 1
    print('Threshold: {:.2f}, Recall: {:.2f}, Precision: {:.2f}'.format(threshold, rec[index], prec[index]))
