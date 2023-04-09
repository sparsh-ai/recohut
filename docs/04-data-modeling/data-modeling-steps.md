# Steps of Building Data Models

## Gathering requirements

Before designing the warehouse table(s), you should always clearly define the end objectives.

Some questions you need answered/explored are

- What does this data represent and why is it needed?
- Who is the end-user of the table(s)?
- What is the business process that generates this data? How is this data generated?
- A few (>= 3) different example queries that the end-user is expected to run?
- What is the expected number of read queries per minute?
- What is an acceptable query execution time for reading from the table(s)?
- What is the expected number of daily records?
- What is the general date range (and/or other) filters for the read queries?
- What is the historical range of data that needs to be available for querying?

Answers to these questions will determine how you model and transform the data.

## Exploration

The next step is to explore the data, check for any data issues, validate assumptions, approximate data size growth, validate business rules, check for missing/duplicate rows on joins, etc

You will need to load the raw data into your data warehouse. There are multiple ways to ingest data into a data warehouse. For exploration, dump the data into a cloud storage system and use a COPY INTO command to load raw data into your data warehouse.

Some points you need answered/explored are:

1. Data schema checks

- Are data types consistent with the columns?
- Are column names consistent?

2. Data quality checks

- Were all the records in the raw file loaded into the raw table? Use wc -l input_data_file.csv to count the number of lines in the input data.
- Check for absence of column values such as NULL, null, 'null', '', N/A, etc
- Do any of the column values have a field delimiter within them? Most data warehouses have options to handle these, e.g. quote_character, FIELD_OPTIONALLY_ENCLOSED_BY.

3. Validate business assumptions

- If you join this data with other business-relevant tables, do you get unexpected duplicates or missing rows? If so, why?
- If you aggregate by some id and aggregate numeric columns in a fact table, are the aggregates accurate? Or does it cause doubles/undercounting? If so, how can you prevent it?
- Does the number of rows per day (and/or other business entities) show clear patterns? (including seasonality)
- Do all the tables have a unique id?
- For every business entity table (aka dimension), is there a table that records every update made to that table?
- Be aware of values with specific meaning. E.g. sometimes -9999 (or similar) can be used to denote NULL or other values.

This will be an ongoing process. Since the data generation process upstream can change, you may find additional data issues, etc.

## Modeling

With knowledge of the requirement and data issues, you are all set to model the end-user table(s). The standard approach is to have fact and dimension table(s). This type of data modeling has the advantage of being able to answer most queries. The downside is that this may require multiple joins, and can be a lot of work to manage.

Note:

> Dimensional/Data modeling always uses the concepts of facts (measures), and dimensions (context). Facts are typically (but not always) numeric values that can be aggregated, and dimensions are groups of hierarchies and descriptors that define the facts. For example, sales amount is a fact; timestamp, product, register#, store#, etc. are elements of dimensions. Dimensional models are built by business process area, e.g. store sales, inventory, claims, etc. Because the different business process areas share some but not all dimensions, efficiency in design, operation, and consistency, is achieved using conformed dimensions, i.e. using one copy of the shared dimension across subject areas.

Some points you need answered/explored are

- Naming conventions: Each company has its standard naming convention. If you don’t, make sure to establish this standard. (e.g. naming standard).
- Slowly changing dimensions: Most business entity tables (aka dimensions) have attributes that change over time. Consider creating an SCD2 table to capture historical changes.
- In-correct aggregates: Running aggregates on any numeric values of the fact table(s) should not produce duplicate/inaccurate results. This is usually a result of having the data representing different columns in one column.
- Pre-aggregating data: At times, the expected query pattern requires data to be rolled up to a higher granularity. In these cases, if your read time is longer than the requirement, you may want to pre-aggregate your data on a set schedule. Pre-aggregating the data will allow “read queries” to be much faster but introduces the additional overhead of creating, scheduling, and maintaining a data pipeline.
- Flat tables: Although the Kimball Model is very popular, it can get tedious for the end-user to query and join multiple tables. A way for the data team to provide a clean interface for the end-user is to create a wide flat table (or view). A flat table is a table with all the facts and dimensional columns. The end-user does not need to worry about joining multiple tables and can concentrate on analyzing the data.

Note:

> In a flat table, if some dimensional attributes change over time, then running a group-by query on those may produce inaccurate results. You can circumvent this by having 2 tables/views one with point-in-time dimensional attributes and the other with the most recent dimensional attribute.

## Data storage

Storing data in the right format can significantly impact your query performance. When modeling your end-user tables, make sure to consider the impact of data storage on read-type queries.

It’s crucial to understand the following concepts.

- Partitioning: Partitioning/Clustering, can significantly reduce the amount of data scanned and hence reduce the cost.
- Storage formats: Such as Parquet, or ORC formats can significantly reduce data size and speed up transformations.
- Sorting: Sorting can also reduce the amount of data to be read and make transformations efficient.
- Cloud storage: External tables allow for data to be stored in a cloud storage system and read when necessary.

Every data warehouse has different naming/implementation/caveats concerning the above, e.g. Snowflake automatically does most of these are for you, while Redshift requires a more hands on approach.