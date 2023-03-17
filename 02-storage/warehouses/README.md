# Data Warehouses

Enterprises are becoming increasingly data driven, and a key component of any enterprise’s data strategy is a data warehouse—a central repository of integrated data from all across the company. Traditionally, the data warehouse was used by data analysts to create analytical reports. But now it is also increasingly used to populate real-time dashboards, to make ad hoc queries, and to provide decision-making guidance through predictive analytics. Because of these business requirements for advanced analytics and a trend toward cost control, agility, and self-service data access, many organizations are moving to cloud-based data warehouses such as Snowfkake, Amazon Redshift and Google BigQuery.

A data warehouse is a piece of technology that acts on 3 ideas: the data modeling, the data storage and processing engine.

In this cloud world where everything is serverless a good data modeling is still a key factor in the performance—which often mean cost—of a data platform. Modeling is often lead by the dimensional modeling but you can also do 3NF or data vault. When it comes to storage it's mainly a row-based vs. a column-based discussion, which in the end will impact how the engine will process data. Processing engines are mainly SMP (Symmetrical Multiprocessing) and MPP (Massively Parallel Processing).

In a modern data warehouse architecture, both the data lake and the data warehouse peacefully coexist, each serving a distinct purpose. The data lake serves as a low cost storage for a large amount of data and also supports exploratory scenarios such as data science and machine learning. The data warehouse stores high value data and is used to power dashboards used by the business and also is used for business intelligence users to query the highly structured data to gain insights about the business.

Data is first ingested into a data lake from various sources - on-premises databases, social media feeds, etc. This data is then transformed using big data analytics frameworks such as Hadoop and Spark, where multiple datasets can also be aggregated and filtered to generate high value structured data. This data is then loaded into a cloud data warehouse to power dashboards, as well as interactive dashboards for BI analysts using their very familiar tool of choice - SQL. In addition, the data lake also empowers a whole new set of scenarios that involve exploratory analysis by data scientists, and also machine learning models that can be fed back into their applications. A simplified representation of the modern data warehouse architecture is provided below:

