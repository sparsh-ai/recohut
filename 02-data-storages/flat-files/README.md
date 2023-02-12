# Flat Files

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
