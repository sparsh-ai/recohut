import pyspark.sql.functions as f

from dependencies.spark import start_spark
from dependencies.utils import extract_parquet_data, load_data_to_s3_as_parquet


def main():
    spark, log, config = start_spark(
        app_name="intermediary_patent_etl_job", files=["../configs/etl_config.json"]
    )

    log.warn("Intermediary Patent ETL Job is up and running")

    patent = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}patent.parquet"
    )

    patent_assignee = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}patent_assignee.parquet"
    )

    assignee = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}assignee.parquet"
    )

    patent_inventor = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}patent_inventor.parquet"
    )

    inventor = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}inventor.parquet"
    )

    location = extract_parquet_data(
        spark, path=f"{config['cleaned_data_s3_path']}location.parquet"
    )

    data_transformed = transform_data(
        patent=patent,
        patent_assignee=patent_assignee,
        assignee=assignee,
        patent_inventor=patent_inventor,
        inventor=inventor,
        location=location,
    )

    # Write the intermediary data to parquet
    load_data_to_s3_as_parquet(
        spark,
        data_transformed,
        path=f"{config['cleaned_data_s3_path']}intermediary_patent.parquet",
    )

    log.warn("Intermediary Patent ETL Job is finished")
    spark.stop()
    return None


def transform_data(
    patent, patent_assignee, assignee, patent_inventor, inventor, location
):
    patent_join_with_patent_assignee = patent.join(
        patent_assignee, patent.id == patent_assignee.patent_id, "left"
    ).select("id", "assignee_id", "location_id")

    # Enrich patent with assignee with owner and location
    patent_with_assignee = patent_join_with_patent_assignee.filter(
        f.col("assignee_id").isNotNull()
    )

    patent_with_assignee = (
        patent_with_assignee.join(
            assignee, patent_with_assignee.assignee_id == assignee.id, "left"
        )
        .drop(assignee.id)
        .select("id", f.col("new_id").alias("owner_id"), "name", "type", "location_id")
    )

    patent_with_assignee_location = (
        patent_with_assignee.join(
            location, patent_with_assignee.location_id == location.id, "left"
        )
        .drop(location.id)
        .select(
            "id",
            "owner_id",
            "name",
            "type",
            f.col("new_id").alias("location_id"),
            f.col("Country").alias("country"),
            f.col("Continent").alias("continent"),
        )
    )

    # Enrich patent without assignee with owner and location
    patent_without_assignee = patent_join_with_patent_assignee.filter(
        f.col("assignee_id").isNull()
    )

    patent_without_assignee_join_inventor = (
        patent_without_assignee.join(
            patent_inventor,
            patent_without_assignee.id == patent_inventor.patent_id,
            "left",
        )
        .drop(patent_without_assignee.location_id)
        .select("id", "inventor_id", "location_id")
    )

    patent_without_assignee_join_inventor = (
        patent_without_assignee_join_inventor.join(
            inventor,
            patent_without_assignee_join_inventor.inventor_id == inventor.id,
            "left",
        )
        .drop(inventor.id)
        .select("id", "name", "type", f.col("new_id").alias("owner_id"), "location_id")
    )

    patent_without_assignee_join_inventor_loc = (
        patent_without_assignee_join_inventor.join(
            location,
            patent_without_assignee_join_inventor.location_id == location.id,
            "left",
        )
        .drop(location.id)
        .select(
            "id",
            "owner_id",
            "name",
            "type",
            f.col("new_id").alias("location_id"),
            f.col("Country").alias("Country"),
            f.col("Continent").alias("continent"),
        )
    )

    # Combined patent with assignee and patent without assignee
    patent_combined = patent_with_assignee_location.union(
        patent_without_assignee_join_inventor_loc
    )

    return patent_combined


# entry point for PySpark ETL application
if __name__ == "__main__":
    main()
