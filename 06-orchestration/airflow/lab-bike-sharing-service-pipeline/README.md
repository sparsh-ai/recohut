# Bike Sharing Service Data Pipeline

This lab will be divided into five different DAG levels. Each DAG level will have specific learning objectives, as follows:

- **Level 1**: Learn how to create a DAG and submit it
- **Level 2**: Learn how to create a BigQuery DAG
- **Level 3**: Learn how to use variables
- **Level 4**: Learn how to apply task idempotency
- **Level 5**: Learn how to handle late data

Level 1 DAG - Creating dummy workflows
--------------------------------------

The main goal of the Level 1 DAG is for us to understand how to create a DAG using Python, how timing in Airflow works, and how to handle task dependencies.

As a first step, we want to declare our DAG. The DAG will have information about the following:

1. DAG **identifier** (**ID**)
2. DAG owner
3. Schedule interval
4. Start date

For **schedule_interval**, it follows the **CronJob** scheduling format. If you are not familiar with the **CronJob** format, it uses five numerical values that represent the following: minute, hour, day(month), month, and day(week).

The tricky part of the DAG is **start_date**. It's a little bit counter-intuitive if you're using Airflow for the first time. Airflow DAG runtime is a combination of both **start_date** and **schedule_interval**. So, if the start date is **January 1** and scheduled at **midnight**, Airflow will know that **midnight** on **January 1** has already passed, and will start the scheduler tomorrow, on **January 2** at **midnight**. So if we want the DAG to start immediately on **January 1**, we need to tell Airflow that the **start_date** value is supposed to be **December 31, 2020** or the day -1.

The other parameters in the DAG declaration are optional---for example, the DAG owner, handling task errors, and other parameters. We will skip these for now but you can find out more about them in the Airflow public documentation.

Level 2 DAG - Scheduling a pipeline from Cloud SQL to GCS and BigQuery datasets
-------------------------------------------------------------------------------

The main goal of the Level 2 DAG is for us to understand how to create a DAG specifically for doing ELT from the data source to GCS and BigQuery. In this exercise, we will create a DAG that extracts data from Cloud SQL to our GCS bucket, and from the GCS bucket to BigQuery tables.

In this exercise, we will need a Cloud SQL instance to demonstrate extraction using Airflow. As a summary, this is what we need to do in the section:

1. Create a Cloud SQL instance.
2. Configure the Cloud SQL service account **identity and access management** (**IAM**) permission as **GCS Object Admin**.
3. Create a **stations** table from the MySQL console.
4. Import the **stations** table data from a **comma-separated values** (**CSV**) file.

If you are already in this state, you are good to go to the next steps. The next steps are given here:

- Using a Cloud SQL operator to extract data to a GCS bucket
- Using GCS storage for a BigQuery operator
- Using **BigQueryOperator** for data transformation

After running the preceding task in our DAG, we will have a new **dwh_bikesharing.temporary_stations_count** table.

And with that, we will have a complete ELT process from data source to BigQuery with transformation. To chain the task dependencies, let's use the bitwise operator by writing it in our DAG Python file, as follows:

```
sql_export_task >> gcs_to_bq_example >> bq_to_bq
```

Sometimes, the Cloud SQL extract task will fail because of parallel tasks running at the same time. If you found that issue, try to rerun the failed DAG Run. Remember that you just need to click the red circle indicator, then find the **CLEAR** button. The entire DAG Run will be rerun after that.

### Things to be avoided in BigQuery DAG

In this Level 2 DAG exercise, you might already have a good understanding of how to use Airflow for BigQuery. You can use Airflow for loading, transforming, or maybe later to export BigQuery data to other storage.

Even though the code is simple and straightforward, using Python as a configuration file is very risky, in the sense that you can do literally anything in the Airflow DAG using Python.

An extreme case would be to call a **machine learning** (**ML**) library or **matplotlib** in the DAG Python file and run it in the DAG as a Python application. This doesn't make sense since it's an extreme example.

But surprisingly, I found out there are common bad practices that people do when using Python for Airflow DAG. Let's talk about that next.

#### Avoid using the BigQuery Python library

