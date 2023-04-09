from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col, trim
from pyspark.sql.types import IntegerType, FloatType

import os


#loading the file in a dataframe
crimeDF = spark.read.csv("./data/crime_dataset.csv", header=True)

"""
Analysis
---------
- District has null values. We don't want null values, hence we can replace null with "unknown" so as to maintain data integrity
- Some fields are empty, not even designated as "null". To fill them with NA or 0
- Last column "location" is redundant since latitude and longitude columns are already present
"""

#fill fields with null values with "unknown"
crimeDF1= crimeDF.fillna({
    "DISTRICT":"Unknown"
})

crimeDF1= crimeDF.fillna({
    "SHOOTING":"Unknown",
    "INCIDENT_NUMBER":"Unknown",
    "OFFENSE_CODE_GROUP":"Unknown",
    "OFFENSE_DESCRIPTION":"Unknown",
    "DAY_OF_WEEK":"Unknown",
    "UCR_PART":"Unknown",
    "STREET":"Unknown"
})

# replacing nulls in numeric columns with sentinel values to indicate absence of data
crimeDF1 = crimeDF1.withColumn("OFFENSE_CODE", when(col("OFFENSE_CODE").isNull(), -1).otherwise(col("OFFENSE_CODE")))
#crimeDF1 = crimeDF1.withColumn("REPORTING_AREA", when(col("REPORTING_AREA").isNull(), -1).otherwise(col("REPORTING_AREA")))
crimeDF1 = crimeDF1.withColumn("OCCURRED_ON_DATE", when(col("OCCURRED_ON_DATE").isNull(), "9999-12-31 23:59:59").otherwise(col("OCCURRED_ON_DATE")))
crimeDF1 = crimeDF1.withColumn("YEAR", when(col("YEAR").isNull(), 9999).otherwise(col("YEAR")))
crimeDF1 = crimeDF1.withColumn("MONTH", when(col("MONTH").isNull(), -1).otherwise(col("MONTH")))
crimeDF1 = crimeDF1.withColumn("HOUR", when(col("HOUR").isNull(), -1).otherwise(col("HOUR")))
crimeDF1 = crimeDF1.withColumn("Lat", when(col("Lat").isNull(), -999).otherwise(col("Lat")))
crimeDF1 = crimeDF1.withColumn("Long", when(col("Long").isNull(), -999).otherwise(col("Long")))

crimeDF1= crimeDF1.fillna({
    "DISTRICT":"Unknown",
})

#some fields are empty, not even designated as "null". To fill them with NA or 0
crimeDF1 = crimeDF1.withColumn("REPORTING_AREA", when(trim(col("REPORTING_AREA")) == "", -999).otherwise(col("REPORTING_AREA")))

#last column "location" is redundant since latitude and longitude columns are already present
crimeDF2 = crimeDF1.drop("Location")

#transforming string datatypes wherever necessary and storing them to new dataframe DF3
crimeDF3 = crimeDF2.withColumn("OFFENSE_CODE",crimeDF2["OFFENSE_CODE"].cast(IntegerType())).withColumn("REPORTING_AREA", crimeDF2["REPORTING_AREA"].cast(FloatType())).withColumn("YEAR", crimeDF2["YEAR"].cast(IntegerType())).withColumn("MONTH", crimeDF2["MONTH"].cast(IntegerType())).withColumn("HOUR", crimeDF2["HOUR"].cast(IntegerType())).withColumn("Lat", crimeDF2["Lat"].cast(FloatType())).withColumn("Long", crimeDF2["Long"].cast(FloatType()))

#finally we will write the final transformed dataframe that has transformed data to a CSV file 
crimeDF3.write.csv("./data/crimes_transformed.csv", header=True)