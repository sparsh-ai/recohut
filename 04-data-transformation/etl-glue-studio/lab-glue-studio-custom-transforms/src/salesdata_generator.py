from awsglue import DynamicFrame
import pyspark.sql.functions as F
import datetime
import time

def salesdata_generator(self, numSamples, year=None):
    if not year:
        # Use last year
        year = datetime.datetime.now().year - 1
    
    year_start_ts = int(time.mktime((year,1,1,0,0,0,0,0,0)))
    year_end_ts = int(time.mktime((year + 1,1,1,0,0,0,0,0,0)))
    ts_range = year_end_ts - year_start_ts
    
    departments = ["bargain", "checkout", "food hall", "sports", "menswear", "womenwear", "health and beauty", "home"]
    dep_array = F.array(*[F.lit(x) for x in departments])
    dep_randomizer = (F.round(F.rand() * (len(departments) -1))).cast("int")

    df = self.glue_ctx.sparkSession.range(numSamples) \
      .withColumn("sale_date", F.from_unixtime(F.lit(year_start_ts) + F.rand() * ts_range)) \
      .withColumn("amount_dollars", F.round(F.rand() * 1000, 2)) \
      .withColumn("department", dep_array.getItem(dep_randomizer))  
    return DynamicFrame.fromDF(df, self.glue_ctx, "sales_synthetic_data")

DynamicFrame.salesdata_generator = salesdata_generator