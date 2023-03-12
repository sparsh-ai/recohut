from pymongo import MongoClient
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

client = MongoClient("mongodb+srv://athoillah:Akuaku123@cluster0.kejexjk.mongodb.net/test")
db = client["sample_training"]
company = db["companies"]

companies = pd.DataFrame()
array_columns = []

for field in company.find():
    comps_dict = {}
    
    for key, value in field.items():
        if key == '_id':
            comps_dict["id"] = str(value)

        elif key == 'offices':
            if len(value) > 0:
                for k, v in value[0].items():
                    comps_dict["offices_" + k] = v
            else:
                pass

        elif type(value) == dict or type(value) == list:
            if key not in array_columns:
                array_columns.append(key)        
            else:
                pass
        
        else:
            comps_dict[key] = value
        
    df_value = pd.DataFrame([comps_dict])
    
    companies = pd.concat([companies,df_value])

companies= companies.drop(['image','acquisition','ipo'], axis = 1)

url = 'postgresql+psycopg2://airflow_user:airflow_pass@localhost:5432/airflow_db'
engine = create_engine(url)

conn = psycopg2.connect(database="airflow_db", user='airflow_user', password='airflow_pass', host='localhost', port= '5432')
cursor = conn.cursor()

sql2 ='''CREATE TABLE IF NOT EXISTS dwh_final.companies(
   id text not null,
   name text,
   permalink text,
   crunchbase_url text,
   homepage_url text,
   blog_url text,
   blog_feed_url text,
   twitter_username text,
   category_code text,
   number_of_employees integer,
   founded_year integer,
   founded_month integer,
   founded_day integer,
   deadpooled_year integer,
   tag_list text, 
   alias_list text,
   email_address text,
   phone_number integer,
   description text,
   created_at text,
   updated_at text,
   overview text,
   total_money_raised integer,
   offices_description text,
   offices_address1 text,
   offices_address2 text,
   offices_zip_code integer,
   offices_city text,
   offices_state_code text,
   offices_country_code text,
   offices_latitude float,
   offices_longitude float,
   deadpooled_month text,
   deadpooled_day text,
   deadpooled_url text
)'''

cursor.execute(sql2)
print("Table created successfully........")
conn.commit()

companies.to_sql('companies', index=False, con=engine, schema='dwh_final', if_exists='replace')