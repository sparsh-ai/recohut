from pymongo import MongoClient
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

client = MongoClient("mongodb+srv://athoillah:Akuaku123@cluster0.kejexjk.mongodb.net/test")
db = client["sample_training"]
zips = db["zips"]


df_zips = pd.DataFrame(list(zips.find()))
df_zip = pd.DataFrame(df_zips['loc'].values.tolist())
df=df_zip.rename(columns = {'y': 'latitude', 'x': 'longitude'})
df_merged = df_zips.join(df)
df_zip_final = df_merged.drop(columns=['loc'])
df_zip_final['_id'] = df_zip_final['_id'].astype('string')

url = 'postgresql+psycopg2://airflow_user:airflow_pass@localhost:5432/airflow_db'
engine = create_engine(url)
conn = psycopg2.connect(database="airflow_db", user='airflow_user', password='airflow_pass', host='localhost', port= '5432')

cursor = conn.cursor()

sql ='''CREATE TABLE IF NOT EXISTS dwh_final.zips(
   _id text not null,
   city text,
   zip integer,
   pop integer,
   state text,
   latitude float,
   longitude float
)'''

cursor.execute(sql)
print("Table created successfully........")
conn.commit()
conn.close()

df_zip_final.to_sql('zips', index=False, con=engine, schema='dwh_final', if_exists='replace')
