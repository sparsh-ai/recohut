# Databricks notebook source
# MAGIC %md
# MAGIC ### Learning Broadcast Joins

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

manual_schema = StructType([
  StructField('Year',IntegerType(),True),
  StructField('Month',IntegerType(),True),
  StructField('DayofMonth',IntegerType(),True),
  StructField('DayOfWeek',IntegerType(),True),
  StructField('DepTime',StringType(),True),
  StructField('CRSDepTime',IntegerType(),True),
  StructField('ArrTime',StringType(),True),
  StructField('CRSArrTime',IntegerType(),True),
  StructField('UniqueCarrier',StringType(),True),
  StructField('FlightNum',IntegerType(),True),
  StructField('TailNum',StringType(),True),
  StructField('ActualElapsedTime',StringType(),True),
  StructField('CRSElapsedTime',StringType(),True),
  StructField('AirTime',StringType(),True),
  StructField('ArrDelay',StringType(),True),
  StructField('DepDelay',StringType(),True),
  StructField('Origin',StringType(),True),
  StructField('Dest',StringType(),True),
  StructField('Distance',StringType(),True),
  StructField('TaxiIn',StringType(),True),
  StructField('TaxiOut',StringType(),True),
  StructField('Cancelled',IntegerType(),True),
  StructField('CancellationCode',StringType(),True),
  StructField('Diverted',IntegerType(),True),
  StructField('CarrierDelay',StringType(),True),
  StructField('WeatherDelay',StringType(),True),
  StructField('NASDelay',StringType(),True),
  StructField('SecurityDelay',StringType(),True),
  StructField('LateAircraftDelay',StringType(),True)
])

# COMMAND ----------

