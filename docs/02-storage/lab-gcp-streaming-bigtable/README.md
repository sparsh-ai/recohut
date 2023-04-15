# Lab: GCP Streaming Bigtable

## Objective

Streaming Data Processing - Streaming Data Pipelines into Bigtable

In this lab, you will use Dataflow to collect traffic events from simulated traffic sensor data made available through Google Cloud PubSub, and write them into a Bigtable table.

In this lab, you will perform the following tasks:

-   Launch Dataflow pipeline to read from Pub/Sub and write into Bigtable.
-   Open an HBase shell to query the Bigtable database.

## Preparation

- Go to the Compute > VM > training-vm instance
- Connect via SSH
- Verify by listing our the files - `ls /training`
 
![](https://user-images.githubusercontent.com/62965911/214003366-93f23160-3465-4460-b07e-7c50fcf978a7.png)

- Next you will download a code repository for use in this lab:

```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

- Set environment variables. On the training-vm SSH terminal enter the following:

```
source /training/project_env.sh
```

This script sets the `DEVSHELL_PROJECT_ID` and `BUCKET` environment variables.

**Prepare HBase quickstart files**

- In the training-vm SSH terminal, run the script to download and unzip the quickstart files (you will later use these to run the HBase shell.):

```
cd ~/training-data-analyst/courses/streaming/process/sandiego
./install_quickstart.sh
```

## Simulate traffic sensor data into Pub/Sub

- In the training-vm SSH terminal, start the sensor simulator. The script reads sample data from a csv file and publishes it to Pub/Sub:

```
/training/sensor_magic.sh
```

This command will send 1 hour of data in 1 minute. Let the script continue to run in the current terminal.

![](https://user-images.githubusercontent.com/62965911/214003254-7bc4d980-3538-49cf-a95a-9298142ffa7a.png)

- Open a second SSH terminal and connect to the training VM

- In the new training-vm SSH terminal, enter the following:

```
source /training/project_env.sh
```

## Launch dataflow pipeline

- To ensure that the proper APIs and permissions are set, execute the following block of code in the Cloud Shell:

```
gcloud services disable dataflow.googleapis.com --force
gcloud services enable dataflow.googleapis.com
```

- In the second training-vm SSH terminal, navigate to the directory for this lab. Examine the script in Cloud Shell or using nano. Do not make any changes to the code.:

```
cd ~/training-data-analyst/courses/streaming/process/sandiego
nano run_oncloud.sh
```

:::tip What does the script do?
The script takes 3 required arguments: project id, bucket name, classname and possibly a 4th argument: options. In this part of the lab, we will use the --bigtable option which will direct the pipeline to write into Cloud Bigtable.
:::

- Press CTRL+X to exit.

- Run the following script to create the Bigtable instance:

```
cd ~/training-data-analyst/courses/streaming/process/sandiego
./create_cbt.sh
```

- Run the Dataflow pipeline to read from PubSub and write into Cloud Bigtable:

```
cd ~/training-data-analyst/courses/streaming/process/sandiego
./run_oncloud.sh $DEVSHELL_PROJECT_ID $BUCKET CurrentConditions --bigtable
```

## Explore the pipeline

- Return to the browser tab for Console. On the Navigation menu, click Dataflow and click on the new pipeline job. Confirm that the pipeline job is listed and verify that it is running without errors.

- Find the write:cbt step in the pipeline graph, and click on the down arrow on the right to see the writer in action. Click on the given writer. Review the Bigtable Options in the Step summary.

![](https://user-images.githubusercontent.com/62965911/214003190-d9bc852f-22a2-4808-8ef3-b78ee9358695.png)

## Query Bigtable data

- In the second training-vm SSH terminal, run the quickstart.sh script to launch the HBase shell:

```
cd ~/training-data-analyst/courses/streaming/process/sandiego/quickstart
./quickstart.sh
```

Note: If it fails, try the above step again.

- When the script completes, you will be in an HBase shell prompt that looks like this:

```
hbase(main):001:0>
```

- At the HBase shell prompt, type the following query to retrieve 2 rows from your Bigtable table that was populated by the pipeline. It may take a few minutes for results to return via the HBase query. Repeat the 'scan' command until you see a list of rows returned:

```
scan 'current_conditions', {'LIMIT' => 2}
```

- Review the output. Notice each row is broken into column, timestamp, value combinations.

- Run another query. This time look only at the lane: speed column, limit to 10 rows, and specify rowid patterns for start and end rows to scan over:

```
scan 'current_conditions', {'LIMIT' => 10, STARTROW => '15#S#1', ENDROW => '15#S#999', COLUMN => 'lane:speed'}
```

- Review the output. Notice that you see 10 of the column, timestamp, value combinations, all of which correspond to Highway 15. Also notice that column is restricted to lane: speed.

![](https://user-images.githubusercontent.com/62965911/214003216-b381f392-96b3-4cc0-8311-8ec470df26da.png)

- Feel free to run other queries if you are familiar with the syntax. Once you're satisfied, enter quit to exit the shell:

```
quit
```

## Cleanup

- In the second training-vm SSH terminal, run the following script to delete your Bigtable instance:

```
cd ~/training-data-analyst/courses/streaming/process/sandiego
./delete_cbt.sh
```

- If prompted to confirm, enter Y.

- On your Dataflow page in your Cloud Console, click on the pipeline job name.

- Click Stop on the top menu bar. Select Cancel, and then click Stop Job.

- Go back to the first SSH terminal with the publisher, and enter Ctrl+C to stop it.

- In the BigQuery console, click on the three dots next to the demos dataset, and click Delete.

- Type delete and then click Delete.

Congratulations!