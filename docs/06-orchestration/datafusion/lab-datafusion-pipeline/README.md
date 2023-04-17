# Lab: Building and Executing a Pipeline Graph with Data Fusion

## Objective

This lab shows you how to use the Wrangler and Data Pipeline features in Cloud Data Fusion to clean, transform, and process taxi trip data for further analysis.

In this lab, you will:

-   Connect Cloud Data Fusion to a couple of data sources
-   Apply basic transformations
-   Join two data sources
-   Write data to a sink

Often times, data needs go through a number of pre-processing steps before analysts can leverage the data to glean insights. For example, data types may need to be adjusted, anomalies removed, and vague identifiers may need to be converted to more meaningful entries. Cloud Data Fusion is a service for efficiently building ETL/ELT data pipelines. Cloud Data Fusion uses Cloud Dataproc cluster to perform all transforms in the pipeline.

The use of Cloud Data Fusion will be exemplified in this tutorial by using a subset of the NYC TLC Taxi Trips dataset on BigQuery.

## Task 1. Creating a Cloud Data Fusion instance

Thorough directions for creating a Cloud Data Fusion instance can be found in the Creating a Cloud Data Fusion instance Guide. The essential steps are as follows:

- To ensure the training environment is properly configured you must first stop and restart the Cloud Data Fusion API. Run the command below in the Cloud Shell. It will take a few minutes to complete.

```
gcloud services disable datafusion.googleapis.com
gcloud services enable datafusion.googleapis.com
```

- On the Navigation menu, select Data Fusion.

- To create a Cloud Data Fusion instance, click Create an Instance.
  - Enter a name for your instance.
  - Select Basic for the Edition type.
  - Under Authorization section, click Grant Permission.
  - Leave all other fields as their defaults and click Create.

Note: Creation of the instance can take around 15 minutes.

- Once the instance is created, you need one additional step to grant the service account associated with the instance permissions on your project. Navigate to the instance details page by clicking the instance name.

- Copy the service account to your clipboard.
- In the GCP Console navigate to the IAM & Admin > IAM.
- On the IAM Permissions page, click +Grant Access add the service account you copied earlier as a new principals and grant the Cloud Data Fusion API Service Agent role.
- Click Save.

## Task 2. Loading the data

Once the Cloud Data Fusion instance is up and running, you can start using Cloud Data Fusion. However, before Cloud Data Fusion can start ingesting data you have to take some preliminary steps.

- In this example, Cloud Data Fusion will read data out of a storage bucket. In the cloud shell console execute the following commands to create a new bucket and copy the relevant data into it:

```
export BUCKET=$GOOGLE_CLOUD_PROJECT
gsutil mb gs://$BUCKET
gsutil cp gs://cloud-training/OCBL017/ny-taxi-2018-sample.csv gs://$BUCKET
```

- In the command line, execute the following command to create a bucket for temporary storage items that Cloud data Fusion will create:

```
gsutil mb gs://$BUCKET-temp
```

- Click the View Instance link on the Data Fusion instances page, or the details page of an instance. Click username. If prompted to take a tour of the service click on No, Thanks. You should now be in the Cloud Data Fusion UI.

Note: You may need to reload or refresh the Cloud Fusion UI pages to allow prompt loading of the page.

- Wrangler is an interactive, visual tool that lets you see the effects of transformations on a small subset of your data before dispatching large, parallel-processing jobs on the entire dataset. On the Cloud Data Fusion UI, choose Wrangler. On the left side, there is a panel with the pre-configured connections to your data, including the Cloud Storage connection.

- Under GCS, select Cloud Storage Default.

- Click on the bucket corresponding to your project name.

- Select ny-taxi-2018-sample.csv. The data is loaded into the Wrangler screen in row/column form.

- In the Parsing Options window, set Use First Row as Header as True. The data splits into multiple columns.

- Click Confirm.

## Task 3. Cleaning the data

Now, you will perform some transformations to parse and clean the taxi data.

- Click the Down arrow next to the trip_distance column, select Change data type and then click on Float. Repeat for the total_amount column.

- Click the Down arrow next to the pickup_location_id column, select Change data type and then click on String.

- If you look at the data closely, you may find some anomalies, such as negative trip distances. You can avoid those negative values by filtering out in Wrangler. Click the Down arrow next to the trip_distance column and select Filter. Click if Custom condition and input >0.0

- Click on Apply.

