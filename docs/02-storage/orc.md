# ORC

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