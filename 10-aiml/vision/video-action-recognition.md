# Video Action Recognition

![content-concepts-raw-computer-vision-video-action-recognition-img](https://user-images.githubusercontent.com/62965911/216822803-052c478d-b961-487b-a68f-702948660afc.png)

## **Introduction**

- **Definition:** This is the task of identifying human activities/actions (e.g. eating, playing) in videos. In other words, this task classifies segments of videos into a set of pre-defined categories.
- **Applications:** Automated surveillance, elderly behavior monitoring, human-computer interaction, content-based video retrieval, and video summarization.
- **Scope:** Human Action only
- **Tools:** OpenCV

## **Models**

### 3D-ResNet

***[Can Spatiotemporal 3D CNNs Retrace the History of 2D CNNs and ImageNet?](https://arxiv.org/abs/1711.09577)***

the authors explore how existing state-of-the-art 2D architectures (such as ResNet, ResNeXt, DenseNet, etc.) can be extended to video classification via 3D kernels.

### R(2+1)D

This model was pre-trained on 65 million social media videos and fine-tuned on Kinetics400.

## Process flow

Step 1: Collect videos

Capture via camera, scrap from the internet or use public datasets

Step 2: Create Labels

Use open-source tools like VGA Video Annotator for video annotation

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

### Kinetics 3D CNN Human Activity Recognition

This dataset consists of 400 human activity recognition classes, at least 400 video clips per class (downloaded via YouTube) and a total of 300,000 videos. Check out [this](https://www.notion.so/Kinetics-3D-CNN-Human-Activity-Recognition-fd10fd7b5858459cba65dc4a6cb73630) notion.

### Action Recognition using R(2+1)D Model

VGA Annotator was used for creating the video annotation for training. Check out [this](https://www.notion.so/Action-Recognition-using-R-2-1-D-Model-4c796f308aed40f29fc230a757af98e8) notion.
