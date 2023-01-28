airflow db init
airflow users create \
    --username admin \
    --password admin \
    --firstname Sparsh \
    --lastname Agarwal \
    --role Admin \
    --email sparsh@example.com
export AIRFLOW_HOME=$(pwd)
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True
export AIRFLOW_VAR_ACLED_BUCKET=wysde2
export AIRFLOW_VAR_ACLED_CRAWLER_NAME=acled
airflow standalone