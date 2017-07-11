cd ~/darkflow
# YOLO
CUDA_VISIBLE_DEVICES=0 flow --model cfg/yolo-idot.cfg --train --load bin/yolo.weights --dataset ~/IDOT-convert/IDOT_dataset/train/frames/ --annotation ~/IDOT-convert/IDOT_dataset/train/xml/ --labels idot-labels.txt --gpu 1.0 --batch 8 --keep 10 --save 4000 --lr 0.00001
CUDA_VISIBLE_DEVICES=1 flow --model cfg/yolo-idot.cfg --train --load bin/yolo.weights --dataset ~/IDOT-convert/IDOT_dataset/train/frames/ --annotation ~/IDOT-convert/IDOT_dataset/train/xml/ --labels idot-labels.txt --gpu 1.0 --batch 8 --keep 10 --save 4000 --lr 0.00001
# YOLO-VOC
CUDA_VISIBLE_DEVICES=0 flow --model cfg/yolo-voc-idot.cfg --train --load bin/yolo-voc.weights --dataset /home/nhat/IDOT-convert/IDOT_dataset/train/frames --annotation /home/nhat/IDOT-convert/IDOT_dataset/train/xml --labels /home/nhat/darkflow/idot-labels.txt --gpu 1.0 --batch 16 --keep 10 --save 4000 --lr 0.00001
CUDA_VISIBLE_DEVICES=1 flow --model cfg/yolo-voc-idot.cfg --train --dataset /home/nhat/IDOT-convert/IDOT_dataset/train/frames --annotation /home/nhat/IDOT-convert/IDOT_dataset/train/xml --labels /home/nhat/darkflow/idot-labels.txt --gpu 1.0 --batch 16 --keep 10 --save 4000 --lr 0.00001
# TINY
CUDA_VISIBLE_DEVICES=0 flow --model cfg/tiny-yolo-voc-idot.cfg --train --load bin/yolo-voc.weights --dataset /home/nhat/IDOT-convert/IDOT_dataset/train/frames --annotation /home/nhat/IDOT-convert/IDOT_dataset/train/xml --labels /home/nhat/darkflow/idot-labels.txt --gpu 1.0 --batch 16 --keep 10 --save 4000 --lr 0.00001
