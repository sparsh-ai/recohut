# Flat Files

## Introduction

Storage formats are a way to define how data is stored in a file. Hadoop doesn't have a default file format, but it supports multiple file formats for storing data. Some of the common storage formats for Hadoop are as follows:

- Text files
- Sequence files
- Parquet files
- Record-columnar (RC) files
- Optimized row columnar (ORC) files
- Avro files

Choosing a write file format will provide significant advantages, such as the following:

- Optimized performance while reading and writing data
- Schema evolution support (allows us to change the attributes in a dataset)
- Higher compression, resulting in less storage space being required
- Splittable files (files can be read in parts)

Let's focus on columnar storage formats as they are widely used in big data applications because of how they store data and can be queried by the SQL engine. The columnar format is very useful when a subset of data needs to be referred to. However, when most of the columns in a dataset need to be fetched, then row-oriented storage formats are beneficial.

Many serialization algorithms and formats are available to data engineers. While the abundance of options is a significant source of pain in data engineering, they are also a massive opportunity for performance improvements. We’ve sometimes seen job performance improve by a factor of 100 simply by switching from CSV to Parquet serialization. As data moves through a pipeline, engineers will also manage reserialization—conversion from one format to another. Sometimes data engineers have no choice but to accept data in an ancient, nasty form; they must design processes to deserialize this format and handle exceptions, and then clean up and convert data for consistent, fast downstream processing and consumption.

## Row-Based Serialization

As its name suggests, row-based serialization organizes data by row. CSV format is an archetypal row-based format. For semistructured data (data objects that support nesting and schema variation), row-oriented serialization entails storing each object as a unit.

#### CSV: The nonstandard standard

CSV is a serialization format that data engineers love to hate. The term CSV is essentially a catchall for delimited text, but there is flexibility in conventions of escaping, quote characters, delimiter, and more.

Data engineers should avoid using CSV files in pipelines because they are highly error-prone and deliver poor performance. Engineers are often required to use CSV format to exchange data with systems and business processes outside their control. CSV is a common format for data archival. If you use CSV for archival, include a complete technical description of the serialization configuration for your files so that future consumers can ingest the data.

CSV (Comma Separated Values) is a simple file format used for storing tabular data, where each line of the file represents a single row and each value in a row is separated by a comma.

Advantages:

- Easy to read and write
- Can be easily imported into a wide range of data analysis tools
- Small file size

Disadvantages:

- Not efficient for storing large data sets with complex data types
- Can lead to data loss if values contain commas or line breaks
- Limited support for encoding

Application: CSV is commonly used for small data sets and as a standard format for data exchange between different applications.

Example

```
name,age,gender
John,25,M
Jane,32,F
Bob,45,M
```

#### XML

Extensible Markup Language (XML) was popular when HTML and the internet were new, but it is now viewed as legacy; it is generally slow to deserialize and serialize for data engineering applications. XML is another standard that data engineers are often forced to interact with as they exchange data with legacy systems and software. JSON has largely replaced XML for plain-text object serialization.

#### JSON and JSONL

JavaScript Object Notation (JSON) has emerged as the new standard for data exchange over APIs, and it has also become an extremely popular format for data storage. In the context of databases, the popularity of JSON has grown apace with the rise of MongoDB and other document stores. Databases such as Snowflake, BigQuery, and SQL Server also offer extensive native support, facilitating easy data exchange between applications, APIs, and database systems.

JSON Lines (JSONL) is a specialized version of JSON for storing bulk semistructured data in files. JSONL stores a sequence of JSON objects, with objects delimited by line breaks. From our perspective, JSONL is an extremely useful format for storing data right after it is ingested from API or applications. However, many columnar formats offer significantly better performance. Consider moving to another format for intermediate pipeline stages and serving.

JSON (JavaScript Object Notation) is a lightweight file format used for storing and exchanging data, which is based on the JavaScript programming language. It is a text-based format that uses a key-value structure to represent data.

Advantages:

- Human-readable and easy to understand
- Can be easily parsed and manipulated with different programming languages
- Supports complex data types, such as arrays and nested objects

Disadvantages:

- Can be less efficient for storing and processing large data sets compared to other binary formats
- Limited support for data compression

Application: JSON is commonly used for web APIs, NoSQL databases, and as a data exchange format between different applications.

Example:

```
{
   "name": "John",
   "age": 25,
   "gender": "M"
},
{
   "name": "Jane",
   "age": 32,
   "gender": "F"
},
{
   "name": "Bob",
   "age": 45,
   "gender": "M"
}
```

