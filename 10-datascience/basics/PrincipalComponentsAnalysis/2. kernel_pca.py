# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.decomposition import KernelPCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
import seaborn as sns
import matplotlib.pyplot as plt

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.3f}'.format

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

num_cols = ['educratio','laborforcepartratio',
  'humandevratio','genderinequality',
  'maternalmortaility','adolescentbirthrate',
  'femaleperparliament','incomepercapita']

gap_sub = un_income_gap[['incomeratio'] + num_cols]

gap_sub.\
  agg(['count','min','median','max']).T
  
corrmatrix = gap_sub.corr(method="pearson")

sns.heatmap(corrmatrix, xticklabels=corrmatrix.columns,
  yticklabels=corrmatrix.columns, cmap="coolwarm")
plt.title('Heat Map of Correlation Matrix')
plt.tight_layout()
plt.show()
  

# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(gap_sub[num_cols],\
  gap_sub[['incomeratio']], test_size=0.2, random_state=0)

# instantiate a pca object and fit the model
kpca = KernelPCA()

rfreg = RandomForestRegressor()

pipe1 = make_pipeline(OutlierTrans(2),
  SimpleImputer(strategy="median"), MinMaxScaler(),
  kpca, rfreg)
 
rfreg_params = {
 'kernelpca__n_components':
    randint(2, 9),
 'kernelpca__gamma':
     np.linspace(0.03, 0.3, 10),
 'kernelpca__kernel':
     ['linear', 'poly', 'rbf', 
      'sigmoid', 'cosine'],
 'randomforestregressor__max_depth':
     randint(2, 20),
 'randomforestregressor__min_samples_leaf':
     randint(5, 11)
}

rs = RandomizedSearchCV(pipe1, rfreg_params,
  cv=4, n_iter=40,
  scoring='neg_mean_absolute_error',
  random_state=1)
rs.fit(X_train, y_train.values.ravel())

rs.best_params_
rs.best_score_

results = \
  pd.DataFrame(rs.cv_results_['mean_test_score'], \
    columns=['meanscore']).\
  join(pd.DataFrame(rs.cv_results_['params'])).\
  sort_values(['meanscore'], ascending=False)

results.iloc[1:3].T
