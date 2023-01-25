import sys
from pyspark.sql import SparkSession


if len(sys.argv) == 1:
   print('no arguments passed')
   sys.exit()


spark = SparkSession\
        .builder\
        .appName("hudi_cow_upsert")\
        .getOrCreate()


# General Constants
OUTPUT_BUCKET="s3://"+sys.argv[1]+"/hudi/hudi_trips_cow"
HUDI_FORMAT = "org.apache.hudi"
TABLE_NAME = "hoodie.table.name"
RECORDKEY_FIELD_OPT_KEY = "hoodie.datasource.write.recordkey.field"
PRECOMBINE_FIELD_OPT_KEY = "hoodie.datasource.write.precombine.field"
OPERATION_OPT_KEY = "hoodie.datasource.write.operation"
BULK_INSERT_OPERATION_OPT_VAL = "bulk_insert"
UPSERT_OPERATION_OPT_VAL = "upsert"
DELETE_OPERATION_OPT_VAL = "delete"
BULK_INSERT_PARALLELISM = "hoodie.bulkinsert.shuffle.parallelism"
UPSERT_PARALLELISM = "hoodie.upsert.shuffle.parallelism"
S3_CONSISTENCY_CHECK = "hoodie.consistency.check.enabled"
HUDI_CLEANER_POLICY = "hoodie.cleaner.policy"
KEEP_LATEST_COMMITS = "KEEP_LATEST_COMMITS"
KEEP_LATEST_FILE_VERSIONS = "KEEP_LATEST_FILE_VERSIONS"
HUDI_COMMITS_RETAINED = "hoodie.cleaner.commits.retained"
HUDI_FILES_RETAINED = "hoodie.cleaner.fileversions.retained"
PAYLOAD_CLASS_OPT_KEY = "hoodie.datasource.write.payload.class.key()"
EMPTY_PAYLOAD_CLASS_OPT_VAL = "org.apache.hudi.EmptyHoodieRecordPayload"

# Hive Constants
HIVE_SYNC_ENABLED_OPT_KEY="hoodie.datasource.hive_sync.enable"
HIVE_PARTITION_FIELDS_OPT_KEY="hoodie.datasource.hive_sync.partition_fields"
HIVE_ASSUME_DATE_PARTITION_OPT_KEY="hoodie.datasource.hive_sync.assume_date_partitioning"
HIVE_PARTITION_EXTRACTOR_CLASS_OPT_KEY="hoodie.datasource.hive_sync.partition_extractor_class"
HIVE_TABLE_OPT_KEY="hoodie.datasource.hive_sync.table"

# Partition Constants
NONPARTITION_EXTRACTOR_CLASS_OPT_VAL="org.apache.hudi.hive.NonPartitionedExtractor"
MULTIPART_KEYS_EXTRACTOR_CLASS_OPT_VAL="org.apache.hudi.hive.MultiPartKeysValueExtractor"
KEYGENERATOR_CLASS_OPT_KEY="hoodie.datasource.write.keygenerator.class"
NONPARTITIONED_KEYGENERATOR_CLASS_OPT_VAL="org.apache.hudi.keygen.NonpartitionedKeyGenerator"
COMPLEX_KEYGENERATOR_CLASS_OPT_VAL="org.apache.hudi.ComplexKeyGenerator"
PARTITIONPATH_FIELD_OPT_KEY="hoodie.datasource.write.partitionpath.field"

#Incremental Constants
VIEW_TYPE_OPT_KEY="hoodie.datasource.query.type"
BEGIN_INSTANTTIME_OPT_KEY="hoodie.datasource.read.begin.instanttime"
VIEW_TYPE_INCREMENTAL_OPT_VAL="incremental"
END_INSTANTTIME_OPT_KEY="hoodie.datasource.read.end.instanttime"

#Bootstrap Constants
BOOTSTRAP_BASE_PATH_PROP="hoodie.bootstrap.base.path"
BOOTSTRAP_KEYGEN_CLASS="hoodie.bootstrap.keygen.class"


## Generates Data

from datetime import datetime

def get_json_data(start, count, dest):
    time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = [{"trip_id": i, "tstamp": time_stamp, "route_id": chr(65 + (i % 10)), "destination": dest[i%10]} for i in range(start, start + count)]
    return data

# Creates the Dataframe
def create_json_df(spark, data):
    sc = spark.sparkContext
    return spark.read.json(sc.parallelize(data))



 ## CHANGE ME ##
config = {
    "table_name": "hudi_trips_cow",
    "primary_key": "trip_id",
    "sort_key": "tstamp"
}


upsert_dest = ["Boston", "Boston", "Boston", "Boston", "Boston","Boston","Boston","Boston","Boston","Boston"]
df = create_json_df(spark, get_json_data(1000000, 10, upsert_dest))


(df.write.format(HUDI_FORMAT)
      .option(PRECOMBINE_FIELD_OPT_KEY, config["sort_key"])
      .option(RECORDKEY_FIELD_OPT_KEY, config["primary_key"])
      .option(TABLE_NAME, config['table_name'])
      .option(OPERATION_OPT_KEY, UPSERT_OPERATION_OPT_VAL)
      .option("hoodie.cleaner.commits.retained",2)
      .option(UPSERT_PARALLELISM, 10)
      .option(HIVE_TABLE_OPT_KEY,config['table_name'])
      .option(HIVE_SYNC_ENABLED_OPT_KEY,"true")
      .mode("Append")
      .save(OUTPUT_BUCKET))



