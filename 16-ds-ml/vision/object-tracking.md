# Object Tracking

![content-concepts-raw-computer-vision-object-tracking-img](https://user-images.githubusercontent.com/62965911/216822794-bbebf98d-269b-46f7-bd51-aa9f417105c8.png)

## Introduction

- **Definition: Object tracking is the process of 1)** Taking an initial set of object detections (such as an input set of bounding box coordinates, 2) Creating a unique ID for each of the initial detections, and then 3) tracking each of the objects as they move around frames in a video, maintaining the assignment of unique IDs.
- **Applications:** In-store consumer behavior tracking, Apply security policies like crowd management, traffic management, vision-based control, human-computer interface, medical imaging, augmented reality, robotics.
- **Scope:** Track objects in images and videos, 2-dimensional tracking, Bounding boxes and pixel masks, Single and Multiple Object Tracking
- **Tools:** Detectron2, OpenCV

## Models

### FairMOT

*[On the Fairness of Detection and Re-Identification in Multiple Object Tracking. arXiv, 2020.](https://arxiv.org/abs/2004.01888)*

### DeepSORT

*[Simple Online and Realtime Tracking with a Deep Association Metric. arXiv, 2017.](https://arxiv.org/abs/1703.07402)*

Detect object with models like YOLO or Mask R-CNN and then track using DeepSORT.

### GOTURN

*[Learning to Track at 100 FPS with Deep Regression Networks. arXiv, 2016.](https://arxiv.org/abs/1604.01802)*

CNN offline learning tracker.

### MDNet

*[Real-Time MDNet. arXiv, 2018.](https://arxiv.org/abs/1808.08834)*

CNN online learning tracker.

### ROLO

*[Spatially Supervised Recurrent Convolutional Neural Networks for Visual Object Tracking. arXiv, 2016.](https://arxiv.org/abs/1607.05781)*

CNN + LSTM tracker.

## Process flow

Step 1: Collect the data

Capture via camera, scrap from the internet or use public datasets

Step 2: Train Object Detection Model

Train an object detector model (or use existing one if available in open-source domain)

Step 3: Annotate the data

Apply object detector on the images to create a training set for object tracking

Step 4: Data Preparation

Clean the data and make it ready for modeling

Step 5: Train the Tracker

Build and train an object tracking model (e.g. DeepSORT, FairMOT) to accurately track the target object in images/videos. Track the progress and experiments

Step 6: Model Validation

Validate the final set of models and select/assemble the final model

Step 7: UAT Testing

Wrap the model inference engine in API for client testing

Step 8: Deployment

Deploy the model on cloud or edge as per the requirement

Step 9: Documentation

Prepare the documentation and transfer all assets to the client

## Use Cases

### Pedestrian Tracking

Pedestrian Tracking with YOLOv3 and DeepSORT. Check out [this](https://www.notion.so/Pedestrian-Tracking-with-YOLOv3-and-DeepSORT-a38ea37a2abf4755aacc691bd6b859a1) notion.

### Object Tracking

Object tracking with FRCNN and SORT. Check out [this](https://www.notion.so/Object-tracking-with-FRCNN-and-SORT-e555d6174d2e4c1e993526c89555f96b) notion.

### Object Tracking

Tested out 5 algorithms on videos - OpticalFlow, DenseFlow, Camshift, MeanShift and Single Object Tracking with OpenCV. Check out [this](https://www.notion.so/Object-Tracking-with-OpenCV-and-Python-2bf91e9f6f49405ca40409c392a2d429) notion.

### Social Distancing Violation Detection

### People and Vehicle Counter Detection
