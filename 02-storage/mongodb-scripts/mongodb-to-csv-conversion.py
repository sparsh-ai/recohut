# MongoDB to CSV conversion

# Pull a noSQL data from MongoDB and convert into Pandas dataframe

import pymongo as pm
from pymongo import MongoClient
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

def _connect_mongo(username, password, host, port, db):
    mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
    conn = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000, ssl=True)
    return conn[db] 

db = _connect_mongo('xxxx', 'xxxx', 'xxxx', xxxx, 'xxxx')
collection = db['xxxx']
test = pd.DataFrame(list(collection.find({}, {"var1":1, "var2":1})))
print(test.info())

# Extracting Non-array data
with open('non_array_features.txt') as f:
    content = f.readlines()
non_array_features = [x.strip() for x in content]

query = ""
for x in non_array_features:
    query+='"'+ x + '":1, '
query = query[:-2]

flat_df = json_normalize(list(collection.find({}, {<paste query string here without ''>})))
flat_df.shape

# Extracting Array data
def extract_array(feature, key, val):
    n1 = pd.DataFrame(list(collection.aggregate([{"$unwind" : "$"+str(feature)}, 
                                        {"$project" : {'key' : "$"+str(feature) + "." + key,
                                                       'value' : "$"+str(feature) + "." + val}}])))
    n2 = n1[~n1['_id'].astype(str).str.contains('timestamp', regex=False)]
    n3 = n2[~n2.set_index(['_id','key'])['value'].index.duplicated(keep='first')]
    n4 = n3.set_index(['_id','key'])['value'].unstack().add_suffix('_').reset_index()
    return n4


'''https://stackoverflow.com/questions/51402430/concatenate-columns-with-same-id-pandas-dataframe'''
def collide_me(x):
    x = x[~x['_id'].astype(str).str.contains('timestamp', regex=False)]
    y = (x.set_index(['_id', x.groupby(['_id']).cumcount()]).unstack().sort_index(axis=1, level=1))
    y.columns = ['{}_{}'.format(i, j) for i, j in y.columns]
    y = y.reset_index()
    return y

def extract_ndarray(df, key, value):
    n1 = df[['_id', key, value]]
    n2 = n1[~n1['_id'].astype(str).str.contains('timestamp', regex=False)]
    n3 = n2[~n2.set_index(['_id',key])[value].index.duplicated(keep='first')]
    n4 = n3.set_index(['_id',key])[value].unstack().add_prefix(key+'_').reset_index()
    return n4

# Key-value feature extraction
af1 = extract_array('array_feature_1', 'key', 'value')
af2 = extract_array('array_feature_2', 'key', 'value')

# Key-multivalue feature extraction
af3 = pd.DataFrame(list(collection.aggregate([{"$unwind" : "$array_feature_3"}, 
                                        {"$project" : {'featurename_31':'$array_feature_3.featurename_31',
                                                       'featurename_32':'$array_feature_3.featurename_32',
                                                       'featurename_33':'$array_feature_3.featurename_33'
                                                      }}])))
af3 = collide_me(af3)

# Key-value multi-dimensional feature extraction
af4 = json_normalize(list(collection.aggregate([{"$unwind": '$array_feature_4'},
                                        {"$project" : {'feature41':'$array_feature_4.feature41'}}
                                        ,{"$unwind": '$responses'}
                                        ,{"$project" : {'feature41_key':'$feature41.key',
                                                        'feature41_value':'$feature41.value'}}
                                       ])))

af4 = extract_ndarray(af4, 'feature41_key', 'feature41_value')

# Joining and exporting data
df = pd.merge(flat_df, af1, on='_id', how='outer')
df = pd.merge(df, af2, on='_id', how='outer')
df = pd.merge(df, af3, on='_id', how='outer')
df = pd.merge(df, af4, on='_id', how='outer')
df.to_csv('mongoDB_to_CSV_converted.csv')