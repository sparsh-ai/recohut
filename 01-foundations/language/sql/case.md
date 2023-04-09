# SQL CASE

The CASE statement is SQL's way of handling if/then logic. The CASE statement is followed by at least one pair of WHEN and THEN statements—SQL's equivalent of IF/THEN in Excel. Because of this pairing, you might be tempted to call this SQL CASE WHEN, but CASE is the accepted term.

Every CASE statement must end with the END statement. The ELSE statement is optional, and provides a way to capture values not specified in the WHEN/THEN statements.

You can also define a number of outcomes in a CASE statement by including as many WHEN/THEN statements as you'd like.

You can also string together multiple conditional statements with AND and OR the same way you might in a WHERE clause.

CASE's slightly more complicated and substantially more useful functionality comes from pairing it with aggregate functions. For example, let's say you want to only count rows that fulfill a certain condition. Since COUNT ignores nulls, you could use a CASE statement to evaluate the condition and produce null or non-null values depending on the outcome.

Combining CASE statements with aggregations can be tricky at first. It's often helpful to write a query containing the CASE statement first and run it on its own.