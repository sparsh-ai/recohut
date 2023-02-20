import json
import time
from kafka import KafkaConsumer, KafkaProducer

OERDER_KAFKA_TOPIC = 'order_details'
ORDER_CONFIRMED_KAFKA_TOPIC = 'order_confirmed'

KAFKA_SERVER_ADDRESS = 'localhost:9092'
# KAFKA_SERVER_ADDRESS = '47.93.191.241:29093`

consumer = KafkaConsumer(OERDER_KAFKA_TOPIC, bootstrap_servers=[KAFKA_SERVER_ADDRESS], security_protocol="PLAINTEXT",
                            value_deserializer=lambda x: json.loads(x.decode('utf-8')))
producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER_ADDRESS], security_protocol="PLAINTEXT",
                            value_serializer=lambda x: json.dumps(x).encode('utf-8'))

while True:
    for message in consumer:
        print("Received order details: {}".format(message.value))
        user_id = message.value['user_id']
        order_id = message.value['order_id']
        user_email = message.value['user_email']
        order_details = message.value['order_details']
        time = message.value['time']
        ## do some suff on the order and check the confirmation
        order_confirmed = {}
        order_confirmed['user_id'] = user_id
        order_confirmed['order_id'] = order_id
        order_confirmed['user_email'] = user_email
        order_confirmed['order_details'] = order_details
        order_confirmed['time'] = time
        order_confirmed['status'] = 'confirmed'
        producer.send(ORDER_CONFIRMED_KAFKA_TOPIC, order_confirmed)
        print("Sent order details {} to kafka topic: {}".format(order_confirmed, ORDER_CONFIRMED_KAFKA_TOPIC))