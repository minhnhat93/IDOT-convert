#!/usr/bin/env bash
./darknet detector train ~/darknet-finetune/gram_finetune/gram.data ~/darknet-finetune/gram_finetune/gram.cfg /data/darknet-finetune-weights/gram-finetune/gram.backup -gpus 0