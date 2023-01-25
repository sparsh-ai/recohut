from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.master("local").appName("create-dataframe").getOrCreate()


stocks = [('Google', 'GOOGL', 'USA', 2984, 'USD'), 
 ('Netflix', 'NFLX', 'USA', 645, 'USD'),
 ('Amazon', 'AMZN', 'USA', 3518, 'USD'),
 ('Tesla', 'TSLA', 'USA', 1222, 'USD'),
 ('Samsung', '005930', 'Korea', 70600, 'KRW'),
 ('Kakao', '035720', 'Korea', 125000, 'KRW')]

schema = ["name", "ticker", "country", "price", "currency"]
df = spark.createDataFrame(data=stocks, schema=schema)

df.show()
# +-------+------+-------+------+--------+                                        
# |   name|ticker|country| price|currency|
# +-------+------+-------+------+--------+
# | Google| GOOGL|    USA|  2984|     USD|
# |Netflix|  NFLX|    USA|   645|     USD|
# | Amazon|  AMZN|    USA|  3518|     USD|
# |  Tesla|  TSLA|    USA|  1222|     USD|
# |Samsung|005930|  Korea| 70600|     KRW|
# |  Kakao|035720|  Korea|125000|     KRW|
# +-------+------+-------+------+--------+

usaStocksDF = df.select("name", "country", "price").where("country == 'USA'").orderBy("price")
usaStocksDF.show()
# +-------+-------+-----+
# |   name|country|price|
# +-------+-------+-----+
# |Netflix|    USA|  645|
# |  Tesla|    USA| 1222|
# | Google|    USA| 2984|
# | Amazon|    USA| 3518|
# +-------+-------+-----+

df.groupBy("currency").max("price").show()
# +--------+----------+
# |currency|max(price)|
# +--------+----------+
# |     KRW|    125000|
# |     USD|      3518|
# +--------+----------+

from pyspark.sql.functions import avg, count
df.groupBy("currency").agg(avg("price")).show()
# +--------+----------+
# |currency|avg(price)|
# +--------+----------+
# |     KRW|   97800.0|
# |     USD|   2092.25|
# +--------+----------+
df.groupBy("currency").agg(count("price")).show()
# +--------+------------+
# |currency|count(price)|
# +--------+------------+
# |     KRW|           2|
# |     USD|           4|
# +--------+------------+