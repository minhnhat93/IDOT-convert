cd ~/darkflow
# YOLO
CUDA_VISIBLE_DEVICES=0 flow --model cfg/yolo-idot.cfg --train --load bin/yolo.weights --dataset ~/IDOT-convert/IDOT_dataset/train/frames/ --annotation ~/IDOT-convert/IDOT_dataset/train/xml/ --labels idot-labels.txt --gpu 1.0 --batch 8 --keep 10 --save 4000 --lr 0.000001 --epoch 5
CUDA_VISIBLE_DEVICES=1 flow --model cfg/yolo-idot.cfg --train --load bin/yolo.weights --dataset ~/IDOT-convert/IDOT_dataset/train/frames/ --annotation ~/IDOT-convert/IDOT_dataset/train/xml/ --labels idot-labels.txt --gpu 1.0 --batch 8 --keep 10 --save 4000 --lr 0.000001 --epoch 5

CUDA_VISIBLE_DEVICES=0 flow --model cfg/yolo-idot.cfg --train --load bin/yolo.weights --dataset ~/IDOT-convert/IDOT_dataset/train/frames/ --annotation ~/IDOT-convert/IDOT_dataset/train/xml/ --labels idot-labels.txt --gpu 1.0 --batch 8 --keep 10 --save 4000 --lr 0.0000001 --epoch 10
CUDA_VISIBLE_DEVICES=1 flow --model cfg/yolo-idot.cfg --train --load bin/yolo.weights --dataset ~/IDOT-convert/IDOT_dataset/train/frames/ --annotation ~/IDOT-convert/IDOT_dataset/train/xml/ --labels idot-labels.txt --gpu 1.0 --batch 8 --keep 10 --save 4000 --lr 0.0000001 --epoch 10
