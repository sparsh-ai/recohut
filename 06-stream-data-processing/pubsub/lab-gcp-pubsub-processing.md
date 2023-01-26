# Streaming Data Processing - Streaming Data Pipelines

## Objective

In this lab, you will use Dataflow to collect traffic events from simulated traffic sensor data made available through Google Cloud PubSub, process them into an actionable average, and store the raw data in BigQuery for later analysis. You will learn how to start a Dataflow pipeline, monitor it, and, lastly, optimize it.

In this lab, you will perform the following tasks:

-   Launch Dataflow and run a Dataflow job
-   Understand how data elements flow through the transformations of a Dataflow pipeline
-   Connect Dataflow to Pub/Sub and BigQuery
-   Observe and understand how Dataflow autoscaling adjusts compute resources to process input data optimally
-   Learn where to find logging information created by Dataflow
-   Explore metrics and create alerts and dashboards with Cloud Monitoring

## Preparation

- Go to the Compute > VM > training-vm instance
- Connect via SSH
- Verify by listing our the files - `ls /training`
 
![](https://user-images.githubusercontent.com/62965911/211250465-ee05a5dd-7b9e-42a3-95cd-d6268d0e53af.png)

- Next you will download a code repository for use in this lab:

```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

- Set environment variables. On the training-vm SSH terminal enter the following:

```
source /training/project_env.sh
```

This script sets the `DEVSHELL_PROJECT_ID` and `BUCKET` environment variables.

## Create a BigQuery dataset and Cloud Storage bucket

- In the Google Cloud Console, select Navigation menu > BigQuery.

- To create a dataset, click on the View actions icon next to your project ID and select Create dataset.

- Next, name your Dataset ID `demos` and leave all other options at their default values, and then click Create dataset.

- A bucket should already exist that has the same name as the Project ID. Verify by going to the Console, on the Navigation menu (Navigation menu icon), click Cloud Storage > Buckets.

## Simulate traffic sensor data into Pub/Sub

- In the training-vm SSH terminal, start the sensor simulator. The script reads sample data from a CSV file and publishes it to Pub/Sub:

```
/training/sensor_magic.sh
```

![](https://user-images.githubusercontent.com/62965911/211250458-3ced9733-961a-4dfa-a6d7-fbae43790139.png)

This command will send 1 hour of data in 1 minute. Let the script continue to run in the current terminal.

- Open a second SSH terminal and connect to the training VM

- In the new training-vm SSH terminal enter the following:

```
source /training/project_env.sh
```

## Launch Dataflow pipeline

**Verify that Google Cloud Dataflow API is enabled for this project**

- To ensure that the proper APIs and permissions are set, execute the following block of code in the Cloud Shell.

```
gcloud services disable dataflow.googleapis.com --force
gcloud services enable dataflow.googleapis.com
```

- Return to the second training-vm SSH terminal. Change into the directory for this lab.

```
cd ~/training-data-analyst/courses/streaming/process/sandiego
```

- Identify the script that creates and runs the Dataflow pipeline.

```
cat run_oncloud.sh
```

![](https://user-images.githubusercontent.com/62965911/211250460-9a2a7320-229e-46b1-97bb-5363abed4a8e.png)

The script requires three arguments: project id, bucket name, classname. A 4th optional argument is options.

There are 4 java files that you can choose from for classname. Each reads the traffic data from Pub/Sub and runs different aggregations/computations.

- Go into the java directory. Identify the source file AverageSpeeds.java.

```
cd ~/training-data-analyst/courses/streaming/process/sandiego/src/main/java/com/google/cloud/training/dataanalyst/sandiego
cat AverageSpeeds.java
```

- Return to the training-vm SSH terminal. Run the Dataflow pipeline to read from PubSub and write into BigQuery:

```
cd ~/training-data-analyst/courses/streaming/process/sandiego
./run_oncloud.sh $DEVSHELL_PROJECT_ID $BUCKET AverageSpeeds
```

This script uses maven to build a Dataflow streaming pipeline in Java.

## Explore the pipeline

This Dataflow pipeline reads messages from a Pub/Sub topic, parses the JSON of the input message, produces one main output and writes to BigQuery.

- Return to the browser tab for Console. On the Navigation menu (Navigation menu icon), click Dataflow and click on your job to monitor progress.

:::note
If Dataflow Job failed, run the command ./run_oncloud.sh $DEVSHELL_PROJECT_ID $BUCKET AverageSpeeds again.
:::

![](https://user-images.githubusercontent.com/62965911/211250453-76a63bec-bae3-4a81-9785-9797e1ff6de1.png)

- After the pipeline is running, click on the Navigation menu (Navigation menu icon), click Pub/Sub > Topics.

- Examine the line for Topic name for the topic sandiego.

![](https://user-images.githubusercontent.com/62965911/211250446-551237d8-0d58-41cd-8001-059e7bea6bdb.png)

- Return to the Navigation menu (Navigation menu icon), click Dataflow and click on your job.

- Compare the [code in the Github](https://github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/streaming/process/sandiego/src/main/java/com/google/cloud/training/dataanalyst/sandiego/AverageSpeeds.java), AverageSpeeds.java and the pipeline graph on the page for your Dataflow job.

- Find the `GetMessages` pipeline step in the graph, and then find the corresponding code in the AverageSpeeds.java file. This is the pipeline step that reads from the Pub/Sub topic. It creates a collection of Strings - which corresponds to Pub/Sub messages that have been read.

Do you see a subscription created?

How does the code pull messages from Pub/Sub?

- Find the `Time Window` pipeline step in the graph and in code. In this pipeline step we create a window of a duration specified in the pipeline parameters (sliding window in this case). This window will accumulate the traffic data from the previous step until end of window, and pass it to the next steps for further transforms.

What is the window interval?

How often is a new window created?

- Find the `BySensor` and `AvgBySensor` pipeline steps in the graph, and then find the corresponding code snippet in the AverageSpeeds.java file. This BySensor does a grouping of all events in the window by sensor id, while AvgBySensor will then compute the mean speed for each grouping.

- Find the `ToBQRow` pipeline step in the graph and in code. This step simply creates a "row" with the average computed from the previous step together with the lane information.

:::note
In practice, other actions could be taken in the ToBQRow step. For example, it could compare the calculated mean against a predefined threshold and log the results of the comparison in Cloud Logging.
:::

- Find the `BigQueryIO.Write` in both the pipeline graph and in the source code. This step writes the row out of the pipeline into a BigQuery table. Because we chose the WriteDisposition.WRITE_APPEND write disposition, new records will be appended to the table.

- Return to the BigQuery web UI tab. Refresh your browser.

- Find your project name and the `demos` dataset you created. The small arrow to the left of the dataset name demos should now be active and clicking on it will reveal the average_speeds table.

![](https://user-images.githubusercontent.com/62965911/211250449-4e4c3de1-f48e-457b-a598-627d19c031a1.png)

:::note
It will take several minutes before the average_speeds table appears in BigQuery.
:::

:::tip ACTIVITY
**Determine throughput rates**

One common activity when monitoring and improving Dataflow pipelines is figuring out how many elements the pipeline processes per second, what the system lag is, and how many data elements have been processed so far. In this activity you will learn where in the Cloud Console one can find information about processed elements and time.

- Return to the browser tab for Console. On the Navigation menu (Navigation menu icon), click Dataflow and click on your job to monitor progress (it will have your username in the pipeline name).
- Select the GetMessages pipeline node in the graph and look at the step metrics on the right.
    - System Lag is an important metric for streaming pipelines. It represents the amount of time data elements are waiting to be processed since they "arrived" in the input of the transformation step.
    - Elements Added metric under output collections tells you how many data elements exited this step (for the Read PubSub Msg step of the pipeline it also represents the number of Pub/Sub messages read from the topic by the Pub/Sub IO connector).
- Select the Time Window node in the graph. Observe how the Elements Added metric under the Input Collections of the Time Window step matches the Elements Added metric under the Output Collections of the previous step GetMessages.
:::

## Review BigQuery output

- In the Query editor window, type (or copy-and-paste) the following query. Use the following query to observe the output from the Dataflow job. Click Run:

```sql
SELECT *
FROM `demos.average_speeds`
ORDER BY timestamp DESC
LIMIT 100
```

- Find the last update to the table by running the following SQL:

```sql
SELECT
MAX(timestamp)
FROM
`demos.average_speeds`
```

- Next use the time travel capability of BigQuery to reference the state of the table at a previous point in time.

The query below will return a subset of rows from the average_speeds table that existed at 10 minutes ago. If you encounter this error please reduce the scope of your time travel by lowering the minute value:

```sql
SELECT *
FROM `demos.average_speeds`
FOR SYSTEM_TIME AS OF TIMESTAMP_SUB(CURRENT_TIMESTAMP, INTERVAL 10 MINUTE)
ORDER BY timestamp DESC
LIMIT 100
```

![](https://user-images.githubusercontent.com/62965911/211250433-388e4536-98a3-43ce-bf3b-2779ffaf0257.png)

:::tip ACTIVITY
**Observe and understand autoscaling**

Observe how Dataflow scales the number of workers to process the backlog of incoming Pub/Sub messages.

- Return to the browser tab for Console. On the Navigation menu (Navigation menu icon), click Dataflow and click on your pipeline job.
- Examine the Job metrics panel on the right, and review the Autoscaling section. How many workers are currently being used to process messages in the Pub/Sub topic?
- Click on More history and review how many workers were used at different points in time during pipeline execution.
- The data from a traffic sensor simulator started at the beginning of the lab creates hundreds of messages per second in the Pub/Sub topic. This will cause Dataflow to increase the number of workers to keep the system lag of the pipeline at optimal levels.
- Click on More history. In the Worker pool, you can see how Dataflow changed the number of workers. Notice the Status column that explains the reason for the change.
:::

![](https://user-images.githubusercontent.com/62965911/211250440-223f73d8-78f3-4c09-8ff1-bc633c750f7d.png)

- Stop the script by returning back to the SSH terminal and type `CTRL+C`.

Congratulations!
