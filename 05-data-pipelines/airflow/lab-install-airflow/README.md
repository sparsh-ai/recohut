# How to install Airflow

In this module, you will learn how to:

1. Install Airflow in MacOS/Unix
1. Setup Airflow on Cloud using AWS EC2 Instance
1. Setup Airflow on Cloud using AWS MWAA Managed Airflow Service
1. Setup Airflow on Cloud using AWS ECS Container Orchestration Service
1. Setup Airflow on Cloud using Google Cloud Composer Service
1. Create a URL for Airflow so that users can directly access the Airflow via the globally accessible URL
1. Create Multiple Users

### Setup Airflow in Mac/Unix

1. Install Anaconda - Refer Makefile
1. Install Java JDK - Refer Makefile
1. Update pip - `pip install -U pip`
1. Install python libs - `pip install -r requirements.txt`
1. Install and Setup Airflow - Refer Makefile

### Setup Airflow on AWS EC2

1. Go to AWS EC2 and select any medium to large scale Ubuntu (v18, v20 or v22) VM of around 4-8 vCPUs and 16GB RAM. You can go higher also.
1. Once the VM starts, go to its security group and allow all traffic to security group by adding an inbound rule.
1. Connect with the root user
1. Configure AWS
1. Follow the Mac/Unix Setup steps 
1. Load the DAGs and Plugins:
    ```sh
    # local to s3
    aws s3 sync dags s3://<path>/dags
    aws s3 sync plugins s3://<path>/plugins

    # s3 to ec2
    aws s3 sync s3://<path> .
    sudo rm -rf dags/__pycache__/
    sudo rm -rf plugins/__pycache__/
    ```
1. Start the airflow
1. Use `iptables` command to update the routes
1. Get the static elastic ip address
1. Get the SSL Certificate
1. Update airflow.cfg cert path and key path

### Setup Airflow on AWS ECS

1. Use `ecs.yaml`

### Setup Airflow on AWS MWAA

1. Deploy `mwaa.yaml` Cloudformation stack