#### Avro

Avro is a row-oriented data format designed for RPCs and data serialization. Avro encodes data into a binary format, with schema metadata specified in JSON. Avro is popular in the Hadoop ecosystem and is also supported by various cloud data tools.

Avro is a data serialization system that was developed by Apache Software Foundation in 2009. It is a row-based format that is designed to be fast, compact, and extensible. Avro is often used in Hadoop-based big data processing systems like Hive and HBase, as well as in other distributed systems like Kafka and Cassandra.

Advantages:

- Compact format: Avro is a compact format that uses binary encoding to reduce storage requirements and improve performance. This makes it ideal for use cases where storage and performance are critical.
- Schema evolution: Avro supports schema evolution, which means that you can add, remove, or modify fields without breaking compatibility with existing data. This makes it easy to update data models over time.
- Dynamic typing: Avro supports dynamic typing, which means that you can change the data type of a field at runtime. This makes it easier to handle changes to data models and to work with data from multiple sources.
- Language-agnostic: Avro is designed to be language-agnostic, which means that it can be used with a variety of programming languages.

Disadvantages:

- Lack of built-in compression: Unlike some other big data file formats, Avro does not include built-in compression. This means that you'll need to use external compression libraries to compress data.
- Slower performance than columnar storage: Avro's row-based storage format can be slower than columnar storage formats like Parquet for analytical queries that involve reading only a subset of columns.
- No support for indexing:

Applications:

1. Distributed computing: Avro is often used in distributed computing environments such as Apache Hadoop, where it is used to serialize data for use in MapReduce jobs.
2. Data storage: Avro is often used as a data storage format for log files, message queues, and other data sources.
3. High-throughput systems: Avro's compactness and support for compression make it ideal for use in high-throughput systems such as web applications and real-time data processing pipelines.

Example of Avro data and schema:

Avro Data

```
{
  "name": "John",
  "age": 30,
  "email": "john@example.com"
}
```

Avro Schema

```
{
  "type": "record",
  "name": "Person",
  "namespace": "example.avro",
  "fields": [
    {"name": "name", "type": "string"},
    {"name": "age", "type": "int"},
    {"name": "email", "type": "string"}
  ]
}
```

## Columnar Serialization

The serialization formats we’ve discussed so far are row-oriented. Data is encoded as complete relations (CSV) or documents (XML and JSON), and these are written into files sequentially.

With columnar serialization, data organization is essentially pivoted by storing each column into its own set of files. One obvious advantage to columnar storage is that it allows us to read data from only a subset of fields rather than having to read full rows at once. This is a common scenario in analytics applications and can dramatically reduce the amount of data that must be scanned to execute a query.

Storing data as columns also puts similar values next to each other, allowing us to encode columnar data efficiently. One common technique involves looking for repeated values and tokenizing these, a simple but highly efficient compression method for columns with large numbers of repeats.

Even when columns don’t contain large numbers of repeated values, they may manifest high redundancy. Suppose that we organized customer support messages into a single column of data. We likely see the same themes and verbiage again and again across these messages, allowing data compression algorithms to realize a high ratio. For this reason, columnar storage is usually combined with compression, allowing us to maximize disk and network bandwidth resources.

Columnar storage and compression come with some disadvantages too. We cannot easily access individual data records; we must reconstruct records by reading data from several column files. Record updates are also challenging. To change one field in one record, we must decompress the column file, modify it, recompress it, and write it back to storage. To avoid rewriting full columns on each update, columns are broken into many files, typically using partitioning and clustering strategies that organize data according to query and update patterns for the table. Even so, the overhead for updating a single row is horrendous. Columnar databases are a terrible fit for transactional workloads, so transactional databases generally utilize some form of row- or record-oriented storage.

#### Parquet

Parquet stores data in a columnar format and is designed to realize excellent read and write performance in a data lake environment. Parquet solves a few problems that frequently bedevil data engineers. Parquet-encoded data builds in schema information and natively supports nested data, unlike CSV. Furthermore, Parquet is portable; while databases such as BigQuery and Snowflake serialize data in proprietary columnar formats and offer excellent query performance on data stored internally, a huge performance hit occurs when interoperating with external tools. Data must be deserialized, reserialized into an exchangeable format, and exported to use data lake tools such as Spark and Presto. Parquet files in a data lake may be a superior option to proprietary cloud data warehouses in a polyglot tool environment.

Parquet format is used with various compression algorithms; speed optimized compression algorithms such as Snappy (discussed later in this appendix) are especially popular.

