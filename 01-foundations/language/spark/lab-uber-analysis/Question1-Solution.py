from pyspark.sql.functions import max

# Read the data from CSV file
uber = spark.read.csv("uber.csv", header=True, inferSchema=True)

# Group the data by date and sum the completed trips
completed_trips_by_date = uber.groupBy("Date").sum("Completed Trips")

# Find the date with the most completed trips
date_with_most_completed_trips = completed_trips_by_date \
    .orderBy("sum(Completed Trips)", ascending=False) \
    .select("Date") \
    .first()["Date"]

print(date_with_most_completed_trips)

#Output:  2012-09-15
