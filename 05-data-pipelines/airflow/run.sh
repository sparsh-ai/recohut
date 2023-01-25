# First install airflow with:
pip install apache-airflow==2.4.1

# Create a new folder and run the following commands inside that folder to start the airflow:
export AIRFLOW_HOME=$(pwd)
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True
airflow db init
airflow users create \
    --username admin \
    --password admin \
    --firstname User \
    --lastname Name \
    --role Admin \
    --email email@example.com
airflow standalone