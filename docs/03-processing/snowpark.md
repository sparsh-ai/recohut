# Snowpark

### What is Snowpark

Snowpark at its core provides an API that developers can use to construct DataFrames that are executed lazily on Snowflake's platform. It enables data engineers, data scientists, and developers coding in languages other than SQL such as Python to take advantage of Snowflake's powerful platform without having to first move data out of Snowflake. This enables data application developers to run complex transformations within Snowflake while taking advantage of the built-in unlimited scalability, performance, governance and security features.

Use Python, Java or Scala with familiar DataFrame and custom function support to build powerful and efficient pipelines, machine learning (ML) workflows, and data applications. And gain the performance, ease of use, governance, and security while working inside Snowflake’s Data Cloud.

### Theory

- DBT generates a wrapper around the python model code that returns a Snowpark data frame.
- The model code gets executed using Stored Procedures, that can be configured as Anonymous or Permanent.
- Anaconda packages and other third-party packages can be specified in PACKAGES and IMPORTS respectively.
