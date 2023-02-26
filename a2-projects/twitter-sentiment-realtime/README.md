# Twitter Sentiment Realtime

## Objective

Real-time Pipeline for pulling data from twitter, estimating sentiment and showing on dashboard

The source is twitter and the main result to display on the dashboard is the sentiment analysis of a list of stocks. The final dashboard looks like this:

![dashboard](https://user-images.githubusercontent.com/62965911/215313939-dec9faf8-5b85-40bd-aed7-817915aceff5.png)

The heatmap indicates the sentiment analysis for each stock. The map indicates headquarters' location with the corresponding sentiment.

## Architecture

![arch](https://user-images.githubusercontent.com/62965911/215313933-59ecdf1e-ebec-451f-aa0b-5382309ae835.png)

## Solution

```
.
├── [ 201]  DockerfileA
├── [ 536]  DockerfileAW
├── [1.7K]  DockerfileB
├── [ 293]  DockerfileK
├── [ 262]  DockerfileS
├── [2.7K]  airflow
│   └── [2.6K]  dags
│       └── [2.6K]  orchestrator.py
├── [6.1K]  beam
│   ├── [1.6K]  Dockerfile
│   └── [4.4K]  dataflow
│       ├── [ 119]  requirements.txt
│       └── [4.1K]  transform.py
├── [5.2K]  docker-compose.yml
├── [ 799]  README.md
├── [  77]  requirements_airflow.txt
├── [  63]  requirements_kafka.txt
├── [  94]  requirements_spark.txt
├── [6.0K]  spark
│   ├── [ 631]  bigquery.py
│   ├── [2.7K]  consumer.py
│   ├── [ 760]  publisher.py
│   └── [1.8K]  utils.py
└── [5.1K]  terraform
    ├── [3.9K]  main.tf
    └── [1.1K]  variables.tf

  73K used in 7 directories, 22 files
```