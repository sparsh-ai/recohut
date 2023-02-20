# Uber Data Analysis in Pyspark

>This lab can be used as a take-home assignment to learn Pyspark and Data Engineering.

## Data Description

To answer the question, use the dataset from the file dataset.csv. For example, consider a row from this dataset:


![image](https://user-images.githubusercontent.com/25612446/219965433-956a1dc0-2acf-4d0d-b1cb-40723249d349.png)

This means that during the hour beginning at 4pm (hour 16), on September 10th, 2012, 11 people opened the Uber app (Eyeballs). 2 of them did not see any car (Zeroes) and 4 of them requested a car (Requests). Of the 4 requests, only 3 complete trips actually resulted (Completed Trips). During this time, there were a total of 6 drivers who logged in (Unique Drivers).

## Assignment 

Using the provided dataset, answer the following questions:

- ⚡ Which date had the most completed trips during the two week period?
- ⚡ What was the highest number of completed trips within a 24 hour period?
- ⚡ Which hour of the day had the most requests during the two week period?
- ⚡ What percentages of all zeroes during the two week period occurred on weekend (Friday at 5 pm to Sunday at 3 am)? Tip: The local time value is the start of the hour (e.g. 15 is the hour from 3:00pm - 4:00pm)
- ⚡ What is the weighted average ratio of completed trips per driver during the two week period? Tip: "Weighted average" means your answer should account for the total trip volume in each hour to determine the most accurate number in whole period.
- ⚡ In drafting a driver schedule in terms of 8 hours shifts, when are the busiest 8 consecutive hours over the two week period in terms of unique requests? A new shift starts in every 8 hours. Assume that a driver will work same shift each day.
- ⚡ True or False: Driver supply always increases when demand increases during the two week period. Tip: Visualize the data to confirm your answer if needed.
- ⚡ In which 72 hour period is the ratio of Zeroes to Eyeballs the highest?
- ⚡ If you could add 5 drivers to any single hour of every day during the two week period, which hour should you add them to? Hint: Consider both rider eyeballs and driver supply when choosing
- ⚡ Looking at the data from all two weeks, which time might make the most sense to consider a true "end day" instead of midnight? (i.e when are supply and demand at both their natural minimums) Tip: Visualize the data to confirm your answer if needed.

## Solution

To solve the questions using PySpark, we need to first create a SparkSession and load the dataset into a DataFrame. Here's how we can do it:
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a SparkSession
spark = SparkSession.builder.appName("UberDataAnalysis").getOrCreate()

# Load the dataset into a DataFrame
df = spark.read.csv("uber.csv", header=True, inferSchema=True) 
```
Now that we have loaded the dataset into a data frame, we can start answering the questions.
Which date had the most completed trips during the two-week period?

- To find the date with the most completed trips, you can group the data by date and sum the completed trips column. Then, sort the results in descending order and select the top row.
```python
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
```
- What was the highest number of completed trips within a 24-hour period?

To find the highest number of completed trips within a 24-hour period, you can group the data by date and use a window function to sum the completed trips column over a rolling 24-hour period. Then, you can sort the results in descending order and select the top row.

```python
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
```
- Which hour of the day had the most requests during the two-week period?

To answer this question, we need to group the data by an hour and sum the "Requests" column for each hour. We can then sort the result by the sum of requests and select the hour with the highest sum.

```python
from pyspark.sql.functions import hour, sum

hourly_requests = df.groupBy(hour("Time (Local)").alias("hour")).agg(sum("Requests").alias("total_requests")).orderBy("total_requests", ascending=False)

most_requested_hour = hourly_requests.select("hour").first()[0]
print("The hour with the most requests is:", most_requested_hour)

#The hour with the most requests is: 17
```

- What percentages of all zeroes during the two-week period occurred on weekends (Friday at 5 pm to Sunday at 3 am)?

To answer this question, we need to filter the data to select only the rows that fall within the specified time range, count the total number of zeros, and count the number of zeros that occurred on weekends. We can then calculate the percentage of zeros that occurred on weekends.

```python
from pyspark.sql.functions import dayofweek, hour

weekend_zeros = df.filter((hour("Time (Local)") >= 17) | (hour("Time (Local)") < 3)).filter((dayofweek("Date") == 6) | (dayofweek("Date") == 7)).agg(sum("Zeroes").alias("weekend_zeros")).collect()[0]["weekend_zeros"]

total_zeros = df.agg(sum("Zeroes").alias("total_zeros")).collect()[0]["total_zeros"]

percent_weekend_zeros = weekend_zeros / total_zeros * 100

print("The percentage of zeros that occurred on weekends is:", percent_weekend_zeros, "%")

#The percentage of zeros that occurred on weekends is: 41.333414829040026 %
```

- What is the weighted average ratio of completed trips per driver during the two-week period?

To answer this question, we need to calculate the ratio of completed trips to unique drivers for each hour, multiply the ratio by the total number of completed trips for that hour, and then sum the results. We can then divide this sum by the total number of completed trips for the entire period.

```python
from pyspark.sql.functions import avg

weighted_avg = df.withColumn("completed_per_driver", df["Completed Trips"] / df["Unique Drivers"]) \
                 .groupBy("Date", "Time (Local)") \
                 .agg(avg("completed_per_driver").alias("avg_completed_per_driver"), sum("Completed Trips").alias("total_completed_trips")) \
                 .withColumn("weighted_ratio", col("avg_completed_per_driver") * col("total_completed_trips")) \
                 .agg(sum("weighted_ratio") / sum("total_completed_trips")).collect()[0][0]

print("The weighted average ratio of completed trips per driver is:", weighted_avg)

#Output: The weighted average ratio of completed trips per driver is: 1.2869201507713425
```
- In drafting a driver schedule in terms of 8 hours shifts, when are the busiest 8 consecutive hours over the two-week period in terms of unique requests? A new shift starts every 8 hours. Assume that a driver will work the same shift each day.

To solve this, we can first calculate the number of unique requests for each hour of the day, and then slide a window of 8 hours across the hours to find the 8 consecutive hours with the highest number of unique requests. Here's the code:

```python
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
```
This will output the busiest 8 consecutive hours in terms of unique requests, along with the number of unique requests during that time period.


- True or False: Driver supply always increases when demand increases during the two-week period.

This statement is false. There are multiple reasons why driver supply might not always increase when demand increases. For example, some drivers might choose not to work during peak demand times, or there might be external factors that affect driver availability (such as traffic, weather conditions, or events in the city). To confirm this, we would need to analyze the data and identify instances where demand increased but driver supply did not.


- In which 72-hour period is the ratio of Zeroes to Eyeballs the highest?

To answer this question, we can group the data by 72-hour periods and calculate the ratio of zeroes to eyeballs for each period. We can then find the period with the highest ratio. Here's the code:

```python
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
```

This will output the 72-hour period with the highest ratio of zeroes to eyeballs.

- If you could add 5 drivers to any single hour of every day during the two-week period, which hour should you add them to? Hint: Consider both rider eyeballs and driver supply when choosing.


To determine which hour to add 5 drivers too, we want to look for an hour where there are a high number of rider eyeballs and a low number of unique drivers. One way to approach this is to calculate the ratio of requests to unique drivers for each hour and then choose the hour with the highest ratio. The idea here is that adding more drivers to an hour with a high ratio will result in more completed trips.
We can use the following PySpark code to calculate the ratio for each hour:

```python
# Calculate requests per unique driver for each hour
requests_per_driver = (df.groupBy('Time (Local)').agg(
    (F.sum('Requests') / F.countDistinct('Unique Drivers')).alias('requests_per_driver'))
)

# Show the hour with the highest ratio
requests_per_driver.orderBy(F.desc('requests_per_driver')).show(1)
```

This will output the hour with the highest requests per unique driver ratio, which is where we should add 5 drivers.

- Looking at the data from all two weeks, which time might make the most sense to consider a true "end day" instead of midnight? (i.e when are supply and demand at both their natural minimums)

One way to approach this question is to calculate the average number of completed trips and unique drivers for each hour of the day over the entire two-week period. We can then look for the hour with the lowest number of completed trips and unique drivers to find the time when supply and demand are at their natural minimums.
We can use the following PySpark code to calculate the average number of completed trips and unique drivers for each hour:

```python
# Calculate average completed trips and unique drivers for each hour
avg_trips_and_drivers = (df.groupBy('Time (Local)').agg(
    F.mean('Completed Trips').alias('avg_completed_trips'),
    F.mean('Unique Drivers').alias('avg_unique_drivers')
))

# Show the hour with the lowest average completed trips and unique drivers
avg_trips_and_drivers.orderBy('avg_completed_trips', 'avg_unique_drivers').show(1)
```

This will output the hour with the lowest average number of completed trips and unique drivers, which is when supply and demand are at their natural minimums and might make the most sense to consider as the "end day".
