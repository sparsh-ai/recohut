# Machine Learning with Big Data

Use big-data tools ([PySpark](https://spark.apache.org/docs/latest/api/python/index.html)) to run topic modeling (unsupervised machine learning) on [Twitter data streamed](https://developer.twitter.com/en/docs/tutorials/stream-tweets-in-real-time) using [AWS Kinesis Firehose](https://aws.amazon.com/kinesis/data-firehose/).

## [Pre-Requisites](#pre-requisites)

1. The following AWS ([1](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_environment.html), [2](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_profiles.html)) and [Twitter Developer API](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) credentials

   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_REGION`
   - `AWS_S3_BUCKET_NAME`
   - `TWITTER_API_KEY`
   - `TWITTER_API_KEY_SECRET`
   - `TWITTER_ACCESS_TOKEN`
   - `TWITTER_ACCESS_TOKEN_SECRET`

   must be stored in a [`.env` file](https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/) stored one level up from the root directory of this project.i.e. one level up from the directory containing this `README.md` file.

## [Usage](#usage)

1. Create AWS resources

   ```bash
   make aws-create
   ```

   In this step, if the code in the [section **See EC2 Public IP Address in Ansible Inventory**](https://nbviewer.org/github/elsdes3/machine-learning-with-big-data/blob/main/1_create_aws_resources.ipynb#set-ec2-public-ip-address-in-ansible-inventory) has **not** been manually executed, then edit

   ```bash
   inventories/production/host_vars/ec2host
   ```

   and replace `...` in `ansible_host: ...` by the public IP address of the newly created EC2 instance from the AWS Console in the EC2 section.
2. Provision the EC2 host, excluding Python package installation

   ```bash
   make provision-pre-python
   ```
3. Install Python packages on the EC2 host

   ```bash
   make provision-post-python
   ```
4. Start the Twitter streaming script locally

   ```bash
   make stream-local-start
   ```
5. Stop the Twitter streaming script running locally

   ```bash
   make stream-local-stop
   ```
6. Start the Twitter streaming script on the EC2 instance

   ```bash
   make stream-start
   ```
7. Stop the Twitter streaming script running on the EC2 instance

   ```bash
   make stream-stop
   ```
8. Run the Twitter streaming script locally, saving to a local CSV file but not to S3

   ```bash
   make stream-check
   ```

   Notes

   - there is no functionality to stop this script (it has to be stopped manually using Ctrl + C, or wait until the specified number of tweets, in `max_num_tweets_wanted` on line 217 of `twitter_s3.py`, have been retrieved)

   Pre-Requisites

   - the following environment variables must be manually set, before running this script, using
     ```bash
     export AWS_ACCESS_KEY_ID=...
     export AWS_SECRET_ACCESS_KEY=...
     export AWS_REGION=...
     export AWS_S3_BUCKET_NAME=...
     export TWITTER_API_KEY=...
     export TWITTER_API_KEY_SECRET=...
     export TWITTER_ACCESS_TOKEN=...
     export TWITTER_ACCESS_TOKEN_SECRET=...
     ```
9. Create AWS SageMaker instance and related resources

   ```bash
   make sagemaker-create
   ```

   Pre-Requisites

   - an AWS IAM Role granting SageMaker full access to **one** pre-existing S3 bucket (the same bucket created in step 1.) must be created using the AWS console **before** running this step.
10. Run quantitative analysis

    ```bash
    make build
    ```

    and run the following two notebooks in order of the numbered prefix in their name

    - `3_combine_raw_data.ipynb`
    - `4_data_processing.ipynb`
11. Destroy AWS SageMaker resources

    ```bash
    make sagemaker-destroy
    ```
12. Destroy AWS resources

    ```bash
    make aws-destroy
    ```

## [Notebooks](#notebooks)

1. `1_create_aws_resources.ipynb` ([view](https://nbviewer.org/github/elsdes3/big-data-ml/blob/main/1_create_aws_resources.ipynb))
   - use the AWS Python SDK (`boto3` [link](https://pypi.org/project/boto3/)) to create AWS resources
     - [S3 storage bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
     - [CloudWatch Log Group and Log Stream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogsConcepts.html)
     - [IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html)
     - [Kinesis Firehose Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
2. `2_create_sagemaker_resources` ([view](https://nbviewer.org/github/elsdes3/big-data-ml/blob/main/2_create_sagemaker_resources.ipynb))
   - use `boto3` to create an [AWS SageMaker instance](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
   - PySpark version 2.4.0 will be used on a [SageMaker notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html)
3. `3_combine_raw_data.ipynb` ([view](https://nbviewer.org/github/elsdes3/big-data-ml/blob/main/3_combine_raw_data.ipynb))
   - combines raw data in the S3 bucket into hourly CSVs
     - since each hour of data files were small enough to read into a single data object (DataFrame), in-memory tools were used to combine each hourly folder of streamed data into a single CSV
   - filters out unwanted tweets based on a list of words that are not relevant to the subject of this project
4. `3_1_combine_raw_data_pyspark.ipynb` ([view](https://nbviewer.org/github/elsdes3/big-data-ml/blob/main/3_1_combine_raw_data_pyspark.ipynb))
   - combines all raw data in the S3 bucket using PySpark and Databricks
     - files in all hourly folders were loaded into a single Spark DataFrame
   - uses only Spark DataFrame methods to filter out unwanted tweets
   - this notebook **must be run on Databricks**
5. `4_data_processing.ipynb` ([view](https://nbviewer.org/github/elsdes3/big-data-ml/blob/main/4_data_processing.ipynb))
   - perform topic modeling (unsupervised machine learning) on combined hourly CSVs using PySpark and PySparkML
   - this notebook **must run on the AWS SageMaker instance** [created in the `2_create_sagemaker_resources.ipynb` notebook](https://nbviewer.org/github/elsdes3/big-data-ml/blob/main/2_create_sagemaker_resources.ipynb)
6. `5_delete_sagemaker_resources.ipynb` ([view](https://nbviewer.org/github/elsdes3/big-data-ml/blob/main/5_delete_sagemaker_resources.ipynb))
   - use `boto3` to delete all AWS resources created to support creation of a SageMaker instance
7. `6_delete_aws_resources.ipynb` ([view](https://nbviewer.org/github/elsdes3/big-data-ml/blob/main/6_delete_aws_resources.ipynb))
   - use `boto3` to delete all AWS resources

## [Notes](#notes)

1. Running the notebooks to create and destroy AWS resources in a non-interactive approach has not been verified. It is not currently known if this is possible.
2. AWS resources are created and destroyed using the `boto3` AWS Python SDK. The AWS EC2 instance that is used to host the Twitter streaming (Python) code is [provisioned using Ansible playbooks](https://www.ansible.com/use-cases/provisioning).
3. The AWS credentials must be associated to a user group whose users have been granted programmatic access to AWS resources. In order to configure this for the IAM user group from the AWS console, see the documentation [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console). For this project, this was done before creating any AWS resources using the AWS Python SDK.
4. The Twitter credentials must be for a user account with [elevated access](https://developer.twitter.com/en/support/twitter-api/v2) to the Twitter Developer API.

## [Project Organization](#project-organization)

    ├── LICENSE
    ├── .gitignore                          <- files and folders to be ignored by version control system
    ├── .pre-commit-config.yaml             <- configuration file for pre-commit hooks
    ├── .github
    │   ├── workflows
    │       └── main.yml                    <- configuration file for CI build on Github Actions
    ├── Makefile                            <- Makefile with commands like`make lint` or `make build`
    ├── README.md                           <- The top-level README for developers using this project.
    ├── ansible.cfg                         <- configuration file for Ansible
    ├── environment.yml                     <- configuration file to create environment to run project on Binder
    ├── manage_host.yml                     <- manage provisioning of EC2 host
    ├── read_data.py                        <- Python script to read streamed Twitter data that has been saved locally
    ├── streamer.py                         <- Wrapper script to control local or remote Twitter streaming
    ├── stream_twitter.yml                  <- stream Twitter data on EC2 instance
    ├── twitter_s3.py                       <- Python script to stream Twitter data locally or on EC2 instance
    ├── variables_run.yaml                  <- Ansible playbook variables
    ├── executed_notebooks
    |   └── *.ipynb                         <- executed notebooks, with output and execution datetime suffix in filename
    ├── data
    │   ├── raw                             <- The original, immutable data dump.
    |   └── processed                       <- Intermediate (transformed) data and final, canonical data sets for modeling.
    ├── 1_create_aws_resources.ipynb        <- create cloud resources on AWS
    ├── 2_create_sagemaker_resources.ipynb  <- create AWS SageMaker resources
    ├── 3_combine_raw_data.ipynb            <- combine raw tweets data in stored in S3 into CSV files
    ├── 4_data_processing.ipynb             <- unsupervised machine learning
    ├── 5_delete_sagemaker_resources.ipynb  <- destroy AWS SageMaker resources
    ├── 6_delete_aws_resources.ipynb        <- destroy AWS cloud resources
    ├── requirements.txt                    <- base packages required to execute all Jupyter notebooks (incl. jupyter)
    ├── inventories
    │   ├── production
    │       ├── host_vars                   <- variables to inject into Ansible playbooks, per target host
    │           └── ec2_host
    |       └── hosts                       <- Ansible inventory
    ├── src                                 <- Source code for use in this project.
    │   ├── __init__.py                     <- Makes src a Python module
    │   │
    │   ├── ansible                         <- Utilities to support Ansible orchestration playbooks
    |       ├── __init__.py                 <- Makes src.ansible a Python module
    │       └── playbook_utils.py
    │   │
    │   ├── cw                              <- Scripts to manage AWS CloudWatch Log Groups and Streams
    |       ├── __init__.py                 <- Makes src.cw a Python module
    │       └── cloudwatch_logs.py
    │   │
    │   ├── data                            <- Scripts to combine raw tweets data pre hour into a CSV file
    |       ├── __init__.py                 <- Makes src.data a Python module
    │       └── combine_data.py
    │   │
    │   ├── ec2                             <- Scripts to manage AWS EC2 instances and security groups
    |       ├── __init__.py                 <- Makes src.ec2 a Python module
    │       └── ec2_instances_sec_groups.py
    │   │
    │   ├── firehose                        <- Scripts to manage AWS Kinesis firehose data streams
    |       ├── __init__.py                 <- Makes src.firehose a Python module
    │       └── kinesis_firehose.py
    │   │
    │   ├── iam                             <- Scripts to manage AWS IAM
    |       ├── __init__.py                 <- Makes src.iam a Python module
    │       └── iam_roles.py
    │   │
    │   ├── keypairs                        <- Scripts to manage AWS EC2 SSH key pairs
    |       ├── __init__.py                 <- Makes src.keypairs a Python module
    │       └── ssh_keypairs.py
    │   │
    │   └── model_interpretation            <- Scripts to manage ML models
    |       ├── __init__.py                 <- Makes src.model_interpretation a Python module
    │       ├── import_export_models.py
    │       └── interpret_models.py
    │   │
    │   └── nlp                             <- Scripts to preform NLP tasks on text data
    |       ├── __init__.py                 <- Makes src.nlp a Python module
    │       ├── clean_text.py
    │   │
    │   └── s3                              <- Scripts to manage AWS S3 buckets
    |       ├── __init__.py                 <- Makes src.s3 a Python module
    │       ├── bucket_contents.py
    │       └── buckets.py
    │   │
    │   └── visualization                   <- Scripts to preform data visualization tasks
    |       ├── __init__.py                 <- Makes src.visualization a Python module
    │       ├── visualize.py
    │
    ├── papermill_runner.py                 <- Python functions that execute system shell commands.
    └── tox.ini                             <- tox file with settings for running tox; see https://tox.readthedocs.io/en/latest/

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
