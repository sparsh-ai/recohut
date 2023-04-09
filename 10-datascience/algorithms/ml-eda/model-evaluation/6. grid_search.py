# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import sklearn.metrics as skmet
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
pd.set_option('display.width', 150)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.3f}'.format

# load the NLS data
landtemps = pd.read_csv("data/landtemps2019avgs.csv")

feature_cols = ['latabs','elevation']

X_train, X_test, y_train, y_test =  \
  train_test_split(landtemps[feature_cols],\
  landtemps[['avgtemp']], test_size=0.3, random_state=0)
      
#X = landtemps[feature_cols]      
#y = landtemps[['avgtemp']]
      

# use linear regression for recursive feature elimination
lr = LinearRegression()
split = KFold(n_splits=5, shuffle=True, random_state=0)

pipe = Pipeline([
 ('scaler', StandardScaler()),
 ('lr', LinearRegression())
        ])

pipeline = make_pipeline(StandardScaler(), LinearRegression())
scores = cross_validate(pipeline, X=X_train, y=y_train, cv=split, n_jobs=1, return_estimator = True)
scores
type(scores)
temp = pipeline.fit(X_train, y_train)


# get predictions and residuals
pred = lr.predict(X_test)

preddf = pd.DataFrame(pred, columns=['prediction'],
  index=X_test.index).join(X_test).join(y_test)
preddf['resid'] = preddf.avgtemp-preddf.prediction

preddf.resid.agg(['mean','median','skew','kurtosis'])


# generate summary model evaluation statistics
mse = skmet.mean_squared_error(y_test, pred)
mse
rmse = skmet.mean_squared_error(y_test, pred, squared=False)
rmse
mae = skmet.mean_absolute_error(y_test, pred)
mae
r2 = skmet.r2_score(y_test, pred)
r2
   

