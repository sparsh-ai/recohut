# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from scipy.stats import uniform
from sklearn.feature_selection import RFECV
from sklearn.impute import SimpleImputer
from scipy.stats import randint
from sklearn.model_selection import RandomizedSearchCV

import sklearn.metrics as skmet
import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans
import nbagames as ng
from displayfunc import dispbound

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

# load the training and testing data
X_train = ng.X_train
X_test = ng.X_test
y_train = ng.y_train
y_test = ng.y_test

# show the decision boundaries for a couple of kernels
pipe0 = make_pipeline(OutlierTrans(2),
  SimpleImputer(strategy="median"),
  StandardScaler())
X_train_enc = \
  pipe0.fit_transform(X_train[['FG_PCT_HOME',
   'DREB_HOME']])

dispbound(SVC(kernel='rbf', gamma=0.1, C=1),
  X_train_enc,['FG_PCT_HOME','DREB_HOME'],
  y_train.values.ravel(),
  "SVC with rbf kernel-gamma=30, C=1")

dispbound(SVC(kernel='poly', degree=10),
  X_train_enc, ['FG_PCT_HOME','DREB_HOME'],
  y_train.values.ravel(),
  "SVC with polynomial kernel - degree=10")


# add feature selection and a linear model to the pipeline and look at the parameter estimates
rfecv = RFECV(estimator=LogisticRegression())

svc = SVC()

pipe1 = make_pipeline(ng.coltrans, rfecv, svc)

svc_params = [
  {
    'svc__kernel': ['rbf'],
    'svc__C': uniform(loc=0, scale=20),
    'svc__gamma': uniform(loc=0, scale=100)
  },
  {
    'svc__kernel': ['poly'],
    'svc__degree': randint(2, 5),
    'svc__C': uniform(loc=0, scale=20),
    'svc__gamma': uniform(loc=0, scale=100)
  },
  {
    'svc__kernel': ['linear','sigmoid'],
    'svc__C': uniform(loc=0, scale=20)
  }
]

rs = RandomizedSearchCV(pipe1, svc_params, cv=5, 
  scoring='accuracy', n_iter=20, n_jobs=-1,
  verbose=20, random_state=0)
rs.fit(X_train, y_train.values.ravel())

rs.best_params_
rs.best_score_

results = \
  pd.DataFrame(rs.cv_results_['mean_test_score'], \
    columns=['meanscore']).\
  join(pd.json_normalize(rs.cv_results_['params'])).\
  sort_values(['meanscore'], ascending=False).\
  rename(columns=\
    {'svc__C':'C',
     'svc__gamma':'gamma',
     'svc__kernel':'kernel',
     'svc__degree':'degree'}).\
  set_index(['meanscore'])

results


pred = rs.predict(X_test)

print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred, pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))

cm = skmet.confusion_matrix(y_test, pred)
cmplot = skmet.ConfusionMatrixDisplay(confusion_matrix=cm, 
  display_labels=['Loss', 'Won'])
cmplot.plot()
cmplot.ax_.set(title='Home Team Win Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')

