
:: GCP vars: Edit these vars to match those when seting up gcp account and virtual mahine
set GOOGLE_APPLICATION_CREDENTIALS_FOLDER=c:/users/marcos/.google/credentials/
set GOOGLE_APPLICATION_CREDENTIALS_FILE=google_credentials.json
set GCP_PROJECT_ID=ghcn-d
set GCP_PROJECT_REGION=europe-west6
set GCP_PROJECT_DATA_LAKE_NAME=ghcnd_raw
set GCP_PROJECT_BQ_DATASET_NAME=ghcnd
:: GCP_PROJECT_BQ_DATASET_DBT_DEV: shoud be <first initial><last name> where these are 
:: the first name and last name used when creating the dbt cloud account.
:: E.g. Marcos Jimenez -> mjimenez
set GCP_PROJECT_BQ_DATASET_DBT_DEV=mjimenez

:: This refers to the past years to be processed.
:: Range from 1763 to 2021. Current year (2022) is processed separately.
:: WARNING! Please note that from 1961 onwards, each year takes more than 1GiB in Big Query. 
:: START_YEAT 2000 will generate a table of around 30GiB in size.
set START_YEAR=1770

:: DBT VARS SECTION
:: These are used to orchestrate dbt job from airflow. If you do want to manually run the job, 
:: there is no need to set these vars.
:: account_id, project_id and job_id are those in the url of the job page created when setting up dbt account
:: https://cloud.getdbt.com/::/accounts/{account_id}/projects/{project_id}/runs/{job_run_id}/
:: E.g. https://cloud.getdbt.com/::/accounts/53940/projects/86481/jobs/71913/
set DBT_ACCOUNT_ID=53940
set DBT_PROJECT_ID=86481
set DBT_JOB_ID=71913
:: Folder where the dbt api key file is stored (when setting up dbt)
set DBT_API_KEY_FOLDER=c:/users/marcos/.dbt/
set DBT_API_KEY_FILE_NAME=api_key.txt

:: DATAPROC VARS SECTION
set GCP_PROJECT_DATAPROC_CLUSTER_NAME=ghcnd

::
:: DO NOT edit the following
::
:: Only for Linux AIRFLOW_UID=$(id -u)
set GOOGLE_APPLICATION_CREDENTIALS=%GOOGLE_APPLICATION_CREDENTIALS_FOLDER%%GOOGLE_APPLICATION_CREDENTIALS_FILE%
set TF_VAR_PROJECT=%GCP_PROJECT_ID%
set TF_VAR_REGION=%GCP_PROJECT_REGION%
set TF_VAR_DATA_LAKE_BUCKET=%GCP_PROJECT_DATA_LAKE_NAME%
set TF_VAR_BQ_DATASET=%GCP_PROJECT_BQ_DATASET_NAME%
set TF_VAR_BQ_DATASET_DBT_DEV=dbt_%GCP_PROJECT_BQ_DATASET_DBT_DEV%
