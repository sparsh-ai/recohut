from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
import pyspark.sql.functions as f

from dependencies import logging
import math

DEFAULT_TEXT_COL_LENGTH = 256
MAX_TEXT_COL_LENGTH = 65535


def extract_parquet_data(spark: SparkSession, path):
    spark_logger = logging.Log4j(spark)
    spark_logger.warn(f"Extracting data from {path}")
    data = spark.read.parquet(path)
    return data


def extract_tsv_data(spark: SparkSession, path, partition_number=10):
    spark_logger = logging.Log4j(spark)
    spark_logger.warn(f"Extracting data from {path}")
    data = (
        spark.read.options(
            header="True",
            delimiter="\t",
            inferSchema="True",
            escape='"',
            multiline="True",
        )
        .csv(path)
        .repartition(partition_number)
    )
    return data


def extract_csv_data(spark: SparkSession, path):
    spark_logger = logging.Log4j(spark)
    spark_logger.warn(f"Extracting data from {path}")
    data = spark.read.options(
        header="True",
        delimiter=",",
        inferSchema="True",
        escape='"',
        multiline="True",
    ).csv(path)
    return data


def extract_json_data(spark: SparkSession, path):
    spark_logger = logging.Log4j(spark)
    spark_logger.warn(f"Extracting data from {path}")
    data = spark.read.options(multiline="True").json(path)
    return data


def load_data_to_redshift(
    spark: SparkSession,
    data: DataFrame,
    db_jdbc_url,
    db_username,
    db_password,
    s3_temp_dir,
    iam_role,
    table,
):
    spark_logger = logging.Log4j(spark)
    spark_logger.warn(f"Writing data to redshift table {table}")
    url = f"{db_jdbc_url}?user={db_username}&password={db_password}"
    data.write.format("io.github.spark_redshift_community.spark.redshift").option(
        "url", url
    ).option("tempdir", s3_temp_dir).option("dbtable", table).mode("overwrite").option(
        "aws_iam_role", iam_role
    ).save()


def load_data_to_s3_as_parquet(
    spark: SparkSession, df: DataFrame, path, partition=None
):
    spark_logger = logging.Log4j(spark)
    spark_logger.warn(f"Writing data to S3 {path}")
    if partition:
        df.write.partitionBy(partition).mode("overwrite").parquet(path)
    else:
        df.write.mode("overwrite").parquet(path)


def load_data_to_s3_as_csv(spark: SparkSession, df: DataFrame, path):
    spark_logger = logging.Log4j(spark)
    spark_logger.warn(f"Writing data to S3 {path}")
    df.write.option("header", True).mode("overwrite").csv(path)


# To workaround issue where spark-redshift library assume the column type to be TEXT varchar(256) for all the strings
# https://gist.github.com/pallavi/f83a45308ba8387f6b227c28aa209077
def prepare_for_write_df_with_long_string(df):
    for (column, data_type) in df.dtypes:
        if data_type == "string":
            max_length = (
                df.select(f.length(df[column]).alias("length"))
                .select(f.max("length"))
                .first()["max(length)"]
            )
            if max_length is not None and max_length > DEFAULT_TEXT_COL_LENGTH:
                col_length = int(
                    pow(2, math.ceil(math.log(max_length) / math.log(2)))
                )  # round up to a power of 2
                col_length = min(MAX_TEXT_COL_LENGTH, col_length)
                df = df.withColumn(
                    column,
                    df[column]
                    .substr(0, col_length)
                    .alias(column, metadata={"maxlength": col_length}),
                )  # truncate column values in case they are longer than Redshift's max allowed length
    return df
