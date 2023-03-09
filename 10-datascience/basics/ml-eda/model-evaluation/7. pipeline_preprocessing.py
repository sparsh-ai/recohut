# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from feature_engine.encoding import OneHotEncoder
from sklearn.impute import KNNImputer
from sklearn.model_selection import cross_validate, KFold
import sklearn.metrics as skmet
from sklearn.compose import ColumnTransformer
from sklearn.compose import TransformedTargetRegressor


import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans


pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format

# load the NLS data and create training and testing DataFrames
nls97wages = pd.read_csv("data/nls97wagesb.csv")
nls97wages.set_index("personid", inplace=True)

nls97wages.dropna(subset=['wageincome'], inplace=True)
nls97wages.loc[nls97wages.motherhighgrade==95,
  'motherhighgrade'] = np.nan
nls97wages.loc[nls97wages.fatherhighgrade==95,
  'fatherhighgrade'] = np.nan

# setup the features and target
num_cols = ['gpascience','gpaenglish','gpamath','gpaoverall',
  'motherhighgrade','fatherhighgrade','parentincome']
cat_cols = ['gender']
bin_cols = ['completedba']

nls97wages[['wageincome'] + num_cols].agg(['count','min','median','max']).T

target = nls97wages[['wageincome']]
features = nls97wages[num_cols + cat_cols + bin_cols]

X_train, X_test, y_train, y_test =  \
  train_test_split(features,\
  target, test_size=0.2, random_state=0)


# setup pipelines for column transformation
standtrans = make_pipeline(OutlierTrans(2),
  StandardScaler())
cattrans = make_pipeline(SimpleImputer(strategy="most_frequent"),
  OneHotEncoder(drop_last=True))
bintrans = make_pipeline(SimpleImputer(strategy="most_frequent"))

coltrans = ColumnTransformer(
  transformers=[
    ("stand", standtrans, num_cols),
    ("cat", cattrans, ['gender']),
    ("bin", bintrans, ['completedba'])
  ]
)

# add feature selection and a linear model to the pipeline and look at the parameter estimates
lr = LinearRegression()

pipe1 = make_pipeline(coltrans,
  KNNImputer(n_neighbors=5), lr)

ttr=TransformedTargetRegressor(regressor=pipe1,
  transformer=StandardScaler())


# run kfold cross-validation
kf = KFold(n_splits=10, shuffle=True, random_state=0)

scores = cross_validate(ttr, X=X_train, y=y_train,
  cv=kf, scoring=('r2', 'neg_mean_absolute_error'),
  n_jobs=1)

print("Mean Absolute Error: %.2f, R-squared: %.2f" % 
  (scores['test_neg_mean_absolute_error'].mean(),
  scores['test_r2'].mean()))


