# Pose Estimation

![content-concepts-raw-computer-vision-pose-estimation-img](https://user-images.githubusercontent.com/62965911/216822795-bdcc650d-08c1-4e8a-9b67-f3a8a0aba2a5.png)

## Introduction

- **Definition:** Pose estimation is a computer vision task that infers the pose of a person or object in an image or video. This is typically done by identifying, locating, and tracking the number of key points on a given object or person. For objects, this could be corners or other significant features. And for humans, these key points represent major joints like an elbow or knee.
- **Applications:** Activity recognition, motion capture, fall detection, plank pose corrector, yoga pose identifier, body ration estimation
- **Scope:** 2D skeleton map, Human Poses, Single and Multi-pose, Real-time
- **Tools:** Tensorflow PoseNet API

## Models

### OpenPose

*[OpenPose: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields. arXiv, 2016.](https://arxiv.org/abs/1812.08008)*

A standard bottom-up model that supports real-time multi-person 2D pose estimation. The authors of the paper have shared two models – one is trained on the Multi-Person Dataset ( MPII ) and the other is trained on the COCO dataset. The COCO model produces 18 points, while the MPII model outputs 15 points.

### PoseNet

PoseNet is a machine learning model that allows for Real-time Human Pose Estimation. PoseNet can be used to estimate either a single pose or multiple poses PoseNet v1 is trained on MobileNet backbone and v2 on ResNet backbone.

![content-concepts-raw-computer-vision-pose-estimation-slide52](https://user-images.githubusercontent.com/62965911/216822796-8d922553-a504-43cf-9718-2ef84a23bc0b.png)

## Process flow

Step 1: Collect Images

Capture via camera, scrap from the internet or use public datasets

Step 2: Create Labels

Use a pre-trained model like PoseNet, OpenPose to identify the key points. These key points are our labels for pose estimation based classification task. If the model is not compatible/available for the required key points (e.g. identify the cap and bottom of a bottle product to measure if manufacturing is correct), we have to first train a pose estimation model using transfer learning in that case (this is out of scope though, as we are only focusing on human poses and pre-trained models are already available for this use case)

Step 3: Data Preparation

Setup the database connection and fetch the data into the environment. Explore the data, validate it, and create a preprocessing strategy. Clean the data and make it ready for modeling

Step 4: Model Building

Create the model architecture in python and perform a sanity check. Start the training process and track the progress and experiments. Validate the final set of models and select/assemble the final model

Step 5: UAT Testing

Wrap the model inference engine in API for client testing

Step 6: Deployment

Deploy the model on cloud or edge as per the requirement

Step 7: Documentation

Prepare the documentation and transfer all assets to the client

## Use Cases

### OpenPose Experiments

Four types of experiments with pre-trained OpenPose model - Single and Multi-Person Pose Estimation with OpenCV, Multi-Person Pose Estimation with PyTorch and Pose Estimation on Videos. Check out [this](https://www.notion.so/Pose-Estimation-with-OpenPose-2D8F5-7f01bee1534243f3836728d03a419969) notion.

### Pose Estimation Inference Experiments

Experimented with pre-trained pose estimation models. Check out [this](https://www.notion.so/Pose-Estimation-with-OpenPifPaf-7517E-8cb982455e01478e876c52e9324d8e6b) notion for experiments with the OpenPifPaf model, [this](https://www.notion.so/Pose-Estimation-with-Keypoint-RCNN-in-TorchVision-96e6aad0f36f44d3bff28e60525c6d31) one for the TorchVision Keypoint R-CNN model, and [this](https://www.notion.so/Detectron-2-D281D-bb7f769860fa434d923feef3a99f9cbb) notion for the Detectron2 model.

### Pose Detection on the Edge

Train the pose detector using Teachable machine, employing the PoseNet model (multi-person real-time pose estimation) as the backbone and serve it to the web browser using ml5.js. This system will infer the end-users pose in real-time via a web browser. Check out [this](https://teachablemachine.withgoogle.com/train/pose) link and [this](https://www.notion.so/ml5-js-Pose-Estimation-with-PoseNet-5661cefe46b449998cc31838441dc26a) notion.

### Pose Detection on the Edge using OpenVINO

Optimize the pre-trained pose estimation model using the OpenVINO toolkit to make it ready to serve at the edge (e.g. small embedded devices) and create an OpenVINO inference engine for real-time inference. Check out [this](https://www.notion.so/OpenVINO-4c4fc4f167cc4601ade5795a241a60da) notion.
