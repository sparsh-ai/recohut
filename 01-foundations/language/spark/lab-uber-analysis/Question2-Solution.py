from pyspark.sql.functions import sum, window

# Read the data from CSV file
uber = spark.read.csv("uber.csv", header=True, inferSchema=True)

# Group the data by 24-hour windows and sum the completed trips
completed_trips_by_window = uber \
    .groupBy(window("Time (Local)", "24 hours")) \
    .agg(sum("Completed Trips").alias("Total Completed Trips")) \
    .orderBy("Total Completed Trips", ascending=False)

# Get the highest number of completed trips within a 24-hour period
highest_completed_trips_in_24_hours = completed_trips_by_window \
    .select("Total Completed Trips") \
    .first()["Total Completed Trips"]

print(highest_completed_trips_in_24_hours)

#Output 2102
