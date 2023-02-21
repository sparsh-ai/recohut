# Facial Analytics

![content-concepts-raw-computer-vision-facial-analytics-img](https://user-images.githubusercontent.com/62965911/216822789-86a34319-c100-48be-9581-ea5671cca059.png)

## Introduction

- **Definition:** Analyze the facial features like age, gender, emotion, and identity.
- **Applications:** Identity verification, emotion detection
- **Scope:** Human faces only, Real-time
- **Tools:** OpenCV, dlib

## Models

### FaceNet

*[FaceNet: A Unified Embedding for Face Recognition and Clustering. CVPR, 2015.](https://openaccess.thecvf.com/content_cvpr_2015/papers/Schroff_FaceNet_A_Unified_2015_CVPR_paper.pdf)*

### RetinaFace

*[RetinaFace: Single-stage Dense Face Localisation in the Wild. arXiv, 2019.](https://arxiv.org/abs/1905.00641v2)*

### FER+

*[Training Deep Networks for Facial Expression Recognition with Crowd-Sourced Label Distribution. arXiv, 2016.](https://arxiv.org/abs/1608.01041v2)*

## Process flow

Step 1: Collect Images

Capture via camera, scrap from the internet or use public datasets

Step 2: Create Labels

Compile a metadata table containing a unique id (preferably the same as the image name) for each face id.

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

### Automatic Attendance System via Webcam

We use Face Recognition library and OpenCV to create a real-time webcam-based attendance system that will automatically recognizes the face and log an attendance into the excel sheet. Check out [this](https://www.notion.so/Face-Recognition-based-Automated-Attendance-System-dfb6f70527994ea4be11caf69b054350) notion.

### Detectron2 Fine-tuning for face detection

Fine-tuned detectron2 on human face dataset to detect the faces in images and videos. Check out [this](https://www.notion.so/Detectron-2-D281D-bb7f769860fa434d923feef3a99f9cbb) notion.
