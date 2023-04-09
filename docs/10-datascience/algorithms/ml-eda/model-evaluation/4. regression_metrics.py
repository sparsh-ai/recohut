# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import sklearn.metrics as skmet
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
      
# scale the data  
scaler = StandardScaler()
scaler.fit(X_train)
X_train = \
  pd.DataFrame(scaler.transform(X_train),
  columns=feature_cols, index=X_train.index)
X_test = \
  pd.DataFrame(scaler.transform(X_test),
  columns=feature_cols, index=X_test.index)

scaler.fit(y_train)
y_train, y_test = \
  pd.DataFrame(scaler.transform(y_train),
  columns=['avgtemp'], index=y_train.index),\
  pd.DataFrame(scaler.transform(y_test),
  columns=['avgtemp'], index=y_test.index)


# use linear regression for recursive feature elimination
lr = LinearRegression()
lr.fit(X_train, y_train)
np.column_stack((lr.coef_.ravel(),X_test.columns.values))

# get predictions and residuals
pred = lr.predict(X_test)

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
plt.show()

# generate summary model evaluation statistics
mse = skmet.mean_squared_error(y_test, pred)
mse
rmse = skmet.mean_squared_error(y_test, pred, squared=False)
rmse
mae = skmet.mean_absolute_error(y_test, pred)
mae
r2 = skmet.r2_score(y_test, pred)
r2
   
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

mae = skmet.mean_absolute_error(y_test, pred)
mae
r2 = skmet.r2_score(y_test, pred)
r2

preddf = pd.DataFrame(pred, columns=['prediction'],
  index=X_test.index).join(X_test).join(y_test)
preddf['resid'] = preddf.avgtemp-preddf.prediction

# plot predictions against the residuals
plt.scatter(preddf.prediction, preddf.resid, color="blue")
plt.axhline(0, color='red', linestyle='dashed', linewidth=1)
plt.title("Scatterplot of Predictions and Residuals with KNN Model")
plt.xlabel("Predicted Temperature")
plt.ylabel("Residuals")
plt.show()

