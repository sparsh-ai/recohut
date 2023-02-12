import pyspark.sql.functions as f

from dependencies.spark import start_spark
from dependencies.utils import (
    extract_parquet_data,
    load_data_to_redshift,
)


def main():
    spark, log, config = start_spark(
        app_name="patents_etl_job", files=["../configs/etl_config.json"]
    )

    log.warn("Patents ETL Job is up and running")

    patent = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}patent.parquet"
    )
    intermediary_patent = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}intermediary_patent.parquet"
    )
    data_transformed = transform_data(
        patent=patent, intermediary_patent=intermediary_patent
    )
    load_data_to_redshift(
        spark,
        data_transformed,
        table="patents",
        db_username=config["redshift"]["username"],
        db_password=config["redshift"]["password"],
        db_jdbc_url=config["redshift"]["jdbc_url"],
        s3_temp_dir=config["redshift"]["s3_temp_dir"],
        iam_role=config["redshift"]["iam_role"],
    )

    log.warn("Patents ETL Job is finished")
    spark.stop()
    return None


def transform_data(patent, intermediary_patent):
    patent_with_owner_and_location = intermediary_patent.select(
        "id", "owner_id", "location_id"
    )
    patent_with_all_fields = (
        patent_with_owner_and_location.join(
            patent, patent_with_owner_and_location.id == patent.id
        )
        .drop(patent.id)
        .select(
            "id",
            f.col("date").alias("granted_date"),
            f.col("id").alias("detail_id"),
            "owner_id",
            "location_id",
            f.col("id").alias("wipo_classification_id"),
            "num_claims",
        )
    )
    return patent_with_all_fields


# entry point for PySpark ETL application
if __name__ == "__main__":
    main()
