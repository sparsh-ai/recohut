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

## Stream Submissions
for submission in FEDEX.stream.submissions():
    #### Wrap in Try Except for safety
    try:
        ####################################### EXTRACT SUBMISSION ATTRIBUTES ######################################
        #### Create variable for submission
        submission_json = {}

        #### Create the attributes for the posts
        submission_json["reddit_url"] = "https://www.reddit.com" + submission.permalink
        ## all of this should have format t3_ + submission.id (t3 = Submission Type)
        submission_json["id"] = submission.name  
        submission_json["title"] = submission.title

        #### Create Text
        raw_text = submission.selftext
        ## Removed Preview URLs
        cleaned_text = re.sub(r'https://preview.\S+', '', raw_text)
        ## Removed zero character whitespace
        cleaned_text = re.sub(r'&#x200B;', '', cleaned_text).replace("\n", "").strip()
        submission_json["text_body"] = cleaned_text

        ## Create Author
        submission_json["author"] = submission.author.name
        submission_json["author_flair"] = submission.author_flair_text
        ## Create Time
        submission_json["create_time"] = int(submission.created_utc)
        ## Create Flair Category
        submission_json["flair_category"] = submission.link_flair_text

        ## Attributes that might need updates (Ups, Upvote Ratio, and Num Comments)
        submission_json["ups"] = submission.ups
        submission_json["upvote_ratio"] = submission.upvote_ratio
        submission_json["num_comments"] = submission.num_comments

        ## Variables for Media
        images = []
        videos = []

        ## Get Media/Image/Preview (if only one image exist)
        if hasattr(submission, "preview"):
            ## We know there is only image
            ## Pick Image at this resolution: 640 width or nearest to that using the item_no
            item_no = min(3, len(submission.preview["images"][0]["resolutions"]) - 1)
            images.append(submission.preview["images"][0]["resolutions"][item_no]["url"])
        
        ## Get Media/Image/Preview (if only one or more image exist)
        if hasattr(submission, "media_metadata"):
            ## We know there is multiple medias
            ## Pick Image at this resolution: 640 width or nearest to that
            for idx, elem in enumerate(submission.media_metadata):
                item_no = min(3, len(submission.media_metadata[elem]["p"]) - 1)
                images.append(submission.media_metadata[elem]["p"][item_no]["u"])
        
        ## Get Video if exist
        if hasattr(submission, "media") and submission.media is not None:
            for idx, elem in enumerate(submission.media):
                if elem == "reddit_video":
                    videos.append(submission.media[elem]["fallback_url"])

        ## Place images and videos into JSON
        submission_json["images"] = images
        submission_json["videos"] = videos

        ## Submit to Kafka Producers 
        producer.send("redditSubmissions", value=submission_json)
        print("producing submission: ", submission_json)

        ####################################### EXTRACT COMMENT ATTRIBUTES ######################################
        ## Iterate through all available comments
        for key_comment, val_comment in submission._comments_by_id.items():
            ## Create Empty Comments Json
            comments_json = {}

            try:
                ### Check author if AutoMod Skip
                if val_comment.author.name != "AutoModerator":
                    #### Create the comment attributes
                    comments_json["id"] = val_comment.name
                    comments_json["submission_url"] = "https://www.reddit.com" + val_comment.permalink
                    comments_json["author"] = val_comment.author.name
                    comments_json["author_flair"] = val_comment.author_flair_text
                    comments_json["create_time"] = int(val_comment.created_utc)

                    ## Text Body
                    comments_json["text_body"] = re.sub(r'&#x200B;', '', val_comment.body).replace("\n", "").strip()

                    ## Comment Parents
                    ## Parent ID of the current comment (t1_* = comment of comment, t3_* = comment in submission)
                    comments_json["parent_id"] = val_comment.parent_id
                    ## Master Parent ID (this should be all t3_*) -> Ties to a submission post
                    comments_json["link_id"] = val_comment.link_id

                    ## Variables that might need updates
                    ## Number of comments in the main posts
                    comments_json["num_comments"] = submission.num_comments
                    comments_json["ups"] = val_comment.ups

                    ## Submit to Kafka Producers 
                    producer.send("redditComments", value=comments_json)
                    print("producing comments: ", comments_json)
            except:
                ## Handle removed comments
                pass

    except:
        ## Handle Random Errors (Ex: Removed Posts ...)
        pass

    