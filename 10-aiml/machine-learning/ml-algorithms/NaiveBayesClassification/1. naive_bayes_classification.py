# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import RFE
from sklearn.naive_bayes import GaussianNB

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import cross_validate, \
  RandomizedSearchCV, RepeatedStratifiedKFold
import sklearn.metrics as skmet

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans

np.set_printoptions(precision=5)

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.5f}'.format

# setup the features and target
nbagames = pd.read_csv("data/nbagames2017plus.csv", parse_dates=['GAME_DATE'])
nbagames = nbagames.loc[nbagames.WL_HOME.isin(['W','L'])]
nbagames.shape

nbagames['WL_HOME'] = \
  np.where(nbagames.WL_HOME=='L',0,1).astype('int')
  
nbagames.WL_HOME.value_counts(dropna=False)

# take a look at some of the data

# identify numeric and categorical data
num_cols = ['FG_PCT_HOME','FTA_HOME','FG3_PCT_HOME',
  'FTM_HOME','FT_PCT_HOME','OREB_HOME','DREB_HOME',
  'REB_HOME','AST_HOME','STL_HOME','BLK_HOME','TOV_HOME',
  'FG_PCT_AWAY','FTA_AWAY','FG3_PCT_AWAY',
  'FT_PCT_AWAY','OREB_AWAY','DREB_AWAY','REB_AWAY',
  'AST_AWAY','STL_AWAY','BLK_AWAY','TOV_AWAY']
cat_cols = ['TEAM_ABBREVIATION_HOME','SEASON']

# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(nbagames[num_cols + cat_cols],\
  nbagames[['WL_HOME']], test_size=0.2, random_state=0)

# setup column transformations
ohe = OneHotEncoder(drop='first', sparse=False)

cattrans = make_pipeline(ohe)
standtrans = make_pipeline(OutlierTrans(2),
  SimpleImputer(strategy="median"), StandardScaler())
coltrans = ColumnTransformer(
  transformers=[
    ("cat", cattrans, cat_cols),
    ("stand", standtrans, num_cols)
  ]
)

# fit an SVR model
nb = GaussianNB()

rfe = RFE(estimator=LogisticRegression(), n_features_to_select=15)

pipe1 = make_pipeline(coltrans, rfe, nb)

# do kfold cross validation
kf = RepeatedStratifiedKFold(n_splits=7, n_repeats=10,\
   random_state=0)

scores = cross_validate(pipe1, X_train, y_train.values.ravel(), \
  scoring=['accuracy','precision','recall','f1'], cv=kf, n_jobs=-1)

print("accuracy: %.2f, precision: %.2f, sensitivity: %.2f, f1: %.2f"  %
  (np.mean(scores['test_accuracy']),\
  np.mean(scores['test_precision']),\
  np.mean(scores['test_recall']),\
  np.mean(scores['test_f1'])))


nb_params = {
    'gaussiannb__var_smoothing': np.logspace(0,-9, num=100)
}

rs = RandomizedSearchCV(pipe1, nb_params, cv=kf, scoring='accuracy')
rs.fit(X_train, y_train.values.ravel())

rs.best_params_
rs.best_score_

results = \
  pd.DataFrame(rs.cv_results_['mean_test_score'], \
    columns=['meanscore']).\
  join(pd.DataFrame(rs.cv_results_['params'])).\
  sort_values(['meanscore'], ascending=False)

results

print("fit time: %.3f, score time: %.3f"  %
  (np.mean(rs.cv_results_['mean_fit_time']),\
  np.mean(rs.cv_results_['mean_score_time'])))


pred = rs.predict(X_test)

print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred, pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))


cm = skmet.confusion_matrix(y_test, pred)
cmplot = skmet.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Loss', 'Won'])
cmplot.plot()
cmplot.ax_.set(title='Home Team Win Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')


