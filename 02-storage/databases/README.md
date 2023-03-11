# Databases

## Postgres

Picking the right database management system is a difficult task due to the vast number of options on the market. Depending on the business model, you can pick a commercial database or an open source database with commercial support. In addition to this, there are several technical and non-technical factors to assess. When it comes to picking a relational database management system, PostgreSQL stands at the top for several reasons. The PostgreSQL slogan, "*The world's most advanced open source database*," emphasizes the sophistication of its features and the high degree of community confidence.

PostgreSQL is an open source object relational database management system. It competes with major relational databases such as Oracle, MySQL, and SQL Server. Its licensing model allows commercial use without any limitations and there are a lot of companies offering commercial support of PostgreSQL. For this reason, start-ups often favor PostgreSQL. Due to its rich extensions, it is often used for research purposes. PostgreSQL code is also a base for a few open source and commercial database solutions such as Greenplum and Amazon Redshift.

PostgreSQL runs on most modern operating systems, including Windows, Mac, and Linux flavors. Its installation and configuration is fairly easy, as it is supported by most packaging tools, such as apt, yum, or Homebrew. Also, there are interactive installers for Windows and macOS. There are extensions and tools that help to manage and monitor PostgreSQL servers, such as pgAdmin and psql. PostgreSQL complies with ANSI SQL standards, which makes it easy to learn and use for database developers and database administrators. Other than this, there are a lot of resources helping developers to learn and troubleshoot PostgreSQL; it has very good and well-structured documentation and a very active and organized community.

PostgreSQL can be used for both **online transaction processing** (**OLTP**) and **online analytical processing** (**OLAP**) applications. In addition to that, PostgreSQL supports both pessimistic and optimistic concurrency control, and the locking behavior can be chosen based on the use case. PostgreSQL provides a lot of features that help to handle very large amounts of data efficiently, such as partitioning and parallel execution. PostgreSQL is scalable thanks to its replication capabilities. All this makes PostgreSQL attractive because it can be used to set up highly available and performant data management solutions.

### Use Cases

#### Financial industry

PostgreSQL is highly suitable for the financial industry. PostgreSQL is fully ACID compliant and therefore ideal for OLTP (Online Transaction Processing) workloads. However, PostgreSQL is not only a good choice for its superior OLTP capabilities – it is also a highly capable analytical database and can be integrated nicely with mathematical software such as Matlab and R.

PostgreSQL can be used for a variety of tasks and operations.

#### Government GIS data

PostgreSQL is not only a tool for the financial industry – there is also a really powerful GIS extension called “PostGIS” which provides hundreds of functions to process geometric data in various formats. PostGIS is highly standard compliant and is one of the de-facto standards in the Open Source GIS world.

In combination with QGIS or GeoServer the Open Source community provides powerful means to handle geodata. Check out website on PostGIS to find out more about our geodata services.

#### Manufacturing

Many world class industrial manufacturers use PostgreSQL to speed up innovation and to drive growth boost through customer-centric processes, and optimize supply chain performance using PostgreSQL as a storage backend. PostgreSQL is a reliable, long term data stores and offers you reliable storage at low costs.

In industrial manufacturing reliability is everything. If a production site is down due to a failure it can easily cost millions. Therefore PostgreSQL is the ideal choice because it can be configured for automatic failover, full redundancy, and almost zero downtime upgrades.

PostgreSQL has gained a lot of momentum in manufacturing recently because Oracle has changed its license policy in a way that it has become hard for many companies to sustain high license costs.

#### Web technology and NoSQL workloads

Modern websites might require thousands or even hundreds of thousands of requests per second to serve your customers. Scalability can be a major issue and the PostgreSQL community has worked hard to address those scalability questions in the past couple of years.

PostgreSQL works fine with all modern web frameworks including but not limited to: Django (Python), node.js (JavaScript), Hibernate (Java), Ruby on rails, PHP, and a lot more. Due to PostgreSQL’s replication capabilities, websites can easily be scaled out to as many database servers as you need.

PostgreSQL is not just a relational database – it can also serve as a NoSQL-style data store. There is no need to choose between the relational and the document oriented world. You can have both in a single product.

#### Scientific data

Research and scientific projects can generate terabytes of data, which have to be handled in the most beneficial and most efficient way possible. PostgreSQL has wonderful analytical capabilities and offers a powerful SQL engine, which makes processing large amounts of data a real joy.

