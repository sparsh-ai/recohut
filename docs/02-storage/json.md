# JSON and JSONL

JavaScript Object Notation (JSON) has emerged as the new standard for data exchange over APIs, and it has also become an extremely popular format for data storage. In the context of databases, the popularity of JSON has grown apace with the rise of MongoDB and other document stores. Databases such as Snowflake, BigQuery, and SQL Server also offer extensive native support, facilitating easy data exchange between applications, APIs, and database systems.

JSON Lines (JSONL) is a specialized version of JSON for storing bulk semistructured data in files. JSONL stores a sequence of JSON objects, with objects delimited by line breaks. From our perspective, JSONL is an extremely useful format for storing data right after it is ingested from API or applications. However, many columnar formats offer significantly better performance. Consider moving to another format for intermediate pipeline stages and serving.

JSON (JavaScript Object Notation) is a lightweight file format used for storing and exchanging data, which is based on the JavaScript programming language. It is a text-based format that uses a key-value structure to represent data.

Advantages:

- Human-readable and easy to understand
- Can be easily parsed and manipulated with different programming languages
- Supports complex data types, such as arrays and nested objects

Disadvantages:

- Can be less efficient for storing and processing large data sets compared to other binary formats
- Limited support for data compression

Application: JSON is commonly used for web APIs, NoSQL databases, and as a data exchange format between different applications.

Example:

```
{
   "name": "John",
   "age": 25,
   "gender": "M"
},
{
   "name": "Jane",
   "age": 32,
   "gender": "F"
},
{
   "name": "Bob",
   "age": 45,
   "gender": "M"
}
```