Parquet is a *columnar* storage format that is optimized for big data workloads. It was developed by Cloudera and Twitter in 2013 as an open-source project. Parquet is built on a compressed columnar data representation, which makes it highly efficient for analytical queries that involve large amounts of data. Parquet is often used in Hadoop-based big data processing systems like Hive, Impala, and Spark.

Advantages:

- Efficient compression: Parquet is highly efficient when it comes to compression. It uses various compression algorithms like Snappy, LZO, and Gzip to compress data, which reduces storage requirements and improves query performance.
- Columnar storage: Parquet stores data in columns rather than rows, which makes it more efficient for analytical queries that typically involve reading only a subset of columns from a large dataset.
- Schema evolution: Parquet supports schema evolution, which means that you can add, remove, or modify columns without breaking compatibility with existing data. This makes it easy to update data models over time.
- Cross-platform support: Parquet is an open-source project and is supported by a variety of big data processing systems, including Hadoop, Spark, and Impala.

Disadvantages:

- Write performance: Parquet's columnar storage format can be slower than row-based formats for writes, especially when adding data to existing columns.
- Not suitable for small datasets: Parquet is optimized for large-scale analytical queries and is not suitable for small datasets or OLTP workloads.
- Query planning overhead: Columnar storage requires more query planning overhead than row-based storage formats. This can increase query planning time and make it more complex.

Applications: Parquet is a popular format for big data processing and is used in a variety of analytical and data science applications. Some specific use cases include:

- Storing and processing large-scale datasets in Hadoop-based systems like Hive and Impala.
- Analyzing data with Spark and other big data processing systems.
- Data warehousing and business intelligence applications that involve analyzing large datasets.

Example:

```
+------+---+---+
| name |age|gender|
+------+---+---+
| John | 25|M |
| Jane | 32|F |
| Bob | 45|M |
+------+---+---+
```

Parquet is a file format that is available within the Hadoop ecosystem and is designed for performant and efficient flat columnar storage format of data compared to row-based files like CSV or TSV files.

Parquet supports all the features that are provided by the RC and ORC file formats. It stores data in binary files with metadata. Using this metadata information, Spark can easily determine data types, column names, and compression by parsing the data files. Because of these features, it is widely used in big data applications.

Rather than using simple flattening of nested namespaces, Parquet uses record shredding and assembly algorithms. Parquet features different ways for efficient data compression and encoding types and is optimized to work with complex data in bulk. This approach is optimal for queries that need to read certain columns from large tables. Parquet can only read the needed columns, which minimizes the I/O.

- Similar to a CSV file, Parquet is a type of file
- Parquet is an open-source format for storing data, licensed under Apache
- Parquet is a columnar storage substrate created for simpler data analysis
- Parquet is a self-describing data format that embeds the schema or structure within the data itself
- This format can speed up queries by allowing only the required columns to be read and calculated
- Parquet is built to support efficient compression schemes, which maximizes the storage efficiency on disks
- Parquet deploys Google's record-shredding and assembly algorithm that can address complex data structures within data storage
- This results in a file that is optimized for query performance and minimizing I/O
- High compatibility with OLAP
- So we can have a better control in performance and the cost

**Parquet and Schema evolution**

When using columnar file formats like Parquet, users can start with a simple schema, and gradually add more columns to the schema as needed. In this way, users may end up with multiple Parquet files with different but mutually compatible schemas. In these cases, Parquet supports automatic schema merging among these files.

Read more about parquet here:

- https://www.databricks.com/glossary/what-is-parquet

#### ORC

Optimized Row Columnar (ORC) is a columnar storage format similar to Parquet. ORC was very popular for use with Apache Hive; while still widely used, we generally see it much less than Apache Parquet, and it enjoys somewhat less support in modern cloud ecosystem tools. For example, Snowflake and BigQuery support Parquet file import and export; while they can read from ORC files, neither tool can export to ORC.

ORC is an open-source, columnar storage format for Hadoop-based data processing systems, such as Hive and Pig. It is designed to provide better performance for large-scale data processing, especially for queries that involve reading or filtering large subsets of columns in a dataset.

Advantages:

- Improved query performance: ORC's columnar storage format makes it easier to read and process data more efficiently, especially for queries that involve reading only a subset of columns. This can lead to significant improvements in query performance and reduced storage costs.
- Reduced I/O and network overhead: ORC uses lightweight compression techniques to reduce storage and I/O requirements, resulting in faster query execution times.
- Support for complex data types: ORC supports complex data types, including maps, lists, and structs, which makes it more flexible and useful for working with complex datasets.
- Easy to use: ORC is designed to be easy to use and integrate with existing Hadoop-based data processing systems, such as Hive and Pig.

