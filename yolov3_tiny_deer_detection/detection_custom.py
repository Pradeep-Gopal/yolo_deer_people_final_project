
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import tensorflow as tf
from yolov3.utils import detect_image, detect_realtime, detect_video, Load_Yolo_model, detect_video_realtime_mp
from yolov3.configs import *

image_path   = "./test_images_and_videos/deer_backside.jpg"
video_path   = "deer_video_1.mp4"

yolo = Load_Yolo_model()
# detect_image(yolo, image_path, "./test_images_and_videos/deer_backside.jpg", input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
detect_video(yolo, video_path, 'deer_output.mp4', input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0))
#detect_realtime(yolo, '', input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255, 0, 0))

#detect_video_realtime_mp(video_path, "Output.mp4", input_size=YOLO_INPUT_SIZE, show=True, CLASSES=TRAIN_CLASSES, rectangle_colors=(255,0,0), realtime=False)
