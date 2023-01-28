# Mistplay Data Engineer Take Home Challenge

This is an exercise for you to demonstrate your design and implementation skills to solve a typical data engineering problem.
We are looking for 3 key things on this exercise:

 1. Detailed Design
 2. Key considerations like data checks and standards
 3. Approach to solve the problem which is modular

## Project Set up Standards

You are expected to create the feature branch as such its deployable and have following components:

 1. DockerFile
 2. Docker Compose
 3. Docker should include Airflow, Kafka, Spark and database for airflow

Fork the github repo and Once you've completed the challenge create a PR.

## ELT workflow Tasks

 1. Create a job which load the data into kafka topics
 2. Create a pipeline which extract the messages from kafka and load it into raw layer using spark or flink or beam.
 3. Create a pipeline for data quality checks and transform the data into curated schema using airflow and spark as a batch job.

For this exercise sample data has been provided under `sample_data`. Once the data loaded work on the Analytics task mentioned below.

## Analytical Tasks

 1. Write down the data quality issues with the datasets provided and the steps performed to clean (if any).
 2. Display the distribution of sales by product name and product type.
 3. Calculate the total amount of all transactions that happened in year 2013 and have not been refunded as of today.
 4. Display the customer name who made the second most purchases in the month of May 2013. Refunds should be excluded.
 5. Find a product that has not been sold at least once (if any).
 6. Calculate the total number of users who purchased the same product consecutively at least 2 times on a given day.
 7. Display all the details of a customer who is currently living at 1154 Winters Blvd.

## Guidelines

 1. You are allowed to use any language and any libraries you wish. However, you should be able to justify your technical decisions.
 2. Make sure you create a design diagram and different approaches as write up document in to repo as elt_readme which included deployments instruction as well.
 3. Feel free to use any reference resources available to you (but please don't have another engineer help you directly.)
 4. The challenge expectation is to complete in 2 days.

All the best for the challenge!