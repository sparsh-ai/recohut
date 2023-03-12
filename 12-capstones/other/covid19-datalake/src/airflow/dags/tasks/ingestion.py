import logging
import time

import awswrangler as awr
from airflow.decorators import task
from tasks.schemas import vaccinations_parquet_schema


@task(
    task_id="ingest_vaccinations",
)
def ingest_into_redshift(bucket: str, boto3_session):
    redshift_client = boto3_session.client("redshift-data")

    aws_account_id = boto3_session.client("sts").get_caller_identity()["Account"]
    for path in awr.s3.list_objects(
        f"{bucket}/data/rki/processed/germany/vaccinations/",
        suffix=".parquet",
        boto3_session=boto3_session,
    ):
        logging.info(f"Ingesting {path}")
        redshift_client.execute_statement(
            ClusterIdentifier="vaccinations-redshift-cluster",
            Database="rki",
            SecretArn=f"arn:aws:secretsmanager:{boto3_session.region_name}:{aws_account_id}:secret:redshift_admin-KPRsmn",  # noqa
            Sql=f"""
            copy vaccinations ({", ".join(vaccinations_parquet_schema.names)})
            from '{path}'
            iam_role 'arn:aws:iam::{aws_account_id}:role/RedshiftServiceRole'
            FORMAT AS PARQUET;
            """,
        )
        time.sleep(60)
        awr.s3.delete_objects(
            path,
            boto3_session=boto3_session,
        )
