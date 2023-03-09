# Azure Synapse Analytics

Azure Synapse Analytics workspaces generation 2, formally released in December 2020, is the industry-leading big data solution for processing and consolidating data of business value. Azure Synapse Analytics has three important components:

* SQL pools and Spark pools for performing data exploration and processing
* Integration pipelines for performing data ingestion and data transformations
* Power BI integration for data visualization

Having data ingestion, processing, and visualization capabilities in a single service with seamless integration with all other services makes Azure Synapse Analytics a very powerful tool in big data engineering projects.

## Azure Synapse Data Flows

Azure Synapse data flows allow us to perform transformations on the data such as converting data format, filtering, merging, and sorting while moving the data from the source to the destination. The best part about Synapse data flows is the user-friendly interface that allows us to perform complex data transformations in a few clicks.

## Labs

### Processing Data Using Azure Synapse Analytics [[Source code](03-procesing/azure-synapse-analytics/lab-data-processing-synapse-analytics/)]

This lab covers exploring data using Synapse Serverless SQL pool, processing data using Synapse Spark Pools, Working with Synapse Lake database, and integrating Synapse Analytics with Power BI

- Recipe 1 - Provisioning an Azure Synapse Analytics workspace
- Recipe 2 - Analyzing data using serverless SQL pool
- Recipe 3 - Provisioning and configuring Spark pools
- Recipe 4 - Processing data using Spark pools and a lake database
- Recipe 5 - Querying the data in a lake database from serverless SQL pool
- Recipe 6 - Scheduling notebooks to process data incrementally

### Transforming Data Using Azure Synapse Dataflows [[Source code](03-procesing/azure-synapse-analytics/lab-azure-synapse-dataflows/)]

This lab focuses on performing transformations using Synapse Dataflows, optimizing data flows using partitioning, and managing dynamic source schema changes using schema drifting

- Recipe 1 - Copying data using a Synapse data flow
- Recipe 2 - Performing data transformation using activities such as join, sort, and filter
- Recipe 3 - Monitoring data flows and pipelines
- Recipe 4 - Configuring partitions to optimize data flows
- Recipe 5 - Parameterizing mapping data flows
- Recipe 6 - Handling schema changes dynamically in data flows using schema drift

### Implementing the Serving Layer Star Schema [[Source code](03-procesing/azure-synapse-analytics/lab-implementing-star-schema/)]

In this lab, we will learn about implementing the serving layer, which involves implementing star schemas, techniques to read and write different data formats, sharing data between services such as SQL and Spark, and more.

Once you complete this lab, you should be able to understand the differences between a Synapse dedicated SQL pool versus traditional SQL systems for implementing the Star schema, the various ways of accessing Parquet data using technologies such as Spark and SQL, and the details involved in storing metadata across services. All this knowledge should help you build a practical and maintainable serving layer in a data lake.

- Recipe 1 - Delivering data in a relational star schema
- Recipe 2 - Implementing a dimensional hierarchy
- Recipe 3 - Delivering data in Parquet files
- Recipe 4 - Maintaining metadata
