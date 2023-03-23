# Cloud

## What is Cloud Computing?

Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing. Instead of buying, owning, and maintaining physical data centers and servers, you can access technology services, such as computing power, storage, and databases, on an as-needed basis from a cloud provider like Amazon Web Services (AWS).

<iframe width="100%" height="480" src="https://www.youtube.com/embed/mxT233EdY5c" title="What is Cloud Computing? | Amazon Web Services" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**The evolution of the generations**:

- Gen 1: On-Premises and Traditional IT Ops
- Gen 2: Hybrid cloud, infrastructure (VM) focused
- Gen 3: Cloud first, agile operations
- Gen 4: Cloud native, born in cloud

Organizations of every type, size, and industry are using the cloud for a wide variety of use cases, such as data backup, disaster recovery, email, virtual desktops, software development and testing, big data analytics, and customer-facing web applications. For example, healthcare companies are using the cloud to develop more personalized treatments for patients. Financial services companies are using the cloud to power real-time fraud detection and prevention. And video game makers are using the cloud to deliver online games to millions of players around the world.

## Benefits of cloud computing

#### Agility

The cloud gives you easy access to a broad range of technologies so that you can innovate faster and build nearly anything that you can imagine. You can quickly spin up resources as you need them–from infrastructure services, such as compute, storage, and databases, to Internet of Things, machine learning, data lakes and analytics, and much more.

You can deploy technology services in a matter of minutes, and get from idea to implementation several orders of magnitude faster than before. This gives you the freedom to experiment, test new ideas to differentiate customer experiences, and transform your business.

Cloud providers are constantly innovating and adding new services and technologies to their offerings depending on what they learn from multiple customers. Leveraging state-of-the-art services and technologies helps you innovate faster for your business scenarios, compared with having in-house developers who might not have the necessary breadth of knowledge across the industry.

#### Elasticity

With cloud computing, you don’t have to over-provision resources up front to handle peak levels of business activity in the future. Instead, you provision the amount of resources that you actually need. You can scale these resources up or down to instantly grow and shrink capacity as your business needs change.

The resources that you need for your business are highly dynamic in nature, and there are times when you need to provision resources for planned and unplanned increases in usage. When you maintain and run your hardware, you are tied to the hardware you have as the ceiling for the growth you can support in your business. Cloud resources have an elastic scale, and you can burst into high demand by leveraging additional resources in a few clicks.

#### Cost savings

The cloud allows you to trade fixed expenses (such as data centers and physical servers) for variable expenses, and only pay for IT as you consume it. Plus, the variable expenses are much lower than what you would pay to do it yourself because of the economies of scale.

#### Lowered TCO

TCO refers to the total cost of ownership of the technical solution you maintain, including the datacenter costs, the software costs, and the salaries of people who need to be employed to manage the operations. In almost all cases, barring a few exceptions, the TCO is significantly lower for building solutions on the cloud compared with the solutions that are built in house and deployed in your on-premises datacenter. This is because you can focus on hiring software teams to write code for your business logic while the cloud providers take care of all other hardware and software needs for you. Some of the contributors to this lowered cost include the following:

**Cost of hardware**

The cloud providers own, build, and support the hardware resources at a lower cost than if you were to build and run your own datacenters, maintain hardware, and renew your hardware when the support runs out. Further, with the advances made in hardware, cloud providers enable newer hardware to be accessible much faster than if you were to build your own datacenters.

**Cost of software**

In addition to building and maintaining hardware, one of the key efforts for an IT organization is to support and deploy operating systems and keep them updated. Typically, these updates involve planned downtimes that can also be disruptive to your organization. The cloud providers take care of this cycle without burdening your IT department. In almost all cases, these updates happen in an abstracted fashion so that you don’t need to be affected by any downtime.

**Pay for what you use**

Most of the cloud services work on a subscription-based billing model, which means that you pay for what you use. If you have resources that are used for certain hours of the day or certain days of the week, you only pay for that time, which is a lot less expensive than having hardware all the time even if you don’t use it.

#### Deploy globally in minutes

With the cloud, you can expand to new geographic regions and deploy globally in minutes. For example, AWS has infrastructure all over the world, so you can deploy your application in multiple physical locations with just a few clicks. Putting applications in closer proximity to end users reduces latency and improves their experience.

## Types of cloud computing

The three main types of cloud computing include Infrastructure as a Service, Platform as a Service, and Software as a Service. Each type of cloud computing provides different levels of control, flexibility, and management so that you can select the right set of services for your needs.

#### Infrastructure as a Service (IaaS)