In the DAG Python file, you can import the BigQuery Python library to load data to BigQuery. Even if you can, don't. Always use the BigQuery native operators for any BigQuery actions, even though under the hood, both are using operators or using BigQuery Python clients calling the same BigQuery API. There are three main considerations that mean you should only use the operators, outlined as follows:

- Your code will be simpler, standardized, and easy to read as a configuration.
- The operators handle the BigQuery client connections for you.
- The operators will handle the logging for you.

Remember that in Airflow, we use Python for DAG configuration, not to code applications. In this case, standardization and simplicity are very important.

#### Avoid downloading data to Airflow

Using Python, you can download data from any database or storage. For our example in this exercise, you can download data from a MySQL database, GCS files, and BigQuery. For example, in the DAG Python code, if you ignore the previous recommendation, you can call the GCS client and download files.

The same thing can happen for MySQL and BigQuery. Even if you can, don't.

You don't want to download the files to Airflow workers in general. Airflow and Airflow are not storage systems. What happens if you download files in the DAG Python script is that it will download to the underlying **virtual machine** (**VM**) hard disks, which are limited, and you don't want that.

Another common example is to load a BigQuery table to a pandas DataFrame in Python. Even though it's not downloading the data to the hard-disk level, loading data to pandas means it will download the table to the workers' memories. In both scenarios, you may have a Airflow issue such as **out-of-memory or hard disk full errors** for all of your DAGs.

#### Avoid processing data in Python

Airflow is an orchestration tool. The main responsibility of an orchestration tool is to trigger jobs and let other system process the job. This is a special case of using Airflow for orchestrating big data.

What does this mean? Similar to the previous recommendation, one bad practice that might happen is to process big data in Airflow workers. For example, you might be tempted to process data from BigQuery or GCS quickly using pandas for its simplicity, and an Airflow DAG allows you to do that.

But never do that for big data. The Airflow workers won't be powerful enough to process the data volume.

In this exercise, we learned how to do a proper ELT process using GCP native operators. We've learned that every GCP service has native operators in Airflow, and for each service, there are specific operators for each task operation. For example, in BigQuery, you can use GCS to **BigQueryOperator** to load data, **BigQueryOperator** for transforming tables, and **BigQueryDelete** for deleting tables.

Using the native operators will help you simplify your DAG Python code, and on top of that, you will avoid carrying out bad practices that may happen in Airflow.

At this point, you can use the Level 2 DAG code to do any data loading to BigQuery for your needs, but we can improve the code for implementing more best practices for data loading to BigQuery. For that, we will practice Level 3 DAG.

Level 3 DAG - Parameterized variables
-------------------------------------

The main goal of the Level 3 DAG is for us to load the other tables for our bike-sharing tables. When loading more than one table, we might realize there are variables that we can parameterize to improve our DAG code. Also, in this exercise, we need to start paying more attention to the table time, since we will load trip data that has time information in it.

In addition to the DAG, we will also use JSON schema files for our BigQuery tables.

You can check the **level_3_dag.py** code to get familiar with it, but at this point, youdon't need to deploy the DAG because before continuing the practice, we will learn some fundamental concepts and Airflow features in the next section.

### Understanding types of variables in Airflow

In the Level 2 DAG exercise, we have some variables that are hardcoded in the DAG script---for example, **GCP_PROJECT_ID**, **INSTANCE_NAME**, **EXPORT_URI**, and **SQL_QUERY**.

Imagine in a scenario that you already have a pipeline running in your current Airflow project. Your infrastructure team says that you need to migrate your Airflow cluster to another project for some reason. What do you need to do?

You will need to move all the DAG code from the GCS bucket to the new project. But don't forget that because the variable is hardcoded, you need to change all the **GCP_PROJECT_ID** variables manually one by one for each script.

Are there any better ways to do that? Yes---using variables.

We have three options for declaring variables, as follows:

1. Environment variables
2. Airflow variables
3. DAG variables

DAG variables are variables that we already used, the variables that live in the DAG script, applicable only to the DAG.

The higher-level variables are Airflow variables. You can call Airflow variables from all of your DAG.

