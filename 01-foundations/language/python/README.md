# Python

Python is a high-level, general-purpose programming language.

## Basics

### Fundamentals

A strong understanding of Python syntax, data types, operators, and control structures is essential.

Some key concepts under Basic Python that data engineers should be familiar :

1. Variables and Data Types: Data engineers should know how to create and manipulate variables of different data types such as integers, floats, strings, and Booleans.
2. Control Structures: Control structures such as if-else statements, loops, and functions are essential for writing efficient and reusable code.
3. Operators: Data engineers should be comfortable with different types of operators like arithmetic, comparison, and logical operators.
4. Input and Output: Data engineers should know how to handle input and output operations in Python, such as reading user input and writing output to the console.
5. Exception Handling: Exception handling is important for dealing with errors and unexpected events that may occur during code execution.
6. Python Built-in Functions: Data engineers should be familiar with commonly used built-in functions in Python such as Len(), range(), print(), and type().

### Data Structures

Data engineers should be proficient in working with data structures like lists, tuples, sets, and dictionaries.

In Python, data structures are containers that hold data in an organized and efficient manner. Some commonly used data structures that data engineers should be proficient in working:

1. Lists: Lists are ordered collections of items that can be of different data types. They are mutable, which means that their contents can be modified after creation.
2. Tuples: Tuples are similar to lists, but they are immutable, meaning that their contents cannot be modified after creation. They are often used to represent fixed sets of data.
3. Sets: Sets are unordered collections of unique items. They are often used to perform set operations like union, intersection, and difference.
4. Dictionaries: Dictionaries are unordered collections of key-value pairs. They are often used to store and retrieve data based on a unique identifier.

Data engineers should be familiar with the operations that can be performed on these data structures, such as adding and removing items, accessing items by index or key, and iterating over items. They should also understand the performance characteristics of each data structure and choose the appropriate one for the task at hand.

Knowledge of data structures is important for efficient data manipulation and analysis in data engineering. In addition to the built-in data structures, data engineers should also be familiar with external libraries that provide specialized data structures for specific use cases.

### Object-Oriented Programming (OOP)

Knowledge of OOP concepts like classes, objects, inheritance, encapsulation, and polymorphism is important.

Object-Oriented Programming is a programming paradigm that organizes code into reusable, modular units called objects. OOP is an important concept for data engineers to understand because many Python libraries and frameworks are built on OOP principles.

Some key concepts of OOP that data engineers should be familiar:

1. Classes: Classes are blueprints for objects that define their properties and behavior.
2. Objects: Objects are instances of a class that contains data and methods.
3. Inheritance: Inheritance is a mechanism for creating new classes based on existing ones.
4. Encapsulation: Encapsulation is the concept of bundling data and methods together in a class, and controlling access to them through methods.
5. Polymorphism: Polymorphism is the ability of objects of different classes to be treated as if they are the same type.

Data engineers should be able to define and use classes, create objects, and implement inheritance, encapsulation, and polymorphism in their code. OOP can help data engineers write more organized, modular, and reusable code that is easier to maintain and extend.

In addition to OOP, data engineers should also be familiar with other programming paradigms like functional programming, which emphasizes the use of pure functions and immutable data structures. A strong understanding of both OOP and functional programming can help data engineers write more efficient and scalable code.

## Intermediate

### File handling

Data engineers should be able to read from and write to files using Python's built-in functions.

File handling is an essential skill for data engineers, as they often need to read data from files, process it, and write the results to other files. In Python, file handling is done using built-in functions like `open()`, `read()`, `write()`, and `close()`.

Some key concepts related to file handling that data engineers should be familiar with are:

1. Opening files: Data engineers should know how to open files in different modes (read, write, append) using the `open()` function.
2. Reading files: Once a file is opened, data engineers should know how to read its contents using functions like `read()`, `readline()`, and `readlines()`.
3. Writing files: Data engineers should know how to write data to files using functions like `write()`.
4. Closing files: It's important to close files after they are opened, to free up system resources and prevent data loss.
5. Exception handling: Data engineers should be familiar with handling errors that can occur during file handling operations, such as file not found errors, permission errors, and disk full errors.

In addition to the basic concepts of file handling, data engineers should also be familiar with common file formats used in data engineering, such as CSV, JSON, and XML. They should know how to read and write data in these formats using Python's built-in functions or third-party libraries like `csv`, `json`, and `xml.etree.ElementTree`. Being proficient in file handling can help data engineers work with large amounts of data efficiently and effectively.

### Regular expressions

Regular expressions are essential for working with text data, so data engineers should be comfortable using them.

Regular expressions, or regex, are a powerful tool for working with text data. They allow data engineers to search for, match and manipulate text patterns flexibly and efficiently.

Some important concepts related to a regex that data engineers should be familiar with are:

1. Basic syntax: Regular expressions consist of special characters and patterns that are used to match specific text patterns. Data engineers should be familiar with basic syntaxes like character classes, quantifiers, and anchors.
2. Meta-characters: Regular expressions use a variety of meta-characters to match specific types of characters or sequences of characters. For example, the dot (.) meta-character matches any single character, while the star (*) matches zero or more occurrences of the preceding pattern.
3. Groups: Data engineers should know how to use groups in regular expressions to capture specific parts of a text pattern for further processing.
4. Lookarounds: Lookarounds are advanced regular expression concepts that allow data engineers to search for patterns that are preceded or followed by specific text patterns.
5. Greedy vs. non-greedy matching: Regular expressions use a greedy matching strategy by default, which matches the longest possible text pattern. Data engineers should be familiar with non-greedy matching strategies, which match the shortest possible text pattern.

