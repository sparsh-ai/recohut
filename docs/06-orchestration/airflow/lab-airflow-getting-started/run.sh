export AIRFLOW_HOME=$(pwd)
export AIRFLOW__CORE__LOAD_EXAMPLES=False
airflow db init
airflow users create \
    --username admin \
    --password admin \
    --firstname Sparsh \
    --lastname Agarwal \
    --role Admin \
    --email sparsh@example.com
airflow standalone