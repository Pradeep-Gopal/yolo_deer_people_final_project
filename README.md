# YOLO_people_deer

#yolo_deer_detection

This repository consists of different YOLO object detection algorithms and steps on how to make them work on Jetson computers.

Google colab notebooks, trained models and datasets can be found here [link](https://drive.google.com/drive/folders/1fCbKae9NmMDIYQtCi8dkCWfjtlI-tBDp?usp=sharing)

The models were tested on Ubuntu, Windows 10 and deployed on Jetson Nano, Jetson TX2 running Ubuntu 18.04

- Ubuntu 18.04
- Tensorflow-GPU 2.3.1
- Pytorch 1.8.0
- CUDA 10.2
- cudnn 8.0
- python 3.6.9
- opencv 4.1.1

Tensorflow installation on Jetson Computers [Reference](https://forums.developer.nvidia.com/t/official-tensorflow-for-jetson-nano/71770)

```
sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran
sudo apt-get install python3-pip
sudo pip3 install -U pip
pip3 install Cython
pip3 install h5py==2.9.0
sudo pip3 install -U pip testresources setuptools numpy==1.16.1 future==0.17.1 mock==3.0.5 keras_preprocessing==1.0.5 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11
sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v44 tensorflow==2.3.1+nv20.12

```

For pytorch installation on Jetson Computers [Reference](https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-8-0-now-available/72048)

```
wget https://nvidia.box.com/shared/static/p57jwntv436lfrd78inwl7iml6p13fzh.whl -O torch-1.8.0-cp36-cp36m-linux_aarch64.whl
sudo apt-get install python3-pip libopenblas-base libopenmpi-dev 
pip3 install Cython
pip3 install numpy torch-1.8.0-cp36-cp36m-linux_aarch64.whl
```

For Torchvision installation
```
sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
git clone --branch <version> https://github.com/pytorch/vision torchvision   # see below for version of torchvision to download

Example:
git clone --branch v0.1.8 https://github.com/pytorch/vision torchvision

cd torchvision
export BUILD_VERSION=0.x.0  # where 0.x.0 is the torchvision version  
python3 setup.py install --user
cd ../  # attempting to load torchvision from build dir will result in import error
pip install 'pillow<7' # always needed for Python 2.7, not needed torchvision v0.5.0+ with Python 3.6

```
