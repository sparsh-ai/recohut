# Load CSV into Postgres

import psycopg2
import pandas as pd
import sqlalchemy as sa

conn = psycopg2.connect(f"host=database-1.us-east-1.rds.amazonaws.com dbname=template1 user=postgres password=")
conn.set_session(autocommit=True)
cur = conn.cursor()
cur.execute("DROP DATABASE IF EXISTS stations WITH (FORCE)")
cur.execute("CREATE DATABASE stations WITH ENCODING 'utf8' TEMPLATE template0")
conn.close()   

conn = psycopg2.connect(f"host=database-1.us-east-1.rds.amazonaws.com dbname=stations user=postgres password=")
DDL = """
CREATE TABLE stations (
  stop_id INTEGER PRIMARY KEY,
  direction_id VARCHAR(1) NOT NULL,
  stop_name VARCHAR(70) NOT NULL,
  station_name VARCHAR(70) NOT NULL,
  station_descriptive_name VARCHAR(200) NOT NULL,
  station_id INTEGER NOT NULL,
  "order" INTEGER,
  red BOOLEAN NOT NULL,
  blue BOOLEAN NOT NULL,
  green BOOLEAN NOT NULL
);
"""
cur = conn.cursor()
cur.execute(DDL)
conn.commit()
conn.close()

df = pd.read_csv("data.csv")
db_url = 'postgresql://<username>:<password>@database-1.us-east-1.rds.amazonaws.com:5432/stations'
engine = sa.create_engine(db_url)
df.to_sql('stations', engine, method='multi', index=False, if_exists='append')