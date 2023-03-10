# Amazon Sagemaker

Amazon SageMaker helps data scientists and developers to prepare, build, train, and deploy machine learning models quickly by bringing together a broad set of purpose-built capabilities. In this demo, learn about how SageMaker can accelerate machine learning development by way of an example where we build the perfect musical playlist tailored to a user's tastes.

<iframe width="100%" height="480" src="https://www.youtube.com/embed/Qv_Tr_BCFCQ" title="Introduction to Amazon SageMaker" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Lab: AWS Sagemaker In-depth

1. Import Data into the S3 Data Lake
2. Query the Amazon S3 Data Lake with Amazon Athena
3. Query Data with AWS Data Wrangler
4. Dive Deep into the Dataset with Athena and SageMaker
5. Convert Raw Text to BERT Features using Hugging Face and TensorFlow
6. Add Features to SageMaker Feature Store
7. Create Experiment and Process Data
8. Query The Feature Store
9. Show the Experiment Tracking Lineage
10. Show Lineage Artifacts For Our Processing Job
11. Fine-Tuning a BERT Model and Create a Text Classifier
12. Specify Manual Hyper-Parameters
13. Load Pretrained BERT Model
14. Setup Hyper-Parameters for Classification Layer
15. Evaluate Model with Amazon SageMaker Processing Jobs and Scikit-Learn
16. Detect Model Bias using smclarify
17. Perform A/B Test using REST Endpoints

## Lab: Managing Machine Learning Workflows and Deployments

