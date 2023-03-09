# Databricks

Databricks is a platform that enables enterprises to quickly build their Data Lakehouse infrastructure and enable all data personas – data engineers, data scientists, and business intelligence personnel – in their organization to extract and deliver insights from the data. The platform provides a curated experience for each data persona, enabling them to execute their daily workflows. The foundational technologies that enable these experiences are open source – Apache Spark, Delta lake, MLflow, and more.

Databricks was founded in 2013 by seven researchers at the University of California, Berkeley.

This was the time when the world was learning how the **Meta, Amazon, Netflix, Google, and Apple** (**MANGA**) companies had built their success by scaling up their use of AI techniques in all aspects of their operations. Of course, they could do this because they invested heavily in talent and infrastructure to build their data and AI systems. Databricks was founded with the mission to enable everyone else to do the same – use data and AI in service of their business, irrespective of their size, scale, or technological prowess.

The mission was to democratize AI. What started as a simple platform, leveraging the open source technologies that the co-founders of Databricks had created, has now evolved into the lakehouse platform, which unifies data, analytics, and AI in one place.

Databricks was born out of the frustration of the Hadoop vendors and two Apache projects: Hadoop and Spark. Databricks is the commercial entity of Apache Spark. Apache Spark was born out of frustration with Apache Hadoop and the commercial vendors where only one is left: Cloudera. Hadoop does not do well with concurrency and it has huge latency issues. Apache MapReduce is dead and was replaced with Apache Spark to remedy these limitations. Apache Spark has problems of its own and thus Databricks was born to take Spark to Enterprise.

