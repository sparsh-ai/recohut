# Citi Bike Trip Histories

The goal of this capstone is to build an end-to-end data pipeline:

![arch](https://user-images.githubusercontent.com/62965911/215285353-2806974e-59db-4533-9c7b-d6ac33fe9756.png)

## Problem description

The project is related to Citi Bike trips. Where do Citi Bikers ride? When do they ride? How far do they go? Which stations are most popular? What days of the week are most rides taken on? The provided data will help you discover the answers to these questions and more.

The key goals of the project are:

* develop a data pipeline that will help to organize data processing in a batch manner (on a monthly basis);
* build analytical dashboard that will make it easy to discern the trends and digest the insights.

The period of the data processing will cover from 2018 to 2020.

## Dataset

The initial data of Citi Bike Trip Histories could be found [here](https://s3.amazonaws.com/tripdata/index.html) in a compressed format.
It contains information about bikes sharing in different regions of New York.

The dataset includes the following columns:

* Trip Duration
* Start Time and Date
* Stop Time and Date
* Start Station Name
* End Station Name
* Station ID
* Station Lat/Long
* Bike ID
* User Type (Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member)
* Gender (0=unknown; 1=male; 2=female)
* Year of Birth

## Technologies

We are going to use the following technologies for this project:

* Cloud: GCP
  * Data Lake (DL): GCS
  * Data Warehouse (DWH): BigQuery
* Infrastructure as code (IaC): Terraform
* Workflow orchestration: Airflow
* Transforming data: DBT
* Data Visualization: Google Data Studio

## Project architecture

The end-to-end data pipeline includes the next steps:

* downloading, processing and uploading of the initial dataset to a DL;
* moving the data from the lake to a DWH;
* transforming the data in the DWH and preparing it for the dashboard;
* dashboard creating.

## Tutorial

This tutorial contains the instructions you need to follow to reproduce the project results.

### 1. Pre-requisites

Make sure you have the following pre-installed components:

* [GCP account](https://cloud.google.com/)
* [Terraform](https://www.terraform.io/downloads)
* [Docker](https://docs.docker.com/get-docker/)

### 2. Google Cloud Platform

To set up GCP, please follow the steps below:

1. If you don't have a GCP account, please create a free trial.
2. Setup new project and write down your Project ID.
3. Configure service account to get access to this project and download auth-keys (.json). Please check the service
   account has all the permissions below:
   * Viewer
   * Storage Admin
   * Storage Object Admin
   * BigQuery Admin
4. Download [SDK](https://cloud.google.com/sdk) for local setup.
5. Set environment variable to point to your downloaded auth-keys:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"

# Refresh token/session, and verify authentication
gcloud auth application-default login
```

6. Enable the following options under the APIs and services section:
   * [Identity and Access Management (IAM) API](https://console.cloud.google.com/apis/library/iam.googleapis.com)
   * [IAM service account credentials API](https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com)
   * [Compute Engine API](https://console.developers.google.com/apis/api/compute.googleapis.com) (if you are going to use VM instance)

### 3. Terraform

We use Terraform to build and manage GCP infrastructure. Terraform configuration files are located in the separate folder `terraform`.
There are 3 configuration files:

* `terraform-version` - contains information about the installed version of Terraform;
* [variables.tf](terraform/variables.tf) - contains variables to make your configuration more dynamic and flexible;
* [main.tf](terraform/main.tf) - is a key configuration file consisting of several sections.

[Here](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_1_basics_n_setup/1_terraform_gcp/1_terraform_overview.md) you can find the detailed description of each section.

Now you can use the steps below to generate resources inside the GCP:

1. Move to the [terraform folder](terraform) using bash command `cd`.
2. Run `terraform init` command to initialize the configuration.
3. Use `terraform plan` to match previews local changes against a remote state.
4. Apply changes to the cloud with `terraform apply` command.

> Note: In steps 3 and 4 Terraform may ask you to specify the Project ID. Please use the ID that you noted down
> earlier at the project setup stage.

If you would like to remove your stack from the Cloud, use the `terraform destroy` command.

### 4. Airflow

The next steps provide you with the instructions of running Apache Airflow, which will allow you to run the entire
orchestration, taking into account that you have already set up a GCP account.

You can run Airflow locally using docker-compose. Before running it, please make sure you have at least 5 GB of free RAM.
Alternatively, you can launch Airflow on a virtual machine in GCP (in this case, please refer to [this video](https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=16)).

#### Setup

Go to the `airflow` subdirectory: here you can find the `Dockerfile` and the lightweight version
of the [docker-compose.yaml](airflow/docker-compose.yaml) file that are required to run Airflow.

The lightweight version of docker-compose file contains the minimum required set of components to run data pipelines.
The only things you need to specify before launching it are your Project ID (`GCP_PROJECT_ID`) and Cloud Storage name (`GCP_GCS_BUCKET`)
in the [docker-compose.yaml](airflow/docker-compose.yaml). Please specify these variables according to your actual GCP setup.

You can easily run Airflow using the following commands:

* `docker-compose build` to build the image (takes ~15 mins for the first-time);
* `docker-compose up airflow-init` to initialize the Airflow scheduler, DB and other stuff;
* `docker-compose up` to kick up the all the services from the container.

Now you can launch Airflow UI and run the DAGs.

> Note: If you want to stop Airflow, please type `docker-compose down` command in your terminal.

#### Running DAGs

Open the [http://localhost:8080/](http://localhost:8080/) address in your browser and login using `airflow` username
and `airflow` password.

On the DAGs View page you can find three dags:

* `data_ingestion_to_gcs_dag` for downloading data from the source, unpacking and converting it to parquet format and
  finally uploading it to the Cloud Storage.
* `gcs_to_bq_dag` to subsequently create an external and then optimized table in BigQuery from the data stored in GCS.
* `data_transform_dag` to prepare data for analytics.

The first dag is scheduled to run every month, while the second one should be triggered manually. Therefore, you need
to activate the `data_ingestion_to_gcs_dag` dag first and wait for it to finish uploading data to GCS. And only after
that manually run the `gcs_to_bq_dag` dag to create tables in DWH. Finally, you can trigger `data_transform_dag`.

### 5. DBT

We are going to use [dbt](https://www.getdbt.com/) for data transformation in DWH and further analytics dashboard development.

First you will need to create a dbt Cloud account (if you don't already have one) using [this link](https://www.getdbt.com/signup/)
and connect to your BigQuery by following [these instructions](https://docs.getdbt.com/docs/dbt-cloud/cloud-configuring-dbt-cloud/cloud-setting-up-bigquery-oauth).
You can find more detailed instructions [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_4_analytics_engineering/dbt_cloud_setup.md).

Note that:

* you can fork or copy an existing dbt project located in the separate folder `dbt` and use a link to the forked/copied version if necessary;
* you need to check that BigQuery already has areas (datasets) for staging and production dbt models (`citibike_dev` and `citibike_prod` in our case);
* you should modify [profiles.yaml](dbt/profiles.yml) file according to your dataset names and credentials.

### 6. Google Data Studio

When the production models are ready, you can start building a dashboard.

The [dashboard](https://datastudio.google.com/s/u5AyaHHljbo) is built using Google Data Studio. The process of the such dashboard creating in Google Data Studio is described in detail in [this video](https://www.youtube.com/watch?v=39nLTs74A3E&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=43).

And the final dashboard includes the following diagrams:

* Total trips count
* Average trips duration per month and year
* User type distribution
* Trips count per month and year
* Trips count by start station on the dynamic Google map

> Note: To build a Google map you need to create a new geo field `start_location` based on `start_station_latitude` and `start_station_longitude` parameters.

![Citibike-trips](https://user-images.githubusercontent.com/55026550/161604025-3cacf391-ea00-485d-b42c-623ef363f7aa.png)
