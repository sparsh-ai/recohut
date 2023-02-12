# Azure Data Engineering

Case study - data lake
----------------------

In a case study question, a use case will be described in detail with multiple inputs such as business requirements and technical requirements. You will have to carefully read the question and understand the requirements before answering the question.

### Background

Let's assume you are a data architect in a retail company that has both online and bricks and mortar outlets all over the world. You have been asked to design their data processing solution. The leadership team wants to see a unified dashboard of daily, monthly, and yearly revenue reports in a graphical format, from across all their geographic locations and the online store.

The company has analysts who are SQL experts.

For simplicity, let's assume that the retail outlets are in friendly countries, so there is no limitation in terms of moving data across the countries.

### Technical details

The online transaction data gets collected into Azure SQL instances that are geographically spread out. The overall size is about 10 GB per day.

The bricks and mortar point of sale transactions are getting collected in local country-specific SQL Server databases with different schemas. The size is about 20 GB per day.

The store details are stored as JSON files in Azure Data Lake Gen2.

The inventory data is available as CSV files in Azure Data Lake Gen2. The size is about 500 MB per day.

> TIP: The trick is to identify key terminologies such as file formats, streaming, or batching (based on the frequency of reports), the size of the data, security restrictions - if any, and technologies to be used, such as SQL in this case (as the analysts are SQL experts). Once we have all this data, the decision-making process becomes a bit simpler.

#### Question 1

Choose the right storage solution to collect and store all the different types of data.

[Options: Azure Synapse SQL pool, Azure Data Lake Gen2, Azure Files, Event Hubs]

#### Solution

**Azure Data Lake Gen2**

#### Explanation

- ADLS Gen2 can handle multiple different types of formats and can store petabytes of data. Hence, it would suit our use case.
- Azure Synapse SQL pool is for storing processed data in SQL tables.
- Azure Files are file sharing storage services that can be accessed via **Server Message Block** (**SMB**) or **Network File System** (**NFS**) protocols. They are used to share application settings, as extended on-premises file servers, and so on.
- Event Hubs is used for streaming real-time events and not an actual analytical data store.

#### Question 2

Choose the mechanism to copy data over into your common storage.

[Choices: PolyBase, Azure Data Factory, Azure Databricks, Azure Stream Analytics]

#### Solution

**Azure Data Factory**

#### Explanation

- ADF provides connectors to read data from a huge variety of sources, both on the cloud and on-premises. Hence, it will be a good fit for this situation.
- PolyBase is mostly used for converting data from different formats to standard SQL table formats and copying them into Synapse SQL pool.
- Azure Databricks can be used for batch and Spark stream processing, not for storing large volumes of data.
- Azure Stream Analytics is used for stream processing, not for storing large volumes of data.

#### Question 3

Choose storage to store the daily, monthly, and yearly data for the analysts to query and generate reports using SQL.

[Choices: Azure Databricks, Azure Queues, Synapse SQL pool, Azure Data Factory]

#### Solution

**Synapse SQL pool**

#### Explanation

- Synapse SQL pool is a data warehouse solution that perfectly fits the requirements for storing data to generate reports and find insights. The daily, monthly, and yearly data is usually the data that is cleaned, filtered, joined, aggregated from various sources, and stored in pre-defined schemas for easy analysis. Since Synapse SQL pools are natively SQL-based, it works well for analysts of the company who are SQL experts.
- Azure Databricks is used for batch and stream processing, not for storing large volumes of data. Hence, it wouldn't fit the bill for our use case.
- Azure Queues storage is a messaging service that can hold millions of messages and that can be processed asynchronously. Hence, it wouldn't fit the bill for our use case.
- Azure Data Factory is used to copy/move data, do basic transformations, and orchestrate pipelines. It cannot be used for storing data.

  > TIP: If you find terminologies that you are not aware of, use the principle of negation to find the most suitable answer. In this case, if you didn't know what Azure Queues does, you can try to establish whether any of the other options is a good solution and then go with it. Or, if you are not sure, try to eliminate the obviously wrong answers and take an educated guess.
  >

#### Question 4

Visualize the insights generated in a graphical format.

[Choices: Azure Data Factory, Synapse Serverless SQL pool, Power BI, Azure Databricks]

#### Solution

**Power BI**

#### Explanation

