# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate

import sklearn.metrics as skmet
import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans,\
  ReplaceVals

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format

# load the health information data
machinefailuretype = pd.read_csv("data/machinefailuretype.csv")
machinefailuretype.info()
machinefailuretype.head()
machinefailuretype.failtype.value_counts(dropna=False).sort_index()
machinefailuretype.machinetype.\
  value_counts(dropna=False).sort_index()

  
# take a look at some of the data

# identify numeric and categorical data
num_cols = ['airtemp','processtemperature','rotationalspeed',
  'torque','toolwear']
cat_cols = ['machinetype']

machinefailuretype[num_cols].agg(['min','median','max']).T

rep_dict = {
  'failtype': {'No Failure"':1,
    'Heat Dissipation Failure':2,
    'Power Failure':3,
    'Overstrain Failure':4,
    'Random Failures':5,
    'Tool Wear Failure':5}
}


# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(machinefailuretype[num_cols + cat_cols],\
  machinefailuretype[['failtypecode']], test_size=0.2, random_state=0)


# setup column transformations
ohe = OneHotEncoder(drop='first', sparse=False)

standtrans = make_pipeline(OutlierTrans(3),SimpleImputer(strategy="median"),
  StandardScaler())
cattrans = make_pipeline(ohe)
coltrans = ColumnTransformer(
  transformers=[
    ("stand", standtrans, num_cols),
    ("cat", cattrans, cat_cols),
  ]
)

# construct a pipeline with preprocessing, feature selection, and logistic model
lr = LogisticRegression(random_state=0, multi_class='multinomial',
  solver='lbfgs', max_iter=1000)

kf = RepeatedStratifiedKFold(n_splits=10, n_repeats=5, random_state=0)

pipe1 = make_pipeline(coltrans, lr)

cm = skmet.confusion_matrix(y_test, pipe1.fit(X_train, y_train.values.ravel()).\
   predict(X_test))
cmplot = skmet.ConfusionMatrixDisplay(confusion_matrix=cm,
   display_labels=['None', 'Heat','Power','Overstrain','Other'])
cmplot.plot()
cmplot.ax_.set(title='Machine Failure Type Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')


scores = cross_validate(pipe1, X_train, y_train.values.ravel(), \
  scoring=['accuracy','precision_weighted','recall_weighted',
           'f1_macro','f1_weighted'], cv=kf, n_jobs=-1)

accuracy, precision, sensitivity, f1_macro, f1_weighted = \
  np.mean(scores['test_accuracy']),\
  np.mean(scores['test_precision_weighted']),\
  np.mean(scores['test_recall_weighted']),\
  np.mean(scores['test_f1_macro']),\
  np.mean(scores['test_f1_weighted'])

accuracy, precision, sensitivity, f1_macro, f1_weighted







