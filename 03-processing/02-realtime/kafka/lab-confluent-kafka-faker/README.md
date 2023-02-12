# Real-time CDC-enabled Extract and Load Pipeline with Kafka in Cloud

## Introduction

![](https://user-images.githubusercontent.com/62965911/211324123-05383bbe-5aeb-4362-9b02-68b23687ab1d.svg)

In this lab, we will setup a distributed multi-cluster (broker) Kafka server in Confluent Cloud Service. We will also connect to it via CLI command-line and Python APIs. We will send and receive events data and analyze various features of the Confluent service.

We will also use Postgres as our Producer, so that instead of sending the events via CLI/Python, we will upload data in Postgres and CDC (Change Data Capture) based Debezium connector in Confluent will automatically pull those changes into a Kafka topic. On the Sink side, we will use Amazon Redshift and S3, who will act as consumers. So the events that we get in our Kafka topic will be written in Amazon Redshift and S3. From S3, we will also use Amazon Athena to analyze the data in real-time in both destinations - Redshift and Athena.

We will use Python's Faker library to generate data.