- Power BI can generate insights from various sources of data, such as Synapse SQL pools, Azure Stream Analytics, Azure SQL, and Cosmos DB. It provides a very rich set of tools to graphically display the data.
- ADF provides connectors to read data from a huge variety of sources and orchestration support. Hence, it will not be a good fit for this situation.
- Synapse SQL pool is a data warehouse solution that can be used to process data and store it, to be used by business intelligence tools such as Power BI.
- Azure Databricks can be used for visualizing data patterns, but not usually for generating and visualizing graphical insights.

## Case study - data lake

The case study questions will have a detailed description of the case followed by the questions.

### Background

You have been hired to build a ticket scanning system for a country's railways department. Millions of passengers will be traveling on the trains every day. It has been observed that some passengers misuse their tickets by sharing them with others or using them for more rides than allowed. The railway officers want a real-time system to track such fraud occurrences.

### Technical details

- A ticket is considered fraudulent it if is used more than 10 times a day.
- Build a real-time alerting system to generate alerts whenever such fraud happens.
- Generate a monthly fraud report of the number of incidents and the train stations where it happens.

You need to build a data pipeline. Recommend the services that can be used to build such a fraud detection system.

#### Question 1

You recommend the following components to be used:

- Azure Blob storage to consume the data
- Azure Stream Analytics to process the fraud alerts
- Power BI to display the monthly report

[Options: Correct/ Incorrect]

#### Solution

**Incorrect**

#### Explanation

We cannot use Azure Blob storage to consume real-time data. It is used to store different formats of data for analytical processing or long-term storage.

#### Question 2

You recommend a system to use:

- IOT Hub to consume the data
- Azure Stream Analytics to process the fraud alerts
- Azure Databricks to store the monthly data and generate the reports
- Power BI to display the monthly report

[Options: Correct/ Incorrect]

#### Solution

**Incorrect**

#### Explanation

We cannot use Azure Databricks to store the monthly data. It is not a storage service; it is a compute service.

#### Question 3

You recommend a system to use:

- IOT Hub to consume the data
- Azure Stream Analytics to process the fraud alerts
- Azure Synapse SQL pool to store the monthly data and generate the reports
- Power BI to display the monthly report

[Options: Correct/ Incorrect]

#### Solution

**Correct**

#### Explanation

IOT Hub can be used to consume real-time data and feed it to Azure Stream Analytics. Stream Analytics can perform real-time fraud detection and store the aggregated results in Synapse SQL pool. Synapse SQL pool can store petabytes of data for longer durations to generate reports. Power BI can graphically display both the real-time alerts and monthly reports. So, this is the right set of options.

Let's look at a data visualization question next.

Data visualization
------------------

You have data from various data sources in JSON and CSV formats that has been copied over into Azure Data Lake Gen2. You need to graphically visualize the data. What tool would you use?

- Power BI
- Azure Databricks/Synapse Spark
- Azure Data Factory
- Azure Storage Explorer

### Solution

**Azure Databricks/Synapse Spark**

### Explanation

- Azure Databricks Spark or Synapse Spark provides graphing options that can be used to sample and visualize data.
- Power BI is not used to visualize raw data. It is used to visualize insights derived from processed data.
- Azure Data Factory provides options to preview the data, but not many options for graphically visualizing it.
- Storage Explorer helps explore the filesystem but doesn't have the ability to visualize the data graphically.

  > TIP: Look for the nuances in the question. The moment we see *graphically visualize*, we tend to select Power BI. But Azure Databricks Spark has built-in graphing tools that can help visualize the data. Power BI is used to build and display insights from processed data.
  >

Let's look at a data partition question next.

Data partitioning
-----------------

You have a table as follows in Azure SQL:

```sql
CREATE TABLE Books {
   BookID VARCHAR(20) NOT NULL,
   CategoryID VARCHAR (20) NOT NULL,
   BookName VARCHAR (100),
   AuthorID VARCHAR (20),
   ISBN VARCHAR (40)
}
```

Assume there are 100 million entries in this table. **CategoryID** has about 25 entries and 60% of the books align to about 20 categories. You need to optimize the performance of this table for queries that aggregate on **CategoryID**. What partitioning technique would you use and what key would you choose?

- Vertical partitioning with **CategoryID**
- Horizontal partitioning with **BookID**
- Vertical partitioning with **BookID**
- Horizontal partitioning with **CategoryID**

### Solution

Horizontal partitioning with **CategoryID**

### Explanation