### Libraries

* **os, pathlib, glob, re (regex)** — These packages serve as building blocks as we start the data engineering journey. These packages allow us to walk the directories and find files.
* **configparser & argparser** — Often we deal with taking user input while running scripts, these package help us in parsing dynamic input and static configurations.
* **requests / urllib3** — As a data engineers we often need to get data from external/internal APIs. These packages helps us in connecting to these APIs and manipulate data.
* **pyscopg2 / mysql-connector-python** — Data engineers often need to interact with RDBMS system to get and store data. These two packages allow us to access database from within our python code.
* **json / pyyaml** — Most API responses are in JSON and we need to handle that. python’s jason package helps us in easy manipulation of json data. Similary YAML is used in many data engineering project as config / manifest. pyyaml helps us to manipulate yaml with python.
* **pandas & numpy** — NumPy is a library for working with large, multi-dimensional arrays and matrices. It provides fast and efficient array operations and mathematical functions. Pandas is a library for data manipulation and analysis. It provides data structures like DataFrames and Series for working with tabular data, and functions for cleaning, transforming, and analyzing data.
* **boto3 / google-api-core / azure-core** — We invariably interact with one or the other cloud providers for data infrastructure. These packages allow us to access their resources programmatically.
* **pydoop / pyspark / dbt** — As a advanced data engineers we need to interact with big data ecosystem and these packages allow us to work with the distributed frameworks and get the most out of them.
* **sqlalchemy** — As data engineers, we need to constantly interact with different databases. To code for each dialect separately becomes a tedioud jobs. Packages like sqlAlchemy help us out here as an ORM.

## Advanced

### Database connectivity

Data engineers should know how to connect to databases, perform CRUD operations, and write efficient SQL queries using libraries like SQLAlchemy.

Data engineers often work with databases, so it's important for them to be proficient in connecting to databases, performing CRUD operations, and writing efficient SQL queries. Some of the most popular Python libraries for database connectivity:

1. SQLAlchemy: is a powerful and flexible Object-Relational Mapping (ORM) library that provides a high-level interface for working with databases. It supports a wide range of database backends, including MySQL, PostgreSQL, Oracle, and Microsoft SQL Server.
2. Psycopg2: Psycopg2 is a PostgreSQL adapter for Python that provides a low-level interface for working with PostgreSQL databases. It allows you to execute SQL statements, manage transactions, and retrieve results.
3. PyMySQL: is a MySQL adapter for Python that provides a simple and easy-to-use interface for working with MySQL databases. It supports all MySQL database versions from 3.23 to 8.0.
4. sqlite3 provides a simple and lightweight interface for working with SQLite databases. It allows you to execute SQL statements, manage transactions, and retrieve results.

### Parallel processing

Familiarity with parallel processing libraries like Multiprocessing and Threading is essential for optimizing code performance.

Parallel processing is the technique of executing multiple processes or threads simultaneously to achieve better performance and efficiency. In data engineering, parallel processing can be useful for optimizing code performance when working with large datasets, running multiple computations at once, or performing multiple I/O operations.

### Lambda Functions

Writing python code to run in AWS Lambda functions.

### Data Pipelines

Writing python code to be run as Airflow DAG.

### Joins and Aggregations

Using pandas and polars for advanced joins and aggregation operations.

Resources - Stratascratch

### Developer Best Practices

- Testing - Unittest and Pytest
- Logging

## Advantages of using Python for Data engineering

Data engineering using Python only gets better, and here is a list of points if you are beginning to think otherwise.

1. The role of a data engineer involves working with different types of data formats. For such cases, Python is best suited. Its standard library supports easy handling of .csv files, one of the most common data file formats.
2. A data engineer is often required to use APIs to retrieve data from databases. The data in such cases is usually stored in JSON (JavaScript Object Notation) format, and Python has a library named JSON-JSON to handle such type of data.
3. The responsibility of a data engineer is not only to obtain data from different sources but also to process it. One of the most popular data process engines is Apache Spark which works with Python DataFrames and even offers an API, PySpark, to build scalable big data projects.
4. Data engineering tools use Directed Acyclic Graphs like Apache Airflow, Apache NiFi, etc. DAGs are nothing but Python codes used for specifying tasks. Thus, learning Python will help data engineers use these tools efficiently.
5. Luigi! No, not the Mario character by Nintendo; we are referring to the Python module that is widely considered a fantastic tool for data engineering.
6. Apart from all the points mentioned above, it is common knowledge that Python is easy to learn and is free to use for the masses. An active community of developers strongly supports it.

## Labs

1. Python Basics
   1. Lists and dictionaries
   2. For loops and while loops
   3. Functions and Inline functions
   4. Reading data from flat files - csv, json, parquet, avro, excel, txt
2. Python Intermediate
   1. Read/Write and Manipulate Data using Pandas
3. Python Advanced
   1. Pulling data from APIs using requests library
   2. Reading and writing data to databases using psycopg2 and sqlalchemy library
   3. Reading data from S3 and athena using aws data wrangler library
   4. Pull credentials from Secrets Manager using boto3 library
4. [ETL process and reading/writing CSV, JSON and XML files in panda](01-foundations/language/python/lab-etl-csv-json-xml/)
5. [Exchange Rate ETL process](01-foundations/language/python/lab-exchange-rate-etl/)
6. [Basic Text Handling with Python](18-nlp/lab-basic-text-handlng-python/)

## References

1. [Python Data Engineer Interview Questions](https://www.stratascratch.com/blog/python-data-engineer-interview-questions/)
2. https://scrimba.com/learn/python