Let's create one by following these steps:

1. Go to Airflow web UI.
2. In the top menu bar, find and click **Admin** | **Variables**, as illustrated in the following screenshot:
3. In the Airflow **Variables** page, let's create a new variable by clicking the **Create** button.
4. The variable is a key-value pair. In the key, input **level_3_dag_settings**.
5. In the **Val** value, input the following:

   ```
   {"gcs_source_data_bucket":"sparsh-data-eng-on-gcp-data-bucket", "bq_raw_dataset":"raw_bikesharing", "bq_dwh_dataset":"dwh_bikesharing" }
   ```

In the example, we want to parameterize the GCS bucket name and BigQuery datasets. These variables might be helpful for other DAGs in the future, so defining these as Airflow variables is a good practice compared to DAG variables.

Notice that the value is defined as a JSON string. This is the recommendation compared to declaring each parameter as individual Airflow variables---for example, key: **bq_dwh_dataset**; value: **dwh_bikesharing**. It is not mandatory to follow this pattern, but it's better for Airflow performance. At the backend, Airflow has an internal application database. Every Airflow variable needs an independent database connection when we call it from a DAG. If we have too many variables, then we might open too many database connections for each DAG. If using the JSON, as we do in this example, we will only open one database connection for each DAG.

The last and broadest-level variables are environment variables. To set an environment variable, you can set it in the Airflow UI. Follow this step to add one:

1. Go to the **Airflow Console** webpage.
2. Choose your Airflow environment---for example, mine is **sparsh-composer-env**.
3. Find the **ENVIRONMENT VARIABLES** button and click it.
4. Click **Edit**.
5. On the **Environment variables** page, click **ADD ENVIRONMENT VARIABLE**.
6. For **Input Name**, insert **MYSQL_INSTANCE_NAME** (all in uppercase).
7. For **Input Value**, insert **mysql-instance** (your Cloud SQL instance name).
8. Click **Save**.

Wait a couple of minutes. After finishing, the environment variables will be available for you.

This way, you can adjust the variable each time you deploy a DAG.

In the next section, we will add macro variables, which are different from environment variables.

### Introducing Airflow macro variables

Airflow macro variables are variables that return information about the DAG Run. For example, you can get the execution date, DAG ID, and task ID. You can see a full list of macros in the Airflow public documentation at the following link:

[https://airflow.apache.org/docs/apache-airflow/stable/macros-ref.html](https://airflow.apache.org/docs/apache-airflow/stable/macros-ref.html)

One variable that is essential for our data pipeline is the execution date. This is a very important and useful variable that you should use to build your data pipeline.

### Loading bike-sharing tables using Airflow

After learning some new concepts, let's continue our code development. In the previous exercise, we created our tasks for loading the **stations** table. Next, we will create tasks for loading **regions** and **trips** tables.

The **regions** table will be loaded from a GCS bucket, and for the **trips** table, we will extract from the BigQuery public dataset this time. The DAG will look like this:

![B16851_04_14](https://user-images.githubusercontent.com/62965911/219851154-c7e3bc9a-3d48-4f11-9c1c-ec4d4ab9ae4c.jpg)

To load regions data from GCS, we will use **GoogleCloudStorageToGoogleCloudStorageOperator**.

For the **trips** table, the case will be a little bit non-realistic here. We will load data from GCS to BigQuery, from the public dataset to our **raw_bikesharing** dataset. In reality, we can simply use **BigQueryOperator** to load the data in a single task. But for the purpose of our practice, we will see the BigQuery public dataset as an external database. So, we will extract the table from the public dataset to the GCS bucket and load data from the GCS bucket to our BigQuery dataset. The idea is that you can reuse this pattern if the data source is not BigQuery. You can apply the same pattern to data from different databases such as **Cloud SQL**, **Oracle**, **Hadoop**, or any other data source.

After this task, you will have your **trips** data in the GCS bucket, and the rest of the steps are similar to the other tables.

The other improvement that we can do in this Level 3 DAG example is to centralize our BigQuery schema in the GCS bucket. For example, in the Level 2 DAG example, we defined **schema_fields** hardcoded in the DAG code.

In the Level 3 DAG example, the schema is loaded from JSON files.

Our sets of tasks and the preceding bitwise instructions will generate this DAG:

![B16851_04_15](https://user-images.githubusercontent.com/62965911/219851155-e40648c6-1602-46a8-b6b0-d225a76ece11.jpg)

Notice that we introduce multiple task dependencies here. For example, **dwh_fact_trips_daily** and **dwh_dim_stations** will only start when all the **gcs_to_bq** tasks are finished. This bitwise operator means that **dwh_fact_trips_daily** will only run after the three tasks in the bracket are finished.

In this exercise, we improved our DAG by utilizing variables. Variables are a very important element in Airflow. You will find using variables more and more important after creating many DAGs, tasks, and dependencies. Using variables allows you to think about automation. It's a very common practice to create DAG templates and think that you only need to change the variables, so this will be very helpful in speeding up your development time. Before continuing to our Level 4 DAG example, we need to understand the three Airflow features.

Level 4 DAG - Guaranteeing task idempotency in Airflow
------------------------------------------------------

The main goal of the Level 4 DAG is to make sure that our tasks are idempotent. More specifically, we will modify our tasks for loading **trips** tables, to make sure there will be no duplication when we rerun the DAG.

### Understanding what task idempotency means

Let's understand more about the task idempotency by way of illustration in the BigQuery table.

Let's say we have a DAG; the DAG will load an **event** table from GCS to BigQuery.

The expected start date is **2021-01-01**.

The current date is **2021-01-03**.

The schedule interval is **daily**.

In this scenario, if we use the **WRITE_APPEND** method, the files from GCS bucket directories will be loaded to BigQuery tables. For an illustration of this, check out the following diagram:

![B16851_04_19](https://user-images.githubusercontent.com/62965911/219851157-2d3f2f99-5130-4bf3-8032-473adea1294e.jpg)

Now, if the DAG needs to be rerun for **2021-02-01**, then the data loading from the date will run for a second time. The problem is that, because the method is **WRITE_APPEND**, the data from GCS will be appended to the BigQuery table, and the date will be duplicated on the second run, like this:

![B16851_04_20](https://user-images.githubusercontent.com/62965911/219851162-43a669c0-a8eb-41d3-95a4-972ac080fa0c.jpg)

The solution is using **WRITE_TRUNCATE** instead of **WRITE_APPEND** for the write disposition parameter. Using **WRITE_TRUNCATE** and changing the GCS directory source using a wildcard will load every file from the GCS bucket under the **/table/** directory to the BigQuery table, and every time there is a new DAG Run, the BigQuery table will be reloaded without duplication.

As an illustration, this diagram shows data loading from the GCS bucket using a wildcard (*****) to the BigQuery table:

![B16851_04_21](https://user-images.githubusercontent.com/62965911/219851166-25d1c69c-2ff8-491f-aca4-f06d97761103.jpg)

If you implement the **WRITE TRUNCATE** method, your task will be idempotent, which means that every time there is a rerun for any date, the data in BigQuery will always be correct without duplication. The BigQuery table won't have repeated data since the records will be reloaded on each DAG Run. But is this a best practice? The answer is: *not yet*.

This is not yet the best practice. Using this approach, you will notice that the BigQuery table will be rewritten over and over again for the whole table. If you have a table of 1 **terabyte** (**TB**) in size and the DAG already runs for 1 year, Airflow will rewrite 1 TB of data 365 times. And we don't want that---we need the BigQuery partition tables to improve this approach.

### Airflow jobs that follow task idempotency for incremental load

Please take a look at our example code and check the difference between the **level_3_dag.py** and **level_4_dag.py** files. First, we want to use the Airflow macro that returns the execution date but with no dash, like this: **20210101**. The **$** postfix followed by the date means that you are targeting a specific table partitioned to load your data. In the preceding example, you will load data to the **trips** table at the **2021-01-01** partition. Finally, in **GoogleCloudStorageToBigQueryOperator**, we will modify the parameters a little bit. We add the **time_partitioning** parameter by **DAY** on the **start_date** field.

With this, every time there is a rerun on a particular date, the table partition will be rewritten, but again, only on a specific partition date, as illustrated in the following diagram:

![B16851_04_23](https://user-images.githubusercontent.com/62965911/219851169-63481c56-7cd3-43ae-af2d-830c0d895ef4.jpg)

With this, your DAG and all tasks are idempotent. Imagine that you want to retry any tasks on any expected day---in that case, you do not need to worry. The tasks are safe to rerun and there will be no data duplication, thanks to the **WRITE_TRUNCATE** method. And also, for the **partitioned_by** date, the table will only rewrite the records on the rerun execution day.

Level 5 DAG - Handling late data using a sensor
-----------------------------------------------

The main goal of the Level 5 DAG is for us to understand how to handle late data. Handling late data means being able to create a flexible DAG runtime depending on the upstream data arrival.

In this exercise, we will use an Airflow sensor to handle the condition and learn about the **poke** mechanism in the sensor.

As the final exercise in this lab, let's add a signal and sensor to our DAG code. The idea is that we want to create a new DAG. The new DAG will write BigQuery data mart tables using data from our bike-sharing fact table. We want this DAG to run only after the fact table is successfully loaded.

Let's create a new DAG called **level_5_downstream_dag.py** for our downstream DAG. These are the steps:

1. We need an empty file for our signal---for example, this **_SUCCESS** file. This static file will be useful for later steps. So, let's copy the file to your GCS bucket. You can use the GCP console or run **gsutil** command from Cloud Shell.
2. First, we want to add a new task to **level_5_dag**. The task will put the **_SUCCESS** file in a specific directory. The task will only run if all other tasks are successfully run. So, let's add this task to **level_5_dag.** Notice that the task is actually only copying our **_SUCCESS** file from the first step, but the key is the **destination_object** parameter. The destination object directory is specifically put under **/dag name/DAG run date (extracted_date)**. This way, we can use the directory for our sensor in our next DAG.
3. Create a new Python file for our new downstream DAG. The task in the DAG will simply create a new BigQuery table from the **fact** table. Besides the preceding main task, there are two tasks that we should add to this DAG. We will follow best practice in this section, with a sensor and a signal.

The signal file from this task won't be used by any other DAG in this exercise, but that's the point of this Level 5 exercise. As a data engineer who develops with Airflow, it's a best practice to keep this as a standard. In doing this, you will always have DAGs that provide a signal for any other downstream data pipelines.

That's it---with these setups, your second DAG will start only if **level_5_dag** successfully runs. Please check the full code in the example code. Try to build a solution yourself first and compare it with the example code.

Before we summarize the lab, don't forget to delete both the Airflow and Cloud SQL instances. Both services are billed by the number of hours running, so make sure you deleted both of the instances after you've finished with the exercises. You can delete them from the GCP console with the **Delete** button, or you can run **gcloud** commands.

For Cloud SQL, delete the instance by running the following command:

`gcloud sql instances delete [CLOUDSQL INSTANCE NAME]`

Let's close this lab with a summary.

Summary
=======

In this lab, we learned about Airflow. Having learned about Airflow, we then needed to know how to work with Airflow. We realized that as an open source tool, Airflow has a wide range of features. We focused on how to use Airflow to help us build a data pipeline for our BigQuery data warehouse. There are a lot more features and capabilities in Airflow that are not covered in this book. You can always expand your skills in this area, but you will already have a good foundation after finishing this lab.

As a tool, Airflow is fairly simple. You just need to know how to write a Python script to define DAGs. We've learned in the *Level 1 DAG* exercise that you just need to write simple code to build your first DAG, but a complication arises when it comes to best practices, as there are a lot of best practices that you can follow. At the same time, there are also a lot of potential bad practices that Airflow developers can make.

By learning the examples in different code levels in this lab, you learned that DAG code decisions can lead to potential data issues, and as data engineers, it's our job to make sure we know which best practice we should apply. Every organization may have different conditions, and every condition may lead to different use cases. Understanding the potential risk and understanding Airflow's best practices are key to building the best orchestrator for your data pipelines.
