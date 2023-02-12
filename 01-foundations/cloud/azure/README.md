# Azure Cloud

## Data Ingestion

This is the process of getting all the raw data into the data lake. Data from various sources lands in the raw zone of the data lake. Based on where the data is coming from, such as on-premise systems, other cloud systems, and so on, we could use different ingestion tools. Let's look at some of the options available in Azure:

- **Azure Data Factory** -- It provides data ingestion support from hundreds of data sources, and even from other clouds such as AWS, GCP, Oracle, and so on.
- **Azure Copy** (**AzCopy**) -- This is a command-line tool that can be used to copy data over the internet and is ideally suited for smaller data sizes (preferably in the 10--15 TB range). You can learn more about AzCopy here: [https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10.](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10%0D)
- **Azure ExpressRoute** -- If you need a secure way to transfer data into Azure, then use ExpressRoute. It routes your data through dedicated private connections to Azure instead of the public internet. This is also the preferred option if you want to have a dedicated pipeline with a faster data transfer speed. You can learn more about Azure ExpressRoute here: [https://docs.microsoft.com/en-us/azure/expressroute/expressroute-introduction.](https://docs.microsoft.com/en-us/azure/expressroute/expressroute-introduction%0D)

## Batch Processing

Here is a useful table reproduced from Azure that can help you decide on the technologies to use for your batch scenarios:

![B17525_09_018](https://user-images.githubusercontent.com/62965911/218308595-df31da23-a5d3-483b-88ba-669994a72789.jpeg)

You can learn more about the batch processing choices here: [https://docs.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/batch-processing.](https://docs.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/batch-processing%0D)

## End-to-end Solutions

### Modern Azure Data Architecture Platform

While Microsoft Azure has a vast collection of resources, the most common components within the Modern Enterprise Data and Analytics Platform are listed in following figure. As an Azure Data Engineer, it will be critical to be able to design and implement an end-to-end solution that follows this architectural process or custom variations of it while accounting for security, high availability, and more. It will also be critical to understand the differences and similarities between multiple data storage and data integration options.

![511918_1_En_1_Fig2_HTML](https://user-images.githubusercontent.com/62965911/218317429-4320444d-5cb1-4210-9b9d-a64b1885f624.jpeg)

### High-level diagram of Azure data architecture with DevOps CI/CD

With free online video tutorials, along with Microsoft’s vast knowledge base of documentation that’s easily accessible, understanding the end-to-end architectural process and how it relates to connectivity, security, infrastructure as code, Azure administration, DevOps CI/CD, and billing and cost management will instill confidence in your holistic understanding of Azure as you help your organization and team evangelize Azure Data Engineering and pioneer their journey into the cloud. Figure below presents a diagram with multiple components, along with how it all ties together from an architectural standpoint.

![511918_1_En_1_Fig6_HTML](https://user-images.githubusercontent.com/62965911/218317641-255befa5-893a-419f-a5e2-ace713a682b6.jpeg)

### Data Lake Architecture

The following image shows a data lake architecture for both batch and stream processing. The diagram also includes examples of the Azure technologies that can be used for each of the data lake zones. The names of the services listed by the icons are presented in the image after this:

![B17525_02_001](https://user-images.githubusercontent.com/62965911/218276767-b43dd30a-03a1-42c9-a09b-be3c3d572fd3.jpeg)

Here are the names of the services represented by the icons in the preceding diagram:

![B17525_02_002](https://user-images.githubusercontent.com/62965911/218276807-570375d0-43d3-43a9-9493-6faa7835cac4.jpeg)

### Data Platform Architecture

Data is ingested into the system and persisted in a storage layer. Processing aggregates and reshapes the data to enable analytics and machine learning scenarios. Orchestration and governance are cross-cutting concerns that cover all the components of the platform. Once processed, data is distributed to other downstream systems. All components are tracked by and deployed from source control.

![IFC_F01_Riscutia2](https://user-images.githubusercontent.com/62965911/218319349-07737795-ddcb-4d9c-90c0-444be388cfb3.png)

## Learning Path

The following figure shows Microsoft’s learning path for the Azure Data Engineer, which covers designing and implementing the management, monitoring, security, and privacy of data using Azure data resources.

![511918_1_En_1_Fig4_HTML](https://user-images.githubusercontent.com/62965911/218317540-0307de7b-9f19-4778-86e1-2fa961a0ef51.png)
