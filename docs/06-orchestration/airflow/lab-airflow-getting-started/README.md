# Getting Started with Airflow

In this lab, we will learn the followings:

- Recipe 1 - How to install airflow in local system
- Recipe 2 - How to start airflow webserver and scheduler
- Recipe 3 - Running your first DAG/Pipeline
- Recipe 4 - Running your second DAG/Pipeline

## How to install Airflow

In this module, you will learn how to:

1. Install Airflow in MacOS/Unix
2. Setup Airflow on Cloud using AWS EC2 Instance
3. Setup Airflow on Cloud using AWS MWAA Managed Airflow Service
4. Setup Airflow on Cloud using AWS ECS Container Orchestration Service
5. Setup Airflow on Cloud using Google Cloud Composer Service
6. Create a URL for Airflow so that users can directly access the Airflow via the globally accessible URL
7. Create Multiple Users

### Setup Airflow in Mac/Unix

1. Install Anaconda - Refer Makefile
2. Install Java JDK - Refer Makefile
3. Update pip - `pip install -U pip`
4. Install python libs - `pip install -r requirements.txt`
5. Install and Setup Airflow - Refer Makefile

### Setup Airflow on AWS EC2

1. Go to AWS EC2 and select any medium to large scale Ubuntu (v18, v20 or v22) VM of around 4-8 vCPUs and 16GB RAM. You can go higher also.
2. Once the VM starts, go to its security group and allow all traffic to security group by adding an inbound rule.
3. Connect with the root user
4. Configure AWS
5. Follow the Mac/Unix Setup steps
6. Load the DAGs and Plugins:
   ```sh
   # local to s3
   aws s3 sync dags s3://<path>/dags
   aws s3 sync plugins s3://<path>/plugins

   # s3 to ec2
   aws s3 sync s3://<path> .
   sudo rm -rf dags/__pycache__/
   sudo rm -rf plugins/__pycache__/
   ```
7. Start the airflow
8. Use `iptables` command to update the routes
9. Get the static elastic ip address
10. Get the SSL Certificate
11. Update airflow.cfg cert path and key path

### Setup Airflow on AWS ECS

1. Use `ecs.yaml`

### Setup Airflow on AWS MWAA

1. Deploy `mwaa.yaml` Cloudformation stack
