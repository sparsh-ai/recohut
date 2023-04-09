# Azure Data Factory

**Azure Data Factory** is the data orchestration service in Azure. Using Azure Data Factory, you can build pipelines that are capable of reading data from multiple sources, transforming the data, and loading the data into data stores to be consumed by reporting applications such as Power BI. Azure Data Factory much like **SQL Server Integration Services** (**SSIS**) in an on-premises world, provides a code-free UI for developing, managing, and maintaining data engineering pipelines.

ADF is a managed cloud service that can be used to coordinate and orchestrate complex cloud- or hybrid- (on-premises)-based pipelines. ADF provides the ability to build ETL and **extract, load, transform** (**ELT**) pipelines. With ADF, you can do the following:

- Ingest data from a wide variety of sources such as databases, file shares, **Internet of Things** (**IoT**) hubs, **Amazon Web Services** (**AWS**), **Google Cloud Platform** (**GCP**), and more.
- Build complex pipelines using variables, parameters, branches, and so on.
- Transform data by using compute services such as Synapse, HDInsight, Cosmos DB, and so on.
- Schedule and monitor ingestions, control flow, and data flow operations.

ADF is built of some basic set of components. The important ones are listed here:

- **Pipelines**---A pipeline is a collection of activities that are linked together to perform some control flow or data transformation.
- **Activities**---Activities in ADF refer to the steps in the pipeline such as copying data, running a Spark job, and so on.
- **Datasets**---This is the data that your pipelines or activities operate on.
- **Linked Services**---Linked services are connections that ADF uses to connect to a variety of data stores and computes in Azure. They are like connection strings that let you access data from external sources.
- **Triggers**---Triggers are events that are used to start pipelines or start an activity.

NOTE

> All ADF transformations happen on datasets. So, before we can do any transformation, we will have to create datasets of the source data.
>
> ![B17525_08_003](https://user-images.githubusercontent.com/62965911/218307653-c4af60b8-fba1-4a6b-a7c1-e2e8fd4f5fa2.jpeg)

## Labs

### Building Data Ingestion Pipelines using Azure Data Factory [[Source code](06-orchestration/azure-data-factory/lab-data-ingestion-pipeline/)]

This lab covers ingesting data using Azure Data Factory and copying data between Azure SQL Database and Azure Data Lake.

- Recipe 1 - Provisioning Azure Data Factory
- Recipe 2 - Copying files to a database from a data lake using a control flow and copy activity
- Recipe 3 - Triggering a pipeline in Azure Data Factory
- Recipe 4 - Copying data from a SQL Server virtual machine to a data lake using the Copy data wizard

### Incremental Data Loading using Azure Data Factory [[Source code](06-orchestration/azure-data-factory/lab-adf-incremental-loading/)]

This lab covers various methods to perform data loading in incremental fashion.

- Recipe 1 - Using Watermarking
- Recipe 2 - Using File Timestamps
- Recipe 3 - Using File partitions and folder structures

### Develop Batch Processing Solution using Azure Data Factory [[Source code](06-orchestration/azure-data-factory/lab-batch-processing-solution/)]

In this lab, we design an end-to-end batch processing solution by using Data Factory, Data Lake, Spark, Azure Synapse Pipelines, PolyBase, and Azure Databricks

- Recipe 1 - Data Ingestion using Data Flow
- Recipe 2 - Data Transformation using Azure Databricks
- Recipe 3 - Data Serving using PolyBase
- Recipe 4 - Data Pipeline using Azure Data Factory Pipeline
- Recipe 5 - End to end data processing with Azure Batch
