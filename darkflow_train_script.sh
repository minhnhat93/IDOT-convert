cd ~/darkflow
CUDA_VISIBLE_DEVICES=0 flow --model cfg/yolo-idot.cfg --train --load bin/yolo.weights --dataset /home/nhat/IDOT-convert/IDOT_dataset/train/frames --annotation /home/nhat/IDOT-convert/IDOT_dataset/train/xml --labels /home/nhat/darkflow/idot-labels.txt --gpu 1.0 --batch 8 
CUDA_VISIBLE_DEVICES=1 flow --model cfg/yolo-idot.cfg --train --load bin/yolo.weights --dataset /home/nhat/IDOT-convert/IDOT_dataset/train/frames --annotation /home/nhat/IDOT-convert/IDOT_dataset/train/xml --labels /home/nhat/darkflow/idot-labels.txt --gpu 1.0 --batch 8
