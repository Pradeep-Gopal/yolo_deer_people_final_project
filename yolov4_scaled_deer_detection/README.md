# Pytorch implementation of scaled yolov4

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
- pytorch 1.8.0

Pytorch installation on Jetson Nano - Follow the steps found in the below google drive link
https://drive.google.com/file/d/1gsnjuYSxC2CeZxzenfRyYAVnqPj3TEls/view?usp=sharing

Install mish activation funciton for cuda
```
git clone https://github.com/JunnYu/mish-cuda
cd mish-cuda
sudo python3 setup.py build install
pip3 install image
pip3 install tqdm
pip3 install matplotlib
```

Steps to Test the Model
```
git clone https://github.com/Easton-Robotics/yolo_deer_detection.git 
cd yolov4_scaled_deer_detection
```

Download the best.pt from the following link and extract the contents to yolov4_scaled_deer_detection

[link](https://drive.google.com/file/d/1mbmg1j3dorVJZ_ntSDCHlRLjXRkYM1mL/view?usp=sharing)

To run the detection script,

```
python3 detect.py --weights best.pt --img 416 --conf 0.4 --source test
```

