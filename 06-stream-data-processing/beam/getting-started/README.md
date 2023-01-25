# Apache Beam Getting Started

## Pipeline 1 - Simple Ingest Data Pipeline

![pipeline1](https://user-images.githubusercontent.com/62965911/214569069-8223b7f5-270d-447c-b0be-c43748d3135f.png)

Notebook: `01-sa-ingest-data-pipeline.ipynb`

## Pipeline 2 - Wordcount

It demonstrates a simple pipeline that uses the Direct Runner to read from a text file, apply transforms to tokenize and count the words, and write the data to an output text file.

![pipeline2](https://user-images.githubusercontent.com/62965911/214569078-1a8cde98-75f6-4e9c-8663-71d8d41e6f94.svg)

Key Concepts:

-   Creating the Pipeline
-   Applying transforms to the Pipeline
-   Reading input
-   Applying ParDo transforms
-   Applying SDK-provided transforms (in this example: Count)
-   Writing output
-   Running the Pipeline

Notebook: `02-sa-wordcount-pipeline.ipynb`

## Apache Beam Basic Operations

In this tutorial, we will learn about:

1. Create and print input data
1. Read data from files
1. Write data into files
1. Read data from SQLite database
1. Map, FlatMap, Reduce, and Combine functions

Notebook: `03-sa-basic-operations.ipynb`

## Windowing

In this tutorial, we will learn about:

1. Global windows
1. Fixed-time windows
1. Sliding-time windows
1. Session windows

Notebook: `04-sa-windowing.ipynb`

## Dataframes

In this tutorial, we will learn about:

1. Pandas dataframe to Beam Dataframe
1. Pandas dataframe to PCollections
1. Beam Dataframe to Pandas dataframe
1. PCollections to Pandas dataframe
1. Beam Dataframe to PCollections
1. PCollections to Beam Dataframe

Notebook: `05-sa-dataframes.ipynb`
