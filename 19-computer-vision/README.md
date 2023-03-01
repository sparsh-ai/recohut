# Computer Vision

## Categories

### Image Similarity

Image similarity is the measure of how similar two images are. In other words, it quantifies the degree of similarity between intensity patterns in two images.

![content-concepts-raw-computer-vision-image-similarity-slide19](https://user-images.githubusercontent.com/62965911/216822791-efe44b82-976d-46ca-81ee-eeb700ee641d.png)

- **Applications:** Duplicate product detection, image clustering, visual search, product recommendations.
- **Scope:** Fine-tuning on classes for greater accuracy
- **Tools:** TFHub

#### Models

- *[DeepRank: A New Deep Architecture for Relevance Ranking in Information Retrieval. arXiv, 2017.](https://arxiv.org/abs/1710.05649)*
- ConvNets: Pre-trained models like MobileNet, EfficientNet, BiT-L/BiT-M can be used to convert images into vectors. These models can be found on TFHub. For more accuracy, fine-tuning can be done.
- FAISS: *[Billion-scale similarity search with GPUs. arXiv, 2017.](https://arxiv.org/abs/1702.08734)* - Faiss is a library for efficient similarity search and clustering of dense vectors.
- Siamese Network: Siamese network is a neural network that contains two or more identical subnetwork. The purpose of this network is to find the similarity or comparing the relationship between two comparable things. Unlike the classification task that uses cross-entropy as the loss function, the siamese network usually uses contrastive loss or triplet loss.
- Similarity Measures: L1 (Manhattan distance), L2 (Euclidean distance), Hinge Loss for Triplets.

#### Process flow

- Step 1: Collect Images - Download the raw image dataset into a directory. Categorize these images into their respective category directories. Make sure that images are of the same type, JPEG recommended. We will also process the metadata and store it in a serialized file, CSV recommended.
- Step 2: Encoder Fine-tuning - Download the pre-trained image model and add two additional layers on top of that: the first layer is a feature vector layer and the second layer is the classification layer. We will only train these 2 layers on our data and after training, we will select the feature vector layer as the output of our fine-tuned encoder. After fine-tuning the model, we will save the feature extractor for later use.
- Step 3: Image Vectorization - Now, we will use the encoder (prepared in step 2) to encode the images (prepared in step 1). We will save the feature vector of each image as an array in a directory. After processing, we will save these embeddings for later use.
- Step 4: Metadata and Indexing - We will assign a unique id to each image and create dictionaries to locate information of this image: 1) Image id to Image name dictionary, 2) Image id to image feature vector dictionary, and 3) (optional) Image id to metadata product id dictionary. We will also create an image id to image feature vector indexing. Then we will save these dictionaries and index objects for later use.
- Step 5: UAT Testing - Wrap the model inference engine in API for client testing. We will receive an image from user, encode it with our image encoder, find Top-K similar vectors using Indexing object, and retrieve the image (and metadata) using dictionaries. We send these images (and metadata) back to the user.
- Step 6: Deployment - Deploy the model on cloud or edge as per the requirement.
- Step 7: Documentation - Prepare the documentation and transfer all assets to the client.

#### Use Cases

**Multi-endpoint API Similarity System**

