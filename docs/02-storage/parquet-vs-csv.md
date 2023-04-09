# Parquet vs CSV

While CSV is simple and the most widely used data format (Excel, Google Sheets), there are several distinct advantages for Parquet, including:

- Parquet is column oriented and CSV is row oriented. Row-oriented formats are optimized for OLTP workloads while column-oriented formats are better suited for analytical workloads.
- Column-oriented databases such as AWS Redshift Spectrum bill by the amount data scanned per query
- Therefore, converting CSV to Parquet with partitioning and compression lowers overall costs and improves performance

Parquet has helped its users reduce storage requirements by at least one-third on large datasets, in addition, it greatly improves scan and deserialization time, hence the overall costs.