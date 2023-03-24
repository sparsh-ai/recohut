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

**Amazon S3** is one of the most commonly used cloud data storage services for web applications, and high-performance compute use cases. It is Amazon's object storage service providing virtually unlimited data storage. Some of the advantages of using Amazon S3 include very high scalability, durability, data availability, security, and performance. Amazon S3 can be used for a variety of cloud-native applications, ranging from simple data storage to very large data lakes to web hosting and high-performance applications, such as training very advanced and compute-intensive ML models. Amazon S3 offers several classes of storage options with differences in terms of data access, resiliency, archival needs, and cost. We can choose the storage class that best suits our use case and business needs. There is also an option for cost saving when the access pattern is unknown or changes over time (S3 Intelligent-Tiering).

<iframe width="1440" height="595" src="https://www.youtube.com/embed/_abfv7Efr5Q" title="Understanding why Amazon S3 is the best place to build your data lake - Aws Online Tech Talks" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

#### Key capabilities and features of Amazon S3

In Amazon S3, data is stored as objects in *buckets*. An object is a file and any metadata that describes the file, and buckets are the resources (containers) for the objects. Some of the key capabilities of Amazon S3 are discussed next.

##### Data durability

Amazon S3 is designed to provide very high levels of durability to the data, up to 99.999999999%. This means that the chances of data objects stored in Amazon S3 getting lost are extremely low (average expected loss of approximately 0.000000001% of objects, or 1 out of 10,000 objects every 10 million years). For HPC applications, data durability is of the utmost importance. For example, for training an ML model, data scientists need to carry out various experiments on the same dataset in order to fine-tune the model parameters to get the best performance. If the data storage from which training and validation data is read is not durable for these experiments, then the results of the trained model will not be consistent and hence can lead to incorrect insights, as well as bad inference results. For this reason, Amazon S3 is used in many ML and other data-dependent HPC applications for storing very large amounts of data.

##### Object size

In Amazon S3, we can store objects up to 5 TB in size. This is especially useful for applications that require processing large files, such as videos (for example, high-definition movies or security footage), large logs, or other similar files. Many high-performance compute applications, such as training ML models for a video classification example, require processing thousands of such large files to come up with a model that makes inferences on unseen data well. A deep learning model can read these large files from Amazon S3 one (or more) at a time, store them temporarily on the model training virtual machine, compute and optimize model parameters, and then move on to the next object (file). This way, even machines with smaller disk space and memory can be used to train these computationally intensive models over large data files. Similarly, at the time of model inference, if there is a need to store the data, it can be stored in Amazon S3 for up to 5 TB of object size.

##### Storage classes

Amazon S3 has various storage classes. We can store data in any of these classes and can also move the data across the classes. The right storage class to pick for storing data depends on our data storage, cost, and retention needs. The different S3 storage classes are as follows:

- S3 Standard
- S3 Standard-Infrequent Access
- S3 One Zone-Infrequent Access
- S3 Intelligent-Tiering
- S3 Glacier Instant Retrieval
- S3 Glacier Flexible Retrieval
- S3 Glacier Deep Archive
- S3 Outposts

##### Storage management

Amazon S3 also has various advanced storage management options, such as data replication, prevention of accidental deletion of data, and data version control. Data in Amazon S3 can be replicated into destination buckets in the same or different AWS Regions. This can be done to add redundancy and hence reliability and also improve performance and latency. This is quite important for HPC applications as well since real-time HPC applications that need access to data stored in Amazon S3 will benefit from accessing data from a geographically closer AWS Region. Performance is generally accelerated by up to 60% when datasets are replicated across multiple AWS Regions. Amazon S3 also supports batch operations for data access, enabling various S3 operations to be carried out on billions of objects with a single API call. In addition, lifecycle policies can be configured for objects stored in Amazon S3. Using these policies, S3 objects can be moved automatically to different storage classes depending on access need, resulting in cost optimization.

##### Storage monitoring

Amazon S3 also has several monitoring capabilities. For example, tags can be assigned to S3 buckets, and AWS cost allocation reports can be used to view aggregated usage and cost using these tags. Amazon CloudWatch can also be used to view the health of S3 buckets. In addition, bucket- and object-level activities can also be tracked using AWS CloudTrail.

