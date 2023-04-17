# Lab: CSV to Parquet Transformation with Glue Studio

Task: Process raw (CSV or JSON) data from the Landing S3 bucket and save it into another S3 bucket in a Columnar format with partitioning

1. Create Glue job using PySpark and enable bookmarking.
2. Make Glue job process raw (CSV or JSON) data from landing S3 bucket and save it into another S3 bucket in a columnar format with partitioning: partition on stock name and bucket on year.
3. Create Glue trigger to automatically start the PySpark job when new files are created in the S3 bucket.
4. Make sure the components are deployable using CloudFormation.

The data from the landing S3 bucket looks like this:

```
Date,Open,High,Low,Close,Volume,ticker_id,ticker_name
2017-11-22 00:00:00-05:00,28.5271320343017,28.5271320343017,28.5271320343017,28.5271320343017,0,0,VASGX
2017-11-24 00:00:00-05:00,28.5954589843749,28.5954589843749,28.5954589843749,28.595458984375,0,0,VASGX
2017-11-27 00:00:00-05:00,28.5356674194335,28.5356674194335,28.5356674194335,28.5356674194335,0,0,VASGX
2017-11-28 00:00:00-05:00,28.7150325775146,28.7150325775146,28.7150325775146,28.7150325775146,0,0,VASGX
2017-11-29 00:00:00-05:00,28.6637859344482,28.6637859344482,28.6637859344482,28.6637859344482,0,0,VASGX
2017-11-30 00:00:00-05:00,28.757734298706,28.757734298706,28.757734298706,28.757734298706,0,0,VASGX
2017-12-01 00:00:00-05:00,28.7150325775146,28.7150325775146,28.7150325775146,28.7150325775146,0,0,VASGX
2017-12-04 00:00:00-05:00,28.6637859344482,28.6637859344482,28.6637859344482,28.6637859344482,0,0,VASGX
2017-12-05 00:00:00-05:00,28.60400390625,28.60400390625,28.60400390625,28.60400390625,0,0,VASGX
```

The following code is our Glue job which processes the CSV file from the landing s3 bucket, splits the date column up, partitions on stock name and buckets on year. No major transformations were needed. All we had to do was convert the date column from a string to a date and then split the column to create ‘year’, ‘month’, ‘and day’ columns. The partitioned data is then written to the output s3 bucket in parquet format.

```py
import sys
import boto3
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col
from pyspark.sql.functions import to_date, split

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Create spark cluster
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Create dynamic frame of CSV from S3 bucket
dynamicFrame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://myonrampbucket/tickers_fct_name.csv"]},
    format="csv",
    format_options={
        "withHeader": True,
        # "optimizePerformance": True,
    },
    )

# Convert dynamic frame to a DataFrame
df = dynamicFrame.toDF()
df.show()
print("Dataframe converted")

# Create 'Year' column from 'date' column
df = df.withColumn("dateAdded", to_date(split(df["Date"], " ").getItem(0)\
    .cast("string"), 'yyyy-MM-dd')) \
    .withColumn("year", split(col("dateAdded"), "-").getItem(0)) \
    .withColumn("month", split(col("dateAdded"), "-").getItem(1)) \
    .withColumn("day", split(col("dateAdded"), "-").getItem(2)) \
    .withColumn("tickerName",col("ticker_name").cast("string")) \
    .orderBy('year')
  
print("Dataframe columns added and sorted by year.")
print(df.show())

# Partition dataframe by year and ticker name
partitioned_dataframe = df.repartition(col("year"), col("tickerName"))
print("Dataframe repartitioned")

# Convert back to dynamic frame
dynamic_frame_write = DynamicFrame.fromDF(partitioned_dataframe, glueContext, "dynamic_frame_write")
print("Dataframe converted to dynamic frame")


# Save dynamic frame into S3 bucket
glueContext.write_dynamic_frame.from_options(frame=dynamic_frame_write, 
    connection_type="s3", 
    connection_options=dict(path="s3://stocks-partitioned/", 
                            partitionKeys=["year", "ticker_name"]), 
                            format="parquet",
                            transformation_ctx="datasink2")

print("Dynamic frame saved in s3")



# Commit file read to Job Bookmark
job.commit()
print("Job completed!!!")


job.commit()
```

Finally, a Lambda trigger that invokes the Glue job using boto3 every time a new item is created in the landing S3 bucket. All components in this story are deployable using CloudFormation.

```py
import json
import urllib.parse
import boto3
from botocore.exceptions import ClientError

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        #return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
      
    def run_glue_job(job_name, arguments = {}):
        session = boto3.session.Session()
        glue_client = session.client('glue')
        try:
            job_run_id = glue_client.start_job_run(JobName=job_name, Arguments=arguments)
            return job_run_id
        except ClientError as e:
            raise Exception( "boto3 client error in run_glue_job: " + e.__str__())
        except Exception as e:
            raise Exception( "Unexpected error in run_glue_job: " + e.__str__())
  
    print(run_glue_job("Stocks"))
```
