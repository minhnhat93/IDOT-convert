import os

def get_no_file(dir_name):
  return len([name for name in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, name))])

DATA_DIR='/home/nhat/engage-project/dataset/GRAM-RTM/GRAM-RTMv4'
f_train = open('gram_finetune/gram_train.txt', 'w')
f_test = open('gram_finetune/gram_test.txt', 'w')
for dataset in ['M-30', 'M-30-HD', 'Urban1']:
  no_files = get_no_file(os.path.join(DATA_DIR, dataset, 'images'))
  no_train = int(no_files / 10.0 * 6)
  for i in range(no_files):
    if i < no_train:
      f_train.write('{}\n'.format(os.path.join(DATA_DIR, dataset, 'images-masked', '{}.jpg'.format(i))))
    else:
      f_test.write('{}\n'.format(os.path.join(DATA_DIR, dataset, 'images-masked', '{}.jpg'.format(i))))
f_train.close()
f_test.close()
