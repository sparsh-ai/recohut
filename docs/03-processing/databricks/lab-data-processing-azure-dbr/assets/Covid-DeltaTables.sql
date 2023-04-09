-- Databricks notebook source
CREATE DATABASE covid

-- COMMAND ----------

CREATE TEMPORARY VIEW covid_data
USING CSV
OPTIONS (path "/FileStore/shared_uploads/sprsag@gmail.com/covid_data.csv", header "true", mode "FAILFAST")

-- COMMAND ----------

CREATE OR REPLACE TABLE covid.covid_data_delta
USING DELTA
LOCATION '/FileStore/shared_uploads/sprsag@gmail.com/covid_data_delta'
AS
SELECT iso_code,location,continent,date,new_deaths_per_million,people_fully_vaccinated,population FROM covid_data

-- COMMAND ----------

DELETE FROM covid.covid_data_delta where population is null or people_fully_vaccinated is null or new_deaths_per_million is null or location is null

-- COMMAND ----------

delete from covid.covid_data_delta;
Select count(*) from covid.covid_data_delta;

-- COMMAND ----------

select * from covid.covid_data_delta version as of 0;

-- COMMAND ----------

RESTORE TABLE covid.covid_data_delta TO VERSION AS OF 0;

-- COMMAND ----------

UPDATE covid.covid_data_delta SET population = population * 1.2 WHERE continent = 'Asia';

-- COMMAND ----------

DELETE FROM covid.covid_data_delta  WHERE continent = 'Europe';

-- COMMAND ----------

MERGE INTO covid.covid_data_delta source
USING covid.covid_data_delta TIMESTAMP AS OF "2023-02-11 11:12:00" target
ON source.location = target.location and source.date = target.date
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED
THEN INSERT *

-- COMMAND ----------