On top of that PostgreSQL can easily be extended. You can write your own aggregation functions and you can come up with your own business logic in the database. By bringing the algorithms close to your data, a lot more efficiency can be achieved than by performing all operations on the application level.

### Customer Success Stories

**Apple**

The tech giant from Cupertino, California has been betting on PostgreSQL for a long time. It uses PostgreSQL in company databases – but that’s not all.

In 2010, Apple replaced MySQL with Postgres as an embedded database in the OS X Lion release. In earlier versions of the server software, Apple focused on Oracle’s database solution. What prompted the change? Product quality and a fear of changes in Oracle’s MySQL licensing. Since then, Apple systems support PostgreSQL. Currently, it’s the default database on macOS Server since OS X Server version 10.7. PostgreSQL is also available in the App Store.

**IMDB**

This site is more than just a list of movies. It’s the world's largest online database on films, actors, directors, screenwriters, film agents, and other people associated with the industry.

The Internet Movie DataBase has been around since 1990 and currently contains nearly 6 million movie titles and over 100 million entries. But it’s also a huge community of people evaluating and discussing films. This is a giant amount of data. A lot of it is processed in PostgreSQL. What's more, users can analyze the data themselves; IMDB provides it for free for personal and non-commercial use. Interested? Then see this page about IMDB datasets. I also recommend using PostgreSQL to analyze this data.

**Instagram**

More than just a social network for sharing photos, Instagram has affected global culture. It’s responsible for the selfie spread. Many people cannot imagine having a meal at a restaurant and not sharing the photo with their friends.

According to Instagram representatives, the number of platform users exceeded a billion last year. This is one-seventh of all humanity. This mass of people publishes nearly 50 million photos a day. Football star Cristiano Ronaldo has over 200 million followers; singer Ariana Grande has over 180 million. Talk about huge databases!

Instagram uses many RDBMSs, but PostgreSQL and Cassandra were chosen for the main tasks. The goal was to reduce delay and ensure users can easily and comfortably use the application.

**Reddit**

Reddit is a social news website where people can exchange opinions and knowledge. It has about 174 million registered users. Alexa ranked Reddit as one of the 25 most popular websites in the world.

Reddit uses PostgreSQL in two different ways. First of all, there’s the ThingDB model. This is the basic Postgres mechanism for storing data for most objects (e.g. links, comments, accounts, and subreddits). In more traditional relational databases based on PostgreSQL, Reddit maintains and analyzes traffic statistics and information on transactions, ads sales, and subscriptions.

**Skype**

This application probably does not need an introduction – it’s one of the most popular instant messaging and video calling services in the world. According to various estimates, Skype is used by nearly 100 million people each month; 40 million people use it daily.

Because of COVID-19, this number has recently increased significantly. In official announcements, Skype representatives have said they use PostgreSQL as their main tool for working with databases. It is used to store user, chat, and call data. The connections are directed to an external VOIP service running on Asterisk, which also uses PostgreSQL.

Skype developers often emphasize Postgres’ ease of optimization, flexibility, and efficiency. Here you can read more about how Skype uses database tools.

**Spotify**

Has it been awhile since you’ve listened to your favorite Metallica songs? Or maybe you're interested in what your friends are listening to. Services like iTunes, Tidal, and Spotify have changed the way we approach music. We don’t have to wait for artists’ next albums to arrive at our local store; they appear in the catalog and subscribers have instant access to them (and 50 million other songs).

In addition to music, Spotify also has podcasts and radio programs for its 271 million monthly users. How do they manage all that info? Using databases. As we read on the official Spotify blog, the application infrastructure uses PostgreSQL and Cassandra.

**Twitch**

This is one of the most popular video streaming platforms. It is mainly used by gamers and e-sport players. Nearly 15 million people log in to the site every day.

The Twitch platform is based on around 125 databases. The vast majority of them are managed using PostgreSQL, including user, broadcast data, and backup databases. Interested in how Twitch uses PostgreSQL? Read this post on their blog.

**International Space Station**

Yes, PostgreSQL has also reached space. This is not the first time that NASA has opted for open source solutions. They worked well on other projects, so why wouldn't they be in orbit?

