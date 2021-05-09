# TensorFlow-2-YOLOv3-Tiny

YOLOv3 implementation in TensorFlow 2.3.1
The model was trained using the Google colab notebook found in this directory

The model was tested on Ubuntu, Windows 10 and deployed on Jetson Nano running Ubuntu 18.04
- NVIDIA Jetson Nano
- Ubuntu 18.04
- Tensorflow-GPU 2.3.1
- CUDA 10.2
- cudnn 8.0
- python 3.6.9
- opencv 4.1.1
- scipy 1.3.3
- pytorch 1.6.0

Pytorch installation on Jetson Nano - Follow the steps found in the below google drive link
https://docs.google.com/document/d/1z0lKeZDvQrDsDrRvyvS4GCktFFPxj81pRc38kaPXbcY/edit?usp=sharing


Steps to Test the Model
```
git clone https://github.com/Easton-Robotics/yolo_deer_detection.git 
cd yolov5_deer_detection
```

Download the yolov5.tar.xz from the following link and extract the contents to yolov5_deer_detection
https://drive.google.com/file/d/13ktWqDcG0TGm7G-tk3CoFHR7Di00M1eO/view?usp=sharing
To run the detection script,

```
python detect.py --weights best.pt --img 416 --conf 0.4 --source test
```

