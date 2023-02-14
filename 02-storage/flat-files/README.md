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

### Comparison

#### Comparing Avro, Parquet, and ORC

![B17525_02_010](https://user-images.githubusercontent.com/62965911/218276979-736b26a9-cb5b-41ed-a43a-fa6b23f29b08.jpeg)

#### Comparing Parquet and CSV

While CSV is simple and the most widely used data format (Excel, Google Sheets), there are several distinct advantages for Parquet, including:

- Parquet is column oriented and CSV is row oriented. Row-oriented formats are optimized for OLTP workloads while column-oriented formats are better suited for analytical workloads.
- Column-oriented databases such as AWS Redshift Spectrum bill by the amount data scanned per query
- Therefore, converting CSV to Parquet with partitioning and compression lowers overall costs and improves performance

Parquet has helped its users reduce storage requirements by at least one-third on large datasets, in addition, it greatly improves scan and deserialization time, hence the overall costs.

## Parquet

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

### Parquet and Schema evolution

When using columnar file formats like Parquet, users can start with a simple schema, and gradually add more columns to the schema as needed. In this way, users may end up with multiple Parquet files with different but mutually compatible schemas. In these cases, Parquet supports automatic schema merging among these files.

Read more about parquet here:

- https://www.databricks.com/glossary/what-is-parquet
