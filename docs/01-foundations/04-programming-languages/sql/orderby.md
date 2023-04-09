# SQL ORDER BY

The ORDER BY clause allows you to reorder your results based on the data in one or more columns.

You can also order by mutiple columns. This is particularly useful if your data falls into categories and you'd like to organize rows by date, for example, but keep all of the results within a given category together.

When using ORDER BY with a row limit (either through the check box on the query editor or by typing in LIMIT), the ordering clause is executed first. This means that the results are ordered before limiting to only a few rows.