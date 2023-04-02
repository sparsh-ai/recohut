# Data Engineering Basics

## What is Data Engineering?

There are tons of definitions but you have to stick to one and understand it deeply. Here is one such good definition:

![](https://user-images.githubusercontent.com/62965911/213917818-65a2146a-5eb3-4818-861f-5bad0155b8d0.svg)

Data engineers have a key role in a modern data organization. It is a multidisciplinary role, so it needs knowledge of programming, data transformation, and mathematics, among other areas. To support these important activities, there are several open source and cloud tools to help data engineers perform their day-to-day operations.

The following are some examples of tasks that are the responsibility of the data engineer:

- Developing data ingestion pipelines
- Setting connectivity standards in data sources with proper security and latency
- Maintaining data pipelines creating scripts for data structures with versioning control
- Applying modern data exploration languages and libraries to generate insights
- Supporting database administrators in the necessary analytical database maintenance routines
- Modeling and implementing data consumption structures aligned with the business area needs
- Supporting the automation of data analysis processes, model creation, and databases (DataOps)

## How It Works?

Make sure you watch this short 15-mins video, as it explains a lot of concepts with great examples:

<iframe width="80%" height="280" src="https://www.youtube.com/embed/qWru-b6m030" title="How Data Engineering Works" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Landscape

![](./img/bigpicture.drawio.svg)

> For more info - https://youtu.be/bFC1MBijB-c

## Role of a Data Engineer

![img](https://user-images.githubusercontent.com/62965911/213917822-612d86ce-85f9-4565-8f3c-47405ae57e4c.svg)

- Big Data Engineers design and build complex data pipelines and have expert knowledge in coding using Python, etc. These professionals collaborate and work closely with data scientists to run the code using various tools such as the Hadoop ecosystem, etc.
- Data Architects are typically the database administrators and are responsible for data management. These professionals have in-depth knowledge in databases, and they also help in business operations.
- Business Intelligence Engineers are skilled in data warehousing and create dimension models for loading data for large scale enterprise reporting solutions. These professionals are experts in using ELT tools and SQL.
- Data Warehouse Engineers are responsible for looking after the ETL processes, performance administration, dimensional design, etc. These professionals take care of the full back-end development and dimensional design of the table structure.
- Technical Architects design and define the overall structure of a system with an aim to improve the business of an organization. The job role of these professionals involves breaking large projects into manageable pieces.

## Skills You Need

1. **SQL** - Querying data using SQL is an essential skill for anyone who works with data. Listed as one of the top technologies on data engineer job listings, SQL is a standardized programming language used to manage relational databases (not exclusively) and perform various operations on the data in them. Data Engineering using Spark SQL.
1. **Python Programming** - As a data engineer you'll be writing a lot of code to handle various business cases such as ETLs, data pipelines, etc. The de facto standard language for data engineering is Python (not to be confused with R or nim that are used for data science, they have no use in data engineering). Python helps data engineers to build efficient data pipelines as many data engineering tools use Python in the backend. Moreover, various tools in the market are compatible with Python and allow data engineers to integrate them into their everyday tasks by simply learning Python.
1. **Cloud Computing** - Data engineers are expected to be able to process and handle data efficiently. Many companies prefer the cloud solutions to the on-premise ones. Amazon Web Services (AWS) is the world's most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services. Data engineers need to meet various requirements to build data pipelines. This is where AWS data engineering tools come into the scenario. AWS data engineering tools make it easier for data engineers to build AWS data pipelines, manage data transfer, and ensure efficient data storage.
1. **Shell Scripting** - Unix machines are used everywhere these days and as a data engineer, they are something we interact with every single day. Understanding common shell tools and how to use them to manipulate data will increase your flexibility and speed when dealing with day to day data activities.
1. **Relational and NoSQL Databases** - RDBMS are the basic building blocks for any application data. A data engineer should know how to design and architect their structures, and learn about concepts that are related to them. NoSQL is a term for any non-relational database model: key-value, document, column, graph, and more. A basic acquaintance is required, but going deeper into any model depends on the job. Column databases are a kind of nosql databases. They deserve their own section as they are essential for the data engineer as working with Big Data online (as opposed to offline batching) usually requires a columnar back-end.
1. **Data Lakes and Warehouses** - Understand the concepts behind data warehouses and familiarize youself with common data warehouse solutions. Also make yourself famliar with data lakes and lakehouse concepts like medallion architecture and delta format.
1. **OLAP Data Modeling** - OLAP (analytical) databases (used in data warehouses) data modeling concepts, modeling the data correctly is essential for a functioning data warehouse.
1. **Batch and Stream Data Processing** - Batch Data processing using Python, SQL and Spark. Everyone should know how it works, but going deep into the details and operations are recommended only if necessary. Stream Data Processing is the data processing on the fly. Suggested to get a good grasp of the subject and then dive deep into a specific tool like Kafka, Spark, Flink, etc.
1. **Pipeline / Workflow Management** - Data engineers should have experience with data pipeline and ETL (extract, transform, load) tools, such as Apache NiFi, Apache Kafka, Apache Airflow, Talend etc. These tools are used to build data pipelines that collect, store, and process data. Airflow is considered to be the defacto standard, but any understanding of DAGs - directed acyclical graphs for tasks will be good.
1. **Spark and Distributed Computing** - Data engineers should understand distributed systems, such as how data is stored and processed across multiple machines. This knowledge is essential for designing and implementing big data systems that can handle large amounts of data.

**Soft skills**

1. Strong analytical and problem-solving skills: Data engineers should have strong analytical and problem-solving skills, as they are responsible for designing and implementing data pipelines, troubleshooting issues, and ensuring data quality.
2. Understanding of data governance and security: Data engineers should be familiar with the best practices and how to implement them in the data pipeline, such as data encryption, access control, and data masking.
3. Strong communication and collaboration skills: Data engineers often work with cross-functional teams and must be able to communicate effectively with data scientists, analysts, internal and external customers and other stakeholders.

**Other Skills**

1. Developer tools - Git, VSCode and Jupyter Notebook
1. DevOps - Infra as Code, Container Orchestration, API Management, CICD Pipelines
1. Basic ML/AI Skills - Machine Learning Basics, NLP & Computer Vision, Recommender Systems, MLOps Pipelines

## Key Concepts

1. Data Warehousing: The process of collecting, storing, and managing large sets of data in a central repository for reporting and analysis. Data warehousing allows organizations to store and access large amounts of data in a structured and efficient manner. This enables users to easily query and extract insights from the data, and it also supports the creation of data-driven reports and dashboards.
2. Data Modeling: The process of designing and creating a conceptual representation of data and its relationships, typically using diagrams or other tools. Data modeling is an important step in the data warehousing process, as it helps to ensure that data is stored in a logical and consistent manner. This makes it easier for users to understand and navigate the data, and it also supports the creation of efficient data queries.
3. Data Integration: The process of combining data from different sources into a single, unified view. Data integration is a critical step in the data warehousing process, as it allows organizations to combine data from different systems and sources into a single repository. This enables users to access and analyze data from multiple sources in a single location, and it also supports the creation of data-driven reports and dashboards.
4. Data Pipelines: The process of creating a series of steps to automatically extract, transform, and load data from one system to another. Data pipelines are an essential component of data warehousing and integration, as they automate the process of moving data from one system to another. This reduces the need for manual data entry and improves the accuracy and efficiency of data processing.
5. Data Quality: The process of ensuring that data is accurate, complete, and relevant, and that it meets the needs of the users and systems that rely on it. Data quality is a critical consideration for data engineers, as it helps to ensure that data is usable and valuable for decision making. This includes tasks such as data validation, data cleaning, and data standardization.
6. Data Governance: The process of creating policies and procedures to manage data throughout its lifecycle, including data security and compliance. Data governance is an important consideration for data engineers, as it helps to ensure that data is used and stored in a secure and compliant manner. This includes tasks such as data security, data privacy, and data compliance.
7. Data Processing: The process of applying algorithms and other methods to extract insights and value from data. Data processing is a critical step in the data warehousing process, as it allows organizations to extract insights and value from their data. This includes tasks such as data analysis, data mining, and machine learning.
8. Data Visualization: The process of creating graphical representations of data to help users understand and explore the data. Data visualization is an important step in the data warehousing process, as it allows users to easily explore and understand their data. This includes creating charts, graphs, and other visualizations that make it easy to see patterns and trends in the data.