![](https://user-images.githubusercontent.com/62965911/214003271-cc4e8517-9deb-4dfb-977b-1e76025407aa.png)

## Task 4. Creating the pipeline

Basic data cleansing is now complete and you've run transformations on a subset of your data. You can now create a batch pipeline to run transformations on all your data.

Cloud Data Fusion translates your visually built pipeline into an Apache Spark or MapReduce program that executes transformations on an ephemeral Cloud Dataproc cluster in parallel. This enables you to easily execute complex transformations over vast quantities of data in a scalable, reliable manner, without having to wrestle with infrastructure and technology.

- On the upper-right side of the Google Cloud Fusion UI, click Create a Pipeline.

- In the dialog that appears, select Batch pipeline.

- In the Data Pipelines UI, you will see a GCSFile source node connected to a Wrangler node. The Wrangler node contains all the transformations you applied in the Wrangler view captured as directive grammar. Hover over the Wrangler node and select Properties.

![](https://user-images.githubusercontent.com/62965911/214003274-67c56282-204c-4504-ac20-811dcbbb0f55.png)

- At this stage, you can apply more transformations by clicking the Wrangle button. Delete the extra column by pressing the red trashcan icon beside its name. Click Validate on top right corner to check for any errors. To close the Wrangler tool click the X button in the top right corner.

## Task 5. Adding a data source

The taxi data contains several cryptic columns such as pickup_location_id, that aren't immediately transparent to an analyst. You are going to add a data source to the pipeline that maps the pickup_location_id column to a relevant location name. The mapping information will be stored in a BigQuery table.

- In a separate tab, open the BigQuery UI in the Cloud Console. Click Done on the 'Welcome to BigQuery in the Cloud Console' launch page.

- In the Explorer section of the BigQuery UI, click the three dots beside your GCP Project ID.

- On the menu that appears click the Create dataset link.

- In the Dataset ID field type in `trips`.

- Click on Create dataset.

- To create the desired table in the newly created dataset, Go to editor window, navigate to More > Query Settings. This process will ensure you can access your table from Cloud Data Fusion.

- Select the item for `Set a destination table for query results`. For Dataset input `trips` select from the dropdown. Table Id input `zone_id_mapping`. Click Save.

- Enter the following query in the Query Editor and then click Run:

```sql
SELECT
  zone_id,
  zone_name,
  borough
FROM
  `bigquery-public-data.new_york_taxi_trips.taxi_zone_geom`
```

![](https://user-images.githubusercontent.com/62965911/214003169-24e75787-cf9a-4159-ac8c-949e30372d69.png)

You can see that this table contains the mapping from zone_id to its name and borough.

- Now, you will add a source in your pipeline to access this BigQuery table. Return to tab where you have Cloud Data Fusion open, from the Plugin palette on the left, select BigQuery from the Source section. A BigQuery source node appears on the canvas with the two other nodes.

- Hover over the new BigQuery source node and click Properties.

- To configure the Reference Name, enter zone_mapping, which is used to identify this data source for lineage purposes.

- The BigQuery Dataset and Table configurations are the Dataset and Table you setup in BigQuery a few steps earlier: `trips` and `zone_id_mapping`. For Temporary Bucket Name input the name of your project followed by "-temp", which corresponds to the bucket you created in Task 2.

- To populate the schema of this table from BigQuery, click Get Schema. The fields will appear on the right side of the wizard.

- Click Validate on top right corner to check for any errors. To close the BigQuery Properties window click the X button in the top right corner.

## Task 6. Joining two sources

Now you can join the two data sources—taxi trip data and zone names—to generate more meaningful output.

- Under the Analytics section in the Plugin Palette, choose Joiner. A Joiner node appears on the canvas.

- To connect the Wrangler node and the BigQuery node to the Joiner node: Drag a connection arrow > on the right edge of the source node and drop on the destination node.

To configure the Joiner node, which is similar to a SQL JOIN syntax:

- Click Properties of Joiner.
- Leave the label as Joiner.
- Change the Join Type to Inner
- Set the Join Condition to join the pickup_location_id column in the Wrangler node to the zone_id column in the BigQuery node.
- To generate the schema of the resultant join, click Get Schema.
- In the Output Schema table on the right, remove the zone_id and pickup_location_id fields by hitting the red garbage can icon.
- Click Validate on top right corner to check for any errors. Close the window by clicking the X button in the top right corner.

## Task 7. Storing the output to BigQuery

You will store the result of the pipeline into a BigQuery table. Where you store your data is called a sink.

- In the Sink section of the Plugin Palette, choose BigQuery.

- Connect the Joiner node to the BigQuery node. Drag a connection arrow > on the right edge of the source node and drop on the destination node.

- Open the BigQuery2 node by hovering on it and then clicking Properties. You will use a configuration that's similar to the existing BigQuery source. Provide bq_insert for the Reference Name field and then use trips for the Dataset and the name of your project followed by "-temp" as Temporary Bucket Name. You will write to a new table that will be created for this pipeline execution. In Table field, enter trips_pickup_name.

- Click Validate on top right corner to check for any errors. Close the window by clicking the X button in the top right corner.

## Task 8. Deploying and running the pipeline

At this point you have created your first pipeline and can deploy and run the pipeline.

- Name your pipeline in the upper left corner of the Data Fusion UI and click Save.

- Now you will deploy the pipeline. In the upper-right corner of the page, click Deploy.

- On the next screen click Run to start processing data.

- When you run a pipeline, Cloud Data Fusion provisions an ephemeral Cloud Dataproc cluster, runs the pipeline, and then tears down the cluster. This could take a few minutes. You can observe the status of the pipeline transition from Provisioning to Starting and from Starting to Running to Succeeded during this time.

![](https://user-images.githubusercontent.com/62965911/214003265-02ac63ea-b61c-46e7-bf5d-b1fc3c53b07d.png)

Note: The pipeline transition may take 10-15 minutes to succeeded.

![](https://user-images.githubusercontent.com/62965911/214003268-0968dec2-638d-47c4-8c3e-9171b2cd2282.png)

## Task 9. Viewing the results

To view the results after the pipeline runs:

Return to the tab where you have BigQuery open. Run the query below to see the values in the trips_pickup_name table:

```
SELECT
  *
FROM
  `trips.trips_pickup_name`
```

![](https://user-images.githubusercontent.com/62965911/214003172-c3b919d2-ca23-4098-a8e7-78eb9c358b7e.png)

Congratulations!
