# GCP Dataflow Size Inputs

## Objective

Serverless Data Analysis with Dataflow - Side Inputs (Python)

In this lab, you learn how to load data into BigQuery and run complex queries. Next, you will execute a Dataflow pipeline that can carry out Map and Reduce operations, use side inputs and stream into BigQuery.

In this lab, you learn how to use BigQuery as a data source into Dataflow, and how to use the results of a pipeline as a side input to another pipeline.

- Read data from BigQuery into Dataflow
- Use the output of a pipeline as a side-input to another pipeline

## Task 1. Preparation

### Ensure that the Dataflow API is successfully enabled

To ensure access to the necessary API, restart the connection to the Dataflow API.

1.  In the Cloud Console, enter Dataflow API in the top search bar. Click on the result for Dataflow API.
2.  Click Manage.
3.  Click Disable API.
4.  If asked to confirm, click Disable.
5.  Click Enable.

When the API has been enabled again, the page will show the option to disable.

### Open the SSH terminal and connect to the training VM

You will be running all code from a curated training VM.

1.  In the Console, on the Navigation menu, click Compute Engine > VM instances.
2.  Locate the line with the instance called training-vm.
3.  On the far right, under Connect, click on SSH to open a terminal window.
4.  In this lab, you will enter CLI commands on the training-vm.

### Download Code Repository

-   Next you will download a code repository for use in this lab. In the training-vm SSH terminal enter the following:

```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

### Create a Cloud Storage bucket

Follow these instructions to create a bucket.

1.  In the Console, on the Navigation menu, click Home.
2.  Select and copy the Project ID.
3.  In the Console, on the Navigation menu, click Cloud Storage > Browser.
4.  Click Create Bucket.
5.  Specify the following, and leave the remaining settings as their defaults:
    | Property | Value (type value or select option as specified) |
    | Name | `<your unique bucket name (Project ID)>` |
    | Location type | `Multi-Region` |
    | Location | `<Your location>` |
6.  Click Create. Record the name of your bucket. You will need it in subsequent tasks.
7.  In the training-vm SSH terminal enter the following to create two environment variables. One named "BUCKET" and the other named "PROJECT". Verify that each exists with the echo command:
    ```
    BUCKET="<your unique bucket name (Project ID)>"
    echo $BUCKET
    PROJECT="<your unique project name (Project ID)>"
    echo $PROJECT
    ```

## Task 2. Try using BigQuery query

1.  In the console, on the Navigation menu, click BigQuery.
2.  If prompted click Done.
3.  Click Compose new query and type the following query:
    ```sql
    SELECT
    content
    FROM
    `cloud-training-demos.github_repos.contents_java`
    LIMIT
    10
    ```
4.  Click on Run.

What is being returned?

The BigQuery table `fh-bigquery.github_extracts.contents_java_2016` contains the content (and some metadata) of all the Java files present in GitHub in 2016.

To find out how many Java files this table has, type the following query and click Run:

```sql
SELECT
  COUNT(*)
FROM
  `cloud-training-demos.github_repos.contents_java`
```

Q: Why do you think zero bytes of data were processed to return the result?

- [ ] There were 0 records returned in the result.
- [ ] BigQuery stores common metadata about the table (like row count). Querying metadata processes 0 bytes.
- [ ] This dataset is not properly set up for billing.
- [ ] Cache is enabled so all queries process 0 bytes.

Q: How many files are there in this dataset?

Q: Is this a dataset you want to process locally or on the cloud?

## Task 3. Explore the pipeline code

- Return to the training-vm SSH terminal and navigate to the directory `/training-data-analyst/courses/data_analysis/lab2/python` and view the file `JavaProjectsThatNeedHelp.py`.

- View the file with Nano. Do not make any changes to the code. Press Ctrl+X to exit Nano.

```
cd ~/training-data-analyst/courses/data_analysis/lab2/python
nano JavaProjectsThatNeedHelp.py
```

Refer to this diagram as you read the code. The pipeline looks like this:

![](https://user-images.githubusercontent.com/62965911/214003265-02ac63ea-b61c-46e7-bf5d-b1fc3c53b07d.png)

Answer the following questions:

-   Looking at the class documentation at the very top, what is the purpose of this pipeline?
-   Where does the content come from?
-   What does the left side of the pipeline do?
-   What does the right side of the pipeline do?
-   What does ToLines do? (Hint: look at the content field of the BigQuery result)
-   Why is the result of ReadFromBQ stored in a named PCollection instead of being directly passed to another step?
-   What are the two actions carried out on the PCollection generated from ReadFromBQ?
-   If a file has 3 FIXMEs and 2 TODOs in its content (on different lines), how many calls for help are associated with it?
-   If a file is in the package com.google.devtools.build, what are the packages that it is associated with?
-   popular_packages and help_packages are both named PCollections and both used in the Scores (side inputs) step of the pipeline. Which one is the main input and which is the side input?
-   What is the method used in the Scores step?
-   What Python data type is the side input converted into in the Scores step?

Note: The Java version of this program is slightly different from the Python version. The Java SDK supports AsMap and the Python SDK doesn't. It supports AsDict instead. In Java, the PCollection is converted into a View as a preparatory step before it is used. In Python, the PCollection conversion occurs in the step where it is used.

## Task 4. Execute the pipeline

- The program requires BUCKET and PROJECT values and whether you want to run the pipeline locally using `--DirectRunner` or on the cloud using `--DataFlowRunner`.

- Execute the pipeline locally by typing the following into the training-vm SSH terminal:

```
python3 JavaProjectsThatNeedHelp.py --bucket $BUCKET --project $PROJECT --DirectRunner
```

Note: Please ignore the warning if any and move forward.

- Once the pipeline has finished executing, On the Navigation menu, click Cloud Storage > Browser and click on your bucket. You will find the results in the javahelp folder. Click on the Result object to examine the output.

- Execute the pipeline on the cloud by typing the following into the training-vm SSH terminal:

```
python3 JavaProjectsThatNeedHelp.py --bucket $BUCKET --project $PROJECT --DataFlowRunner
```

Note: Please ignore the warning if any and move forward.

- Return to the browser tab for Console. On the Navigation menu, click Dataflow and click on your job to monitor progress.

- Once the pipeline has finished executing, On the Navigation menu, click Cloud Storage > Browser and click on your bucket. You will find the results in the javahelp folder. Click on the Result object to examine the output. The file name will be the same but you will notice that the file creation time is more recent.