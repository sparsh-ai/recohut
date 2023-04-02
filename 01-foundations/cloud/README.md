# Cloud

## Basic Concepts

1. <a href="#/01-foundations/cloud/cloud-basics.md" target="_blank">Cloud Computing Basics ⤻</a>
1. <a href="#/01-foundations/cloud/cloud-comparison.md" target="_blank">Comparison of Cloud Services ⤻</a>

## Amazon Web Services (AWS)

### Concepts

1. <a href="#/01-foundations/cloud/ec2.md" target="_blank">EC2 ⤻</a>
1. <a href="#/01-foundations/cloud/iam.md" target="_blank">IAM ⤻</a>
1. <a href="#/01-foundations/cloud/glue.md" target="_blank">Glue ⤻</a>
1. <a href="#/01-foundations/cloud/rds.md" target="_blank">RDS ⤻</a>
1. <a href="#/01-foundations/cloud/s3.md" target="_blank">S3 ⤻</a>
1. <a href="#/01-foundations/cloud/dms.md" target="_blank">DMS ⤻</a>
1. <a href="#/01-foundations/cloud/secrets-manager.md" target="_blank">Secrets Manager ⤻</a>
1. <a href="#/01-foundations/cloud/aws-containers.md" target="_blank">AWS Container Services ⤻</a>
1. AWS Certified Solutions Architect - Download the slides from S3 using `sh resources/download.sh` command and learn the concepts

### Commands

```Makefile
install:
	pip install awscli

setup:
	aws configure

sts-identity:
	aws sts get-caller-identity

secret_manager_get_values:
	aws secretsmanager get-secret-value --secret-id wysde --query SecretString --output text

s3_create_bucket:
	TS=$(date +%s)
	aws s3api create-bucket --bucket <bucket-name>-$TS --region us-east-1

create_policy:
	aws iam create-policy --policy-name <policy-name> --policy-document file://<file-name>.json

create_role:
	aws iam create-role --role-name <role-name> --assume-role-policy-document file://role-trust.json

attach_policy_to_role:
	aws iam attach-role-policy --policy-arn <> --role-name <>

iam_keys_rotation:
	aws iam list-users
	aws iam list-access-keys --user-name jan31
	aws iam create-access-key --user-name jan31
	aws iam update-access-key --access-key-id <> --status Inactive --user-name jan31
	aws iam delete-access-key --access-key-id <> --user-name jan31

create-redshift-cluster:
# Use the following command to create a two-node dc2.large cluster with the minimal set of parameters of cluster-identifier (any unique identifier for the cluster), node-type/number-of-nodes and the master user credentials. Replace $MasterUserPassword in the following command with a password of your choice. The password must be 8-64 characters long and must contain at least one uppercase letter, one lowercase letter, and one number. You can use any printable ASCII character except /, "", or, or @:
	aws redshift create-cluster --node-type dc2.large --number-of-nodes 2 --master-username adminuser --master-user-password $MasterUserPassword --cluster-identifier myredshiftcluster
# It will take a few minutes to create the cluster. You can monitor the status of the cluster creation process using the following command:
	aws redshift describe-clusters --cluster-identifier myredshiftcluster
# Note that "ClusterStatus": "available" indicates that the cluster is ready for use and that you can connect to it using the "Address": "myredshiftcluster.abcdefghijk.eu-west-1.redshift.amazonaws.com" endpoint. The cluster is now ready. Now, you use an ODBC/JDBC to connect to the Amazon Redshift cluster.

ec2_port_routing:
	sudo iptables -t nat -L
	sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 8080
	sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-ports 8080
	sudo iptables -t nat -D PREROUTING 1 # to remove
	iptables -P INPUT ACCEPT
	iptables -P OUTPUT ACCEPT
	iptables -P FORWARD ACCEPT
	iptables -F

get_ssl_cert:
	sudo snap install core; sudo snap refresh core
	sudo apt-get remove certbot
	sudo snap install --classic certbot
	sudo ln -s /snap/bin/certbot /usr/bin/certbot
	sudo certbot certonly --standalone

ec2_login_ssh:
	chmod 400 sparsh.pem
	sudo chown -R ubuntu /home/ubuntu
	ssh -i "sparsh.pem" ubuntu@ec2-111-11-11-111.compute-1.amazonaws.com

secretsmanager_python:
	#!/usr/bin/python
	import boto3
	import json
	def get_secret(secret_name, region_name="us-east-1"):
		session = boto3.session.Session()
		client = session.client(
			service_name='secretsmanager',
			region_name=region_name)
		get_secret_value_response = client.get_secret_value(SecretId=secret_name)
		get_secret_value_response = json.loads(get_secret_value_response['SecretString'])
		return get_secret_value_response

secretsmanager_python_postgres:
	import pandas as pd
	import psycopg2
	import boto3
	import json
	from sqlalchemy import create_engine
	from sqlalchemy import text

	def get_secret(secret_name='wysde'):
		region_name = "us-east-1"
		session = boto3.session.Session()
		client = session.client(
			service_name='secretsmanager',
			region_name=region_name)
		get_secret_value_response = client.get_secret_value(SecretId=secret_name)
		get_secret_value_response = json.loads(get_secret_value_response['SecretString'])
		return get_secret_value_response

	secret_vals = get_secret()

	postgres_endpoint = secret_vals['RDS_POSTGRES_HOST']
	postgres_user = secret_vals['RDS_POSTGRES_USERNAME']
	postgres_pass = secret_vals['RDS_POSTGRES_PASSWORD']
	port = secret_vals['RDS_POSTGRES_PORT']
	dbname = "postgres"

	engine_string = "postgresql+psycopg2://%s:%s@%s:%s/%s" \
	% (postgres_user, postgres_pass, postgres_endpoint, port, dbname)
	engine = create_engine(engine_string)

	query = """
	SELECT *
	FROM pg_catalog.pg_tables
	WHERE schemaname != 'pg_catalog' AND 
		schemaname != 'information_schema';
	"""
	df = pd.read_sql_query(text(query), engine)
```

