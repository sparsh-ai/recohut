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

### Who is a data engineer?

A data engineer is a person who is responsible for designing and maintaining data pipelines, data storage systems, and data processing systems. These tasks include data modelling, warehousing, integration, quality management, and security. They also ensure that the data pipelines are efficient and scalable and can handle the volume, velocity and variety of data that the organization is dealing with to ensure that the data is accessible, accurate, and useful for analysis.

Watch these videos:

- https://www.youtube.com/watch?v=m5hLUknIi5c
- https://www.youtube.com/watch?v=h0GhXADnFGI
- https://www.youtube.com/watch?v=rULI2LOuhw4

### Tasks of the data engineer

Data engineers have a key role in a modern data organization. It is a multidisciplinary role, so it needs knowledge of programming, data transformation, and mathematics, among other areas. To support these important activities, there are several open source and cloud tools to help data engineers perform their day-to-day operations.

The following are some examples of tasks that are the responsibility of the data engineer:

- Developing data ingestion pipelines
- Setting connectivity standards in data sources with proper security and latency
- Maintaining data pipelines creating scripts for data structures with versioning control
- Applying modern data exploration languages and libraries to generate insights
- Supporting database administrators in the necessary analytical database maintenance routines
- Modeling and implementing data consumption structures aligned with the business area needs
- Supporting the automation of data analysis processes, model creation, and databases (DataOps)

This is just a short list of the responsibilities of the data engineer. This role is usually very flexible in most organizations, and more specialized in organizations that have more people and greater demand, where there is a need for assembling integration pipelines or data modeling. Now, let's get to know the data engineer tools on Azure.

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

## Data Engineering Challenges

Watch this video: https://www.youtube.com/watch?v=VxZu4B8wIbQ

## Data Flow

Watch this video: https://www.youtube.com/watch?v=bFC1MBijB-c

