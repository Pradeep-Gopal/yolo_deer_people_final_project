## Yolov4 tiny Deploying Instructions for NVIDIA Jetson Computers

1. Clone the Darknet repository from github

cd ${HOME}/project
git clone https://github.com/AlexeyAB/darknet.git
cd darknet

2. Modify the first few lines of “Makefile” as follows. Note that CUDA architecture of Jetson Nano is “53”, while TX2 “62” and AGX Xavier “72” [Reference](https://developer.nvidia.com/cuda-gpus) 

```
GPU=1
CUDNN=1
CUDNN_HALF=1
OPENCV=1
AVX=0
OPENMP=1
LIBSO=1
ZED_CAMERA=0
ZED_CAMERA_v2_8=0

......

USE_CPP=0
DEBUG=0

ARCH= -gencode arch=compute_53,code=[sm_53,compute_53]

```

Find the sample Makefile in the yolov4_deer_people directory. Edit the Makefile lines 43 - 47 to support NVIDIA nano and TX2 accordingly.

3. Build the code with “make”. The executable, “darknet”, should be generated when done.

```
make
```

4. Set Jetson Nano to max performance mode (only for Nano)

```
sudo nvpmodel -m 0
sudo jetson_clocks
```

5. Download the trained weights - custom-yolov4-detector_best.weights and config for two classes - custom-yolov4-detector.cfg for yolov4 to detect people and deer from Google Drive and save it in the darknet directory

[download link](https://drive.google.com/drive/folders/1IJUCA0dISDsKr61UAFPrdz0S27UpNLjU?usp=sharing)

6. Download test dataset and store it in the darknet directory
[download link](https://drive.google.com/file/d/152A5n42lOL66NeNRTdyzUWygMnWD0e4T/view?usp=sharing)

7. Edit darknet_video.py and change the "from queue import Queue" to "from Queue import *"

8. Edit the data/coco.names file with the classes used to train the model. In our case, edit the file and add,
```
deer
people
```

9. Edit the cfg/coco.data file as follows,

```
classes= 2
train  = /home/pjreddie/data/coco/trainvalno5k.txt
valid  = coco_testdev
#valid = data/coco_val_5k.list
names = data/coco.names
backup = /home/pjreddie/backup/
eval=coco
```

10. 8. Edit the cfg/coco.names file with the classes used to train the model. In our case, edit the file and add,
```
deer
people
```

11. Run the detection using the following script

```
python darknet_video.py --input deer_video_1.mp4 --out_filename output_video.mp4 --weights yolov4_tiny_2000deer_300people_92_70.weights --config_file cfg/custom-yolov4-tiny-detector_2_classes.cfg
```



