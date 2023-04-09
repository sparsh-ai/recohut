# Snippets related to Lambda function

## Create a CloudFormation template for creating a Lambda function that writes to an S3 bucket

The code creates a text file that reads ‘Hello world!’ and stores it into the s3 bucket. 

```py
import os
import boto3
import io

def lambda_handler(event, context):
    bucket_name = event['bucket_name']
    file_name = event['file_name']
    
    file = io.BytesIO(bytes('Hello world!', encoding='utf-8'))
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket_object = bucket.Object(file_name)
    bucket_object.upload_fileobj(file)
```

The template consists of the following resources:

1. Lambda Function: HelloWorld
1. S3 Bucket: LambdaZipsBucket
1. IAM Role: HelloWorldRole

```yml
AWSTemplateFormatVersion: 2010-09-09
Resources:
  HelloWorld:
    Type: 'AWS::Lambda::Function'
    Properties:
        FunctionName: helloWorld
        Handler: lambda_function.lambda_handler
        Role: !GetAtt HelloWorldRole.Arn
        Runtime: python3.9
        Code:
            S3Bucket: 'mybucket'
            S3Key: 'lambda_function.py.zip'
  LambdaZipsBucket:
    Type: 'AWS::S3::Bucket'
    Properties:
        BucketName: 'lambdazips2'
  HelloWorldRole:
    Type: 'AWS::IAM::Role'
    Properties:
      RoleName: HelloWorldRole
      ManagedPolicyArns: 
        - "arn:aws:iam::aws:policy/CloudWatchFullAccess"
        - "arn:aws:iam::aws:policy/AmazonS3FullAccess"
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - lambda.amazonaws.com
            Action:
              - 'sts:AssumeRole'
      Path: /
      Policies:
        - PolicyName: AWSLambdaBasicExecutionRole
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - 'logs:CreateLogGroup'
                  - 'logs:CreateLogStream'
                  - 'logs:PutLogEvents'
                Resource: '*'
```