![img](https://user-images.githubusercontent.com/62965911/213917834-967b67bb-89e6-483a-bbbe-db8cf5ddf36c.svg)

## Key Concepts

1. Data Warehousing: The process of collecting, storing, and managing large sets of data in a central repository for reporting and analysis. Data warehousing allows organizations to store and access large amounts of data in a structured and efficient manner. This enables users to easily query and extract insights from the data, and it also supports the creation of data-driven reports and dashboards.
2. Data Modeling: The process of designing and creating a conceptual representation of data and its relationships, typically using diagrams or other tools. Data modeling is an important step in the data warehousing process, as it helps to ensure that data is stored in a logical and consistent manner. This makes it easier for users to understand and navigate the data, and it also supports the creation of efficient data queries.
3. Data Integration: The process of combining data from different sources into a single, unified view. Data integration is a critical step in the data warehousing process, as it allows organizations to combine data from different systems and sources into a single repository. This enables users to access and analyze data from multiple sources in a single location, and it also supports the creation of data-driven reports and dashboards.
4. Data Pipelines: The process of creating a series of steps to automatically extract, transform, and load data from one system to another. Data pipelines are an essential component of data warehousing and integration, as they automate the process of moving data from one system to another. This reduces the need for manual data entry and improves the accuracy and efficiency of data processing.
5. Data Quality: The process of ensuring that data is accurate, complete, and relevant, and that it meets the needs of the users and systems that rely on it. Data quality is a critical consideration for data engineers, as it helps to ensure that data is usable and valuable for decision making. This includes tasks such as data validation, data cleaning, and data standardization.
6. Data Governance: The process of creating policies and procedures to manage data throughout its lifecycle, including data security and compliance. Data governance is an important consideration for data engineers, as it helps to ensure that data is used and stored in a secure and compliant manner. This includes tasks such as data security, data privacy, and data compliance.
7. Data Processing: The process of applying algorithms and other methods to extract insights and value from data. Data processing is a critical step in the data warehousing process, as it allows organizations to extract insights and value from their data. This includes tasks such as data analysis, data mining, and machine learning.
8. Data Visualization: The process of creating graphical representations of data to help users understand and explore the data. Data visualization is an important step in the data warehousing process, as it allows users to easily explore and understand their data. This includes creating charts, graphs, and other visualizations that make it easy to see patterns and trends in the data.

## Big Data

![Six Vs of big data](https://user-images.githubusercontent.com/62965911/213918079-10af46d9-f906-4c3e-9b84-ddc47708bd15.png)

### Big Data Architectures

#### Lambda

Lambda architecture comprises Batch Layer, Speed Layer (also known as Stream layer), and Serving Layer.

The batch layer operates on the complete data and thus allows the system to produce the most accurate results. However, the results come at the cost of high latency due to high computation time. The batch layer stores the raw data as it arrives and computes the batch views for consumption. Naturally, batch processes will occur at some interval and will be long-lived. The scope of data is anywhere from hours to years.

The speed layer generates results in a low-latency, near real-time fashion. The speed layer is used to compute the real-time views to complement the batch views. The speed layer receives the arriving data and performs incremental updates to the batch layer results. Thanks to the incremental algorithms implemented at the speed layer, the computation cost is significantly reduced.

The batch views may be processed with more complex or expensive rules and may have better data quality and less skew, while the real-time views give you up-to-the-moment access to the latest possible data.

Finally, the serving layer enables various queries of the results sent from the batch and speed layers. The outputs from the batch layer in the form of batch views and the speed layer in the form of near-real-time views are forwarded to the serving layer, which uses this data to cater to the pending queries on an ad-hoc basis.

![](https://user-images.githubusercontent.com/62965911/213918086-32e76d06-a398-40ad-9271-16b9ffc3bb6b.png)

**Pros**

- It is a good balance of speed, reliability, and scalability. The batch layer of Lambda architecture manages historical data with the fault-tolerant, distributed storage, ensuring a low possibility of errors even if the system crashes.
- Access to both real-time and offline results in covering many data analysis scenarios very well.
- Having access to a complete data set in a batch window may yield specific optimizations that make Lambda better performing and perhaps even simpler to implement.

**Cons**

- Although the offline layer and the real-time stream face different scenarios, their internal processing logic is the same, so there are many duplicate modules and coding overhead.
- Reprocesses every batch cycle, which is not beneficial in specific scenarios.
- A data set modeled with Lambda architecture is difficult to migrate or reorganize.

**Use Cases**

- User queries are required to be served on an ad-hoc basis using immutable data storage.
- Quick responses are required, and the system should handle various updates in new data streams.
- None of the stored records shall be erased, and it should allow the addition of updates and new data to the database.

#### Kappa

The Kappa architecture solves the redundant part of the Lambda architecture. It is designed with the idea of replaying data. Kappa architecture avoids maintaining two different code bases for the batch and speed layers. The key idea is to handle real-time data processing, and continuous data reprocessing using a single stream processing engine and avoid a multi-layered Lambda architecture while meeting the standard quality of service.

![](https://user-images.githubusercontent.com/62965911/213918082-56da8775-caee-4db4-b515-7c20ee2bc6bd.png)

**Pros**

- Applications can read and write directly to Kafka (or other message queue) as developed. For existing event sources, listeners are used to stream writes directly from database logs (or datastore equivalents), eliminating the need for batch processing during ingress, resulting in fewer resources.
- Treating every data point in your organization as a streaming event also provides you the ability to 'time travel' to any point and see the state of all data in your organization.
- Queries only need to look in a single serving location instead of going against batch and speed views.

**Cons**

- The complication of this architecture mainly revolves around having to process this data in a stream, such as handling duplicate events, cross-referencing events, or maintaining order - operations that are generally easier to do in batch processing.
- Although the Kappa architecture looks concise, it isn't easy to implement, especially for the data replay.
- For Lambda, catalog services can auto-discover and document file and database systems. Kafka doesn't align with this tooling, so supporting scaling to enterprise-sized environments strongly infers implementing confluent enterprise with a schema registry that attempts to play the role of a catalog service.

**Use Cases**

- When the algorithms applied to the real-time data and the historical data are identical, it is very beneficial to use the same code base to process historical and real-time data and, therefore, implement the use-case using the Kappa architecture.
- Kappa architecture can be used to develop data systems that are online learners and therefore don't need the batch layer.
- The order of the events and queries is not predetermined. Stream processing platforms can interact with the database at any time.

Kappa is not a replacement for Lambda as some use-cases deployed using the Lambda architecture cannot be migrated.

When you seek an architecture that is more reliable in updating the data lake as well as efficient in training the machine learning models to predict upcoming events robustly, then use the Lambda architecture as it reaps the benefits of both the batch layer and speed layer to ensure few errors and speed.

On the other hand, when you want to deploy big data architecture using less expensive hardware and require it to deal effectively with unique events occurring continuously, then select the Kappa architecture for your real-time data processing needs.

Check out [this whitepaper](https://www.qlik.com/us/resource-library/modernizing-your-data-architecture-to-unlock-business-value) and [related webinar](https://videos.qlik.com/watch/mm2p55sd3zvdYHqkzhqRaH?_ga=2.269188596.401343546.1664008674-358725923.1664008674) to deep dive into this topic.
