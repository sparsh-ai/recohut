import tweepy
import json 
from kafka import KafkaProducer

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

class ProcessStream(tweepy.Stream):
  def on_data(self, raw_data):
    data = json.loads(raw_data)
    if "lang" in data and data["lang"] == "ko":
      korean_tweet = {
        "text": data["text"],
        "timestamp_ms": data["timestamp_ms"]
      }
      producer.send("korean-tweets", json.dumps(korean_tweet).encode("utf-8"))

twitter_stream = ProcessStream(
  consumer_key,
  consumer_secret,
  access_token,
  access_token_secret
)

twitter_stream.filter(track=["Twitter"])