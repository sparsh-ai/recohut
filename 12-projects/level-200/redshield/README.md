# AWS Kafka and DynamoDB for real time fraud detection

## Problem Statement

Organizations need to move data in realtime and serve the data with minimal latency to their end users. Kafka is a real-time data pipeline used to move the data in real time. DynamoDB is a low-latency, high throughput data layer that can scale and handle extreme spikes in workload. These services work great together to enable use cases such as offloading mainframe banking data in real time to Kafka and ingesting the Kafka stream into DynamoDB. Once the data is in DynamoDB, it can be serve real-time requests from an API.

In this workshop, we add a Kinesis Data Analytics application to enable real-time fraud detection as this data is ingesting.

The environment for this lab consists of:

- An EC2 instance with kafdrop.
  - Kafdrop is a web UI for viewing Kafka topics and browsing consumer groups. The tool displays information such as brokers, topics, partitions, consumers, and lets you view messages.
- In addition to the EC2 instance and networking components, the provided CloudFormation script creates the following AWS resources
  - A Managed Streaming for Kafka (MSK) cluster
  - A Kinesis Data Anayltics application
  - A DynamoDB fraud audit table

**Kafka Topics**

- Demo_transactions.
  - Topic to hold sample transactions (populated by Lambda SampleTransactionGenerator)
  - This topic should have transaction as sample transaction lambda function was started by the cloud formation script
- Flagged_accounts
  - Topic to hold flagged account Ids (populated by Lambda FlagAccountGenerator)
  - Initially, this topic will be empty as we need to manually run the lambda function to generate flagged acounts
- Processed_topic
  - Topic to hold flagged transactions (populated by flink application)
  - Initially, this topic will also be empty but will become populated once the sample transaction can successfully join with Flagged Accounts

![arch](https://user-images.githubusercontent.com/62965911/215308579-76b96550-f6a0-413a-b6bc-89f38e0874b6.png]

## Project Structure

```
.
├── [ 16K]  01-sa-kafka-dynamodb.ipynb
├── [2.0K]  assets
│   ├── [ 205]  download.sh
│   └── [1.6K]  ee-default-keypair.pem
├── [ 52K]  cfn
│   └── [ 51K]  fraud-detection-stack.json
└── [2.2K]  README.md

 377K used in 2 directories, 5 files
```