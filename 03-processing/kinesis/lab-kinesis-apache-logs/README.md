# Real Time Apache Log Analytics with Kinesis

## Objective

Build ETL pipelines with Kinesis processing Apache Logs data

![](https://user-images.githubusercontent.com/62965911/214810555-c3637a3c-7391-4076-892e-437e3219810c.png)

## Direct PUT Pipeline

Direct PUT is a method to send data directly from the clients to Kinesis Data Firehose. In this part, you'll create a Firehose Delivery Stream and will use a script to send data to Firehose with Direct PUT using AWS SDK for Python (boto3). Firehose receives the records and delivers them to S3 into a configured bucket/folder and partitions the incoming records based on the their arrival date and time.

1. Create the Kinesis Firehose Delivery Stream
1. Send the data using Boto3 `firehose` client
1. Check the ingested data in S3

## Send via Kinesis Data Streams

1. Create Kinesis Data Stream
1. Create Firehose Delivery Stream
1. Set up Amazon Kinesis Data Generator
1. Check the ingested data in S3

## Anomaly Detection with Kinesis and Glue Jobs

In this module, you will learn how to ingest, process, and consume streaming data using AWS serverless services such as Kinesis Data Streams, Glue, S3, and Athena. To simulate the data streaming input, we will use Kinesis Data Generator (KDG).

![](https://user-images.githubusercontent.com/62965911/214810281-014f57ff-ed16-4bf5-89b7-2c473e583aaf.png)

1. Create the Infra by using `./KinesisGlueETL/template.yml` template
1. Set up the Kinesis Stream
1. Create table for Kinesis stream source in the glue data catalog
1. Create and trigger the glue streaming job
1. Trigger the streaming data from KDG
1. Verify the glue stream Job
1. Create Glue crawler for the transformed data
1. Trigger the abnormal transaction data from KDG
1. Detect abnormal transactions using Ad-hoc query from Athena

## Log analytics with Kinesis Firehose

Log analytics is a use case that allows you to analyze log data from websites, mobile devices, servers, sensors, and more for a wide variety of applications such as security event monitoring, digital marketing, application monitoring, fraud detection, ad tech, gaming, and IoT. In this lab, you will learn how to ingest and deliver Apache logs to Amazon S3 using Amazon Kinesis Data Firehose without managing any infrastructure. You can then use Amazon Athena to query log files to understand access patterns and web site performance issues.

![](https://user-images.githubusercontent.com/62965911/214810320-b27f4355-6f05-4f31-8b1c-4ef8a7b31983.png)

1. Create the Infra by using `./LogAnalyticsFirehose/template.yml` template
1. Send Apache access logs to Kinesis Firehose
1. Check the ingested data in S3
1. Analyze the data in Athena

## Streaming ETL using Kinesis Firehose

![](https://user-images.githubusercontent.com/62965911/214810237-e3dc797d-4924-4e6c-b55c-6d66e7f89914.png)

1. Create the Infra by using `./FirehoseKinesisStreamETL/template.yml` template
1. Send Apache access logs to Kinesis Firehose
1. Check the transformed data in S3
1. Analyze the data in Athena

## Optimize data streaming for storage and performance

While Apache access logs can provide insights into web applicaton usage, analyzing log files can be challenging considering the volume of data that a busy web application can generate. The queries you run on JSON data will become slower with the increasing data volumes. We can address this issue by converting the JSON input data into Apache Parquet or Apache ORC . Parquet and ORC are columnar data formats that save space and enable faster queries compared to row-oriented formats like JSON. Amazon Kinesis Data Firehose can convert the format of your input data from JSON to Apache Parquet or Apache ORC before storing the data in Amazon S3.

In this module, we will show you how you can convert the incoming tab delimited files into JSON using AWS Lambda function and then use record format conversion feature of Firehose to covert the JSON data into Parquet format before sending it to S3. We will use AWS Glue to store metadata. Finally, we query Parquet formatted data using Amazon Athena.

![](https://user-images.githubusercontent.com/62965911/214810344-9c52a0b6-a254-4738-8850-098dd767f68e.png)

1. Create the Infra by using `./FirehoseKinesisStreamETLParquet/template.yml` template
1. Send Apache access logs to Kinesis Firehose
1. Check the ingested data in S3
1. Run the Crawler
1. Analyze the Glue table
1. Querying Real Time Data