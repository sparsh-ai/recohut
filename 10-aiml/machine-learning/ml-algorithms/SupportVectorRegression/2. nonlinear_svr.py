# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVR, SVR
from scipy.stats import uniform
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.compose import TransformedTargetRegressor
from sklearn.impute import KNNImputer
from sklearn.model_selection import RandomizedSearchCV
import sklearn.metrics as skmet
import matplotlib.pyplot as plt

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans


pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

# load the land temperatures data
landtemps = pd.read_csv("data/landtempsb2019avgs.csv")
landtemps.set_index('locationid', inplace=True)

feature_cols = ['latabs','elevation']

landtemps[['avgtemp'] + feature_cols].\
  agg(['count','min','median','max']).T

# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(landtemps[feature_cols],\
  landtemps[['avgtemp']], test_size=0.1, random_state=0)


# add feature selection and a linear model to the pipeline and look at the parameter estimates
svr = LinearSVR(epsilon=1.0, max_iter=100000)

knnimp = KNNImputer(n_neighbors=45)

pipe1 = make_pipeline(OutlierTrans(3), knnimp, StandardScaler(), svr)

ttr=TransformedTargetRegressor(regressor=pipe1,
  transformer=StandardScaler())

svr_params = {
 'regressor__linearsvr__epsilon': uniform(loc=0, scale=1.5),
 'regressor__linearsvr__C': uniform(loc=0, scale=20)
}

rs = RandomizedSearchCV(ttr, svr_params, cv=10, scoring='neg_mean_absolute_error')
rs.fit(X_train, y_train)

rs.best_params_
rs.best_score_


# get predictions and residuals
pred = rs.predict(X_test)

preddf = pd.DataFrame(pred, columns=['prediction'],
  index=X_test.index).join(X_test).join(y_test)

preddf['resid'] = preddf.avgtemp-preddf.prediction

plt.scatter(preddf.prediction, preddf.resid, color="blue")
plt.axhline(0, color='red', linestyle='dashed', linewidth=1)
plt.title("Scatterplot of Predictions and Residuals")
plt.xlabel("Predicted Gax Tax")
plt.ylabel("Residuals")
plt.show()

# do a grid search to find the best value of alpha
svr = SVR(kernel='rbf')

pipe1 = make_pipeline(OutlierTrans(3), knnimp, StandardScaler(), svr)

ttr=TransformedTargetRegressor(regressor=pipe1,
  transformer=StandardScaler())

svr_params = {
 'regressor__svr__epsilon': uniform(loc=0, scale=5),
 'regressor__svr__C': uniform(loc=0, scale=20),
 'regressor__svr__gamma': uniform(loc=0, scale=100)
 }

rs = RandomizedSearchCV(ttr, svr_params, cv=10, scoring='neg_mean_absolute_error')
rs.fit(X_train, y_train)

rs.best_params_
rs.best_score_


# get predictions and residuals
pred = rs.predict(X_test)

preddf = pd.DataFrame(pred, columns=['prediction'],
  index=X_test.index).join(X_test).join(y_test)

preddf['resid'] = preddf.avgtemp-preddf.prediction

plt.scatter(preddf.prediction, preddf.resid, color="blue")
plt.axhline(0, color='red', linestyle='dashed', linewidth=1)
plt.title("Scatterplot of Predictions and Residuals")
plt.xlabel("Predicted Gax Tax")
plt.ylabel("Residuals")
plt.show()


pd.DataFrame(np.logspace(0, 4, 10), columns=['values']).to_excel('views/test.xlsx')

uniform(loc=0, scale=4).rvs(10)
uniform(loc=0.1, scale=2.0).rvs(100)

# plot the residuals
plt.hist(preddf.resid, color="blue", bins=np.arange(-0.5,1.0,0.25))
plt.axvline(preddf.resid.mean(), color='red', linestyle='dashed', linewidth=1)
plt.title("Histogram of Residuals for Gax Tax Model")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.xlim()
plt.show()

# plot predictions against the residuals
plt.scatter(preddf.prediction, preddf.resid, color="blue")
plt.axhline(0, color='red', linestyle='dashed', linewidth=1)
plt.title("Scatterplot of Predictions and Residuals")
plt.xlabel("Predicted Gax Tax")
plt.ylabel("Residuals")
plt.show()


# do kfold cross validation
X_train, X_test, y_train, y_test =  \
  train_test_split(features,\
  target, test_size=0.1, random_state=22)

kf = KFold(n_splits=3, shuffle=True, random_state=0)

cross_validate(ttr, X=X_train, y=y_train,
  cv=kf, scoring=('r2', 'neg_mean_absolute_error'), n_jobs=-1)

