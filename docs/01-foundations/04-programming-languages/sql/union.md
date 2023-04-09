# SQL UNION

SQL joins allow you to combine two datasets side-by-side, but UNION allows you to stack one dataset on top of the other. Put differently, UNION allows you to write two separate SELECT statements, and to have the results of one statement display in the same table as the results from the other statement.

SQL has strict rules for appending data:

- Both tables must have the same number of columns
- The columns must have the same data types in the same order as the first table

While the column names don't necessarily have to be the same, you will find that they typically are. This is because most of the instances in which you'd want to use UNION involve stitching together different parts of the same dataset.