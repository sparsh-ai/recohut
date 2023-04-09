# Getting Started

## Prerequisites

### Docker

In this project, we run Apache Airflow using docker in our local machine, hence we need to have the docker and docker-compose installed in our machine:
- Install Docker following the instruction [here](https://docs.docker.com/engine/install/)
- Install Docker Compose following the instruction [here](https://docs.docker.com/compose/install/)

### Setup AWS user and Redshift

#### Create an AWS Account

Please follow the instruction on this [link](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)

#### Create a new IAM User

In this project, we are going to access AWS S3 from Airflow, hence we need the AWS credentials
Please follow this step to create one:
- Go to AWS IAM service and click on the "Add user" button to create a new IAM user in your AWS account.
- Choose a name of your choice.
- Select "Programmatic access" as the access type. Click Next.
- Choose the `Attach existing policies directly` tab, and select the "AdministratorAccess". Click Next.
- Skip adding any tags. Click Next.
- Review and create the user. It will show you a pair of access key ID and secret.
- Take note of the pair of access key ID and secret. This pair is collectively known as Access key.

#### Create a Redshift cluster

- Create a Redshift Cluster
- Set the cluster to be publicly accessible following this [instruction](https://aws.amazon.com/premiumsupport/knowledge-center/redshift-cluster-private-public/) so Airflow can access it

#### Create an S3 bucket

We will store our raw and cleaned data in S3 bucket. Create an S3 bucket in the same region as your Redshift cluster. Please refer to this [instruction](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)

## Setup

### Running Apache Airflow Docker

The docker-compose provided in this repository is customized for our use case from docker-compose file provided by airflow [here](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#docker-compose-yaml) 
  - Create a `.env` file in the root directory of this project, and add these two values:
```commandline
AIRFLOW_UID=50000
AIRFLOW_HOME="<insert the absolute path to this project root directory>"
```
- Initialize airflow database. Open your command line, go to the project directory and run this command
```commandline
docker-compose up airflow-init
```
- Start running airflow. Open your command line, go to the project directory and run this command
```commandline
docker-compose up
```
- The airflow web interface is available at http://localhost:8080

### Set the Airflow connections

Access your airflow web UI and add the following connections in Airflow:
- Create connection `aws_credentials`, set the connection type as `Amazon Web Services`, put the value of the AWS user `Access key ID` as the `login` and `Secret code` as the `Password`. In the `Extra` column add the following json value:
```json
{"region_name": "<fill with your preferred AWS region e.g. ap-southeast-1>"}
```
- Create connection `emr_credentials`, set the connection type as `Amazon Elastic Map Reduce`, put the value of the AWS user `Access key ID` as the `login` and `Secret code` as the `Password`.
- Create connection `redshift`, set the connection type as `Postgres`, get the host name from your AWS Redshift cluster and put the value in `host`, put the schema as `dev`, fill in the `login` and `password` with the admin credentials you specified in your AWS Redshift, and lastly put the port as `5439`

### Create the tables in redshift

In your Airflow UI go to DAGs tab, and enable dag `patent_analytics_drop_create_table` and click start
By running this dag, all the necessary tables in Redshift are created. If there are existing tables, those will be dropped and recreated.

### Run the patent analytic dag

- Before running this dag, you need to ensure all the scripts are copied from spark folder:
  - Ensure you have created the configuration file in the `spark` folder as mentioned in the `spark` folder README.md
  - Open a command line and go to the directory of the `spark` folder
  - Run ```./copy_jobs_to_airflow.sh```
- Go to your Airflow UI, enable dag `patent_analytics_dag` and click start.



