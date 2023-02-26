# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.compose import TransformedTargetRegressor
from sklearn.pipeline import make_pipeline
from sklearn.impute import KNNImputer
from sklearn.model_selection import GridSearchCV

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 25)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

landtemps = pd.read_csv("data/landtempsb2019avgs.csv")
landtemps.set_index('locationid', inplace=True)

feature_cols = ['latabs','elevation']

# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(landtemps[feature_cols],\
  landtemps[['avgtemp']], test_size=0.1, random_state=0)

    
knnimp = KNNImputer(n_neighbors=45)

sgdr = SGDRegressor()

pipe1 = make_pipeline(OutlierTrans(3),knnimp,StandardScaler(), sgdr)

ttr=TransformedTargetRegressor(regressor=pipe1,transformer=StandardScaler())

sgdr_params = {
 'regressor__sgdregressor__alpha': 10.0 ** -np.arange(1, 7),
 'regressor__sgdregressor__loss': ['huber','epsilon_insensitive'],
 'regressor__sgdregressor__penalty': ['l2', 'l1', 'elasticnet'],
 'regressor__sgdregressor__epsilon': np.arange(0.1, 1.6, 0.1)
}


gs = GridSearchCV(ttr,param_grid=sgdr_params, cv=5, scoring="r2")
gs.fit(X_train, y_train)

gs.best_params_
gs.best_score_

results = \
  pd.DataFrame(gs.cv_results_['mean_test_score'], \
    columns=['meanscore']).\
  join(pd.DataFrame(gs.cv_results_['params'])).\
  sort_values(['meanscore'], ascending=False)

results.head(3).T

