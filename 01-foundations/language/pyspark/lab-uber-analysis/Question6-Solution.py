from pyspark.sql.functions import col, hour, countDistinct
from pyspark.sql.window import Window

# Calculate the number of unique requests for each hour of the day
hourly_unique_requests = (df
  .groupBy(hour("Time (Local)").alias("hour"))
  .agg(countDistinct("Requests").alias("unique_requests"))
)

# Slide a window of 8 hours to find the busiest 8 consecutive hours
window = Window.orderBy(col("unique_requests").desc()).rowsBetween(0, 7)
busiest_8_consecutive_hours = (hourly_unique_requests
  .select("*", sum("unique_requests").over(window).alias("consecutive_sum"))
  .orderBy(col("consecutive_sum").desc())
  .limit(1)
)

# Print the result
busiest_8_consecutive_hours.show()
