from kafka import KafkaProducer 
import csv 
import json 
import time 

brokers = ["localhost:9091", "localhost:9092", "localhost:9093"]
producer = KafkaProducer(bootstrap_servers = brokers)

topicName = "trips"

with open("./trips/yellow_tripdata_2021-01.csv", "r") as file:
  reader = csv.reader(file)
  headings = next(reader)

  for row in reader:
    producer.send(topicName, json.dumps(row).encode("utf-8"))
    print(row)
    time.sleep(1)