Disadvantages:

- Limited compatibility: ORC is primarily designed for use with Hadoop-based data processing systems, which limits its compatibility with other systems.
- Limited adoption: ORC is not as widely adopted as some other storage formats, such as Parquet and Avro.

Applications:

- Big data processing: ORC is well-suited for processing large datasets in big data environments. Its efficient storage and retrieval mechanisms make it ideal for processing large datasets and running complex queries on those datasets.
- Analytics and reporting: ORC is commonly used for storing and processing data for analytics and reporting purposes, as it can help to provide faster query performance and reduced storage costs.
- Data warehousing: ORC can be used for storing and querying data in a data warehouse environment, where it can provide improved query performance and reduced storage costs.

Example

Note that ORC files are binary files, so the data appears as binary data in the file. The below example shows only the structure of the file, not the actual binary data.

```
<ORC>
  <Metadata/>
  <Stripes>
    <Stripe>
      <Column>
        <Data>
          <Binary>
            <!-- binary data for first row of the first column -->
          </Binary>
          <Binary>
            <!-- binary data for second row of the first column -->
          </Binary>
          <!-- ... more data ... -->
        </Data>
      </Column>
      <!-- ... more columns ... -->
    </Stripe>
    <!-- ... more stripes ... -->
  </Stripes>
</ORC>
```

#### Apache Arrow or in-memory serialization

When we introduced serialization as a storage raw ingredient at the beginning of this chapter, we mentioned that software could store data in complex objects scattered in memory and connected by pointers, or more orderly, densely packed structures such as Fortran and C arrays. Generally, densely packed in-memory data structures were limited to simple types (e.g., INT64) or fixed-width data structures (e.g., fixed-width strings). More complex structures (e.g., JSON documents) could not be densely stored in memory and required serialization for storage and transfer between systems.

The idea of Apache Arrow is to rethink serialization by utilizing a binary data format that is suitable for both in-memory processing and export.1 This allows us to avoid the overhead of serialization and deserialization; we simply use the same format for in-memory processing, export over the network, and long-term storage. Arrow relies on columnar storage, where each column essentially gets its own chunks of memory. For nested data, we use a technique called shredding, which maps each location in the schema of JSON documents into a separate column.

This technique means that we can store a data file on disk, swap it directly into program address space by using virtual memory, and begin running a query against the data without deserialization overhead. In fact, we can swap chunks of the file into memory as we scan it, and then swap them back out to avoid running out of memory for large datasets.

One obvious headache with this approach is that different programming languages serialize data in different ways. To address this issue, the Arrow Project has created software libraries for a variety of programming languages (including C, Go, Java, JavaScript, MATLAB, Python, R, and Rust) that allow these languages to interoperate with Arrow data in memory. In some cases, these libraries use an interface between the chosen language and low-level code in another language (e.g., C) to read and write from Arrow. This allows high interoperability between languages without extra serialization overhead. For example, a Scala program can use the Java library to write arrow data and then pass it as a message to a Python program.

Arrow is seeing rapid uptake with a variety of popular frameworks such as Apache Spark. Arrow has also spanned a new data warehouse product; Dremio is a query engine and data warehouse built around Arrow serialization to support fast queries.

## Hybrid Serialization

We use the term hybrid serialization to refer to technologies that combine multiple serialization techniques or integrate serialization with additional abstraction layers, such as schema management. We cite as examples Apache Hudi and Apache Iceberg.

#### Hudi

Hudi stands for Hadoop Update Delete Incremental. This table management technology combines multiple serialization techniques to allow columnar database performance for analytics queries while also supporting atomic, transactional updates. A typical Hudi application is a table that is updated from a CDC stream from a transactional application database. The stream is captured into a row-oriented serialization format, while the bulk of the table is retained in a columnar format. A query runs over both columnar and row-oriented files to return results for the current state of the table. Periodically, a repacking process runs that combines the row and columnar files into updated columnar files to maximize query efficiency.

#### Iceberg

Like Hudi, Iceberg is a table management technology. Iceberg can track all files that make up a table. It can also track files in each table snapshot over time, allowing table time travel in a data lake environment. Iceberg supports schema evolution and can readily manage tables at a petabyte scale.

The following are some columnar file formats:

