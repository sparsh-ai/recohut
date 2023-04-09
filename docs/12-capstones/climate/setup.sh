#!/bin/bash
set -a

# GCP vars: Edit these vars to match those when seting up gcp account and virtual mahine
GOOGLE_APPLICATION_CREDENTIALS_FOLDER="/home/marcos/.google/credentials/"
GOOGLE_APPLICATION_CREDENTIALS_FILE="google_credentials.json"
GCP_PROJECT_ID=ghcn-d
GCP_PROJECT_REGION=europe-west6
GCP_PROJECT_DATA_LAKE_NAME=ghcnd_raw
GCP_PROJECT_BQ_DATASET_NAME=ghcnd
# GCP_PROJECT_BQ_DATASET_DBT_DEV: shoud be <first initial><last name> where these are 
# the first name and last name used when creating the dbt cloud account.
# E.g. Marcos Jimenez -> mjimenez
GCP_PROJECT_BQ_DATASET_DBT_DEV=mjimenez

# This refers to the past years to be processed.
# Range from 1763 to 2021. Current year (2022) is processed separately.
# WARNING! Please note that from 1961 onwards, each year takes more than 1GiB in Big Query. 
# START_YEAT 2000 will generate a table of around 30GiB in size.
START_YEAR=2000

# DBT VARS SECTION
# These are used to orchestrate dbt job from airflow. If you do want to manually run the job, 
# there is no need to set these vars.
# account_id, project_id and job_id are those in the url of the job page created when setting up dbt account
# https://cloud.getdbt.com/#/accounts/{account_id}/projects/{project_id}/runs/{job_run_id}/
# E.g. https://cloud.getdbt.com/#/accounts/53940/projects/86481/jobs/71913/
DBT_ACCOUNT_ID=53940
DBT_PROJECT_ID=86481
DBT_JOB_ID=71913
# Folder where the dbt api key file is stored (when setting up dbt)
DBT_API_KEY_FOLDER="/home/marcos/.dbt/"
DBT_API_KEY_FILE_NAME="api_key.txt"

# DATAPROC VARS SECTION
GCP_PROJECT_DATAPROC_CLUSTER_NAME='ghcnd'

#
# DO NOT edit the following
#
AIRFLOW_UID=$(id -u)
GOOGLE_APPLICATION_CREDENTIALS=${GOOGLE_APPLICATION_CREDENTIALS_FOLDER}${GOOGLE_APPLICATION_CREDENTIALS_FILE}
TF_VAR_PROJECT=${GCP_PROJECT_ID}
TF_VAR_REGION=${GCP_PROJECT_REGION}
TF_VAR_DATA_LAKE_BUCKET=${GCP_PROJECT_DATA_LAKE_NAME}
TF_VAR_BQ_DATASET=${GCP_PROJECT_BQ_DATASET_NAME}
TF_VAR_BQ_DATASET_DBT_DEV="dbt_${GCP_PROJECT_BQ_DATASET_DBT_DEV}"
set +a