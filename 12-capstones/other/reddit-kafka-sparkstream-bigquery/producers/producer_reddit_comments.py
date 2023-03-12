from json import dumps
from kafka import KafkaProducer
import praw
import re
# import pprint
import argparse

## Get KAFKA_ADDRESS through user arguments
parser = argparse.ArgumentParser(description='')
parser.add_argument('--KAFKA_ADDRESS',  type=str, required=True, help='External IP Address of Kafka VM')

args = parser.parse_args()
KAFKA_ADDRESS = args.KAFKA_ADDRESS
print("KAFKA_ADDRESS: ", KAFKA_ADDRESS)

## Create Kafka Producer -> Value Serializer is encoded as UTF-8
producer = KafkaProducer(bootstrap_servers=[KAFKA_ADDRESS + ':9092'],
                         api_version=(0,11,5),
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

## Create PRAW Instances
reddit = praw.Reddit(
    client_id="i9VuhpBLxkcF2k4CgOcYeg",
    client_secret="-R-7AnHMMyAgqkJz5ooNTsBuTh5DbQ",
    user_agent="python:test:v1.0 (by u/jjjjj12377)",
)

## Make sure it is read-only
print("Read Only: ", reddit.read_only)

## Define GLobal Subreddit Thread
FEDEX = reddit.subreddit("Fedex")

## Print Subreddit Simple Attributes
print("Subreddit Path: ", FEDEX._path)
print("Subredit Title: ", FEDEX.title)


## Stream Comments
for comment in FEDEX.stream.comments():
    try:
        comments_json = {}
        ### Check author if AutoMod Skip
        if comment.author.name != "AutoModerator":
            #### Create the comment attributes
            comments_json["id"] = comment.name
            comments_json["submission_url"] = comment.link_permalink
            comments_json["author"] = comment.author.name
            comments_json["author_flair"] = comment.author_flair_text
            comments_json["create_time"] = int(comment.created_utc)

            ## Text Body
            comments_json["text_body"] = re.sub(r'&#x200B;', '', comment.body).replace("\n", "").strip()

            ## Comment Parents
            ## Parent ID of the current comment (t1_* = comment of comment, t3_* = comment in submission)
            comments_json["parent_id"] = comment.parent_id
            ## Master Parent ID (this should be all t3_*) -> Ties to a submission post
            comments_json["link_id"] = comment.link_id

            ## Variables that might need updates
            ## Number of comments in the main posts
            comments_json["num_comments"] = comment.num_comments
            comments_json["ups"] = comment.ups

            ## Submit to Kafka Producers 
            producer.send("redditComments", value=comments_json)
            print("producing comments: ", comments_json)
    except:
        ## Handle removed comments
        pass