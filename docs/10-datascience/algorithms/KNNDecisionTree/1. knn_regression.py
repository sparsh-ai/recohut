# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectFromModel
import seaborn as sns
import matplotlib.pyplot as plt

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 12)
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

gap_sub.head()

gap_sub.\
  agg(['count','min','median','max']).T
  
# show a heatmap of correlations
corrmatrix = gap_sub.corr(method="pearson")
corrmatrix

sns.heatmap(corrmatrix, xticklabels=corrmatrix.columns,
  yticklabels=corrmatrix.columns, cmap="coolwarm")
plt.title('Heat Map of Correlation Matrix')
plt.tight_layout()
plt.show()
  
# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(gap_sub[num_cols],\
  gap_sub[['incomeratio']], test_size=0.2, random_state=0)


# construct a pipeline with preprocessing, feature selection, and knn model
knnreg = KNeighborsRegressor()

feature_sel = SelectFromModel(LinearRegression(), threshold="0.8*mean")

pipe1 = make_pipeline(OutlierTrans(3), \
  SimpleImputer(strategy="median"), StandardScaler(), \
  feature_sel, knnreg)

knnreg_params = {
 'kneighborsregressor__n_neighbors': \
     np.arange(3, 21, 2),
 'kneighborsregressor__metric': \
     ['euclidean','manhattan','minkowski']
}

# do a randmoized parameter search
rs = RandomizedSearchCV(pipe1, knnreg_params, cv=4, n_iter=20, \
  scoring='neg_mean_absolute_error', random_state=1)
rs.fit(X_train, y_train)

rs.best_params_
rs.best_score_

selected = rs.best_estimator_['selectfrommodel'].get_support()
np.array(num_cols)[selected]

rs.best_estimator_['selectfrommodel'].\
  get_feature_names_out(np.array(num_cols))

results = \
  pd.DataFrame(rs.cv_results_['mean_test_score'], \
    columns=['meanscore']).\
  join(pd.DataFrame(rs.cv_results_['params'])).\
  sort_values(['meanscore'], ascending=False)

results.head(3).T

# get predictions and residuals
pred = rs.predict(X_test)

preddf = pd.DataFrame(pred, columns=['prediction'],
  index=X_test.index).join(X_test).join(y_test)

preddf['resid'] = preddf.incomeratio-preddf.prediction

preddf.resid.agg(['mean','median','skew','kurtosis'])

plt.hist(preddf.resid, color="blue", bins=5)
plt.axvline(preddf.resid.mean(), color='red', linestyle='dashed', linewidth=1)
plt.title("Histogram of Residuals for Income Ratio Model")
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

preddf.loc[np.abs(preddf.resid)>=0.1,
  ['incomeratio','prediction','resid','laborforcepartratio',
  'humandevratio']].T
