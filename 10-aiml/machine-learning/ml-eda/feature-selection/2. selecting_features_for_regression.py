# import necessary libraries
import pandas as pd
from feature_engine.encoding import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_regression,\
  mutual_info_regression
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.3f}'.format

# load the NLS data
nls97wages = pd.read_csv("data/nls97wages.csv")

feature_cols = ['satverbal','satmath','gpascience',
  'gpaenglish','gpamath','gpaoverall','gender','motherhighgrade',
  'fatherhighgrade','parentincome','completedba']

X_train, X_test, y_train, y_test =  \
  train_test_split(nls97wages[feature_cols],\
  nls97wages[['wageincome']], test_size=0.3, random_state=0)
      
# encode and scale the data
ohe = OneHotEncoder(drop_last=True, variables=['gender'])
X_train_enc = ohe.fit_transform(X_train)
scaler = StandardScaler()
standcols = X_train_enc.iloc[:,:-1].columns
X_train_enc = \
  pd.DataFrame(scaler.fit_transform(X_train_enc[standcols]),
  columns=standcols, index=X_train_enc.index).\
  join(X_train_enc[['gender_Male']])

y_train = \
  pd.DataFrame(scaler.fit_transform(y_train),
  columns=['wageincome'], index=y_train.index)

# select 5 best features for predicting wage income
ksel = SelectKBest(score_func=f_regression, k=5)
ksel.fit(X_train_enc, y_train.values.ravel())
selcols = X_train_enc.columns[ksel.get_support()]
selcols
pd.DataFrame({'score': ksel.scores_,
  'feature': X_train_enc.columns},
   columns=['feature','score']).\
   sort_values(['score'], ascending=False)

# select the 5 best features using mutual information
from functools import partial
ksel = SelectKBest(score_func=\
  partial(mutual_info_regression, random_state=0),
  k=5)
ksel.fit(X_train_enc, y_train.values.ravel())
selcols = X_train_enc.columns[ksel.get_support()]
selcols
pd.DataFrame({'score': ksel.scores_,
  'feature': X_train_enc.columns},
   columns=['feature','score']).\
   sort_values(['score'], ascending=False)

