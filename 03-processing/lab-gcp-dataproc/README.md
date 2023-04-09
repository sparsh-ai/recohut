# Running Apache Spark jobs on Cloud Dataproc

## Objective

Running Apache Spark jobs on Cloud Dataproc

In this lab you will learn how to migrate Apache Spark code to Cloud Dataproc. You will follow a sequence of steps progressively moving more of the job components over to GCP services:

-   Run original Spark code on Cloud Dataproc (Lift and Shift)
-   Replace HDFS with Cloud Storage (cloud-native)
-   Automate everything so it runs on job-specific clusters (cloud-optimized)

In this lab you will learn how to:

-   Migrate existing Spark jobs to Cloud Dataproc
-   Modify Spark jobs to use Cloud Storage instead of HDFS
-   Optimize Spark jobs to run on Job specific clusters

**Scenario**

You are migrating an existing Spark workload to Cloud Dataproc and then progressively modifying the Spark code to make use of GCP native features and services.

## Task 1. Lift and shift

### Migrate existing Spark jobs to Cloud Dataproc

You will create a new Cloud Dataproc cluster and then run an imported Jupyter notebook that uses the cluster's default local Hadoop Distributed File system (HDFS) to store source data and then process that data just as you would on any Hadoop cluster using Spark. This demonstrates how many existing analytics workloads such as Jupyter notebooks containing Spark code require no changes when they are migrated to a Cloud Dataproc environment.

### Configure and start a Cloud Dataproc cluster

1.  In the GCP Console, on the Navigation menu, in the Analytics section, click Dataproc.
2.  Click Create Cluster.
3.  Click Create for the item `Cluster on Compute Engine`.
4.  Enter `sparktodp` for Cluster Name.
5.  In the Versioning section, click Change and select 2.0 (Debian 10, Hadoop 3.2, Spark 3.1). This version includes Python3, which is required for the sample code used in this lab.
6.  Click Select.
7.  In the Components > Component gateway section, select Enable component gateway.
8.  Under Optional components, Select Jupyter Notebook.
9.  Click Create.

