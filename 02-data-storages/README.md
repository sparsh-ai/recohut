# Data Storages

#### Postgres vs MySQL

When it comes to choosing a relational database management system (RDBMS), two popular options are PostgreSQL and MySQL. Both have been around for decades and have proven to be highly reliable, secure, and scalable. However, they have different strengths and weaknesses that make one more suitable for certain use cases than the other.

Follow [this](https://dbconvert.com/blog/mysql-vs-postgresql/?utm_source=pocket_reader) link for more information.

#### When should you use a data lake?

We can consider using data lakes for the following scenarios:

- If you have data that is too big to be stored in structured storage systems like data warehouses or SQL databases
- When you have raw data that needs to be stored for further processing, such as an ETL system or a batch processing system
- Storing continuous data such as **Internet of Things** (**IoT**) data, sensor data, tweets, and so on for low latency, high throughput streaming scenarios
- As the staging zone before uploading the processed data into an SQL database or data warehouse
- Storing videos, audios, binary blob files, log files, and other semi-structured data such as **JavaScript Object Notation** (**JSON**), **Extensible Markup Language** (**XML**), or **YAML Ain't Markup Language** (**YAML**) files for short-term or long-term storage.
- Storing processed data for advanced tasks such as ad hoc querying, **machine learning** (**ML**), data exploration, and so on.
