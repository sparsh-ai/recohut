# Calculate requests per unique driver for each hour
requests_per_driver = (df.groupBy('Time (Local)').agg(
    (F.sum('Requests') / F.countDistinct('Unique Drivers')).alias('requests_per_driver'))
)

# Show the hour with the highest ratio
requests_per_driver.orderBy(F.desc('requests_per_driver')).show(1)
