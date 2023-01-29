import pyspark.sql.functions as f

from dependencies.spark import start_spark
from dependencies.utils import (
    extract_parquet_data,
    load_data_to_redshift,
    prepare_for_write_df_with_long_string,
)


def main():
    spark, log, config = start_spark(
        app_name="details_etl_job", files=["../configs/etl_config.json"]
    )

    log.warn("Details ETL Job is up and running")

    data = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}patent.parquet"
    )
    data_transformed = transform_data(data)
    load_data_to_redshift(
        spark,
        data_transformed,
        table="details",
        db_username=config["redshift"]["username"],
        db_password=config["redshift"]["password"],
        db_jdbc_url=config["redshift"]["jdbc_url"],
        s3_temp_dir=config["redshift"]["s3_temp_dir"],
        iam_role=config["redshift"]["iam_role"],
    )

    log.warn("Details ETL Job is finished")
    spark.stop()
    return None


def transform_data(data):
    transformed_data = data.select(f.col("id").alias("detail_id"), "title", "abstract")
    transformed_data = prepare_for_write_df_with_long_string(transformed_data)
    return transformed_data


# entry point for PySpark ETL application
if __name__ == "__main__":
    main()
