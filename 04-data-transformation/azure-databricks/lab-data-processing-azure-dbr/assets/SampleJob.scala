// Databricks notebook source
val diamonds = spark.read.format("csv")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")

// COMMAND ----------

diamonds.createOrReplaceTempView("diamonds_view")

// COMMAND ----------

// MAGIC %sql
// MAGIC Select cut, color, avg(price) as avg_price, max(price) as max_price
// MAGIC From diamonds_view
// MAGIC Group by cut,color
// MAGIC order by avg_price desc, cut, color