- Horizontal partitioning with **CategoryID** is the right choice as we need to horizontally partition (shard) the data based on **categoryID**, which has a fairly good distribution. This can speed up the processing by distributing the data evenly across the partitions.
- Vertical partitioning with **CategoryID** - Splitting the table vertically will not optimize as we will have to scan through the entire database to aggregate the categories. Vertical partitioning is effective when we need to speed up queries only based on a few columns.
- Horizontal partitioning with **BookID** - Horizontal partitioning (sharding) is fine, but the key we are looking to optimize is the categories. So **BookID** will not create the optimal partitions.
- Vertical partitioning with **BookID** - For the same reason as vertical partitioning with **CategoryID**, vertical partitions will not be efficient as we need to access all the rows.

Let's look at a Synapse SQL pool design question next.

Synapse SQL pool table design - 1
---------------------------------

You are the architect of a cab company. You are designing the schema to store trip information. You have a large fact table that has a billion rows. You have dimension tables in the range of 500--600 MB and you have daily car health data in the range of 50 GB. The car health data needs to be loaded into a staging table as quickly as possible. What distributions would you choose for each of these types of data?

- A - Fact table
- B - Dimension tables
- C - Staging table

[Options: Round Robin, Hash, Replicated]

### Solution

- A - Fact table - Hash
- B - Dimension tables - Replicated
- C - Staging table - Round Robin

### Explanation

- **Replicated** - Use replication to copy small tables to all the nodes so that the processing is much faster without much network traffic.
- **Hash** - Use hash distribution for fact tables that contain millions or billions of rows/are several GBs in size. For small tables, hash distribution will not be very performant.
- **Round Robin** - Use round robin for staging tables where you want to quickly load the data.

Let's look at another Synapse SQL pool design question next.

Synapse SQL pool table design - 2
---------------------------------

You are a data engineer for an online bookstore. The bookstore processes hundreds of millions of transactions every month. It has a Catalog table of about 100 MB. Choose the optimal distribution for the Catalog table and complete the following script:

```sql
CREATE TABLE Catalogue (
   BookID VARCHAR 50,
   BookName VARCHAR 100,
   ISBN: VARCHAR 100,
   FORMAT: VARCHAR 20
) WITH
   CLUSTERED COLUMNSTORE INDEX,
   DISTRIBUTION = ___________
)
```

[Options: **ROUND-ROBIN**, **REPLICATE**, **HASH**, **PARTITION**]

### Solution

**Replicate**

### Explanation

- Replicate distribution copies the data to all the compute nodes. Hence, the processing will be much faster in the case of smaller tables.
- **Hash** - Use hash distribution for fact tables that contain millions of rows or are several GBs in size. For small tables, hash distribution will not be very performant.
- **Round Robin** - Use round robin for staging tables where you want to quickly load the data.
- **Partition** - This is used for data partitioning, which is not our use case.

Let's look at a slowly changing dimension question next.

Slowly changing dimensions
--------------------------

Identify the type of SCD by looking at this table definition:

```sql
CREATE TABLE DimCustomer (
   SurrogateID IDENTITY,
   CustomerID VARCHAR(20),
   Name VARCHAR(100),
   Email VARCHAR(100),
   StartDate DATE,
   EndDate DATE,
   IsActive INT
)
```

[Options: SCD Type 1, SCD Type 2, SCD Type 3]

### Solution

**SCD Type 2**

### Explanation

SCD Type 2 keeps track of all the previous records using the **StartDate**, **EndDate**, and, optionally, an **IsActive** or a **VersionNumber** field.

Let's look at a storage tier-based question next.

Storage tiers
-------------

You are a data engineer working with an ad serving company. There are three types of data the company wants to store in Azure Blob storage. Select the storage tiers that you should recommend for each of the following scenarios.

- A - Auditing data for the last 5 years for yearly financial reporting
- B - Data to generate monthly customer expenditure reports
- C - Media files to be displayed in online ads

[Options: Hot, Cold, Archive]

### Solution

A - Archive

B - Cold

C - Hot

### Explanation

- Auditing data is accessed rarely and the use case says yearly financial reporting. So, this is a good candidate for the archive tier. The archive tier requires the data to be stored for at least 180 days.
- Monthly customer expenditure data is not used frequently, so it is a good candidate for cold storage. Cold storage requires the data to be stored for at least 30 days.
- Media files to be displayed in ads will be used every time the ad is displayed. Hence, this needs to be on the hot tier.

Let's look at a disaster recovery question next.

