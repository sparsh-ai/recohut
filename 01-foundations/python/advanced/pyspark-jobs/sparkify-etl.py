import configparser
import pyspark.sql.functions as f
import os
from pyspark.sql.window import Window
from pyspark.sql import SparkSession
from datetime import datetime

config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    # get filepath to song data file
    song_data = input_data + "song_data/*/*/*/"
    
    # read song data file
    df = spark.read.json(song_data)

    # extract columns to create songs table
    songs_table = df.select(["song_id", "title", "artist_id", "year", "duration"]).distinct()
    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.parquet(output_data + 'songs/' + 'songs.parquet', partitionBy=['year', 'artist_id'])

    # extract columns to create artists table
    artists_table = df.select(["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]).distinct() 
    
    # write artists table to parquet files
    artists_table.write.parquet(output_data + 'artist/' + 'artist.parquet', partitionBy=["artist_id"])


def process_log_data(spark, input_data, output_data):
    # get filepath to log data file
    log_data = input_data + "log_data/*/*/*.json"

    # read log data file
    df = spark.read.json(log_data)
    
    # filter by actions for song plays
    df = df.where("page='NextSong'")

    # extract columns for users table    
    artists_table = df.select(["userId", "firstNmae", "lastName", "gender", "level"]).distinct()
    
    # write users table to parquet files
    artists_table.write.parquet(output_data + 'users/' + 'users.parquet', partitionBy=["userId"])

    # create timestamp column from original timestamp column
    df = df.withColumn('timestamp', ((df.ts.cast('float')/1000).cast("timestamp")))

    # extract columns to create time table
    time_table = df.select(f.col("timestamp").alias("start_time"),
                          f.hour("timestamp").alias("hour"),
                          f.dayofmonth("timestamp").alias("day"),
                          f.weekofyear("timestamp").alias("week"),
                          f.month("timestamp").alias("month"),
                          f.year("timestamp").alias("year"),
                          f.date_format(f.col("timestamp"), "t").alias("weekday")
                          )
    
    # write time table to parquet files partitioned by year and month
    time_table.write.parquet(output_data + 'time/' + 'time.parquet', partitionBy=["start_time"])

    # read in song data to use for songplays table
    song_df = spark.read.json(input_data + 'song_data/*/*/*/*.json')

    # extract columns from joined song and log datasets to create songplays table 
    song_log_joined_table = df.join(song_df, (df.song == song_df.title) & (df.artist == song_df.artist_name) & (df.length == song_df.duration), how='inner')
    songplays_table = song_log_joined_table.distinct() \
                        .select("userId", "timestamp", "song_id", "artist_id", "level", "sessionId", "location", "userAgent" ) \
                        .withColumn("songplay_id", F.row_number().over( Window.partitionBy('timestamp').orderBy("timestamp"))) \
                        .withColumnRenamed("userId","user_id")        \
                        .withColumnRenamed("timestamp","start_time")  \
                        .withColumnRenamed("sessionId","session_id")  \
                        .withColumnRenamed("userAgent", "user_agent") \

    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.parquet(output_data + 'songplays/' + 'songplays.parquet',partitionBy=['start_time', 'user_id'])


def main():
    spark = create_spark_session()
    input_data = "s3a://wysde-datasets/sparkify"
    output_data = "s3a://wysde-assets/usecases/sparkify"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()