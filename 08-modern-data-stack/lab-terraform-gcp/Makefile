keys:
	terraform output airbyte_sa_key > keys/airbyte.txt
	terraform output airflow_sa_key > keys/airflow.txt
	terraform output dbt_sa_key > keys/dbt.txt
	terraform output metabase_sa_key > keys/metabase.txt
	echo "[value from the previous command]" | base64 -d