Disaster recovery
-----------------

You work in a stock trading company that stores most of its data on ADLS Gen2 and the company wants to ensure that the business continues uninterrupted even when an entire data center goes down. Select the disaster recovery option(s) that you should choose for such a requirement:

- **Geo-Redundant Storage** (**GRS**)
- **Zone-Redundant Storage** (**ZRS**)
- **Geo-Zone-Redundant Storage** (**GZRS**)
- **Locally Redundant Storage** (**LRS**)
- **Geo-Replication**

### Solution

- **Geo-Redundant Storage** (**GRS**) or **Geo-Zone-Redundant Storage** (**GZRS**)

### Explanation

- Both **Geo-Redundant Storage** (**GRS**) and **Geo-Zone-Redundant Storage** (**GZRS**) can ensure that the data will be available even if entire data centers or regions go down. The difference between GRS and GZRS is that in GRS, the data is synchronously copied three times within the primary region using the LRS technique, but in GZRS, the data is synchronously copied three times within the primary region using ZRS. With GRS and GZRS, the data in the secondary region will not be available for simultaneous read or write access. If you need simultaneous read access in the secondary regions, you could use the **Read-Access - Geo-Redundant Storage** (**RA-GRS**) or **Read-Access Geo-Zone-Redundant Storage** (**RA-GZRS**) options.
- LRS - LRS provides only local redundancy, but doesn't guarantee data availability if entire data centers or regions go down.
- ZRS - ZRS provides zone-level redundancy but doesn't hold up if the entire data center or region goes down.
- Geo-replication - This is an Azure SQL replication feature that replicates the entire SQL server to another region and provides read-only access in the secondary region.

  > TIP: If you notice any options that you are not aware of, don't panic. Just look at the ones you are aware of and check whether any of those could be the answer. For example, in the preceding question, if you had not read about geo-replication, it would have still been okay because the answer was among the choices that you already knew.
  >

Synapse SQL external tables
---------------------------

Fill in the missing code segment to read Parquet data from an ADLS Gen2 location into Synapse Serverless SQL:

```sql
IF NOT EXISTS (SELECT * FROM sys.external_file_formats
WHERE name = 'SynapseParquetFormat')
    CREATE ____________ [SynapseParquetFormat]
    WITH (FORMAT_TYPE = PARQUET)
IF NOT EXISTS (SELECT * FROM sys.external_data_sources
WHERE name = 'sample_acct')
    CREATE _____________ [sample_acct]
    WITH (
        LOCATION   = 'https://sample_acct.dfs.core.windows.net/users',
    )

CREATE ______________ TripsExtTable (
    [TripID] varchar(50),
    [DriverID] varchar(50),
    . . .
    )
    WITH (
    LOCATION = 'path/to/*.parquet',
    DATA_SOURCE = [sample_acct],
    FILE_FORMAT = [SynapseParquetFormat]
    )

GO
```

[Options: **TABLE**, **EXTERNAL TABLE**, **EXTERNAL FILE FORMAT**, **EXTERNAL DATA SOURCE**, **VIEW**, **FUNCTION**]

You can reuse the options provided above for more than one blank if needed.

### Solution

**EXTERNAL FILE FORMAT**, **EXTERNAL DATA SOURCE**, **EXTERNAL TABLE**

### Explanation

- The correct keywords are **EXTERNAL FILE FORMAT**, **EXTERNAL DATA SOURCE**, and **EXTERNAL TABLE** in the order in which they appear in the question.
- You cannot use **TABLE** as this is not an internal table. We are reading external Parquet data as an external table.
- You cannot use **VIEW** as views are logical projections of existing tables.
- You cannot use **FUNCTION** as this is not a UDF.

Let's next look at some sample questions from the data processing section.

Data lake design
----------------

You are working in a marketing firm. The firm provides social media sentiment analysis to its customers. It captures data from various social media websites, Twitter feeds, product reviews, and other online forums.

Technical requirements:

- The input data includes files in CSV, JSON, image, video, and plain text formats.
- The data is expected to have inconsistencies such as duplicate entries and missing fields.
- The overall data size would be about 5 petabytes every month.
- The engineering team are experts in Scala and Python and would like a Notebook experience.
- Engineers must be able to visualize the data for debugging purposes.
- The reports have to be generated on a daily basis.
- The reports should have charts with the ability to filter and sort data directly in the reports.

