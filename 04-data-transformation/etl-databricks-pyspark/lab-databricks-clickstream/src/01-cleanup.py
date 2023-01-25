# Databricks notebook source
# MAGIC %sql 
# MAGIC CREATE DATABASE IF NOT EXISTS aws_cdl_devdays
# MAGIC LOCATION "s3://aws-cdl-devdays/";

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DATABASE aws_cdl_devdays;

# COMMAND ----------

# MAGIC %sql
# MAGIC USE aws_cdl_devdays;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES;

# COMMAND ----------

# DBTITLE 1,Clean up Tables
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS clicks_bronze;
# MAGIC DROP TABLE IF EXISTS clicks_silver;
# MAGIC DROP TABLE IF EXISTS clicks_with_profile;
# MAGIC DROP TABLE IF EXISTS clicks_with_profile_GOLD;
# MAGIC DROP TABLE IF EXISTS clicks_with_profile_GOLD_athena;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Databricks Utilities - dbutils
# MAGIC * You can access DBFS and S3 buckets using the Databricks Utilities class (and other file IO routines).
# MAGIC * An instance of DBUtils is already declared for us as `dbutils`.
# MAGIC * For in-notebook documentation on DBUtils you can execute the command `dbutils.help()`.
# MAGIC * See also <a href="https://docs.databricks.com/user-guide/dbutils.html" target="_blank">Databricks Utilities - dbutils</a>

# COMMAND ----------

display(dbutils.fs.ls("/databricks-datasets"))

# COMMAND ----------

# MAGIC %fs ls "s3://aws-cdl-devdays"

# COMMAND ----------

# DBTITLE 1,Clean up the aws-cdl-devdays S3 bucket working folders
dbutils.fs.rm("s3://aws-cdl-devdays/clicks-bronze", True)
dbutils.fs.rm("s3://aws-cdl-devdays/clicks-silver", True)
dbutils.fs.rm("s3://aws-cdl-devdays/clicks-with-profile", True)
dbutils.fs.rm("s3://aws-cdl-devdays/clicks_with_profile_GOLD", True)
dbutils.fs.rm("s3://aws-cdl-devdays/checkpoint-clicks-bronze", True)
dbutils.fs.rm("s3://aws-cdl-devdays/checkpoint-clicks-silver", True)

# COMMAND ----------

# MAGIC %md
# MAGIC ###Notebooks support <a href="https://github.com/KaTeX/KaTeX/wiki" target="_blank">KaTeX</a> for displaying mathematical formulas and equations
# MAGIC 
# MAGIC \\( f(\beta)= -Y_t^T X_t \beta + \sum log( 1+{e}^{X_t\bullet\beta}) + \frac{1}{2}\delta^t S_t^{-1}\delta\\)
# MAGIC 
# MAGIC where \\(\delta=(\beta - \mu_{t-1})\\)

# COMMAND ----------

# MAGIC %md
# MAGIC ### [Back to the main demo - Step2](https://field-eng.cloud.databricks.com/#notebook/1566801/command/1566808)
