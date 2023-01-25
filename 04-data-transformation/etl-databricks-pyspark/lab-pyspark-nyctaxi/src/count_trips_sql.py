from pyspark.sql import SparkSession
# import pandas as pd

spark = SparkSession.builder.appName("uber-date-trips-sql").getOrCreate()

directory = "/Users/keon/fastcampus/data-engineering/01-spark/data"
filename = "fhvhv_tripdata_2020-03.csv"

data = spark.read.csv(f"file:///{directory}/{filename}", inferSchema = True, header = True)


# data.show(5)
# +-----------------+--------------------+-------------------+-------------------+------------+------------+-------+
# |hvfhs_license_num|dispatching_base_num|    pickup_datetime|   dropoff_datetime|PULocationID|DOLocationID|SR_Flag|
# +-----------------+--------------------+-------------------+-------------------+------------+------------+-------+
# |           HV0005|              B02510|2020-03-01 00:03:40|2020-03-01 00:23:39|          81|         159|   null|
# |           HV0005|              B02510|2020-03-01 00:28:05|2020-03-01 00:38:57|         168|         119|   null|
# |           HV0003|              B02764|2020-03-01 00:03:07|2020-03-01 00:15:04|         137|         209|      1|
# |           HV0003|              B02764|2020-03-01 00:18:42|2020-03-01 00:38:42|         209|          80|   null|
# |           HV0003|              B02764|2020-03-01 00:44:24|2020-03-01 00:58:44|         256|         226|   null|
# +-----------------+--------------------+-------------------+-------------------+------------+------------+-------+

data.createOrReplaceTempView("mobility_data")
# spark.sql("SELECT pickup_datetime FROM mobility_data LIMIT 5").show()
# +-------------------+                                                           
# |    pickup_datetime|
# +-------------------+
# |2020-03-01 00:03:40|
# |2020-03-01 00:28:05|
# |2020-03-01 00:03:07|
# |2020-03-01 00:18:42|
# |2020-03-01 00:44:24|
# +-------------------+

# data.show()
# +-----------------+--------------------+-------------------+-------------------+------------+------------+-------+
# |hvfhs_license_num|dispatching_base_num|    pickup_datetime|   dropoff_datetime|PULocationID|DOLocationID|SR_Flag|
# +-----------------+--------------------+-------------------+-------------------+------------+------------+-------+
# |           HV0005|              B02510|2020-03-01 00:03:40|2020-03-01 00:23:39|          81|         159|   null|
# |           HV0005|              B02510|2020-03-01 00:28:05|2020-03-01 00:38:57|         168|         119|   null|
# |           HV0003|              B02764|2020-03-01 00:03:07|2020-03-01 00:15:04|         137|         209|      1|
# |           HV0003|              B02764|2020-03-01 00:18:42|2020-03-01 00:38:42|         209|          80|   null|
# |           HV0003|              B02764|2020-03-01 00:44:24|2020-03-01 00:58:44|         256|         226|   null|
# |           HV0003|              B02682|2020-03-01 00:17:23|2020-03-01 00:39:35|          79|         263|   null|
# |           HV0003|              B02764|2020-03-01 00:01:18|2020-03-01 00:38:52|          61|          29|   null|
# |           HV0003|              B02764|2020-03-01 00:43:27|2020-03-01 00:47:27|         150|         150|      1|

spark.sql("select pickup_date, count(*) from (SELECT split(pickup_datetime,' ')[0] as pickup_date FROM mobility_data) group by pickup_date").show()


# SELECT split(pickup_datetime,' ')[0] as pickup_date FROM mobility_data
# +--------------------------------+                                              
# |split(pickup_datetime,  , -1)[0]|
# +--------------------------------+
# |                      2020-03-01|
# |                      2020-03-01|
# |                      2020-03-01|
# |                      2020-03-01|
# |                      2020-03-01|
# select pickup_date, count(*) from (SELECT split(pickup_datetime,' ')[0] as pickup_date FROM mobility_data) group by pickup_date
# +-----------+--------+                                                          
# |pickup_date|count(1)|
# +-----------+--------+
# | 2020-03-02|  648986|
# | 2020-03-01|  784246|
# | 2020-03-03|  697880|
# | 2020-03-04|  707879|
# | 2020-03-05|  731165|
# | 2020-03-06|  872012|

# data.printSchema()
# root
#  |-- hvfhs_license_num: string (nullable = true)
#  |-- dispatching_base_num: string (nullable = true)
#  |-- pickup_datetime: string (nullable = true)
#  |-- dropoff_datetime: string (nullable = true)
#  |-- PULocationID: integer (nullable = true)
#  |-- DOLocationID: integer (nullable = true)
#  |-- SR_Flag: integer (nullable = true)

# [('hvfhs_license_num', 'string'), 
#  ('dispatching_base_num', 'string'),
#  ('pickup_datetime', 'string'),
#  ('dropoff_datetime', 'string'),
#  ('PULocationID', 'int'),
#  ('DOLocationID', 'int'),
#  ('SR_Flag', 'int')]

# data.select("pickup_datetime")


# #####
# rdd = sc.parallelize([2, 3, 4], 4)
# rdd.reduce(lambda x, y: x*y)
# # 24
# rdd.fold(1, lambda x, y: x*y)
# # 24

# rdd.reduce(lambda x, y: x+y)
# # 9
# rdd.fold(1, lambda x, y: x+y)
# # 14

# rdd.fold(0, lambda x, y: x*y)
# # 0