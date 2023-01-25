# these 4 exports are specific to my account, you will get these values from cloudformation stack
export JOB_ROLE_ARN=arn:aws:iam::684199068947:role/EMRServerlessS3RuntimeRole
export S3_BUCKET=emrserverless-workshop-684199068947
export APPLICATION_ID=00f5rr7j2lct8g09

export AIRFLOW_HOME=$(pwd)
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True
airflow db init
airflow users create \
    --username admin \
    --password admin \
    --firstname Sparsh \
    --lastname Agarwal \
    --role Admin \
    --email sparsh@example.com
airflow standalone