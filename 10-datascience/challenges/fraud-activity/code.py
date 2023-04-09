
from __future__ import print_function
import math
import datetime 
from time import strftime
from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os
import csv as csv
from sklearn import metrics
from sklearn import cross_validation
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

from tensorflow.python.data import Dataset
from tensorflow.contrib.tensor_forest.python import tensor_forest
from tensorflow.python.ops import resources

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format


data = pd.read_csv('Fraud/Fraud_Data.csv')
ip_addresses = pd.read_csv("Fraud/IpAddress_to_Country.csv")

#shuffle the data ahead
data = data.reindex(np.random.permutation(data.index))

# check if the user_id is unique
if len(data['user_id']) == len(set(data['user_id'])):
	print ('User Id are unique')

#get the country from the ipaddress range
country = [None]*(len(data['user_id']))
for i in range(len(data['ip_address'])):
	for j in range(len(ip_addresses['lower_bound_ip_address'])):
		if ip_addresses['upper_bound_ip_address'][j] >= data['ip_address'][i] >= ip_addresses['lower_bound_ip_address'][j]:
			country[i] = ip_addresses['country'][j]
			continue
data['country'] = country
#count the most frequent country and select the most frequent 50 countries and turn others as 'others'
print (data['country'].values_count())
country_list=country.sorted()[1:50]

new_country = ['others']*len(data['user_id'])
for i in range(len(data['country'])):
	if data['country'][i] in country_list:
		new_country[i] = data['country'][i]
data['country'] = new_country

#convert the datatime to timestamp
def convertTime(time):
	new_time = [0]*len(time)
	for i in range(len(time)):
		dt = datetime.datetime.strptime(time[i], "%Y-%m-%d %H:%M:%S")
		epoch = datetime.datetime.fromtimestamp(0)
		new_time[i] = (dt - epoch).total_seconds()
	return new_time

data['signup_timestamp'] = convertTime(data['signup_time'])
data['purchase_timestamp'] = convertTime(data['purchase_time'])

#get the time difference between signup and purchase and set it as another feature
purchase_signup_diff = data['signup_timestamp']-data['purchase_timestamp']


# get the week of the year
def getWeek(time):
	week = [0]*len(time)
	for i in range(len(time)):
		dt = datetime.datetime.strptime(time[i],"%Y-%m-%d %H:%M:%S")
		week[i] = int(dt.isocalendar()[1])
	return week
#get the day of the week
def getDay(time):
	day = [0]*len(time)
	for i in range(len(time)):
		dt = datetime.datetime.strptime(time[i],"%Y-%m-%d %H:%M:%S")
		day[i] = int(dt.isocalendar()[2])
	return day

data['signup_wy'] = getWeek(data['signup_time'])
data['purchase_wy'] = getWeek(data['purchase_time'])
data['signup_dw'] = getDay(data['signup_time'])
data['purchase_dw'] = getDay(data['purchase_time'])


#another way of getting the data with selected columns
#train_data = data.drop(data.columns[[0,1,2,4]],axis=1,inplace = True)
#print (list(train_data.columns.values))

def Labelencorder(data):
  encoder = LabelEncoder()
  sex = encoder.fit_transform(data["sex"])
  data["sex"] = sex
  source = encoder.fit_transform(data["source"])
  data["source"] = source
  browser = encoder.fit_transform(data["browser"])
  data["browser"] = browser
  country = encoder.fit_transform(data["country"])
  data["country"] = country 
  return data

def preprocess_features(data_dataframe):
	selected_features = data_dataframe[[
	'purchase_value', 'source', 'browser', 'sex', 'age',
	'ip_address', 'country','signup_wy', 'purchase_wy', 
	'signup_dw', 'purchase_dw']]
	processed_features = selected_features.copy()
	return processed_features

def preprocess_targets(data_dataframe):

	output_targets = pd.DataFrame()
	output_targets["class"] = data_dataframe["class"]
	return output_targets


data = Labelencorder(data)
data_features = preprocess_features(data)
data_target = preprocess_targets(data)

#print (data_features.head())
#print (data_features.dtypes)
#print (data_target.dtypes)


from sklearn.cross_validation import train_test_split
train_sample, test_sample, train_target, test_target = train_test_split(data_features, data_target, test_size = 0.25, random_state = 0)

print (train_sample.dtypes)

num_features = 10
num_steps = 100
num_classes = 2
num_trees = 50
max_nodes = 1000
batch_size = 100
# Input and Target placeholders
X = tf.placeholder(tf.float32, shape=[None, num_features])
# For random forest, labels must be integers (the class id)
Y = tf.placeholder(tf.int64, shape=[None,1])

hparams = tensor_forest.ForestHParams(
	num_classes=num_classes, 
	num_features=num_features, 
	num_trees=num_trees, 
	max_nodes=max_nodes,
	).fill()
# Build the Random Forest
forest_graph = tensor_forest.RandomForestGraphs(hparams)

# Get training graph and loss
train_op = forest_graph.training_graph(X, Y)
loss_op = forest_graph.training_loss(X, Y)

# Measure the accuracy
infer_op, _, _ = forest_graph.inference_graph(X)
correct_prediction = tf.equal(tf.argmax(infer_op, 1), tf.cast(Y, tf.int64))
accuracy_op = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Initialize the variables (i.e. assign their default value) and forest resources
init_vars = tf.group(tf.global_variables_initializer(), resources.initialize_resources(resources.shared_resources()))
    
# Start TensorFlow session
sess = tf.Session()

# Run the initializer
sess.run(init_vars)



# Training
for i in range(1,num_steps+1):
	#prepare batch data
	_, l = sess.run([train_op, loss_op], feed_dict={X: train_sample, Y: train_target})
	if i % 50 == 0 or i == 1:
		acc = sess.run(accuracy_op, feed_dict={X: train_sample, Y: train_target})
		print('Step %i, Loss: %f, Acc: %f' % (i, l, acc))

# Test Model
print("Test Accuracy:", sess.run(accuracy_op, feed_dict={X: test_sample, Y: test_target}))

#data['device_id_count'] = data.groupby(['device_id']).count()
#data['ip_address'] = data.groupby(['ip_address']).count
