# Databricks notebook source
#Integrate S3 into our environment.
!mkdir -p ~/.aws
!pip install awscli

# COMMAND ----------

# MAGIC %%writefile ~/.aws/credentials
# MAGIC [default]
# MAGIC aws_access_key_id=
# MAGIC aws_secret_access_key=
# MAGIC region=us-east-1
# MAGIC output=json

# COMMAND ----------

import boto3
session = boto3.Session(profile_name='default')
credentials = session.get_credentials()

sc._jsc.hadoopConfiguration().set("fs.s3a.access.key", credentials.access_key)
sc._jsc.hadoopConfiguration().set("fs.s3a.secret.key", credentials.secret_key)
aws_region = "us-east-1"
sc._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3." + aws_region + ".amazonaws.com")

# COMMAND ----------

!aws s3 ls s3://jan16-data/temp/

# COMMAND ----------

s3_path = "s3a://jan16-data/temp/yellow_tripdata_sample_2019-01.csv"

# COMMAND ----------

df = spark.read.csv(s3_path, inferSchema=True, header=True)

# COMMAND ----------

display(df.limit(5))

# COMMAND ----------

df.createOrReplaceTempView ('df')

# COMMAND ----------

df.count()

# COMMAND ----------

df1 = spark.sql("select vendor_id, sum(passenger_count) as PASS_COUNT from df group by vendor_id order by PASS_COUNT desc")

# COMMAND ----------

display(df1.limit(5))

# COMMAND ----------

df1.write.format("parquet").mode("overwrite").save("s3://jan16-data/temp/trips/vendor_count")

# COMMAND ----------

!aws s3 ls s3://jan16-data/temp/trips/vendor_count/

# COMMAND ----------

df1.write.format("delta").mode("overwrite").save("s3://jan16-data/temp/trips/vendor_count-delta")

# COMMAND ----------

!aws s3 ls s3://jan16-data/temp/trips/vendor_count_delta/