![](https://user-images.githubusercontent.com/62965911/214503488-88a696f6-8e78-495f-813f-4a95ef7cfe7e.png)

![dbr_arch](https://user-images.githubusercontent.com/62965911/215255929-f0b96773-f515-4c3c-afd7-8e1d254a5317.png)

## Databricks Case Studies

Data teams across the world are using Databricks to solve the toughest data problems. Every Databricks success story brings a unique set of challenges and new learning for architects and data professionals. Databricks can be used as a transformation layer, a real-time streaming engine, or a solution for machine learning and advanced analytics. In this note, we will look at several real-world case study examples and learn how Databricks is used to help drive innovation across various industries around the world.

In this note, we will learn about use cases from the following industries:

- Learning case studies from the manufacturing industry
- Learning case studies from the media and entertainment industry
- Learning case studies from the retail and FMCG industry
- Learning case studies from the pharmaceutical industry
- Learning case studies from the e-commerce industry
- Learning case studies from the logistics and supply chain industry

Let's begin with the case studies from the manufacturing industry.

**Learning case studies from the manufacturing industry**

Data and statistical analysis help manufacturing organizations make accurate decisions and streamline processes. This makes manufacturing processes become more efficient and prevents unwanted losses for the organizations.

### Case study 1 -- leading automobile manufacturing company

An organization was looking for a cloud-scale analytics platform to support growing **online analytical processing** (**OLAP**) requirements, a modernized visualization capability to support business intelligence needs, and advanced analytical and **artificial intelligence** (**AI**) solutions for existing data.

The proposed solution architecture was as follows:

- Data from the Oracle database and flat files was extracted using Azure Data Factory and loaded into Azure Data Lake.
- Azure Databricks was used to transform the historical data. Then, the data would be loaded into the Azure Synapse Data Warehouse.
- A lead scoring system was built using Azure Databricks for predictive analytics.
- Data modeling was performed in Power BI, and several reports and dashboards were built using the historical and predicted data.

The solution architecture is depicted in the following diagram:

![B17782_08_01](https://user-images.githubusercontent.com/62965911/218824377-b7ed8bff-881f-4a64-b264-68e33b9c887e.jpg)

Figure -- Solution architecture diagram for the leading automobile manufacturing company

Next, we will learn about another automobile manufacturing case study.

### Case study 2 -- international automobile manufacturing giant

A automobile manufacturing giant faced several challenges in its data journey. They were previously using an on-premises SQL Server that had performance limitations, leading to access to refreshed data being reduced. Other significant issues that were faced by the organization included scalability issues, the absence of real-time data analytics, lower utilization of Power BI premium features, and limited self-service analytics. The proposed solution architecture was as follows:

- Data from Microsoft Dynamics 365 and the on-premises database was pushed to Azure Data Lake.
- Azure Databricks was used for parallel and in-memory data cleaning and massaging.
- A data model was built using **Azure Synapse Analytics**, thereby helping to access data with minimal data preparation activities and an efficient mechanism to manage large volumes of data.
- Power BI reports and dashboards were built on top of the data in Azure Synapse Analytics.

The solution architecture is depicted in the following diagram:

![B17782_08_02](https://user-images.githubusercontent.com/62965911/218824387-1adf3ad4-a827-4e2c-9284-9ca4d5a99812.jpg)

Figure -- Solution architecture diagram for the international automobile manufacturing giant

Next, we will learn about a chemical corporate case study.

### Case study 3 -- graph search in a chemical corporate firm

A chemical corporate firm was having an issue with the chemical composition of mixtures and products and their test results. They were also struggling with the sales data of a particular chemical. The scenario was focused on querying data and information for a UK-based firm that stores production data in various stages and forms that have complex parent-child relationships. The major task was to create metadata and relationships in the data so that it could be queried using a graph database, without utilizing much of its compute power, as well within the time constraint of 5 seconds. The proposed solution architecture was as follows:

- The data from CSV files and the real-time feed from Azure Event Hubs were imported, cleaned, and transformed using Azure Databricks.
- After forming relationships and transforming data into graphs in Azure Databricks, data was pushed into Azure Cosmos DB.
- The data was queried using the Gremlin API of Azure Cosmos Graph and questions such as "*In the last 3 years, who did we sell materials to and in what quantity?*" and "*What products contain chemical X or its derived chemical and in what quantity?*" were answered.
- Power BI was used to visualize this real-time streaming data for recording and information scoring purposes.

The solution architecture is depicted in the following diagram:

![B17782_08_03_new](https://user-images.githubusercontent.com/62965911/218824391-abf2761f-b9b8-41d3-9210-afaa13cc7519.jpg)

Figure -- Solution architecture diagram for the chemical corporate firm

Next, we will learn about a case study from a leading medical equipment manufacturer.

### Case study 4 -- real-time loyalty engine for a leading medical equipment manufacturer

This case study is about capturing customer behaviors and calculating loyalty points and tiers for a customer in near-real time. There were about five different sources of data where these behaviors were tracked that needed to be pulled into **Azure Data Lake** in real time, calculations done and stored (history tracking enabled), and then the calculated information (summary and details) was passed to a data hub (Cosmos DB) that would eventually be consumed by the presentation layer.

The idea was to deliver this on the Azure platform with Azure Databricks being the real-time processing engine. Currently, the engine is live with one source of behavior -- that is, *Salesforce* -- where the real-time orders get processed based on the rule criteria where the points are allocated. The engine is highly configurable, which means that adding a new source, rule, or behavior will not affect the code or need any code changes. The in-memory rule parser was designed to parse any rule criteria over the incoming data efficiently.

The solution architecture is depicted in the following diagram:

![B17782_08_04_new](https://user-images.githubusercontent.com/62965911/218824400-9b17cc14-a5bf-4aa5-8ada-0f80dd02b554.jpg)

Figure -- Solution architecture diagram for the leading medical equipment manufacturer

Next, we will learn about a case study from the media and entertainment industry.

**Learning case studies from the media and entertainment industry**

Data plays a crucial role for media and entertainment organizations as it helps them understand viewer behavior and identify the true market value of the content being shared. This helps in improving the quality of content being delivered and at the same time opens up new monetization avenues for the production houses.

### Case study 5 -- HD Insights to Databricks migration for a media giant

In this case study, the prime requirement of the organization was processing and number crunching datasets that were 2-3 TB in size every day. This was required to perform analytics on on-demand advertising video service's user data to generate reports and dashboards for the marketing team. Also, the organization was not able to automate the **extract, transform, and load** (**ETL**) process of their web and mobile platform viewer's data. This ETL process was being executed using Azure HD Insights. Moreover, managing HD Insights was an operational overhead. Besides this, they were also interested in performance and cost optimization for their ETL jobs.

Migrating ETL workloads from HD Insights to Azure Databricks helped reduce costs by 26%. Azure Databricks, being a fully managed service, eliminated the operational overhead of managing the platform, therefore increasing productivity. Databricks' seamless integration with the Azure ecosystem helped in automating the processes using Azure Data Factory.

Caching data within Delta Lake helped to provide the much-needed acceleration of queries. Also, managing Spark clusters with auto-scaling and decoupling compute and storage helped to simplify the organization's infrastructure and further optimize operational costs. The migration from Hadoop to Databricks delivered significant value by reducing the cost of failure, increasing processing speeds, and simplifying data exploration for ad hoc analytics.

The complete customer success story can be read here: [https://databricks.com/customers/viacom18](https://databricks.com/customers/viacom18). The solution architecture is depicted in the following diagram:

![B17782_08_05](https://user-images.githubusercontent.com/62965911/218824404-a378658b-688a-41bf-a18b-9781f76e0912.jpg)

Figure -- Solution architecture diagram for the media giant

Next, we will learn about a case study from the retail and FMCG industry.

**Learning case studies from the retail and FMCG industry**

Data is more important than ever for the retail and FMCG industry. It can be very helpful for maintaining a lean inventory. In addition, data is critical for optimizing the prices of products on demand. Also, a data-driven approach can boost relationships with business partners, thereby helping to smoothen the supply chain.

### Case study 6 -- real-time analytics using IoT Hub for a retail giant

An organization wanted to build an end-to-end solution wherein edge devices gathered metrics at a certain frequency from all the instruments on the floor shop. These metrics were to be utilized to conduct edge analytics for real-time issues. Thereon, the data would be pushed to a cloud platform where near-real-time data transformations would be done and delivered to a dashboard for visualization. The same data would be persisted for batch processing and leveraged machine learning to gain insights.

The proposed solution architecture was as follows:

- Three devices (three metrics per device) were integrated with Azure **IoT Hub** to get the real-time device telemetry data into the Azure cloud.
- From IoT Hub, the data points were consumed by Azure Databricks to perform real-time transformation and to prepare useful insights.
- The transformed data was pushed to Power BI for live dashboard generation and to enable attentiveness when the data changed beyond the configured limits (Alert Mechanism).

The solution architecture is depicted in the following diagram:

![B17782_08_06_new](https://user-images.githubusercontent.com/62965911/218824414-d3b2e6d3-eadb-4105-ac54-5ac314122ffb.jpg)

Figure -- Solution architecture diagram for the retail giant

Next, we will learn about a case study from the pharmaceutical industry.

**Learning case studies from the pharmaceutical industry**

Data analytics and AI in the pharmaceutical industry play a crucial role in optimizing clinical trials, analyzing patients' behavior, improving logistics, and reducing costs.

### Case study 7 -- pricing analytics for a pharmaceutical company

The organization required a pricing decision support framework to get insights on gross margin increment based on historical events, the prioritization of SKUs, review indicators, and more. The framework was to be designed in a way so that the smart machine learning models could be transferred and scaled to retain the quality and depth of the information gathered.

A pricing decision framework was developed using machine learning on Azure Databricks, which helped to predict the SKU that should go for pricing review. The system was also capable of predicting the next month's volume, which helped in deciding the correct price for a specific SKU.

The solution architecture is depicted in the following diagram:

![B17782_08_07](https://user-images.githubusercontent.com/62965911/218824419-9925777b-be4a-43c9-b00a-bc014a248c50.jpg)

Figure -- Solution architecture diagram for the pharmaceutical company

Next, we will learn about a case study from the e-commerce industry.

**Learning case studies from the e-commerce industry**

**Big data analytics** in the e-commerce industry helps businesses understand consumer purchase patterns, improve user experience, and increase revenue.

### Case study 8 -- migrating interactive analytical apps from Redshift to Postgres

An organization in the e-commerce space was using AWS Redshift as their data warehouse and Databricks as their ETL engine. The setup was deployed across different data centers in different regions on **Amazon Web Services** (**AWS**) and **Google Cloud Platform** (**GCP**). They were also running into performance bottlenecks and were incurring egress costs unnecessarily. The data was growing faster than the compute required to process that data. AWS Redshift was unable to independently scale storage and compute. Hence, the organization decided to migrate its data and analytics landscape to Azure.

AWS Redshift's data was migrated to Azure Database for PostgreSQL Hyperscale (Citus). Citus is an open source extension to Postgres. It transforms Postgres into a distributed database where data can be sharded or partitioned across multiple nodes of the server. The migration effort was minimal as Redshift is also based on PostgreSQL. It took about 2 weeks to migrate from Redshift to Hyperscale (Citus). The highlights of the migration were as follows:

- 600 tables were migrated. Over 500 of them were distributed across the worker nodes of Postgres Hyperscale (Citus).
- Nearly 80% of the queries were dropped in, with no modifications.
- Almost 200 Databricks jobs were dropped in, with minimal changes. This is because Redshift uses the same JDBC driver that Azure Database does for PostgreSQL Hyperscale (Citus).

The complete customer success story can be read here: [https://techcommunity.microsoft.com/t5/azure-database-for-postgresql/migrating-interactive-analytics-apps-from-redshift-to-postgres/ba-p/1825730](https://techcommunity.microsoft.com/t5/azure-database-for-postgresql/migrating-interactive-analytics-apps-from-redshift-to-postgres/ba-p/1825730). The solution architecture is depicted in the following diagram:

![B17782_08_08](https://user-images.githubusercontent.com/62965911/218824428-2b4e039a-359a-4e1a-9254-840e821a6bd0.jpg)

Figure -- Solution architecture diagram for the pharmaceutical company

Next, we will learn about a case study from the logistics and supply chain industry.

**Learning case studies from the logistics and supply chain industry**

Data analytics and machine learning play a crucial role in the functioning of the logistics and supply chain industry. Data can help reduce inefficiencies in the supply chain processes and optimize deliveries at the same time. Machine learning and predictive analytics help in better planning, procurement, and consumer fulfillment.

### Case study 9 -- accelerating intelligent insights with tailored big data analytics

An organization wanted to create an end-to-end data warehousing platform on Azure. Their original process involved manually collecting data from siloed sources and creating necessary reports from it. There was a need to integrate all the data sources and implement a single source of truth, which would be on the Azure cloud. The proposed solution architecture was as follows:

- Full load and incremental data pipelines were developed using Azure Data Factory to ingest data into Azure Synapse (data warehouse). Azure Synapse also allows you to build pipelines, just like Azure Data Factory. Refer to the following link for differences between the two: [https://docs.microsoft.com/en-us/azure/synapse-analytics/data-integration/concepts-data-factory-differences](https://docs.microsoft.com/en-us/azure/synapse-analytics/data-integration/concepts-data-factory-differences).
- Data was loaded in **Azure Data Lake Storage** (**ADLS**) for big data transformations and analytics in Azure Databricks.
- The data lake was mounted on Azure Databricks for complex transformations and advanced use cases such as machine learning.
- The modeling that was done on the synapse layer included creating optimized views and tables that implemented business logic.
- Data modeling on Azure Analysis Services included defining relationships and creating the columns, measures, and tables necessary for Power BI's **key performance indicators** (**KPIs**).
- Cubes were created on Azure Analysis Services to ensure that data was refreshed quicker for Power BI reports. The reports were also created for a multi-lingual interface.

The solution architecture is depicted in the following diagram:

![B17782_08_09_new](https://user-images.githubusercontent.com/62965911/218824436-00d08e7f-9b37-4a3a-9e30-ca1c2fbc2480.jpg)

Figure -- Solution architecture diagram for the logistics and supply chain company

This brings us to the end of the case studies. To learn about more Databricks success stories, check out the official page: [https://databricks.com/customers](https://databricks.com/customers).

In this section, we learned about several Databricks case studies, ranging from manufacturing and media to logistics and the supply chain. All these solution architectures have employed Databricks in different ways. Irrespective of its role in an organization's data journey, Databricks has always emerged as a game-changer in the world of big data analytics.

## Labs

1. [Building a Cybersecurity Lakehouse for CrowdStrike Falcon Events in Databricks](03-processing/databricks/lab-cybersecurity-databricks/)
2. [Databricks AWS Integration and Clickstream Analysis](03-processing/databricks/lab-databricks-clickstream/)
3. [Create an elementary Data Lakehouse using Databricks and the Delta lake technology](03-processing/databricks/lab-databricks-deltalake/)
4. [Delta Lake Optimizations](03-processing/databricks/lab-deltalake-optimizations/)
5. [Compare dbt and Delta Live Tables (dlt) for data transformation](03-processing/databricks/lab-dlt-dbt/)
6. [Unlocking the Power of Health Data With a Modern Data Lakehouse](03-processing/databricks/lab-healthcare-databricks/)
7. [Real-time Health Tracking and Monitoring System](03-processing/databricks/lab-iot-health-tracker/)
8. [Simplifying Data Engineering and Analytics with Delta](03-processing/databricks/lab-loan-application/)
9. [Real-Time Point-of-Sale Analytics With the Data Lakehouse](03-processing/databricks/lab-retail-pos-databricks/)
10. [Data Engineering with Databricks](03-processing/databricks/project-databricks-de/)
11. [Data Engineer Learner Path with Databricks](03-processing/databricks/project-learnerbricks/)
12. [Advanced Data Engineering with Databricks](03-processing/databricks/project-advancedbricks/)
13. [Databricks PySpark Ecommerce Data Processing Case Study](03-processing/databricks/project-bedbricks/)
14. [Data Pipeline with Databricks PySpark and Superset](03-processing/databricks/project-databricks-superset/)
15. Creating and Monitoring Production Data Processing Jobs in Databricks
16. Processing Data Using Azure Databricks - Configuring the Azure Databricks environment, Integrate Databricks with Azure Key Vault, Mounting an Azure Data Lake container in Databricks, Processing data using notebooks, Scheduling notebooks using job clusters, Working with Delta Lake tables [[source code](03-processing/databricks/lab-data-processing-azure-db/)]

## Resources

1. [Data Lakehouse Explained](https://youtu.be/yumysN3XwbQ)
2. [What is Delta Lake](https://youtu.be/PftRBoqjhZM)
3. [Delta Lake Deep Dive](https://youtu.be/BMO90DI82Dc)
