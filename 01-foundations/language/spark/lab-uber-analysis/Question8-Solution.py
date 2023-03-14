from pyspark.sql.functions import col, sum

# Group the data by 72-hour periods and calculate the ratio of zeroes to eyeballs for each period
period_ratios = (df
  .groupBy(((col("Date").cast("timestamp").cast("long") / (72*3600)).cast("int")).alias("period"))
  .agg(sum("Zeroes").alias("zeroes"), sum("Eyeballs").alias("eyeballs"))
  .withColumn("ratio", col("zeroes") / col("eyeballs"))
)

# Find the period with the highest ratio
highest_ratio_period = period_ratios.orderBy(col("ratio").desc()).limit(1)

# Print the result
highest_ratio_period.show()
