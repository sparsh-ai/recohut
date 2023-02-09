# Incremental Data Load

There are mainly two types of data loading which includes Full load and Incremental load.

Full load: The entire dataset is replaced or overwritten with the new dataset. Performing full load is easy in terms of implementation and design. However, the full load process will consume a lot of time when size of data increases.

![](https://user-images.githubusercontent.com/62965911/213924400-566f123a-73b5-413d-9b21-269a74611dd3.png)

Incremental Load: Instead of overwriting the old data, incremental data load identifies the difference between the source data and target data and append the difference to the target data thus increasing the performance significantly especially when one is dealing with huge volume of data. The maintenance is a bit complex.

![](https://user-images.githubusercontent.com/62965911/213924401-5a4b5d49-c5df-46f2-88e8-a937790800dd.png)

