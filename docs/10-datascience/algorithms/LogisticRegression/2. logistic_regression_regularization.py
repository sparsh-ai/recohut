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
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from scipy.stats import uniform
import sklearn.metrics as skmet

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans,\
  MakeOrdinal, ReplaceVals

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.3f}'.format

healthinfo = pd.read_csv("data/healthinfosample.csv")
healthinfo.set_index("personid", inplace=True)

# take a look at some of the data
healthinfo['heartdisease'] = \
  np.where(healthinfo.heartdisease=='No',0,1).\
  astype('int')

# identify numeric and categorical data
num_cols = ['bmi','physicalhealthbaddays',
   'mentalhealthbaddays','sleeptimenightly']
binary_cols = ['smoking','alcoholdrinkingheavy',
  'stroke','walkingdifficult','physicalactivity',
  'asthma','kidneydisease','skincancer']
cat_cols = ['gender','ethnicity']
spec_cols1 = ['agecategory']
spec_cols2 = ['genhealth']
spec_cols3 = ['diabetic']

rep_dict = {
  'genhealth': {'Poor':0,'Fair':1,'Good':2,
    'Very good':3,'Excellent':4},
  'diabetic': {'No':0,
    'No, borderline diabetes':0,'Yes':1,
    'Yes (during pregnancy)':1}           
}

# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(healthinfo[num_cols + 
    binary_cols + cat_cols + spec_cols1 +
    spec_cols2 + spec_cols3],\
  healthinfo[['heartdisease']], test_size=0.2,
    random_state=0)

# setup column transformations
ohe = OneHotEncoder(drop='first', sparse=False)

standtrans = make_pipeline(OutlierTrans(3),
  SimpleImputer(strategy="median"),
  StandardScaler())
spectrans1 = make_pipeline(MakeOrdinal(),
  StandardScaler())
spectrans2 = make_pipeline(ReplaceVals(rep_dict),
  StandardScaler())
spectrans3 = make_pipeline(ReplaceVals(rep_dict))
bintrans = make_pipeline(ohe)
cattrans = make_pipeline(ohe)
coltrans = ColumnTransformer(
  transformers=[
    ("stand", standtrans, num_cols),
    ("spec1", spectrans1, spec_cols1),
    ("spec2", spectrans2, spec_cols2),
    ("spec3", spectrans3, spec_cols3),
    ("bin", bintrans, binary_cols),
    ("cat", cattrans, cat_cols),
  ]
)

# construct a pipeline with preprocessing, feature selection, and logistic model
lr = LogisticRegression(random_state=1, class_weight='balanced',
  max_iter=1000)

kf = RepeatedStratifiedKFold(n_splits=7, n_repeats=3, random_state=0)

pipe1 = make_pipeline(coltrans, lr)

reg_params = [
  {
    'logisticregression__solver': ['liblinear'],
    'logisticregression__penalty': ['l1','l2'],
    'logisticregression__C': uniform(loc=0, scale=10)
  },
  {
    'logisticregression__solver': ['newton-cg'],
    'logisticregression__penalty': ['l2'],
    'logisticregression__C': uniform(loc=0, scale=10)
  },
  {
    'logisticregression__solver': ['saga'],
    'logisticregression__penalty': ['elasticnet'],
    'logisticregression__l1_ratio': uniform(loc=0, scale=1),   
    'logisticregression__C': uniform(loc=0, scale=10)
  }
]


rs = RandomizedSearchCV(pipe1, reg_params, cv=kf, 
  n_iter=20, scoring='roc_auc')
rs.fit(X_train, y_train.values.ravel())

rs.best_params_
rs.best_score_

results = \
  pd.DataFrame(rs.cv_results_['mean_test_score'], \
    columns=['meanscore']).\
  join(pd.json_normalize(rs.cv_results_['params'])).\
  sort_values(['meanscore'], ascending=False)

results.head(3).T

# get predictions and residuals
pred = rs.predict(X_test)

cm = skmet.confusion_matrix(y_test, pred)
cmplot = \
  skmet.ConfusionMatrixDisplay(confusion_matrix=cm,
  display_labels=['Negative', 'Positive'])
cmplot.plot()
cmplot.ax_.\
  set(title='Heart Disease Prediction Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')


print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred,
    pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))