You need to build a data pipeline to accomplish the preceding requirements. What are the components you would select for the following zones of your data lake?

**Landing zone**:

[Options: Azure Data Lake Gen2, Azure Blob storage, Azure Synapse SQL, Azure Data Factory]

**Transformation zone**:

[Options: Synapse SQL pool, Azure Databricks Spark, Azure Stream Analytics]

**Serving zone**:

[Options: Synapse SQL pool, Azure Data Lake Gen2, Azure Stream Analytics]

**Reporting**:

[Azure Databricks Spark, Power BI, the Azure portal]

### Solution

- **Landing zone**: Azure Blob storage
- **Transformation zone**: Azure Databricks Spark
- **Serving zone**: Synapse SQL pool
- **Reporting**: Power BI

### Explanation

**Landing zone**:

- Since the input contains a wide variety of data formats, including images and videos, it is better to store them in Azure Blob storage.
- Azure Data Lake Gen2 provides a hierarchical namespace and is usually a good storage choice for data lakes. But since this use case includes images and videos, it is not recommended here.
- Synapse SQL pool is a data warehouse solution that can be used to process data and store it to be used by business intelligence tools such as Power BI.
- Azure Data Factory provides connectors to read data from a huge variety of sources and orchestration support. Hence, it will not be a good fit for this situation.

**Transformation zone**:

- Since the requirement includes cleaning up the incoming data, visualizing the data, and transforming the different formats into a standard schema that can be consumed by reports, Azure Databricks would fit the bill. Azure Databricks also supports Notebooks with Scala and Python support.
- Synapse SQL pool can be used to store the processed data generated by Azure Databricks, but would not be a good fit for Scala and Python support.
- Azure Stream Analytics is used for real-time processing. Hence, it will not work for our use case.

**Serving zone**:

- Synapse SQL pool, being a data warehouse that can support petabytes of data, would be a perfect choice here.
- Azure Data Lake Gen2 provides a hierarchical namespace and is usually a good storage choice for data lake landing zones, but not for the serving zone. Serving zones need to be able to serve the results quickly to BI systems, so usually SQL-based or key-value-based services work the best.
- Azure Stream Analytics is used for real-time data processing. Hence, it will not work for our use case.

**Reporting**:

- Power BI is a graphical business intelligence tool that can help visualize data insights. It provides a rich set of graphs and data filtering, aggregating, and sorting options.
- The Azure portal is the starting page for all Azure services. It is the control center for all services that provides options for creating, deleting, managing, and monitoring the services.

Let's next look at an ASA windowed aggregates question.

ASA windows
-----------

You are working for a credit card company. You have been asked to design a system to detect credit card transaction fraud. One of the scenarios is to check whether a credit card has been used more than 3 times within the last 10 mins. The system is already configured to use Azure Event Hubs and Azure Stream Analytics. You have decided to use the windowed aggregation feature of ASA. Which of the following solutions would work? (Select one or more)

- A - Use a tumbling window with a size of 10 mins and check whether the count for the same credit card > 3.
- B - Use a sliding window with a size of 10 mins and check whether the count for the same credit card > 3.
- C - Use a hopping window with a size of 10 mins and a hop of 3 mins and check whether the count for the same credit card > 3.
- D - Use a session window with a size of 10 mins and check whether the count for the same credit card > 3.

### Solution

**B - Sliding Window**

### Explanation

- A sliding window has a fixed size, but the window moves forward only when events are either added or removed. Otherwise, it won't emit any results. This will work perfectly as the window is of a fixed size and is moving after considering each and every event in progressive windows of 10 mins. This is a typical use case for a sliding window: *For every 10 seconds, alert if an event appears more than 5 times*.
- A tumbling window calculates the number of events in fixed-size non-overlapping windows, so it might miss out on counting the events across window boundaries. Here's a typical use case: *Find the number of events grouped by card number, in 10-second-wide tumbling windows*.
- A hopping window calculates the count of events at every X interval, for the previous Y window width duration. If the overlap window is not big enough, this will also miss counting the events across window boundaries. Here's a typical use case: *Every 10 seconds, fetch the transaction count for the last 20 seconds*.
- Session windows don't have fixed sizes. We need to specify a maximum window size and a timeout duration for session windows. The session window tries to grab as many events as possible within the max window size. Since this is not a fixed-size window, it will not work for our use case. Here's a typical use case: *Find the number of trips that occur within 5 seconds of each other*.

Let's next look at a Spark transformation question.

