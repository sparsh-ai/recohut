// Databricks notebook source
val covid_raw_data = spark.read.format("csv")
.option("header", "true")
.option("inferSchema", "true")
.load("/FileStore/shared_uploads/sprsag@gmail.com/covid_data.csv")

// COMMAND ----------

display(covid_raw_data)

// COMMAND ----------

covid_raw_data.count()

// COMMAND ----------

val covid_remove_duplicates = covid_raw_data.dropDuplicates()

// COMMAND ----------

covid_remove_duplicates.printSchema()

// COMMAND ----------

val covid_selected_columns = covid_remove_duplicates.select("iso_code","location","continent","date","new_deaths_per_million","people_fully_vaccinated","population")

// COMMAND ----------

val covid_clean_data = covid_selected_columns.na.drop()
covid_clean_data.count()

// COMMAND ----------

covid_clean_data.createOrReplaceTempView("covid_view")

// COMMAND ----------

// MAGIC %sql
// MAGIC SELECT iso_code, location, continent,
// MAGIC SUM(new_deaths_per_million) as death_sum,
// MAGIC MAX(people_fully_vaccinated * 100 / population) as percentage_vaccinated FROM covid_view
// MAGIC WHERE population > 1000000
// MAGIC GROUP BY iso_code,location,continent
// MAGIC ORDER BY death_sum desc

// COMMAND ----------


