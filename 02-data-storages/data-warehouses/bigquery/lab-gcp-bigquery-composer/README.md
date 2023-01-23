# GCP BigQuery Composer

> Cloud Composer - Copying BigQuery Tables Across Different Locations

## Objective

Copying BigQuery Tables Across Different Locations using Cloud Composer

## Introduction

In this advanced lab, you will learn how to create and run an [Apache Airflow](http://airflow.apache.org/) workflow in Cloud Composer that completes the following tasks:

- Reads from a config file the list of tables to copy
- Exports the list of tables from a [BigQuery](https://cloud.google.com/bigquery/docs/) dataset located in US to [Cloud Storage](https://cloud.google.com/storage/docs/)
- Copies the exported tables from US to EU [Cloud Storage](https://cloud.google.com/storage/docs/) buckets
- Imports the list of tables into the target BigQuery Dataset in EU

### Step 1: Create Cloud Composer environment

1. First, create a Cloud Composer environment by clicking on Composer in the Navigation menu:
1. Then click Create environment.
2.  In dropdown menu, select Composer 1.
3.  Set the following parameters for your environment:
    -   Name: composer-advanced-lab
    -   Location: us-east1
    -   Zone: us-east1-c
    - Leave all other settings as default.
1.  Click Create.

The environment creation process is completed when the green checkmark displays to the left of the environment name on the Environments page in the Cloud Console.

Note: It can take up to 20 minutes for the environment to complete the setup process. Move on to the next section `Create Cloud Storage buckets and BigQuery destination dataset`.

### Step 2: Create Cloud Storage buckets

1.  Create two Cloud Storage Multi-Regional buckets.
2.  Give your two buckets a universally unique name including the location as a suffix:
    -   one located in the US as *source* (e.g. 6552634-us)
    -   the other located in EU as *destination* (e.g. 6552634-eu)

Click Confirm for `Public access will be prevented` pop-up if prompted.

These buckets will be used to copy the exported tables across locations, i.e., US to EU.

### Step 3: BigQuery destination dataset

1.  Create the destination BigQuery Dataset in EU from the BigQuery new web UI.
2.  Go to Navigation menu > BigQuery.
1.  Click Done.
2.  Then click the three dots next to your project ID and select Create dataset.
3.  Use the name nyc_tlc_EU and Data location EU.
4.  Click CREATE DATASET.

### Step 4: Defining the workflow

Cloud Composer workflows are comprised of [DAGs (Directed Acyclic Graphs)](https://airflow.apache.org/docs/apache-airflow/1.10.15/concepts.html). The code shown in [bq_copy_across_locations.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/16de3b44f1a9faeccca5bc1cd8a719afc104dc65/composer/workflows/bq_copy_across_locations.py) is the workflow code, also referred to as the DAG. Open the file now to see how it is built. Next will be a detailed look at some of the key components of the file.

To orchestrate all the workflow tasks, the DAG imports the following operators:

1.  `DummyOperator`: Creates Start and End dummy tasks for better visual representation of the DAG.
2.  `BigQueryToCloudStorageOperator`: Exports BigQuery tables to Cloud Storage buckets using Avro format.
3.  `GoogleCloudStorageToGoogleCloudStorageOperator`: Copies files across Cloud Storage buckets.
4.  `GoogleCloudStorageToBigQueryOperator`: Imports tables from Avro files in Cloud Storage bucket.

In this example, the function `read_master_file()` is defined to read the config file and build the list of tables to copy:

```py
# --------------------------------------------------------------------------------
# Functions
# --------------------------------------------------------------------------------
def read_table_list(table_list_file):
    """
    Reads the master CSV file that will help in creating Airflow tasks in
    the DAG dynamically.
    :param table_list_file: (String) The file location of the master file,
    e.g. '/home/airflow/framework/master.csv'
    :return master_record_all: (List) List of Python dictionaries containing
    the information for a single row in master CSV file.
    """
    master_record_all = []
    logger.info('Reading table_list_file from : %s' % str(table_list_file))
    try:
        with open(table_list_file, 'rb') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # skip the headers
            for row in csv_reader:
                logger.info(row)
                master_record = {
                    'table_source': row[0],
                    'table_dest': row[1]
                }
                master_record_all.append(master_record)
            return master_record_all
    except IOError as e:
        logger.error('Error opening table_list_file %s: ' % str(
            table_list_file), e)
```

The name of the DAG is `bq_copy_us_to_eu_01`, and the DAG is not scheduled by default so needs to be triggered manually.

```py
default_args = {
    'owner': 'airflow',
    'start_date': datetime.today(),
    'depends_on_past': False,
    'email': [''],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
# DAG object.
with models.DAG('bq_copy_us_to_eu_01',
                default_args=default_args,
                schedule_interval=None) as dag:

```

To define the Cloud Storage plugin, the class `Cloud StoragePlugin(AirflowPlugin)` is defined, mapping the hook and operator downloaded from the Airflow 1.10-stable branch.

```py
# Import operator from plugins
from gcs_plugin.operators import gcs_to_gcs
```

### Step 5: Viewing environment information

1.  Go back to Composer to check on the status of your environment.
2.  Once your environment has been created, click the name of the environment to see its details.

The Environment details page provides information, such as the Airflow web UI URL, Google Kubernetes Engine cluster ID, name of the Cloud Storage bucket connected to the DAGs folder.

Note: Cloud Composer uses [Cloud Storage](https://cloud.google.com/storage) to store Apache Airflow DAGs, also known as *workflows*. Each environment has an associated Cloud Storage bucket. Cloud Composer schedules only the DAGs in the Cloud Storage bucket.

**Creating a virtual environment**

Note: Use Google Compute Shell

Python virtual environments are used to isolate package installation from the system.

Install the `virtualenv` environment:

```
apt-get install -y virtualenv
```

Note: If prompted [Y/n], press `Y` and then `Enter`. If you get Permission denied error, then run the command `sudo apt-get install -y virtualenv`.

Build the virtual environment:

```
python3 -m venv venv
```

Activate the virtual environment.

```
source venv/bin/activate
```

### Step 6: Setting DAGs Cloud Storage bucket

In Cloud Shell, run the following to copy the name of the DAGs bucket from your Environment Details page and set a variable to refer to it in Cloud Shell:

Note: Make sure to replace your DAGs bucket name in the following command. Navigate to Navigation menu > Storage, it will be similar to `us-east1-composer-advanced-YOURDAGSBUCKET-bucket`.

```
DAGS_BUCKET=YOURDAGSBUCKET
```

You will be using this variable a few times during the lab.

### Step 7: Setting Airflow variables

Airflow variables are an Airflow-specific concept that is distinct from [environment variables](https://cloud.google.com/composer/docs/how-to/managing/environment-variables). In this step, you'll set the following three [Airflow variables](https://airflow.apache.org/concepts.html#variables) used by the DAG we will deploy: `table_list_file_path`, `gcs_source_bucket`, and `gcs_dest_bucket`.

| Key                    | Value                                                   | Details                                                                          |
| ---------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `table_list_file_path` | /home/airflow/gcs/dags/bq\_copy\_eu\_to\_us\_sample.csv | CSV file listing source and target tables, including dataset                     |
| `gcs_source_bucket`    | {UNIQUE ID}-us                                          | Cloud Storage bucket to use for exporting BigQuery tabledest\_bbucks from source |
| `gcs_dest_bucket`      | {UNIQUE ID}-eu                                          | Cloud Storage bucket to use for importing BigQuery tables at destination         |

The next `gcloud composer` command executes the Airflow CLI sub-command [variables](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#variables). The sub-command passes the arguments to the `gcloud` command line tool.

To set the three variables, you will run the `composer command` once for each row from the above table. The form of the command is this:

```
gcloud composer environments run ENVIRONMENT_NAME\
--location LOCATION variables --\
set KEY VALUE
```

You can safely ignore this gcloud error: `(ERROR: gcloud crashed (TypeError): 'NoneType' object is not callable)`. This is a [known issue](https://cloud.google.com/composer/docs/known-issues#gcloud-410) with using `gcloud composer environments run` with the 410.0.0 version of gcloud. Your variables will still be set accordingly despite the error message.

-   `ENVIRONMENT_NAME` is the name of the environment.
-   `LOCATION` is the Compute Engine region where the environment is located. The gcloud composer command requires including the `--location` flag or [setting the default location](https://cloud.google.com/composer/docs/gcloud-installation) before running the gcloud command.
-   `KEY` and `VALUE` specify the variable and its value to set. Include a space two dashes space ( `--` ) between the left-side `gcloud` command with gcloud-related arguments and the right-side Airflow sub-command-related arguments. Also include a space between the `KEY` and `VALUE` arguments. using the `gcloud composer environments run` command with the variables sub-command in

For example, the `gcs_source_bucket` variable would be set like this:

```
gcloud composer environments run composer-advanced-lab\
--location us-east1 variables --\
set gcs_source_bucket My_Bucket-us
```

To see the value of a variable, run the Airflow CLI sub-command [variables](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#variables) with the `get` argument or use the [Airflow UI](https://cloud.google.com/composer/docs/quickstart#variables-ui).

For example, run the following:

```
gcloud composer environments run composer-advanced-lab\
    --location us-east1 variables --\
    get gcs_source_bucket
```

Note: Make sure to set all three Airflow variables used by the DAG.

### Step 8: Uploading the DAG and dependencies to Cloud Storage

Copy the Google Cloud Python docs samples files into your Cloud shell:

```
cd ~
gsutil -m cp -r gs://spls/gsp283/python-docs-samples .
```

Upload a copy of the third party hook and operator to the plugins folder of your Composer DAGs Cloud Storage bucket:

```
gsutil cp -r python-docs-samples/third_party/apache-airflow/plugins/* gs://$DAGS_BUCKET/plugins
```

Next, upload the DAG and config file to the DAGs Cloud Storage bucket of your environment:

```
gsutil cp python-docs-samples/composer/workflows/bq_copy_across_locations.py gs://$DAGS_BUCKET/dags
gsutil cp python-docs-samples/composer/workflows/bq_copy_eu_to_us_sample.csv gs://$DAGS_BUCKET/dags
```

Cloud Composer registers the DAG in your Airflow environment automatically, and DAG changes occur within 3-5 minutes. You can see task status in the Airflow web interface and confirm the DAG is not scheduled as per the settings.

### Step 9: Using the Airflow UI

To access the Airflow web interface using the Cloud Console:

1.  Go back to the Composer Environments page.
2.  In the Airflow webserver column for the environment, click the Airflow link.
1.  Click on your lab credentials.
2.  The Airflow web UI opens in a new browser window. Data will still be loading when you get here. You can continue with the lab while this is happening.

**Viewing variables**

The variables you set earlier are persisted in your environment.

View the variables by selecting Admin >Variables from the Airflow menu bar.

![](https://user-images.githubusercontent.com/62965911/214003152-6d34e7ce-9760-4ee5-b3f6-0b0cf5f9e13b.png)

**Trigger the DAG to run manually**

Click on the DAGs tab and wait for the links to finish loading.

To trigger the DAG manually, click the play button for `composer_sample_bq_copy_across_locations`.

Click Trigger to confirm this action.

**Exploring DAG runs**

When you upload your DAG file to the DAGs folder in Cloud Storage, Cloud Composer parses the file. If no errors are found, the name of the workflow appears in the DAG listing, and the workflow is queued to run immediately if the schedule conditions are met, in this case, None as per the settings.

The DAG Runs status turns green once the play button is pressed:

1.  Click the name of the DAG to open the DAG details page. This page includes a graphical representation of workflow tasks and dependencies.
1.  Now, in the toolbar, click Graph, then mouseover the graphic for each task to see its status. Note that the border around each task also indicates the status (green border = running; red = failed, etc.).

To run the workflow again from the Graph view:

1.  In the Airflow UI Graph View, click the start graphic.
2.  Click Clear to reset all the tasks and then click OK to confirm.

Refresh your browser while the process is running to see the most recent information.

### Step 10: Validate the results

Now check the status and results of the workflow by going to these Cloud Console pages:

The exported tables were copied from the US bucket to the EU Cloud Storage bucket. Click on Cloud Storage to see the intermediate Avro files in the source (US) and destination (EU) buckets.

The list of tables were imported into the target BigQuery Dataset. Click on BigQuery, then click on your project name and the nyc_tlc_EU dataset to validate the tables are accessible from the dataset you created.

Congratulations!

You've have completed this advanced lab and copied 2 tables programmatically from US to EU! This lab is based on this [blog post](https://cloud.google.com/blog/products/data-analytics/how-to-transfer-bigquery-tables-between-locations-with-cloud-composer) by David Sabater Dinter.