Spark transformation
--------------------

You work for a cab company that is storing trip data in Parquet format and fare data in CSV format. You are required to generate a report to list all the trips aggregated using the **City** field. The report should contain all fields from both files.

**Trip file format (Parquet)**:

**tripId, driverId, City, StartTime, EndTime**

**Fare file format (CSV)**:

**tripId, Fare**

Fill in the blanks of the following code snippet to achieve the preceding objective:

```python
%%scala
val fromcsv = spark.read.options(Map("inferSchema"->"true","header"->"true"))
.csv("abfss://path/to/csv/*")
val fromparquet = spark.read.options(Map("inferSchema"->"true"))
.parquet("abfss:// abfss://path/to/parquet/*")
val joinDF = fromcsv.________(fromparquet,fromcsv("tripId") === fromparquet("tripId"),"inner")._________("City")
```

[Options: **join**, **orderBy**, **select**, **groupBy**]

### Solution

**Join**, **groupBy**

### Explanation

- **join()** - To join two tables based on the provided conditions
- **groupBy()** - Used to aggregate values based on some column values, such as **City** in this case
- **select()** - To select the data from a subset of columns
- **orderBy()** - To sort the rows by a particular column

Let's next look at an ADF integration runtime-based question.

ADF - integration runtimes
--------------------------

You are working as a data engineer for a tax consulting firm. The firm processes thousands of tax forms for its customers every day. Your firm is growing and has decided to move to the cloud, but they want to be in a hybrid mode as they already have invested in a good set of on-premises servers for data processing. You plan to use ADF to copy data over nightly. Which of the following integration runtimes would you suggest?

- A - Azure integration runtime
- B - Self-Hosted integration runtime
- C - Azure - SSIS integration runtime

### Solution

**B - Self-Hosted Integration Runtime**: Since this is an on-premises to the cloud use case, the self-hosted integration would be ideal. Also, since they have their local compute available, it would become much easier to set up the IR on the local servers.

### Explanation

**Azure Integration Runtime** - This is the default option and supports connecting data stores and compute services across public endpoints. Use this option to copy data between Azure-hosted services.

**Self-Hosted Integration Runtime** - Use the self-hosted IR when you need to copy data between on-premises clusters and Azure services. You will need machines or VMs on the on-premises private network to install a self-hosted integration runtime.

**Azure - SSIS Integration Runtime** - The SSIS IRs are used for **SQL Server Integration Services** (**SSIS**) lift and shift use cases.

Let's next look at a question on ADF triggers.

ADF triggers
------------

Choose the right kind of trigger for your ADF pipelines:

- A - Trigger when a file gets deleted in Azure Blob storage
- B - To handle custom events in Event Grid
- C - Trigger a pipeline every Monday and Wednesday at 9:00 A.M. EST
- D - Trigger a pipeline daily at 9:00 A.M. EST but wait for the previous run to complete

[Options: Storage event trigger, Custom event trigger, Tumbling window trigger, Schedule trigger]

### Solution

- A - Storage event trigger
- B - Custom event trigger
- C - Schedule trigger
- D - Tumbling window trigger

### Explanation

- **Schedule trigger** - These are triggers that get fired on fixed schedules. You specify the start date, recurrence, and end date, and ADF takes care of firing the pipeline at the mentioned date and time.
- **Tumbling window trigger** - These are stateful scheduled triggers that are aware of the previous pipeline runs and offer retry capabilities.
- **Storage event trigger** - These are triggers that get fired on Blob storage events such as creating or deleting a file.
- **Custom trigger** - These are triggers that work on custom events mainly for Event Grid.

Let's next look at a question from the data security section.

TDE/Always Encrypted
--------------------

You have configured active geo-replication on an Azure Synapse SQL instance. You are worried that the data might be accessible from the replicated instances or backup files and need to safeguard it. Which security solution do you configure?

- Enable Always Encrypted
- Enable **Transport Layer Security** (**TLS**)
- Enable **Transparent Data Encryption** (**TDE**)
- Enable row-level security

### Solution

Enable** Transparent Data Encryption** (**TDE**)

### Explanation

- TDE encrypts the complete database, including offline access files such as backup files and log files.
- Always Encrypted is used to encrypt specific columns of database tables, not the complete database or the offline files.
- TLS is for encrypting data in motion. It doesn't deal with encrypting databases.
- Row-level security is for hiding selected rows from non-privileged database users. It doesn't encrypt the database itself.

