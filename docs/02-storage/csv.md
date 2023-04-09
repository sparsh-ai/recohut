# CSV: The nonstandard standard

CSV is a serialization format that data engineers love to hate. The term CSV is essentially a catchall for delimited text, but there is flexibility in conventions of escaping, quote characters, delimiter, and more.

Data engineers should avoid using CSV files in pipelines because they are highly error-prone and deliver poor performance. Engineers are often required to use CSV format to exchange data with systems and business processes outside their control. CSV is a common format for data archival. If you use CSV for archival, include a complete technical description of the serialization configuration for your files so that future consumers can ingest the data.

CSV (Comma Separated Values) is a simple file format used for storing tabular data, where each line of the file represents a single row and each value in a row is separated by a comma.

Advantages:

- Easy to read and write
- Can be easily imported into a wide range of data analysis tools
- Small file size

Disadvantages:

- Not efficient for storing large data sets with complex data types
- Can lead to data loss if values contain commas or line breaks
- Limited support for encoding

Application: CSV is commonly used for small data sets and as a standard format for data exchange between different applications.

Example

```
name,age,gender
John,25,M
Jane,32,F
Bob,45,M
```