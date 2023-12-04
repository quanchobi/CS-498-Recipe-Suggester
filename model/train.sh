#!/usr/bin/env bash

# Trains a dataset with input dataset
yolo task=detect \
mode=train \
model=yolov8s.pt \
data=./dataset/data.yaml \
epochs=100 \
imgsz=640