Let's next look at an Azure SQL/Synapse SQL auditing question.

Auditing Azure SQL/Synapse SQL
------------------------------

You work for a financial institution that stores all transactions in an Azure SQL database. You are required to keep track of all the delete activities on the SQL server. Which of the following activities should you perform? (Select one or more correct options)

- Create alerts using Azure SQL Metrics.
- Enable auditing.
- Configure Log Analytics as the destination for the audit logs.
- Build custom metrics for delete events.

### Solution

- Enable auditing.
- Configure Log Analytics as the destination for the audit logs.

### Explanation

- Enabling auditing will track all the events in the database, including delete activities.
- Configuring the destination as Log Analytics or Storage (Blob) will suffice the requirement to keep track of the activities. Log Analytics provides the advantage of Kusto queries, which can be run to analyze the audit logs. In the case of Blob storage, we will have to write custom code to analyze the audit logs.
- Building custom metrics is not required as the audit function will automatically keep track of all deletions.
- Creating alerts is not required as the requirement is to only keep track of the delete activities, not to alert.

Let's next look at a **Dynamic Data Masking** (**DDM**) question.

Dynamic data masking
--------------------

You need to partially mask the numbers of an SSN column. Only the last four digits should be visible. Which of the following solutions would work?

- A -- **ALTER TABLE [dbo].[Customer] ALTER COLUMN SSN ADD MASKED WITH FUNCTION ='PARTIAL(4, "xxx-xx-", 4)');**
- B -- **ALTER TABLE [dbo].[Customer] ALTER COLUMN SSN ADD MASKED WITH FUNCTION = 'PARTIAL(4, "xxx-xx-", 0)');**
- C -- **ALTER TABLE [dbo].[Customer] ALTER COLUMN SSN ADD MASKED WITH (FUNCTION = 'PARTIAL(0,"xxx-xx-", 4)');**
- D -- **ALTER TABLE [dbo].[Customer] ALTER COLUMN SSN ADD MASKED WITH FUNCTION = 'PARTIAL("xxx-xx-")');**

### Solution

**C** -- **ALTER TABLE [dbo].[Customer] ALTER COLUMN SSN ADD MASKED WITH FUNCTION ='PARTIAL(0, 'xxx-xx-', 4)');**

### Explanation

The syntax for partial masking is **partial(prefix,[padding],suffix)**.

Let's next look at an RBAC-based question.

RBAC - POSIX
------------

Let's assume that you are part of the engineering AAD security group in your company. The sales team has a directory with the following details:

| Container | Owner                    | Permission (POSIX) |
| -------- | ----------------------- | ----------------- |
| /Sales    | Sales AAD security group | 740                |

Will you be able to read the files under the **/Sales** directory?

### Solution

**No**

### Explanation

In POSIX representation, there are numbers to indicate the permissions for **Owner**, **Owner Group**, and **Others**.

In our question, the 740 would expand into:

**Owner**: 7 (Read - 4, Write - 2, Execute - 1. Total: 4+2+1 = 7) // Can Read, Write, and Execute

**Owner Group**: 4 (Read - 4, Write - 0, Execute - 0. Total: 4+0+0 = 4) // Can Read, but not Write or Execute

**Others**: 0 (Read - 0, Write - 0, Execute - 0. Total: 0+0+0 = 0) // Cannot Read, Write, or Execute

So, the answer to the question would be *No*. Since you are part of the engineering security group, you would fall under the **Other** category, which doesn't have any permissions.

Let's next look at a row-level security question.

Row-level security
------------------

You are building a learning management system and you want to ensure that a teacher can see only the students in their class with any **SELECT** queries. Here is the **STUDENT** table:

```sql
CREATE TABLE StudentTable {
  StudentId VARCHAR (20),
  StudentName VARCHAR(40),
  TeacherName sysname,
  Grade VARCHAR (3)
}
```

Fill in the missing sections of the following row-level security script:

1. Step 1:

   CREATE ______ Security.TeacherPredicate (@TeacherName AS sysname)

   RETURNS TABLE

   AS RETURN SELECT 1

   WHERE @TeacherName = USER_NAME()

[Options: **FUNCTION**, **TABLE**, **VIEW**]

1. Step 2:

   CREATE ___________ PrivFilter

   ADD FILTER PREDICATE Security**.TeacherPredicate **(**TeacherName**)

   ON StudentTable WITH (STATE = ON);

