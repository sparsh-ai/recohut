# Lab: GCP Dataflow Pipeline - A Simple Dataflow Pipeline (Python)

## Objective

In this lab, you will open a Dataflow project, use pipeline filtering, and execute the pipeline locally and on the cloud.

-   Open Dataflow project
-   Pipeline filtering
-   Execute the pipeline locally and on the cloud

In this lab, you learn how to write a simple Dataflow pipeline and run it both locally and on the cloud.

-   Setup a Python Dataflow project using Apache Beam
-   Write a simple pipeline in Python
-   Execute the query on the local machine
-   Execute the query on the cloud

## Task 1. Ensure that the Dataflow API is successfully enabled

-  Execute the following block of code in the Cloud Shell:

```
gcloud services disable dataflow.googleapis.com --force
gcloud services enable dataflow.googleapis.com
```

## Task 2. Preparation

### Open the SSH terminal and connect to the training VM

You will be running all code from a curated training VM.

1.  In the console, on the Navigation menu, click Compute Engine > VM instances.
2.  Locate the line with the instance called training-vm.
3.  On the far right, under Connect, click on SSH to open a terminal window.
4.  In this lab, you will enter CLI commands on the training-vm.

### Download code repository

-   Download a code repository to use in this lab. In the training-vm SSH terminal enter the following:

```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

### Create a Cloud Storage bucket

Follow these instructions to create a bucket.

1.  In the console, on the Navigation menu, click Home.
2.  Select and copy the Project ID.
3.  In the console, on the Navigation menu, click Cloud Storage > Browser.
4.  Click Create Bucket.
5.  Specify the following, and leave the remaining settings as their defaults:
    | Property | Value (type value or select option as specified) |
    | -------- | ------------------------------------------------ |
    | Name | `<your unique bucket name (Project ID)>` |
    | Location type | `Multi-Region` |
    | Location | `<Your location>` |
6.  Click Create.
7. Record the name of your bucket to use in subsequent tasks.
8. In the training-vm SSH terminal enter the following to create an environment variable named "BUCKET" and verify that it exists with the echo command:
    ```
    BUCKET="<your unique bucket name (Project ID)>"
    echo $BUCKET
    ```

## Task 3. Pipeline filtering

The goal of this lab is to become familiar with the structure of a Dataflow project and learn how to execute a Dataflow pipeline.

1.  Return to the training-vm SSH terminal and navigate to the directory `/training-data-analyst/courses/data_analysis/lab2/python` and view the file `grep.py`.
2.  View the file with Nano. Do not make any changes to the code:
    ```
    cd ~/training-data-analyst/courses/data_analysis/lab2/python
    nano grep.py
    ```
3.  Press CTRL+X to exit Nano.

Can you answer these questions about the file `grep.py`?

-   What files are being read?
-   What is the search term?
-   Where does the output go?

There are three transforms in the pipeline:

-   What does the transform do?
-   What does the second transform do?
-   Where does its input come from?
-   What does it do with this input?
-   What does it write to its output?
-   Where does the output go?
-   What does the third transform do?

## Task 4. Execute the pipeline locally

1.  In the training-vm SSH terminal, locally execute `grep.py`:
    ```
    python3 grep.py
    ```
2.  The output file will be `output.txt`. If the output is large enough, it will be sharded into separate parts with names like: `output-00000-of-00001`.
3.  Locate the correct file by examining the file's time:
    ```
    ls -al /tmp
    ```
4.  Examine the output file(s).
5.  You can replace "-*" below with the appropriate suffix:
    ```
    cat /tmp/output-*
    ```

![](https://user-images.githubusercontent.com/62965911/214003251-70c4c151-62ec-436e-ba71-8f7edc283da4.png)

Does the output seem logical?

### Task 5. Execute the pipeline on the cloud

1.  Copy some Java files to the cloud. In the training-vm SSH terminal, enter the following command:
    ```
    gsutil cp ../javahelp/src/main/java/com/google/cloud/training/dataanalyst/javahelp/*.java gs://$BUCKET/javahelp
    ```
2.  Using Nano, edit the Dataflow pipeline in `grepc.py`:
    ```
    nano grepc.py
    ```
3.  Replace PROJECT and BUCKET with your Project ID and Bucket name.
4.  Save the file and close Nano by pressing the CTRL+X key, then type Y, and press Enter.
5.  Submit the Dataflow job to the cloud:
    ```
    python3 grepc.py
    ```
6. Note: Ignore the message: **WARNING:root:Make sure that locally built Python SDK docker image has Python 3.7 interpreter.** Your Dataflow job will start successfully.

Because this is such a small job, running on the cloud will take significantly longer than running it locally (on the order of 7-10 minutes).

1.  Return to the browser tab for the console.
2.  On the Navigation menu, click Dataflow and click on your job to monitor progress.
3.  Wait for the Job status to be Succeeded.
4.  Examine the output in the Cloud Storage bucket.
5.  On the Navigation menu, click Cloud Storage > Browser and click on your bucket.
6.  Click the `javahelp` directory. This job generates the file `output.txt`. If the file is large enough, it will be sharded into multiple parts with names like: `output-0000x-of-000y`. You can identify the most recent file by name or by the Last modified field.
7.  Click on the file to view it.

![](https://user-images.githubusercontent.com/62965911/214003230-dfe6d1bb-8c8b-4027-a1aa-8d196953a3e8.png)

![](https://user-images.githubusercontent.com/62965911/214003210-11693a50-df04-4ea4-b5cb-4313491016b3.png)

Alternatively, you can download the file via the training-vm SSH terminal and view it:

```
gsutil cp gs://$BUCKET/javahelp/output* .
cat output*
```

Congratulations!