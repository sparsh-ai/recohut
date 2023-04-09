# Designing for incremental loading

Incremental loading or delta loading refers to the process of loading smaller increments of data into a storage solution—for example, we could have daily data that is being loaded into a data lake or hourly data flowing into an extract, transform, load (ETL) pipeline, and so on. During data-ingestion scenarios, it is very common to do a bulk upload followed by scheduled incremental loads.

There are mainly two types of data loading which includes Full load and Incremental load.

Full load: The entire dataset is replaced or overwritten with the new dataset. Performing full load is easy in terms of implementation and design. However, the full load process will consume a lot of time when size of data increases.

![](https://user-images.githubusercontent.com/62965911/213924400-566f123a-73b5-413d-9b21-269a74611dd3.png)

Incremental Load: Instead of overwriting the old data, incremental data load identifies the difference between the source data and target data and append the difference to the target data thus increasing the performance significantly especially when one is dealing with huge volume of data. The maintenance is a bit complex.

![](https://user-images.githubusercontent.com/62965911/213924401-5a4b5d49-c5df-46f2-88e8-a937790800dd.png)

There are different ways in which we can design incremental loading. Based on the type of data source, we can have different techniques to implement incremental loading. Some of them are listed here:

## Watermarks

Watermarking is a very simple technique whereby we just keep track of the last record loaded (our watermark) and load all the new records beyond the watermark in the next incremental run.

In relational storage technologies such as SQL databases, we can store the watermark details as just another simple table and automatically update the watermark with stored procedures. Every time a new record is loaded, the stored procedure should get triggered, which will update our watermark table. The next incremental copy pipeline can use this watermark information to identify the new set of records that need to be copied.