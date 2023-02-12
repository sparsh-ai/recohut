# Azure Data Lakes

Azure Data Lake is a highly scalable and durable object-based cloud storage solution from Microsoft. It is optimized to store large amounts of structured and semi-structured data such as logs, application data, and documents.

Azure Data Lake can be used as a data source and destination in data engineering projects. As a source, it can be used to stage structured or semi-structured data. As a destination, it can be used to store the result of a data pipeline.

Azure Data Lake is provisioned as a storage account in Azure, capable of storing files (blobs), tables, or queues. Azure Blob storage is one of the four storage services available in Azure Storage. The other storage services are  **Table** ,  **Queue** , and  **File Share** . Table storage is used to store non-relational structured data as key-value pairs, queue storage is used to store messages as queues, and file share is used for creating file share directories/mount points that can be accessed using the NFS/SMB protocols.

Azure provides several storage technologies that can cater to a wide range of cloud and hybrid use cases. Some of the important Azure storage technologies includes: Blobs, Files, Queues, Tables, SQL Database, Cosmos DB, Synapse SQL Warehouse, and Azure Data Lake Storage (ADLS). Azure bundles the four fundamental storage technologies, namely:—Blobs, Files, Queues, and Tables—as Azure Storage. Other advanced services such as Cosmos DB, SQL Database, ADLS, and so on are provided as independent Azure services.

## Azure Data Lake Gen 2

**Azure Data Lake Gen2** or **Azure Data Lake Storage Gen 2** ( **ADLS Gen2** ) is a superset []()of Blob storage []()that is optimized for  **big data analytics** . ADLS Gen2 is the preferred option for data []()lake solutions in Azure. It provides hierarchical namespace support on top of Blob storage. Hierarchical namespace support just means that directories are supported. Unlike Blob storage, which provides pseudo directory operations via namespaces, ADLS Gen2 provides real support []()for directories with POSIX compliance and **Access Control List** ( **ACL** ) support. This makes operations such as renaming and deleting directories atomic and quick. For example, if you have 100 files under a directory in Blob storage, renaming that directory would require hundred metadata operations. But, in ADLS Gen2, just one metadata operation will need to be performed at the directory []()level. ADLS Gen2 also supports **role-based access controls** ( **RBACs** ), just like Blob storage does.

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
