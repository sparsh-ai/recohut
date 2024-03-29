# SQL Comparison Operators

**Comparison operators on numerical data**

The most basic way to filter data is using comparison operators. The easiest way to understand them is to start by looking at a list of them:

| Equal to                 | `=`          |
|--------------------------|--------------|
| Not equal to             | `<>` or `!=` |
| Greater than             | `>`          |
| Less than                | `<`          |
| Greater than or equal to | `>=`         |
| Less than or equal to    | `<=`         |

These comparison operators make the most sense when applied to numerical columns.

**Comparison operators on non-numerical data**

All of the above operators work on non-numerical data as well. `=` and `!=` make perfect sense—they allow you to select rows that match or don't match any value, respectively.

There are some important rules when using these operators, though. If you're using an operator with values that are non-numeric, you need to put the value in single quotes: 'value'.

You can use `>`, `<`, and the rest of the comparison operators on non-numeric columns as well---they filter based on alphabetical order.

If you're using `>`, `<`, `>=`, or `<=`, you don't necessarily need to be too specific about how you filter.

**Arithmetic in SQL**

You can perform arithmetic in SQL using the same operators you would in Excel: `+`, `-`, `*`, `/`. However, in SQL you can only perform arithmetic across columns on values in a given row. To clarify, you can only add values in multiple columns *from the same row* together using `+`---if you want to add values across multiple rows, you'll need to use aggregate functions.

The columns that contain the arithmetic functions are called "derived columns" because they are generated by modifying the information that exists in the underlying data.

As in Excel, you can use parentheses to manage the order of operations.

It occasionally makes sense to use parentheses even when it's not absolutely necessary just to make your query easier to read.