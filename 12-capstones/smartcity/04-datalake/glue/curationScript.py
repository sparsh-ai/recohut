import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job    

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
logger = glueContext.get_logger()
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

## database = "swipebike", table_name = "rides"
ds_rides = glueContext.create_dynamic_frame.from_catalog(database = "swipebike", table_name = "rides", transformation_ctx = "ds_rides")

## print the structure of rides 
#ds_rides.printSchema()

## relationalize RIDES so that bikedetail struct<> ends up being its own table
relationalized = Relationalize.apply(frame = ds_rides, staging_path = args["TempDir"], name = "rides", transformation_ctx = "relationalized")

## write the relationalized files to S3 - in this case keep them in JSON format just as an example 
relationalize_datasink = glueContext.write_dynamic_frame.from_options(frame = relationalized, connection_type = "s3", connection_options = {"path": "s3://{YOUR-S3-BUCKET}/curated/rides-relationalized"}, format = "json", transformation_ctx = "relationalize_datasink")

## database = "swipebike", table_name = "stations"
ds_stations = glueContext.create_dynamic_frame.from_catalog(database = "swipebike", table_name = "stations", transformation_ctx = "ds_stations")

## remove not needed columns from ds_rides and ds_stations
ds_station_min = ds_stations.drop_fields(['latitude','longitude']).rename_field('stationid', 'station-st-id')
ds_station_min = ds_station_min.resolveChoice(specs = [('station-st-id','cast:long')])

ds_rides_min =  ds_rides.drop_fields(['tripDuration', 'partition_0', 'partition_1', 'partition_2', 'partition_3','bikeDetail.bikeNum', 'bikeDetail.bikeAttributes.attribName', 'bikeDetail.bikeAttributes.attribValue']).rename_field('stationId', 'ride-st-id')

ds_station_min.printSchema()
ds_rides_min.printSchema()


ds_joined = Join.apply(ds_station_min, ds_rides_min, 'station-st-id', 'ride-st-id')
#logger.info("Count:", ds_joined.count())


glueContext.write_dynamic_frame.from_options(frame = ds_joined,
          connection_type = "s3",
          connection_options = {"path": "s3://{YOUR-S3-BUCKET}/curated/stationincome"},
          format = "parquet")
          
logger.info("Finishing the job")
## commit the job
job.commit()
