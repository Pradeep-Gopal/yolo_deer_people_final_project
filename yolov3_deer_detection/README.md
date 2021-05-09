# TensorFlow-2-YOLOv3

YOLOv3 implementation in TensorFlow 2.3.1
The model was trained with following specs:
- MSI GS65 with RTX 2060, 32Gb RAM
- OS Windows 10
- CUDA 10.2
- cudnn 7
- Tensorflow-GPU 2.2.0
- python 3.6.3
- opencv 4.5.1

The model was tested on Ubuntu, Windows 10 and deployed on Jetson computers running Ubuntu 18.04

- Ubuntu 18.04
- Tensorflow-GPU 2.3.1
- CUDA 10.2
- cudnn 8.0
- python 3.6.9
- opencv 4.1.1


Steps to Run the Model
```
cd yolov3_deer_detection
```

Download the checkpoints folder and extract it inside yolov3_deer_detection
[download link](https://drive.google.com/drive/folders/1r4eikcn5-uqjL4VQSWR2Sh7PdG85DhhH?usp=sharing)

Download the model_data folder and extract it inside yolov3_deer_detection
[download link](https://drive.google.com/drive/folders/1SDcu8qR2NbZh-613enbxMIE_l2vb-694?usp=sharing)


To run the detection script,
```
python detection_custom.py
```

To train your own custom model, use API like LabelImg or some other software to label the images and paste the dataset in the custom dataset folder.
- Edit the XML_to_YOLOv3.py to choose the data_dir, dataset_names_path, dataset_train, dataset_test and run the file.

```
cd tools/
python XML_to_YOLOV3.py
```
This will generate the names.txt, train.txt and test.txt files which will be used for training.

Next step is to run the train.py

```
cd ..
python train.py
```

The trained model can be found in the checkpoints folder

Reference: https://www.youtube.com/watch?v=1A8B5Yy4tps



