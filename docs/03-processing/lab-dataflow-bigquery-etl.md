# Lab: ETL Processing on Google Cloud Using Dataflow and BigQuery

## Objective

ETL Processing on Google Cloud Using Dataflow and BigQuery

## Introduction

In this lab you build several Data Pipelines that ingest data from a publicly available dataset into BigQuery, using these Google Cloud services:

- Cloud Storage
- Dataflow
- BigQuery

You will create your own Data Pipeline, including the design considerations, as well as implementation details, to ensure that your prototype meets the requirements. Be sure to open the python files and read the comments when instructed to.

### Step 1: Enable the Dataflow API

To ensure access to the necessary API, restart the connection to the Dataflow API.

1.  In the Cloud Console, enter "Dataflow API" in the top search bar. Click on the result for Dataflow API.
2.  Click Manage.
3.  Click Disable API.
4.  If asked to confirm, click Disable.
5.  Click Enable.

When the API has been enabled again, the page will show the option to disable.

### Step 2: Download the starter code

In the cloud shell, run the following command to get Dataflow Python Examples from [Google Cloud's professional services GitHub](https://github.com/GoogleCloudPlatform/professional-services/blob/master/examples/dataflow-python-examples/README.md):

```
gsutil -m cp -R gs://spls/gsp290/dataflow-python-examples .
```

Now set a variable equal to your project id, replacing `<YOUR-PROJECT-ID>` with your lab Project ID:

```
export PROJECT=gcp-01-472f3925df21
gcloud config set project $PROJECT
```

### Step 3: Create Cloud Storage Bucket

Use the make bucket command to create a new regional bucket in the us-west2-b region within your project:

```
gsutil mb -c regional -l us-west2  gs://$PROJECT
```

### Step 4: Copy files to your bucket

Use the gsutil command to copy files into the Cloud Storage bucket you just created:

```
gsutil cp gs://spls/gsp290/data_files/usa_names.csv gs://$PROJECT/data_files/
gsutil cp gs://spls/gsp290/data_files/head_usa_names.csv gs://$PROJECT/data_files/
```

### Step 5: Create the BigQuery dataset

Create a dataset in BigQuery called lake. This is where all of your tables will be loaded in BigQuery:

```
bq mk lake
```

### Step 6: Data Ingestion Pipeline

You will create an append-only Dataflow which will ingest data into the BigQuery table.

You will build a Dataflow pipeline with a TextIO source and a BigQueryIO destination to ingest data into BigQuery. More specifically, it will:

-   Ingest the files from Cloud Storage.
-   Filter out the header row in the files.
-   Convert the lines read to dictionary objects.
-   Output the rows to BigQuery.

You can use the built-in code editor which will allow you to view and edit the code in the Google Cloud console.

1. Navigate to the source code by clicking on the Open Editor icon in Cloud Shell.
2. If prompted click on Open in a New Window. It will open the code editor in new window.

In the Code Editor navigate to `dataflow-python-examples` > `dataflow_python_examples` and open the `data_ingestion.py` file. Read through the comments in the file, which explain what the code is doing. This code will populate the data in BigQuery.

![](https://user-images.githubusercontent.com/62965911/214003202-cd8eb3be-2113-4eff-8119-d40b8ceac795.png)

**Run the Apache Beam pipeline**

1.  Return to your Cloud Shell session for this step. You will now do a bit of set up for the required python libraries.

The Dataflow job in this lab requires `Python3.7`. To ensure you're on the proper version, you will run the process on a Python 3.7 Docker container.

Run the following in Cloud Shell:

```
docker run -it -e PROJECT=$PROJECT -v $(pwd)/dataflow-python-examples:/dataflow python:3.7 /bin/bash
```

This command will pull a Docker container with the latest stable version of Python 3.7 and execute a command shell to run the next commands within the container. The `-v` flag provides the source code as a `volume` for the container so that we can edit in Cloud Shell editor and still access it within the container.

Once the container finishes pulling, run the following to install `apache-beam`:

```
pip install apache-beam[gcp]==2.24.0
```

Next, change directories into where you linked the source code:

```
cd dataflow/
```
You will run the Dataflow pipeline in the cloud.

The following will spin up the workers required, and shut them down when complete:

```
python dataflow_python_examples/data_ingestion.py\
  --project=$PROJECT --region=us-west2\
  --runner=DataflowRunner\
  --staging_location=gs://$PROJECT/test\
  --temp_location gs://$PROJECT/test\
  --input gs://$PROJECT/data_files/head_usa_names.csv\
  --save_main_session
```

Return to the Cloud Console and open the Navigation menu > Dataflow to view the status of your job.

Click on the name of your job to watch it's progress. Once your Job Status is Succeeded.

Navigate to BigQuery (Navigation menu > BigQuery) see that your data has been populated.

Click on your project name to see the usa_names table under the `lake` dataset.

Click on the table then navigate to the Preview tab to see examples of the `usa_names` data.

Note: If you don't see the `usa_names` table, try refreshing the page or view the tables using the classic BigQuery UI.

![](https://user-images.githubusercontent.com/62965911/214003223-c9978288-7368-4270-b3bd-4b3b10de768c.png)

![](https://user-images.githubusercontent.com/62965911/214003185-9ef0f776-d270-46f1-b3b3-47dff5e6a54a.png)

### Step 8: Data Transformation Pipeline

You will now build a Dataflow pipeline with a TextIO source and a BigQueryIO destination to ingest data into BigQuery. More specifically, you will:

-   Ingest the files from Cloud Storage.
-   Convert the lines read to dictionary objects.
-   Transform the data which contains the year to a format BigQuery understands as a date.
-   Output the rows to BigQuery.

In the Code Editor, open `data_transformation.py` file. Read through the comments in the file which explain what the code is doing.

**Run the Apache Beam pipeline**

You will run the Dataflow pipeline in the cloud. This will spin up the workers required, and shut them down when complete.

Run the following commands to do so:

```
python dataflow_python_examples/data_transformation.py \
  --project=$PROJECT \
  --region=us-west2 \
  --runner=DataflowRunner \
  --staging_location=gs://$PROJECT/test \
  --temp_location gs://$PROJECT/test \
  --input gs://$PROJECT/data_files/head_usa_names.csv \
  --save_main_session
```

Navigate to Navigation menu > Dataflow and click on the name of this job to view the status of your job.

When your Job Status is Succeeded in the Dataflow Job Status screen, navigate to BigQuery to check to see that your data has been populated.

You should see the usa_names_transformed table under the lake dataset.

Click on the table and navigate to the Preview tab to see examples of the usa_names_transformed data.

Note: If you don't see the usa_names_transformed table, try refreshing the page or view the tables using the classic BigQuery UI.

### Step 9: Data Enrichment Pipeline

You will now build a Dataflow pipeline with a TextIO source and a BigQueryIO destination to ingest data into BigQuery. More specifically, you will:

-   Ingest the files from Cloud Storage.
-   Filter out the header row in the files.
-   Convert the lines read to dictionary objects.
-   Output the rows to BigQuery.

**Review pipeline python code**

In the Code Editor, open `data_enrichment.py` file. Check out the comments which explain what the code is doing. This code will populate the data in BigQuery.

Line 83 currently looks like:

```
values = [x.decode('utf8') for x in csv_row]
```

Edit it so it looks like the following:

```
values = [x for x in csv_row]
```

**Run the Apache Beam pipeline**

Here you'll run the Dataflow pipeline in the cloud.

Run the following to spin up the workers required, and shut them down when complete:

```
python dataflow_python_examples/data_enrichment.py \
  --project=$PROJECT \
  --region=us-west2 \
  --runner=DataflowRunner \
  --staging_location=gs://$PROJECT/test \
  --temp_location gs://$PROJECT/test \
  --input gs://$PROJECT/data_files/head_usa_names.csv \
  --save_main_session
```

Navigate to Navigation menu > Dataflow to view the status of your job.

Once your Job Status is Succeed in the Dataflow Job Status screen, navigate to BigQuery to check to see that your data has been populated.

You should see the usa_names_enriched table under the lake dataset.

Click on the table and navigate to the Preview tab to see examples of the usa_names_enriched data.

Note: If you don't see the usa_names_enriched table, try refreshing the page or view the tables using the classic BigQuery UI.

### Step 10: Data lake to Mart Pipeline

Now build a Dataflow pipeline that reads data from 2 BigQuery data sources, and then joins the data sources. Specifically, you:

-   Ingest files from 2 BigQuery sources.
-   Join the 2 data sources.
-   Filter out the header row in the files.
-   Convert the lines read to dictionary objects.
-   Output the rows to BigQuery.

**Review pipeline python code**

In the Code Editor, open data_lake_to_mart.py file. Read through the comments in the file which explain what the code is doing. This code will populate the data in BigQuery.

**Run the Apache Beam Pipeline**

Now you'll run the Dataflow pipeline in the cloud.

Run the following to spin up the workers required, and shut them down when complete:

```
python dataflow_python_examples/data_lake_to_mart.py \
  --worker_disk_type="compute.googleapis.com/projects//zones//diskTypes/pd-ssd" \
  --max_num_workers=4 \
  --project=$PROJECT \
  --runner=DataflowRunner \
  --staging_location=gs://$PROJECT/test \
  --temp_location gs://$PROJECT/test \
  --save_main_session \
  --region=us-west2
```

Navigate to Navigation menu > Dataflow and click on the name of this new job to view the status.

Once your Job Status is Succeeded in the Dataflow Job Status screen, navigate to BigQuery to check to see that your data has been populated.

You should see the orders_denormalized_sideinput table under the lake dataset.

Click on the table and navigate to the Preview section to see examples of orders_denormalized_sideinput data.

Note: If you don't see the orders_denormalized_sideinput table, try refreshing the page or view the tables using the classic BigQuery UI.

Congratulations!

You have used python files to ingest data into BigQuery using Dataflow.