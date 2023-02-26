"""
Fetch exchange rates from the National Bank of Poland.
"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.sensors.http import HttpSensor


dag_id = "exchange_rates_extract"
http_conn_id = "http_nbp"
currencies = ["eur", "usd"]
file_path = "/Users/sparshagarwal/Desktop/projects/de/_tmp/airflow-forex/data/exchange_rates/{{ macros.ds_format(ds, '%Y-%m-%d', '%Y') }}/"


def _get_endpoint(currency):
    """Returns a currency-specific endpoint."""
    return f"a/{currency}/{{{{ ds }}}}/?format=json"


default_args = {
    "email": ["first.last@example.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 5,
    "retry_delay": timedelta(minutes=15),
}

dag = DAG(                                                     
   dag_id=dag_id,                          
   start_date=datetime(2022, 12, 31),
   schedule_interval="@daily",
   default_args=default_args,
   max_active_runs=5,
   tags=["exchange_rates", "extract"],
)

dag.doc_md = __doc__

for currency in currencies:
    sense_data = HttpSensor(
        task_id=f"sense_data_{currency}",
        http_conn_id=http_conn_id,
        endpoint=_get_endpoint(currency),
        poke_interval=5,
        timeout=20,
        soft_fail=True,
        dag=dag,
    )

    download_data = BashOperator(
        task_id=f"download_data_{currency}",
        bash_command=\
            f"""
            mkdir -p {file_path}{currency}/ && 
                touch '{file_path}{currency}/{{{{ ds }}}}' && 
                wget {{{{ conn.http_nbp.host }}}}{_get_endpoint(currency)} -O '{file_path}{currency}/{{{{ ds }}}}'
            """,
        depends_on_past=True,
        dag=dag,
    )

    sense_data >> download_data
