## Import PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
from pyspark.storagelevel import StorageLevel
import argparse

############################ Global Variables #########################################
### Define KAFKA_ADDRESS
## To Get Local IP: ipconfig/all
## Get KAFKA_ADDRESS through user arguments
parser = argparse.ArgumentParser(description='')
parser.add_argument('--KAFKA_ADDRESS',  type=str, required=True, help='External IP Address of Kafka VM')

args = parser.parse_args()
KAFKA_ADDRESS = args.KAFKA_ADDRESS
print("KAFKA_ADDRESS: ", KAFKA_ADDRESS)

## Define Comments Schema
commentSchema = StructType([
                    StructField("id",StringType(),False),
                    StructField("submission_url",StringType(),False),
                    StructField("author",StringType(),False),
                    StructField("author_flair",StringType(),True),
                    StructField("create_time",IntegerType(),False),
                    StructField("text_body",StringType(),False),
                    StructField("parent_id",StringType(),False),
                    StructField("link_id",StringType(),False),
                    StructField("num_comments",IntegerType(),True),
                    StructField("ups",IntegerType(),True)
                ])

## Define SUbmission Schema
submissionSchema = StructType([
                        StructField("id",StringType(),False),
                        StructField("reddit_url",StringType(),False),
                        StructField("title",StringType(),False),
                        StructField("author",StringType(),False),
                        StructField("author_flair",StringType(),True),
                        StructField("create_time",IntegerType(),False),
                        StructField("text_body",StringType(),False),
                        StructField("flair_category",StringType(),False),
                        StructField("ups",IntegerType(),True),
                        StructField("upvote_ratio",IntegerType(),True),
                        StructField("num_comments",IntegerType(),True),
                        StructField("images", ArrayType(StringType(), True),True),
                        StructField("videos", ArrayType(StringType(), True),True)
                    ])

########################################################################################


### Define Spark Configuration
KAFKA_CONFIG_JARS = "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.3"

## Need this to run in normal terminal
spark = SparkSession.builder \
                .appName('spark-kafka') \
                .config("spark.jars.packages", KAFKA_CONFIG_JARS) \
                .getOrCreate()

spark.conf.set("temporaryGCSBucket", "sparkclusterbucket")
spark.conf.set("google.cloud.auth.service.account.enable", "true")

spark.streams.resetTerminated()

## Read from Kafka Topic Submissions
redditSubmissions = spark \
                  .readStream \
                  .format("kafka") \
                  .option("kafka.bootstrap.servers", KAFKA_ADDRESS + ":9092") \
                  .option("subscribe", "redditSubmissions") \
                  .option("failOnDataLoss", "False") \
                  .option("startingOffsets", "earliest") \
                  .load()

## Read from Kafka Topic Comments
redditComments = spark \
                  .readStream \
                  .format("kafka") \
                  .option("kafka.bootstrap.servers", KAFKA_ADDRESS + ":9092") \
                  .option("subscribe", "redditComments") \
                  .option("failOnDataLoss", "False") \
                  .option("startingOffsets", "earliest") \
                  .load()

## Read Data from Topic Submissions
redditSubmissionsDF = redditSubmissions.selectExpr("CAST(value AS STRING)") \
                                 .select(from_json(col("value"), submissionSchema).alias("data")) \
                                 .select("data.*")

## Add Attributes for Submissions Partition
redditSubmissionsDF = redditSubmissionsDF.withColumn("year", from_unixtime(col("create_time"), "yyyy"))
redditSubmissionsDF = redditSubmissionsDF.withColumn("month", from_unixtime(col("create_time"), "MM"))
redditSubmissionsDF = redditSubmissionsDF.withColumn("day", from_unixtime(col("create_time"), "dd"))

redditSubmissionsDF = redditSubmissionsDF.withColumn("submission_datetime", to_timestamp(from_unixtime(col("create_time"), "yyyy-MM-dd HH:mm:ss")))



## Read Data from Topic Comments
redditCommentsDF = redditComments.selectExpr("CAST(value AS STRING)") \
                                 .select(from_json(col("value"), commentSchema).alias("data")) \
                                 .select("data.*")

## Add Attributes for Comments Partition
redditCommentsDF = redditCommentsDF.withColumn("year", from_unixtime(col("create_time"), "yyyy"))
redditCommentsDF = redditCommentsDF.withColumn("month", from_unixtime(col("create_time"), "MM"))
redditCommentsDF = redditCommentsDF.withColumn("day", from_unixtime(col("create_time"), "dd"))

redditCommentsDF = redditCommentsDF.withColumn("comment_datetime", to_timestamp(from_unixtime(col("create_time"), "yyyy-MM-dd HH:mm:ss")))

## Write to File Submissions, Trigger is every 4 hours
redditSubmissionDFStream = redditSubmissionsDF.writeStream \
                                                .format("parquet") \
                                                .partitionBy("year", "month", "day") \
                                                .option("path", "gs://kafka-reddit-submissions-stream/") \
                                                .option("checkpointLocation", "gs://kafka-reddit-submissions-stream/checkpoint/") \
                                                .trigger(processingTime = "14400 seconds") \
                                                .outputMode("append")

## Write to File Comments, Trigger is every 4 hours
redditCommentsDFStream = redditCommentsDF.writeStream \
                                        .format("parquet") \
                                        .partitionBy("year", "month", "day") \
                                        .option("path", "gs://kafka-reddit-comments-stream/") \
                                        .option("checkpointLocation", "gs://kafka-reddit-comments-stream/checkpoint/") \
                                        .trigger(processingTime = "14400 seconds") \
                                        .outputMode("append")


## Start Spark Stream
redditSubmissionDFStream.start()
redditCommentsDFStream.start()

## Wait until termination for Streams
spark.streams.awaitAnyTermination()

# ## WriteStream to Console
# redditCommentsDF.writeStream \
#        .format("console") \
#        .outputMode("append") \
#        .start() \
#        .awaitTermination()