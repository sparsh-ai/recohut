# Flat Files

Storage formats are a way to define how data is stored in a file. Hadoop doesn't have a default file format, but it supports multiple file formats for storing data. Some of the common storage formats for Hadoop are as follows:

- Text files
- Sequence files
- Parquet files
- **Record-columnar (RC)** files
- **Optimized row columnar (ORC)** files
- Avro files

Choosing a write file format will provide significant advantages, such as the following:

- Optimized performance while reading and writing data
- Schema evolution support (allows us to change the attributes in a dataset)
- Higher compression, resulting in less storage space being required
- Splittable files (files can be read in parts)

Let's focus on columnar storage formats as they are widely used in big data applications because of how they store data and can be queried by the SQL engine. The columnar format is very useful when a subset of data needs to be referred to. However, when most of the columns in a dataset need to be fetched, then row-oriented storage formats are beneficial.

The following are some columnar file formats:

- **RC files**: This stands for **record columnar files**. They provide many advantages over non-columnar files, such as fast data loading, quick query processing, and highly efficient storage space utilization. RC files are a good option for querying data, but writing them requires more memory and computation. Also, they don't support schema evolution.
- **ORC files**: This stands for **optimized row columnar files**. They have almost the same advantages and disadvantages as RC files. However, ORC files have better compression. They were designed for Hive and cannot be used with non-Hive MapReduce interfaces such as Pig, Java, or Impala.
- **Parquet files**: Parquet is a columnar data format that is suitable for large-scale queries. Parquet is just as good as RC and ORC in terms of performance while reading data, but it is slower when writing compared to other columnar file formats. Parquet supports schema evolution, which is not supported in RC and ORC file formats. Parquet also supports column pruning and predicate pushdown, which are not supported in CSV or JSON.

## CSV

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

## JSON

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

## Parquet

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

## Avro

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

## ORC

ORC (Optimized Row Columnar) is an open-source, *columnar *storage format for Hadoop-based data processing systems, such as Hive and Pig. It is designed to provide better performance for large-scale data processing, especially for queries that involve reading or filtering large subsets of columns in a dataset.

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

## Comparison

#### Comparing Avro, Parquet, and ORC

![B17525_02_010](https://user-images.githubusercontent.com/62965911/218276979-736b26a9-cb5b-41ed-a43a-fa6b23f29b08.jpeg)

#### Comparing Parquet and CSV

While CSV is simple and the most widely used data format (Excel, Google Sheets), there are several distinct advantages for Parquet, including:

- Parquet is column oriented and CSV is row oriented. Row-oriented formats are optimized for OLTP workloads while column-oriented formats are better suited for analytical workloads.
- Column-oriented databases such as AWS Redshift Spectrum bill by the amount data scanned per query
- Therefore, converting CSV to Parquet with partitioning and compression lowers overall costs and improves performance

Parquet has helped its users reduce storage requirements by at least one-third on large datasets, in addition, it greatly improves scan and deserialization time, hence the overall costs.
