#!/usr/bin/env bash
IMAGE_DIR=/home/nhat/engage-project/dataset/GRAM-RTM/GRAM-RTMv4/Images
PARENT_DIR=$(dirname ${IMAGE_DIR})
CURR_DIR=$(pwd)

for DATASET in M-30 M-30-HD Urban1
do
  mkdir ${PARENT_DIR}/${DATASET}
  mv ${IMAGE_DIR}/${DATASET} ${PARENT_DIR}/${DATASET}/images
  cd ${PARENT_DIR}/${DATASET}/images
  NO_OF_FILES=$(ls | wc -l)
  for ((i=0; i<${NO_OF_FILES}; i++))
  do
    old_fn=$(printf "image%06d.jpg" $((i+1)))
    new_fn=$(printf "%d.jpg" ${i})
    mv ${old_fn} ${new_fn}
  done
done