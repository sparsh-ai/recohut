# Data Lakes

## Before the cloud data lake architecture

To understand how cloud data lakes help with the growing data needs of an organization, its important for us to first understand how data processing and insights worked a few decades ago. Businesses often thought of data as something that supplemented a business problem that needs to be solved. The approach was business problem centric, and involved the following steps :-

1. Identify the problem to be solved.
2. Define a structure for data that can help solve the problem.
3. Collect or generate the data that adheres with the structure.
4. Store the data in an Online Transaction Processing (OLTP) database, such as SQL Servers.
5. Use another set of transformations (filtering, aggregations etc) to store data in Online Analytics Processing (OLAP) databases, SQL servers are used here as well.
6. Build dashboards and queries from these OLAP databases to solve your business problem.

For instance, when an organization wanted to understand the sales, they built an application for sales people to input their leads, customers, and engagements, along with the sales data, and this application was supported by one or more operational databases.For example, there could be one database storing customer information, another storing employee information for the sales force, and a third database that stored the sales information that referenced both the customer and the employee databases. On-premises (referred to as on-prem) have three layers:

1. Enterprise data warehouse - this is the component where the data is stored. It contains a database component to store the data, and a metadata component to describe the data stored in the database.
2. Data marts - data marts are a segment of the enteprise data warehouse, that contain a business/topic focused databases that have data ready to serve the application. Data in the warehouse goes through another set of transformations to be stored in the data marts.
3. Consumption/BI layer - this consists of the various visualization and query tools that are used by BI analysts to query the data in the data marts (or the warehouse) to generate insights.

