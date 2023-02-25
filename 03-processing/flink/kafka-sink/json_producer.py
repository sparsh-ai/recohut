from kafka import KafkaProducer
import json

data = [
  {"framework": "Spark", "chapter": "1"},
  {"framework": "Airflow", "chapter": "2"},
  {"framework": "Kafka", "chapter": "3"},
  {"framework": "Flink", "chapter": "4"},
]

producer = KafkaProducer(bootstrap_servers = ["localhost:9092"])
for d in data:
  producer.send("example-source", json.dumps(d).encode("utf-8"))
producer.flush()