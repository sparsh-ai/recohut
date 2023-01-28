# Log Analytics and Processing in Real-Time

## Lab 1: Apache Flink on Amazon Kinesis Data Analytics

In this workshop, you will build an end-to-end streaming architecture to ingest, analyze, and visualize streaming data in near real-time. You set out to improve the operations of a taxi company in New York City. You'll analyze the telemetry data of a taxi fleet in New York City in near-real time to optimize their fleet operations.

We use a scenario to analyze the telemetry data of a taxi fleet in New York City in near real-time to optimize the fleet operation.

In this scenario, every taxi in the fleet is capturing information about completed trips. The tracked information includes the pickup and drop-off locations, number of passengers, and generated revenue. This information is produced into a Kinesis data stream as a simple JSON blob.

From there, the data is processed and analyzed to identify areas that are currently requesting a high number of taxi rides. The derived insights are finally visualized in a dashboard for operators to inspect.

![flink-arch](https://user-images.githubusercontent.com/62965911/215279757-dcb251a5-751a-4572-af17-94e5906aa75b.png)

Throughout the course of this workshop, you will build a fully managed infrastructure that can analyze the data in near-time, ie, within seconds, while being scalable and highly available. The architecture will leverage Amazon Kinesis Data Stream as a streaming store, Amazon Kinesis Data Analytics  to run an Apache Flink  application in a fully managed environment, and Amazon OpenSearch Service  and Kibana  for visualization.

Along the way, we will learn about basic Flink concepts and common patterns for streaming analytics. We will also cover how KDA for Apache Flink is different from a self-managed environment and how to effectively operate and monitor streaming architectures.

## Lab 2: Apache Flink on Amazon Kinesis Data Analytics Studio

In this lab we will explore Kinesis Data Analytics (KDA) via. KDA Studio Notebooks. KDA Studio Notebooks provide an interactive development experience for Apache Flink. Studio notebooks allow us to easily develop Flink applications and then deploy them as long running KDA applications.

For this lab we will stream and analyze the NYC Taxi Cab trips data set  with the SQL language in Flink .

We will implement the following architecture:

![flink-stdo-arch](https://user-images.githubusercontent.com/62965911/215279759-13866655-1300-47f9-987b-113916a4dab0.png)

## Lab 3: Apache Beam on Amazon Kinesis Data Analytics

In this workshop, we explore an end to end example that combines batch and streaming aspects in one uniform Apache Beam pipeline. We start to analyze incoming taxi trip events in near real time with an Apache Beam pipeline. We then show how to archive the trip data to Amazon S3 for long term storage. We subsequently explain how to read the historic data from S3 and backfill new metrics by executing the same Beam pipeline in a batch fashion. Along the way, you also learn how you can deploy and execute the Beam pipeline with Amazon Kinesis Data Analytics in a fully managed environment.

![beam-arch](https://user-images.githubusercontent.com/62965911/215279753-6c15a80c-fff5-460f-abe3-ef889294bed3.png)

So you will not only learn how you can leverage Apache Beam’s expressive programming model to unify batch and streaming you will also learn how AWS can help you to effectively build and operate Beam based streaming architectures with low operational overhead.

![kibana_nyc](https://user-images.githubusercontent.com/62965911/215279760-6cbcc4a8-0ea9-4808-a901-69915763cb45.png)

## Project Structure

```
├── [ 35K]  01-sa-apache-flink-kinesis.ipynb
├── [ 12K]  02-sa-apache-flink-kinesis-studio.ipynb
├── [ 32K]  03-sa-apache-beam-kinesis.ipynb
├── [3.6K]  README.md
├── [ 339]  assets
│   └── [ 243]  download.sh
├── [204K]  cfn
│   ├── [102K]  beam_lab.json
│   └── [102K]  flink_lab.json
└── [  59]  download.sh

 287K used in 2 directories, 8 files
```