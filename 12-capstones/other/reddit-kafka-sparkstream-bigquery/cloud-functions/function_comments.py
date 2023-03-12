## Load BigQuery Imports
from google.cloud import bigquery

def hello_gcs(event, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed,
       and works for all Cloud Storage CRUD operations.
    Args:
        event (dict):  The dictionary with data specific to this type of event.
                       The `data` field contains a description of the event in
                       the Cloud Storage `object` format described here:
                       https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Cloud Logging
    """


    ## Take only events where PARQUET file is updated
    if "parquet" in event["name"]:
        print('Event ID: {}'.format(context.event_id))
        print('Event type: {}'.format(context.event_type))
        print('Bucket: {}'.format(event['bucket']))
        print('File: {}'.format(event['name']))
        print('Created: {}'.format(event['timeCreated']))

        ################################ LOAD PARQUET FILE SECTION ############################################
        ### Global Variables
        BQ_CLIENT = bigquery.Client()
        TYPE = "comments"
        ## Format = projectID.BQ_Dataset.TableName
        TABLE_ID = "learning-gcp-356802.fedex_reddit_dataset." + TYPE

        ## Configuration
        job_config = bigquery.LoadJobConfig(source_format="PARQUET",
                                            write_disposition="WRITE_APPEND",
                                            time_partitioning=bigquery.table.TimePartitioning("DAY", field=TYPE[:-1] + "_datetime"))
        URI = "gs://kafka-reddit-" + TYPE + "-stream/" + event["name"]

        ## Check Rows Before load
        try:
            ## If Table Exists
            destination_table = BQ_CLIENT.get_table(TABLE_ID)
            prev_rows = destination_table.num_rows

            ## Make an API Request
            load_job = BQ_CLIENT.load_table_from_uri(URI, TABLE_ID, job_config=job_config)  

            ## Wait for Job to complete
            load_job.result()

            ## Print Results
            destination_table = BQ_CLIENT.get_table(TABLE_ID)
            after_rows = destination_table.num_rows
            print("Loaded {} rows.".format(after_rows - prev_rows))

        except:
            ## If Table does not exist
            prev_rows = 0

            ## Make an API Request
            URI = "gs://kafka-reddit-" + TYPE + "-stream/year=2022/*"
            load_job = BQ_CLIENT.load_table_from_uri(URI, TABLE_ID, job_config=job_config)  

            ## Wait for Job to complete
            load_job.result()

            ## Print Results
            destination_table = BQ_CLIENT.get_table(TABLE_ID)
            after_rows = destination_table.num_rows
            print("Loaded {} rows.".format(after_rows - prev_rows))