The world learned about everything from this small mention on the PostgreSQL.org mailing group. I think that reading such a request triggers emotions even for the most experienced programmers. NASA needed to implement Nagios on the Space Station and they wanted to use PostgreSQL to store the data on the orbit and then replicate that database on the ground.

If there’s such a thing as a cool job, working with guys who fly in space and perhaps know if aliens are out there is one of them.

If there’s such a thing as a cool job, working with guys who fly in space and perhaps know if aliens are out there is one of them.

### Setup Postgres

```bash
pip install psycopg2-binary
```

Watch this video: https://www.youtube.com/watch?v=EZAa0LSxPPU

#### Setup RDS Postgres

Watch this video: https://www.youtube.com/watch?v=t_Q5NTtYbx4

### How to connect to Postgres

1. Connect via VS-Code SQLTools Extension
2. Connect via DBeaver
3. Connect via pgpAdmin
4. Connect via CLI
5. Connect via Python

### Makefile

```Makefile
connect:
	psql --host=<> --port=5432 --username=<> --dbname=<>
	psql -h localhost -p 5432 -d <db_name> -U <user_name> -W
	PGPASSWORD=student createdb -h 127.0.0.1 -U student pagila
	PGPASSWORD=student psql -q -h 127.0.0.1 -U student -d pagila -f Data/pagila-schema.sql

connect_database:
	\connect <database_name>;

create_dump:
	pg_dump --host=<hostname> --port=3306  --user=<username> --password --dbname=database_name --table=table_name --format=plain > data-to-be-loaded.sql
	pg_dump --host=<hostname> --port=3306  --user=<username> --password --dbname=database_name --table=table_name --format=tar > data-to-be-loaded.tar

restore_dump:
	\include data-to-be-loaded.sql;
	pg_restore --user=<username> --host=<hostname> --password --dbname=<database_name> < data-to-be-loaded.tar

describe_table:
	\d <table_name>

restart_service_mac:
	brew services restart postgresql

import_data_from_sql:
	\i path_of_your_dump_file.sql

import_data_from_csv:
	\copy drivers(id, first_name, last_name)
	from './data/drivers.csv'
	with delimiter ','
	csv header;

psql_general:
	CREATE DATABASE <db_name>;
	CREATE USER <user_name> WITH ENCRYPTED PASSWORD '<password>';
	GRANT ALL ON DATABASE <db_name> TO <user_name>;
	GRANT pg_read_server_files TO <user_name>;
	\q

connect_py:
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

	creds = get_secret("wysde")
	USERNAME = creds["RDS_POSTGRES_USERNAME"]
	PASSWORD = creds["RDS_POSTGRES_PASSWORD"]
	HOST = creds["RDS_POSTGRES_HOST"]
	DATABASE = 'sparsh'

	conn_str = 'postgresql://{0}:{1}@{2}/{3}'.format(USERNAME, PASSWORD, HOST, DATABASE)

	%config SqlMagic.autopandas=True
	%config SqlMagic.displaycon=False
	%config SqlMagic.feedback=False
	%config SqlMagic.displaylimit=5
	%reload_ext sql
	%sql {conn_str}

connect_and_create_db_py:
	import os
	import pandas as pd
	from sqlalchemy import create_engine

	POSTGRES_USERNAME = ''
	POSTGRES_PASSWORD = ''
	POSTGRES_ENDPOINT = ''
	POSTGRES_DATABASE = ''

	CONN = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_ENDPOINT}:5432/{POSTGRES_DATABASE}"
	engine = create_engine(CONN)
	conn = engine.connect()

	try: 
		conn.execution_options(isolation_level="AUTOCOMMIT").execute("CREATE DATABASE mydb")
	except Exception as e:
		print(e)
	finally:
		conn.close()

load_data_py:
	import psycopg2
	import pandas as pd
	import sqlalchemy as sa

	conn = psycopg2.connect(f"host=database-1.us-east-1.rds.amazonaws.com dbname=template1 user=postgres password=")
	conn.set_session(autocommit=True)
	cur = conn.cursor()
	cur.execute("DROP DATABASE IF EXISTS stations WITH (FORCE)")
	cur.execute("CREATE DATABASE stations WITH ENCODING 'utf8' TEMPLATE template0")
	conn.close()   

	conn = psycopg2.connect(f"host=database-1.us-east-1.rds.amazonaws.com dbname=stations user=postgres password=")
	DDL = """
	CREATE TABLE stations (
	stop_id INTEGER PRIMARY KEY,
	direction_id VARCHAR(1) NOT NULL,
	stop_name VARCHAR(70) NOT NULL,
	station_name VARCHAR(70) NOT NULL,
	station_descriptive_name VARCHAR(200) NOT NULL,
	station_id INTEGER NOT NULL,
	"order" INTEGER,
	red BOOLEAN NOT NULL,
	blue BOOLEAN NOT NULL,
	green BOOLEAN NOT NULL
	);
	"""
	cur = conn.cursor()
	cur.execute(DDL)
	conn.commit()
	conn.close()

	df = pd.read_csv("data.csv")
	db_url = 'postgresql://<username>:<password>@database-1.us-east-1.rds.amazonaws.com:5432/stations'
	engine = sa.create_engine(db_url)
	df.to_sql('stations', engine, method='multi', index=False, if_exists='append')
```

