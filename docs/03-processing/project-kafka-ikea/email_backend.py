import json
import time

from kafka import KafkaConsumer, KafkaProducer
# from flask import Flask, jsonify, request

ORDER_CONFIRMED_KAFKA_TOPIC = 'order_confirmed'
EMAIL_SENT_KAFKA_TOPIC = 'order_email_sent'

KAFKA_SERVER_ADDRESS = 'localhost:9092'
# KAFKA_SERVER_ADDRESS = '47.93.191.241:29093`

producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER_ADDRESS], security_protocol="PLAINTEXT",
                            value_serializer=lambda x: json.dumps(x).encode('utf-8'))

consumer = KafkaConsumer(ORDER_CONFIRMED_KAFKA_TOPIC, bootstrap_servers=[KAFKA_SERVER_ADDRESS], security_protocol="PLAINTEXT",
                            value_deserializer=lambda x: json.loads(x.decode('utf-8')))


def send_email(user_id, order_id, user_email, order_details, time, status):
    print("Sending email to user: {} with order details: {}".format(user_email, order_details))
    # send email to user
    # ...
    # ...
    # ...
    # ...   
    return True


while True:
    for message in consumer:
        # read data from consumer and call the send_email() function
        print("Received order details: {}".format(message.value))
        user_id = message.value['user_id']
        order_id = message.value['order_id']
        user_email = message.value['user_email']
        order_details = message.value['order_details']
        time = message.value['time']
        status = message.value['status']
        email_send_status = send_email(user_id, order_id, user_email, order_details, time, status)
        email_sent = {}
        email_sent['user_id'] = user_id
        email_sent['order_id'] = order_id
        email_sent['user_email'] = user_email
        email_sent['order_details'] = order_details
        email_sent['time'] = time
        email_sent['status'] = email_send_status
        producer.send(EMAIL_SENT_KAFKA_TOPIC, email_sent)
        print("Sent email details {} to kafka topic: {}".format(email_sent, EMAIL_SENT_KAFKA_TOPIC))