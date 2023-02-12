# Data Engineering

![](https://user-images.githubusercontent.com/62965911/213917818-65a2146a-5eb3-4818-861f-5bad0155b8d0.svg)

With the advent of cloud computing, the amount of data generated every moment reached an unprecedented scale. The discipline of data science flourishes in this environment, deriving knowledge and insights from massive amounts of data. As data science becomes critical to business, its processes must be treated with the same rigor as other components of business IT. For example, software engineering teams today embrace DevOps to develop and operate services with 99.99999% availability guarantees. Data engineering brings a similar rigor to data science, so data-centric processes run reliably, smoothly, and in a compliant way.

The goal of data engineering is to make large and complex data accessible for others to interpret. When data — both structured and unstructured — enters a company’s systems, data engineers are the first people to get their hands on it. Data engineering also sees to the creation of data management systems and infrastructure that allows data scientists and analysts to access, process and analyze data with ease. This includes building data lakes, warehouses, and marts and creating data access and retrieval systems. It is a very important component of the data life cycle which enables organizations to effectively collect, manage and use large volumes of data. Data engineering is where software engineering, cloud and DevOps meet.

The Data Engineering Ecosystem includes several different components. It includes disparate data types, formats, and sources of data. Data Pipelines gather data from multiple sources, transform it into analytics-ready data, and make it available to data consumers for analytics and decision-making. Data repositories, such as relational and non-relational databases, data warehouses, data marts, data lakes, and big data stores process and store this data. Data Integration Platforms combine disparate data into a unified view for the data consumers. You will learn about each of these components. You will also learn about Big Data and the use of some of the Big Data processing tools.

## How it works?

![](https://user-images.githubusercontent.com/62965911/213917819-7afbfc9c-b35b-4459-a86c-c28c09f4a429.svg)

A typical Data Engineering lifecycle includes architecting data platforms, designing data stores, and gathering, importing, wrangling, querying, and analyzing data. It also includes performance monitoring and finetuning to ensure systems are performing at optimal levels.

Let's expand it and analyze the complete ecosystem from a wider perspective:

![](https://user-images.githubusercontent.com/62965911/213917792-c61931fb-c440-4ea3-b133-edf8bfbc40e0.gif)

The first type of data engineering is SQL-focused. The work and primary storage of the data is in relational databases. All of the data processing is done with SQL or a SQL-based language. Sometimes, this data processing is done with an ETL tool. The second type of data engineering is Big Data–focused. The work and primary storage of the data is in Big Data technologies like Hadoop, Cassandra, and HBase. All of the data processing is done in Big Data frameworks like MapReduce, Spark, and Flink. While SQL is used, the primary processing is done with programming languages like Java, Scala, and Python.

<iframe width="1440" height="595" src="https://www.youtube.com/embed/qWru-b6m030" title="How Data Engineering Works" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Data engineering is the part of data science that deals with the practical applications of collecting and analyzing data. It aims to bring engineering rigor to the process of building and supporting reliable data systems.

The ML part of data science deals with building a model. In the Netflix scenario, the data model recommends, based on your viewing history, which movies you are likely to enjoy next. The data engineering part of the discipline deals with building a system that continuously gathers and cleans up the viewing history, then runs the model at scale on the data of all users and distributes the results to the recommendation user interface. All of this provided in an automated fashion with monitoring and alerting build around each step of the process.

Data engineering deals with building and operating big data platforms to support all data science scenarios. There are various other terms used for some of these aspects: DataOps refers to moving data in a data system, MLOps refers to running ML at scale as in our Netflix example. (ML combined with DevOps is also known as MLOps.) Our definition of data engineering encompasses all of these and looks at how we can implement DevOps for data science.

## Why Is It Important?

Data engineers are in the business of moving data—either getting it from one location to another or transforming the data in some man‐ ner. It is these hard workers who provide the digital grease that makes a data project a reality.

Internet companies create a lot of data. Datasets are getting larger and messier in he internet era where there are large datasets for all the actions and interactions users make with your website all the way to product descriptions, images, time series info, comments etc.

It is said that data is the new oil. For natural oil, we also need a way to drill and mine this oil for it to be useful. In the same way, we need a way to mine and make sense of all this data to be useful.

On one had, there is a desire by executives and management to get insights from these datasets.

There is also a desire by data scientists and ML practitioners to have clean datasets to model with.

![](https://user-images.githubusercontent.com/62965911/213917822-612d86ce-85f9-4565-8f3c-47405ae57e4c.svg)

There are some really interesting trade-offs to make when you do this. And knowing about these can help you in your own journey as a data scientist or ML person working with large data. Irrespective of where you are in your data journey, I think you will find these interesting.

## Role of a Data Engineer

**Who is a data engineer?**

A data engineer is a person who is responsible for designing and maintaining data pipelines, data storage systems, and data processing systems. These tasks include data modelling, warehousing, integration, quality management, and security. They also ensure that the data pipelines are efficient and scalable and can handle the volume, velocity and variety of data that the organization is dealing with to ensure that the data is accessible, accurate, and useful for analysis.

Watch these videos:

- https://www.youtube.com/watch?v=m5hLUknIi5c
- https://www.youtube.com/watch?v=h0GhXADnFGI
- https://www.youtube.com/watch?v=rULI2LOuhw4

## Data Engineering Challenges

Watch this video: https://www.youtube.com/watch?v=VxZu4B8wIbQ

## Skills You Need to Become a Data Engineer

### SQL

Querying data using SQL is an essential skill for anyone who works with data.

Listed as one of the top technologies on data engineer job listings, SQL is a standardized programming language used to manage relational databases (not exclusively) and perform various operations on the data in them. Data Engineering using Spark SQL.

### Programming Language

As a data engineer you'll be writing a lot of code to handle various business cases such as ETLs, data pipelines, etc. The de facto standard language for data engineering is Python (not to be confused with R or nim that are used for data science, they have no use in data engineering).

Python helps data engineers to build efficient data pipelines as many data engineering tools use Python in the backend. Moreover, various tools in the market are compatible with Python and allow data engineers to integrate them into their everyday tasks by simply learning Python.

### Cloud Computing

Data engineers are expected to be able to process and handle data efficiently. Many companies prefer the cloud solutions to the on-premise ones. Amazon Web Services (AWS) is the world's most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services.

Data engineers need to meet various requirements to build data pipelines. This is where AWS data engineering tools come into the scenario. AWS data engineering tools make it easier for data engineers to build AWS data pipelines, manage data transfer, and ensure efficient data storage.

### Shell Scripting

Unix machines are used everywhere these days and as a data engineer, they are something we interact with every single day. Understanding common shell tools and how to use them to manipulate data will increase your flexibility and speed when dealing with day to day data activities.

### Developer tools - Git, VSCode and Jupyter Notebook

Git is one of the skills that every software engineer needs to manage the code base efficiently. GitHub or any version control software is important for any software development projects, including those which are data driven. GitHub allows version control of your projects through Git.

The VSCode provides rich functionalities, extensions (plugins), built-in Git, ability to run and debug code, and complete customization for the workspace. You can build, test, deploy, and monitor your data engineering applications and pipelines without leaving the application.

Jupyter Notebook is one of the most widely used tool in data engineering that use Python. This is due to the fact, that it is an ideal environment for developing reproducible data pipelines with Python. Colaboratory, or “Colab” for short, is a provide Jupyter-like environment on the cloud.

### Relational and NoSQL Databases

RDBMS are the basic building blocks for any application data. A data engineer should know how to design and architect their structures, and learn about concepts that are related to them.

NoSQL is a term for any non-relational database model: key-value, document, column, graph, and more. A basic acquaintance is required, but going deeper into any model depends on the job. Column databases are a kind of nosql databases. They deserve their own section as they are essential for the data engineer as working with Big Data online (as opposed to offline batching) usually requires a columnar back-end.

### Data Lakes and Warehouses

Understand the concepts behind data warehouses and familiarize youself with common data warehouse solutions. Also make yourself famliar with data lakes and lakehouse concepts like medallion architecture and delta format.

### OLAP Data Modeling

OLAP (analytical) databases (used in data warehouses) data modeling concepts, modeling the data correctly is essential for a functioning data warehouse.

### Batch and Stream Data Processing

Batch Data processing using Python, SQL and Spark. Everyone should know how it works, but going deep into the details and operations are recommended only if necessary.

Stream Data Processing is the data processing on the fly. Suggested to get a good grasp of the subject and then dive deep into a specific tool like Kafka, Spark, Flink, etc.

### Pipeline / Workflow Management

Data engineers should have experience with data pipeline and ETL (extract, transform, load) tools, such as Apache NiFi, Apache Kafka, Apache Airflow, Talend etc. These tools are used to build data pipelines that collect, store, and process data. Airflow is considered to be the defacto standard, but any understanding of DAGs - directed acyclical graphs for tasks will be good.

### Distributed Systems

Data engineers should understand distributed systems, such as how data is stored and processed across multiple machines. This knowledge is essential for designing and implementing big data systems that can handle large amounts of data.

### Soft skills

1. Strong analytical and problem-solving skills: Data engineers should have strong analytical and problem-solving skills, as they are responsible for designing and implementing data pipelines, troubleshooting issues, and ensuring data quality.
2. Understanding of data governance and security: Data engineers should be familiar with the best practices and how to implement them in the data pipeline, such as data encryption, access control, and data masking.
3. Strong communication and collaboration skills: Data engineers often work with cross-functional teams and must be able to communicate effectively with data scientists, analysts, internal and external customers and other stakeholders.

### DevOps Skills

- Infra as Code
- Container Orchestration
- API Management
- CICD Pipelines

### Basic ML/AI Skills

- Machine Learning Basics
- NLP & Computer Vision
- Recommender Systems
- MLOps Pipelines

## Data Flow

Watch this video: https://www.youtube.com/watch?v=bFC1MBijB-c

![img](https://user-images.githubusercontent.com/62965911/213917834-967b67bb-89e6-483a-bbbe-db8cf5ddf36c.svg)
