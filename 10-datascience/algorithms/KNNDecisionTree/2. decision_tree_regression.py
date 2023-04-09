# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectFromModel
import matplotlib.pyplot as plt

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans


pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

# load the land temperatures data
un_income_gap = pd.read_csv("data/un_income_gap.csv")
un_income_gap.set_index('country', inplace=True)
un_income_gap['incomeratio'] = \
  un_income_gap.femaleincomepercapita / \
    un_income_gap.maleincomepercapita
un_income_gap['educratio'] = \
  un_income_gap.femaleyearseducation / \
     un_income_gap.maleyearseducation
un_income_gap['laborforcepartratio'] = \
  un_income_gap.femalelaborforceparticipation / \
     un_income_gap.malelaborforceparticipation
un_income_gap['humandevratio'] = \
  un_income_gap.femalehumandevelopment / \
     un_income_gap.malehumandevelopment
un_income_gap.dropna(subset=['incomeratio'], inplace=True)


num_cols = ['educratio','laborforcepartratio','humandevratio',
  'genderinequality','maternalmortaility',
  'adolescentbirthrate', 'femaleperparliament','incomepercapita']

gap_sub = un_income_gap[['incomeratio'] + num_cols]

# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(gap_sub[num_cols],\
  gap_sub[['incomeratio']], test_size=0.2, random_state=0)

# construct a pipeline with preprocessing and knn model
dtreg_example = DecisionTreeRegressor(min_samples_leaf=5,
  max_depth=3)

pipe0 = make_pipeline(OutlierTrans(3),
  SimpleImputer(strategy="median"))

X_train_imp = pipe0.fit_transform(X_train)

dtreg_example.fit(X_train_imp, y_train)

plot_tree(dtreg_example, feature_names=X_train.columns,
  label="root", fontsize=10)

# construct a decision tree model
dtreg = DecisionTreeRegressor()

feature_sel = SelectFromModel(LinearRegression(),
  threshold="0.8*mean")

pipe1 = make_pipeline(OutlierTrans(3),
  SimpleImputer(strategy="median"),
  feature_sel, dtreg)

dtreg_params={
 "decisiontreeregressor__max_depth": np.arange(2, 20),
 "decisiontreeregressor__min_samples_leaf": np.arange(5, 11)
}

rs = RandomizedSearchCV(pipe1, dtreg_params, cv=4, n_iter=20,
  scoring='neg_mean_absolute_error', random_state=1)
rs.fit(X_train, y_train.values.ravel())

rs.best_params_
rs.best_score_

# construct a random forest model
rfreg = RandomForestRegressor()

rfreg_params = {
 'randomforestregressor__max_depth': np.arange(2, 20),
 'randomforestregressor__max_features': ['auto', 'sqrt'],
 'randomforestregressor__min_samples_leaf':  np.arange(5, 11)
}

pipe2 = make_pipeline(OutlierTrans(3), 
  SimpleImputer(strategy="median"),
  feature_sel, rfreg)

rs = RandomizedSearchCV(pipe2, rfreg_params, cv=4, n_iter=20,
  scoring='neg_mean_absolute_error', random_state=1)
rs.fit(X_train, y_train.values.ravel())

rs.best_params_
rs.best_score_

# get predictions and residuals
pred = rs.predict(X_test)


preddf = pd.DataFrame(pred, columns=['prediction'],
  index=X_test.index).join(X_test).join(y_test)

preddf['resid'] = preddf.incomeratio-preddf.prediction


plt.hist(preddf.resid, color="blue", bins=5)
plt.axvline(preddf.resid.mean(), color='red', linestyle='dashed', linewidth=1)
plt.title("Histogram of Residuals for Income Ratio")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.xlim()
plt.show()


plt.scatter(preddf.prediction, preddf.resid, color="blue")
plt.axhline(0, color='red', linestyle='dashed', linewidth=1)
plt.title("Scatterplot of Predictions and Residuals")
plt.xlabel("Predicted Income Ratio")
plt.ylabel("Residuals")
plt.show()

preddf.loc[np.abs(preddf.resid)>=0.12,
  ['incomeratio','prediction','resid',
  'laborforcepartratio', 'humandevratio']].T
