# Tickets ETL with Glue Studio

You can use AWS Glue Studio to create jobs that extract structured or semi-structured data from a data source, perform a transformation of that data, and save the result set in a data target.

In this lab, you will create a job in AWS Glue Studio using Amazon S3 as the Source and Target. By completing these steps, you will learn how visual jobs are created and how to edit nodes, the component building blocks in the visual job editor.

You will learn how to:

- Configure the data source node to a data source. In this lab, you will set the data source to Amazon S3.
- Apply and edit a transform node. In this lab, you will apply the ApplyMapping transform to the job.
- Configure the data target node. In this lab, you will set the data target to Amazon S3.
- View and edit the job script.
- Run the job and view run details for the job.

## Steps

### Step 1: Setup the lab environment with Cloudformation template

To launch the stack, we will use aws cli command:

```sh
aws cloudformation create-stack \
	--stack-name GlueETLTickets \
	--template-body file://stack.yaml \
	--capabilities CAPABILITY_NAMED_IAM
```

This stack will create the 4 resources - Glue Database, Glue Table, S3 Bucket and IAM Role.

### Step 2: Create the Glue ETL Job

Refer to the `etl.py` script to create the job in Glue ETL Studio. Feel free to use visual editor to design the job flow and configuration. In this script, make sure to change the account number in target S3 path.

Once you create the job and save it, run the job and wait untils it gets completed. It generally takes less than 2 minutes to complete.

After the job completes, check the target s3 path. There should be files in that path.

### Step 3: Add the table in Glue Catalog

Once the data is available in the target S3 path, we will register the data as table in the glue catalog. For this, one option could be to send the glue crawler to the s3 path and it will fetch the result. Other option is to manually add the table by using the commands in AWS Athena. Refer `athena.sql` script.

You will see a new table added in the glue database. Now run the following query to validate that the transformed data is successfully loaded in the glue table:

```sql
SELECT * FROM tickets_transformd_new LIMIT 10;
```