![S3 storage monitoring and management](https://user-images.githubusercontent.com/62965911/214261108-9900b907-cc1a-4025-91de-130aa505b21e.png)

The preceding figure shows that we can also configure Amazon **Simple Notification Service** (**SNS**) to trigger AWS Lambda to carry out various tasks in the case of certain events, such as new file uploads and so on.

##### Data transfer

For any application built upon large amounts of data and using S3, the data first needs to be transferred to S3. There are various services provided by AWS that work with S3 for different data transfer needs, including hybrid (premises/cloud) storage and online and offline data transfer. For example, if we want to extend our on-premise storage with cloud AWS storage, we can use **AWS Storage Gateway**. Some of the commonly implemented use cases for AWS Storage Gateway are the replacement of tape libraries, cloud storage backend file shares, and low-latency caching of data for on-premise applications.

![Data transfer example using AWS Storage Gateway](https://user-images.githubusercontent.com/62965911/214261360-cf2084ac-c47e-43e9-b5b6-87842da49a96.png)

For use cases requiring online data transfer, AWS DataSync can be used to efficiently transfer hundreds of terabytes into Amazon S3. In addition, AWS Transfer Family can also be used to transfer data to S3 using SFTP, FTPS, and FTP. For offline data transfer use cases, AWS Snow Family has a few options available, including AWS Snowcone, AWS Snowball, and AWS Snowmobile.

##### Performance

One big advantage of S3 for HPC applications is that it supports parallel requests. Each S3 prefix supports 3,500 requests per second to add data and 5,500 requests per second to retrieve data. Prefixes are used to organize data in S3 buckets. These are a sequence of characters at the beginning of an object's key name. We can have as many prefixes as we need in parallel, and each prefix will support this throughput. This way, we can achieve the desired throughput for our application by adding prefixes. In addition, if there is a long geographic separation between the client and the S3 bucket, we can use Amazon S3 Transfer Acceleration to transfer data. Amazon CloudFront is a globally distributed network of edge locations.

Using S3 Transfer Allocation, data is first transferred to an edge location in Amazon CloudFront. From the edge location, an optimized high-bandwidth and low-latency network path is then used to transfer the data to the S3 bucket. Furthermore, data can also be cached in CloudFront edge locations for frequently accessed requests, further optimizing performance. These performance-related features help in improving throughput and reducing latency for data access, especially suited to various HPC applications.

##### Consistency

Data storage requests to Amazon S3 have strong read-after-write consistency. This means that any data written (new or an overwrite) to S3 is available immediately.

##### Analytics

Amazon S3 also has analytics capabilities, including S3 Storage Lens and S3 Storage Class Analysis. S3 Storage Lens can be used to improve storage cost efficiency, as well as to provide best practices for data protection. In addition, it can be used to look into object storage usage and activity trends. It can provide a single view across thousands of accounts in an organization and can generate insights on various levels, such as account, bucket, and prefix. Using S3 Storage Class, we can optimize cost by deciding on when to move data to the right storage class. This information can be used to configure the lifecycle policy to make the data transfer for the S3 bucket. Amazon S3 Inventory is another S3 feature that generates daily or weekly reports, including bucket names, key names, last modification dates, object size, class, replication, encryption status, and a few additional properties.

##### Data security

Amazon S3 has various security measures and features. These features include blocking unauthorized users from accessing data, locking objects to prevent deletions, modifying object ownership for access control, identity and access management, discovery and protection of sensitive data, server-side and client-side encryption, the inspection of an AWS environment, and connection to S3 from on-premise or in the cloud using private IP addresses.

#### Tiered storage for cost optimization: Amazon S3 storage classes

AWS provides options for configuring its data storage services with various different tiers of storage types. This significantly helps with optimizing cost and performance depending on the use case requirements. In this section, we will discuss the tiered storage options for Amazon.

##### Amazon S3 Standard

Amazon S3 Standard is the general-purpose S3 object storage commonly used for frequently accessed data. It provides high throughput and low latency. Some of the common applications of S3 Standard are online gaming, big data analytics, ML model training and data storage, an offline feature store for ML applications, content storage, and distribution, and websites with dynamic content.

##### Amazon S3 Intelligent-Tiering

**Amazon S3 Intelligent-Tiering** is the storage class for unknown, unpredictable, and changing access patterns. There are three access tiers in S3 Intelligent-Tiering -- frequent, infrequent, and archive tiers. S3 Intelligent-Tiering monitors access patterns and moves data to the appropriate tiers accordingly in order to save costs without impacting performance, retrieval fees, or creating operational overhead. In addition, we can also set up S3 Intelligent-Tiering to move data to the Deep Archive Access tier for data that is accessed very rarely (180 days or more). This can result in further additional cost savings.

##### Amazon S3 Standard-Infrequent Access

**Amazon S3 Standard-Infrequent Access** is for use cases where data is generally accessed less frequently, but rapid access may be required. It offers a low per GB storage price and retrieval charge but the same performance and durability as S3 Standard. Some of the common use cases for this tier are backups, a data store for disaster recovery, and long-term storage. For high-performance compute applications, such as ML, this storage tier can be used to store historical data on which models have already been trained or analytics have already been carried out and is not needed for model retraining for a while.

##### Amazon S3 One Zone-Infrequent Access

**Amazon S3 One Zone-Infrequent Access** is very similar to Amazon S3 Standard-Infrequent Access, but the data is stored in only one AZ (multiple devices) instead of the default three AZs within the same AWS Region as for other S3 storage classes. This is even more cost-effective than the S3 Standard-Infrequent Access storage class and is commonly used for storing secondary backups or easily re-creatable data, for example, engineered features no longer used for active ML model training.

##### Amazon S3 Glacier

**Amazon S3 Glacier** storage classes are highly flexible, low-cost, and high-performance data archival storage classes. In Amazon S3 Glacier, there are three storage classes. Amazon S3 Glacier Instant Retrieval is generally used where data is accessed very rarely, but the retrieval is required with latency in milliseconds, for example, news media assets and genomics data. Amazon S3 Flexible Retrieval is for use cases where large datasets such as backup recovery data need to be retrieved at no additional cost, but instant retrieval is not a requirement. The usual retrieval times for such use cases are a few minutes to a few hours. Amazon S3 Glacier Deep Archive is for use cases that require very infrequent retrieval, such as preserved digital media and compliance archives, for example. It is the lowest-cost storage of all the options discussed previously, and the typical retrieval time is 12 hours to 2 days.

##### S3 on Outposts

For on-premise AWS Outposts environments, object storage can be configured using **Amazon S3 on Outposts**. It stores data reliably and redundantly across multiple devices and servers on AWS Outposts, especially suited for use cases with local data residency requirements.

## <a href="#/" target="_blank">Lab: Learn S3 Commands ⤻</a>

1. Learn AWS CLI S3 essential commands
2. Copy and Sync data to/from S3 with AWS CLI

Documentation - https://docs.aws.amazon.com/cli/latest/reference/s3/

```bash
# s3 make bucket (create bucket)
aws s3 mb s3://tgsbucket --region us-west-2

# s3 remove bucket
aws s3 rb s3://tgsbucket
aws s3 rb s3://tgsbucket --force

# s3 ls commands
aws s3 ls
aws s3 ls s3://tgsbucket
aws s3 ls s3://tgsbucket --recursive
aws s3 ls s3://tgsbucket --recursive  --human-readable --summarize

# s3 cp commands
aws s3 cp getdata.php s3://tgsbucket
aws s3 cp /local/dir/data s3://tgsbucket --recursive
aws s3 cp s3://tgsbucket/getdata.php /local/dir/data
aws s3 cp s3://tgsbucket/ /local/dir/data --recursive
aws s3 cp s3://tgsbucket/init.xml s3://backup-bucket
aws s3 cp s3://tgsbucket s3://backup-bucket --recursive

# s3 mv commands
aws s3 mv source.json s3://tgsbucket
aws s3 mv s3://tgsbucket/getdata.php /home/project
aws s3 mv s3://tgsbucket/source.json s3://backup-bucket
aws s3 mv /local/dir/data s3://tgsbucket/data --recursive
aws s3 mv s3://tgsbucket s3://backup-bucket --recursive

# s3 rm commands
aws s3 rm s3://tgsbucket/queries.txt
aws s3 rm s3://tgsbucket --recursive

# s3 sync commands
aws s3 sync backup s3://tgsbucket
aws s3 sync s3://tgsbucket/backup /tmp/backup
aws s3 sync s3://tgsbucket s3://backup-bucket
```

**Create a bucket named `de-first`**

```sh
aws s3api create-bucket --bucket de-first
```

**List all the buckets**

```sh
aws s3 ls
```

**List the content of a bucket named `de-first`**

```sh
aws s3 ls s3://de-first/
```

**Copy a local file `/Files/sample.txt` to the bucket `de-first`**

```sh
aws s3 cp /Files/sample.txt s3://de-first/sample.txt
```

**Sync all files of a folder `/Files` to the bucket's `datafiles` folder**

```sh
aws s3 sync /Files s3://de-first/datafiles
```

**To copy all JSON Reference data to same location**

```sh
aws s3 cp . s3://de-first/data/ --recursive --exclude "*" --include "*.json"
```

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
