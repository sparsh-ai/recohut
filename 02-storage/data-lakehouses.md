# Data Lakehouses

We have been collecting data for decades. The flat file storages of the 60s led to the data warehouses of the 80s to **Massively Parallel Processing (MPP)** and NoSQL databases, and eventually to data lakes and now the lakehouses. New paradigms continue to be coined but it would be fair to say that most enterprise organizations have settled on some variation of a data lake and lakehouse:

![](https://user-images.githubusercontent.com/62965911/213930645-9bdd3fe4-9602-4006-a8c6-a8e3dcef4516.png)

In the last few years, many organizations have modernized their data engineering and analytics platforms by moving away from traditional data warehouses to data lakes. The move to the data lake has undoubtedly given them the flexibility to store and compute any format of data at a large scale. However, these advantages did not come without a few sacrifices along the way. The biggest one is the reliability of data. Like data warehouses, there is no transactional assurance available in a data lake. This need led to the launch of an open source storage layer known as Delta Lake. After its launch, experts came up with the idea of mixing the power of resilient data warehouses with the flexibility of data lakes and they called it a lakehouse.

Traditionally, organizations have been using a data warehouse for their analytical needs. As the business requirements evolved and data scale increased, they started adopting a modern data warehouse architecture which can process massive amounts of data in a relational format and in parallel across multiple compute nodes. At the same time, they started collecting and managing their non-relational big data that was in semi-structured or unstructured format with a data lake. These two disparate yet related systems ran in silos, increasing development time, operational overhead, and overall total cost of ownership.  It caused an inconvenience to end users to integrate data if they needed access to the data from both systems to meet their business requirements. Data Lakehouse platform architecture combines the best of both worlds in a single data platform, offering and combining capabilities from both these earlier data platform architectures into a single unified data platform – sometimes also called as medallion architecture. It means, the data lakehouse is the one platform to unify all your data, analytics, and Artificial Intelligence/Machine Learning (AI/ML) workloads.

![](https://user-images.githubusercontent.com/62965911/213930628-d8e2a629-999e-463c-a8fb-4f33d3bf4f51.svg)

Most data engineering teams when building data pipelines typically move data from Application Databases to Data Lakes and then move a subset of the data into a Data Warehouse for reporting purposes. But with Lakehouse architecture, we combine Data Lake and Data Warehouse into a Lakehouse, so that your data is moving across just two types of systems. Also Lakehouse can support ingestion of both Streaming and Batch data into the same data structure. This obviates the extra step to consolidate batch and streaming data. This results in a more streamlined Data Pipeline with the fewest hops and faster time to value. So, with a Lakehouse, in most cases, it takes less than 5 minutes to get your data from the point it was generated to the point where it can be reported on in a dashboard.

![](https://user-images.githubusercontent.com/62965911/213930649-c437586c-30fc-442a-a7c9-d56b7cc337b6.svg)

NOTE

> You now run all scenarios - BI as well as data science, on a single platform, and you don’t have a cloud data warehouse.

Lakehouse helps you simplify data processing and democratize the usage of the data across your organization at the lowest cost possible. This is a game changer for small and big enterprises which are falling behind in the pursuit of leveraging data to gain competitive advantage. So say goodbye to Data warehouses and say hello to Lakehouse and you will never look back as you will be the superhero to all your data users.

NOTE

> To enable a data lakehouse architecture, you need to ensure you leverage one of the open data technologies such as Apache Iceberg or Delta Lake or Apache Hudi, and a compute framework that understands and respects these formats. Cloud providers are continuing to work on toolsets and services that simplify the architecture and operationalization of the data lakehouse. Specifically, an example worth calling out is AWS services that make a data lakehouse implementation easier by leveraging AWS Glue for data integration and orchestration, AWS S3 as the cloud data lake storage, and Amazon Athena to query data from AWS S3 using standard SQL that is familiar to business intelligence users.

Data warehouses have a long history in decision support and business intelligence applications. Since its inception in the late 1980s, data warehouse technology continued to evolve and MPP architectures led to systems that were able to handle larger data sizes. But while warehouses were great for structured data, a lot of modern enterprises have to deal with unstructured data, semi-structured data, and data with high variety, velocity, and volume. Data warehouses are not suited for many of these use cases, and they are certainly not the most cost efficient.

As companies began to collect large amounts of data from many different sources, architects began envisioning a single system to house data for many different analytic products and workloads. About a decade ago companies began building data lakes – repositories for raw data in a variety of formats. While suitable for storing data, data lakes lack some critical features: they do not support transactions, they do not enforce data quality, and their lack of consistency / isolation makes it almost impossible to mix appends and reads, and batch and streaming jobs. For these reasons, many of the promises of the data lakes have not materialized, and in many cases leading to a loss of many of the benefits of data warehouses.

The need for a flexible, high-performance system hasn’t abated. Companies require systems for diverse data applications including SQL analytics, real-time monitoring, data science, and machine learning. Most of the recent advances in AI have been in better models to process unstructured data (text, images, video, audio), but these are precisely the types of data that a data warehouse is not optimized for. A common approach is to use multiple systems – a data lake, several data warehouses, and other specialized systems such as streaming, time-series, graph, and image databases. Having a multitude of systems introduces complexity and more importantly, introduces delay as data professionals invariably need to move or copy data between different systems.

![](https://user-images.githubusercontent.com/62965911/213930637-2fd0ee92-49e3-4d13-94cf-d17be08a8799.png)

New systems are beginning to emerge that address the limitations of data lakes. A lakehouse is a new, open architecture that combines the best elements of data lakes and data warehouses. Lakehouses are enabled by a new open and standardized system design: implementing similar data structures and data management features to those in a data warehouse, directly on the kind of low cost storage used for data lakes. They are what you would get if you had to redesign data warehouses in the modern world, now that cheap and highly reliable storage (in the form of object stores) are available.

A lakehouse has the following key features:

- Transaction support: In an enterprise lakehouse many data pipelines will often be reading and writing data concurrently. Support for ACID transactions ensures consistency as multiple parties concurrently read or write data, typically using SQL.
- Schema enforcement and governance: The Lakehouse should have a way to support schema enforcement and evolution, supporting DW schema architectures such as star/snowflake-schemas. The system should be able to reason about data integrity, and it should have robust governance and auditing mechanisms.
- BI support: Lakehouses enable using BI tools directly on the source data. This reduces staleness and improves recency, reduces latency, and lowers the cost of having to operationalize two copies of the data in both a data lake and a warehouse.
- Storage is decoupled from compute: In practice this means storage and compute use separate clusters, thus these systems are able to scale to many more concurrent users and larger data sizes. Some modern data warehouses also have this property.
- Openness: The storage formats they use are open and standardized, such as Parquet, and they provide an API so a variety of tools and engines, including machine learning and Python/R libraries, can efficiently access the data directly.
- Support for diverse data types ranging from unstructured to structured data: The lakehouse can be used to store, refine, analyze, and access data types needed for many new data applications, including images, video, audio, semi-structured data, and text.
- Support for diverse workloads: including data science, machine learning, and SQL and analytics. Multiple tools might be needed to support all these workloads but they all rely on the same data repository.
- End-to-end streaming: Real-time reports are the norm in many enterprises. Support for streaming eliminates the need for separate systems dedicated to serving real-time data applications.

These are the key attributes of lakehouses. Enterprise grade systems require additional features. Tools for security and access control are basic requirements. Data governance capabilities including auditing, retention, and lineage have become essential particularly in light of recent privacy regulations. Tools that enable data discovery such as data catalogs and data usage metrics are also needed. With a lakehouse, such enterprise features only need to be implemented, tested, and administered for a single system.

Read the full research paper on the [inner workings of the Lakehouse](https://databricks.com/research/delta-lake-high-performance-acid-table-storage-overcloud-object-stores).

![lakehouse-architecture](https://user-images.githubusercontent.com/62965911/216760249-832980a9-2e58-4c7f-8dcf-a482cadc2415.png)

Table formats are instrumental for getting the scalability benefits of the data lake and the underlying object store, while at the same time getting the data quality and governance associated with data warehouses. Previously, users had to pick one or the other, or replicate data from a lake to the warehouse and hope (or pray) that it stays up-to-date. But by using a table format, lakehouse users don’t have to accept tradeoffs and get the benefits of both.

Three table formats have emerged over the past few years to power data lakehouses. Apache Iceberg was created by engineers at Netflix and Apple who were tired of trying to use Apache Hive’s metastore to track data updates and manage transactions. [Databricks](https://www.databricks.com/) created its own table format to live at the heart of its Delta Lake offering, and then open sourced it. Apache Hudi, meanwhile, was created by engineers at Uber to provide support for transactions for a massive data lake running on Hadoop.

The whole elevator pitch for lakehouse is ACID transactions. Not to turn it into an OLTP database, but is the data that we’re doing these analytics on or building these machine learning models on–is this valid data? Is it consistent? Or are we basically chasing our tail? That was the real driver of this. From that, you then get all the other goodies, like now with a table structure, we can do much more granular governance. Arguably there are ways to basically accelerate processing Parquet. But basically with tables, you can get much better performance that you can through file scans than you can with something like Impala.

## Medallion Architecture

A medallion architecture is a data design pattern used to logically organize data in a lakehouse, with the goal of incrementally and progressively improving the structure and quality of data as it flows through each layer of the architecture (from Bronze ⇒ Silver ⇒ Gold layer tables). Medallion architectures are sometimes also referred to as "multi-hop" architectures.

![](https://user-images.githubusercontent.com/62965911/213927430-13be2919-ad25-4094-8488-17048701f745.png)

A lakehouse is a new data platform architecture paradigm that combines the best features of data lakes and data warehouses. A modern lakehouse is a highly scalable and performant data platform hosting both raw and prepared data sets for quick business consumption and to drive advanced business insights and decisions. It breaks data silos and allows seamless, secure data access to authorized users across the enterprise on one platform.

### Benefits of a lakehouse architecture

- Simple data model
- Easy to understand and implement
- Enables incremental ETL
- Can recreate your tables from raw data at any time
- ACID transactions, time travel

### Layers

#### Landing area

An optional layer that is often seen at organizations implementing a data platform is a landing area or landing zone. A landing area is an intermediate location in which data from various source systems will be stored before moving it into the Bronze layer. This layer is often needed in situations in which it's hard to extract data from the target source system. For example, when working with external customers or SaaS vendors. In such scenarios, you have a dependency or sometimes receive data in an unpreferred (file) format or structure.

The solution design of a landing zone varies between organizations. Often, it's a simple Blob storage account. In other cases, the landing zone is part of the data lake services, for example, container, bucket, or specific folder in which the data is ingested. Data within landing zones is often highly diverse. File formats could be CSV, JSON, XML, Parquet, Delta, and so on.

#### Bronze layer

The bronze layer is usually a reservoir that stores data in its natural and original state. It contains unvalidated data (without having to first define schemas). In this layer you either get data using full loads or delta loads. Data that is stored in bronze has usually the following characteristics:

- Maintains the raw state of the data source in the structure "as-is".
- Data is immutable (read-only).
- Managed using interval partitioned tables, for example, using a YYYYMMDD or datetime folder structure.
- Retains the full (unprocessed) history of each dataset in an efficient storage format, for example, Parquet or Delta.
- For transactional data: Can be appended incrementally and grow over time.
- Provides the ability to recreate any state of a given data system.
- Can be any combination of streaming and batch transactions.
- May include extra metadata, such as schema information, source file names or recording the time data was processed.

The question that I often hear is "What is the best file format? Should I use Delta or Parquet?" Delta is faster, but since data is already versioned or historized using a folder structure, I don't see any compelling benefits for maintaining a transaction log or apply versioning. Data in Bronze is generally new data or being appended. So, if you would like to go for Parquet, that's fine. Alternatively, you use Delta in line with all other layers.

Some people say that data in Bronze is useful for business users for querying or ad-hoc analysis. In my experience, while working with customers, I rarely see raw data being used as input for running queries or ad-hoc analysis. Raw data is hard to work with. It requires in-depth understanding of how the source system has been designed. It requires you to work out complex business logic that has been encapsulated with the data itself. It often has many small tables, hence it's impossible to secure. To conclude: Bronze is a staging layer and input for other layers. It's mainly accessed by technical accounts.

#### Silver layer

The Silver layer provides a refined structure over data that has been ingested. It represents a validated, enriched version of our data that can be trusted for downstream workloads, both operational and analytical. In addition to that, Silver may have the following characteristics:

- Uses data quality rules for validating and processing data.
- Typically contains only functional data. So, technical data or irrelevant data from Bronze is filtered out.
- Historization is usually applied by merging all data. Data is processed using slowly changing dimensions (SCD), either type 2 or type 4. This means additional columns are added, such as start, end and current columns.
- Data is stored in an efficient storage format; preferably Delta, alternatively Parquet.
- Uses versioning for rolling back processing errors.
- Handles missing data, standardizes clean or empty fields.
- Data is usually enriched with reference and/or master data.
- Data is often cluttered around certain subject areas.
- Data is often still source-system aligned and organized.

For Silver there are a couple of attention points:

Some people say that Silver can act as a temporary storage layer. Thus, older data can be wiped out or storage accounts can be created on the fly. Customers question me, do you see this as well? Well, it depends. If you aren't planning on using data in the original context for operational reporting or operational analytics, then Silver can be a temporal layer. However, if you plan on retaining history and use this data for operational reporting and analytics, then, I encourage you to make Silver a persistent layer.

Data in Silver is queryable. From a data modeling standpoint, this means that for Silver it's recommended to follow a more denormalized data model. Why? Because such a design better utilizes the distributed column-based storage that is separated from compute. Does this mean that you shouldn't use a 3rd-normal form or Data Vault-like data model? Well, you could implement a design that is heavier normalized. On the flip side, I don't see any compelling arguments. Delta already provides isolation and protection. For example, you can turn on merge schema for handling changes. Besides that, you have history in Silver and also history in your Bronze layer from which you can (re)load data again. Thus, flexibility is already provided. So, then why add increased complexity, slow down performance and add more expensive runtimes to your design? It's a trade-off you should make. If you would like to learn more on this subject, then I recommend you to watch the [video from Simon Whiteley](https://www.youtube.com/watch?v=RNMoWnSWcTo) in which he provides many considerations.

Another discussion that I sometimes have is on whether you should already join or integrate data between applications and source systems. Here the situation is a bit more nuanced. I recommend, if possible, breaking things apart for better managing and isolating concerns. For facilitating scenarios in which you utilize Silver for operational reporting or operational analytics, this consequently means that it's recommended to not already combine and integrate data between source systems. If you would do so, then you would create unnecessary coupling points between applications. For example, for another consumer or user that is only interested in data from a single source, there's also coupling to other systems, because data first is combined in a harmonized layer, and then served out. So, such data consumers are more likely to see potential impact from other systems. If you aim for such an isolated design, then consequently the combination or integration of data between sources moves up one layer.

The same above argument holds true when aligning your lake houses with the source-system side of your architecture. If you plan on building data products and strongly want to align data ownership, then I wouldn't encourage your engineers to already cross-join data between applications from other domains.

For the enrichments, such as calculations, there are also considerations you should make. If you plan to facilitate operational reporting and for that, enrichments are needed, then I recommend already enriching your data in the Silver layer. This potentially could result in some extra calibration when combining data at a later stage in Gold. Yes, this might be additional work, but it's worth having the benefits of flexibility.

#### Gold layer

Data in the Gold layer, according to the principles of a Lakehouse architecture, is typically organized in consumption-ready "project-specific" databases. From from this perspective, you could argue that data ownership changes, because data is no longer source-system is aligned. Instead, it has been integrated and combined with other data.

For Gold, depending on your use cases, I recommend a more de-normalized and read-optimized data model with fewer joins. So, a Kimball-style star schema. In addition to that, expect the following characteristics:

- Gold tables represent data that has been transformed for consumption or use cases.
- Data is stored in an efficient storage format, preferably Delta.
- Gold uses versioning for rolling back processing errors.
- Historization is applied only for the set of use cases or consumers. So, Gold can be a selection or aggregation of data that's found in Silver.
- In Gold you apply complex business rules. So, it uses many post-processing activities, calculations, enrichments, use-case specific optimizations, etc.
- Data is highly governed and well-documented.

Gold is often the most complex layer because its design varies on the scope of your architecture. In the simplest scenario, your Lakehouses are only aligned with the source-system side. If so, data that sits in Gold will represent "data product" data. Thus, data is generic and user-friendly for broad distribution to many other domains. Then, and after distribution, you expect data to land in another platform. This could be a Lakehouse again. If so, you would expect Gold in these platform to match the precise requires of analytical consumers. Thus, data has been modelled. Its shape and structure is highly specific for the use case you're working on. The upper way of working could lead to principles in which you allow domains to only operate on internal data that is not directly served to other domains. So, there might be tables that are flexible and can be adjusted at any times. And there are other tables with a formal status that are being consumed by other parties.

If your Lakehouse scope is larger and targets both sides, then, extra layers are expected. Some people call these extra layers workspace or presentation layers. In such a design, data in Gold is more generic. It's integrated and prepared for a set of use cases. Then, within these workspace or presentation layers you see subsets. Such a design is very similar to how you usually do data modeling within data warehousing. Gold behaves like a generic integration layer from which data marts or subsets can be populated.

Some companies also use these workspace or presentation layers for sharing data across to other platforms or teams. So, they make selections and/or prefilter data for specific use cases. Other customers apply tokenization, which means that they replace sensitive values with randomized data strings. Other use additional services for data anonymization. You could argue that this data in a way behaves as "data product" data.

### Medallion architecture and data mesh

The Medallion architecture is compatible with the concept of a data mesh. Bronze and silver tables can be joined together in a "one-to-many" fashion, meaning that the data in a single upstream table could be used to generate multiple downstream tables.

### Hybrid approaches

Depending on your organizational needs, the maturity of your scenarios, and your data platform strategy, you could end up having a hybrid approach to your data lake. As an example, when most of the organization runs on a cloud data warehouse as its central data repository, there is a center of innovation working with a set of handpicked scenarios on a data lake architecture and then gradually expanding to the rest of the company. On another hand, while most of the organizations adopt a data lakehouse architecture, you might find some teams still dependent on legacy infrastructure that would take years to move.

### Tools

The Databricks Platform has the architectural features of a lakehouse. Microsoft’s Azure Synapse Analytics service, which integrates with Azure Databricks, enables a similar lakehouse pattern. Other managed services such as BigQuery and Redshift Spectrum have some of the lakehouse features listed above, but they are examples that focus primarily on BI and other SQL applications. Companies who want to build and implement their own systems have access to open source file formats (Delta Lake, Apache Iceberg, Apache Hudi) that are suitable for building a lakehouse.

Merging data lakes and data warehouses into a single system means that data teams can move faster as they are able use data without needing to access multiple systems. The level of SQL support and integration with BI tools among these early lakehouses are generally sufficient for most enterprise data warehouses. Materialized views and stored procedures are available but users may need to employ other mechanisms that aren’t equivalent to those found in traditional data warehouses. The latter is particularly important for “lift and shift scenarios”, which require systems that achieve semantics that are almost identical to those of older, commercial data warehouses.

What about support for other types of data applications? Users of a lakehouse have access to a variety of standard tools (Spark, Python, R, machine learning libraries) for non BI workloads like data science and machine learning. Data exploration and refinement are standard for many analytic and data science applications. Delta Lake is designed to let users incrementally improve the quality of data in their lakehouse until it is ready for consumption.

NOTE

> While distributed file systems can be used for the storage layer, objects stores are more commonly used in lakehouses. Object stores provide low cost, highly available storage, that excel at massively parallel reads – an essential requirement for modern data warehouses.