import sys
import boto3
from datetime import datetime
from awsglue.transforms import *
from delta.tables import *
from pyspark.sql.functions import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job


sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'raw_s3_path', 'stage_s3_path',
                          'processed_s3_bucket_name', 'processed_s3_prefix'])

# Parameters
cdc_date = datetime.now().strftime("%d/%m/%Y")
raw_s3_path = args['raw_s3_path']
stage_s3_path = args['stage_s3_path']
processed_s3_bucket_name = args['processed_s3_bucket_name']
processed_s3_prefix = args['processed_s3_prefix']
processed_s3_path = f"s3://{processed_s3_bucket_name}/{processed_s3_prefix}"


def s3_object_cnt(bucket_name, prefix):
    """
    This function will return object count in specified s3 prefix.
    """
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)
    count = bucket.objects.filter(Prefix=prefix)
    cnt = len(list(count))
    print(f'objects count in {bucket_name} and {prefix} prefix is {cnt} ')
    return cnt


def add_emp_key(df):
    """
    This function will genrate hash key using sha2 and adds new column emp_key to dataframe.
    """
    return df.withColumn("emp_key", sha2(concat_ws("||", col("emp_id"), col("first_name"), col("last_name"), col("Address"), col("phone_number"), col("isContractor")), 256))


def create_deltalake_tbl(df, s3_path):
    """
    This function will write dataframe to S3 in deltalake format.
    """
    df.write.format("delta").mode("append").save(s3_path)


def create_stage_deltalake_tbl(df, s3_path):
    """
    This function will overwrites exsiting data in s3 prefix and write dataframe to S3 in deltalake format.
    """
    df.write.format("delta").mode("overwrite").option(
        "mergeSchema", "true").save(s3_path)
    return DeltaTable.forPath(spark, s3_path)


def employee_capture_changes(stage_tbl, base_tbl):
    """
    This function will identify chnages between source data and target deltalake dataset.

    """
    # join base and stage tables to identify updates
    updates_df = stage_tbl.toDF().alias("stage")\
        .join(base_tbl.alias("base"), "emp_id", "left")\
        .filter((col('base.emp_key').isNull()) | (col('base.emp_key') != col('stage.emp_key')))

    cols = ['emp_id', 'first_name', 'last_name', 'Address',
            'phone_number', 'isContractor', 'emp_key', 'delete_flag']
    stage_updates = updates_df.select(
        'stage.*').withColumn("delete_flag", lit(False)).select(*cols)
    base_updates = updates_df.select('base.*').drop('isCurrent', 'start_date', 'end_date').select(*cols)

    # perform union
    union_updates = base_updates.union(
        stage_updates).filter(col('emp_key').isNotNull())

    # identify deleted records
    base_tbl.alias('base').join(
        stage_tbl.toDF().alias('stage'), 'emp_id', 'anti')

    drop_del_cols = ['delete_flag', 'start_date', 'end_date', 'isCurrent']
    del_df = base_tbl.alias('base')\
        .join(stage_tbl.toDF().alias('stage'), 'emp_id', 'anti')\
        .drop(*drop_del_cols)\
        .withColumn("merge_delete_flag", lit(True))\
        .withColumnRenamed('merge_delete_flag', 'delete_flag')

    union_updates_dels = union_updates.union(del_df)

    return union_updates_dels


def employee_delta_records(base_tbl, union_updates_dels):
    """
    This function will identify delete records and sets delete_flag to true and updates end_date.
    """
    delete_join_cond = "employee.emp_id=employeeUpdates.emp_id and employee.emp_key = employeeUpdates.emp_key"
    delete_cond = "employee.emp_key == employeeUpdates.emp_key and employee.isCurrent = true and employeeUpdates.delete_flag = true"

    base_tbl.alias("employee").merge(union_updates_dels.alias("employeeUpdates"), delete_join_cond).whenMatchedUpdate(
        condition=delete_cond, set={"isCurrent": "false", "end_date": current_date(), "delete_flag": "true"}).execute()


def employee_upsert_records(base_tbl, union_updates_dels):
    """
    This function will identify insert/update records and performs merge operation on exsiting deltalake dataset.
    """
    upsert_cond = "employee.emp_id=employeeUpdates.emp_id and employee.emp_key = employeeUpdates.emp_key and employee.isCurrent = true"
    upsert_update_cond = "employee.isCurrent = true and employeeUpdates.delete_flag = false"

    base_tbl.alias("employee").merge(union_updates_dels.alias("employeeUpdates"), upsert_cond).whenMatchedUpdate(condition=upsert_update_cond, set={"isCurrent": "false", "end_date": current_date()}).whenNotMatchedInsert(
        values={"isCurrent": "true", "emp_id": "employeeUpdates.emp_id", "first_name": "employeeUpdates.first_name", "last_name": "employeeUpdates.last_name", "Address": "employeeUpdates.Address", "phone_number": "employeeUpdates.phone_number",
                "isContractor": "employeeUpdates.isContractor", "emp_key": "employeeUpdates.emp_key", "start_date": current_date(), "delete_flag":  "employeeUpdates.delete_flag", "end_date": "null"}).execute()


def employees_scd(raw_s3_path, stage_s3_path, processed_s3_path):
    """
    This function will perform scd type 2 on deltalake dataset on s3 for employees sample dataset. 
    """
    srcDyf = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={
                                                           "paths": [raw_s3_path], "recurse": True, }, transformation_ctx="srcDyf")

    srcDF = add_emp_key(srcDyf.toDF())

    if s3_object_cnt(processed_s3_bucket_name, processed_s3_prefix) != 0:
        print(f'Deltalake employees data already exists. started loading data ...')

        # delta lake satge table for input data source.
        stage_tbl = create_stage_deltalake_tbl(srcDF, stage_s3_path)

        # read delta lake base table for current records
        base_tbl = DeltaTable.forPath(spark, processed_s3_path)

        base_tbl_df = base_tbl.toDF().where((col('isCurrent') == "true")
                                            & (col('delete_flag') == "false"))

        union_updates_dels = employee_capture_changes(stage_tbl, base_tbl_df)

        # perform soft deletes
        employee_delta_records(base_tbl, union_updates_dels)

        # refresh base table and perform merge operation
        base_tbl = DeltaTable.forPath(spark, processed_s3_path)

        employee_upsert_records(base_tbl, union_updates_dels)

    else:
        print(f'Delta lake employees data  dosent exists. Performing inital data load ...')

        srcDF = srcDF.withColumn("start_date", current_date()).withColumn("end_date", lit(None).cast(
            StringType())).withColumn("isCurrent", lit(True)).withColumn("delete_flag", lit(False))

        create_deltalake_tbl(srcDF, processed_s3_path)


employees_scd(raw_s3_path, stage_s3_path, processed_s3_path)
