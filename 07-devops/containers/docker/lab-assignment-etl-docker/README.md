# ETL Docker

## Objective

Data Transformation and Containerization

## Problem

An address provider returns addresses only with concatenated street names and numbers. Our own system on the other hand has separate fields for street name and street number.

### Input

string of address

### Output

string of street and string of street-number as JSON object

### Examples

1. Write a simple program that does the task for the most simple cases, e.g.
   1. `"Winterallee 3"` -> `{"street": "Winterallee", "housenumber": "3"}`
   1. `"Musterstrasse 45"` -> `{"street": "Musterstrasse", "housenumber": "45"}`
   1. `"Blaufeldweg 123B"` -> `{"street": "Blaufeldweg", "housenumber": "123B"}`

2. Consider more complicated cases
   1. `"Am Bächle 23"` -> `{"street": "Am Bächle", "housenumber": "23"}`
   1. `"Auf der Vogelwiese 23 b"` -> `{"street": "Auf der Vogelwiese", "housenumber": "23 b"}`

3. Consider other countries (complex cases)
   1. `"4, rue de la revolution"` -> `{"street": "rue de la revolution", "housenumber": "4"}`
   1. `"200 Broadway Av"` -> `{"street": "Broadway Av", "housenumber": "200"}`
   1. `"Calle Aduana, 29"` -> `{"street": "Calle Aduana", "housenumber": "29"}`
   1. `"Calle 39 No 1540"` -> `{"street": "Calle 39", "housenumber": "No 1540"}`

### Instructions

When choosing your approach of implementation, please keep following things in mind:

* While we will try to evaluate all code that you share, keep in mind that we will feel most comfortable with the tools we know:
    * Python
    * Pandas
    * PySpark
    * SQL
* We prefer quality over speed. It does not only matter if your solution yields correct results, but we will also take a close look on your overall project structure, the tools used, test coverage, documentation, etc.