The task was to build an API that will support multiple endpoints. Each endpoint supports a separate similarity system. We built 2 endpoints: endpoint 1 would find tok-K most similar fashion images and endpoint 2 would find top-K most similar food images. Checkout the notion [here](https://www.notion.so/Multi-endpoint-Image-Similarity-System-159b47b635ea42299a0214551630e740).

**Beanstalk Image Similarity System**

There are 2 endpoints in the API - one for training and the other for inference. During training, the system will receive a zipped file of images. At the time of inference, this trained system would receive an image over inference endpoint and send back top-K most similar images with a confidence score. The API was deployed on AWS beanstalk. Checkout the notion [here](https://www.notion.so/Image-Similarity-AWS-b8f33261750047a69744e91a554eabff).

**Image + Text Similarity**

Use the textual details and images of products, find the exact similar product among different groups. Around 35 GB of retail product images was scraped and used to build the system. Checkout the notion [here](https://www.notion.so/Image-Text-Similarity-fe5130324ae14ab48a30c93444348f4a).

**Siamese Network Image Similarity on MNIST**

Siamese networks are incredibly powerful networks, responsible for significant increases in face recognition, signature verification, and prescription pill identification applications. The objective was to build image pairs for the siamese network, train the siamese network with TF Keras, and then compare image similarity with this siamese network.

**Visual Recommendation**

Use image similarity to recommend users visually similar products based on what they searched. Checkout the notion [here](https://www.notion.so/Image-Similarity-Detection-in-Action-with-Tensorflow-2-0-c2b4421d75dd42a3a1becf9c98251ccb).


### Object Detection

Object detection is a computer vision technique that allows us to identify and locate objects in an image or video.

![content-concepts-raw-computer-vision-object-detection-slide29](https://user-images.githubusercontent.com/62965911/216822793-68a55d64-a10e-4ae2-aa2b-53c3c8100117.png)

#### Introduction

- **Applications:** Crowd counting, Self-driving cars, Video surveillance, Face detection, Anomaly detection
- **Scope:** Detect objects in images and videos, 2-dimensional bounding boxes, Real-time
- **Tools:** Detectron2, TF Object Detection API, OpenCV, TFHub, TorchVision

#### Models

- *[Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks. arXiv, 2016.](https://arxiv.org/abs/1506.01497)*
- *[SSD: Single Shot MultiBox Detector. CVPR, 2016.](https://arxiv.org/abs/1512.02325)*
- [*YOLOv3: An Incremental Improvement. arXiv, 2018.*](https://arxiv.org/abs/1804.02767)
- *[EfficientDet: Scalable and Efficient Object Detection. CVPR, 2020.](https://arxiv.org/abs/1911.09070)* - It achieved 55.1 AP on COCO test-dev with 77M parameters.

#### Process flow

- Step 1: Collect Images - Capture via camera, scrap from the internet or use public datasets
- Step 2: Create Labels - This step is required only if the object category is not available in any pre-trained model or labels are not freely available on the web. To create the labels (bounding boxes) using either open-source tools like Labelme or any other professional tool
- Step 3: Data Acquisition - Setup the database connection and fetch the data into python environment
- Step 4: Data Exploration - Explore the data, validate it and create preprocessing strategy
- Step 5: Data Preparation - Clean the data and make it ready for modeling
- Step 6: Model Building - Create the model architecture in python and perform a sanity check
- Step 7: Model Training - Start the training process and track the progress and experiments
- Step 8: Model Validation - Validate the final set of models and select/assemble the final model
- Step 9: UAT Testing - Wrap the model inference engine in API for client testing
- Step 10: Deployment - Deploy the model on cloud or edge as per the requirement
- Step 11: Documentation - Prepare the documentation and transfer all assets to the client

#### Use Cases

**Automatic License Plate Recognition**

Recognition of vehicle license plate number using various methods including YOLO4 object detector and Tesseract OCR. Checkout the notion [here](https://www.notion.so/Automatic-License-Plate-Recognition-10ec22181b454b1facc99abdeadbf78f).

**Object Detection App**

This is available as a streamlit app. It detects common objects. 3 models are available for this task - Caffe MobileNet-SSD, Darknet YOLO3-tiny, and Darknet YOLO3. Along with common objects, this app also detects human faces and fire. Checkout the notion [here](https://www.notion.so/Object-Detector-App-c60fddae2fcd426ab763261436fb15d8).

**Logo Detector**

Build a REST API to detect logos in images. API will receive 2 zip files - 1) a set of images in which we have to find the logo and 2) an image of the logo. Deployed the model in AWS Elastic Beanstalk. Checkout the notion [here](https://www.notion.so/Logo-Detection-91bfe4953dcf4558807b342efe05a9ff).

**TF Object Detection API Experiments**

The TensorFlow Object Detection API is an open-source framework built on top of TensorFlow that makes it easy to construct, train, and deploy object detection models. We did inference on pre-trained models, few-shot training on single class, few-shot training on multiple classes and conversion to TFLite model. Checkout the notion [here](https://www.notion.so/Tensorflow-Object-Detection-API-499b017e502d4950a9d448fb35a41d58).

**Pre-trained Inference Experiments**

Inference on 6 pre-trained models - Inception-ResNet (TFHub), SSD-MobileNet (TFHub), PyTorch YOLO3, PyTorch SSD, PyTorch Mask R-CNN, and EfficientDet. Checkout the notion [here](https://www.notion.so/Object-Detection-Inference-Experiments-568fa092b1d34471b676fd43a42974b2) and [here](https://www.notion.so/Object-Detection-Inference-with-Pre-trained-models-da9e2e5bfab944bc90f568f6bc4b3e1f).

**Object Detection App**

TorchVision Mask R-CNN model Gradio App. Checkout the notion [here](https://www.notion.so/MaskRCNN-TorchVision-Object-Detection-Gradio-App-c22f2a13ab63493b9b38720b20c50051).

**Real-time Object Detector in OpenCV**

Build a model to detect common objects like scissors, cups, bottles, etc. using the MobileNet SSD model in the OpenCV toolkit. It will task input from the camera and detect objects in real-time. Checkout the notion [here](https://www.notion.so/Object-Detection-with-OpenCV-MobileNet-SSD-38ff496d2f0d427185a9c51cebc1ddf2). Available as a Streamlit app also (this app is not real-time).

**EfficientDet Fine-tuning**

Fine-tune YOLO4 model on new classes. Checkout the notion [here](https://www.notion.so/EfficientDet-fine-tuning-01a6ffd1e11f4dc1941073aff4b9b486).

**YOLO4 Fine-tuning**

Fine-tune YOLO4 model on new classes. Checkout the notion [here](https://www.notion.so/YOLO-4-b32c2d2a4b8644b59f1c05e6887ffcca).

**Detectron2 Fine-tuning**

Fine-tune Detectron2 Mask R-CNN (with PointRend) model on new classes. Checkout the notion [here](https://www.notion.so/YOLO-4-b32c2d2a4b8644b59f1c05e6887ffcca).



### Image Segmentation

Image segmentation is the task of assigning labels to each pixel of an image.

![content-concepts-raw-computer-vision-image-segmentation-slide46](https://user-images.githubusercontent.com/62965911/216822790-17e672b8-9485-4189-be5c-38032dc37d11.png)

- **Applications:** Medical imaging, self-driving cars, satellite imaging
- **Scope:** Semantic and Instance masks, 2D pixel-mask, Real-time
- **Tools:** Detectron2, TFHub, TorchVision, DeepLab

#### Models

- *[U-Net: Convolutional Networks for Biomedical Image Segmentation. arXiv, 2015.](https://arxiv.org/abs/1505.04597)* - It was originally designed to perform medical image segmentation but it works well on a wide variety of tasks, from segmenting cells on microscope images to detecting ships or houses on photos taken from satellites.
- *[Mask R-CNN. arXiv, 2017.](https://arxiv.org/abs/1703.06870)* - The Mask R-CNN framework is built on top of Faster R-CNN. ****So, for a given image, Mask R-CNN, in addition to the class label and bounding box coordinates for each object, will also return the object mask.
- DeepLabV3+: *[Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation. arXiv, 2018.](https://arxiv.org/abs/1802.02611)* - It achieves a mean IOU score of 89% on the PASCAL VOC 2012 dataset.

#### Process flow

- Step 1: Collect Images - Capture via camera, scrap from the internet or use public datasets
- Step 2: Create Labels - This step is required only if the object category is not available in any pre-trained model or labels are not freely available on the web. To create the labels (pixel masks) using either open-source tools like Labelme or any other professional tool
- Step 3: Data Acquisition - Setup the database connection and fetch the data into python environment
- Step 4: Data Exploration - Explore the data, validate it and create preprocessing strategy
- Step 5: Data Preparation - Clean the data and make it ready for modeling
- Step 6: Model Building - Create the model architecture in python and perform a sanity check
- Step 7: Model Training - Start the training process and track the progress and experiments
- Step 8: Model Validation - Validate the final set of models and select/assemble the final model
- Step 9: UAT Testing - Wrap the model inference engine in API for client testing
- Step 10: Deployment - Deploy the model on cloud or edge as per the requirement
- Step 11: Documentation - Prepare the documentation and transfer all assets to the client

#### Use Cases

**Satellite Image Segmentation for Agricultural Fields**

An image with 1800 x 1135 resolution and 60 channels. Every Month 5 bands images were shot from agricultural land for 12 months. There is 8 type of croplands. Task is to classify all unknown label pixels into one of these 8 categories. U-Net model was trained from scratch on patches. Checkout [this](https://www.notion.so/F991454-Satellite-Image-Segmentation-for-Agricultural-Fields-9914b549617746578c509e0382deb211) notion.

**Detectron2 Fine-tuning**

Fine-tune Detectron2 Mask R-CNN (with PointRend) model on new classes. It supports semantic, instance, and panoptic segmentation. We fine-tuned on balloons, chipsets, and faces. Checkout [this](https://www.notion.so/Detectron-2-D281D-bb7f769860fa434d923feef3a99f9cbb) notion.

**Industrial Use Cases for Image Segmentation**

Experimented with 3 industrial use cases - Carvana Vehicle Image Masking, Airbus Ship Detection, and Severstal Steel Defect Detection. Checkout [this](https://www.notion.so/Kaggle-Image-Segmentation-Experiments-770728c2ef9a493da20863789b112d78) notion.

**Real-time segmentation on Videos**

Real-time tracking and segmentation with SiamMask, semantic segmentation with LightNet++ and instance segmentation with YOLACT. Checkout [this](https://www.notion.so/Image-Segmentation-Inference-Experiments-26fac32c220f419a902121129b2924db) notion.

**Image Segmentation Exercises**

Thresholding with Otsu and Riddler–Calvard, Image segmentation with self-organizing maps, Random Walk segmentation with scikit-image, Skin color segmentation with the GMM–EM algorithm, Medical image segmentation, Deep semantic segmentation, Deep instance segmentation. Checkout [this](https://www.notion.so/Image-Segmentation-Exercises-cc3262c55d374fb684362f5d333fb91a) notion.

**TorchVision Inference Experiments**

FCN-ResNet and DeepLabV3 (both are available in TorchVision library) inference. Available as a streamlit app. Checkout [this](https://www.notion.so/FCN-ResNet-vs-DeepLab-App-FF841-5168fac2ed0b42b1ad95a0b9e8b26d53) notion.


### Face Detection and Recognition

Analyze the facial features like age, gender, emotion, and identity.

![content-concepts-raw-computer-vision-facial-analytics-img](https://user-images.githubusercontent.com/62965911/216822789-86a34319-c100-48be-9581-ea5671cca059.png)

**Applications:** Identity verification, emotion detection

**Scope:** Human faces only, Real-time

**Tools:** OpenCV, dlib

#### Models

* *[FaceNet: A Unified Embedding for Face Recognition and Clustering. CVPR, 2015.](https://openaccess.thecvf.com/content_cvpr_2015/papers/Schroff_FaceNet_A_Unified_2015_CVPR_paper.pdf)*
* [RetinaFace: Single-stage Dense Face Localisation in the Wild. arXiv, 2019.](https://arxiv.org/abs/1905.00641v2)
* *[FER+: Training Deep Networks for Facial Expression Recognition with Crowd-Sourced Label Distribution. arXiv, 2016.](https://arxiv.org/abs/1608.01041v2)*

#### Process flow

- Step 1: Collect Images - Capture via camera, scrap from the internet or use public datasets
- Step 2: Create Labels - Compile a metadata table containing a unique id (preferably the same as the image name) for each face id.
- Step 3: Data Preparation - Setup the database connection and fetch the data into the environment. Explore the data, validate it, and create a preprocessing strategy. Clean the data and make it ready for modeling
- Step 4: Model Building - Create the model architecture in python and perform a sanity check. Start the training process and track the progress and experiments. Validate the final set of models and select/assemble the final model
- Step 5: UAT Testing - Wrap the model inference engine in API for client testing
- Step 6: Deployment - Deploy the model on cloud or edge as per the requirement
- Step 7: Documentation - Prepare the documentation and transfer all assets to the client

#### Use Cases

**Automatic Attendance System via Webcam**

We use Face Recognition library and OpenCV to create a real-time webcam-based attendance system that will automatically recognizes the face and log an attendance into the excel sheet. Check out [this](https://www.notion.so/Face-Recognition-based-Automated-Attendance-System-dfb6f70527994ea4be11caf69b054350) notion.

**Detectron2 Fine-tuning for face detection**

Fine-tuned detectron2 on human face dataset to detect the faces in images and videos. Check out [this](https://www.notion.so/Detectron-2-D281D-bb7f769860fa434d923feef3a99f9cbb) notion.


### Object Tracking

Object tracking is the process of 1)** Taking an initial set of object detections (such as an input set of bounding box coordinates, 2) Creating a unique ID for each of the initial detections, and then 3) tracking each of the objects as they move around frames in a video, maintaining the assignment of unique IDs.

![content-concepts-raw-computer-vision-object-tracking-img](https://user-images.githubusercontent.com/62965911/216822794-bbebf98d-269b-46f7-bd51-aa9f417105c8.png)

- **Applications:** In-store consumer behavior tracking, Apply security policies like crowd management, traffic management, vision-based control, human-computer interface, medical imaging, augmented reality, robotics.
- **Scope:** Track objects in images and videos, 2-dimensional tracking, Bounding boxes and pixel masks, Single and Multiple Object Tracking
- **Tools:** Detectron2, OpenCV

#### Models

- **FairMOT**: *[On the Fairness of Detection and Re-Identification in Multiple Object Tracking. arXiv, 2020.](https://arxiv.org/abs/2004.01888)*
- **DeepSORT**: *[Simple Online and Realtime Tracking with a Deep Association Metric. arXiv, 2017.](https://arxiv.org/abs/1703.07402)* - Detect object with models like YOLO or Mask R-CNN and then track using DeepSORT.
- **GOTURN**: *[Learning to Track at 100 FPS with Deep Regression Networks. arXiv, 2016.](https://arxiv.org/abs/1604.01802)* - CNN offline learning tracker.
- **MDNet**: *[Real-Time MDNet. arXiv, 2018.](https://arxiv.org/abs/1808.08834)* - CNN online learning tracker.
- **ROLO**: *[Spatially Supervised Recurrent Convolutional Neural Networks for Visual Object Tracking. arXiv, 2016.](https://arxiv.org/abs/1607.05781)* - CNN + LSTM tracker.

#### Process flow

- Step 1: Collect the data - Capture via camera, scrap from the internet or use public datasets
- Step 2: Train Object Detection Model - Train an object detector model (or use existing one if available in open-source domain)
- Step 3: Annotate the data - Apply object detector on the images to create a training set for object tracking
- Step 4: Data Preparation - Clean the data and make it ready for modeling
- Step 5: Train the Tracker - Build and train an object tracking model (e.g. DeepSORT, FairMOT) to accurately track the target object in images/videos. Track the progress and experiments
- Step 6: Model Validation - Validate the final set of models and select/assemble the final model
- Step 7: UAT Testing - Wrap the model inference engine in API for client testing
- Step 8: Deployment - Deploy the model on cloud or edge as per the requirement
- Step 9: Documentation - Prepare the documentation and transfer all assets to the client

#### Use Cases

**Pedestrian Tracking**

Pedestrian Tracking with YOLOv3 and DeepSORT. Check out [this](https://www.notion.so/Pedestrian-Tracking-with-YOLOv3-and-DeepSORT-a38ea37a2abf4755aacc691bd6b859a1) notion.

**Object Tracking**

Object tracking with FRCNN and SORT. Check out [this](https://www.notion.so/Object-tracking-with-FRCNN-and-SORT-e555d6174d2e4c1e993526c89555f96b) notion.

**Object Tracking**

Tested out 5 algorithms on videos - OpticalFlow, DenseFlow, Camshift, MeanShift and Single Object Tracking with OpenCV. Check out [this](https://www.notion.so/Object-Tracking-with-OpenCV-and-Python-2bf91e9f6f49405ca40409c392a2d429) notion.

**Social Distancing Violation Detection**

**People and Vehicle Counter Detection**


### Pose Estimation

Pose estimation is a computer vision task that infers the pose of a person or object in an image or video. This is typically done by identifying, locating, and tracking the number of key points on a given object or person. For objects, this could be corners or other significant features. And for humans, these key points represent major joints like an elbow or knee.

![content-concepts-raw-computer-vision-pose-estimation-img](https://user-images.githubusercontent.com/62965911/216822795-bdcc650d-08c1-4e8a-9b67-f3a8a0aba2a5.png)

- **Applications:** Activity recognition, motion capture, fall detection, plank pose corrector, yoga pose identifier, body ration estimation
- **Scope:** 2D skeleton map, Human Poses, Single and Multi-pose, Real-time
- **Tools:** Tensorflow PoseNet API

#### Models

- *[OpenPose: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields. arXiv, 2016.](https://arxiv.org/abs/1812.08008)* - A standard bottom-up model that supports real-time multi-person 2D pose estimation. The authors of the paper have shared two models – one is trained on the Multi-Person Dataset ( MPII ) and the other is trained on the COCO dataset. The COCO model produces 18 points, while the MPII model outputs 15 points.
- PoseNet is a machine learning model that allows for Real-time Human Pose Estimation. PoseNet can be used to estimate either a single pose or multiple poses PoseNet v1 is trained on MobileNet backbone and v2 on ResNet backbone.

![content-concepts-raw-computer-vision-pose-estimation-slide52](https://user-images.githubusercontent.com/62965911/216822796-8d922553-a504-43cf-9718-2ef84a23bc0b.png)

#### Process flow

- Step 1: Collect Images - Capture via camera, scrap from the internet or use public datasets
- Step 2: Create Labels - Use a pre-trained model like PoseNet, OpenPose to identify the key points. These key points are our labels for pose estimation based classification task. If the model is not compatible/available for the required key points (e.g. identify the cap and bottom of a bottle product to measure if manufacturing is correct), we have to first train a pose estimation model using transfer learning in that case (this is out of scope though, as we are only focusing on human poses and pre-trained models are already available for this use case)
- Step 3: Data Preparation - Setup the database connection and fetch the data into the environment. Explore the data, validate it, and create a preprocessing strategy. Clean the data and make it ready for modeling
- Step 4: Model Building - Create the model architecture in python and perform a sanity check. Start the training process and track the progress and experiments. Validate the final set of models and select/assemble the final model
- Step 5: UAT Testing - Wrap the model inference engine in API for client testing
- Step 6: Deployment - Deploy the model on cloud or edge as per the requirement
- Step 7: Documentation - Prepare the documentation and transfer all assets to the client

#### Use Cases

**OpenPose Experiments**

Four types of experiments with pre-trained OpenPose model - Single and Multi-Person Pose Estimation with OpenCV, Multi-Person Pose Estimation with PyTorch and Pose Estimation on Videos. Check out [this](https://www.notion.so/Pose-Estimation-with-OpenPose-2D8F5-7f01bee1534243f3836728d03a419969) notion.

**Pose Estimation Inference Experiments**

Experimented with pre-trained pose estimation models. Check out [this](https://www.notion.so/Pose-Estimation-with-OpenPifPaf-7517E-8cb982455e01478e876c52e9324d8e6b) notion for experiments with the OpenPifPaf model, [this](https://www.notion.so/Pose-Estimation-with-Keypoint-RCNN-in-TorchVision-96e6aad0f36f44d3bff28e60525c6d31) one for the TorchVision Keypoint R-CNN model, and [this](https://www.notion.so/Detectron-2-D281D-bb7f769860fa434d923feef3a99f9cbb) notion for the Detectron2 model.

**Pose Detection on the Edge**

Train the pose detector using Teachable machine, employing the PoseNet model (multi-person real-time pose estimation) as the backbone and serve it to the web browser using ml5.js. This system will infer the end-users pose in real-time via a web browser. Check out [this](https://teachablemachine.withgoogle.com/train/pose) link and [this](https://www.notion.so/ml5-js-Pose-Estimation-with-PoseNet-5661cefe46b449998cc31838441dc26a) notion.

**Pose Detection on the Edge using OpenVINO**

Optimize the pre-trained pose estimation model using the OpenVINO toolkit to make it ready to serve at the edge (e.g. small embedded devices) and create an OpenVINO inference engine for real-time inference. Check out [this](https://www.notion.so/OpenVINO-4c4fc4f167cc4601ade5795a241a60da) notion.


### Scene Text Recognition

Text—as a fundamental tool of communicating information—scatters throughout natural scenes, e.g., street signs, product labels, license plates, etc. Automatically reading text in natural scene images is an important task in machine learning and gains increasing attention due to a variety of applications. For example, accessing text in images can help the visually impaired understand the surrounding environment. To enable autonomous driving, one must accurately detect and recognize every road sign. Indexing text in images would enable image search and retrieval from billions of consumer photos on the internet.

![content-concepts-raw-computer-vision-scene-text-recognition-img](https://user-images.githubusercontent.com/62965911/216822802-f8a98007-4d46-42bf-9198-0132a6a8a270.png)

- **Applications:** Indexing of multimedia archives, recognizing signs in driver assisted systems, providing scene information to visually impaired people, identifying vehicles by reading their license plates.
- **Scope:** No scope decided yet.
- **Tools:** OpenCV, Tesseract, PaddleOCR

#### Models

- **Semantic Reasoning Networks**: *[Towards Accurate Scene Text Recognition with Semantic Reasoning Networks. arXiv, 2020.](https://arxiv.org/abs/2003.12294v1)*
- **Differentiable Binarization**: *[Real-time Scene Text Detection with Differentiable Binarization. arXiv, 2019.](https://arxiv.org/abs/1911.08947v2)*
- **CRAFT**: *[Character Region Awareness for Text Detection. arXiv, 2019.](https://arxiv.org/abs/1904.01941v1)*
- *[EAST: An Efficient and Accurate Scene Text Detector. arXiv, 2017.](https://arxiv.org/abs/1704.03155v2)*

#### Process flow

- Step 1: Collect Images - Fetch from database, scrap from the internet or use public datasets. Setup the database connection and fetch the data into python environment.
- Step 2: Data Preparation - Explore the data, validate it and create preprocessing strategy. Clean the data and make it ready for processing.
- Step 3: Model Building - Apply different kinds of detection, recognition and single-shot models on the images. Track the progress and experiments. Validate the final set of models and select/assemble the final model.
- Step 4: UAT Testing - Wrap the model inference engine in API for client testing
- Step 5: Deployment - Deploy the model on cloud or edge as per the requirement
- Step 6: Documentation - Prepare the documentation and transfer all assets to the client

#### Use Cases

**Scene Text Detection with EAST Tesseract**

Detect the text in images and videos using EAST model. Read the characters using Tesseract. Check out [this](https://www.notion.so/Scene-Text-Detection-with-EAST-Tesseract-583f882db70b43b5b3005d89ced8d8fd) notion.

**Scene Text Recognition with DeepText**

Detect and Recognize text in images with an end-to-end model named DeepText. Check out [this](https://www.notion.so/Scene-Text-Recognition-with-DeepText-3dbc00e6bdf548a3b8539be1adb8f2d5) notion.

**Automatic License Plate Recognition**

Read the characters on the license plate image using Tesseract OCR. Check out [this](https://www.notion.so/Automatic-License-Plate-Recognition-10ec22181b454b1facc99abdeadbf78f) notion.

**Keras OCR Toolkit Experiment**

Keras OCR is a deep learning based toolkit for text recognition in images. Check out [this](https://www.notion.so/Keras-OCR-d15bff7629fa4fbf8d8a7fb21d2a69c5) notion.

**OCR Experiments**

Experiments with three OCR tools - Tesseract OCR, Easy OCR, and Arabic OCR. Check out [this](https://www.notion.so/OCR-Simple-Experiments-a606ff9003b14de589073864c150aa81) and [this](https://www.notion.so/Optical-Character-Recognition-6eec9092cc70455a91dd92278e4677a8) notion.

**PaddleOCR Experiments**

Experiments with state of the art lightweight and multi-lingual OCR. Check out [this](https://www.notion.so/Paddle-OCR-5ab56a38a594478da92314f246159193) notion.


### Video Action Recognition

This is the task of identifying human activities/actions (e.g. eating, playing) in videos. In other words, this task classifies segments of videos into a set of pre-defined categories.

![content-concepts-raw-computer-vision-video-action-recognition-img](https://user-images.githubusercontent.com/62965911/216822803-052c478d-b961-487b-a68f-702948660afc.png)

- **Applications:** Automated surveillance, elderly behavior monitoring, human-computer interaction, content-based video retrieval, and video summarization.
- **Scope:** Human Action only
- **Tools:** OpenCV

#### **Models**

- **3D-ResNet**: **[Can Spatiotemporal 3D CNNs Retrace the History of 2D CNNs and ImageNet?](https://arxiv.org/abs/1711.09577)** - the authors explore how existing state-of-the-art 2D architectures (such as ResNet, ResNeXt, DenseNet, etc.) can be extended to video classification via 3D kernels.
- **R(2+1)D**: This model was pre-trained on 65 million social media videos and fine-tuned on Kinetics400.

#### Process flow

- Step 1: Collect videos - Capture via camera, scrap from the internet or use public datasets
- Step 2: Create Labels - Use open-source tools like VGA Video Annotator for video annotation
- Step 3: Data Acquisition - Setup the database connection and fetch the data into python environment
- Step 4: Data Exploration - Explore the data, validate it and create preprocessing strategy
- Step 5: Data Preparation - Clean the data and make it ready for modeling
- Step 6: Model Building - Create the model architecture in python and perform a sanity check
- Step 7: Model Training - Start the training process and track the progress and experiments
- Step 8: Model Validation - Validate the final set of models and select/assemble the final model
- Step 9: UAT Testing - Wrap the model inference engine in API for client testing
- Step 10: Deployment - Deploy the model on cloud or edge as per the requirement
- Step 11: Documentation - Prepare the documentation and transfer all assets to the client

#### Use Cases

**Kinetics 3D CNN Human Activity Recognition**

This dataset consists of 400 human activity recognition classes, at least 400 video clips per class (downloaded via YouTube) and a total of 300,000 videos. Check out [this](https://www.notion.so/Kinetics-3D-CNN-Human-Activity-Recognition-fd10fd7b5858459cba65dc4a6cb73630) notion.

**Action Recognition using R(2+1)D Model**

VGA Annotator was used for creating the video annotation for training. Check out [this](https://www.notion.so/Action-Recognition-using-R-2-1-D-Model-4c796f308aed40f29fc230a757af98e8) notion.
