# Python

### Basics

1. [Stratascratch](./basics/stratascratch/)

### Intermediate

1. [Stratascratch](./intermediate/stratascratch/)

## Note

> Python is a high-level, general-purpose programming language

### Advantages of using Python for Data engineering

Data engineering using Python only gets better, and here is a list of points if you are beginning to think otherwise.

1. The role of a data engineer involves working with different types of data formats. For such cases, Python is best suited. Its standard library supports easy handling of .csv files, one of the most common data file formats.
2. A data engineer is often required to use APIs to retrieve data from databases. The data in such cases is usually stored in JSON (JavaScript Object Notation) format, and Python has a library named JSON-JSON to handle such type of data.
3. The responsibility of a data engineer is not only to obtain data from different sources but also to process it. One of the most popular data process engines is Apache Spark which works with Python DataFrames and even offers an API, PySpark, to build scalable big data projects.
4. Data engineering tools use Directed Acyclic Graphs like Apache Airflow, Apache NiFi, etc. DAGs are nothing but Python codes used for specifying tasks. Thus, learning Python will help data engineers use these tools efficiently.
5. Luigi! No, not the Mario character by Nintendo; we are referring to the Python module that is widely considered a fantastic tool for data engineering.
6. Apart from all the points mentioned above, it is common knowledge that Python is easy to learn and is free to use for the masses. An active community of developers strongly supports it.

### Python Packages for Data Engineers

* **os, pathlib, glob, re (regex)** — These packages serve as building blocks as we start the data engineering journey. These packages allow us to walk the directories and find files.
* **configparser & argparser** — Often we deal with taking user input while running scripts, these package help us in parsing dynamic input and static configurations.
* **requests / urllib3** — As a data engineers we often need to get data from external/internal APIs. These packages helps us in connecting to these APIs and manipulate data.
* **pyscopg2 / mysql-connector-python** — Data engineers often need to interact with RDBMS system to get and store data. These two packages allow us to access database from within our python code.
* **json / pyyaml** — Most API responses are in JSON and we need to handle that. python’s jason package helps us in easy manipulation of json data. Similary YAML is used in many data engineering project as config / manifest. pyyaml helps us to manipulate yaml with python.
* **pandas & numpy** — Defacto python package for data manipulation.
* **boto3 / google-api-core / azure-core** — We invariably interact with one or the other cloud providers for data infrastructure. These packages allow us to access their resources programmatically.
* **pydoop / pyspark / dbt** — As a advanced data engineers we need to interact with big data ecosystem and these packages allow us to work with the distributed frameworks and get the most out of them.
* **sqlalchemy** — As data engineers, we need to constantly interact with different databases. To code for each dialect separately becomes a tedioud jobs. Packages like sqlAlchemy help us out here as an ORM.

## References

1. [Python Data Engineer Interview Questions](https://www.stratascratch.com/blog/python-data-engineer-interview-questions/)
