install:
	export AIRFLOW_HOME=$(pwd)
	export AIRFLOW_PLUGINS=$(pwd)/airflow/plugins
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

set_variable:
	airflow variables set 'key' 'value'

start:
	airflow standalone

start_webserver:
	airflow webserver -p 8081

start_scheduler:
	airflow scheduler

list:
	airflow dags list

db:
	airflow db reset
	airflow db init

docker:
#!/bin/bash
# Note: this script is a bit of a "hack" to run Airflow in a single container.
# This is obviously not ideal, but convenient for demonstration purposes.
# In a production setting, run Airflow in separate containers, as explained in Chapter 10.
	set -x
	SCRIPT_DIR=$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)
	docker run \
	-ti \
	-p 8080:8080 \
	-v ${SCRIPT_DIR}/../dags/download_rocket_launches.py:/opt/airflow/dags/download_rocket_launches.py \
	--name airflow
	--entrypoint=/bin/bash \
	apache/airflow:2.0.0-python3.8 \
	-c '( \
	airflow db init && \
	airflow users create --username admin --password admin --firstname Anonymous --lastname Admin --role Admin --email admin@example.org \
	); \
	airflow webserver & \
	airflow scheduler \
	'