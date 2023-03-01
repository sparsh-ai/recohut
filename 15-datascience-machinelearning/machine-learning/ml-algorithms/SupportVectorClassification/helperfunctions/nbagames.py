# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans

# setup the features and target
nbagames = pd.read_csv("data/nbagames2017plus.csv", parse_dates=['GAME_DATE'])
nbagames = nbagames.loc[nbagames.WL_HOME.isin(['W','L'])]
nbagames['WL_HOME'] = \
  np.where(nbagames.WL_HOME=='L',0,1).astype('int')


# identify numeric and categorical data
num_cols = ['FG_PCT_HOME','FTA_HOME','FG3_PCT_HOME',
  'FTM_HOME','FT_PCT_HOME','OREB_HOME','DREB_HOME',
  'REB_HOME','AST_HOME','STL_HOME','BLK_HOME','TOV_HOME',
  'FG_PCT_AWAY','FTA_AWAY','FG3_PCT_AWAY',
  'FT_PCT_AWAY','OREB_AWAY','DREB_AWAY','REB_AWAY',
  'AST_AWAY','STL_AWAY','BLK_AWAY','TOV_AWAY']
cat_cols = ['TEAM_ABBREVIATION_HOME','SEASON']


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
