# Lab: Simplifying Data Engineering and Analytics with Delta

## Objective

1. Delta Lake for Loan Application Analysis
1. Simplifying Data Engineering and Analytics with Delta

## Introduction

Delta lake is an open-source storage layer for data lakes that brings ACID transactions to Apache Spark and big data workloads. Delta helps you generate reliable insights at scale and simplifies architecture around data pipelines, allowing you to focus primarily on refining the use cases being worked on. This is especially important when you consider that existing architecture is frequently reused for new use cases. It is becoming a defacto-standard for storing big amounts data for analytical purposes in a data lake. But what is behind it? How does it work under the hood? In this lab you we will dive deep into the internals of Delta Lake by unpacking the transaction log and also highlight some common pitfalls when working with Delta Lake (and show how to avoid them).

![arch](https://user-images.githubusercontent.com/62965911/214519834-8e6a0365-1a72-4c3b-93f5-df86c6b395bd.png)

The data used is a modified version of the public data from [Lending Club](https://www.kaggle.com/wendykan/lending-club-loan-data). It includes all funded loans from 2012 to 2017. Each loan includes applicant information provided by the applicant as well as the current loan status (Current, Late, Fully Paid, etc.) and latest payment information. For a full view of the data please view the data dictionary available [here](https://resources.lendingclub.com/LCDataDictionary.xlsx).

In this lab, we will explore and understand the following features of delta lake:

- ACID Transactions: Ensures data integrity and read consistency with complex, concurrent data pipelines.
- Unified Batch and Streaming Source and Sink: A table in Delta Lake is both a batch table, as well as a streaming source and sink. Streaming data ingest, batch historic backfill, and interactive queries all just work out of the box. 
- Schema Enforcement and Evolution: Ensures data cleanliness by blocking writes with unexpected.
- Time Travel: Query previous versions of the table by time or version number.
- Deletes and upserts: Supports deleting and upserting into tables with programmatic APIs.
- Open Format: Stored as Parquet format in blob storage.
- Audit History: History of all the operations that happened in the table.
- Scalable Metadata management: Able to handle millions of files are scaling the metadata operations with Spark.
- Explore the key challenges of traditional data lakes
- Appreciate the unique features of Delta that come out of the box
- Address reliability, performance, and governance concerns using Delta
- Analyze the open data format for an extensible and pluggable architecture
- Handle multiple use cases to support BI, AI, streaming, and data discovery
- Discover how common data and machine learning design patterns are executed on Delta
- Build and deploy data and machine learning pipelines at scale using Delta
- Introduction to Spark
- Complex Data Types in Spark
- Delta CRUD
- Delta for Batch and Streaming
- Data Consolidation in Delta Lake
- Handling Common Data Patterns with Delta
- Atypical Scenarios

![loanapp](https://user-images.githubusercontent.com/62965911/214520854-731ee4e3-295a-4b1e-a72d-bc618e480741.png)