IaaS contains the basic building blocks for cloud IT. It typically provides access to networking features, computers (virtual or on dedicated hardware), and data storage space. IaaS gives you the highest level of flexibility and management control over your IT resources. It is most similar to the existing IT resources with which many IT departments and developers are familiar.

#### Platform as a Service (PaaS)

PaaS removes the need for you to manage underlying infrastructure (usually hardware and operating systems), and allows you to focus on the deployment and management of your applications. This helps you be more efficient as you don’t need to worry about resource procurement, capacity planning, software maintenance, patching, or any of the other undifferentiated heavy lifting involved in running your application.

#### Software as a Service (SaaS)

SaaS provides you with a complete product that is run and managed by the service provider. In most cases, people referring to SaaS are referring to end-user applications (such as web-based email). With a SaaS offering, you don’t have to think about how the service is maintained or how the underlying infrastructure is managed. You only need to think about how you will use that particular software.

## Comparison of Cloud Services

<html>
<table>
<thead>
  <tr>
    <th>Service</th>
    <th>Amazon Web Services (AWS)</th>
    <th>Microsoft Azure</th>
    <th>Google Cloud Platform (GCP)</th>
  </tr>
</thead>
<tbody>
  <tr>
      <td colspan='4'><center><b>Servers and Containers</b></center></td>
  </tr>
  <tr>
    <td>Virtual Servers</td>
    <td>Elastic Cloud Compute</td>
    <td>Virtual Machines</td>
    <td>Google Compute Engine</td>
  </tr>
  <tr>
    <td>Serverless Computing</td>
    <td>Lambda</td>
    <td>Azure Functions</td>
    <td>Cloud Functions</td>
  </tr>
  <tr>
    <td>Kubernetes Management</td>
    <td>Elastic Kubernetes Service</td>
    <td>Kubernetes Service</td>
    <td>Kubernetes Engine</td>
  </tr>
  <tr>
    <td colspan='4'><center><b>Data Storage</b></center></td>
  </tr>
  <tr>
    <td>Object Storage</td>
    <td>Simple Storage Service</td>
    <td>Azure Blob</td>
    <td>Cloud Storage</td>
  </tr>
  <tr>
    <td>File Storage</td>
    <td>Elastic File Storage</td>
    <td>Azure Files</td>
    <td>Filestore</td>
  </tr>
  <tr>
    <td>Block Storage</td>
    <td>Elastic Block Storage</td>
    <td>Azure Disk</td>
    <td>Persistent Disk</td>
  </tr>
  <tr>
    <td>Relational Database</td>
    <td>Relational Database Service</td>
    <td>SQL Database</td>
    <td>Cloud SQL</td>
  </tr>
  <tr>
    <td>NoSQL Database</td>
    <td>DynamoDB</td>
    <td>Cosmos DB</td>
    <td>Firestore</td>
  </tr>
  <tr>
    <td colspan='4'><center><b>Network</b></center></td>
  </tr>
  <tr>
    <td>Virtual Network</td>
    <td>Virtual Private Cloud</td>
    <td>Azure VNet</td>
    <td>Virtual Private Network</td>
  </tr>
  <tr>
    <td>Content Delivery Network</td>
    <td>CloudFront</td>
    <td>Azure CDN</td>
    <td>Cloud CDN</td>
  </tr>
  <tr>
    <td>DNS Service</td>
    <td>Route 53</td>
    <td>Traffic Manager</td>
    <td>Cloud DNS</td>
  </tr>
  <tr>
    <td colspan='4'><center><b>Security and Authorization</b></center></td>
  </tr>
  <tr>
    <td>Authentication and Authorization</td>
    <td>IAM</td>
    <td>Azure Active Directory</td>
    <td>Cloud IAM</td>
  </tr>
  <tr>
    <td>Key Management</td>
    <td>KMS</td>
    <td>Azure Key Vault</td>
    <td>KMS</td>
  </tr>
  <tr>
    <td>Network Security</td>
    <td>AWS WAF</td>
    <td>Application Gateway</td>
    <td>Cloud Armor</td>
  </tr>
</tbody>
</table>
</html>

