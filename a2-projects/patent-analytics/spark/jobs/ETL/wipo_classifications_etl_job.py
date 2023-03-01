import pyspark.sql.functions as f

from dependencies.spark import start_spark
from dependencies.utils import extract_parquet_data, load_data_to_redshift


def main():
    spark, log, config = start_spark(
        app_name="wipo_classifications_etl_job", files=["../configs/etl_config.json"]
    )

    log.warn("Wipo Classifications ETL Job is up and running")

    wipo_data = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}wipo.parquet"
    )
    wipo_field_data = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}wipo_field.parquet"
    )

    data_transformed = transform_data(
        wipo_data=wipo_data, wipo_field_data=wipo_field_data
    )
    load_data_to_redshift(
        spark,
        data_transformed,
        table="wipo_classifications",
        db_username=config["redshift"]["username"],
        db_password=config["redshift"]["password"],
        db_jdbc_url=config["redshift"]["jdbc_url"],
        s3_temp_dir=config["redshift"]["s3_temp_dir"],
        iam_role=config["redshift"]["iam_role"],
    )

    log.warn("Wipo Classifications ETL Job is finished")
    spark.stop()
    return None


def transform_data(wipo_data, wipo_field_data):
    transformed_data = wipo_data.join(
        wipo_field_data, wipo_data.field_id == wipo_field_data.id
    ).select(
        f.col("patent_id").alias("wipo_classification_id"),
        f.col("sector_title").alias("sector"),
        f.col("field_title").alias("field"),
    )
    return transformed_data


# entry point for PySpark ETL application
if __name__ == "__main__":
    main()
