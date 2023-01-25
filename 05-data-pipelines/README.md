# Data Pipelines

## Steps

1. [Airflow](./airflow/)
1. [Cloud Data Fusion](./datafusion/)
1. [Prefect](./prefect/)
1. [Nifi](./nifi/)
1. [Step Functions](./stepfunctions/)

## Note

### What is a Data Pipeline?

A data pipeline is a means of moving data from one place (the source) to a destination (such as a data warehouse). Along the way, data is transformed and optimized, arriving in a state that can be analyzed and used to develop business insights.

A data pipeline essentially is the steps involved in aggregating, organizing, and moving data. Modern data pipelines automate many of the manual steps involved in transforming and optimizing continuous data loads. Typically, this includes loading raw data into a staging table for interim storage and then changing it before ultimately inserting it into the destination reporting tables.

Collecting and restructuring data from online transaction processing systems is often a multistep process. Some common patterns in data warehousing pipelines are as follows:

- Extraction, transformation, and load (ETL)
- Extraction, load, and transformation (ELT)
- Extraction and load
- Change data capture

These are often batch processing pipelines, but they can have some characteristics of streaming pipelines, especially in the case of change data capture.

### Benefits of a Data Pipeline

Your organization likely deals with massive amounts of data. To analyze all of that data, you need a single view of the entire data set. When that data resides in multiple systems and services, it needs to be combined in ways that make sense for in-depth analysis. Data flow itself can be unreliable: there are many points during the transport from one system to another where corruption or bottlenecks can occur. As the breadth and scope of the role data plays increases, the problems only get magnified in scale and impact.

That is why data pipelines are critical. They eliminate most manual steps from the process and enable a smooth, automated flow of data from one stage to another. They are essential for real-time analytics to help you make faster, data-driven decisions. They’re important if your organization:

- Relies on real-time data analysis
- Stores data in the cloud
- Houses data in multiple sources

By consolidating data from your various silos into one single source of truth, you are ensuring consistent data quality and enabling quick data analysis for business insights.

### Elements

Data pipelines consist of three essential elements: a source or sources, processing steps, and a destination.

1. Sources - Sources are where data comes from. Common sources include relational database management systems like MySQL, CRMs such as Salesforce and HubSpot, ERPs like SAP and Oracle, social media management tools, and even IoT device sensors.

2. Processing steps - In general, data is extracted data from sources, manipulated and changed according to business needs, and then deposited it at its destination. Common processing steps include transformation, augmentation, filtering, grouping, and aggregation.

3. Destination - A destination is where the data arrives at the end of its processing, typically a data lake or data warehouse for analysis.

### How a Typical Data Engineering Pipeline Looks

This is one example of a standard data pipeline in AWS ecosystem:

![data_engg_aws drawio](https://user-images.githubusercontent.com/62965911/214554162-a925ff70-7e4c-4d42-9f29-ad3bd9678431.svg)

![data_engg_aws_notes drawio](https://user-images.githubusercontent.com/62965911/214554158-ccc7a4d5-8164-465f-a3a3-39999615ac5c.svg)

### Data Pipeline vs ETL

Extract, transform, and load (ETL) systems are a kind of data pipeline in that they move data from a source, transform the data, and then load the data into a destination. But ETL is usually just a sub-process. Depending on the nature of the pipeline, ETL may be automated or may not be included at all. On the other hand, a data pipeline is broader in that it is the entire process involved in transporting data from one location to another.

### Characteristics of a Data Pipeline

Only robust end-to-end data pipelines can properly equip you to source, collect, manage, analyze, and effectively use data so you can generate new market opportunities and deliver cost-saving business processes. Modern data pipelines make extracting information from the data you collect fast and efficient.

Characteristics to look for when considering a data pipeline include:

- Continuous and extensible data processing
- The elasticity and agility of the cloud
- Isolated and independent resources for data processing
- Democratized data access and self-service management
- High availability and disaster recovery

### In the Cloud

Modern data pipelines can provide many benefits to your business, including easier access to insights and information, speedier decision-making, and the flexibility and agility to handle peak demand. Modern, cloud-based data pipelines can leverage instant elasticity at a far lower price point than traditional solutions. Like an assembly line for data, it is a powerful engine that sends data through various filters, apps, and APIs, ultimately depositing it at its final destination in a usable state. They offer agile provisioning when demand spikes, eliminate access barriers to shared data, and enable quick deployment across the entire business.

### Build Production-ready Pipelines

Watch this video: https://www.youtube.com/watch?v=CSkQbo-vIA4

### EL, ELT, ETL

Watch this video: https://www.youtube.com/watch?v=bFC1MBijB-c

## Explore further

Watch this video: https://www.youtube.com/watch?v=Hv1XiSsouU8

Watch this video: https://www.youtube.com/watch?v=VtzvF17ysbc