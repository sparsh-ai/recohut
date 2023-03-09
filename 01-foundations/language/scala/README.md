# Scala

## Why Scala?

- Expressive
  - First-class functions
  - Closures
- Concise
  - Type inference
  - Literal syntax for function creation
- Java interoperability
  - Can reuse java libraries
  - Can reuse java tools
  - No performance penalty

## How Scala?

- Compiles to java bytecode
- Works with any standard JVM
  - Or even some non-standard JVMs like Dalvik
  - Scala compiler written by author of Java compiler

## How to install

```
pip install spylon-kernel
python -m spylon_kernel install
```

To install scala in Anaconda, first create an empty venv (`env-scala` in our case) and then install the scala from `anaconda-cluster` channel.

```
conda create -n env-scala
conda install -c anaconda-cluster scala
conda install -c conda-forge spylon-kernel
```

## Labs

1. Introduction to Scala programming
2. Getting started with Spark Scala
3. [Building extract and load pipeline with Scala, S3 and Postgres](03-processing/databricks/lab-databricks-scala-postgres-s3/)
