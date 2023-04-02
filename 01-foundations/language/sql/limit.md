# SQL LIMIT

As you might expect, the limit restricts how many rows the SQL query returns.

**Why should you limit your results?**

Many analysts use limits as a simple way to keep their queries from taking too long to return. The aim of many of your queries will simply be to see what a particular table looks like—you'll want to scan the first few rows of data to get an idea of which fields you care about and how you want to manipulate them. If you query a very large table (such as one with hundreds of thousands or millions of rows) and don't use a limit, you could end up waiting a long time for all of your results to be displayed, which doesn't make sense if you only care about the first few.