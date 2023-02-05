# Scene Text Recognition

![content-concepts-raw-computer-vision-scene-text-recognition-img](https://user-images.githubusercontent.com/62965911/216822802-f8a98007-4d46-42bf-9198-0132a6a8a270.png)

## Introduction

- **Definition:** Text—as a fundamental tool of communicating information—scatters throughout natural scenes, e.g., street signs, product labels, license plates, etc. Automatically reading text in natural scene images is an important task in machine learning and gains increasing attention due to a variety of applications. For example, accessing text in images can help the visually impaired understand the surrounding environment. To enable autonomous driving, one must accurately detect and recognize every road sign. Indexing text in images would enable image search and retrieval from billions of consumer photos on the internet.
- **Applications:** Indexing of multimedia archives, recognizing signs in driver assisted systems, providing scene information to visually impaired people, identifying vehicles by reading their license plates.
- **Scope:** No scope decided yet.
- **Tools:** OpenCV, Tesseract, PaddleOCR

## Models

### Semantic Reasoning Networks

*[Towards Accurate Scene Text Recognition with Semantic Reasoning Networks. arXiv, 2020.](https://arxiv.org/abs/2003.12294v1)*

### Differentiable Binarization

*[Real-time Scene Text Detection with Differentiable Binarization. arXiv, 2019.](https://arxiv.org/abs/1911.08947v2)*

### CRAFT

*[Character Region Awareness for Text Detection. arXiv, 2019.](https://arxiv.org/abs/1904.01941v1)*

### EAST

*[EAST: An Efficient and Accurate Scene Text Detector. arXiv, 2017.](https://arxiv.org/abs/1704.03155v2)*

## Process flow

Step 1: Collect Images

Fetch from database, scrap from the internet or use public datasets. Setup the database connection and fetch the data into python environment.

Step 2: Data Preparation

Explore the data, validate it and create preprocessing strategy. Clean the data and make it ready for processing.

Step 3: Model Building

Apply different kinds of detection, recognition and single-shot models on the images. Track the progress and experiments. Validate the final set of models and select/assemble the final model.

Step 4: UAT Testing

Wrap the model inference engine in API for client testing

Step 5: Deployment

Deploy the model on cloud or edge as per the requirement

Step 6: Documentation

Prepare the documentation and transfer all assets to the client

## Use Cases

### Scene Text Detection with EAST Tesseract

Detect the text in images and videos using EAST model. Read the characters using Tesseract. Check out [this](https://www.notion.so/Scene-Text-Detection-with-EAST-Tesseract-583f882db70b43b5b3005d89ced8d8fd) notion.

### Scene Text Recognition with DeepText

Detect and Recognize text in images with an end-to-end model named DeepText. Check out [this](https://www.notion.so/Scene-Text-Recognition-with-DeepText-3dbc00e6bdf548a3b8539be1adb8f2d5) notion.

### Automatic License Plate Recognition

Read the characters on the license plate image using Tesseract OCR. Check out [this](https://www.notion.so/Automatic-License-Plate-Recognition-10ec22181b454b1facc99abdeadbf78f) notion.

### Keras OCR Toolkit Experiment

Keras OCR is a deep learning based toolkit for text recognition in images. Check out [this](https://www.notion.so/Keras-OCR-d15bff7629fa4fbf8d8a7fb21d2a69c5) notion.

### OCR Experiments

Experiments with three OCR tools - Tesseract OCR, Easy OCR, and Arabic OCR. Check out [this](https://www.notion.so/OCR-Simple-Experiments-a606ff9003b14de589073864c150aa81) and [this](https://www.notion.so/Optical-Character-Recognition-6eec9092cc70455a91dd92278e4677a8) notion.

### PaddleOCR Experiments

Experiments with state of the art lightweight and multi-lingual OCR. Check out [this](https://www.notion.so/Paddle-OCR-5ab56a38a594478da92314f246159193) notion.