### Commands

```sql
CREATE USER airflow WITH PASSWORD 'airflow' CREATEDB;
CREATE DATABASE airflow
    WITH 
    OWNER = airflow
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE USER warehouse WITH PASSWORD 'warehouse' CREATEDB;
CREATE DATABASE warehouse
    WITH 
    OWNER = warehouse
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE USER superset WITH PASSWORD 'superset' CREATEDB;
CREATE DATABASE superset
    WITH 
    OWNER = superset
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE USER redash WITH PASSWORD 'redash' CREATEDB;
CREATE DATABASE redash
    WITH 
    OWNER = redash
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
```

## MySQL

```Makefile
start:
	start_mysql

connect:
	mysql --host=<hostname> --port=3306  --user=<username> --password

create_database:
	create database <dbname>;

create_table:
	create table mytbl(ts datetime, vid int, type char(15), pid smallint);

disconnect:
	exit

create_dump:
	mysqldump --host=<hostname> --port=3306  --user=<username> --password <database_name> <table_name> > data-to-be-loaded.sql

restore_dump:
	source data-to-be-loaded.sql;
	mysql --host=<hostname> --port=3306  --user=<username> --password <database_name> < data-to-be-loaded.sql

show_tables:
	SHOW FULL TABLES WHERE table_type = 'BASE TABLE';

describe_table:
	describe <table_name>

connect_python:
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
	creds = get_secret("wysde")
	USERNAME = creds["RDS_MYSQL_USERNAME"]
	PASSWORD = creds["RDS_MYSQL_PASSWORD"]
	HOST = creds["RDS_MYSQL_HOST"]
	DATABASE = 'sparsh'
	conn_str = 'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(USERNAME, PASSWORD, HOST, DATABASE)
	%config SqlMagic.autopandas=True
	%config SqlMagic.displaycon=False
	%config SqlMagic.feedback=False
	%config SqlMagic.displaylimit=5
	%reload_ext sql
	%sql {conn_str}

ddl_ingest_python:
	TABLE = "table_to_be_loaded"
	df = pd.read_csv(f"./data/{TABLE}.csv")
	print(pd.io.sql.get_schema(df, name=TABLE, con=conn))
	df.to_csv(f"./data/{TABLE}.csv", index=False)
	echo mysqlimport --local \
		--compress \
		--user={USERNAME} \
		--password \
		--host={HOST} \
		--ignore-lines=1 \
		--fields-terminated-by=\',\' {DATABASE} data/{TABLE}.csv
```

### Explore further