![workflow-arch](https://user-images.githubusercontent.com/62965911/224300324-ca77de3c-0adf-4ed0-ac7e-26e15d8e901d.png)

We will cover the following recipes in this lab:

1. Working with Hugging Face models
1. Preparing the prerequisites of a multi-model endpoint deployment
1. Hosting multiple models with multi-model endpoints
1. Setting up A/B testing on multiple models with production variants
1. Preparing the Step Functions execution role
1. Managing ML workflows with AWS Step Functions and the Data Science SDK
1. Managing ML workflows with SageMaker Pipelines

## Lab: Music Recommendation using Amazon SageMaker

Creating the perfect personalized musical playlist with Amazon SageMaker.

![musicrec-arch](https://user-images.githubusercontent.com/62965911/224300316-8e1b0bd0-a78d-4efd-9389-e86e43713dad.png)

## Lab: Automate medical diagnosis using Amazon SageMaker

Detecting cancer cells by analyzing medical images using computer vision with Amazon SageMaker.

![medical-diagnosis-output](https://user-images.githubusercontent.com/62965911/224300300-b99fcfb5-d527-4811-aeaf-4d44d3ad3979.png)

## Lab: End-to-end workflow for auto claims fraud detection using Amazon SageMaker

The purpose of this end-to-end example is to demonstrate how to prepare, train, and deploy a model that detects auto insurance claims.

"Auto insurance fraud ranges from misrepresenting facts on insurance applications and inflating insurance claims to staging accidents and submitting claim forms for injuries or damage that never occurred, to false reports of stolen vehicles. Fraud accounted for between 15 percent and 17 percent of total claims payments for auto insurance bodily injury in 2012, according to an Insurance Research Council (IRC) study. The study estimated that between $5.6 billion and $7.7 billion was fraudulently added to paid claims for auto insurance bodily injury payments in 2012, compared with a range of $4.3 billion to $5.8 billion in 2002. " source: Insurance Information Institute

In this example, we will use an auto insurance domain to detect claims that are possibly fraudulent. more precisely we address the use-case: "what is the likelihood that a given auto claim is fraudulent?" , and explore the technical solution.

![frauddetect-arch](https://user-images.githubusercontent.com/62965911/224300286-6e98a323-e4b7-46fc-9c6f-9bda8bd1abef.png)

## Lab: Customer Churn Prediction with XGBoost

Using Gradient Boosted Trees to Predict Mobile Customer Departure

Losing customers is costly for any business. Identifying unhappy customers early on gives you a chance to offer them incentives to stay. This notebook describes using machine learning (ML) for the automated identification of unhappy customers, also known as customer churn prediction. ML models rarely give perfect predictions though, so this notebook is also about how to incorporate the relative costs of prediction mistakes when determining the financial outcome of using ML.

We use a familiar example of churn: leaving a mobile phone operator. Seems like one can always find fault with their provider du jour! And if the provider knows that a customer is thinking of leaving, it can offer timely incentives - such as a phone upgrade or perhaps having a new feature activated – and the customer may stick around. Incentives are often much more cost-effective than losing and reacquiring a customer.

## Lab: Recommendation Engine for E-Commerce Sales

This lab gives an overview of techniques and services offer by SageMaker to build and deploy a personalized recommendation engine.

## Solution

1. [Managing Machine Learning Workflows and Deployments](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/Managing_Machine_Learning_Workflows_and_Deployments.ipynb)
2. [Music Recommendation using Amazon SageMaker](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/Music_Recommendation_using_Amazon_SageMaker.ipynb)
3. [How to automate medical diagnosis using Amazon SageMaker](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/How_to_automate_medical_diagnosis_using_Amazon_SageMaker.ipynb)
4. [End-to-end workflow for auto claims fraud detection using Amazon SageMaker](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/End_to_end_workflow_for_auto_claims_fraud_detection_using_Amazon_SageMaker.ipynb)
5. [Customer Churn Prediction with XGBoost](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/SageMaker_3cases.ipynb)
6. [Recommendation Engine for E-Commerce Sales](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/Recommendation_Engine_for_E_Commerce_Sales.ipynb)
7. [AWS Sagemaker In-depth](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/aws-sagemaker-indepth.ipynb)
1. AWS Innovate, AI/ML Edition, EMEA (February 2021)
1. Various demos on SageMaker Studio [ https://www.youtube.com/playlist?list=PLJgojBtbsuc0MjdtpJPo4g4PL8mMsd2nK ]
1. [Managing Machine Learning Workflows and Deployments](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/Managing_Machine_Learning_Workflows_and_Deployments.ipynb)
2. [Music Recommendation using Amazon SageMaker](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/Music_Recommendation_using_Amazon_SageMaker.ipynb)
3. [How to automate medical diagnosis using Amazon SageMaker](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/How_to_automate_medical_diagnosis_using_Amazon_SageMaker.ipynb)
4. [End-to-end workflow for auto claims fraud detection using Amazon SageMaker](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/End_to_end_workflow_for_auto_claims_fraud_detection_using_Amazon_SageMaker.ipynb)
5. [Customer Churn Prediction with XGBoost](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/SageMaker_3cases.ipynb)
6. [Recommendation Engine for E-Commerce Sales](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/Recommendation_Engine_for_E_Commerce_Sales.ipynb)
7. [AWS Sagemaker In-depth](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/aws-sagemaker-indepth.ipynb)

```
# install tree command (helpful in printing folder structures)
apt-get install tree

# setup AWS cli
mkdir -p ~/.aws && cp /content/drive/MyDrive/AWS/d01_admin/* ~/.aws
chmod 600 ~/.aws/credentials
pip install awscli

# install boto3 and sagemaker
pip install boto3
pip install sagemaker

# install dependencies
pip install pyathena
pip install awswrangler
pip install smclarify
pip install sagemaker-experiments
pip install sagemaker-tensorflow
pip install smclarify

# install nlp libs
pip install transformers
```

```py
import boto3
import sagemaker
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import os
import sys
import time
import json
from sagemaker.estimator import Estimator

### global variables
role = "sagemakerRole"
base_job_prefix = "sklearn-housing"
training_instance_type = "ml.m5.xlarge"

### setup sagemaker session
sess = sagemaker.Session()
bucket = sess.default_bucket()
region = boto3.Session().region_name
account_id = boto3.client("sts").get_caller_identity().get("Account")
role_arn = "arn:aws:iam::{}:role/{}".format(account_id, role)
sm = boto3.Session().client(service_name="sagemaker", region_name=region)
s3 = boto3.Session().client(service_name="s3", region_name=region)
```