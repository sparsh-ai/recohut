# Iceberg

Like Hudi, Iceberg is a table management technology. Iceberg can track all files that make up a table. It can also track files in each table snapshot over time, allowing table time travel in a data lake environment. Iceberg supports schema evolution and can readily manage tables at a petabyte scale.

The following are some columnar file formats:

- **RC files**: This stands for **record columnar files**. They provide many advantages over non-columnar files, such as fast data loading, quick query processing, and highly efficient storage space utilization. RC files are a good option for querying data, but writing them requires more memory and computation. Also, they don't support schema evolution.
- **ORC files**: This stands for **optimized row columnar files**. They have almost the same advantages and disadvantages as RC files. However, ORC files have better compression. They were designed for Hive and cannot be used with non-Hive MapReduce interfaces such as Pig, Java, or Impala.
- **Parquet files**: Parquet is a columnar data format that is suitable for large-scale queries. Parquet is just as good as RC and ORC in terms of performance while reading data, but it is slower when writing compared to other columnar file formats. Parquet supports schema evolution, which is not supported in RC and ORC file formats. Parquet also supports column pruning and predicate pushdown, which are not supported in CSV or JSON.