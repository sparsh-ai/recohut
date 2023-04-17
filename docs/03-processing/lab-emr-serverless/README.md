# Lab: EMR Serverless

> Creating and submitting Word count Spark Job in EMR Serverless

## Objective

Data Transformation with PySpark using Amazon EMR Serverless Application

## Introduction

By the end of the lab, you will be able to:

1. Create Amazon EMR Serverless Application for Spark
1. Submit Spark jobs to EMR Serverless Application
1. Create Amazon EMR Serverless Application for Hive
1. Submit Hive jobs to EMR Serverless Application
1. Use Spark UI for monitoring and debugging

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/03-processing/lab-emr-serverless)

```
├── [ 503]  README.md
├── [7.1K]  assets
│   └── [7.0K]  mwaa_plugin.zip
├── [ 22K]  cfn
│   ├── [4.7K]  emr-serverless-cfn-v2.json
│   └── [ 17K]  mwaa_emr.yml
├── [ 26K]  main.ipynb
├── [ 52K]  orchestration
│   ├── [ 49K]  airflow.cfg
│   ├── [1.1K]  dags
│   │   └── [1004]  example_emr_serverless.py
│   ├── [ 589]  init.sh
│   ├── [ 120]  requirments.txt
│   └── [ 754]  scripts
│       └── [ 658]  pi.py
└── [ 20K]  src
    ├── [ 105]  count.sql
    ├── [ 778]  create_taxi_trip.sql
    ├── [2.3K]  example_emr_serverless.py
    ├── [3.7K]  hudi-cow.py
    ├── [3.8K]  hudi-mor.py
    ├── [3.7K]  hudi-upsert-cow.py
    ├── [3.8K]  hudi-upsert-mor.py
    └── [1.1K]  wordcount.py

 128K used in 6 directories, 18 files
```

## Notebook

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/03-processing/lab-emr-serverless/main.ipynb)