![](https://user-images.githubusercontent.com/62965911/213930650-191c6bc4-5b45-4275-b88e-dfc90c98e4cb.png)

There is now a question you would naturally ask here - what is the difference between using a cloud data warehouse directly, why is a data lake necessary in between? Specially, if I only have structured data, do I even need a data lake? If I can say so myself, these are great questions. There are a few reasons why you would need a data lake in this architecture.

1. Data lakes cost a lot lesser than a data warehouse, and can act as your long term repository of data. It is of note to remember that data lakes are typically used to store large volumes of data (think tens or hundreds of petabytes) that the difference in cost is material.
2. Data lakes support a variety of modern tools and frameworks around data science and machine learning, that you can enable completely new scenarios.
3. Data lakes let you future-proof your design to scale to your growing needs. As an example, you might start off your initial data lake architecture to load data from your on-premises systems on a nightly basis and publish reports or dashboards for your business intelligence users, however, the same architecture is extensible to support real time data ingestion without having to rearchitect your solution.
4. Data of all forms and structures are largely becoming relevant to organizations. Even if you are focused on structured data today, as you saw in the example above, you might find value in all kinds of data such as weather, social media feeds, etc.

Cloud adoption continues to grow with even highly regulated industries such as healthcare and Fintech embracing the cloud for cost-effective alternatives to keep pace with innovation; otherwise, they risk being left behind. People who have used security as the reason for not going to the cloud should be reminded that all the massive data breaches that have been splashing the media in recent years have all been from on-premises setups. Cloud architectures have more scrutiny and are in some ways more governed and secure.

Most enterprises currently have three types of data storage systems.

1. Application Databases — Transactional systems which capture data from all operations in the enterprise e.g. HR, Finance, CRM, Sales etc.
2. Data Lakes — These are catch-all cloud storage systems which store structured and unstructured data like application data backups, logs, web-click-streams, pictures, videos etc.
3. Data Warehouses — Integrated, cleansed data organized in a way to enhance query performance so that we can run reports and dashboards quickly.

## Benefits and Challenges of Modern Data Warehouse Architecture

The modern data warehouse has an important benefit of helping the business analysts leverage familiar Business Intelligence tool sets (SQL based) for consumption, while also enabling more modern scenarios around data science and machine learning that were originally not possible in their on-premises implementation of a data warehouse. This is primarily accomplished with a data lake, that serves as a no-silos data store supporting advanced data science and machine learning scenarios with cloud native services, while retaining the familiar data warehouse like SQL based interface for business intelligence users. In addition, the data administrators can isolate the access of the data to the data warehouse for the BI teams using familiar access control methods of the data warehouse. Their applications running on-premises can also be ported to the cloud over time to completely eliminate the need to maintain two sets of infrastructures. Further, the business is overall able to lower their costs by backing up the operational data into a data lake for a longer time period.

There are also a few challenges with this approach. The data engineers and administrators need to still maintain two sets of infrastructures - a data lake and data warehouse. The flexibility of storing all kinds of data in a data lake also poses a challenge - managing data in the data lake and assuming guarantees of data quality is a huge challenge that data engineers and data administrators now have to solve. They did not have this problem before. The data lake also runs the risk of growing into a data swamp if the data is not managed properly making your insights be hidden like a needle in a haystack. If BI users or business decision makers need new data sets, they need to rely upon the data engineers to process this data and load it into the warehouse, introducing a critical path. Further, if there is an interesting slice of data in the warehouse that the data scientists want to include for exploratory analysis, they need to load it back into the data lake, in a different data format, as well as a different data store, increasing the complexity of sharing.

### Speed vs Granularity tradeoff in data systems

You can do additional processing on top of dimensional data modeling to increase speed of access. Optimizing for speed does require sacrificing granularity, but as technology continues to improve, these tradeoffs become less consequential. Denormalized tables and OLAP cubes are the two ways to increase speed of access. Building denormalized tables, or summary tables, on top of your dimensional data models enables faster performance, but it does require some sacrifice of granularity. For example, you can save the “last 7 day purchases” on a per-user basis in a single data table for fast access, but you’ll lose the ability to get “last 8 day purchases”. For many usage patterns, the speed is worth the tradeoff because users would rather see pre-baked data in 3 seconds than wait 30 seconds for customization.

OLAP cubes are a more intensive option to increase speed of access. An OLAP cube pre-aggregates the data so much that lookup queries are near-instant. However, they require much more prep, and they sacrifice more granularity. Denormalized tables are a better way to satisfy performance for most use cases.

It's also worth noting that newer technologies such as Druid and Pinot can have extremely fast querying using a single table. This makes denormalized tables an appealing option if you choose to use these technologies since you don't have to pre-aggregate.

In addition to this, there are also in-memory implementations of data models that allow for fast data access. Tableau has Tableau Data Extract – first with the tde format and more recently hyper formats to enable fast access of large datasets. Arrow is another in-memory approach that allows for data systems to be built with interactive performance.

![](https://user-images.githubusercontent.com/62965911/214000302-c6e7373c-fd30-47ad-bfca-b7431d542ec6.png)

This graph provides a rough representation of the speed vs. granularity tradeoff that’s central to dimensional data modeling. As speed increases, granularity decreases, and vise-versa. But what’s exciting to note is that as technology improves, the graph shifts further to the right. That is, we’re able to maintain more granularity at higher speeds. As each step gets faster, all of a sudden you can use the more granular technique for certain workloads and still meet user time expectations. This means a simpler data pipeline and less loss of granularity to achieve the same goals.

To drive the point home, consider the OLAP cube. OLAP cubes have largely fallen out of favor because recent advancements make denormalized tables a pretty good balance of performance and flexibility for most teams today.

## Data Warehouse Options

#### Traditional Solutions for Data Warehouse

- SQL Server
- PostgreSQL
- MySQL

#### Cloud Data Warehouses

- BigQuery (Google Cloud)
- Redshift (AWS Cloud)
- Snowflake

#### Other Options

- AWS Athena
- Hadoop Hive

## Building a Data Warehouse/Lake solution on Cloud

#### 1. Data Warehouse Management (Strong SQL and Data Modeling Skills)

- Data Modeling
- Optimizing Queries
- Billing/Cost Management
- User/Access Management
- Enabling BI/Analytics for Query Management
- Data Governance and Security

#### 2. ETL/Data Movement (Strong Scripting/Coding skills along with understanding of cloud components)

- Writing Pipelines using Scala/Java/Python
- Data Orchestration Tools (Airflow/Step Functions)
- Deployment and Integration of Analytics/ML Models
- Know-how of best solutions for deploying scalable pipelines
- Logging, alerting and notifications

## Designing a data warehouse from the ground up

In general, the process of designing a data warehouse may involve the following steps:

1. Identify the business requirements: The first step in designing a data warehouse is to understand the needs of the organization and the types of data that will be required to support the business. This may involve working with stakeholders to identify the specific goals and objectives of the data warehouse, as well as the types of data that will be needed to support these goals.
2. Select the tools and technologies: The next step in designing a data warehouse is to choose the tools and technologies that will be used to build and manage the data warehouse. This may include selecting a database management system (DBMS), data integration and extraction tools, and analysis and visualization tools.
3. Design the data model: After the tools and technologies have been selected, the next step is to design the data model for the data warehouse. This may involve identifying the data sources, defining the data structures and relationships, and establishing the data governance and security protocols that will be used to manage the data.
4. Load and test the data: Once the data model has been designed, the final step is to load the data into the data warehouse and test it to ensure that it meets the business requirements and can be accessed and analyzed as needed. This may involve setting up ETL (extract, transform, load) processes to move data from the various sources into the data warehouse, and testing the data to ensure that it is accurate and up-to-date.

#### Select the tools and technologies

Tools and technologies, in today's world, can be influenced by many factors for example whether you prefer cloud or on-premise or if you go with cloud, then your existing cloud infrastructure.

For on-premises data warehousing (building the data warehouse on your own physical hardware), some popular tools include Oracle Database, Microsoft SQL Server, IBM Db2, Teradata, and SAP HANA. These tools offer advanced features like data compression, real-time analytics, support for unstructured data, and parallel processing.

There are also several popular cloud data warehousing tools that organizations can use to design and build their data warehouses in the cloud:

1. Amazon Redshift: Amazon Redshift is a fully managed, cloud-based data warehousing service offered by Amazon Web Services (AWS). It offers fast querying and analysis of data using SQL and can handle petabyte-scale data warehouses.
2. Google BigQuery: Google BigQuery is a fully managed, cloud-based data warehousing service offered by Google Cloud. It offers real-time analysis of large and complex datasets and can handle petabyte-scale data warehouses.
3. Azure Synapse Analytics: Azure Synapse Analytics is a fully managed, cloud-based data warehousing service offered by Microsoft Azure. It offers integration with Azure Machine Learning and support for real-time analytics.
4. Snowflake: Snowflake is a fully managed, cloud-based data warehousing platform that offers a range of features including support for semi-structured data, data sharing, and data lake integration.

#### Design the data model

There are multiple steps you need to take to design data modeling in your data warehouse.

1. Identify the business process
2. pick the right grain
3. pick the right dimensions
4. pick the right measures

**Identify the business process**

It's very important to focus on business process and not business departments as many departments share the same business process and if we focus on department, we might end up with multiple copies of models and have different sources of truth.

When the right business process is picked, then we should start with the most impactful model with the lowest risk. In other words, the models should be used frequently and be critical to the business and also it must be built accurately. If we don't have a high quality data for the model, it would impose a risk of inaccuracy and it would nullify its business impact.

For picking the impactful models, consult with the stakeholders and they can help you decide which models to start with.

**pick the right grain**

Grain refers to the level of granularity, or detail, at which the data in the data warehouse should be organized. The grain of a data warehouse is an important aspect of its design because it affects the types of questions that can be asked of the data and the efficiency with which queries can be answered. Since, it's not possible to predict the type of queries your analysts are interested in, it's better to pick the most atomic level for your model.

For example, if the grain of a data warehouse is set at the customer level, then it would be easy to answer questions about individual customers, such as their purchase history or demographic information. On the other hand, if the grain is set at the transaction level, then it would be easy to answer questions about individual transactions, such as the products purchased and the total amount spent.

In order to identify the right grain for a data warehouse, it is important to consider the types of questions that will be asked of the data and to design the data warehouse accordingly. This may involve trade-offs between the level of detail that is captured and the efficiency of querying the data. It is also important to consider the size and complexity of the data, as well as the resources available for storing and processing it.

If you don't pick a right grain, you need to spend a lot of time to redo your design. Moreover, if you don't pick the most granular grain, then you might lose the data, and it is sometimes not possible to go back. For example, if you pick a granularity of month for your data, if you hadn't stored the historical data, then it's impossible to go back to day granularity.

**pick the right dimensions**

Right dimensions are the relevant data attributes that will be used to organize and categorize the data in the warehouse. These dimensions provide a way to slice and dice the data, allowing users to analyze and understand the data from various perspectives.

For example, in a data warehouse for a retail business, some common dimensions might include time, location, product, and customer. Time might be used to track sales data over different time periods (e.g. daily, monthly, yearly). Location might be used to track sales data by store or region. Product might be used to track sales data by product category or specific product. Customer might be used to track sales data by customer demographics or customer loyalty status.

Choosing the right dimensions is important because it determines the level of detail and granularity of the data that can be analyzed in the warehouse. If the wrong dimensions are chosen, it may be difficult or impossible to get the insights that are needed from the data. On the other hand, if the right dimensions are chosen, it will be much easier to explore and analyze the data in meaningful ways.

**pick the right measures**

Choosing the right measures refers to selecting the appropriate metrics or quantities that you want to track and analyze in your data warehouse. These measures can be used to support business decision-making and help you understand trends and patterns within your data.

There are several factors to consider when selecting measures for your data warehouse:

1. Relevance: The measures you choose should be relevant to your business goals and objectives. For example, if you are a retail company, you might want to track metrics like sales revenue and customer loyalty.
2. Accuracy: It's important to choose measures that are accurate and reliable. If the data you are using to calculate a measure is incorrect or incomplete, the resulting measure will also be inaccurate.
3. Timeliness: Choose measures that are up-to-date and timely. If you are tracking metrics that are out-of-date, they may not be useful for decision-making.
4. Consistency: Make sure the measures you choose are consistent over time. If you are tracking a metric that fluctuates significantly from one time period to the next, it may be difficult to identify trends or patterns.
5. Comparability: Consider whether the measures you choose can be compared to other data sources or to past performance. This can help you understand how your business is performing relative to other companies or to its own performance over time.

## Amazon Redshift

Amazon Redshift is a data warehousing service optimized for **online analytical processing** (**OLAP**) applications. You can start with just a few hundred **gigabytes** (**GB**) of data and scale to a **petabyte** (**PB**) or more. Designing your database for analytical processing lets you take full advantage of Amazon Redshift's columnar architecture.

An analytical schema forms the foundation of your data model. You can choose a star or snowflake schema by using Normalized, Denormalized, or Data Vault data modeling techniques. Redshift is a relational database management system (RDBMS) that supports a number of data model structures, including dimensional, denormalized, and aggregate (rollup) structures. This makes it optimal for analytics.

Watch this video: https://www.youtube.com/watch?v=lWwFJV_9PoE

### Data Ingestion in Amazon Redshift

Data ingestion is the process of getting data from the source system to Amazon Redshift. This can be done by using one of many AWS cloud-based ETL tools like AWS Glue, Amazon EMR, or AWS Step Functions, or you can simply load data from Amazon Simple Storage Service (Amazon S3) to Amazon Redshift using the COPY command. A COPY command is the most efficient way to load a table because it uses the Amazon Redshift massively parallel processing (MPP) architecture to read and load data in parallel from a file or multiple files in an S3 bucket.

Now SQL users can easily automate data ingestion from Amazon S3 to Amazon Redshift with a simple SQL command using the Amazon Redshift auto-copy feature. COPY statements are triggered and start loading data when Amazon Redshift auto-copy detects new files in the specified Amazon S3 paths. This also ensures end-users have the latest data available in Amazon Redshift shortly after the source data is available.

Copy jobs have the following benefits:

- SQL users such as data analysts can now load data from Amazon S3 automatically without having to build a pipeline or using an external framework
- Copy jobs offer continuous and incremental data ingestion from an Amazon S3 location without the need to implement a custom solution
- This functionality comes at no additional cost
- Existing COPY statements can be converted into copy jobs by appending the JOB CREATE <job_name> parameter
- It keeps track of all loaded files and prevents data duplication
- It can be easily set up using a simple SQL statement and any JDBC or ODBC client

### Explore further

1. [Accelerate Application Development with Real Time Streams in Amazon Redshift](https://bit.ly/3Se99Ur)
2. [Data Engineering at Udem](https://www.slideshare.net/ankarabigdata/data-engineering-at-udemy?qid=d835f0e3-f290-4445-bd19-d6ac6824e24c&v=&b=&from_search=5)
3. [Implement a slowly changing dimension in Amazon Redshift](https://aws.amazon.com/blogs/big-data/implement-a-slowly-changing-dimension-in-amazon-redshift/)

### Makefile

```makefile
# Redshift Cluster Management

Connect to Redshift using Python:
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

	redshift_endpoint = secret_vals['REDSHIFT_HOST']
	redshift_user = secret_vals['REDSHIFT_USERNAME']
	redshift_pass = secret_vals['REDSHIFT_PASSWORD']
	port = 5439
	dbname = "dev"

	engine_string = "postgresql+psycopg2://%s:%s@%s:%d/%s" \
	% (redshift_user, redshift_pass, redshift_endpoint, port, dbname)
	engine = create_engine(engine_string)

	query = """
	SELECT *
	FROM pg_catalog.pg_tables
	WHERE schemaname != 'pg_catalog' AND 
		schemaname != 'information_schema';
	"""
	df = pd.read_sql_query(text(query), engine)

	query = """
	SELECT * FROM "dev"."public"."users";
	"""
	df = pd.read_sql_query(text(query), engine)

Create AWS Redshift Cluster:
	import pandas as pd
	import boto3
	import json
	import psycopg2

	from botocore.exceptions import ClientError
	import configparser

	from random import random
	import threading
	import time

	# Tracking Cluster Creation Progress
	progress = 0
	cluster_status = ''
	cluster_event = threading.Event()

	def initialize():
		"""
		Summary line. 
		This function starts the create_cluster function. 

		Parameters: 
		NONE

		Returns: 
		None
		"""  
		# Get the config properties from dwh.cfg file
		config = configparser.ConfigParser()
		config.read_file(open('./aws/aws-capstone.cfg'))

		KEY                    = config.get('AWS','KEY')
		SECRET                 = config.get('AWS','SECRET')

		DWH_CLUSTER_TYPE       = config.get("CLUSTER","DWH_CLUSTER_TYPE")
		DWH_NUM_NODES          = config.get("CLUSTER","DWH_NUM_NODES")
		DWH_NODE_TYPE          = config.get("CLUSTER","DWH_NODE_TYPE")

		DWH_CLUSTER_IDENTIFIER = config.get("CLUSTER","DWH_CLUSTER_IDENTIFIER")
		DWH_DB                 = config.get("CLUSTER","DWH_DB")
		DWH_DB_USER            = config.get("CLUSTER","DWH_DB_USER")
		DWH_DB_PASSWORD        = config.get("CLUSTER","DWH_DB_PASSWORD")
		DWH_PORT               = config.get("CLUSTER","DWH_PORT")

		DWH_IAM_ROLE_NAME      = config.get("IAM_ROLE", "DWH_IAM_ROLE_NAME")


		df = pd.DataFrame({"Param":
						["DWH_CLUSTER_TYPE", "DWH_NUM_NODES", "DWH_NODE_TYPE", "DWH_CLUSTER_IDENTIFIER", "DWH_DB", "DWH_DB_USER", "DWH_DB_PASSWORD", "DWH_PORT", "DWH_IAM_ROLE_NAME"],
					"Value":
						[DWH_CLUSTER_TYPE, DWH_NUM_NODES, DWH_NODE_TYPE, DWH_CLUSTER_IDENTIFIER, DWH_DB, DWH_DB_USER, DWH_DB_PASSWORD, DWH_PORT, DWH_IAM_ROLE_NAME]
					})

		print(df)


		ec2 = boto3.resource('ec2',
							region_name="us-west-2",
							aws_access_key_id=KEY,
							aws_secret_access_key=SECRET
							)

		s3 = boto3.resource('s3',
							region_name="us-west-2",
							aws_access_key_id=KEY,
							aws_secret_access_key=SECRET
						)

		iam = boto3.client('iam',aws_access_key_id=KEY,
							aws_secret_access_key=SECRET,
							region_name='us-west-2'
						)

		redshift = boto3.client('redshift',
							region_name="us-west-2",
							aws_access_key_id=KEY,
							aws_secret_access_key=SECRET
							)


		roleArn = create_iam_role(iam, DWH_IAM_ROLE_NAME)

		create_cluster(redshift, roleArn, DWH_CLUSTER_TYPE, DWH_NODE_TYPE, DWH_NUM_NODES, DWH_DB, DWH_CLUSTER_IDENTIFIER, DWH_DB_USER, DWH_DB_PASSWORD)

		#thread = threading.Thread(target=check_cluster_status)
		thread = threading.Thread(target=lambda : check_cluster_status(redshift, DWH_CLUSTER_IDENTIFIER, 'create', 'available'))
		#thread = threading.Thread(target=lambda : check_cluster_status(redshift, DWH_CLUSTER_IDENTIFIER, 'available'))
		thread.start()

		# wait here for the result to be available before continuing
		while not cluster_event.wait(timeout=5):  
			print('\r{:5}Waited for {} seconds. Redshift Cluster Creation in-progress...'.format('', progress), end='', flush=True)
		print('\r{:5}Cluster creation completed. Took {} seconds.'.format('', progress))  

		myClusterProps = get_cluster_properties(redshift, DWH_CLUSTER_IDENTIFIER)
		#print(myClusterProps)
		prettyRedshiftProps(myClusterProps[0])
		DWH_ENDPOINT = myClusterProps[1]
		DWH_ROLE_ARN = myClusterProps[2]
		print('DWH_ENDPOINT = {}'.format(DWH_ENDPOINT))
		print('DWH_ROLE_ARN = {}'.format(DWH_ROLE_ARN))

		open_ports(ec2, myClusterProps[0], DWH_PORT)

		conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format( DWH_ENDPOINT, DWH_DB, DWH_DB_USER, DWH_DB_PASSWORD, DWH_PORT ))
		cur = conn.cursor()

		print('Connected')  

		conn.close()
		print('Done!')

	def create_iam_role(iam, DWH_IAM_ROLE_NAME):
		"""
		Summary line. 
		Creates IAM Role that allows Redshift clusters to call AWS services on your behalf

		Parameters: 
		arg1 : IAM Object
		arg2 : IAM Role name

		Returns: 
		NONE
		"""  
		try:
			print("1.1 Creating a new IAM Role") 
			dwhRole = iam.create_role(
				Path='/',
				RoleName=DWH_IAM_ROLE_NAME,
				Description = "Allows Redshift clusters to call AWS services on your behalf.",
				AssumeRolePolicyDocument=json.dumps(
					{'Statement': [{'Action': 'sts:AssumeRole',
					'Effect': 'Allow',
					'Principal': {'Service': 'redshift.amazonaws.com'}}],
					'Version': '2012-10-17'})
			)  
		except Exception as e:
			print(e)

		print("1.2 Attaching Policy")
		iam.attach_role_policy(RoleName=DWH_IAM_ROLE_NAME,
							PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
							)['ResponseMetadata']['HTTPStatusCode']

		print("1.3 Get the IAM role ARN")
		roleArn = iam.get_role(RoleName=DWH_IAM_ROLE_NAME)['Role']['Arn']

		print('{:5} ARN : {}'.format('',roleArn))
		return roleArn

	def create_cluster(redshift, roleArn, DWH_CLUSTER_TYPE, DWH_NODE_TYPE, DWH_NUM_NODES, DWH_DB, DWH_CLUSTER_IDENTIFIER, DWH_DB_USER, DWH_DB_PASSWORD):
		"""
		Summary line. 
		Creates Redshift Cluster

		Parameters: 
		arg1 : Redshift Object
		arg2 : Cluster Name

		Returns: 
		None
		"""  
		print('1.4 Starting Redshift Cluster Creation')
		try:
			response = redshift.create_cluster(  
				#HW
				ClusterType=DWH_CLUSTER_TYPE,
				NodeType=DWH_NODE_TYPE,
				NumberOfNodes=int(DWH_NUM_NODES),

				#Identifiers & Credentials
				DBName=DWH_DB,
				ClusterIdentifier=DWH_CLUSTER_IDENTIFIER,
				MasterUsername=DWH_DB_USER,
				MasterUserPassword=DWH_DB_PASSWORD,

				#Roles (for s3 access)
				IamRoles=[roleArn]  
			)
		except Exception as e:
			print(e)

	def prettyRedshiftProps(props):
		"""
		Summary line. 
		Returns the Redshift Cluster Properties in a dataframe

		Parameters: 
		arg1 : Redshift Properties

		Returns: 
		dataframe with column key, value
		"""  

		pd.set_option('display.max_colwidth', -1)
		keysToShow = ["ClusterIdentifier", "NodeType", "ClusterStatus", "MasterUsername", "DBName", "Endpoint", "NumberOfNodes", 'VpcId']
		#print(props)
		x = [(k, v) for k,v in props.items() if k in keysToShow]
		'''
		#(OR) Below is longer version above is shorter version
		xx = []
		for k in props:
			if k in keysToShow:
				v = props.get(k)
				xx.append((k,v))
				print('{} : {}'.format(k, v))  
		print('XX = ',xx)
		'''
		#print('X = ',x)
		return pd.DataFrame(data=x, columns=["Key", "Value"])

	def check_cluster_status(redshift, DWH_CLUSTER_IDENTIFIER, action, status):
		"""
		Summary line. 
		Check the cluster status in a loop till it becomes available/none. 
		Once the desired status is set, updates the threading event variable

		Parameters: 
		arg1 : Redshift Object
		arg2 : Cluster Name
		arg3 : action which can be (create or delete)
		arg4 : status value to check 

		Returns: 
		NONE
		"""  

		global progress
		global cluster_status

		# wait here for the result to be available before continuing  
		while cluster_status.lower() != status:
			time.sleep(5)
			progress+=5
			if action == 'create':
				myClusterProps = redshift.describe_clusters(ClusterIdentifier=DWH_CLUSTER_IDENTIFIER)['Clusters'][0]
				#print(myClusterProps)
				df = prettyRedshiftProps(myClusterProps)
				#print(df)
				#In keysToShow 2 is ClusterStatus
				cluster_status = df.at[2, 'Value']    
			elif action =='delete':
				myClusterProps = redshift.describe_clusters()
				#print(myClusterProps)
				if len(myClusterProps['Clusters']) == 0 :
					cluster_status = 'none'
				else:
					myClusterProps = redshift.describe_clusters(ClusterIdentifier=DWH_CLUSTER_IDENTIFIER)['Clusters'][0]
					#print(myClusterProps)
					df = prettyRedshiftProps(myClusterProps)
					#print(df)
					#In keysToShow 2 is ClusterStatus
					cluster_status = df.at[2, 'Value']                    

			print('Cluster Status = ',cluster_status)  
	
		# when the calculation is done, the result is stored in a global variable
		cluster_event.set()
		# Thats it

	def get_cluster_properties(redshift, DWH_CLUSTER_IDENTIFIER):
		"""
		Summary line. 
		Retrieve Redshift clusters properties

		Parameters: 
		arg1 : Redshift Object
		arg2 : Cluster Name

		Returns: 
		myClusterProps=Cluster Properties, DWH_ENDPOINT=Host URL, DWH_ROLE_ARN=Role Amazon Resource Name
		"""  
		myClusterProps = redshift.describe_clusters(ClusterIdentifier=DWH_CLUSTER_IDENTIFIER)['Clusters'][0]
		DWH_ENDPOINT = myClusterProps['Endpoint']['Address']
		DWH_ROLE_ARN = myClusterProps['IamRoles'][0]['IamRoleArn']
		print("DWH_ENDPOINT :: ", DWH_ENDPOINT)
		print("DWH_ROLE_ARN :: ", DWH_ROLE_ARN)
		return myClusterProps, DWH_ENDPOINT, DWH_ROLE_ARN

	def open_ports(ec2, myClusterProps, DWH_PORT):
		"""
		Summary line. 
		Update clusters security group to allow access through redshift port

		Parameters: 
		arg1 : ec2 Object
		arg2 : Cluster Properties
		arg3 : Redshift Port

		Returns: 
		NONE
		"""  
		try:
			vpc = ec2.Vpc(id=myClusterProps['VpcId'])
			defaultSg = list(vpc.security_groups.all())[0]
			print(defaultSg)
			defaultSg.authorize_ingress(
				GroupName=defaultSg.group_name,
				CidrIp='0.0.0.0/0',
				IpProtocol='TCP',
				FromPort=int(DWH_PORT),
				ToPort=int(DWH_PORT)
			)
		except Exception as e:
			print(e)

	def main():
		initialize()

	if __name__ == "__main__":
		main()
```

## Amazon Athena

> Athena is a Serverless Query Service from Amazon based on Presto engine

Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.

Athena is easy to use. Simply point to your data in Amazon S3, define the schema, and start querying using standard SQL. Most results are delivered within seconds. With Athena, there’s no need for complex ETL jobs to prepare your data for analysis. This makes it easy for anyone with SQL skills to quickly analyze large-scale datasets.

![](https://user-images.githubusercontent.com/62965911/214001856-3d835c43-3eef-42a0-8e6f-ad1eca4e807f.png)

Athena is out-of-the-box integrated with AWS Glue Data Catalog, allowing you to create a unified metadata repository across various services, crawl data sources to discover schemas and populate your Catalog with new and modified table and partition definitions, and maintain schema versioning.

Presto (or PrestoDB) is an open source, distributed SQL query engine, designed from the ground up for fast analytic queries against data of any size. It supports both non-relational sources, such as the Hadoop Distributed File System (HDFS), Amazon S3, Cassandra, MongoDB, and HBase, and relational data sources such as MySQL, PostgreSQL, Amazon Redshift, Microsoft SQL Server, and Teradata.

Presto can query data where it is stored, without needing to move data into a separate analytics system. Query execution runs in parallel over a pure memory-based architecture, with most results returning in seconds. You’ll find it used by many well-known companies like Facebook, Airbnb, Netflix, Atlassian, and Nasdaq.

Amazon Athena lets you deploy Presto using the AWS Serverless platform, with no servers, virtual machines, or clusters to setup, manage, or tune. Simply point to your data at Amazon S3, define the schema, and start querying using the built-in query editor, or with your existing Business Intelligence (BI) tools. Athena automatically parallelizes your query, and dynamically scales resources for queries to run quickly. You pay only for the queries that you run.

Athena is "Managed Presto"

Athena doesn't support

1. DML Operations
2. Stored Procedures or MQT

### Benefits

#### Start querying instantly

**Serverless, no ETL**

Athena is serverless. You can quickly query your data without having to setup and manage any servers or data warehouses. Just point to your data in Amazon S3, define the schema, and start querying using the built-in query editor. Amazon Athena allows you to tap into all your data in S3 without the need to set up complex processes to extract, transform, and load the data (ETL).

#### Open, powerful, standard

**Built on Presto, runs standard SQL**

Amazon Athena uses Presto with ANSI SQL support and works with a variety of standard data formats, including CSV, JSON, ORC, Avro, and Parquet. Athena is ideal for interactive querying and can also handle complex analysis, including large joins, window functions, and arrays. Amazon Athena is highly available; and executes queries using compute resources across multiple facilities and multiple devices in each facility. Amazon Athena uses Amazon S3 as its underlying data store, making your data highly available and durable.

tip:

Presto: Released as open source by Facebook, it’s an open source distributed SQL query engine for running interactive analytic queries against data sources of all sizes. Presto allows querying data where it lives, including Hive, Cassandra, relational databases and file systems. It can perform queries on large data sets in a manner of seconds. It is independent of Hadoop but integrates with most of its tools, especially Hive to run SQL queries.

#### Pay per query

**Only pay for data scanned**

With Amazon Athena, you pay only for the queries that you run. You are charged $5 per terabyte scanned by your queries. You can save from 30% to 90% on your per-query costs and get better performance by compressing, partitioning, and converting your data into columnar formats. Athena queries data directly in Amazon S3. There are no additional storage charges beyond S3.

#### Fast, really fast

**Interactive performance even for large datasets**

With Amazon Athena, you don't have to worry about having enough compute resources to get fast, interactive query performance. Amazon Athena automatically executes queries in parallel, so most results come back within seconds.

### Athena Federation

Run federated queries against relational databases, data warehouses, object stores, and non-relational data stores. Federated SQL queries allow you to query the data in-place from wherever it resides. You can use familiar SQL to JOIN data across multiple data sources for quick analysis, and store results in Amazon S3 for subsequent use. Athena federated query also introduces a new Query Federation SDK that allows you to write your own data source connectors to query custom data stores.

Athena uses data source connectors that run on AWS Lambda to execute federated queries. A data source connector is a piece of code that can translate between your target data source and Athena. You can think of a connector as an extension of Athena's query engine. When a query is submitted against a data source, Athena invokes the corresponding connector to identify parts of the tables that need to be read, manages parallelism, and pushes down filter predicates. Based on the user submitting the query, connectors can provide or restrict access to specific data elements.

### Athena ACID Transactions

ACID transactions enable multiple users to concurrently and reliably add and delete Amazon S3 objects in an atomic manner, while isolating any existing queries by maintaining read consistency for queries against the data lake. Athena ACID transactions add single-table support for write, delete, update, and time travel operations to the Athena SQL data manipulation language (DML). You and multiple concurrent users can use Athena ACID transactions to make reliable, row-level modifications to Amazon S3 data. Athena transactions automatically manage locking semantics and coordination and do not require a custom record locking solution.

Athena ACID transactions and familiar SQL syntax simplify updates to your business and regulatory data. For example, to respond to a data erasure request, you can perform a SQL DELETE operation. To make manual record corrections, you can use a single UPDATE statement. To recover data that was recently deleted, you can issue time travel queries using a SELECT statement.

Athena supports read, time travel, and write queries for Apache Iceberg tables that use the Apache Parquet format for data and the AWS Glue catalog for their metastore.

### Watch these videos

- https://www.youtube.com/watch?v=whR4J5Arj78
- https://www.youtube.com/watch?v=M5ptG0YaqAs
- https://www.youtube.com/watch?v=1lzpeVV2hDQ

## BigQuery

BigQuery is server-less, highly scalable, and cost-effective Data warehouse designed for Google cloud Platform (GCP) to store and query petabytes of data. The query engine is capable of running SQL queries on terabytes of data in a matter of seconds, and petabytes in only minutes. You get this performance without having to manage any infrastructure and without having to create or rebuild indexes.

BigQuery supports standard SQL, so if you ever develop with relational database like Oracle, PostgreSQL, MySQL, Microsoft SQL Server, etc, it is easy to familiarize yourself with BigQuery. There are a few BigQuery functions to support modern-day requirements, and learning about them will make your job easier.

There is no infrastructure required. We don’t need to worry about the size of storage, number of processors, or memory allocation for processing query. BigQuery scales automatically to run query, and then release the resource when it is done. We don't even charged for memory or processor allocation.

Storing and querying massive datasets can be time consuming and expensive without the right hardware and infrastructure. BigQuery is a serverless, highly scalable [cloud data warehouse](https://cloud.google.com/solutions/bigquery-data-warehouse) that solves this problem by enabling super-fast SQL queries using the processing power of Google's infrastructure. Simply move your data into BigQuery and let us handle the hard work. You can control access to both the project and your data based on your business needs, such as giving others the ability to view or query your data.

### ETL, EL, and ELT

The traditional way to work with data warehouses is to start with an Extract, Transform, and Load (ETL) process, wherein raw data is extracted from its source location, transformed, and then loaded into the data warehouse. Indeed, BigQuery has a native, highly efficient columnar storage format9 that makes ETL an attractive methodology. The data pipeline, typically written in either Apache Beam or Apache Spark, extracts the necessary bits from the raw data (either streaming data or batch files), transforms what it has extracted to do any necessary cleanup or aggregation, and then loads it into BigQuery. The reference architecture for ETL into BigQuery uses Apache Beam pipelines executed on Cloud Dataflow and can handle both streaming and batch data using the same code.

Even though building an ETL pipeline in Apache Beam or Apache Spark tends to be quite common, it is possible to implement an ETL pipeline purely within BigQuery. Because BigQuery separates compute and storage, it is possible to run BigQuery SQL queries against CSV (or JSON or Avro) files that are stored as-is on Google Cloud Storage; this capability is called federated querying. You can take advantage of federated queries to extract the data using SQL queries against data stored in Google Cloud Storage, transform the data within those SQL queries, and then materialize the results into a BigQuery native table.

If transformation is not necessary, BigQuery can directly ingest standard formats like CSV, JSON, or Avro into its native storage—an EL (Extract and Load) workflow, if you will. The reason to end up with the data loaded into the data warehouse is that having the data in native storage provides the most efficient querying performance.

We strongly recommend that you design for an EL workflow if possible, and drop to an ETL workflow only if transformations are needed. If possible, do those transformations in SQL, and keep the entire ETL pipeline within BigQuery. If the transforms will be difficult to implement purely in SQL, or if the pipeline needs to stream data into BigQuery as it arrives, build an Apache Beam pipeline and have it executed in a serverless fashion using Cloud Dataflow. Another advantage of implementing ETL pipelines in Beam/Dataflow is that, because this is programmatic code, such pipelines integrate better with Continuous Integration (CI) and unit testing systems.

Besides the ETL and EL workflows, BigQuery makes it possible to do an Extract, Load, and Transform (ELT) workflow. The idea is to extract and load the raw data as-is and rely on BigQuery views to transform the data on the fly. An ELT workflow is particularly useful if the schema of the raw data is in flux. For example, you might still be carrying out exploratory work to determine whether a particular timestamp needs to be corrected for the local time zone. The ELT workflow is useful in prototyping and allows an organization to start deriving insights from the data without having to make potentially irreversible decisions too early.

### Where does BigQuery fit in the data lifecycle?

BigQuery is part of Google Cloud’s comprehensive data analytics platform that covers the entire analytics value chain including ingesting, processing, and storing data, followed by advanced analytics and collaboration. BigQuery is deeply integrated with GCP analytical and data processing offerings, allowing customers to set up an enterprise ready cloud-native data warehouse.

At each stage of the data lifecycle, GCP provides multiple services to manage data. This means customers can select a set of services tailored to their data and workflow.

![](https://user-images.githubusercontent.com/62965911/214002602-9d841ba2-318e-4688-aa9c-f524671590e3.png)

### Ingesting data into BigQuery

BigQuery supports several ways to ingest data into its managed storage. The specific ingestion method depends on the origin of the data. For example, some data sources in GCP, like Cloud Logging and Google Analytics, support direct exports to BigQuery.

BigQuery Data Transfer Service enables data transfer to BigQuery from Google SaaS apps (Google Ads, Cloud Storage), Amazon S3, and other data warehouses (Teradata, Redshift).

Streaming data, such as logs or IoT device data, can be written to BigQuery using Cloud Dataflow pipelines, Cloud Dataproc jobs, or directly using the BigQuery stream ingestion API.

You can access BigQuery by using the [Console](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui), [Web UI](https://console.cloud.google.com/bigquery?utm_source=bqui&utm_medium=link&utm_campaign=classic&project=cloud-solutions-group) or a [command-line tool](https://cloud.google.com/bigquery/docs/cli_tool) using a variety of [client libraries](https://cloud.google.com/bigquery/docs/reference/libraries) such as Java, .NET, or Python. There are also a variety of [solution providers](https://cloud.google.com/bigquery/providers) that you can use to interact with BigQuery.

### BigQuery Architecture

BigQuery’s serverless architecture decouples storage and compute and allows them to scale independently on demand. This structure offers both immense flexibility and cost controls for customers because they don’t need to keep their expensive compute resources up and running all the time. This is very different from traditional node-based cloud data warehouse solutions or on-premise massively parallel processing (MPP) systems. This approach also allows customers of any size to bring their data into the data warehouse and start analyzing their data using Standard SQL without worrying about database operations and system engineering.

![](https://user-images.githubusercontent.com/62965911/214002594-10e8a071-7a25-4bc7-94d1-57d111cc114a.png)

### Watch the video

Watch this video: https://www.youtube.com/watch?v=2UGA6b5MFI0

### Introducing BigQuery partitioning

There is one essential feature in BigQuery called a BigQuery partitioned table. A BigQuery partitioned table will logically divide the data in the BigQuery table by partitioning it into segments using a key.

There are three partition key options, outlined as follows:

- **Time-unit columns**: Based on a column containing **TIMESTAMP**, **DATE**, or **DATETIME** value
- **Ingestion time**: Based on the timestamp when BigQuery ingests data to the table
- **Integer range**: Based on a column containing the integer value

The most common scenario is using either a time-unit column or ingestion time, and even though you can partition up to an hourly granular level, the most common scenario is still partitioning at a daily level. This feature will benefit mainly cost and performance optimization, but other than those two factors, using BigQuery partitioned tables can help our load jobs.

Take a look at the next example.

We create a table with **PARTITION BY** (column), as follows:

```sql
CREATE TABLE example_table
(
val1 INT64,
val2  STRING,
date  DATE,
)
PARTITION BY (date);
```

Under the hood of BigQuery storage, the **example_table** table will be divided based on the **Date** column.

Every table record will be stored in a separate storage location. With this, it's theoretically the same as having multiple tables with the same schemas. But you don't need to worry about this, as BigQuery will handle this seamlessly. What you can do as a user is to access the table, and filter the table using the **partition** column, like this:

```sql
SELECT val1
FROM example_table
WHERE date = '2018-01-03';
```

The query will only access a partial amount of data from the table, which is the **val1** column at **2021-01-03**.

This is the idea of partitioned tables in BigQuery. The other main reason why people use partitioned tables in BigQuery is for cost optimization.

### Exploring a BigQuery Public Dataset

Storing and querying massive datasets can be time consuming and expensive without the right hardware and infrastructure. BigQuery is an enterprise data warehouse that solves this problem by enabling super-fast SQL queries using the processing power of Google's infrastructure. Simply move your data into BigQuery and let it handle the hard work. You can control access to both the project and your data based on your business needs, such as giving others the ability to view or query your data.

You access BigQuery through the Cloud Console, the command-line tool, or by making calls to the BigQuery REST API using a variety of client libraries such as Java, .NET, or Python. There are also a variety of third-party tools that you can use to interact with BigQuery, such as visualizing the data or loading the data. In this lab, you access BigQuery using the web UI.

You can use the BigQuery web UI in the Cloud Console as a visual interface to complete tasks like running queries, loading data, and exporting data. This hands-on lab shows you how to query tables in a public dataset and how to load sample data into BigQuery through the Cloud Console.

Given all the advantages of BigQuery, keep in mind that BigQuery is not a transactional database. BigQuery is not designed for millisecond query latency. It can process 1 TB of data in 5 seconds, but this doesn't mean you can process 1 MB of data in 0.0005 seconds. It is simply not designed for that purpose.

### Watch these videos

- Introduction to BigQuery - https://www.youtube.com/watch?v=xuuXXmvRLWQ
- Demo: Querying TB of data in seconds - https://www.youtube.com/watch?v=DAPiUo3sAFA
- Analytic window functions - https://www.youtube.com/watch?v=B6FhilGH6NA
- GIS functions - https://www.youtube.com/watch?v=9K2hTGv3SSc

### Connect to BigQuery from Google Colab

```py
from google.colab import auth
auth.authenticate_user()
print('Authenticated')

############################################

query = """SELECT
    source_year AS year,
    COUNT(is_male) AS birth_count
FROM `bigquery-public-data.samples.natality`
GROUP BY year
ORDER BY year DESC
LIMIT 15""" 

project_id = 'silken-psyxxx-xxxxxx'

import pandas as pd
df = pd.read_gbq(query, project_id=project_id, dialect='standard')
df.head()

from google.cloud import bigquery
client = bigquery.Client(project=project_id)
df = client.query(query).to_dataframe()
df.head()
```

## Snowflake

Snowflake is the Data Cloud that enables you to build data-intensive applications without operational burden, so you can focus on data and analytics instead of infrastructure management.

> Snowflake is the next big thing, and it is becoming a full-blown data ecosystem. With the level of scalability and efficiency in handling massive volumes of data and also with several new concepts in it, this is the right time to wrap your head around Snowflake and have it in your toolkit.

Snowflake started out because its founders understood and knew the truth about how users suffered with traditional relational OLAP solutions. Makes sense, they came from Oracle. They also understood how the cloud works. The founders didn't want to port an Oracle-like database over to the cloud as is. That would not solve the problems that the user base was experiencing. What were users suffering from: scale, performance, concurrency, and tons of expensive resources to keep the lights on! So they built Snowflake to solve these problems by taking all the good of a relational database platform and applying it to the cloud. The cloud allows for simple manifestation of environments with elasticity for size or scale.

Who competes with Snowflake directly? All cloud-based OLAP databases like: Redshift, Teradata, Oracle, Synapse, and Databricks. Yes, dare I say it Cloudera. Snowflake is starting to blur the lines a bit with Iceberg (Data Lake), SnowPark(Data Science/Data Engineering), Data Sharing/Marketplace(Third Party Data), and coming soon: Unistore (OLTP).

### Architecture

Even the improved traditional data platforms, especially those that were implemented on premises, couldn’t adequately address modern data problems or solve the long-standing scalability issue. The Snowflake team made the decision to take a unique approach. Rather than trying to incrementally improve or transform existing software architectures, they built an entirely new, modern data platform, just for the cloud, that allows multiple users to concurrently share live data.

The unique Snowflake design physically separates but logically integrates storage and compute along with providing services such as security and management. As we explore the many unique Snowflake features throughout the upcoming chapters, you’ll be able to see for yourself why the Snowflake architecture is the only architecture that can enable the Data Cloud.

The Snowflake hybrid-model architecture is composed of three layers, which are shown in the following image: the cloud services layer, the compute layer, and the data storage layer.

![](https://user-images.githubusercontent.com/62965911/214011273-c6c43e89-1b73-4d0f-9a59-4b42f3a9933e.png)

Watch this video: https://www.youtube.com/watch?v=ZOqmqfe8WvM

### Object hierarchy

![](https://user-images.githubusercontent.com/62965911/214011288-13335fff-954f-40fd-9b26-ea4cb231cfea.png)

### Snowpark

With Snowpark, developers can program using a familiar construct like the DataFrame, and bring in complex transformation logic through UDFs, and then execute directly against Snowflake’s processing engine, leveraging all of its performance and scalability characteristics in the Data Cloud.

Snowpark provides several benefits over how developers have designed and coded data-driven solutions in the past:

- Simplifies architecture and data pipelines by bringing different data users to the same data platform, and processes against the same data without moving it around.
- Accelerates data pipeline workloads by executing with performance, reliability, and scalability with Snowflake’s elastic performance engine.
- Eliminates maintenance and overhead with managed services and near-zero maintenance.
- Creates a single governance framework and a single set of policies to maintain by using a single platform.
- Provides a highly secure environment with administrators having full control over which libraries are allowed to execute inside the Java/Scala runtimes for Snowpark.

### Snowflake Data Ingestion/Loading and Extraction

![](https://user-images.githubusercontent.com/62965911/214011557-32f11577-390b-45e0-85b1-7ca33afdafee.png)

As the diagram above shows, Snowflake supports a wide range of use-cases including:

- Data File Loading: Which is the most common and highly efficient data loading method in Snowflake. This involves using SnowSQL to execute SQL commands to rapidly load data into a landing table. Using this technique it’s possible to quickly load terabytes of data, and this can be executed on a batch or micro-batch basis. Once the data files are held in a cloud stage (EG. S3 buckets), the COPY command can be used to load the data into Snowflake. For the majority of large volume batch data ingestion this is the most common method, and it’s normally good practice to size data files at around 100–250 megabytes of compressed data optionally breaking up very large data files were appropriate.
- Replication from on Premises Databases: Snowflake supports a range of data replication and ETL tools including HVR, Stitch, Fivetran and Qlik Replicate which will seamlessly replicate changes from operational or legacy warehouse systems with zero impact upon the source system. Equally there are a huge range of data integration tools which support Snowflake in addition to other database platforms and these can be used to extract and load data. Equally, some customers choose to write their own data extract routines and use the Data File Loading and COPY technique described above.
- Data Streaming: Options to stream data into Snowflake include using the Snowflake Kafka Connector to automatically ingest data directly from a Kafka topic as demonstrated by this video demonstration. Unlike the COPY command which needs a virtual warehouse, Snowpipe is an entirely serverless process, and Snowflake manages the operation entirely, scaling out the compute as needed. Equally, the option exists to simply trigger Snowpipe to automatically load data files when they arrive on cloud storage.
- Inserts using JDBC and ODBC: Although not the most efficient way to bulk load data into Snowflake (using COPY or Snowpipe is always faster and more efficient), the Snowflake JDBC and ODBC connectors are available in addition to a range of Connectors and Drivers including Python, Node.js and Go.
- Ingestion from a Data Lake: While Snowflake can be used to host a Data Lake, customers with an existing investment in a cloud data lake can make use of Snowflake External Tables to provide a transparent interface to data in the lake. From a Snowflake perspective, the data appears to be held in a read-only table, but the data is transparently read from the underlying files on cloud storage.
- Data Sharing: For customers with multiple Snowflake deployments, the Data Exchange provides a seamless way to share data across the globe. Using the underlying Snowflake Data Sharing technology, customers can query and join data in real time from multiple sources without the need to copy. Existing in-house data can also be enriched with additional attributes from externally sourced data using the Snowflake Data Marketplace.

**Batch/Bulk Data Ingestion**

1. Write/load the data into your staging location (S3 bucket)
2. Ingest the data into Snowflake in batches at frequent time intervals using:
   1. Snowflake copy commands scheduled using Snowflake tasks
   2. Trigger copy commands using Python/Glue/Airflow running at specified time intervals

**Real-time Data Ingestion**

1. Write/load the data into your staging location (S3 bucket) and ingest the data in real-time using:
   1. Snowpipe (continuous data ingestion)
   2. Airflow S3 sensors/triggers
2. Kafka-Snowflake Connector for real-time data ingestion

### SnowSQL

SnowSQL is the command line client for connecting to Snowflake to execute SQL queries and perform all DDL and DML operations, including loading data into and unloading data out of database tables. It is a modern command line tool designed for Snowflake Cloud data warehouse that is built on high security standards and has tight integration with Snowflake core architecture. It has very powerful scripting capability, and it can be further enhanced when used along with Python. Also, to upload/download any files to Snowflake internal stage you need SnowSql as put and get command work only with command line and not Web UI.

### SnowPipe

> Getting the volume and variety of today’s data into your data warehouse is paramount to obtain immediate, data-driven insight. Unfortunately, legacy data warehouses require batch-oriented loading and scheduling at off-peak times to avoid contention with the crucial needs of data analytics users. Snowpipe is a new data loading service for Snowflake that significantly improves the process of making data available for analysis.

Snowpipe is an event based data ingest tool. Snowpipe provides two main methods for triggering a data loading event. This trigger could be a cloud storage notification (i.e. AWS S3 ObjectCreated event) or by directly calling the Snowpipe insertFiles REST API.

When building data applications, your users count on seeing the latest. Stale data is less actionable and could lead to costly errors. That's why continuously generated data is essential. Snowflake provides a data loading tool to drive updates, ensuring your databases are accurate by updating tables in micro-batches.

### Best Practices for Data Engineering on Snowflake

1. Follow the standard ingestion pattern: This involves the multi-stage process of landing the data files in cloud storage and then loading to a landing table before transforming the data. Breaking the overall process into predefined steps makes it easier to orchestrate and test.
2. Retain history of raw data: Unless your data is sourced from a raw data lake, it makes sense to keep the raw data history which should ideally be stored using the [VARIANT](https://docs.snowflake.com/en/sql-reference/data-types-semistructured.html#variant) data type to benefit from automatic schema evolution. This means you have the option of truncating and re-processing data if bugs are found in the transformation pipeline and provides an excellent raw data source for Data Scientists. While you may not yet have any machine learning requirements, it's almost certain you will, if not now, then in the years to come. Keep in mind that Snowflake data storage is remarkably cheap, unlike on-premises solutions.
3. Use multiple data models: On-premises data storage was so expensive it was not feasible to store multiple copies of data with each using a different data model to match the need. However, using Snowflake it makes sense to store raw data history in either structured or variant format, cleaned and conformed data in [3rd Normal Form](https://dwbi1.wordpress.com/2011/03/28/storing-history-on-3rd-normal-form/) or using a [Data Vault](https://www.analytics.today/blog/when-should-i-use-data-vault) model and finally data ready for consumption in a [Kimball Dimensional Data model](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/). Each data model has unique benefits and storing the results of intermediate steps has huge architectural benefits, not least, the ability to reload and reprocess the data in the event of mistakes.
4. Use the right tool: As the quote above implies, if you only know one tool, you'll use it inappropriately. The decision should be based upon a range of factors including, the existing skill set in the team, whether you need rapid near real-time delivery, whether you're doing a once off data load or a regular repeating process. Be aware, Snowflake can natively handle a range of file formats including Avro, Parquet, ORC, JSON and CSV and there is extensive guidance on [loading data into Snowflake](https://docs.snowflake.com/en/user-guide-data-load.html#loading-data-into-snowflake) on the online documentation.
5. Use COPY or SNOWPIPE to load data: Around 80% of data loaded into a data warehouse is either ingested using a regular batch process or increasingly, immediately the data files arrive. By far the fastest, most cost efficient way to load data is using COPY and SNOWPIPE, so avoid the temptation to use other methods (for example queries against external tables) for regular data loads. Effectively, this is another example of *use the right tool*.
6. Avoid JDBC or ODBC for regular large data loads: Another *right tool* recommendation. While a JDBC or ODBC interface may be fine to load a few megabytes of data, these interfaces will not scale to the massive throughput of COPY and SNOWPIPE. Use them by all means, but not for large regular data loads.
7. Avoid Scanning Files: When using the COPY command to ingest data, use [partitioned staged data](https://docs.snowflake.com/en/user-guide/data-load-considerations-manage.html#partitioning-staged-data-files) files which is described as step 1 in the [Top 3 Snowflake Performance Tuning Tactics](https://www.analytics.today/blog/top-3-snowflake-performance-tuning-tactics). This reduces the effort of scanning large numbers of data files in cloud storage.
8. Choose a sensible Virtual Warehouse size: Another tip from the [Top 3 Snowflake Performance Tuning Tactics](https://www.analytics.today/blog/top-3-snowflake-performance-tuning-tactics), don't assume an X6-LARGE virtual warehouse will load massive data files any faster than an X-SMALL. Each physical file is loaded sequentially, and it therefore pays to follow the [Snowflake File Sizing Recommendations](https://docs.snowflake.com/en/user-guide/data-load-considerations-prepare.html#general-file-sizing-recommendations) and either split multi-gigabyte files into chunks of 100--250Mb or load multiple concurrent data files in parallel.
9. Ensure 3rd party tools push down: ETL tools like Ab Initio, Talend and Informatica were originally designed to extract data from source systems into an ETL server, transform the data and write them to the warehouse. As Snowflake can draw upon massive on-demand compute resources and automatically scale out, it makes no sense to use have data copied to an external server. Instead, use the ELT (Extract, Load and Transform) method, and ensure the tools generate and execute SQL statements on Snowflake to maximise throughput and reduce costs.
10. Transform data in Steps: A common mistake by inexperienced data engineers is to write huge SQL statements that join, summarise and process lots of tables in the mistaken belief this is an efficient way of working. In reality the code becomes over-complex and difficult to maintain and worst still, often performs poorly. Instead, break the transformation pipeline into multiple steps and write results to intermediate tables. This makes it easier to test intermediate results, simplifies the code and often produces simple SQL code that runs faster.
11. Use Transient tables for intermediate results: During a complex ELT pipeline, write intermediate results to a [transient table](https://docs.snowflake.com/en/user-guide/tables-temp-transient.html#transient-tables) which may be truncated prior to the next load. This reduces the time-travel storage to just one day and avoids an additional 7 days of fail-safe storage. By all means use [temporary tables](https://docs.snowflake.com/en/user-guide/tables-temp-transient.html#temporary-tables) if sensible, but it's often helpful to check the results of intermediate steps in a complex ELT pipeline.
12. Avoid row-by-row processing: Modern analytics platforms like Snowflake are designed to ingest, process and analyse billions of rows at amazing speed using simple SQL statements which act upon the data *set-at-a-time*. However, people tend to think in terms of row-by-row processing and this sometimes leads to programming loops which fetch and update rows, one at a time. Be aware, [row-by-row processing](https://www.sqlskills.com/blogs/paul/reconciling-set-based-operations-with-row-by-row-iterative-processing/) is by far the single biggest way of killing query performance. Use SQL statements to process all table entries at a time and avoid row-by-row processing at all cost.
13. Use Query Tags: When you start any multi-step transformation task set the [session query tag using](https://docs.snowflake.com/en/sql-reference/sql/alter-session.html#alter-session): ALTER SESSION SET QUERY_TAG = 'XXXXXX' and ALTER SESSION UNSET QUERY_TAG. This stamps every SQL statement until reset with an identifier and is invaluable to System Administrators. As every SQL statement (and QUERY_TAG) is recorded in the [QUERY_HISTORY](https://docs.snowflake.com/en/sql-reference/account-usage/query_history.html#query-history-view) view you can then track the job performance over time. This can be used to quickly identify when a task change has resulted in poor performance, identify inefficient transformation jobs or indicate when a job would be better executed on a larger or smaller warehouse.
14. Keep it Simple: Probably the best indicator of an experienced data engineer is the value they place on *simplicity*. You can always make a job 10% faster or generic or more elegant and it *may* be beneficial but it's *always* beneficial to simplify a solution. Simple solutions are easier to understand, easier to diagnose problems and are therefore easier to maintain. Around 50% of the performance challenges I face are difficult to resolve because the solution is a single, monolithic complex block of code. The first thing I do, is to break down the solution into steps and only then identify the root cause.

Watch this video: https://www.youtube.com/watch?v=jKJTqfvwFOg

## Labs

1. [Copying Data from S3 into Redshift](02-storage/warehouses/lab-redshift-copy-from-s3/)
2. [Redshift with Python](02-storage/warehouses/lab-redshift-python/)
3. [Implement a slowly changing dimension in Amazon Redshift](02-storage/warehouses/lab-redshift-scd/)
4. [Taxi Data Process and Save to Redshift using AWS Wrangler](02-storage/warehouses/lab-redshift-taxi/)
5. [Sales Analytics with Redhshift](02-storage/warehouses/project-redshift-sale/)
6. [Building Federated Query System using Amazon Athena](02-storage/warehouses/project-athena-federated/)
7. [Getting Started with Snowflake](02-storage/warehouses/lab-snowflake-getting-started/)
8. [Snowflake with Python](02-storage/warehouses/lab-snowflake-connect-python/)
9. [Snowpark Churn](02-storage/warehouses/lab-snowpark-churn/)
10. [Snowpark Streamlit](02-storage/warehouses/lab-snowpark-streamlit/)
11. [Snowflake SnowSQL](02-storage/warehouses/lab-snowflake-snowsql/)
12. [Using BigQuery to do analysis](02-storage/warehouses/lab-bigquery-analysis/)
13. [Bigquery basics command line operations](02-storage/warehouses/lab-bigquery-commandline/)
14. [Creating a Data Warehouse Through Joins and Unions](02-storage/warehouses/lab-bigquery-data-warehousing/)
15. [Build and Optimize Data Warehouses with BigQuery](02-storage/warehouses/lab-bigquery-optimization/)
16. [Optimizing your BigQuery Queries for Performance](02-storage/warehouses/lab-bigquery-query-optimization/)
17. [Building a BigQuery Data Warehouse](02-storage/warehouses/lab-biqeury-building-warehouse/)
18. [Predict Visitor Purchases with a Classification Model in BigQuery ML](02-storage/warehouses/lab-bigquery-ml/)
19. [NYC Cab Prediction Model in BigQuery ML](02-storage/warehouses/lab-bigquery-nyctaxi/)

## Interview Questions

[Read here](02-storage/warehouses/interview-questions.md)

## Explore Further

1. Transactional databases versus data warehouses - https://www.youtube.com/watch?v=GIAEAzoclgU
2. The modern data warehouse - https://www.youtube.com/watch?v=EsvenuliSsc
