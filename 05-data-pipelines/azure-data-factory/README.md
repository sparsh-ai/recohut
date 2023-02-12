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
