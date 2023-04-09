from __future__ import print_function
import math
from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os
import csv as csv
from sklearn import metrics
import tensorflow as tf
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import LabelEncoder

from tensorflow.python.data import Dataset

data = pd.read_csv('Fraud/Fraud_Data.csv')
ip_addresses = read.csv("Fraud/IpAddress_to_Country.csv")

if len(data[user_id]) == len(set(data[user_id])):
	print ('User Id are unique')



