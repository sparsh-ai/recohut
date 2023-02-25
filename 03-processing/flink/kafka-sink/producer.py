from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers = ["localhost:9092"])
producer.send("example-source", b"testing out flink and kafka!!!")
producer.flush()