- **RC files**: This stands for **record columnar files**. They provide many advantages over non-columnar files, such as fast data loading, quick query processing, and highly efficient storage space utilization. RC files are a good option for querying data, but writing them requires more memory and computation. Also, they don't support schema evolution.
- **ORC files**: This stands for **optimized row columnar files**. They have almost the same advantages and disadvantages as RC files. However, ORC files have better compression. They were designed for Hive and cannot be used with non-Hive MapReduce interfaces such as Pig, Java, or Impala.
- **Parquet files**: Parquet is a columnar data format that is suitable for large-scale queries. Parquet is just as good as RC and ORC in terms of performance while reading data, but it is slower when writing compared to other columnar file formats. Parquet supports schema evolution, which is not supported in RC and ORC file formats. Parquet also supports column pruning and predicate pushdown, which are not supported in CSV or JSON.

## Comparing Avro, Parquet, and ORC

![B17525_02_010](https://user-images.githubusercontent.com/62965911/218276979-736b26a9-cb5b-41ed-a43a-fa6b23f29b08.jpeg)

## Comparing Parquet and CSV

While CSV is simple and the most widely used data format (Excel, Google Sheets), there are several distinct advantages for Parquet, including:

- Parquet is column oriented and CSV is row oriented. Row-oriented formats are optimized for OLTP workloads while column-oriented formats are better suited for analytical workloads.
- Column-oriented databases such as AWS Redshift Spectrum bill by the amount data scanned per query
- Therefore, converting CSV to Parquet with partitioning and compression lowers overall costs and improves performance

Parquet has helped its users reduce storage requirements by at least one-third on large datasets, in addition, it greatly improves scan and deserialization time, hence the overall costs.

## Database Storage Engines

To round out the discussion of serialization, we briefly discuss database storage engines. All databases have an underlying storage engine; many don’t expose their storage engines as a separate abstraction (for example, BigQuery, Snowflake). Some (notably, MySQL) support fully pluggable storage engines. Others (e.g., SQL Server) offer major storage engine configuration options (columnar versus row-based storage) that dramatically affect database behavior.

Typically, the storage engine is a separate software layer from the query engine. The storage engine manages all aspects of how data is stored on a disk, including serialization, the physical arrangement of data, and indexes.

Storage engines have seen significant innovation in the 2000s and 2010s. While storage engines in the past were optimized for direct access to spinning disks, modern storage engines are much better optimized to support the performance characteristics of SSDs. Storage engines also offer improved support for modern types and data structures, such as variable-length strings, arrays, and nested data.

Another major change in storage engines is a shift toward columnar storage for analytics and data warehouse applications. SQL Server, PostgreSQL, and MySQL offer robust columnar storage support.

## gzip, bzip2, Snappy

The math behind compression algorithms is complex, but the basic idea is easy to understand: compression algorithms look for redundancy and repetition in data, then reencode data to reduce redundancy. When we want to read the raw data, we decompress it by reversing the algorithm and putting the redundancy back in.

For example, you’ve noticed that certain words appear repeatedly in reading this book. Running some quick analytics on the text, you could identify the words that occur most frequently and create shortened tokens for these words. To compress, you would replace common words with their tokens; to decompress, you would replace the tokens with their respective words.

Perhaps we could use this naive technique to realize a compression ratio of 2:1 or more. Compression algorithms utilize more sophisticated mathematical techniques to identify and remove redundancy; they can often realize compression ratios of 10:1 on text data.

Note that we’re talking about lossless compression algorithms. Decompressing data encoded with a lossless algorithm recovers a bit-for-bit exact copy of the original data. Lossy compression algorithms for audio, images, and video aim for sensory fidelity; decompression recovers something that sounds like or looks like the original but is not an exact copy. Data engineers might deal with lossy compression algorithms in media processing pipelines but not in serialization for analytics, where exact data fidelity is required.

Traditional compression engines such as gzip and bzip2 compress text data extremely well; they are frequently applied to JSON, JSONL, XML, CSV, and other text-based data formats. Engineers have created a new generation of compression algorithms that prioritize speed and CPU efficiency over compression ratio in recent years. Major examples are Snappy, Zstandard, LZFSE, and LZ4. These algorithms are frequently used to compress data in data lakes or columnar databases to optimize for fast query performance.

## <a href="#/02-storage/flat-files/lab-data-loading-python/" target="_blank">Lab: Loading Data in Python ⤻</a>

## <a href="#/02-storage/flat-files/lab-processing-json-data/" target="_blank">Lab: Processing JSON data in Python ⤻</a>