## Google Cloud Platform (GCP)

1. <a href="#/01-foundations/cloud/gcp-basics.md" target="_blank">GCP Basics ⤻</a>
1. <a href="#/01-foundations/cloud/gcp-setup.md" target="_blank">GCP Setup ⤻</a>

## Azure Cloud

1. <a href="#/01-foundations/cloud/azure-basics.md" target="_blank">Azure Basics ⤻</a>
1. <a href="#/01-foundations/cloud/azure-data-ingestion.md" target="_blank">Azure Data Ingestion ⤻</a>
1. <a href="#/01-foundations/cloud/azure-data-ingestion.md" target="_blank">Azure Batch Processing ⤻</a>
1. <a href="#/01-foundations/cloud/azure-fullstack-solutions.md" target="_blank">Azure Full-stack Solutions ⤻</a>

## Labs

### <a href="#/01-foundations/cloud/lab-aws-setup/" target="_blank">Lab: AWS Account Setup ⤻</a>

1. Install AWS CLI
2. Create IAM user and generate credentials
3. Setup AWS credentials

### <a href="#/01-foundations/cloud/lab-create-iam-policy-role/" target="_blank">Lab: AWS IAM Service ⤻</a>

1. Create policies and roles
2. Attach policies to the roles

### <a href="#/01-foundations/cloud/lab-aws-secrets-manager/" target="_blank">Lab: AWS Secrets Manager Service ⤻</a>

1. Create a Secret in Secrets Manager Vault
2. Get the credential using AWS CLI

### <a href="#/01-foundations/cloud/lab-create-your-first-vpc/" target="_blank">Lab: Create AWS VPC ⤻</a>

### <a href="#/01-foundations/cloud/lab-create-your-first-ec2-instance-linux/" target="_blank">Lab: Create AWS EC2 instance ⤻</a>
