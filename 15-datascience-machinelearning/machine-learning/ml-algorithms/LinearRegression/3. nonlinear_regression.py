# import pandas, numpy, and matplotlib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.compose import TransformedTargetRegressor
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
from sklearn.impute import KNNImputer
import matplotlib.pyplot as plt

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans

pd.set_option('display.width', 150)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 100)
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

# do a linear reqression and cross validate
lr = LinearRegression()

knnimp = KNNImputer(n_neighbors=45)

pipe1 = make_pipeline(OutlierTrans(3),knnimp,StandardScaler(), lr)

ttr=TransformedTargetRegressor(regressor=pipe1,transformer=StandardScaler())

kf = KFold(n_splits=10, shuffle=True, random_state=0)
      
scores = cross_validate(ttr, X=X_train, y=y_train,
  cv=kf, scoring=('r2', 'neg_mean_absolute_error'), n_jobs=1)

scores['test_r2'].mean(), scores['test_neg_mean_absolute_error'].mean()

# get predictions and residuals
ttr.fit(X_train, y_train)

pred = ttr.predict(X_test)

preddf = pd.DataFrame(pred, columns=['prediction'],
  index=X_test.index).join(X_test).join(y_test)

preddf['resid'] = preddf.avgtemp-preddf.prediction

preddf.resid.agg(['mean','median','skew','kurtosis'])

# plot the residuals
plt.hist(preddf.resid, color="blue")
plt.axvline(preddf.resid.mean(), color='red', linestyle='dashed', linewidth=1)
plt.title("Histogram of Residuals for Linear Model of Temperature")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.show()

# plot predictions against the residuals
plt.scatter(preddf.prediction, preddf.resid, color="blue")
plt.axhline(0, color='red', linestyle='dashed', linewidth=1)
plt.title("Scatterplot of Predictions and Residuals")
plt.xlabel("Predicted Temperature")
plt.ylabel("Residuals")
plt.xlim(-20,40)
plt.ylim(-27,10)
plt.show()


# do a polynomial transformation
polytrans = PolynomialFeatures(degree=4, include_bias=False)
polytrans.fit(X_train.dropna())
featurenames = polytrans.get_feature_names(feature_cols)
featurenames

# get predictions and residuals
pipe2 = make_pipeline(OutlierTrans(3), knnimp,
  polytrans, StandardScaler(), lr)

ttr2 = TransformedTargetRegressor(regressor=pipe2,\
  transformer=StandardScaler())

ttr2.fit(X_train, y_train)

pred = ttr2.predict(X_test)

preddf = pd.DataFrame(pred, columns=['prediction'],
  index=X_test.index).join(X_test).join(y_test)

preddf['resid'] = preddf.avgtemp-preddf.prediction

preddf.resid.agg(['mean','median','skew','kurtosis'])

# plot the residuals
plt.hist(preddf.resid, color="blue")
plt.axvline(preddf.resid.mean(), color='red', linestyle='dashed', linewidth=1)
plt.title("Histogram of Residuals for Temperature Model")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.show()

# plot predictions against the residuals
plt.scatter(preddf.prediction, preddf.resid, color="blue")
plt.axhline(0, color='red', linestyle='dashed', linewidth=1)
plt.title("Scatterplot of Predictions and Residuals")
plt.xlabel("Predicted Temperature")
plt.ylabel("Residuals")
plt.xlim(-20,40)
plt.ylim(-27,10)
plt.show()

scores = cross_validate(ttr2, X=X_train, y=y_train,
  cv=kf, scoring=('r2', 'neg_mean_absolute_error'), n_jobs=1)

scores['test_r2'].mean(), scores['test_neg_mean_absolute_error'].mean()



