from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import CronSchedule

DeploymentSpec(
    name="simple-etl-pipeline-deployment",
    flow_location="./flows/simple_etl_pipeline.py",
    tags=['tutorial','test'],
    schedule=CronSchedule(cron="0 0 * * *")
)
