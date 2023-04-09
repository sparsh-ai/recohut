from pyspark.sql.functions import avg

weighted_avg = df.withColumn("completed_per_driver", df["Completed Trips"] / df["Unique Drivers"]) \
                 .groupBy("Date", "Time (Local)") \
                 .agg(avg("completed_per_driver").alias("avg_completed_per_driver"), sum("Completed Trips").alias("total_completed_trips")) \
                 .withColumn("weighted_ratio", col("avg_completed_per_driver") * col("total_completed_trips")) \
                 .agg(sum("weighted_ratio") / sum("total_completed_trips")).collect()[0][0]

print("The weighted average ratio of completed trips per driver is:", weighted_avg)

#Output: The weighted average ratio of completed trips per driver is: 1.2869201507713425
