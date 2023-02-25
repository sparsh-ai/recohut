# Connect to Postgres using Python

import os
import pandas as pd
from sqlalchemy import create_engine

POSTGRES_USERNAME = ''
POSTGRES_PASSWORD = ''
POSTGRES_ENDPOINT = ''
POSTGRES_DATABASE = ''

CONN = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_ENDPOINT}:5432/{POSTGRES_DATABASE}"
engine = create_engine(CONN)
conn = engine.connect()

try: 
    conn.execution_options(isolation_level="AUTOCOMMIT").execute("CREATE DATABASE mydb")
except Exception as e:
    print(e)
finally:
    conn.close()