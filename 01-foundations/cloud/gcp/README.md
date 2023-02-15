# GCP Cloud Essentials

## A quick overview of GCP services for data engineering

As you can see in the GCP Console navigation bar, there are a lot of services in GCP. The services are not only limited to data and analytics. They also cover other areas such as application development, machine learning, networks, source repositories, and many more. As a data engineer working on GCP, you will face situations when you need to decide which services you need to use for your organization.

You might be wondering, who in an organization should decide on the services to use? Is it the CTO, IT manager, solution architect, or data engineers? The answer depends on the experience of using GCP of each of them. But most of the time, data engineers need to be involved in the decision.

So how should we decide? In my experience, there are three important decision factors:

- Choose services that are serverless.
- Understand the mapping between the service and the data engineering areas.
- If there is more than one option in one area, choose the most popular service in the market.

Choosing a serverless service or, to use another common term, a fully managed service, **Software as a Service** (**SaaS**), can also mean choosing services that are the easiest. The easiest in terms of Google manages everything for us, so we can just use the tool.

Now let's discuss these three factors in more detail in the following subsections.

### Understanding the GCP serverless service

In general, there are three groups of services in GCP:

- **VM-based**
- **Managed services**
- **Serverless (fully managed services)**

*VM-based* means you, as a user, use a Google-managed **Virtual Machine** (**VM**) (in GCP, the service is called Compute Engine). You don't need to buy your own machine and install an OS, but you need to install the software yourself. This is still an option because not all software is available in GCP. As an example from my own experience, Google doesn't have a managed service for the Elasticsearch database, so what I need to do is to create VMs in **Google Compute Engine** (**GCE**) and install Elasticsearch on top of the VMs.

*Managed service* means Google manages the software for you. Not only do you not need to install an OS but you don't need to install software dependencies either, or carry out maintenance. For another real example, the first time I used GCP was because I wanted to use Hadoop in the cloud. At the time, I took the VM-based approach. I installed Hadoop from an open source installer on some VMs, until I realized that is not the best practice. The best practice if you want to use Hadoop on GCP is to use **Dataproc**. Using Dataproc, we don't need to install Hadoop ourselves; Google manages it for us. But as a user, I still need to configure the machine size, choose the networks, and other configurations.

A *serverless service* means *simply use it*. You just use the software instantly. You don't need to set up anything to use the software, for example, BigQuery. In BigQuery, we can instantly create tables and trigger SQL queries without configuring anything. But on the other hand, we also have zero visibility of the underlying infrastructure.

The following table shows you the key differences between the three groups and on-premises for comparison:

![B16851_02_14](https://user-images.githubusercontent.com/62965911/219051208-74692035-f817-4014-8bb4-741c6f527fd5.jpeg)

Let's see what **X** and **O** in the preceding table mean:

- (**X**) means: You as a developer don't need to do it. Google manages it for you.
- (**O**) means:  You as a developer need to do it. Google gives you flexibility.

Let's take a look at a practical example. As a GCP data engineer, you are requested to store and process CSV data. The file size is 1 TB and your end user wants to access it in table format using SQL. How do you solve the request? 

For sure you need a big data service to handle this amount of data, and there are three possible scenarios:

**Scenario 1** -- **VM-based**:

1. Provision multiple VM instances in GCP using Compute Engine. Then configure the VM networks, OS, packages, and any infra requirements. 
2. Install the Hadoop cluster on top of the Compute Engine instances. You can choose any Hadoop version that you like.
3. Store data in HDFS and create a hive table on top of the Hadoop cluster.

**Scenario 2** -- **Managed service**:

1. Provision a Hadoop managed service cluster (Dataproc).
2. Store data in HDFS and create a hive table on top of the Hadoop cluster.

**Scenario 3** -- **Fully managed service**:

1. Store data in a BigQuery table, which is a fully managed service for a data warehouse.

Scenario 3 only has one step; it shows you that fully managed service products, in general, are the best choice for simplicity since you can jumpstart directly to the development stage without worrying about setting up the infrastructure and software installation.

What is the drawback? Flexibility. In scenario 1, you can install any software and its version as you like, you have full control of your infrastructure, but you need to take care of its scalability, availability, logging, and other management stuff yourself.

In scenario 2, when using Dataproc, you don't need to create each VM instance manually; Google will set the underlying Hadoop infrastructure for you, but you need to choose the version that is available.

In general, use a fully managed service if one is available and suits your needs. Unless you have issues with compatibility, have specific feature requirements, or the cost doesn't meet your budget, then you may consider scenarios 1 and 2.

### Service mapping and prioritization

So, what products should we focus on first? As described before, there are two aspects that I use to decide what to focus on:

- How close is the service to the core of data engineering?
- The number of adoptions by companies across industries.

To understand service categorization in GCP, let's take a look at the following figure:

![B16851_02_15](https://user-images.githubusercontent.com/62965911/219052914-ed010071-a812-4291-81ef-b40898da926a.jpeg)

*Figure - Big data service mapping and priority*

The GCP services are mapped to their main categories. There are five main categories, and in each category, there are service options that are represented by three different box colors:

- **White**: Priority 1
- **Light gray**: Priority 2
- **Dark gray**: Priority 3

Take your time to check each service in the figure and its priority. The reason we want to use the two aspects to decide on our first focus is we want to make sure we start with the data engineer's main responsibility. 

And on top of that, if there are options in the same category, I would prefer to start with services that have been adopted the most by GCP customers. The reason is, when many GCP customers use services, it gives us confidence that the services are proven both in scalability and maturity. And on top of that, the service will be highly supported by the product team at Google in the long-term future, and this is a very important aspect of choosing products.

If you are wondering why there are so many products, the answer is because each product is meant for specific purposes. Unlike most traditional IT products that tried to provide full stack products as one bundled product, in GCP each service usually has one specific purpose. And as data engineers, we need to combine them together to build solutions.

Now that we know the categorization of each prioritized product from the previous section, we want to quickly look at each product's main position in data engineering.  

### Big data

Here is the list of services under **big data**:

1. **BigQuery**: A fully managed data warehouse service
2. **Dataproc**: A Hadoop-managed service including HDFS, MapReduce, Spark, Presto, and more
3. **Dataflow**: A fully managed distributed processing framework service, very suitable for streaming jobs
4. **Pub/Sub**: A fully managed service messaging system, to publish and subscribe data

### Storage and DB

Here is the list of services under **storage and database**:

1. **Cloud Storage**: A fully managed service for storing large files
2. **Bigtable**: A fully managed NoSQL database service
3. **SQL**: A managed service for application databases, for example, MySQL, PostgreSQL, and SQL Server
4. **Datastore**: A fully managed NoSQL document database service

### ETL orchestrator

Here is the list of services under **ETL orchestrator**:

1. **Cloud Composer**: An Airflow-managed service. Airflow is a Python-based job orchestration tool.
2. **Data Fusion**: A UI-based orchestration tool to run Hadoop jobs on Dataproc.
3. **Dataprep**: A UI-based data wrangling tool. While data wrangling is similar to the ETL process in general, Dataprep has unique features, for example, checking data distribution in histograms and checking missing values. Dataprep is managed by a third party, **Trifacta**, which means that GCP customers need to have separate legal agreements with Trifacta. 

### Identity and management tools

Here is the list of services under **Identity and management tools**:

1. **IAM & Admin**: User and project management for all GCP services
2. **Logging**: A logging system for all GCP services
3. **Monitoring**: A monitoring system with dashboards driven by data from Cloud Logging
4. **Data Catalog**: A metadata system that stores data from GCS, BigQuery, and PubSub

### ML and BI

Here is the list of services under **machine learning and BI tools**:

1. **Vertex AI**: All the tools that you need to build ML and MLOps, for example, notebook, pipeline, model store, and other ML-related services
2. **Looker**: A full-fledged BI tool to visualize data in reports and dashboards
3. **Data Studio**: A simple visualization tool to visualize data

At this point, I have only added very short and simple descriptions for each service. The reason is what is important for now, at this stage, is for us to know the services' positioning. A detailed explanation of each service can be found easily on the internet.