[Options: **SECURITY POLICY**, **TABLE**, **VIEW**]

### Solution

- Step 1: **FUNCTION**
- Step 2: **SECURITY POLICY**

### Explanation

- Step 1: You must create a **FUNCTION** that can be applied as a **FILTER PREDICATE**, not a **TABLE** or a **VIEW**.
- Step 2: You must create a **SECURITY POLICY** that can be applied on the table, not a **TABLE** or a **VIEW**.

Let's next look at a few sample questions from the monitoring and optimization section.

Blob storage monitoring
-----------------------

You have been hired as an external consultant to evaluate Azure Blob storage. Your team has been using Blob storage for a month now. You want to find the usage and availability of the Blob storage.

**Question 1**:

You can find the Blob storage usage from the **Storage Metrics** tab.

[Options: Yes/No]

**Question 2**:

You can find the Blob availability metrics from the **Storage Metrics** tab.

[Options: Yes/No]

**Question 3**:

You can find the Blob availability metrics from the **Azure Monitor** -> **Storage Accounts** --> **Insights **tab.

[Options: Yes/No]

### Solution

1. **Question 1**: **Yes**
2. **Question 2**: **No**
3. **Question 3**: **Yes**

### Explanation

You can find the Blob storage usage from the **Metrics** tab on the Storage portal page. But it doesn't have the store availability metrics. To look at the availability, you will have to go to Azure Monitor and click on the **Insights** tab under **Storage accounts**.

T-SQL optimization
------------------

You are running a few T-SQL queries and realize that the queries are taking much longer than before. You want to analyze why the queries are taking longer. Which of the following solutions will work? (Select one or more).

- A - Create a diagnostic setting for Synapse SQL pool to send the **ExecRequests** and **Waits** logs to Log Analytics and analyze the diagnostics table using Kusto to get the details of the running query and the query waits.
- B - Run a T-SQL query against the **sys.dm_pdw_exec_requests** and **sys.dm_pdw_waits** table to get the details of the running query and the query waits.
- C - Go to the Synapse SQL Metrics dashboard and look at the query execution and query wait metrics.

### Solution

**B**

### Explanation

The diagnostic setting for Synapse SQL pool didn't provide the options for **ExecRequests** and **Waits** as of writing this book.

**sys.dm_pdw_exec_requests** - Contains all the current and recently active requests in Azure Synapse Analytics.

**sys.dm_pdw_waits** - Contains details of the wait states in a query, including locks and waits on transmission queues.

The SQL Metrics dashboard doesn't provide the query performance details.

Let's next look at an ADF monitoring question.

ADF monitoring
--------------

There are two sub-questions for this question. Select all the statements that apply.

**Question 1**:

How would you monitor ADF pipeline performance for the last month?

- A - Use the ADF pipeline **activity** dashboard.
- B - Create a diagnostic setting, route the pipeline data to Log Analytics, and use Kusto to analyze the performance data.

[Options: A, B]

**Question 2**:

How would you monitor ADF pipeline performance for the last 3 months?

- A - Use the ADF pipeline **activity** dashboard.
- B - Create a diagnostic setting, route the pipeline data to Log Analytics, and use Kusto to analyze the performance data.

[Options: A, B]

### Solution

**Question 1**:

**A** and **B**

**Question 2**:

**Only A**

### Explanation

The ADF activity dashboard only keeps 45 days of data. Beyond that, we need to use Azure Monitoring and Log Analytics.

Let's next look at an ASA alert-related question.

Setting up alerts in ASA
------------------------

Select the four steps required to set up an alert to fire if SU % goes above 80%. Arrange the steps in the right order:

- A - Configure diagnostic settings.
- B - Define the actions to be done when the alert is triggered.
- C - Select the signal as SU % utilization.
- D - Redirect logs to Log Analytics and use Kusto to check for Threshold > 80%
- E - Select the scope as your Azure Stream Analytics job.
- F - Set the alert logic as **Greater Than** Threshold value **80**%.

### Solution

**E, C, F, B**

### Explanation

The steps involved in setting up an ASA alert for SU % utilization are as follows:

- Select the scope as your Azure Stream Analytics job.
- Select the signal as SU % utilization.
- Set the alert logic as **Greater Than** Threshold value **80**%.
- Define the actions to be done when the alert is triggered.

Diagnostic settings and Log Analytics are not required. The required SU % utilization metric is already available as part of ASA metrics.
