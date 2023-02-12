import time 
from kafka import KafkaProducer 

producer = KafkaProducer(bootstrap_servers = ["localhost:9092"])

TAXI_TRIPS_TOPIC = "taxi-trips"
with open("./trips/yellow_tripdata_2021-01.csv", "r") as f:
  next(f)
  for row in f:
    producer.send(TAXI_TRIPS_TOPIC, row.encode("utf-8"))
    print(row)
    time.sleep(1)

producer.flush()