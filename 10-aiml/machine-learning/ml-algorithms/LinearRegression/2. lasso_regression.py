# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.compose import TransformedTargetRegressor
from sklearn.feature_selection import RFE
from sklearn.impute import KNNImputer
from sklearn.model_selection import cross_validate, KFold, GridSearchCV
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

fftaxrate14 = pd.read_csv("data/fossilfueltaxrate14.csv")
fftaxrate14.set_index('countrycode', inplace=True)

# setup the features and target
num_cols = ['fuel_income_dependence','national_income_per_cap',
  'VAT_Rate',  'gov_debt_per_gdp','polity','goveffect',
  'democracy_index']
dummy_cols = ['democracy_polity','autocracy_polity','democracy',
  'nat_oil_comp','nat_oil_comp_state']
spec_cols = ['motorization_rate']

target = fftaxrate14[['gas_tax_imp']]
features = fftaxrate14[num_cols + dummy_cols + spec_cols]

X_train, X_test, y_train, y_test =  \
  train_test_split(features,\
  target, test_size=0.2, random_state=0)
      
# setup pipelines for column transformation
standtrans = make_pipeline(OutlierTrans(2), SimpleImputer(strategy="median"),
  StandardScaler())
cattrans = make_pipeline(SimpleImputer(strategy="most_frequent"))
spectrans = make_pipeline(OutlierTrans(2), StandardScaler())
coltrans = ColumnTransformer(
  transformers=[
    ("stand", standtrans, num_cols),
    ("cat", cattrans, dummy_cols),
    ("spec", spectrans, spec_cols)
  ]
)

# add feature selection and a linear model to the pipeline and look at the parameter estimates
lasso = Lasso(alpha=0.1,fit_intercept=False)

pipe1 = make_pipeline(coltrans, KNNImputer(n_neighbors=5), lasso)

ttr=TransformedTargetRegressor(regressor=pipe1,transformer=StandardScaler())

ttr.fit(X_train, y_train)

coefs = ttr.regressor_['lasso'].coef_
np.column_stack((coefs.ravel(), num_cols + dummy_cols + spec_cols))

# get predictions and residuals
pred = ttr.predict(X_test)

preddf = pd.DataFrame(pred, columns=['prediction'],
  index=X_test.index).join(X_test).join(y_test)

preddf['resid'] = preddf.gas_tax_imp-preddf.prediction

preddf.resid.agg(['mean','median','skew','kurtosis'])

# generate summary model evaluation statistics
print("Mean Absolute Error: %.2f, R-squared: %.2f" % 
  (skmet.mean_absolute_error(y_test, pred),
  skmet.r2_score(y_test, pred)))


# plot the residuals
plt.hist(preddf.resid, color="blue", bins=np.arange(-0.5,1.0,0.25))
plt.axvline(preddf.resid.mean(), color='red', linestyle='dashed', linewidth=1)
plt.title("Histogram of Residuals for Gax Tax Model")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
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

kf = KFold(n_splits=4, shuffle=True, random_state=0)

scores = cross_validate(ttr, X=X_train, y=y_train,
  cv=kf, scoring=('r2', 'neg_mean_absolute_error'), n_jobs=1)


print("Mean Absolute Error: %.2f, R-squared: %.2f" % 
  (scores['test_neg_mean_absolute_error'].mean(),
  scores['test_r2'].mean()))


# do a grid search to find the best value of alpha
lasso = Lasso()

pipe1 = make_pipeline(coltrans, KNNImputer(n_neighbors=5), lasso)

lasso_params = {'regressor__lasso__alpha': np.arange(0.05, 1, 0.05)}

gs = GridSearchCV(ttr,param_grid=lasso_params, cv=5)
gs.fit(X_train, y_train)

gs.best_params_
gs.best_score_


