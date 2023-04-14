# Calculate average completed trips and unique drivers for each hour
avg_trips_and_drivers = (df.groupBy('Time (Local)').agg(
    F.mean('Completed Trips').alias('avg_completed_trips'),
    F.mean('Unique Drivers').alias('avg_unique_drivers')
))

# Show the hour with the lowest average completed trips and unique drivers
avg_trips_and_drivers.orderBy('avg_completed_trips', 'avg_unique_drivers').show(1)
