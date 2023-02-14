from pyspark.sql import SparkSession
# import pandas as pd

spark = SparkSession.builder.appName("uber-date-trips-sql").getOrCreate()

directory = "/Users/keon/fastcampus/data-engineering/01-spark/data"
filename = "fhvhv_tripdata_2020-03.csv"
taxi_zone_lookup = "taxi+_zone_lookup.csv"

taxi_data = spark.read.csv(f"file:///{directory}/{filename}", inferSchema = True, header = True)
taxi_zone_lookup = spark.read.csv(f"file:///{directory}/{taxi_zone_lookup}", inferSchema = True, header = True)


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

taxi_data.createOrReplaceTempView("taxi_data")
taxi_zone_lookup.createOrReplaceTempView("taxi_zone")
# spark.sql("SELECT pickup_datetime FROM mobility_data LIMIT 5").show()

# spark.sql("SELECT * FROM taxi_zone").show()
# +----------+-------------+--------------------+------------+                    
# |LocationID|      Borough|                Zone|service_zone|
# +----------+-------------+--------------------+------------+
# |         1|          EWR|      Newark Airport|         EWR|
# |         2|       Queens|         Jamaica Bay|   Boro Zone|
# |         3|        Bronx|Allerton/Pelham G...|   Boro Zone|
# |         4|    Manhattan|       Alphabet City| Yellow Zone|
# |         5|Staten Island|       Arden Heights|   Boro Zone|

# spark.sql("SELECT * FROM taxi_data join taxi_zone on taxi_data.PULocationID = taxi_zone.LocationID where taxi_zone.Borough = 'Manhattan'").show()
# +-----------------+--------------------+-------------------+-------------------+------------+------------+-------+----------+---------+--------------------+------------+
# |hvfhs_license_num|dispatching_base_num|    pickup_datetime|   dropoff_datetime|PULocationID|DOLocationID|SR_Flag|LocationID|  Borough|                Zone|service_zone|
# +-----------------+--------------------+-------------------+-------------------+------------+------------+-------+----------+---------+--------------------+------------+
# |           HV0003|              B02869|2020-03-01 00:50:32|2020-03-01 01:15:27|         230|         243|   null|       230|Manhattan|Times Sq/Theatre ...| Yellow Zone|
# |           HV0003|              B02882|2020-03-01 00:29:13|2020-03-01 00:54:47|         230|           7|      1|       230|Manhattan|Times Sq/Theatre ...| Yellow Zone|
# |           HV0003|              B02835|2020-03-01 00:22:40|2020-03-01 00:38:55|         230|         226|   null|       230|Manhattan|Times Sq/Theatre ...| Yellow Zone|
# |           HV0003|              B02617|2020-03-01 00:09:07|2020-03-01 00:39:03|         230|         218|   null|       230|Manhattan|Times Sq/Theatre ...| Yellow Zone|

spark.sql("SELECT taxi_zone.Zone, count(*) as trips FROM taxi_data join taxi_zone on taxi_data.PULocationID = taxi_zone.LocationID group by taxi_zone.Zone").show()
# +--------------------+------+
# |                Zone| trips|
# +--------------------+------+
# |           Homecrest| 42106|
# |              Corona| 43104|
# |    Bensonhurst West| 46127|
# |         Westerleigh|  9080|
# |          Douglaston|  6841|
# |Charleston/Totten...|  4274|
# |      Newark Airport|   362|
# |      Pelham Parkway| 46436|
# |East Concourse/Co...| 95510|