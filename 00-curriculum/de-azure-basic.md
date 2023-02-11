# Curriculum - Data Engineering Training (Azure) | Basic

## Foundations

### Setup

#### Create Azure Account

#### Install Azure Powershell

Install Azure PowerShell on your machine; instructions for installing it can be found at [https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-6.6.00](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-6.6.00).

Run these commands to install and connect to azure:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force
Import-Module Az
Connect-AzAccount
```

## Azure Data Lake

### Creating and Managing Data in Azure Data Lake

[Source code](../02-data-storages/data-lakes/azure-data-lakes/lab-create-manage-data)

This lab focuses on provisioning, uploading, and managing the data life cycle in Azure Data Lake accounts.

- Recipe 1a - Provisioning an Azure storage account using the Azure portal
- Recipe 1b - Provisioning an Azure storage account using PowerShell
- Recipe 2 - Creating containers and uploading files to Azure Blob storage using PowerShell
- Recipe 3 - Managing blobs in Azure Storage using PowerShell
  - Recipe 3a - Copying blobs between containers
  - Recipe 3b - Listing blobs in an Azure storage container
  - Recipe 3c - Modifying a blob access tier
  - Recipe 3d - Downloading a blob
  - Recipe 3e - Deleting a blob
- Recipe 4 - Configuring blob lifecycle management for blob objects using the Azure portal

### Securing and Monitoring Data in Azure Data Lake

[Source code](../02-data-storages/data-lakes/azure-data-lakes/lab-securing-monitoring-lakes)

This lab covers securing an Azure Data Lake account using firewall and private links, accessing data lake accounts using managed identities, and monitoring an Azure Data Lake account using Azure Monitor.

- Recipe 1 - Configuring a firewall for an Azure Data Lake account using the Azure portal
- Recipe 2 - Configuring virtual networks for an Azure Data Lake account using the Azure portal
- Recipe 3 - Configuring encryption using Azure Key Vault for Azure Data Lake
- Recipt 4 - Creating an alert to monitor an Azure storage account

## Azure Data Factory

### Building Data Ingestion Pipelines Using Azure Data Factory

[Source code](../05-data-pipelines/azure-data-factory/lab-data-ingestion-pipeline)

This lab covers ingesting data using Azure Data Factory and copying data between Azure SQL Database and Azure Data Lake.

- Recipe 1 - Provisioning Azure Data Factory
- Recipe 2 - Copying files to a database from a data lake using a control flow and copy activity
- Recipe 3 - Triggering a pipeline in Azure Data Factory
- Recipe 4 - Copying data from a SQL Server virtual machine to a data lake using the Copy data wizard

## Azure SQL Database

### Configuring and Securing Azure SQL Database

[Source code](../02-data-storages/databases/azure-sql/lab-securing-azure-sql-databases)

This lab covers configuring a Serverless SQL database, Hyperscale SQL database, and securing Azure SQL Database using virtual networks and private links.

- Recipe 1 - Provisioning and connecting to an Azure SQL database using PowerShell
- Recipe 2 - Implementing an Azure SQL Database elastic pool using PowerShell

### Implementing High Availability and Monitoring in Azure SQL Database

This lab explains configuring high availability to Azure SQL Database using auto-failover groups and read replicas, monitoring Azure SQL Database, and the automated scaling of Azure SQL Database during utilization spikes.

## Azure Databricks

### Processing Data Using Azure Databricks

[Source code](../04-data-transformation/azure-databricks/lab-data-processing-azure-dbr)

This lab covers integrating Azure Databricks with Azure Data Lake and Azure Key Vault, processing data using Databricks notebooks, and working with Delta tables.

- Recipe 1 - Configuring the Azure Databricks environment
- Recipe 2 - Integrate Databricks with Azure Key Vault
- Recipe 3 - Mounting an Azure Data Lake container in Databricks
- Recipe 4 - Processing data using notebooks
- Recipe 5 - Scheduling notebooks using job clusters
- Recipe 6 - Working with Delta Lake tables

## Azure Synapse Analytics

### Processing Data Using Azure Synapse Analytics

[Source code](../04-data-transformation/azure-synapse-analytics/lab-data-processing-synapse-analytics)

This lab covers exploring data using Synapse Serverless SQL pool, processing data using Synapse Spark Pools, Working with Synapse Lake database, and integrating Synapse Analytics with Power BI.

* Recipe 1 - Provisioning an Azure Synapse Analytics workspace
* Recipe 2 - Analyzing data using serverless SQL pool
* Recipe 3 - Provisioning and configuring Spark pools
* Recipe 4 - Processing data using Spark pools and a lake database
* Recipe 5 - Querying the data in a lake database from serverless SQL pool
* Recipe 6 - Scheduling notebooks to process data incrementally

### Transforming Data Using Azure Synapse Dataflows

This lab focuses on performing transformations using Synapse Dataflows, optimizing data flows using partitioning, and managing dynamic source schema changes using schema drifting.

### Building the Serving Layer in Azure Synapse SQL Pools

This lab covers loading processed data into Synapse dedicated SQL pools, performing data archival using partitioning, managing table distributions, and optimizing performance using statistics and workload management.

### Monitoring Synapse SQL and Spark Pools

This lab covers monitoring Synapse dedicated SQL and Spark pools using Azure Log Analytics workbooks, Kusto scripts, and Azure Monitor, and monitoring Synapse dedicated SQL pools using Dynamic Management Views (DMVs).

### Optimizing and Maintaining Synapse SQL and Spark Pools

This lab offers techniques for tuning query performance by optimizing query plans, rebuilding replication caches and maintenance scripts to optimize Delta tables, and automatically pausing SQL pools during inactivity, among other things.

## Azure Data Engineering Pipelines

### Monitoring and Maintaining Azure Data Engineering Pipelines

This lab covers monitoring and managing end-to-end data engineering pipelines, which includes tracking data lineage using Microsoft Purview and improving the observability of pipeline executions using log analytics and query labeling.
