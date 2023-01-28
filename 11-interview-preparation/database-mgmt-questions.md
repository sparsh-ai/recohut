# Database Management Interview Questions

### What is a relational database?

Answer: A relational database is a type of database that stores data in tables. Tables are composed of rows and columns. Data in relational databases is organized into relations, which are similar to tables.

### What is data skewness?

Answer: Data skewness is a statistical phenomenon that occurs when the distribution of a dataset is not symmetrical. Data skew can impact the performance of data processing and analysis.

### What are the different file storage formats and how do you know when to use them?

Answer: The different file storage formats are text, CSV, JSON, XML, and binary. Each file storage format has its own advantages and disadvantages. The format that you choose should be based on the needs of your project.

### Describe a time you had difficulty merging data. How did you solve this issue?

Answer: I once had difficulty merging data because the data sets were in different formats. I solved this issue by using a data transformation tool to convert the data into the same format.

### How would you design a data warehouse given limited resources?

Answer: I would design a data warehouse by considering the needs of the business. I would also consider the size of the data sets and the resources that are available. I would then choose the appropriate storage format and file structure.

### What is a columnar database? How is it different from a relational database?

Answer: A columnar database is a type of database that stores data in columns. Columnar databases are designed for data warehousing and data analysis. They are different from relational databases because they are optimized for query performance.

### What are the different types of SQL statements?

Answer: The different types of SQL statements are DDL, DML, and DCL.

- DDL statements are used to create and modify tables.
- DML statements are used to query and update data.
- DCL statements are used to control access to the database.

### How would you normalize a database?

Answer: To normalize a database, I would first identify the functional dependencies. I would then create a table for each functional dependency. I would then create relationships between the tables.

### What is your experience with Data Modeling?

Answer: I have experience working with Data Modeling. I have used Data Modeling to create conceptual, logical, and physical data models. I have also used Data Modeling to reverse engineer data models.

### What is your experience with Data Mining?

Answer: I have experience working with Data Mining. I have used Data Mining to discover hidden patterns and trends in data.

## Data Engineer SQL Interview Questions


### Write SQL to insert a new date’s data into a datestamp-partitioned table using incremental data from the other date partitions.

Answer:

```sql
INSERT INTO table_name (date, data)

SELECT date, data

FROM other_table

WHERE date > ‘YYYY-MM-DD’

AND date < ‘YYYY-MM-DD’;
```

### How would you create a view in SQL?

Answer:

```sql
CREATE VIEW view_name AS

SELECT column_name

FROM table_name;
```

### What is a primary key?

Answer: A primary key is a column or set of columns that uniquely identify a row in a table.

### What is a foreign key?

Answer: A foreign key is a column or set of columns that contains a reference to a primary key in another table.

### What is a join? How would you create one in SQL?

Answer: A join is a SQL statement that allows you to combine data from two or more tables. Joins are created using the JOIN keyword. For example, the following SQL statement would join the “customers” and “orders” tables:

```sql
SELECT * FROM customers JOIN orders ON customers.id = orders.customer_id;
```

### How do joins work and what is an example of an inner join?

Answer: Joins work by matching the values in the columns of two or more tables. An inner join is a type of join that returns only rows that have matching values in the columns of both tables. For example,

```sql
SELECT * FROM customers JOIN orders ON customers.id = orders.customer_id;
```

This SQL statement would return all rows from the “customers” and “orders” tables where the id column in the “customers” table matches the customer_id column in the “orders” table.

### What is a self-join? How would you create one in SQL?

Answer: A self-join is a join between two copies of the same table. Self-joins are created using the JOIN keyword. For example, the following SQL statement would join the “customers” table to itself:

```sql
SELECT * FROM customers c1 JOIN customers c2 ON c1.id = c2.id;
```

This SQL statement would return all rows from the “customers” table where the id column in one row matches the id column in another row.

### Write a function that can break a large SMS message string given a length limit per substring. Words must stay together. If a word is longer than the limit, use the word in a new substring and split it as relevant.

```
Example input: “Joe is the funniest guy”, 6

Example output: [“Joe is”, “the”, “funnie”, “st guy”]
```

Answer:

```py
def sms_messages(sms_text_str, limit_int):
    messages = []
    current_message = “”
    for word in sms_text_str.split():
        if len(word) + len(current_message) <= limit:
            current_message += word + “ “
        else:
            messages.append(current_message)
            current_message = word + “ “
            messages.append(current_message)
    return messages
```