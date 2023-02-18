from awsglue import DynamicFrame
import pyspark.sql.functions as F

def repartition_date(self, dateCol, partitionCols="", numPartitionsExpected=None):
    partition_list = partitionCols.split(",") if partitionCols else []
    partition_list += ["year", "month", "day"]

    date_col = F.col(dateCol)
    df = self.toDF()\
      .withColumn("year", F.year(date_col).cast("string"))\
      .withColumn("month", F.format_string("%02d", F.month(date_col)))\
      .withColumn("day", F.format_string("%02d", F.dayofmonth(date_col)))

    if not numPartitionsExpected:
        numPartitionsExpected = df.selectExpr(f"COUNT(DISTINCT {','.join(partition_list)})").collect()[0][0]

    # Reorganize the data so the partitions in memory are aligned when the file partitioning on s3
    # So each partition has the data for a combination of partition column values
    df = df.repartition(numPartitionsExpected, partition_list)
    return DynamicFrame.fromDF(df, self.glue_ctx, self.name)

DynamicFrame.repartition_date = repartition_date