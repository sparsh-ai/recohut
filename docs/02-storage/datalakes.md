# Data Lakes

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

## When should you use a data lake?

We can consider using data lakes for the following scenarios:

- If you have data that is too big to be stored in structured storage systems like data warehouses or SQL databases
- When you have raw data that needs to be stored for further processing, such as an ETL system or a batch processing system
- Storing continuous data such as **Internet of Things** (**IoT**) data, sensor data, tweets, and so on for low latency, high throughput streaming scenarios
- As the staging zone before uploading the processed data into an SQL database or data warehouse
- Storing videos, audios, binary blob files, log files, and other semi-structured data such as **JavaScript Object Notation** (**JSON**), **Extensible Markup Language** (**XML**), or **YAML Ain't Markup Language** (**YAML**) files for short-term or long-term storage.
- Storing processed data for advanced tasks such as ad hoc querying, **machine learning** (**ML**), data exploration, and so on.