![Traditional on-premises data warehouse](https://user-images.githubusercontent.com/62965911/213930653-e195afbb-1d65-4c41-8e47-b73bec31783c.png)

## Limitations of on-premises data warehouse solutions

While this works well for providing insights into the business, there are a few key limitations with this architecture, as listed below.

1. Highly structured data: This architecture expects data to be highly structured every step of the way. As we saw in the examples above, this assumption is not realistic anymore, data can come from any source such as IoT sensors, social media feeds, video/audio files, and can be of any format (JSON, CSV, PNG, fill this list with all the formats you know), and in most cases, a strict structure cannot be enforced.
2. Siloed data stores: There are multiple copies of the same data stored in data stores that are specialized for specific purposes. This proves to be a disadvantage because there is a high cost for storing these multiple copies of the same data, and the process of copying data back and forth is both expensive, error prone, and results in inconsistent versions of data across multiple data stores while the data is being copied.
3. Hardware provisioning for peak utilization: On-premises data warehouses requires organizations to install and maintain the hardware required to run these services. When you expect bursts in demand (think of budget closing for the fiscal year or projecting more sales over the holidays), you need to plan ahead for this peak utilization and buy the hardware, even if it means that some of your hardware needs to be lying around underutilized for the rest of the time. This increases your total cost of ownership. Do note that this is specifically a limitation with respect on on-premises hardware rather than a difference between data warehouse vs data lake architecture.

## What is a Cloud Data Lake Architecture

The big data scenarios go way beyond the confines of the traditional enterprise data warehouses. Cloud data lake architectures are designed to solve these exact problems, since they were designed to meet the needs of explosive growth of data and their sources, without making any assumptions on the source, the formats, the size, or the quality of the data. In contrast to the problem-first approach taken by traditional data warehouses, cloud data lakes take a data-first approach. In a cloud data lake architecture, all data is considered to be useful - either immediately or to meet a future need. And the first step in a cloud data architecture involves ingesting data in their raw, natural state, without any restrictions on the source, the size, or the format of the data. This data is stored in a cloud data lake, a storage system that is highly scalable and can store any kind of data. This raw data has variable quality and value, and needs more transformations to generate high value insights.

![Cloud data lake architecture](https://user-images.githubusercontent.com/62965911/213930623-d2ad377e-d09d-4e44-be4d-7ec534ed5fb2.png)

The processing systems on a cloud data lake work on the data that is stored in the data lake, and allow the data developer to define a schema on demand, i.e. describe the data at the time of processing. These processing systems then operate on the low value unstructured data to generate high value data, that is often structured, and contains meaningful insights. This high value structured data is then either loaded into an enterprise data warehouse for consumption, and can also be consumed directly from the data lake.

Watch this video: https://www.youtube.com/watch?v=zlBZrG8dDMM

## Benefits of a Cloud Data Lake Architecture

At a high level, this cloud data lake architecture addresses the limitations of the traditional data warehouse architectures in the following ways:

- No restrictions on the data - As we saw, a data lake architecture consists of tools that are designed to ingest, store, and process all kinds of data without imposing any restrictions on the source, the size, or the structure of the data. In addition, these systems are designed to work with data that enters the data lake at any speed - real time data emitted continously as well as volumes of data ingested in batches on a scheduled basis. Further, the data lake storage is extremely low cost, so this lets us store all data by default without worrying about the bills. Think about how you would have needed to think twice before taking pictures with those film roll cameras, and these days click away without as much as a second thought with your phone cameras.
- Single storage layer with no silos - Note that in a cloud data lake architecture, your processing happens on data in the same store, where you don’t need specialized data stores for specialized purposes anymore. This not only lowers your cost, but also avoids errors involved in moving data back and forth across different storage systems.
- Flexibility of running diverse compute on the same data store - As you can see, a cloud data lake architecture inherently decouples compute and storage, so while the storage layer serves as a no-silos repository, you can run a variety of data processing computational tools on the same storage layer. As an example, you can leverage the same data storage layer to do data warehouse like business intelligence queries, advanced machine learning and data science computations, or even bespoke domain specific computations such as high performance computing like media processing or analysis of seismic data.
- Pay for what you use - Cloud services and tools are always designed to elastically scale up and scale down on demand, and you can also create and delete processing systems on demand, so this would mean that for those bursts in demand during holiday season or budget closing, you can choose to spin these systems up on demand without having them around for the rest of the year. This drastically reduces the total cost of ownership.
- Independently scale compute and storage - In a cloud data lake architecture, compute and storage are different types of resources, and they can be independently scaled, thereby allowing you to scale your resources depending on need. Storage systems on the cloud are very cheap, and enable you to store a large amount of data without breaking the bank. Compute resources are traditionally more expensive than storage, however, they do have the capability to be started or stopped on demand, thereby offering economy at scale.

NOTE

> Technically, it is possible to scale compute and storage independently in an on-premises Hadoop architecture as well. However, this involves careful consideration of hardware choices that are optimized specifically for compute and storage, and also have an optimized network connectivity. This is exactly what cloud providers offer with their cloud infrastructure services. Very few organizations have this kind of expertise, and explicitly choose to run their services on-premises.

This flexibility in processing all kinds of data in a cost efficient fashion helps organizations realize the value of data and turn them into valuable transformational insights.

## On-premises Hadoop cluster vs Cloud data lakes

![On-premises versus cloud architectures](https://user-images.githubusercontent.com/62965911/213930652-1784028d-8974-46ed-9e7c-4924df84a5c2.png)

## Components of the cloud data lake architecture

There are four key components that create the foundation and serve as building blocks for the cloud data lake architecture. These components are:

1. The data itself - structured, semi-structured and unstructured data
2. The data lake storage - e.g. Amazon S3 (Simple Storage Service), Azure Data Lake Storage (ADLS) and Google Cloud Storage (GCS)
3. The big data analytics engines that process the data - e.g. Apache Hadoop, Apache Spark and Real-time stream processing pipelines
4. The cloud data warehouse - e.g. Amazon RedShift, Google BigQuery, Azure Synapse Analytics and Snowflake Data Platform

![img](https://user-images.githubusercontent.com/62965911/213930629-c3148c37-b5b0-4812-9d3d-122c8ba2bca3.svg)

## When should you use a data lake?

We can consider using data lakes for the following scenarios:

- If you have data that is too big to be stored in structured storage systems like data warehouses or SQL databases
- When you have raw data that needs to be stored for further processing, such as an ETL system or a batch processing system
- Storing continuous data such as **Internet of Things** (**IoT**) data, sensor data, tweets, and so on for low latency, high throughput streaming scenarios
- As the staging zone before uploading the processed data into an SQL database or data warehouse
- Storing videos, audios, binary blob files, log files, and other semi-structured data such as **JavaScript Object Notation** (**JSON**), **Extensible Markup Language** (**XML**), or **YAML Ain't Markup Language** (**YAML**) files for short-term or long-term storage.
- Storing processed data for advanced tasks such as ad hoc querying, **machine learning** (**ML**), data exploration, and so on.

## AWS S3

Watch this video: https://www.youtube.com/watch?v=_abfv7Efr5Q

## Google Cloud Storage (GCS)

**Google Cloud Storage** (**GCS**) is object storage. It's a service that is fully managed by GCP, which means we don't need to think about any underlying infrastructure for GCS. For example, we don't need to think about pre-sizing the storage, the network bandwidth, number of nodes, or any other infrastructure-related stuff.

What is object storage? **Object storage** is a highly scalable data storage architecture that can store very large amounts of data in any format. 

Because the technology can store data in almost any size and format, GCS is often used by developers to store any large files, for example, images, videos, and large CSV data. But, from the data engineering perspective, we will often use GCS for storing files, for example, as dump storage from databases, for exporting historical data from **BigQuery**, for storing machine learning model files, and for any other purpose related to storing files.

## Azure Data Lakes

Azure Data Lake is a highly scalable and durable object-based cloud storage solution from Microsoft. It is optimized to store large amounts of structured and semi-structured data such as logs, application data, and documents.

Azure Data Lake can be used as a data source and destination in data engineering projects. As a source, it can be used to stage structured or semi-structured data. As a destination, it can be used to store the result of a data pipeline.

Azure Data Lake is provisioned as a storage account in Azure, capable of storing files (blobs), tables, or queues. Azure Blob storage is one of the four storage services available in Azure Storage. The other storage services are  **Table** ,  **Queue** , and  **File Share** . Table storage is used to store non-relational structured data as key-value pairs, queue storage is used to store messages as queues, and file share is used for creating file share directories/mount points that can be accessed using the NFS/SMB protocols.

Azure provides several storage technologies that can cater to a wide range of cloud and hybrid use cases. Some of the important Azure storage technologies includes: Blobs, Files, Queues, Tables, SQL Database, Cosmos DB, Synapse SQL Warehouse, and Azure Data Lake Storage (ADLS). Azure bundles the four fundamental storage technologies, namely:—Blobs, Files, Queues, and Tables—as Azure Storage. Other advanced services such as Cosmos DB, SQL Database, ADLS, and so on are provided as independent Azure services.

## Azure Data Lake Gen 2

**Azure Data Lake Gen2** or **Azure Data Lake Storage Gen 2** ( **ADLS Gen2** ) is a superset []()of Blob storage that is optimized for  **big data analytics**. ADLS Gen2 is the preferred option for data []()lake solutions in Azure. It provides hierarchical namespace support on top of Blob storage. Hierarchical namespace support just means that directories are supported. Unlike Blob storage, which provides pseudo directory operations via namespaces, ADLS Gen2 provides real support []()for directories with POSIX compliance and **Access Control List** ( **ACL** ) support. This makes operations such as renaming and deleting directories atomic and quick. For example, if you have 100 files under a directory in Blob storage, renaming that directory would require hundred metadata operations. But, in ADLS Gen2, just one metadata operation will need to be performed at the directory []()level. ADLS Gen2 also supports **role-based access controls** ( **RBACs** ), just like Blob storage does.

Another important feature of ADL Gen2 is that it is a  **Hadoop-compatible filesystem** . So, building any open source analytics pipeline on top of ADL Gen2 is a breeze.

Since we are talking about ADL Gen2, you might be curious to learn about what happened to ADL Gen1.

ADL Gen1, as its name suggests, was the first generation of highly scalable and high-performing data lake storage that was built for data analytics. It is still available but will be deprecated in February 2024. ADLS Gen1 is optimized for large files, so it works best for file sizes of 256 MB and above. The features of Gen1 are available in Gen2 now. Gen2 also has some additional advantages, such as better regional availability, meaning that it is available in all Azure regions, compared to a select few regions where Gen1 is []()available. Gen2 also supports **Locally Redundant Storage** ( **LRS** ), **Zone Redundant Storage** ( **ZRD** ), and **Geo Redundant Storage** (**GRS**) for data redundancy []()and recovery, while Gen1 only supports LRS.

## Data lake architecture

The following image shows a data lake architecture for both batch and stream processing. The diagram also includes examples of the Azure technologies that can be used for each of the data lake zones. The names of the services listed by the icons are presented in the image after this:

![B17525_02_001](https://user-images.githubusercontent.com/62965911/218276767-b43dd30a-03a1-42c9-a09b-be3c3d572fd3.jpeg)

Here are the names of the services represented by the icons in the preceding diagram:

![B17525_02_002](https://user-images.githubusercontent.com/62965911/218276807-570375d0-43d3-43a9-9493-6faa7835cac4.jpeg)

### Various layers in data lake

![511918_1_En_3_Fig1_HTML](https://user-images.githubusercontent.com/62965911/218318221-b4722c92-bdc8-41b1-97fc-d564e50fa6bf.png)

### Zones, Directories, and Files

![511918_1_En_3_Fig5_HTML](https://user-images.githubusercontent.com/62965911/218318356-d6c84b3d-ac10-41b5-8fb9-c741042cec03.png)

## Labs

1. Working with S3 using Boto3 in Python
2. [Building a data lake for a healthcare](02-storage/datalakes/lab-datalake-healthcare-s3-glue-athena/) [company with AWS, S3 and Athena](02-storage/datalakes/lab-datalake-healthcare-s3-glue-athena/)
3. [Creating and Managing Data in Azure Data Lake](02-storage/datalakes/lab-adl-create-manage-data/)
4. [Securing and Monitoring Data in Azure Data Lake](02-storage/datalakes/lab-adl-securing-monitoring-lakes/)