![cloud](https://user-images.githubusercontent.com/62965911/221352820-d1b634a7-ddd2-4976-bc2c-2c8cb4ad19e6.png)

## Amazon Web Services (AWS)

### EC2

The foundational service that provides compute resources for customers to build their applications on AWS is called Amazon EC2. Amazon EC2 provides customers with a choice of 500+ instance types. Customers can then tailor the right combination of instance types for their business applications.

Amazon EC2 provides five types of instances:

- General purpose instances
- Compute optimized instances
- Accelerated computing instances
- Memory optimized instances
- Storage optimized instances

Each of the instance types listed here is actually a family of instances, as shown in figure below:

![](https://user-images.githubusercontent.com/62965911/214259507-9afe5ab4-fc44-4d11-a6d9-6a1ca44e5688.png)

### IAM

> Securely manage identities and access to AWS services and resources

With AWS Identity and Access Management (IAM), you can specify who or what can access services and resources in AWS, centrally manage fine-grained permissions, and analyze access to refine permissions across AWS.

### Glue

[AWS Glue](https://aws.amazon.com/glue/) is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development. AWS Glue provides all the capabilities needed for data integration so that you can start analyzing your data and put it to use in minutes instead of months.

![key_capabilities](https://user-images.githubusercontent.com/62965911/214893307-67708ea2-5f96-4332-9c30-907a6cdfda78.png)

#### Glue Crawler

AWS Glue crawler connects to a data store, progresses through a prioritized list of classifiers to extract the schema of your data and other statistics, and then populates the Glue Data Catalog with this metadata. Crawlers can run periodically to detect the availability of new data as well as changes to existing data, including table definition changes. Crawlers automatically add new tables, new partitions to existing tables, and new versions of table definitions. You can customize Glue crawlers to classify your own file types.

When you define a crawler, you choose one or more classifiers that evaluate the format of your data to infer a schema. When the crawler runs, the first classifier in your list to successfully recognize your data store is used to create a schema for your table. You can use built-in classifiers or define your own. You define your custom classifiers in a separate operation, before you define the crawlers. AWS Glue provides built-in classifiers to infer schemas from common files with formats that include JSON, CSV, and Apache Avro.

#### Glue Data Catalog

The AWS Glue Data Catalog is a central repository to store structural and operational metadata for all your data assets. For a given data set, you can store its table definition, physical location, add business relevant attributes, as well as track how this data has changed over time. AWS Glue provides a number of ways to populate metadata into the AWS Glue Data Catalog. AWS Glue Data Catalog is Apache Hive Metastore compatible. You can point to the Glue Data Catalog endpoint and use it as an Apache Hive Metastore replacement. The metadata stored in the AWS Glue Data Catalog can be readily accessed from Glue ETL, Amazon Athena, Amazon EMR, Amazon Redshift Spectrum, and third-party services.

![awsglue](https://user-images.githubusercontent.com/62965911/217855503-54966554-7971-4d11-bac8-c601047291d9.png)

#### Glue Studio

AWS Glue Studio is a new graphical interface that makes it easy to create, run, and monitor extract, transform, and load (ETL) jobs in AWS Glue. You can visually compose data transformation workflows and seamlessly run them on AWS Glue’s Apache Spark-based serverless ETL engine. You can inspect the schema and data results in each step of the job.

AWS Glue Studio is designed not only for tabular data, but also for semi-structured data, which is difficult to render in spreadsheet-like data preparation interfaces. Examples of semi-structured data include application logs, mobile events, Internet of Things (IoT) event streams, and social feeds.

When creating a job in AWS Glue Studio, you can choose from a variety of data sources that are stored in AWS services. You can quickly prepare that data for analysis in data warehouses and data lakes. AWS Glue Studio also offers tools to monitor ETL workflows and validate that they are operating as intended. You can preview the dataset for each node. This helps you to debug your ETL jobs by displaying a sample of the data at each step of the job.

AWS Glue Studio provides a visual interface that makes it easy to:

- Pull data from an Amazon S3, Amazon Kinesis, or JDBC source.
- Configure a transformation that joins, samples, or transforms the data.
- Specify a target location for the transformed data.
- View the schema or a sample of the dataset at each point in the job.
- Run, monitor, and manage the jobs created in AWS Glue Studio.

#### Glue Studio Notebook

AWS Glue Studio Job Notebooks allows you to interactively author extract-transform-and-load (ETL) jobs in a notebook interface based on Jupyter Notebooks. AWS Glue Studio Job Notebooks requires minimal setup so developers can get started quickly, and feature one-click conversion of notebooks into AWS Glue data integration jobs. Notebooks also support live data integration, fast startup times, and built-in cost management.

#### Glue ETL job

An AWS Glue job encapsulates a script that connects to your source data, processes it, and then writes it out to your data target. Typically, a job runs extract, transform, and load (ETL) scripts. Jobs can also run general-purpose Python scripts (Python shell jobs.) AWS Glue triggers can start jobs based on a schedule or event, or on demand. You can monitor job runs to understand runtime metrics such as completion status, duration, and start time.

You can use scripts that AWS Glue generates, or you can provide your own. Given a source schema and target location or schema, the AWS Glue code generator can automatically create an Apache Spark API (PySpark) script. You can use this script as a starting point and edit it to meet your needs.

#### Monitoring with Glue Studio

The Glue Studio Monitor dashboard provides an overall summary of the job runs, with totals for the jobs with a status of Running, Canceled, Success, or Failed. Additional tiles provide the overall job run success rate, the estimated DPU usage for jobs, a breakdown of the job status counts by job type, worker type, and by day.

#### Glue interactive sessions

With AWS Glue interactive sessions, you can rapidly build, test, and run data preparation and analytics applications. Interactive Sessions provides a programmatic and visual interface for building and testing extract, transform, and load (ETL) scripts for data preparation. Interactive sessions run Apache Spark analytics applications and provide on-demand access to a remote Spark runtime environment. AWS Glue transparently manages serverless Spark for these interactive sessions.

Unlike AWS Glue development endpoints, AWS Glue interactive sessions are serverless with no infrastructure to manage. You can start interactive sessions very quickly. Interactive sessions have a 1-minute billing minimum with cost-control features. This reduces the cost of developing data preparation applications.

Because interactive sessions are flexible, you can build and test applications from the environment of your choice. You can create and work with interactive sessions through the AWS Command Line Interface and the API. You can use Jupyter-compatible notebooks to visually author and test your notebook scripts. Interactive sessions provide an open-source Jupyter kernel that integrates almost anywhere that Jupyter does, including integrating with IDEs such as PyCharm, IntelliJ, and VS Code. This enables you to author code in your local environment and run it seamlessly on the interactive sessions backend.

Using the Interactive Sessions API, customers can programmatically run applications that use Apache Spark analytics without having to manage Spark infrastructure. You can run one or more Spark statements within a single interactive session.

Interactive sessions therefore provide a faster, cheaper, more-flexible way to build and run data preparation and analytics applications.

**Note**
AWS Glue provides multiple options to develop and test Spark code. Data engineers and data scientists can use tools of their choice to author Glue ETL scripts before deploying them to production. Data scientists can continue to work with Sagemaker notebooks connected to Glue Dev Endpoint, others can use Glue Job Notebooks to quickly launch and use jupyter-based fully-managed notebooks directly in browser. If you prefer to work locally, you can use Glue interactive sessions.

#### Glue Workflows

In AWS Glue, you can use workflows to create and visualize complex extract, transform, and load (ETL) activities involving multiple crawlers, jobs, and triggers. Each workflow manages the execution and monitoring of all its components. As a workflow runs each component, it records execution progress and status, providing you with an overview of the larger task and the details of each step. The AWS Glue console provides a visual representation of a workflow as a graph.

#### Glue Trigger

AWS Glue manages dependencies between two or more jobs or dependencies on external events using triggers. Triggers can watch one or more jobs as well as invoke one or more jobs. You can have a scheduled trigger that invokes jobs periodically, an on-demand trigger, or a job completion trigger. Multiple jobs can be triggered in parallel or sequentially by triggering them on a job completion event. You can also trigger one or more Glue jobs from an external source such as an AWS Lambda function.

#### Glue Streaming Job

You can create Glue Streaming extract, transform, and load (ETL) jobs that run continuously, consume data from streaming sources like Amazon Kinesis Data Streams, Apache Kafka, and Amazon Managed Streaming for Apache Kafka (Amazon MSK). The jobs cleanse and transform the data, and then load the results into Amazon S3 data lakes or JDBC data stores. Glue streaming is built based on Spark streaming which is micro-batch oriented and inherits all features of Spark Streaming. Spark Streaming seamlessly integrates with other Spark components like MLlib and Spark SQL. It is different from other systems that either have a processing engine designed only for streaming, or have similar batch and streaming APIs but compile internally to different engines. Spark’s single execution engine and unified programming model for batch and streaming data leads to some unique benefits over other traditional streaming systems.

#### Glue Databrew

AWS Glue DataBrew is a visual data preparation tool that makes it easy for data analysts and data scientists to prepare data with an interactive, point-and-click visual interface without writing code. With Glue DataBrew, you can easily visualize, clean, and normalize terabytes, and even petabytes of data directly from your data lake, data warehouses, and databases, including Amazon S3, Amazon Redshift, Amazon Aurora, and Amazon RDS.

AWS Glue DataBrew is built for users who need to clean and normalize data for analytics and machine learning. Data analysts and data scientists are the primary users. For data analysts, examples of job functions are business intelligence analysts, operations analysts, market intelligence analysts, legal analysts, financial analysts, economists, quants, or accountants. For data scientists, examples of job functions are materials scientists, bioanalytical scientists, and scientific researchers.

#### Glue DataBrew Project

The interactive data preparation workspace in DataBrew is called a project. Using a data project, you manage a collection of related items: data, transformations, and scheduled processes. As part of creating a project, you choose or create a dataset to work on. Next, you create a recipe, which is a set of instructions or steps that you want DataBrew to act on. These actions transform your raw data into a form that is ready to be consumed by your data pipeline.

A recipe is a set of instructions or steps for data that you want DataBrew to act on. A recipe can contain many steps, and each step can contain many actions. You use the transformation tools on the toolbar to set up all the changes that you want to make to your data. Later, when you're ready to see the finished product of your recipe, you assign this job to DataBrew and schedule it. DataBrew stores the instructions about the data transformation, but it doesn't store any of your actual data. You can download and reuse recipes in other projects. You can also pubish multiple versions of a recipe.

#### Glue DataBrew Job

DataBrew takes on the job of transforming your data by running the instructions that you set up when you made a recipe. The process of running these instructions is called a job. A job can put your data recipes into action according to a preset schedule. But you aren't confined to a schedule. You can also run jobs on demand. If you want to profile some data, you don't need a recipe. In that case, you can just set up a profile job to create a data profile.

#### Explore further

1. [Data Preparation on AWS: Comparing ELT Options to Cleanse and Normalize Data](https://knowledgetree.notion.site/Data-Preparation-on-AWS-Comparing-ELT-Options-to-Cleanse-and-Normalize-Data-Shared-5a16da581ef845d2a7e38f06ca0b35c0)
2. [Transform JSON / CSV files to Parquet through Aws Glue](https://hkdemircan.medium.com/how-can-we-json-css-files-transform-to-parquet-through-aws-glue-465773b43dad)
3. [Data Transformation at scale with AWS Glue](https://knowledgetree.notion.site/Data-Transformation-at-scale-with-AWS-Glue-Shared-65b9c00215bf42e69d94365a07a82f5a)

### RDS

> Amazon Relational Database Services

#### Watch the videos

- https://www.youtube.com/watch?v=eMzCI7S1P9M
- https://www.youtube.com/watch?v=FzxqIdIZ9wc

### S3

**Amazon S3** is one of the most commonly used cloud data storage services for web applications, and high-performance compute use cases. It is Amazon's object storage service providing virtually unlimited data storage. Some of the advantages of using Amazon S3 include very high scalability, durability, data availability, security, and performance. Amazon S3 can be used for a variety of cloud-native applications, ranging from simple data storage to very large data lakes to web hosting and high-performance applications, such as training very advanced and compute-intensive ML models. Amazon S3 offers several classes of storage options with differences in terms of data access, resiliency, archival needs, and cost. We can choose the storage class that best suits our use case and business needs. There is also an option for cost saving when the access pattern is unknown or changes over time (S3 Intelligent-Tiering).

### DMS

AWS Database Migration Service (AWS DMS) helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. The AWS Database Migration Service can migrate your data to and from the most widely used commercial and open-source databases.

AWS Database Migration Service supports homogeneous migrations such as Oracle to Oracle, as well as heterogeneous migrations between different database platforms, such as Oracle or Microsoft SQL Server to Amazon Aurora. With AWS Database Migration Service, you can also continuously replicate data with low latency from any supported source to any supported target. For example, you can replicate from multiple sources to Amazon Simple Storage Service (Amazon S3) to build a highly available and scalable data lake solution. You can also consolidate databases into a petabyte-scale data warehouse by streaming data to Amazon Redshift.

### Container Services

#### Watch these videos

1. [Containers on AWS Overview: ECS | EKS | Fargate | ECR](https://youtu.be/AYAh6YDXuho)
2. [An Overview of AWS Elastic Container Service (ECS)](https://youtu.be/I9VAMGEjW-Q)
3. [AWS EC2 on ECS vs Fargate | Whats the Difference and When To Use What?](https://youtu.be/DVrGXjjkpig)

### Secrets Manager

> AWS Secrets Management Service

### Makefile

```Makefile
install:
	pip install awscli

setup:
	aws configure

sts-identity:
	aws sts get-caller-identity

secret_manager_get_values:
	aws secretsmanager get-secret-value --secret-id wysde --query SecretString --output text

s3_create_bucket:
	TS=$(date +%s)
	aws s3api create-bucket --bucket <bucket-name>-$TS --region us-east-1

create_policy:
	aws iam create-policy --policy-name <policy-name> --policy-document file://<file-name>.json

create_role:
	aws iam create-role --role-name <role-name> --assume-role-policy-document file://role-trust.json

attach_policy_to_role:
	aws iam attach-role-policy --policy-arn <> --role-name <>

iam_keys_rotation:
	aws iam list-users
	aws iam list-access-keys --user-name jan31
	aws iam create-access-key --user-name jan31
	aws iam update-access-key --access-key-id <> --status Inactive --user-name jan31
	aws iam delete-access-key --access-key-id <> --user-name jan31

create-redshift-cluster:
# Use the following command to create a two-node dc2.large cluster with the minimal set of parameters of cluster-identifier (any unique identifier for the cluster), node-type/number-of-nodes and the master user credentials. Replace $MasterUserPassword in the following command with a password of your choice. The password must be 8-64 characters long and must contain at least one uppercase letter, one lowercase letter, and one number. You can use any printable ASCII character except /, "", or, or @:
	aws redshift create-cluster --node-type dc2.large --number-of-nodes 2 --master-username adminuser --master-user-password $MasterUserPassword --cluster-identifier myredshiftcluster
# It will take a few minutes to create the cluster. You can monitor the status of the cluster creation process using the following command:
	aws redshift describe-clusters --cluster-identifier myredshiftcluster
# Note that "ClusterStatus": "available" indicates that the cluster is ready for use and that you can connect to it using the "Address": "myredshiftcluster.abcdefghijk.eu-west-1.redshift.amazonaws.com" endpoint. The cluster is now ready. Now, you use an ODBC/JDBC to connect to the Amazon Redshift cluster.

ec2_port_routing:
	sudo iptables -t nat -L
	sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 8080
	sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-ports 8080
	sudo iptables -t nat -D PREROUTING 1 # to remove
	iptables -P INPUT ACCEPT
	iptables -P OUTPUT ACCEPT
	iptables -P FORWARD ACCEPT
	iptables -F

get_ssl_cert:
	sudo snap install core; sudo snap refresh core
	sudo apt-get remove certbot
	sudo snap install --classic certbot
	sudo ln -s /snap/bin/certbot /usr/bin/certbot
	sudo certbot certonly --standalone

ec2_login_ssh:
	chmod 400 sparsh.pem
	sudo chown -R ubuntu /home/ubuntu
	ssh -i "sparsh.pem" ubuntu@ec2-111-11-11-111.compute-1.amazonaws.com

secretsmanager_python:
	#!/usr/bin/python
	import boto3
	import json
	def get_secret(secret_name, region_name="us-east-1"):
		session = boto3.session.Session()
		client = session.client(
			service_name='secretsmanager',
			region_name=region_name)
		get_secret_value_response = client.get_secret_value(SecretId=secret_name)
		get_secret_value_response = json.loads(get_secret_value_response['SecretString'])
		return get_secret_value_response

secretsmanager_python_postgres:
	import pandas as pd
	import psycopg2
	import boto3
	import json
	from sqlalchemy import create_engine
	from sqlalchemy import text

	def get_secret(secret_name='wysde'):
		region_name = "us-east-1"
		session = boto3.session.Session()
		client = session.client(
			service_name='secretsmanager',
			region_name=region_name)
		get_secret_value_response = client.get_secret_value(SecretId=secret_name)
		get_secret_value_response = json.loads(get_secret_value_response['SecretString'])
		return get_secret_value_response

	secret_vals = get_secret()

	postgres_endpoint = secret_vals['RDS_POSTGRES_HOST']
	postgres_user = secret_vals['RDS_POSTGRES_USERNAME']
	postgres_pass = secret_vals['RDS_POSTGRES_PASSWORD']
	port = secret_vals['RDS_POSTGRES_PORT']
	dbname = "postgres"

	engine_string = "postgresql+psycopg2://%s:%s@%s:%s/%s" \
	% (postgres_user, postgres_pass, postgres_endpoint, port, dbname)
	engine = create_engine(engine_string)

	query = """
	SELECT *
	FROM pg_catalog.pg_tables
	WHERE schemaname != 'pg_catalog' AND 
		schemaname != 'information_schema';
	"""
	df = pd.read_sql_query(text(query), engine)
```

### AWS Certified Solutions Architect

Download the slides from S3 using `sh resources/download.sh` command and learn the concepts

## <a href="#/01-foundations/cloud/lab-aws-setup/" target="_blank">Lab: AWS Account Setup ⤻</a>

1. Install AWS CLI
2. Create IAM user and generate credentials
3. Setup AWS credentials

## <a href="#/01-foundations/cloud/lab-create-iam-policy-role/" target="_blank">Lab: AWS IAM Service ⤻</a>

1. Create policies and roles
2. Attach policies to the roles

## <a href="#/01-foundations/cloud/lab-aws-secrets-manager/" target="_blank">Lab: AWS Secrets Manager Service ⤻</a>

1. Create a Secret in Secrets Manager Vault
2. Get the credential using AWS CLI

## <a href="#/01-foundations/cloud/lab-create-your-first-vpc/" target="_blank">Lab: Create AWS VPC ⤻</a>

## <a href="#/01-foundations/cloud/lab-create-your-first-ec2-instance-linux/" target="_blank">Lab: Create AWS EC2 instance ⤻</a>

## Google Cloud Platform (GCP)

There are a lot of services in GCP. The services are not only limited to data and analytics. They also cover other areas such as application development, machine learning, networks, source repositories, and many more. As a data engineer working on GCP, you will face situations when you need to decide which services you need to use for your organization.

You might be wondering, who in an organization should decide on the services to use? Is it the CTO, IT manager, solution architect, or data engineers? The answer depends on the experience of using GCP of each of them. But most of the time, data engineers need to be involved in the decision.

So how should we decide? In my experience, there are three important decision factors:

- Choose services that are serverless.
- Understand the mapping between the service and the data engineering areas.
- If there is more than one option in one area, choose the most popular service in the market.

Choosing a serverless service or, to use another common term, a fully managed service, **Software as a Service** (**SaaS**), can also mean choosing services that are the easiest. The easiest in terms of Google manages everything for us, so we can just use the tool.

Now let's discuss these three factors in more detail in the following subsections.

#### Understanding the GCP serverless service

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

#### Service mapping and prioritization

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

#### Big data

Here is the list of services under **big data**:

1. **BigQuery**: A fully managed data warehouse service
2. **Dataproc**: A Hadoop-managed service including HDFS, MapReduce, Spark, Presto, and more
3. **Dataflow**: A fully managed distributed processing framework service, very suitable for streaming jobs
4. **Pub/Sub**: A fully managed service messaging system, to publish and subscribe data

#### Storage and DB

Here is the list of services under **storage and database**:

1. **Cloud Storage**: A fully managed service for storing large files
2. **Bigtable**: A fully managed NoSQL database service
3. **SQL**: A managed service for application databases, for example, MySQL, PostgreSQL, and SQL Server
4. **Datastore**: A fully managed NoSQL document database service

#### ETL orchestrator

Here is the list of services under **ETL orchestrator**:

1. **Cloud Composer**: An Airflow-managed service. Airflow is a Python-based job orchestration tool.
2. **Data Fusion**: A UI-based orchestration tool to run Hadoop jobs on Dataproc.
3. **Dataprep**: A UI-based data wrangling tool. While data wrangling is similar to the ETL process in general, Dataprep has unique features, for example, checking data distribution in histograms and checking missing values. Dataprep is managed by a third party, **Trifacta**, which means that GCP customers need to have separate legal agreements with Trifacta. 

#### Identity and management tools

Here is the list of services under **Identity and management tools**:

1. **IAM & Admin**: User and project management for all GCP services
2. **Logging**: A logging system for all GCP services
3. **Monitoring**: A monitoring system with dashboards driven by data from Cloud Logging
4. **Data Catalog**: A metadata system that stores data from GCS, BigQuery, and PubSub

#### ML and BI

Here is the list of services under **machine learning and BI tools**:

1. **Vertex AI**: All the tools that you need to build ML and MLOps, for example, notebook, pipeline, model store, and other ML-related services
2. **Looker**: A full-fledged BI tool to visualize data in reports and dashboards
3. **Data Studio**: A simple visualization tool to visualize data

At this point, I have only added very short and simple descriptions for each service. The reason is what is important for now, at this stage, is for us to know the services' positioning. A detailed explanation of each service can be found easily on the internet.

### Setup

To set up GCP, please follow the steps below:

1. If you don't have a GCP account, please create a free trial.
2. Setup new project and write down your Project ID.
3. Configure service account to get access to this project and download auth-keys (.json). Please check the service
   account has all the permissions below:
   * Viewer
   * Storage Admin
   * Storage Object Admin
   * BigQuery Admin
4. Download [SDK](https://cloud.google.com/sdk) for local setup.
5. Set environment variable to point to your downloaded auth-keys:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"

# Refresh token/session, and verify authentication
gcloud auth application-default login
```

6. Enable the following options under the APIs and services section:
   * [Identity and Access Management (IAM) API](https://console.cloud.google.com/apis/library/iam.googleapis.com)
   * [IAM service account credentials API](https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com)
   * [Compute Engine API](https://console.developers.google.com/apis/api/compute.googleapis.com) (if you are going to use VM instance)

## Azure Cloud

### Data Ingestion

This is the process of getting all the raw data into the data lake. Data from various sources lands in the raw zone of the data lake. Based on where the data is coming from, such as on-premise systems, other cloud systems, and so on, we could use different ingestion tools. Let's look at some of the options available in Azure:

- **Azure Data Factory** -- It provides data ingestion support from hundreds of data sources, and even from other clouds such as AWS, GCP, Oracle, and so on.
- **Azure Copy** (**AzCopy**) -- This is a command-line tool that can be used to copy data over the internet and is ideally suited for smaller data sizes (preferably in the 10--15 TB range). You can learn more about AzCopy here: [https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10.](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10%0D)
- **Azure ExpressRoute** -- If you need a secure way to transfer data into Azure, then use ExpressRoute. It routes your data through dedicated private connections to Azure instead of the public internet. This is also the preferred option if you want to have a dedicated pipeline with a faster data transfer speed. You can learn more about Azure ExpressRoute here: [https://docs.microsoft.com/en-us/azure/expressroute/expressroute-introduction.](https://docs.microsoft.com/en-us/azure/expressroute/expressroute-introduction%0D)

### Batch Processing

Here is a useful table reproduced from Azure that can help you decide on the technologies to use for your batch scenarios:

![B17525_09_018](https://user-images.githubusercontent.com/62965911/218308595-df31da23-a5d3-483b-88ba-669994a72789.jpeg)

You can learn more about the batch processing choices here: [https://docs.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/batch-processing.](https://docs.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/batch-processing%0D)

### End-to-end Solutions

#### Modern Azure Data Architecture Platform

While Microsoft Azure has a vast collection of resources, the most common components within the Modern Enterprise Data and Analytics Platform are listed in following figure. As an Azure Data Engineer, it will be critical to be able to design and implement an end-to-end solution that follows this architectural process or custom variations of it while accounting for security, high availability, and more. It will also be critical to understand the differences and similarities between multiple data storage and data integration options.

![511918_1_En_1_Fig2_HTML](https://user-images.githubusercontent.com/62965911/218317429-4320444d-5cb1-4210-9b9d-a64b1885f624.jpeg)

#### High-level diagram of Azure data architecture with DevOps CI/CD

With free online video tutorials, along with Microsoft’s vast knowledge base of documentation that’s easily accessible, understanding the end-to-end architectural process and how it relates to connectivity, security, infrastructure as code, Azure administration, DevOps CI/CD, and billing and cost management will instill confidence in your holistic understanding of Azure as you help your organization and team evangelize Azure Data Engineering and pioneer their journey into the cloud. Figure below presents a diagram with multiple components, along with how it all ties together from an architectural standpoint.

![511918_1_En_1_Fig6_HTML](https://user-images.githubusercontent.com/62965911/218317641-255befa5-893a-419f-a5e2-ace713a682b6.jpeg)

#### Data Lake Architecture

The following image shows a data lake architecture for both batch and stream processing. The diagram also includes examples of the Azure technologies that can be used for each of the data lake zones. The names of the services listed by the icons are presented in the image after this:

![B17525_02_001](https://user-images.githubusercontent.com/62965911/218276767-b43dd30a-03a1-42c9-a09b-be3c3d572fd3.jpeg)

Here are the names of the services represented by the icons in the preceding diagram:

![B17525_02_002](https://user-images.githubusercontent.com/62965911/218276807-570375d0-43d3-43a9-9493-6faa7835cac4.jpeg)

#### Data Platform Architecture

Data is ingested into the system and persisted in a storage layer. Processing aggregates and reshapes the data to enable analytics and machine learning scenarios. Orchestration and governance are cross-cutting concerns that cover all the components of the platform. Once processed, data is distributed to other downstream systems. All components are tracked by and deployed from source control.

![IFC_F01_Riscutia2](https://user-images.githubusercontent.com/62965911/218319349-07737795-ddcb-4d9c-90c0-444be388cfb3.png)

### Learning Path

The following figure shows Microsoft’s learning path for the Azure Data Engineer, which covers designing and implementing the management, monitoring, security, and privacy of data using Azure data resources.

![511918_1_En_1_Fig4_HTML](https://user-images.githubusercontent.com/62965911/218317540-0307de7b-9f19-4778-86e1-2fa961a0ef51.png)