1. https://learnsql.com/blog/companies-that-use-postgresql-in-business/
2. https://www.cybertec-postgresql.com/en/postgresql-overview/solutions-who-uses-postgresql/
3. [10 Essential PSQL Commands For Data Engineers](https://towardsdatascience.com/10-essential-psql-commands-for-data-engineers-c1ea42279160)
4. [Building Your Data Warehouse On Top Of PostgreSQL](https://www.dataengineeringpodcast.com/postgresql-data-warehouse-episode-186/)

## SQLite

SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world.

## DuckDB

DuckDB is a really interesting project aimed at being a SQLite style database with a focus on OLAP (online analytical processing). OLAP is typically associated with analytics due to its design catering to long running queries over large datasets or aggregations over joins of multiple tables with vast amounts of data. DuckDB is an open source project developed by the non-profit organization, DuckDB Labs based in Amsterdam, Netherlands and takes donations and contracting work around their database.

Watch this video: https://youtu.be/5GewuzicW7k

## GCP CloudSQL

CloudSQL is a fully managed relational database service for MySQL, PostgreSQL, and SQL Server with rich extension collections, configuration flags, and developer ecosystems.

## Azure SQL Databases

Azure SQL Database, a fundamental relational database as a service offered in Azure, acts as a source, destination, or even as an intermediate storage layer in data engineering pipelines. Azure SQL Database can be used to consolidate data coming from several relational data sources and build mini data warehouses or data marts. With the introduction of Hyperscale tier in Azure SQL Database, the capacity of Azure SQL Database has increased leaps and bounds too. Securing Azure SQL Database is also pivotal in protecting access to the database. Having a strong understanding of Azure SQL Database's capabilities and security options is essential for any data engineer.

## Labs

1. [CSV Data Ingestion into MySQL](02-storage/databases/lab-mysql-data-ingestion/)
2. [SQLite Basics](02-storage/databases/lab-sqlite-basics/)
3. [Getting Started with Postgres](02-storage/databases/lab-postgres-getting-started/)
4. [Use bash shell commands to extract, transform and load data into Postgre](02-storage/databases/lab-postgres-bash-etl/)
5. [Building a Database for Crime Reports using Postgres](02-storage/databases/lab-postgres-crime-reports/)
6. [Generate Trips Data using Stored Procedure](02-storage/databases/lab-postgres-trips-stored-procedure/)
7. [Police API Data Engineering Task](02-storage/databases/lab-mysql-police-api-etl/)
8. [Loading Taxi Data into Google Cloud SQL](02-storage/databases/lab-gcp-cloudsql-nyctaxi/)
9. [Configuring and Securing Azure SQL Database](02-storage/databases/lab-azure-sql-securing-databases/)
10. [db2 BookShop and PetSale Data Ingestion and Stored Procedure](02-storage/databases/db2/lab-dbt-bookshop-petsale-data-ingestion/)
11. [OLAP Analytics on bank, TPCH and NYC Taxi datasets using DuckDB](02-storage/databases/duckdb/lab-analytics-bank-tpch-nyctaxi/)
12. [Extract from Hipolabs API, Transform and Load into SQLite database](02-storage/databases/lab-sqlite-hipolabs-api/)

## Interview Questions

### What is a relational database?

Answer: A relational database is a type of database that stores data in tables. Tables are composed of rows and columns. Data in relational databases is organized into relations, which are similar to tables.

### What is data skewness?

Answer: Data skewness is a statistical phenomenon that occurs when the distribution of a dataset is not symmetrical. Data skew can impact the performance of data processing and analysis.

### What are the different file storage formats and how do you know when to use them?

Answer: The different file storage formats are text, CSV, JSON, XML, and binary. Each file storage format has its own advantages and disadvantages. The format that you choose should be based on the needs of your project.

### Describe a time you had difficulty merging data. How did you solve this issue?

Answer: I once had difficulty merging data because the data sets were in different formats. I solved this issue by using a data transformation tool to convert the data into the same format.

### How would you design a data warehouse given limited resources?

Answer: I would design a data warehouse by considering the needs of the business. I would also consider the size of the data sets and the resources that are available. I would then choose the appropriate storage format and file structure.

### What is a columnar database? How is it different from a relational database?

Answer: A columnar database is a type of database that stores data in columns. Columnar databases are designed for data warehousing and data analysis. They are different from relational databases because they are optimized for query performance.

### What are the different types of SQL statements?

Answer: The different types of SQL statements are DDL, DML, and DCL.

- DDL statements are used to create and modify tables.
- DML statements are used to query and update data.
- DCL statements are used to control access to the database.

### How would you normalize a database?

Answer: To normalize a database, I would first identify the functional dependencies. I would then create a table for each functional dependency. I would then create relationships between the tables.

### What is your experience with Data Modeling?

Answer: I have experience working with Data Modeling. I have used Data Modeling to create conceptual, logical, and physical data models. I have also used Data Modeling to reverse engineer data models.

### What is your experience with Data Mining?

Answer: I have experience working with Data Mining. I have used Data Mining to discover hidden patterns and trends in data.