# Read csv files to create Spark dataframe
airlines_1987_to_2008 = (
  spark
  .read
  .option("header",True)
  .option("delimiter",",")
  .schema(manual_schema)
  .csv("dbfs:/databricks-datasets/asa/airlines/*")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- create lookup table
# MAGIC CREATE TABLE lookup_table(
# MAGIC iata_code STRING NOT NULL,
# MAGIC airport_name STRING NOT NULL
# MAGIC )
# MAGIC USING DELTA
# MAGIC LOCATION 'dbfs:/broadcast_joins/lookup_table'

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Insert values in lookup table
# MAGIC INSERT INTO lookup_table(iata_code,airport_name) VALUES 
# MAGIC ('ABE','Lehigh Valley International Airport'),
# MAGIC ('ABI','Abilene Regional Airport'),
# MAGIC ('ABQ','Albuquerque International Sunport'),
# MAGIC ('ABY','Southwest Georgia Regional Airport'),
# MAGIC ('ACK','Nantucket Memorial Airport'),
# MAGIC ('ACT','Waco Regional Airport'),
# MAGIC ('ACV','Arcata Airport'),
# MAGIC ('ACY','Atlantic City International Airport'),
# MAGIC ('ADQ','Kodiak Airport'),
# MAGIC ('AEX','Alexandria International Airport'),
# MAGIC ('AGS','Augusta Regional Airport'),
# MAGIC ('AKN','King Salmon Airport'),
# MAGIC ('ALB','Albany International Airport'),
# MAGIC ('ALO','Waterloo Regional Airport'),
# MAGIC ('AMA','Rick Husband Amarillo International Airport'),
# MAGIC ('ANC','Ted Stevens Anchorage International Airport'),
# MAGIC ('ANI','Aniak Airport'),
# MAGIC ('ASE','Aspen/Pitkin County Airport'),
# MAGIC ('ATL','Hartsfield–Jackson Atlanta International Airport'),
# MAGIC ('ATW','Appleton International Airport'),
# MAGIC ('AUS','Austin–Bergstrom International Airport'),
# MAGIC ('AVL','Asheville Regional Airport'),
# MAGIC ('AVP','Wilkes-Barre/Scranton International Airport'),
# MAGIC ('AZO','Kalamazoo/Battle Creek International Airport'),
# MAGIC ('BDL','Bradley International Airport'),
# MAGIC ('BET','Bethel Airport'),
# MAGIC ('BFF','Western Nebraska Regional Airport'),
# MAGIC ('BFI','King County International Airport'),
# MAGIC ('BFL','Meadows Field'),
# MAGIC ('BGM','Greater Binghamton Airport'),
# MAGIC ('BGR','Bangor International Airport'),
# MAGIC ('BHM','Birmingham–Shuttlesworth International Airport'),
# MAGIC ('BIL','Billings Logan International Airport'),
# MAGIC ('BIS','Bismarck Municipal Airport'),
# MAGIC ('BJI','Bemidji Regional Airport'),
# MAGIC ('BLI','Bellingham International Airport'),
# MAGIC ('BMI','Central Illinois Regional Airport at Bloomington-Normal'),
# MAGIC ('BNA','Nashville International Airport'),
# MAGIC ('BOI','Boise Airport'),
# MAGIC ('BOS','Gen. Edward Lawrence Logan International Airport'),
# MAGIC ('BPT','Jack Brooks Regional Airport'),
# MAGIC ('BQK','Brunswick Golden Isles Airport'),
# MAGIC ('BQN','Rafael Hernández International Airport'),
# MAGIC ('BRO','Brownsville/South Padre Island International Airport'),
# MAGIC ('BRW','Wiley Post–Will Rogers Memorial Airport'),
# MAGIC ('BTM','Bert Mooney Airport'),
# MAGIC ('BTR','Baton Rouge Metropolitan Airport'),
# MAGIC ('BTV','Burlington International Airport'),
# MAGIC ('BUF','Buffalo Niagara International Airport'),
# MAGIC ('BUR','Hollywood Burbank Airport'),
# MAGIC ('BWI','Baltimore/Washington International Airport'),
# MAGIC ('BZN','Bozeman Yellowstone International Airport'),
# MAGIC ('CAE','Columbia Metropolitan Airport'),
# MAGIC ('CAK','Akron–Canton Airport'),
# MAGIC ('CCR','Buchanan Field Airport'),
# MAGIC ('CDC','Cedar City Regional Airport'),
# MAGIC ('CDV','Merle K. (Mudhole) Smith Airport'),
# MAGIC ('CHA','Chattanooga Metropolitan Airport'),
# MAGIC ('CHO','Charlottesville–Albemarle Airport'),
# MAGIC ('CHS','Charleston International Airport'),
# MAGIC ('CID','The Eastern Iowa Airport'),
# MAGIC ('CKB','North Central West Virginia Airport'),
# MAGIC ('CLE','Cleveland Hopkins International Airport'),
# MAGIC ('CLL','Easterwood Airport'),
# MAGIC ('CLT','Charlotte Douglas International Airport'),
# MAGIC ('CMH','John Glenn Columbus International Airport'),
# MAGIC ('CMI','University of Illinois - Willard Airport'),
# MAGIC ('CMX','Houghton County Memorial Airport'),
# MAGIC ('COD','Yellowstone Regional Airport'),
# MAGIC ('COS','City of Colorado Springs Municipal Airport'),
# MAGIC ('CPR','Casper–Natrona County International Airport'),
# MAGIC ('CRP','Corpus Christi International Airport'),
# MAGIC ('CRW','Yeager Airport'),
# MAGIC ('CSG','Columbus Airport'),
# MAGIC ('CVG','Cincinnati/Northern Kentucky International Airport'),
# MAGIC ('CWA','Central Wisconsin Airport'),
# MAGIC ('DAB','Daytona Beach International Airport'),
# MAGIC ('DAL','Dallas Love Field'),
# MAGIC ('DAY','James M. Cox Dayton International Airport'),
# MAGIC ('DBQ','Dubuque Regional Airport'),
# MAGIC ('DCA','Ronald Reagan Washington National Airport'),
# MAGIC ('DEN','Denver International Airport'),
# MAGIC ('DFW','Dallas/Fort Worth International Airport'),
# MAGIC ('DHN','Dothan Regional Airport'),
# MAGIC ('DLG','Dillingham Airport'),
# MAGIC ('DLH','Duluth International Airport'),
# MAGIC ('DRO','Durango–La Plata County Airport'),
# MAGIC ('DSM','Des Moines International Airport'),
# MAGIC ('DTW','Detroit Metropolitan Wayne County Airport'),
# MAGIC ('DUT','Unalaska Airport'),
# MAGIC ('EAU','Chippewa Valley Regional Airport'),
# MAGIC ('EGE','Eagle County Regional Airport'),
# MAGIC ('EKO','Elko Regional Airport'),
# MAGIC ('ELM','Elmira/Corning Regional Airport'),
# MAGIC ('ELP','El Paso International Airport'),
# MAGIC ('ERI','Erie International Airport'),
# MAGIC ('EUG','Eugene Airport'),
# MAGIC ('EVV','Evansville Regional Airport'),
# MAGIC ('EWN','Coastal Carolina Regional Airport'),
# MAGIC ('EWR','Newark Liberty International Airport'),
# MAGIC ('EYW','Key West International Airport'),
# MAGIC ('FAI','Fairbanks International Airport'),
# MAGIC ('FAR','Hector International Airport'),
# MAGIC ('FAT','Fresno Yosemite International Airport'),
# MAGIC ('FAY','Fayetteville Regional Airport'),
# MAGIC ('FCA','Glacier Park International Airport'),
# MAGIC ('FLG','Flagstaff Pulliam Airport'),
# MAGIC ('FLL','Fort Lauderdale–Hollywood International Airport'),
# MAGIC ('FLO','Florence Regional Airport'),
# MAGIC ('FNT','Bishop International Airport'),
# MAGIC ('FSD','Sioux Falls Regional Airport'),
# MAGIC ('FSM','Fort Smith Regional Airport'),
# MAGIC ('FWA','Fort Wayne International Airport'),
# MAGIC ('GCC','Gillette–Campbell County Airport'),
# MAGIC ('GCN','Grand Canyon National Park Airport'),
# MAGIC ('GEG','Spokane International Airport'),
# MAGIC ('GFK','Grand Forks International Airport'),
# MAGIC ('GGG','East Texas Regional Airport'),
# MAGIC ('GJT','Grand Junction Regional Airport'),
# MAGIC ('GNV','Gainesville Regional Airport'),
# MAGIC ('GPT','Gulfport–Biloxi International Airport'),
# MAGIC ('GRB','Green Bay–Austin Straubel International Airport'),
# MAGIC ('GRK','Killeen–Fort Hood Regional Airport'),
# MAGIC ('GRR','Gerald R. Ford International Airport'),
# MAGIC ('GSO','Piedmont Triad International Airport'),
# MAGIC ('GSP','Greenville–Spartanburg International Airport'),
# MAGIC ('GST','Gustavus Airport'),
# MAGIC ('GTF','Great Falls International Airport'),
# MAGIC ('GTR','Golden Triangle Regional Airport'),
# MAGIC ('GUC','Gunnison–Crested Butte Regional Airport'),
# MAGIC ('GUM','Antonio B. Won Pat International Airport'),
# MAGIC ('HDN','Yampa Valley Airport'),
# MAGIC ('HHH','Hilton Head Airport'),
# MAGIC ('HLN','Helena Regional Airport'),
# MAGIC ('HNL','Daniel K. Inouye International Airport'),
# MAGIC ('HOU','William P. Hobby Airport'),
# MAGIC ('HPN','Westchester County Airport'),
# MAGIC ('HRL','Valley International Airport'),
# MAGIC ('HSV','Huntsville International Airport (Carl T. Jones Field)'),
# MAGIC ('HTS','Tri-State Airport'),
# MAGIC ('HVN','Tweed-New Haven Airport'),
# MAGIC ('IAD','Washington Dulles International Airport'),
# MAGIC ('IAH','George Bush Intercontinental Airport'),
# MAGIC ('ICT','Wichita Dwight D. Eisenhower National Airport'),
# MAGIC ('IDA','Idaho Falls Regional Airport'),
# MAGIC ('ILM','Wilmington International Airport'),
# MAGIC ('IND','Indianapolis International Airport'),
# MAGIC ('INL','Falls International Airport'),
# MAGIC ('ISP','Long Island MacArthur Airport'),
# MAGIC ('ITH','Ithaca Tompkins International Airport'),
# MAGIC ('ITO','Hilo International Airport'),
# MAGIC ('JAC','Jackson Hole Airport'),
# MAGIC ('JAN','Jackson–Medgar Wiley Evers International Airport'),
# MAGIC ('JAX','Jacksonville International Airport'),
# MAGIC ('JFK','John F. Kennedy International Airport'),
# MAGIC ('JNU','Juneau International Airport'),
# MAGIC ('KOA','Ellison Onizuka Kona International Airport at Keahole'),
# MAGIC ('KSM','St. Marys Airport'),
# MAGIC ('KTN','Ketchikan International Airport'),
# MAGIC ('LAN','Capital Region International Airport'),
# MAGIC ('LAS','McCarran International Airport'),
# MAGIC ('LAW','Lawton–Fort Sill Regional Airport'),
# MAGIC ('LAX','Los Angeles International Airport'),
# MAGIC ('LBB','Lubbock Preston Smith International Airport'),
# MAGIC ('LCH','Lake Charles Regional Airport'),
# MAGIC ('LEX','Blue Grass Airport'),
# MAGIC ('LFT','Lafayette Regional Airport'),
# MAGIC ('LGA','LaGuardia Airport'),
# MAGIC ('LGB','Long Beach Airport'),
# MAGIC ('LIH','Lihue Airport'),
# MAGIC ('LIT','Clinton National Airport'),
# MAGIC ('LNK','Lincoln Airport'),
# MAGIC ('LNY','Lanai Airport'),
# MAGIC ('LRD','Laredo International Airport'),
# MAGIC ('LSE','La Crosse Regional Airport'),
# MAGIC ('LWB','Greenbrier Valley Airport'),
# MAGIC ('LWS','Lewiston–Nez Perce County Airport'),
# MAGIC ('LYH','Lynchburg Regional Airport'),
# MAGIC ('MAF','Midland International Air and Space Port'),
# MAGIC ('MBS','MBS International Airport'),
# MAGIC ('MCI','Kansas City International Airport'),
# MAGIC ('MCN','Middle Georgia Regional Airport'),
# MAGIC ('MCO','Orlando International Airport'),
# MAGIC ('MDT','Harrisburg International Airport'),
# MAGIC ('MDW','Chicago Midway International Airport'),
# MAGIC ('MEI','Meridian Regional Airport'),
# MAGIC ('MEM','Memphis International Airport'),
# MAGIC ('MFE','McAllen Miller International Airport'),
# MAGIC ('MFR','Rogue Valley International–Medford Airport'),
# MAGIC ('MGM','Montgomery Regional Airport (Dannelly Field)'),
# MAGIC ('MHT','Manchester–Boston Regional Airport'),
# MAGIC ('MIA','Miami International Airport'),
# MAGIC ('MKE','Milwaukee Mitchell International Airport'),
# MAGIC ('MKG','Muskegon County Airport'),
# MAGIC ('MKK','Molokai Airport'),
# MAGIC ('MLB','Melbourne Orlando International Airport'),
# MAGIC ('MLI','Quad City International Airport'),
# MAGIC ('MLU','Monroe Regional Airport'),
# MAGIC ('MOB','Mobile Regional Airport'),
# MAGIC ('MOT','Minot International Airport'),
# MAGIC ('MQT','Sawyer International Airport'),
# MAGIC ('MRY','Monterey Regional Airport'),
# MAGIC ('MSN','Dane County Regional Airport'),
# MAGIC ('MSO','Missoula International Airport'),
# MAGIC ('MSP','Minneapolis–St. Paul International Airport'),
# MAGIC ('MSY','Louis Armstrong New Orleans International Airport'),
# MAGIC ('MTJ','Montrose Regional Airport'),
# MAGIC ('MYR','Myrtle Beach International Airport'),
# MAGIC ('OAJ','Albert J. Ellis Airport'),
# MAGIC ('OAK','Oakland International Airport'),
# MAGIC ('OGD','Ogden-Hinckley Airport'),
# MAGIC ('OGG','Kahului Airport'),
# MAGIC ('OKC','Will Rogers World Airport'),
# MAGIC ('OMA','Eppley Airfield'),
# MAGIC ('OME','Nome Airport'),
# MAGIC ('ONT','Ontario International Airport'),
# MAGIC ('ORD','Chicago OHare International Airport'),
# MAGIC ('ORF','Norfolk International Airport'),
# MAGIC ('ORH','Worcester Regional Airport'),
# MAGIC ('OTH','Southwest Oregon Regional Airport'),
# MAGIC ('OTZ','Ralph Wien Memorial Airport'),
# MAGIC ('PBI','Palm Beach International Airport'),
# MAGIC ('PDX','Portland International Airport'),
# MAGIC ('PHF','Newport News/Williamsburg International Airport'),
# MAGIC ('PHL','Philadelphia International Airport'),
# MAGIC ('PHX','Phoenix Sky Harbor International Airport'),
# MAGIC ('PIA','General Downing-Peoria International Airport'),
# MAGIC ('PIE','St. Pete–Clearwater International Airport'),
# MAGIC ('PIH','Pocatello Regional Airport'),
# MAGIC ('PIR','Pierre Regional Airport'),
# MAGIC ('PIT','Pittsburgh International Airport'),
# MAGIC ('PLN','Pellston Regional Airport'),
# MAGIC ('PNS','Pensacola International Airport'),
# MAGIC ('PSC','Tri-Cities Airport'),
# MAGIC ('PSE','Mercedita International Airport'),
# MAGIC ('PSG','Petersburg James A. Johnson Airport'),
# MAGIC ('PSP','Palm Springs International Airport'),
# MAGIC ('PUB','Pueblo Memorial Airport'),
# MAGIC ('PVD','Rhode Island T. F. Green International Airport'),
# MAGIC ('PVU','Provo Municipal Airport'),
# MAGIC ('PWM','Portland International Jetport'),
# MAGIC ('RAP','Rapid City Regional Airport'),
# MAGIC ('RDD','Redding Municipal Airport'),
# MAGIC ('RDM','Redmond Municipal Airport'),
# MAGIC ('RDU','Raleigh–Durham International Airport'),
# MAGIC ('RFD','Chicago Rockford International Airport'),
# MAGIC ('RHI','Rhinelander–Oneida County Airport'),
# MAGIC ('RIC','Richmond International Airport'),
# MAGIC ('RKS','Southwest Wyoming Regional Airport'),
# MAGIC ('RNO','Reno/Tahoe International Airport'),
# MAGIC ('ROA','Roanoke–Blacksburg Regional Airport'),
# MAGIC ('ROC','Greater Rochester International Airport'),
# MAGIC ('ROP','Rota International Airport'),
# MAGIC ('ROW','Roswell International Air Center'),
# MAGIC ('RST','Rochester International Airport'),
# MAGIC ('RSW','Southwest Florida International Airport'),
# MAGIC ('SAN','San Diego International Airport'),
# MAGIC ('SAT','San Antonio International Airport'),
# MAGIC ('SAV','Savannah/Hilton Head International Airport'),
# MAGIC ('SBA','Santa Barbara Municipal Airport'),
# MAGIC ('SBN','South Bend International Airport'),
# MAGIC ('SBP','San Luis Obispo County Regional Airport'),
# MAGIC ('SCC','Deadhorse Airport (Prudhoe Bay Airport)'),
# MAGIC ('SCE','University Park Airport'),
# MAGIC ('SCK','Stockton Metropolitan Airport'),
# MAGIC ('SDF','Louisville International Airport'),
# MAGIC ('SEA','Seattle–Tacoma International Airport'),
# MAGIC ('SFO','San Francisco International Airport'),
# MAGIC ('SGF','Springfield–Branson National Airport'),
# MAGIC ('SGU','St. George Regional Airport'),
# MAGIC ('SHV','Shreveport Regional Airport'),
# MAGIC ('SIT','Sitka Rocky Gutierrez Airport'),
# MAGIC ('SJC','Norman Y. Mineta San José International Airport'),
# MAGIC ('SJT','San Angelo Regional Airport'),
# MAGIC ('SJU','Luis Muñoz Marín International Airport'),
# MAGIC ('SLC','Salt Lake City International Airport'),
# MAGIC ('SMF','Sacramento International Airport'),
# MAGIC ('SMX','Santa Maria Public Airport'),
# MAGIC ('SNA','John Wayne Airport'),
# MAGIC ('SPI','Abraham Lincoln Capital Airport'),
# MAGIC ('SPN','Saipan International Airport'),
# MAGIC ('SPS','Wichita Falls Regional Airport'),
# MAGIC ('SRQ','Sarasota–Bradenton International Airport'),
# MAGIC ('STL','St. Louis Lambert International Airport'),
# MAGIC ('STT','Cyril E. King Airport'),
# MAGIC ('STX','Henry E. Rohlsen Airport'),
# MAGIC ('SUN','Friedman Memorial Airport'),
# MAGIC ('SUX','Sioux Gateway Airport'),
# MAGIC ('SWF','Stewart International Airport'),
# MAGIC ('SYR','Syracuse Hancock International Airport'),
# MAGIC ('TLH','Tallahassee International Airport'),
# MAGIC ('TOL','Toledo Express Airport'),
# MAGIC ('TPA','Tampa International Airport'),
# MAGIC ('TRI','Tri-Cities Regional Airport'),
# MAGIC ('TTN','Trenton Mercer Airport'),
# MAGIC ('TUL','Tulsa International Airport'),
# MAGIC ('TUP','Tupelo Regional Airport'),
# MAGIC ('TUS','Tucson International Airport'),
# MAGIC ('TVC','Cherry Capital Airport'),
# MAGIC ('TWF','Magic Valley Regional Airport'),
# MAGIC ('TXK','Texarkana Regional Airport'),
# MAGIC ('TYR','Tyler Pounds Regional Airport'),
# MAGIC ('TYS','McGhee Tyson Airport'),
# MAGIC ('VLD','Valdosta Regional Airport'),
# MAGIC ('VPS','Destin–Fort Walton Beach Airport'),
# MAGIC ('WRG','Wrangell Airport'),
# MAGIC ('WYS','Yellowstone Airport'),
# MAGIC ('XNA','Northwest Arkansas National Airport'),
# MAGIC ('YAK','Yakutat Airport'),
# MAGIC ('YKM','Yakima Air Terminal'),
# MAGIC ('YUM','Yuma International Airport')

# COMMAND ----------

# Standard Join
lookup_table = spark.table("lookup_table")

standard_join = (airlines_1987_to_2008
                 .join(lookup_table,airlines_1987_to_2008.Origin == lookup_table.iata_code,"inner")
                 .drop('Origin')
                )

standard_join.write.format('delta').mode('overwrite').save('dbfs:/broadcast_joins/standard_join')

# COMMAND ----------

# Broadcast Join
lookup_table = spark.table("lookup_table")

broadcast_join = (airlines_1987_to_2008
                 .join(broadcast(lookup_table),airlines_1987_to_2008.Origin == lookup_table.iata_code,"inner")
                 .drop('Origin')
                )

broadcast_join.write.format('delta').mode('overwrite').save('dbfs:/broadcast_joins/broadcast_join')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Learning Apache Arrow in Pandas

# COMMAND ----------

import numpy as np
import pandas as pd

spark.conf.set("spark.sql.execution.arrow.enabled", "true")

# COMMAND ----------

pdf = pd.DataFrame(np.random.rand(1000, 3))

# COMMAND ----------

df = spark.createDataFrame(pdf)
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Understanding Shuffle Partitions

# COMMAND ----------

spark.conf.get('spark.sql.shuffle.partitions')

# COMMAND ----------

spark.conf.set('spark.sql.shuffle.partitions',8)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Understanding Caching in Spark

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

manual_schema = StructType([
  StructField('Year',IntegerType(),True),
  StructField('Month',IntegerType(),True),
  StructField('DayofMonth',IntegerType(),True),
  StructField('DayOfWeek',IntegerType(),True),
  StructField('DepTime',StringType(),True),
  StructField('CRSDepTime',IntegerType(),True),
  StructField('ArrTime',StringType(),True),
  StructField('CRSArrTime',IntegerType(),True),
  StructField('UniqueCarrier',StringType(),True),
  StructField('FlightNum',IntegerType(),True),
  StructField('TailNum',StringType(),True),
  StructField('ActualElapsedTime',StringType(),True),
  StructField('CRSElapsedTime',StringType(),True),
  StructField('AirTime',StringType(),True),
  StructField('ArrDelay',StringType(),True),
  StructField('DepDelay',StringType(),True),
  StructField('Origin',StringType(),True),
  StructField('Dest',StringType(),True),
  StructField('Distance',StringType(),True),
  StructField('TaxiIn',StringType(),True),
  StructField('TaxiOut',StringType(),True),
  StructField('Cancelled',IntegerType(),True),
  StructField('CancellationCode',StringType(),True),
  StructField('Diverted',IntegerType(),True),
  StructField('CarrierDelay',StringType(),True),
  StructField('WeatherDelay',StringType(),True),
  StructField('NASDelay',StringType(),True),
  StructField('SecurityDelay',StringType(),True),
  StructField('LateAircraftDelay',StringType(),True)
])

# COMMAND ----------

# Read csv files to create Spark dataframe
airlines_1987_to_2008 = (
  spark
  .read
  .option("header",True)
  .option("delimiter",",")
  .schema(manual_schema)
  .csv("dbfs:/databricks-datasets/asa/airlines/*")
)

# COMMAND ----------

# Display the dataframe
display(airlines_1987_to_2008
        .groupBy(col("Year"))
        .count()
        .orderBy(col('count').desc())
       )

# COMMAND ----------

# Caching the dataframe and returning count
airlines_1987_to_2008.cache().count()

# COMMAND ----------

# Display the dataframe after caching
display(airlines_1987_to_2008
        .groupBy(col("Year"))
        .count()
        .orderBy(col('count').desc())
       )

# COMMAND ----------

# Un-cache the dataframe
airlines_1987_to_2008.unpersist()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adaptive Query Execution

# COMMAND ----------

spark.conf.set('spark.sql.adaptive.enabled','true')

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create "items" table.
# MAGIC 
# MAGIC CREATE TABLE items
# MAGIC USING delta
# MAGIC AS
# MAGIC SELECT id AS item_sku,
# MAGIC CAST(rand() * 1000 AS INT) AS price
# MAGIC FROM RANGE(30000000);

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create "sales" table with skew.
# MAGIC -- Item with id 200 is in 80% of all sales.
# MAGIC 
# MAGIC CREATE TABLE sales
# MAGIC USING delta
# MAGIC AS
# MAGIC SELECT CASE WHEN rand() < 0.8 THEN 200 ELSE CAST(rand() * 30000000 AS INT) END AS item_sku,
# MAGIC CAST(rand() * 100 AS INT) AS quantity,
# MAGIC DATE_ADD(current_date(), - CAST(rand() * 360 AS INT)) AS date
# MAGIC FROM RANGE(1000000000);

# COMMAND ----------

# MAGIC %sql SELECT * FROM items

# COMMAND ----------

# MAGIC %sql SELECT * FROM sales

# COMMAND ----------

# MAGIC %md
# MAGIC **Dynamically coalescing shuffle partitions**

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT date, sum(quantity) AS total_quantity
# MAGIC FROM sales
# MAGIC GROUP BY date
# MAGIC ORDER BY total_quantity DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Here, we are trying to query the total sales grouped by date. Next, we can open the Associated SQL Query diagram of the query in the Spark UI. You can find this option in the SQL section of the Spark UI. If we expand the Exchange box, we can see that the partitions after aggregation are very small in size (roughly 13 KB on average):
# MAGIC   
# MAGIC ![B17782_07_04](https://user-images.githubusercontent.com/62965911/218821170-99f81149-a25a-4152-af69-7ac920b5bef3.jpeg)
# MAGIC 
# MAGIC AQE automatically identified the small partitions and has coalesced those numerous small partitions into one large partition. This is confirmed by the CustomShuffleReader box. In the following screenshot, we can see that the number of partitions equals 1. This is the result of coalescing several small partitions into one single partition so that we have only one task and therefore a lower load on Spark's task scheduler.
# MAGIC 
# MAGIC ![B17782_07_05](https://user-images.githubusercontent.com/62965911/218821378-7a131d79-6c33-4923-9c5a-7c8620928d39.jpeg)

# COMMAND ----------

# MAGIC %md 
# MAGIC **Dynamically switching join strategies**

# COMMAND ----------

# MAGIC %sql
# MAGIC EXPLAIN FORMATTED
# MAGIC SELECT date, sum(quantity * price) AS total_sales
# MAGIC FROM sales AS s
# MAGIC JOIN items AS i ON s.item_sku = i.item_sku
# MAGIC WHERE price < 10
# MAGIC GROUP BY date
# MAGIC ORDER BY total_sales DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC We can clearly note in the Physical Plan that Spark intends to perform a sort-merge join. In this kind of join strategy, Spark sorts both the datasets and then performs an inner join between them. It is considered to be a computationally expensive join operation.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT date, sum(quantity * price) AS total_sales
# MAGIC FROM sales AS s
# MAGIC JOIN items AS i ON s.item_sku = i.item_sku
# MAGIC WHERE price < 10
# MAGIC GROUP BY date
# MAGIC ORDER BY total_sales DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Let's take a look at the executed query's Associated SQL Query diagram in the Spark UI. We can clearly see that Spark has changed the join strategy at runtime. From a sort-merge join, it has dynamically switched to a broadcast hash join.
# MAGIC 
# MAGIC ![B17782_07_06](https://user-images.githubusercontent.com/62965911/218821671-3041b912-e3ee-4385-88fc-778e64f162df.jpeg)

# COMMAND ----------

# MAGIC %md
# MAGIC **Dynamically optimizing skew joins**

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT date, sum(quantity * price) AS total_sales
# MAGIC FROM sales AS s
# MAGIC JOIN items AS i ON s.item_sku = i.item_sku
# MAGIC GROUP BY date
# MAGIC ORDER BY total_sales DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Now, let's check the Associated SQL Query diagram of the query in the Spark UI. This will help us understand exactly what happened under the hood:
# MAGIC 
# MAGIC ![B17782_07_07](https://user-images.githubusercontent.com/62965911/218821856-41ba5a0b-07f2-428c-81a8-9eab3129bb6a.jpeg)
# MAGIC 
# MAGIC Here, we can see that one partition is skewed (the item with an item_sku value of 200) in the CustomShuffleReader box. This single skewed partition is further split into 26 different partitions, due to AQE.
# MAGIC 
# MAGIC This brings us to the end of the section on AQE. As we can see, AQE is a highly beneficial Spark optimization technique that helps to speed up queries at query runtime. And in most of the latest Databricks Runtime (DBR) versions, it comes enabled by default.
