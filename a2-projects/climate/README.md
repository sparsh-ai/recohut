# Global Historical Climatology Network Daily Data Pipeline

## Objective

To build a global historical climatology network data pipeline that runs daily

## Architecture

![](https://user-images.githubusercontent.com/62965911/215285541-61bbd070-3a73-4d58-84ce-ad68f980566c.jpg)

## Problem statement

Global historical weather data is large, collected from year 1763 until today. There are over 160K weather stations across the world, each of them generating several observations on a daily basis. This sum up a total of more than 1.75B observations.  
The data is also not ready to perform analytics tasks over the entire dataset or those requiring geolocation information.
All that information has to be processed (ELT) to enable analytics tasks using information from several years, locations, observation date and type ans so on.

As an example:  

- Max daily temperature in France (over all territory) in 1992.
- Plot a comparison of the main daily minimum temperature by year between NewYork and Miami.
- Overall ten hottest days in Madrid.

It is advisable that joins and aggregations will be needed for such kind of analysis.

## Main objective

Develop the data infrastructure including data pipeline and dashboard for users to perform advanced analytics tasks on the global historical weather data:

- Select a dataset.
- Create a pipeline for processing this dataset and putting it to a data-lake.
- Create a pipeline for moving the data from the lake to a data warehouse.
- Transform the data in the data warehouse: prepare it for the dashboard.
- Create a dashboard.

## Dataset description

**NOAA Global Historical Climatology Network Daily (GHCN-D)**  
[Global Historical Climatology Network - Daily](https://github.com/awslabs/open-data-docs/tree/main/docs/noaa/noaa-ghcn) is a dataset from NOAA that contains daily observations over global land areas (e.g. TMAX, SNOW...). It contains station-based observations from land-based stations worldwide. It is updated daily. The data is in CSV format. Each file corresponds to a year from 1763 to present and is named as such.  
Each file contains all weather observations from all the stations for all days in that year.  
Data description of the stations and countries, including geolocation, are available in a separate files.  

Information of all stations is stored in a specific file.
File format examples:
- http://noaa-ghcn-pds.s3.amazonaws.com/csv.gz/1788.csv.gz
- http://noaa-ghcn-pds.s3.amazonaws.com/csv.gz/1788.csv
- http://noaa-ghcn-pds.s3.amazonaws.com/ghcnd-stations.txt

Observation format:
- ID = 11 character station identification code
- YEAR/MONTH/DAY = 8 character date in YYYYMMDD format (e.g. 19860529 = May 29, 1986)
- ELEMENT = 4 character indicator of element type:
  - PRCP = Precipitation (tenths of mm)
  - SNOW = Snowfall (mm)
	- SNWD = Snow depth (mm)
  - TMAX = Maximum temperature (tenths of degrees C)
  - TMIN = Minimum temperature (tenths of degrees C)
- DATA VALUE = 5 character data value for ELEMENT 
- M-FLAG = 1 character Measurement Flag 
- Q-FLAG = 1 character Quality Flag 
- S-FLAG = 1 character Source Flag 
- OBS-TIME = 4-character time of observation in hour-minute format (i.e. 0700 =7:00 am

Format of ghcnd-stations.txt  
- Variable   Columns   Type
- ID            1-11   Character
- LATITUDE     13-20   Real
- LONGITUDE    22-30   Real
- ELEVATION    32-37   Real
- STATE        39-40   Character
- NAME         42-71   Character
- GSN FLAG     73-75   Character
- HCN/CRN FLAG 77-79   Character
- WMO ID       81-85   Character

Format of ghcnd-countries.txt  
- Variable   Columns   Type
- CODE          1-2    Character
- NAME         4-50    Character

## Proposal

### Technologies
- Cloud: GCP
- Infrastructure as code (IaC): Terraform
- Workflow orchestration: Airflow (ingestion pipeline and transformation pipeline)
- Data Warehouse: BigQuery
- Data Lake: GCS
- Batch processing/Transformations: dbt cloud or DataProc/Spark (transformation pipeline)
- Stream processing: None
- Dashboard: Google Data Studio

### Repository organization
- \airflow: airflow files (docker-compose.yaml, Dockerfile, requirements, dags folder, etc.).  
- \assets: pictures.  
- \dbt: dbt files (dbt_project.yml, models, etc.).  
- \spark: python program for data transformation (option b).  
- \terraform: terraform files for the definition of the infrastructure to deploy.  
- \README.md: this document.  
- \setup.sh: script to configure the pipeline to run.  
- \setup_dbt.md: instructions to configure dbt cloud account.  
- \setup_gcp.md: instructions to configure cgp account.  
- \setup_vm.md: instructions to setup the VM in GCP.  

In order to save space and costs, the range of years to be processed can be configured.

**Infrastructure as code:**  

  Use Terraform to create a bucket GCS and dataset in BQ  
  - ghcdn_raw bucket to store parquet files.
  - dhcdn dataset for the ingestion into BigQuery.
  - dbt_xxxx dataset for dbt cloud development environment.
  - production dataset for dbt cloud production environment. 
  
**Orchestration:**  
  
  Use Airflow to orchestrate data ingestion and transformation (dbt) pipelines. Orchestration of dbt cloud job with airflow requires access to API (either trial or team or enterprise plans). If you do not have access to API, it is possible ro run dbt cloud job manually.

**Data ingestion:**  
  
  Use Airflow to get data from AWS bucket to CGS and then to BigQuery (regular, non external tables).  
  Although it is possible to use BigQuery external tables (linked to parquet files in GCS) to perform transformations, these may be slower than regular tables. Also, optimization of queries over external tables would require partitioning of parquet files.
  - Dag `aws_gcs_other_datasets_dag` to ingest stations and countries data only once.  
    - stations and countries are txt files, so need to be transformed to csv and then to parquet files.  
  - Dag `aws_gcs_past_years_dag` to ingest observations from last years (until 2021) on a yearly basis with catchup.  
    - This dag can be run only one, since these observations will likely not change anymore.  
  - Dag `aws_gcs_current_year_dag` to ingest observations from current year on a daily basis (catchup of only one day):  
  
  To accelerate queries and data processing, each table of year (with observations) has been partitioned by date of observation (so 365 partitions in each table for specific year) and clustered by station. 
  Original date type string from cvs is transformed to date type in order to be able to partition by time.  

**Transformations (option A):**  
  
  Use dbt cloud to perform unions, joins and aggregations on BQ.  
  - Staging (materialized=view):  
    - Stations and countries: Create staged model from stations and countries tables in Big Query.  
    - The output will be `stg_stations` and `stg_countries` models.  
      In the stations model, extract country_code field from the station id field.  
    - Observations:
      - Option 1 (discarded). Create staged model (view) for each year. 
        The number of years may be too large. There is a one to one restriction model-table in dbt. So it is pointless to have such a large number of models. 
      - Option 2: Create a fact_observations model that will loop through all BigQuery year tables, transforms them and union all together.  
        Transformation for each year table:
        Observations with q_flag (quality flag) are discarded.
        Each row will have all observations for an specific day from a station. This will save space and will perform better.
        In case of several observations (by a single station) of the same type in the same day, observations are averaged.
        tmax and tmin observations are converted to degree. Max and min temperatures outside the range (-70,+70) are discarded.  
        The transformation is implemented as a macro (process_year_table).  
        The output will be a model (`stg_years_unioned`) with all years tables transformed and unioned.  
       
  - Core (materialized=table):
    - `fact_observations` materialized model by joining `stg_years_unioned` with `stg_stations` and `stg_country` models. Generated table will be partitioned by date (year) and clustered by country_code and station id. This will provide enough performance since it is advisable that the date field will be the most used while partitions will be big enough (e.g. >1GB from 1960), and country and station id will provide geolocation dimension.
    - In addition, a `fact_observations_yearly` model has been created. This model averages the daily observations over each year,e.g. tmax for 2002 is the average over all daily max temperature observations made during 2002. This will save costs and increment performance in those queries made on a yearly basis.  
  - Job:
    - For the convenient creation of the production dataset, a job `dbt build` will be created.
    - This job can be run manually from dbt cloud or through airflow dag `data_transformation_dbt_job`, which will run on a daily basis.

**Transformations (option B):**  

  In order to compare different solutions for the transformation stage, option A uses DataProc (managed solution of Spark&Hadoop) to perform the same transformations of those of option A, but reading directly from the Google Cloud bucket the parquet files.  
  The output will be tables `fact_observations_spark` and `fact_observations_spark_yearly` in Big Query. In order to control cost and resources in DataProc, a DataProc cluster is created and deleted in each dag execution.  
  This solution will be orchestrated by Airflow with the `data_transformation_dataproc_spark_job` dag which will perform the following tasks:  

  - `create_dataproc_cluster_task`: At least, 2 nodes, 16GB, 4 vCores each one.
  - `upload_main_to_gcs_task`: DataProc will get the main program to execute for the job from Google Cloud Storage, so we will upload it in our bucket. The main program is a `python-pyspark` program located in the `spark` folder.
  - `submit_dataproc_spark_job_task`: A job is submitted to DataProc cluster in order to execute our main program.  
    The main program processes each year in a loop. The operations are the same than those in option a, however, in order to avoid join operations, append mode is used when writing data to BigQuery tables.
  - `delete_dataproc_cluster_task`: Delete the cluster in order to avoid unnecessary costs. **Warning!** Dataproc uses temporal buckets to store internal data, once the cluster is deleted, it is possible that these buckets are not deleted, so check you google cloud storage.    

**Dashboard:**  
  
  Connect Google Data Studio to BQ dataset and design dashboard  

## Results

**Dashboard**

![](https://user-images.githubusercontent.com/62965911/215285535-3cf5a01c-b67d-4aa8-8a48-e2aee12df7a2.PNG)

Note: Record counts depends on the years configured.  

**Other dataset ingestion pipeline (stations and countries)** 

![other datasets ingestion pipeline](https://user-images.githubusercontent.com/62965911/215285537-7547eaf3-e8c9-41b8-9a93-dc2994ab0c9c.PNG)

**Past years ingestion pipeline**

![past years ingestion pipeline](https://user-images.githubusercontent.com/62965911/215285539-4af520d6-948a-4d74-9d1c-223341cad0b3.PNG)

**Transformation pipeline (option A - dbt cloud)**

![Transformation pipeline A](https://user-images.githubusercontent.com/62965911/215285549-cb5b6712-8236-48a0-a1c5-d786c5e3d2b2.PNG)

**Transformation pipeline (option B - DataProc)**

![Transformation pipeline B](https://user-images.githubusercontent.com/62965911/215285547-2f37ffdc-81d9-4c94-adb2-a79cf185809e.PNG)

## Setup and running

Terraform and Airflow will run in a VM in Google Cloud. Airflow will run as docker containers.
For data transformation:  
- Option a: Dbt cloud will be used to perform data transformation pipeline.  
- Option b: Dataproc cluster will be used to run a pyspark jop.  
  
Your gcp account will be used and, unless you have google's welcome credit, it will have some cost.
Your dbt cloud account will be used. Developer account is free. However, if you wish to orchestrate it with Airflow, you will need access to dbt API which is only available during free trial and for team and enterprise plans.  

If you wish to install the required tools in your own machine instead of in the VM, the instructions in `setup_gcp.md` will be a good starting point.

### Setup

Note: This setup is not mean to be for production environment. More specific service account roles should be implemented as well as changing default passwords (e.g. `sudo passwd` in your VM to create the root password since VMs in GCE does not provide a password for root user).

Follow the following steps in the same order:
1. Google Cloud Platform account and project:  
  Follow the instructions in `setup_gcp.md`  
2. Virtual Machine in Google Cloud Compute Engine:  
  Follow the instructions in `setup_vm.md`
3. dbt cloud account:  
  Follow the instructions in `setup_dbt.md`
  
### Run pipelines

Note: If you run pipelines in your own machine, 16GB or RAM are needed  
In case you have 8GB, modify the parameter `max_active_runs` to 1 in `aws_bq_past_years_dag.py`  

1. In the VM, go to the directory ghcn-d and edit the parameters in setup.sh
  If you wish to orchestrate dbt cloud from airflow, complete the dbt vars section
2. Run `source setup.sh` to apply the configuration
3. Terraform
     - `cd terraform`
     - `terraform init`
     - `terraform plan`
     - `terraform apply`
     - `yes`
4. Airflow
     - `cd ..`
     - `cd airflow`
     - `docker-compose build`
     - `docker-compose up airflow-init`
     - `docker-compose up`
     - Open browser. Enter `http://localhost:8080` 
     - Log in with `user:pass`: `airflow:airflow`  
     - Enable `data_ingestion_ghcn_other_datasets`
     - Enable `data_ingestion_past_years`. This will ingest data from START_YEAR until 2021. This may take long.
     - Enable `data_ingestion_current_year` for current year (2022), after `data_ingestion_past_years` finishes (otherwise too much memory will be used)  
5. Transformation  
     - Option a: dbt cloud  
       `fact_observations` table will be generated in the `production` dataset. You have two options:
       - a) Run `data_transformation_dbt_job` from Airflow. Please not that you have to setup env vars in `setup.sh` (DBT VARS SECTION). Also do not forget to edit the job in order to set the starting and end years for the job execution.  
       - b) Run `dbt build` from jobs menu in dbt cloud.
     - Option b: Dataproc
       - `fact_observations_spark` table will be generated in the `production` dataset. Run `data_transformation_dataproc_spark_job` from Airflow. Please not that you have to setup env vars in setup.sh accordingly.
6. Google Data Studio
     - Log in datastudio.google.com
     - Create Data Source -> BigQuery
     - Select project, dataset and table: ghcn-d -> ghcnd -> fact_observations -> Connect
     - Create Report -> Add to report
     - Make you own report.

## Improvements (ToDo)

- <strike>Local solution with postgres: ingestion and dbt~~
  - Launch docker container with postgres server (done)
  - Create database with Terraform (done)
  - Create network to connect to airflow executors (done)
  - Create dags for ingestions (done)
  - Install and run local dbt with docker (done)</strike>
   
- Orchestrate dbt local through airflow. By including dbtcore in airflow executor?
- Documentation in dbt
- CI/CD in dbt
 
- Setup

  - Parametrize local postgres dag solution better.
  - Parametrize terraform to support local or cloud solutions.
  - Modify setup_vm script to download bq and cgs connectors.
  - Modify Terraform to create VM with script to setup docker and so on. Terraform may be run in a small instance or locally.

- Project documentation
  
  - Explain local (windows) and cloud solutions.  
  - ~~Update documentation to include setup_vm.~~  
  - Update documentation to support local windows setup.bat project.  
  - Generate documentation for setup local windows machine applications.  
  - Generate documentation for local solution.  
    - Local postgres db in a separate container. 
    - dbt core installation and usage to run transformation pipelines.
    - setup.bat to setup project vars in Windows
    - Launch local postgres.
    - Airflow accessing to local network created by local postgres.
    - Specific dags for local ingestions.
    - Run airflow dags 
    - Run dbt core command (manually)
    
- Custom dashboard with BQ client for python. (bq api use) or postgresql client for python.
  - Develop Django app for this dashboard.

- Check cloud solutions from other providers (AWS)
  - E.g. Check AWS batch to run AWS batch job from a docker image. Airflow orchestrates the job, but the job is executed by AWS. E.g. Ingestion pipeline with all tasks in a single python program?

- Improvements
  
  - Find a solution to better process all years from 1760.
    - Create huge external table, or regular table from parquet files. Then process it in a single model everything.
    - Fix in dbt with incremental model or even better, dynamic models.
    - Or just large number of models materialized and unioned in the last stage (the problem with views and final materialized model is that it is too large query or too complex to process). Delete temporal tables. Alternative: Do not union, but create bq table from *tables directly in bq, but calling from dbt.
  - Fix spark/dataproc problems and improve performance
    - Add clustering by id in spark when generating fact table (works by country_code, not by id ¿...?)
    - Fix spark running locally out of memory (java heap). Even with 2022 year!!!
    - Fix spark can not partition yearly fact table by date
    - Check why Dataproc buckets are not deleted after cluster deletion.
    - Check low CPU usage in DataProc clusters.
  - dbt local postgres
    - dbt does not set primary key to materialized tables. https://github.com/dbt-labs/postgres  
    - If then else in dbt macros are not standarized. Works with BQ but it is different for PG. Fix it. The same happens with date_trunc function.  
    - Improve the performance of postgres
      - Partition.
      - Clustering.
    - ~~Implement create or replace table when creating tables.~~
    - The definition of the sources in dbt macros is written in code, and not parametrized as models. This causes differences for BQ and PG. Form instance, ' vs " and date_trunc. 
  
- Cost analysis (europe-west6)
  
  - BigQuery.
    - Active storage $0.025 per GB per month. The first 10 GB is free each month.
    - Queries (on-demand)	$7.00 per TB. The first 1 TB per month is free.    
  - GCS
    - $0.026 per GB per month. First 5GB is free each month.
  
- Bugs
  - Check setup_vm.sh if the creation of the bin directory is correct.
  - stations source text file has wmo_id. This field shopud be integer type