# Parquet

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
