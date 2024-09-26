#!/bin/sh
LEARNING_RATE=0.0001
WEIGHT_DECAY=0.0001
RUN=1
MODEL=resnet18
IMAGE_REP=Skeleton-DML

python train_minds.py -vp 1 -tp 2 -lr $LEARNING_RATE -wd $WEIGHT_DECAY -d minds -im $IMAGE_REP -m $MODEL -r $RUN
