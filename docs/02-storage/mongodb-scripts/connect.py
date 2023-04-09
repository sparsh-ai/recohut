"""
!pip uninstall pymongo
!pip install pymongo[srv]
"""

import os
import pymongo
from bson.json_util import dumps

MONGODB_USER = 'kafka-demo'
MONGODB_PASSWORD = '<your-pass>'
MONGODB_CLUSTER = 'cluster0.ca4wh.mongodb.net'
MONGODB_DATABASE = 'movielens'

mongo_uri = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER}/{MONGODB_DATABASE}?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)