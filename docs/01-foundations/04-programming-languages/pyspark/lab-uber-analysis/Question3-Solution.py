from pyspark.sql.functions import hour, sum

hourly_requests = df.groupBy(hour("Time (Local)").alias("hour")).agg(sum("Requests").alias("total_requests")).orderBy("total_requests", ascending=False)

most_requested_hour = hourly_requests.select("hour").first()[0]
print("The hour with the most requests is:", most_requested_hour)

#The hour with the most requests is: 17