![](https://user-images.githubusercontent.com/62965911/214003314-ad107306-8093-496d-a75d-a80ed9ce4582.png)

The cluster should start in a few minutes. You can proceed to the next step without waiting for the Cloud Dataproc Cluster to fully deploy.

### Clone the source repository for the lab

In the Cloud Shell you clone the Git repository for the lab and copy the required notebook files to the Cloud Storage bucket used by Cloud Dataproc as the home directory for Jupyter notebooks.

- To clone the Git repository for the lab enter the following command in Cloud Shell:

```
git -C ~ clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

- To locate the default Cloud Storage bucket used by Cloud Dataproc enter the following command in Cloud Shell:

```
export DP_STORAGE="gs://$(gcloud dataproc clusters describe sparktodp --region=us-central1 --format=json | jq -r '.config.configBucket')"
```

- To copy the sample notebooks into the Jupyter working folder enter the following command in Cloud Shell:

```
gsutil -m cp ~/training-data-analyst/quests/sparktobq/*.ipynb $DP_STORAGE/notebooks/jupyter
```

### Log in to the Jupyter Notebook

As soon as the cluster has fully started up you can connect to the Web interfaces. Click the refresh button to check as it may be deployed fully by the time you reach this stage.

1.  On the Dataproc Clusters page wait for the cluster to finish starting and then click the name of your cluster to open the Cluster details page.
2.  Click Web Interfaces.
3.  Click the Jupyter link to open a new Jupyter tab in your browser. This opens the Jupyter home page. Here you can see the contents of the `/notebooks/jupyter` directory in Cloud Storage that now includes the sample Jupyter notebooks used in this lab.
4.  Under the Files tab, click the GCS folder and then click 01_spark.ipynb notebook to open it.
5.  Click Cell and then Run All to run all of the cells in the notebook.
6.  Page back up to the top of the notebook and follow as the notebook completes runs each cell and outputs the results below them.

![](https://user-images.githubusercontent.com/62965911/214003305-e80b09a4-9d58-4b5f-a42f-d366f90987e3.png)

![](https://user-images.githubusercontent.com/62965911/214003309-5d1e41c8-29e1-49c8-9307-ae826d41e8f1.png)

[Download notebook](./nbs/01_spark.ipynb)

You can now step down through the cells and examine the code as it is processed so that you can see what the notebook is doing. In particular pay attention to where the data is saved and processed from.

## Task 2. Separate compute and storage

### Modify Spark jobs to use Cloud Storage instead of HDFS

Taking this original 'Lift & Shift' sample notebook you will now create a copy that decouples the storage requirements for the job from the compute requirements. In this case, all you have to do is replace the Hadoop file system calls with Cloud Storage calls by replacing `hdfs://` storage references with `gs://` references in the code and adjusting folder names as necessary.

You start by using the cloud shell to place a copy of the source data in a new Cloud Storage bucket.

- In the Cloud Shell create a new storage bucket for your source data:

```
export PROJECT_ID=$(gcloud info --format='value(config.project)')
gsutil mb gs://$PROJECT_ID
```

- In the Cloud Shell copy the source data into the bucket:

```
wget https://storage.googleapis.com/cloud-training/dataengineering/lab_assets/sparklab/kddcup.data_10_percent.gz
gsutil cp kddcup.data_10_percent.gz gs://$PROJECT_ID/
```

Make sure that the last command completes and the file has been copied to your new storage bucket.

1.  Switch back to the `01_spark` Jupyter Notebook tab in your browser.
2.  Click File and then select Make a Copy.
3.  When the copy opens, click the 01_spark-Copy1 title and rename it to `De-couple-storage`.
4.  Open the Jupyter tab for `01_spark`.
5.  Click File and then Save and checkpoint to save the notebook.
6.  Click File and then Close and Halt to shutdown the notebook.
7. If you are prompted to confirm that you want to close the notebook click Leave or Cancel.
8. Switch back to the `De-couple-storage` Jupyter Notebook tab in your browser, if necessary.

You no longer need the cells that download and copy the data onto the cluster's internal HDFS file system so you will remove those first. Delete the initial comment cells and the first three code cells ( `In [1]`, `In [2]`, and `In [3]`) so that the notebook now starts with the section Reading in Data.

You will now change the code in the first cell ( still called `In[4]` unless you have rerun the notebook ) that defines the data file source location and reads in the source data. The cell currently contains the following code:

```py
from pyspark.sql import SparkSession, SQLContext, Row
spark = SparkSession.builder.appName("kdd").getOrCreate()
sc = spark.sparkContext
data_file = "hdfs:///kddcup.data_10_percent.gz"
raw_rdd = sc.textFile(data_file).cache()
raw_rdd.take(5)
```

Replace the contents of cell `In [4]` with the following code. The only change here is create a variable to store a Cloud Storage bucket name and then to point the `data_file` to the bucket we used to store the source data on Cloud Storage:

```py
from pyspark.sql import SparkSession, SQLContext, Row
gcs_bucket='[Your-Bucket-Name]'
spark = SparkSession.builder.appName("kdd").getOrCreate()
sc = spark.sparkContext
data_file = "gs://"+gcs_bucket+"//kddcup.data_10_percent.gz"
raw_rdd = sc.textFile(data_file).cache()
raw_rdd.take(5)
```

In the cell you just updated, replace the placeholder `[Your-Bucket-Name]` with the name of the storage bucket you created in the first step of this section. You created that bucket using the Project ID as the name. Replace all of the placeholder text, including the brackets `[]`.

Click Cell and then Run All to run all of the cells in the notebook.

You will see exactly the same output as you did when the file was loaded and run from internal cluster storage. Moving the source data files to Cloud Storage only requires that you repoint your storage source reference from `hdfs://` to `gs://`.

[Download notebook](./nbs/De-couple-storage.ipynb)

## Task 3. Deploy Spark jobs

### Optimize Spark jobs to run on Job specific clusters

You now create a standalone Python file, that can be deployed as a Cloud Dataproc Job, that will perform the same functions as this notebook. To do this you add magic commands to the Python cells in a copy of this notebook to write the cell contents out to a file. You will also add an input parameter handler to set the storage bucket location when the Python script is called to make the code more portable.

1.  In the `De-couple-storage` Jupyter Notebook menu, click File and select Make a Copy.
2.  When the copy opens, click the De-couple-storage-Copy1 and rename it to `PySpark-analysis-file`.
3.  Open the Jupyter tab for `De-couple-storage`.
4.  Click File and then Save and checkpoint to save the notebook.
5.  Click File and then Close and Halt to shutdown the notebook.
6. If you are prompted to confirm that you want to close the notebook click Leave or Cancel.
7.  Switch back to the `PySpark-analysis-file` Jupyter Notebook tab in your browser, if necessary.
8.  Click the first cell at the top of the notebook.
9.  Click Insert and select Insert Cell Above.
10.  Paste the following library import and parameter handling code into this new first code cell:

```
%%writefile spark_analysis.py
import matplotlib
matplotlib.use('agg')
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--bucket", help="bucket for input and output")
args = parser.parse_args()
BUCKET = args.bucket
```

The `%%writefile spark_analysis.py` Jupyter magic command creates a new output file to contain your standalone python script. You will add a variation of this to the remaining cells to append the contents of each cell to the standalone script file.

This code also imports the `matplotlib` module and explicitly sets the default plotting backend via `matplotlib.use('agg')` so that the plotting code runs outside of a Jupyter notebook.

- For the remaining cells insert `%%writefile -a spark_analysis.py` at the start of each Python code cell. These are the five cells labelled In [x].

- In the last cell, where the Pandas bar chart is plotted, remove the `%matplotlib inline` magic command.

Note: You must remove this inline matplotlib Jupyter magic directive or your script will fail when you run it.

- Make sure you have selected the last code cell in the notebook then, in the menu bar, click Insert and select Insert Cell Below.

- Paste the following code into the new cell:

```
%%writefile -a spark_analysis.py
ax[0].get_figure().savefig('report.png');
```

- Add another new cell at the end of the notebook and paste in the following:

```
%%writefile -a spark_analysis.py
import google.cloud.storage as gcs
bucket = gcs.Client().get_bucket(BUCKET)
for blob in bucket.list_blobs(prefix='sparktodp/'):
    blob.delete()
bucket.blob('sparktodp/report.png').upload_from_filename('report.png')
```

- Add a new cell at the end of the notebook and paste in the following:

```
%%writefile -a spark_analysis.py
connections_by_protocol.write.format("csv").mode("overwrite").save(
    "gs://{}/sparktodp/connections_by_protocol".format(BUCKET))
```

You now test that the PySpark code runs successfully as a file by calling the local copy from inside the notebook, passing in a parameter to identify the storage bucket you created earlier that stores the input data for this job. The same bucket will be used to store the report data files produced by the script.

- In the `PySpark-analysis-file` notebook add a new cell at the end of the notebook and paste in the following:

```
BUCKET_list = !gcloud info --format='value(config.project)'
BUCKET=BUCKET_list[0]
print('Writing to {}'.format(BUCKET))
!/opt/conda/miniconda3/bin/python spark_analysis.py --bucket=$BUCKET
```

This code assumes that you have followed the earlier instructions and created a Cloud Storage Bucket using your lab Project ID as the Storage Bucket name. If you used a different name modify this code to set the `BUCKET` variable to the name you used.

- Add a new cell at the end of the notebook and paste in the following:

```
!gsutil ls gs://$BUCKET/sparktodp/**
```

This lists the script output files that have been saved to your Cloud Storage bucket.

- To save a copy of the Python file to persistent storage, add a new cell and paste in the following:

```
!gsutil cp spark_analysis.py gs://$BUCKET/sparktodp/spark_analysis.py
```

- Click Cell and then Run All to run all of the cells in the notebook.

[Download notebook](./nbs/PySpark-analysis-file.ipynb)

### Run the Analysis Job from Cloud Shell.

- Switch back to your Cloud Shell and copy the Python script from Cloud Storage so you can run it as a Cloud Dataproc Job:

```
gsutil cp gs://$PROJECT_ID/sparktodp/spark_analysis.py spark_analysis.py
```

- Create a launch script:

````
nano submit_onejob.sh
```

- Paste the following into the script:

```
#!/bin/bash
gcloud dataproc jobs submit pyspark\
       --cluster sparktodp\
       --region us-central1\
       spark_analysis.py\
       -- --bucket=$1
```

- Press `CTRL+X` then `Y` and `Enter` key to exit and save.

- Make the script executable:

```
chmod +x submit_onejob.sh
```

- Launch the PySpark Analysis job:

```
./submit_onejob.sh $PROJECT_ID
```

1.  In the Cloud Console tab navigate to the Dataproc > Clusters page if it is not already open.
2.  Click Jobs.
3.  Click the name of the job that is listed. You can monitor progress here as well as from the Cloud shell. Wait for the Job to complete successfully.
4.  Navigate to your storage bucket and note that the output report, `/sparktodp/report.png` has an updated time-stamp indicating that the stand-alone job has completed successfully.

![](https://user-images.githubusercontent.com/62965911/214003301-9c41aed5-7119-493c-996d-34ee3e7710ed.png)

The storage bucket used by this Job for input and output data storage is the bucket that is used just the Project ID as the name.

1.  Navigate back to the Dataproc > Clusters page.
2.  Select the sparktodp cluster and click Delete. You don't need it any more.
3.  Click CONFIRM.
4.  Close the Jupyter tabs in your browser.

Congratulations!