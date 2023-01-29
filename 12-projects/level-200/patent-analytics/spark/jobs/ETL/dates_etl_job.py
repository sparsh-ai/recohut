import pyspark.sql.functions as f

from dependencies.spark import start_spark
from dependencies.utils import extract_parquet_data, load_data_to_redshift


def main():
    spark, log, config = start_spark(
        app_name="dates_etl_job", files=["../configs/etl_config.json"]
    )

    log.warn("Dates ETL Job is up and running")

    data = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}patent.parquet"
    )
    data_transformed = transform_data(data)
    load_data_to_redshift(
        spark,
        data_transformed,
        table="dates",
        db_username=config["redshift"]["username"],
        db_password=config["redshift"]["password"],
        db_jdbc_url=config["redshift"]["jdbc_url"],
        s3_temp_dir=config["redshift"]["s3_temp_dir"],
        iam_role=config["redshift"]["iam_role"],
    )

    log.warn("Dates ETL Job is finished")
    spark.stop()
    return None


def transform_data(data):
    transformed_data = (
        data.select("date").distinct().select("date", f.year("date").alias("year"))
    )
    return transformed_data


# entry point for PySpark ETL application
if __name__ == "__main__":
    main()
