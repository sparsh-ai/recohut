# Lab: Glue ETL and CDC UPSERT

> Handle UPSERT data operations using open-source Delta Lake and AWS Glue

Many customers need an ACID transaction (atomic, consistent, isolated, durable) data lake that can log change data capture (CDC) from operational data sources. There is also demand for merging real-time data into batch data. Delta Lake framework provides these two capabilities. In this lab, we learn how to handle UPSERTs (updates and inserts) of the operational data using natively integrated Delta Lake with [AWS Glue](https://aws.amazon.com/glue/), and query the Delta Lake using [Amazon Athena](https://aws.amazon.com/athena/).

We examine a hypothetical insurance organization that issues commercial policies to small- and medium-scale businesses. The insurance prices vary based on several criteria, such as where the business is located, business type, earthquake or flood coverage, and so on. This organization is planning to build a data analytical platform, and the insurance policy data is one of the inputs to this platform. Because the business is growing, hundreds and thousands of new insurance policies are being enrolled and renewed every month. Therefore, all this operational data needs to be sent to Delta Lake in near-real time so that the organization can perform various analytics, and build machine learning (ML) models to serve their customers in a more efficient and cost-effective way.

The use case we use in this lab is about a commercial insurance company. We use a simple dataset that contains the following columns:

* **Policy** – Policy number, entered as text
* **Expiry** – Date that policy expires
* **Location** – Location type (Urban or Rural)
* **State** – Name of state where property is located
* **Region** – Geographic region where property is located
* **Insured Value** – Property value
* **Business Type ** – Business use type for property, such as Farming or Retail
* **Earthquake** – Is earthquake coverage included (Y or N)
* **Flood** – Is flood coverage included (Y or N)

Note: The dataset contains a sample of 25 insurance policies. In the case of a production dataset, it may contain millions of records.

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/03-processing/lab-glue-deltalake-cdc-upsert)

```
├── [2.2K]  README.md
├── [1.8K]  data
│   ├── [ 282]  cdc-load.csv
│   └── [1.4K]  full-load.csv
├── [ 158]  glue-targets.json
├── [6.8K]  jobs
│   ├── [3.9K]  CDC-Load-Job.json
│   └── [2.8K]  Full-Load-Job.json
├── [ 51K]  main.ipynb
├── [ 634]  policy-document.json
└── [ 238]  role-trust.json

  63K used in 2 directories, 9 files
```

## Notebook

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/03-processing/lab-glue-deltalake-cdc-upsert/main.ipynb)