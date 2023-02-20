from pyspark.sql.functions import dayofweek, hour

weekend_zeros = df.filter((hour("Time (Local)") >= 17) | (hour("Time (Local)") < 3)).filter((dayofweek("Date") == 6) | (dayofweek("Date") == 7)).agg(sum("Zeroes").alias("weekend_zeros")).collect()[0]["weekend_zeros"]

total_zeros = df.agg(sum("Zeroes").alias("total_zeros")).collect()[0]["total_zeros"]

percent_weekend_zeros = weekend_zeros / total_zeros * 100

print("The percentage of zeros that occurred on weekends is:", percent_weekend_zeros, "%")

#The percentage of zeros that occurred on weekends is: 41.333414829040026 %
