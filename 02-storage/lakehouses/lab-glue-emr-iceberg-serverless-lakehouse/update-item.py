from pyspark.sql import SparkSession

from pyspark.sql.functions import col, lit, when, concat



spark = SparkSession \
        .builder \
        .config("hive.metastore.client.factory.class", "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory") \
        .enableHiveSupport() \
        .getOrCreate()    


#Variables 
DB_NAME = "datalake"
TPC_DS_DATABASE = "tpc-source"
TABLE_NAME_ITEM = "item_iceberg"

input_data =  spark.sql(f"""
    SELECT *
    FROM `{TPC_DS_DATABASE}`.item
    WHERE i_current_price > 90.0;
    ;"""
)

#Create a batch of update and insert records
temp_data = input_data.withColumn("i_brand",when(col("i_brand").like("corpnameless%"), "Unknown") \
                                            .otherwise(col("i_brand")))

update_data = temp_data.withColumn("i_item_id", when(temp_data.i_brand != "Unknown",(concat(col("i_item_id"), lit("N"))))\
                                                .otherwise(col("i_item_id")))


# update table with the batch of new inserts and updated records
update_data.createOrReplaceTempView("item_records")

spark.sql(f"""
    MERGE INTO dev.`{DB_NAME}`.`{TABLE_NAME_ITEM}` item
    USING item_records changed
        ON item.i_item_id = changed.i_item_id
    WHEN MATCHED THEN UPDATE SET item.i_brand = changed.i_brand
    WHEN NOT MATCHED THEN INSERT *
""")
