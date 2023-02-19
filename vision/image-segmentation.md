# Image Segmentation

![content-concepts-raw-computer-vision-image-segmentation-slide46](https://user-images.githubusercontent.com/62965911/216822790-17e672b8-9485-4189-be5c-38032dc37d11.png)

## Introduction

- **Definition:** Image segmentation is the task of assigning labels to each pixel of an image.
- **Applications:** Medical imaging, self-driving cars, satellite imaging
- **Scope:** Semantic and Instance masks, 2D pixel-mask, Real-time
- **Tools:** Detectron2, TFHub, TorchVision, DeepLab

## Models

### U-Net

*[U-Net: Convolutional Networks for Biomedical Image Segmentation. arXiv, 2015.](https://arxiv.org/abs/1505.04597)*

It was originally designed to perform medical image segmentation but it works well on a wide variety of tasks, from segmenting cells on microscope images to detecting ships or houses on photos taken from satellites.

### Mask R-CNN

*[Mask R-CNN. arXiv, 2017.](https://arxiv.org/abs/1703.06870)*

The Mask R-CNN framework is built on top of Faster R-CNN. ****So, for a given image, Mask R-CNN, in addition to the class label and bounding box coordinates for each object, will also return the object mask.

### DeepLabV3+

*[Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation. arXiv, 2018.](https://arxiv.org/abs/1802.02611)*

It achieves a mean IOU score of 89% on the PASCAL VOC 2012 dataset.

## Process flow

Step 1: Collect Images

Capture via camera, scrap from the internet or use public datasets

Step 2: Create Labels

This step is required only if the object category is not available in any pre-trained model or labels are not freely available on the web. To create the labels (pixel masks) using either open-source tools like Labelme or any other professional tool

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

### Satellite Image Segmentation for Agricultural Fields

An image with 1800 x 1135 resolution and 60 channels. Every Month 5 bands images were shot from agricultural land for 12 months. There is 8 type of croplands. Task is to classify all unknown label pixels into one of these 8 categories. U-Net model was trained from scratch on patches. Checkout [this](https://www.notion.so/F991454-Satellite-Image-Segmentation-for-Agricultural-Fields-9914b549617746578c509e0382deb211) notion.

### Detectron2 Fine-tuning

Fine-tune Detectron2 Mask R-CNN (with PointRend) model on new classes. It supports semantic, instance, and panoptic segmentation. We fine-tuned on balloons, chipsets, and faces. Checkout [this](https://www.notion.so/Detectron-2-D281D-bb7f769860fa434d923feef3a99f9cbb) notion.

### Industrial Use Cases for Image Segmentation

Experimented with 3 industrial use cases - Carvana Vehicle Image Masking, Airbus Ship Detection, and Severstal Steel Defect Detection. Checkout [this](https://www.notion.so/Kaggle-Image-Segmentation-Experiments-770728c2ef9a493da20863789b112d78) notion.

### Real-time segmentation on Videos

Real-time tracking and segmentation with SiamMask, semantic segmentation with LightNet++ and instance segmentation with YOLACT. Checkout [this](https://www.notion.so/Image-Segmentation-Inference-Experiments-26fac32c220f419a902121129b2924db) notion.

### Image Segmentation Exercises

Thresholding with Otsu and Riddler–Calvard, Image segmentation with self-organizing maps, Random Walk segmentation with scikit-image, Skin color segmentation with the GMM–EM algorithm, Medical image segmentation, Deep semantic segmentation, Deep instance segmentation. Checkout [this](https://www.notion.so/Image-Segmentation-Exercises-cc3262c55d374fb684362f5d333fb91a) notion.

### TorchVision Inference Experiments

FCN-ResNet and DeepLabV3 (both are available in TorchVision library) inference. Available as a streamlit app. Checkout [this](https://www.notion.so/FCN-ResNet-vs-DeepLab-App-FF841-5168fac2ed0b42b1ad95a0b9e8b26d53) notion.
