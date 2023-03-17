# Taxi Data Process and Save to Redshift using AWS Wrangler

```sh
pip install psycopg2-binary awscli boto3 awswrangler
```

```py
import os
import boto3
import json
from time import time

import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import awswrangler as wr


SECRET_NAME = "wysde"
URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet"
INFILE = "yellow_tripdata_2022-01.parquet"
S3_PATH = "s3://wysde/taxi"
DB_NAME = "dev"
TABLE_NAME = "yellow_tripdata_2022_01"
CONN_NAME = "aws-data-wrangler-redshift-dev"

CONN = wr.redshift.connect(CONN_NAME)

os.system(f"wget {URL} -O {INFILE}")
wr.s3.upload(local_file=INFILE, path=S3_PATH+"/"+INFILE)
dfs = wr.s3.read_parquet(path=S3_PATH+"/"+INFILE, chunked=100000)

for df in dfs:
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    wr.redshift.copy(
        df=df,
        path=S3_PATH+"/"+INFILE,
        con=CONN,
        schema='public',
        table=TABLE_NAME,
        mode="upsert",
        primary_keys=["VendorID"]
    )
```