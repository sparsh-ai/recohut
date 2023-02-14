# Databricks notebook source
# MAGIC %md ### Writing to Redshift
# MAGIC `spark-redshift` will first create the table in Redshift using JDBC. It then copies the partitioned RDD encapsulated by the source DataFrame instance to the temporary S3 folder. Finally, it executes the Redshift [COPY](http://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html) command that performs a high performance distributed copy of S3 folder contents to the newly created Redshift table.
# MAGIC 
# MAGIC ![](https://databricks.com/wp-content/uploads/2015/10/image00.gif "Redshift Data Egression")
# MAGIC 
# MAGIC The **`spark-redshift`** automatically creates a Redshift table with the appropriate schema determined from the table/DataFrame being written.
# MAGIC 
# MAGIC The default behavior is to create a new table and to throw an error message if a table with the same name already exists.
# MAGIC 
# MAGIC Docs: https://docs.databricks.com/data/data-sources/aws/amazon-redshift.html#authenticating-to-s3-and-redshift

# COMMAND ----------

# DBTITLE 1,Obtain Secret Credentials
username = dbutils.secrets.get("oetrta", "oetrta-redshift-username")
password = dbutils.secrets.get("oetrta", "redshift-password")
redshift_endpoint = dbutils.secrets.get(scope = "oetrta", key = "oetrta-redshift-endpoint")
tempdir = dbutils.secrets.get(scope = "oetrta", key = "redshift-temp-dir")
iam_role = dbutils.secrets.get(scope = "oetrta", key = "redshift-iam-role")
redshift_database = dbutils.secrets.get(scope = "oetrta", key = "redshift-database")

# COMMAND ----------

# MAGIC %fs ls "s3://aws-cdl-devdays/clicks_with_profile_GOLD"

# COMMAND ----------

clicks_df = spark.read.format("delta").options(header='true', inferSchema='true').load('s3://aws-cdl-devdays/clicks_with_profile_GOLD')

# COMMAND ----------

# DBTITLE 1,Construct the JDBC URL
jdbcUrl = "jdbc:redshift://{}/dev?user={}&password={}".format(redshift_endpoint, username, password)
print(jdbcUrl)

# COMMAND ----------

# DBTITLE 1,Identify the Table Name
table = "clicks_with_profile_GOLD_redshift"

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Go to  [Redshift](https://us-west-2.console.aws.amazon.com/redshiftv2/home?region=us-west-2#dashboard) to delete the table `clicks_with_profile_GOLD_redshift` before running the next cell
# MAGIC   

# COMMAND ----------

# DBTITLE 1,Write to Redshift
(clicks_df.write 
  .format("com.databricks.spark.redshift") 
  .option("url", jdbcUrl)
  .option("dbtable", table) 
  .option("tempdir", tempdir) 
  .option("aws_iam_role", iam_role)
  .save())

# COMMAND ----------

# DBTITLE 1,Read from Redshift
read_df = spark.read \
  .format("com.databricks.spark.redshift") \
  .option("url", jdbcUrl) \
  .option("dbtable", table) \
  .option("tempdir", tempdir) \
  .option("aws_iam_role", iam_role)\
  .load()

display(read_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### [Back to the main demo page - Step6](https://field-eng.cloud.databricks.com/#notebook/1566801/command/1566812)
