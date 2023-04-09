CREATE EXTERNAL TABLE if not exists `nytaxitrip`(
  `vendorid` bigint, 
  `tpep_pickup_datetime` string, 
  `tpep_dropoff_datetime` string, 
  `passenger_count` bigint, 
  `trip_distance` double, 
  `ratecodeid` bigint, 
  `store_and_fwd_flag` string, 
  `pulocationid` bigint, 
  `dolocationid` bigint, 
  `payment_type` bigint, 
  `fare_amount` double, 
  `extra` double, 
  `mta_tax` double, 
  `tip_amount` double, 
  `tolls_amount` double, 
  `improvement_surcharge` double, 
  `total_amount` double, 
  `congestion_surcharge` string)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
's3://wysde-datasets/tripdata/'; 