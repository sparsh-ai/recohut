from kafka import KafkaConsumer
import os


## Get KAFKA_ADDRESS
KAFKA_ADDRESS = "localhost"
print("KAFKA_ADDRESS: ", KAFKA_ADDRESS)

## To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('redditComments',
                         bootstrap_servers=[KAFKA_ADDRESS + ':9092'])

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))