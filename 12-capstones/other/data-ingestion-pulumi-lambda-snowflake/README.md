# paas-data-ingestion

Ingest and prepare data with AWS lambdas, Snowflake and dbt in a scalable, fully replayable manner.

## Overview
This repository contains a fully PaaS infrastructure for data ingestion and transformation at scale. This repository has a companion [blog post](https://towardsdatascience.com/the-modern-data-pattern-d34d42216c81), to which we refer the reader for in-depth analysis of the proposed patterns and the motivations behind the project. While you can enjoy this repository in isolation, please note that our pipeline is part of a bigger architecture, detailed in our [MLOps without Much Ops series](https://towardsdatascience.com/tagged/mlops-without-much-ops).

The ingestion pipeline mimics a typical data flow for data-driven applications: clients send events, an endpoint collects them and dumps them into a stream, finally a data warehouse stores them for further processing:

![](https://user-images.githubusercontent.com/62965911/224529511-c1ef35b0-1e8a-4bc4-8846-16878c78f6fd.jpg)

We make use of three main technologies:

* [Pulumi](https://www.pulumi.com/), which allows us to manipulate infrastructure-as-code, and to do so in a language we are very familiar with, Python (this is our first project using it coming from Terraform, so any feedback is very welcome!).
* [Snowflake](https://signup.snowflake.com/), which allows us to store raw data at scale and manipulate it with powerful SQL queries, abstracting away all the complexity of distributed computing in a simple API.
* [dbt](https://www.getdbt.com/), which allows us to define data transformation as versioned, replayable DAGs, and mix-and-match materialization strategies to suite our needs.

Finally, it is worth mentioning that the repository is e-commerce related as a results of mainly three factors:

* our own experience in building [pipelines for the industry](https://github.com/jacopotagliabue/you-dont-need-a-bigger-boat);
* the availability of high-volume, [high-quality data](https://github.com/coveooss/SIGIR-ecom-data-challenge) to simulate a realistic scenario;
* finally, the high bar set by e-commerce as far as data quantity and data-driven applications: due to the nature of the business and the competition, even medium-sized digital shops tend to produce an enormous amount of data, and to run pretty sophisticated ML flows on top it - in other words, something that works for e-commerce is going to reasonably work for many other use cases out of the box, as they are likely less data intensive and less sophisticated ML-wise.

Our goal was to keep the code realistic enough for the target use cases, but simple enough as to make it easy for everybody to port this stack to a different industry.

## Prerequisites

* _Dataset_: we use the [Coveo Data Challenge dataset](https://github.com/coveooss/SIGIR-ecom-data-challenge) as our real-world dataset (if you prefer to use your own data, you can still re-use the `pumper.py` app if you adapt the format to your input files).
* _Snowflake account_: [sign-up for a 30-day free trial](https://signup.snowflake.com).
* _Pulumi account_: [sign-up for a free Individual account](https://www.pulumi.com).
* _AWS account_: [sign-up for a free AWS account](https://aws.amazon.com/free/) (S3, API Gateway & Lambda have a free tier).

Please note that by running this project you *may incur* in some cloud costs: make sure to keep costs and infrastructure monitored and to understand how much your experiments are covered by the free tier.

## Structure

The project is divided in three main components and a simulation script.

### Infrastructure

Following the infrastructure-as-code paradigm, the folder contains the Pulumi code necessary to properly set up the AWS (lambda function, API Gateway, Cloudwatch, Firehose, etc.) and Snowflake components needed for the ingestion platform to work. For instructions on how to run it, see below.

[infrastructure/__main__.py](https://github.com/jacopotagliabue/paas-data-ingestion/blob/main/infrastructure/__main__.py) checks which services have to be created/updated/removed. The script defines:

- `s3_logs_bucket` is the S3 bucket we use to store the logs sent to Firehose;
- `sf_database` is the database on Snowflake;
- `sf_warehouse` is the Snowflake warehouse;
- `sf_roles` is a custom module to create and manage two roles:
  - a Read-Write `*_RW` profile (for admins),
  - a Read-Only `*_RO` profile;
- `sf_stream_schema` is the schema for RAW logs;
- `sf_stream_logs_snowpipe` is a custom module to configure Snowpipe and the policies required to read the data stored on your bucket;
  - `self.firehose` is the [Firehose](https://aws.amazon.com/it/kinesis/data-firehose/) stream where RAW logs are sent by the ingestion endpoint (Lambda Function);
  - `self.table` is the final table where RAW logs are stored by Snowpipe;
  - `self.storage_integration`, `self.stage` & `self.pipe` define the Snowflake resource required to allow Snowpipe to read your data;
  - `aws.s3.BucketNotification` notifies Snowpipe every time a new object is stored (by Firehose) on your bucket;
- `api` & `api_stage` define [API Gateway](https://aws.amazon.com/it/api-gateway/), a public entry-point for the Lambda function;
- `lambda_api_collect` is a custom module to define the Lambda function for the `/collect` endpoint.

### dbt

The folder contains a typical dbt project, whose goal is to collect, organize, version all the transformations needed to go from the raw data ingested by the pixel endpoint to the pre-calculated features and aggregations that can be consumed by downstream processes (BI, ML, etc.). For instructions on how to run the dbt project, see below.

We used dbt to process RAW logs and to normalize the data into 3 different schemes:

- `EVENTS`, stored on [dbt/models/events/marts](https://github.com/jacopotagliabue/paas-data-ingestion/blob/main/dbt/models/events/marts), contains all the materialized tables (`events`, `logs`, `pageviews`, `product_actions`, `purchases` & `user_agents`) with the data computed during the last execution;
- `EVENTS_LIVE`, stored on [dbt/models/events/live](https://github.com/jacopotagliabue/paas-data-ingestion/blob/main/dbt/models/events/live), contains the same tables above (`events`, `logs` etc...) updated in real-time; the views are the result of the union of the materialized table and the new events;
- `STATS`, stored on [dbt/models/stats](https://github.com/jacopotagliabue/paas-data-ingestion/blob/main/dbt/models/stats), defines materialized tables (`overview_1h`, `overview_1d`) containing all the main pre-calculated stats a dashboard can use (`pageviews`, `add_to_cart`, `transactions`, `transaction_revenue` etc).

We define the queries in macros because the tables stored on the `EVENTS` & `EVENTS_LIVE` schemes are the same but contain data from different analysis periods. For example, the `logs` table containing all the sessionized and enriched logs is used as to power the other tables:

- [dbt/models/events/marts/logs.sql](https://github.com/jacopotagliabue/paas-data-ingestion/blob/main/dbt/models/events/marts/logs.sql) is the materialized version of the table (`EVENTS.LOGS`); we use an incremental materialization and the SQL query is defined on the [dbt/macros/models/events/select_logs.sql](https://github.com/jacopotagliabue/paas-data-ingestion/blob/main/dbt/macros/models/events/select_logs.sql) table;
- [dbt/models/events/live/logs_live.sql](https://github.com/jacopotagliabue/paas-data-ingestion/blob/main/dbt/models/events/live/logs_live.sql) is the live version of the table (`EVENTS_LIVE.LOGS`); the script does a UNION between all the events stored on `EVENTS.LOGS` with all the new events defined on the `EVENTS.LOGS_STAGED` table ([dbt/models/events/live/logs_staged.sql](https://github.com/jacopotagliabue/paas-data-ingestion/blob/main/dbt/models/events/live/logs_staged.sql))

Both the `EVENTS.LOGS` and the `EVENTS_LIVE.LOGS_STAGED` table uses the same macro [dbt/macros/models/events/select_logs.sql](https://github.com/jacopotagliabue/paas-data-ingestion/blob/main/dbt/macros/models/events/select_logs.sql) but with different filters.

Finally, for pedagogical purposes, we have integrated the [UAParser.js](https://github.com/faisalman/ua-parser-js/tree/master/dist) library for parsing the user-agents directly on Snowflake.

Please see the *Bonus* section below for a more detailed functional explanation of the overall pattern. As a visual overview, this is the DAG generated by dbt when describing the data transformations we prepared:

![](https://user-images.githubusercontent.com/62965911/224529514-e8fcebd7-dcaa-4484-ae5f-caa85c2949aa.png)

These screenshots should get you a sense of how the shape of the data changes from the original [log table](https://user-images.githubusercontent.com/62965911/224529516-3607779f-25f1-4410-a66c-5ff7945e7549.png) storing the [JSON event](https://user-images.githubusercontent.com/62965911/224529502-4d129857-834e-4a54-8218-dd3ad5f308ce.png) from the endpoint, to the final [aggregations](https://user-images.githubusercontent.com/62965911/224529507-9c7fa0c4-623a-40c8-9981-08dd9f4bee41.png).


### AWS lambda

A simple AWS lambda function implementing a [data collection pixel](https://medium.com/tooso/serving-1x1-pixels-from-aws-lambda-endpoints-9eff73fe7631). Once deployed, the resulting `/collect` endpoint will accept `POST` requests from clients sending e-commerce data: the function is kept simple for pedagogical reason - after accepting the body, it prepares a simple but structured event, and uses another AWS PaaS service, Firehose, to dump it in a stream for downstream storage and further processing.

### Data pumper

To simulate a constant stream of events reaching the collect endpoint, we provide a script that can be run at will to upload e-commerce events in the [Google Analytics](https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters) format.

The events are based on the real-world clickstream dataset open sourced in 2021, the [Coveo Data Challenge](https://github.com/coveooss/SIGIR-ecom-data-challenge) dataset. By using real-world anonymized events we provide practitioners with a realistic, non-toy scenario to get acquainted with the design patterns we propose. Please cite our work, share / star the repo if you find the dataset useful!

## How to run it

Running the stack involves running three operations:

* setting up the infrastructure;
* send data;
* run dbt transformations.

### Setting up the infrastructure

1. [Install Pulumi](https://www.pulumi.com/docs/get-started/install/) on your computer and configure your [Pulumi account](https://www.pulumi.com/docs/reference/cli/pulumi_login/):
    ```sh
    pulumi login
    ```
2. Jump into the project folder & setup the python venv
    ```sh
    cd infrastructure
    make install
    ```
3. Create a new Pulumi Stack:
    ```sh
    pulumi stack init dev
    ```
4. Configure the new stack with all the required credentials:
    ```sh
    # AWS
    pulumi config set aws:region <value>
    pulumi config set aws:accessKey <value>
    pulumi config set aws:secretKey <value> --secret
    # Snowflake
    pulumi config set snowflake:region <value>
    pulumi config set snowflake:account <value>
    pulumi config set snowflake:password <value> --secret
    pulumi config set snowflake:username <value>
    ```
    All the configurations will be stored on the `Pulumi.dev.yaml` file.
5. Deploy the stack:
    ```sh
    make up
    ```

Notes:
- Make sure to use the [AWS credentiales with Administrator permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html);
- Use the same region for AWS and Snowflake (e.g. `us-east-1`);
- Follow [this guide](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html) to identify your Snowflake account & region name.


### Send data with the pumper

* To pump data into the newly created stack, `cd` into the [utils/pumper](https://github.com/jacopotagliabue/paas-data-ingestion/blob/main/utils/pumper) folder, and run `make install`.
* Download and unzip the [Coveo Data Challenge dataset](https://github.com/coveooss/SIGIR-ecom-data-challenge) into `utils/pumper/dataset`. Make sure the target folder directly contains the `.csv` files, without additional nesting.
* Create a copy of `.env.local` named `.env`, and use the dataset path as the value for `DATA_FOLDER`, the AWS url for the lambda function for `COLLECT_URL`.
* Run `make pump` to start sending Google Analytics events to the endpoint. The script will run until `N_EVENTS` has been sent (change the variable in your `.env` file to what you like).

At every run, [pumper.py](https://github.com/jacopotagliabue/paas-data-ingestion/blob/main/utils/pumper/pumper.py) will send events as they are happening in that very moments: so running the code two times will not produce duplicate events, but events with similar categorical features and different id, timestamp etc.

Please note that if you want to jump start the log table by bulk-loading the dataset (or a portion of it) to Snowflake, you can avoid some idle time waiting for events to be sent by using the [copy into](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table.html) function over the raw csv.


### Run dbt transformations

1. Jump into the project folder & setup the python venv
    ```sh
    cd dbt
    make install
    ```
2. Configure your dbt profile following the [official guide](https://docs.getdbt.com/dbt-cli/configure-your-profile):
    ```yaml
    paas-data-ingestion:
        target: dev
        outputs:
            dev:
                type: snowflake
                account: <value>
                user: <value>
                password: <value>

                role: ACCOUNTADMIN
                database: "PAAS_DATA_INGESTION_DEV"
                warehouse: "PAAS_DATA_INGESTION_DEV_WH"
                schema: RAW
                threads: 5
                client_session_keep_alive: False

    ```
5. Launch DBT:
    ```sh
    make dbt-run
    make dbt-rest
    make dbt-docs
    ```

## Bonus: mix and match materialization options

A basic computation in almost any analytics platform is the "sessionization" of clickstream data ingested from the app. That is the post hoc grouping (_inside the data warehouse_) of the uninterrupted stream of events into "sessions", which conventionally are defined with a 30 minutes threshold (i.e. given a user, two events 29 minutes apart are in the same session, if 31 minutes have passed, we now have two sessions):

![](https://user-images.githubusercontent.com/62965911/224529517-0b430e84-6ffc-4ba6-aba5-d340300026dc.jpg)

Sessionization requires some heavy lifting with window functions, so we would like to run that computation in batch without much latency constraints every X hours; on the other hand, it would be nice if recent events (e.g. session counts) could still be actionable in the stack. The stylized flow below shows how the tables in the repo can be used to solve the problem within a single stack:

![](https://user-images.githubusercontent.com/62965911/224529519-e675cc91-1784-4242-8f54-20456bc29187.jpg)

Please refer to our [blog post](https://towardsdatascience.com/the-modern-data-pattern-d34d42216c81) for more details.

## Contributors

This project has been brought to you with love by:

* [Luca Bigon](https://www.linkedin.com/in/bigluck/): design, infrastructure, SQL-ing
* [Jacopo Tagliabue](https://www.linkedin.com/in/jacopotagliabue/): design, data

A lot of people helped with the [blog post](https://towardsdatascience.com/the-modern-data-pattern-d34d42216c81): please refer to our article for more details.

## License

The code is provided "as is" and released under an open MIT License.
