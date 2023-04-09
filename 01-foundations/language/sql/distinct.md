# SQL DISTINCT

You'll occasionally want to look at only the unique values in a particular column. You can do this using SELECT DISTINCT syntax.

DISTINCT can be particularly helpful when exploring a new data set. In many real-world scenarios, you will generally end up writing several preliminary queries in order to figure out the best approach to answering your initial question. Looking at the unique values on each column can help identify how you might want to group or filter the data.

You can use DISTINCT when performing an aggregation. You'll probably use it most commonly with the COUNT function.

It's worth noting that using DISTINCT, particularly in aggregations, can slow your queries down quite a bit.