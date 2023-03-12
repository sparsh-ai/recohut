import json
from kafka import KafkaConsumer
from sqlalchemy import create_engine, text
import psycopg2

# connection to postgres
url = 'postgresql+psycopg2://airflow_user:airflow_pass@localhost:5432/airflow_db'
engine = create_engine(url)
conn = psycopg2.connect(database="airflow_db", user='airflow_user', password='airflow_pass', host='localhost', port= '5432')
cursor = conn.cursor()
sql ='''CREATE TABLE IF NOT EXISTS dwh_final.topic_currency (
                currency_id varchar,
                currency_name varchar,
                rate float,
                timestamp timestamp
)'''

cursor.execute(sql)
print("Table created successfully........")
conn.commit()
conn.close()
consumer = KafkaConsumer(
                'TopicCurrency'
                , bootstrap_servers=['localhost:9092']
                , api_version=(0,10)
                , value_deserializer = lambda m: json.loads(m.decode("utf-8"))
            )

for message in consumer:
    json_data = message.value
    event = {
        "currency_id": json_data["currency_id"],
        "currency_name": json_data["currency_name"],
        "rate": json_data["rate"],
        "timestamp": json_data["timestamp"]
    }
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO dwh_final.topic_currency 
                VALUES (:currency_id, :currency_name, :rate, :timestamp)"""),
            [event]
        )