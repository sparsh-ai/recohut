# Object Detection

![content-concepts-raw-computer-vision-object-detection-slide29](https://user-images.githubusercontent.com/62965911/216822793-68a55d64-a10e-4ae2-aa2b-53c3c8100117.png)

## Introduction

- **Definition:** Object detection is a computer vision technique that allows us to identify and locate objects in an image or video.
- **Applications:** Crowd counting, Self-driving cars, Video surveillance, Face detection, Anomaly detection
- **Scope:** Detect objects in images and videos, 2-dimensional bounding boxes, Real-time
- **Tools:** Detectron2, TF Object Detection API, OpenCV, TFHub, TorchVision

## Models

### Faster R-CNN

*[Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks. arXiv, 2016.](https://arxiv.org/abs/1506.01497)*

### SSD (Single Shot Detector)

*[SSD: Single Shot MultiBox Detector. CVPR, 2016.](https://arxiv.org/abs/1512.02325)*

### YOLO (You Only Look Once)

[*YOLOv3: An Incremental Improvement. arXiv, 2018.*](https://arxiv.org/abs/1804.02767)

### EfficientDet

*[EfficientDet: Scalable and Efficient Object Detection. CVPR, 2020.](https://arxiv.org/abs/1911.09070)*

It achieved 55.1 AP on COCO test-dev with 77M parameters.

## Process flow

Step 1: Collect Images

Capture via camera, scrap from the internet or use public datasets

Step 2: Create Labels

This step is required only if the object category is not available in any pre-trained model or labels are not freely available on the web. To create the labels (bounding boxes) using either open-source tools like Labelme or any other professional tool.

Step 3: Data Acquisition

Setup the database connection and fetch the data into python environment

Step 4: Data Exploration

Explore the data, validate it and create preprocessing strategy

Step 5: Data Preparation

Clean the data and make it ready for modeling

Step 6: Model Building

Create the model architecture in python and perform a sanity check

Step 7: Model Training

Start the training process and track the progress and experiments

Step 8: Model Validation

Validate the final set of models and select/assemble the final model

Step 9: UAT Testing

Wrap the model inference engine in API for client testing

Step 10: Deployment

Deploy the model on cloud or edge as per the requirement

Step 11: Documentation

Prepare the documentation and transfer all assets to the client

## Use Cases

### Automatic License Plate Recognition

Recognition of vehicle license plate number using various methods including YOLO4 object detector and Tesseract OCR. Checkout the notion [here](https://www.notion.so/Automatic-License-Plate-Recognition-10ec22181b454b1facc99abdeadbf78f).

### Object Detection App

This is available as a streamlit app. It detects common objects. 3 models are available for this task - Caffe MobileNet-SSD, Darknet YOLO3-tiny, and Darknet YOLO3. Along with common objects, this app also detects human faces and fire. Checkout the notion [here](https://www.notion.so/Object-Detector-App-c60fddae2fcd426ab763261436fb15d8).

### Logo Detector

Build a REST API to detect logos in images. API will receive 2 zip files - 1) a set of images in which we have to find the logo and 2) an image of the logo. Deployed the model in AWS Elastic Beanstalk. Checkout the notion [here](https://www.notion.so/Logo-Detection-91bfe4953dcf4558807b342efe05a9ff).

### TF Object Detection API Experiments

The TensorFlow Object Detection API is an open-source framework built on top of TensorFlow that makes it easy to construct, train, and deploy object detection models. We did inference on pre-trained models, few-shot training on single class, few-shot training on multiple classes and conversion to TFLite model. Checkout the notion [here](https://www.notion.so/Tensorflow-Object-Detection-API-499b017e502d4950a9d448fb35a41d58).

### Pre-trained Inference Experiments

Inference on 6 pre-trained models - Inception-ResNet (TFHub), SSD-MobileNet (TFHub), PyTorch YOLO3, PyTorch SSD, PyTorch Mask R-CNN, and EfficientDet. Checkout the notion [here](https://www.notion.so/Object-Detection-Inference-Experiments-568fa092b1d34471b676fd43a42974b2) and [here](https://www.notion.so/Object-Detection-Inference-with-Pre-trained-models-da9e2e5bfab944bc90f568f6bc4b3e1f).

### Object Detection App

TorchVision Mask R-CNN model Gradio App. Checkout the notion [here](https://www.notion.so/MaskRCNN-TorchVision-Object-Detection-Gradio-App-c22f2a13ab63493b9b38720b20c50051).

### Real-time Object Detector in OpenCV

Build a model to detect common objects like scissors, cups, bottles, etc. using the MobileNet SSD model in the OpenCV toolkit. It will task input from the camera and detect objects in real-time. Checkout the notion [here](https://www.notion.so/Object-Detection-with-OpenCV-MobileNet-SSD-38ff496d2f0d427185a9c51cebc1ddf2). Available as a Streamlit app also (this app is not real-time).

### EfficientDet Fine-tuning

Fine-tune YOLO4 model on new classes. Checkout the notion [here](https://www.notion.so/EfficientDet-fine-tuning-01a6ffd1e11f4dc1941073aff4b9b486).

### YOLO4 Fine-tuning

Fine-tune YOLO4 model on new classes. Checkout the notion [here](https://www.notion.so/YOLO-4-b32c2d2a4b8644b59f1c05e6887ffcca).

### Detectron2 Fine-tuning

Fine-tune Detectron2 Mask R-CNN (with PointRend) model on new classes. Checkout the notion [here](https://www.notion.so/YOLO-4-b32c2d2a4b8644b59f1c05e6887ffcca).
