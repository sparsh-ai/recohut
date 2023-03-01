# import pandas, numpy, and matplotlib
import pandas as pd
from feature_engine.encoding import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.0f}'.format
nls97compba = pd.read_csv("data/nls97compba.csv")

feature_cols = ['satverbal','satmath','gpascience',
  'gpaenglish','gpamath','gpaoverall','gender','motherhighgrade',
  'fatherhighgrade','parentincome']

# separate NLS data into train and test datasets
X_train, X_test, y_train, y_test =  \
  train_test_split(nls97compba[feature_cols],\
  nls97compba[['completedba']], test_size=0.3, random_state=0)
      
# do one hot encoding and scaling
ohe = OneHotEncoder(drop_last=True, variables=['gender'])
ohe.fit(X_train)
X_train_enc, X_test_enc = \
  ohe.transform(X_train), ohe.transform(X_test)

scaler = StandardScaler()
standcols = X_train_enc.iloc[:,:-1].columns
scaler.fit(X_train_enc[standcols])
X_train_enc = \
  pd.DataFrame(scaler.transform(X_train_enc[standcols]),
  columns=standcols, index=X_train_enc.index).\
  join(X_train_enc[['gender_Female']])
X_test_enc = \
  pd.DataFrame(scaler.transform(X_test_enc[standcols]),
  columns=standcols, index=X_test_enc.index).\
  join(X_test_enc[['gender_Female']])

# logistic regression for feature importance
lr = LogisticRegression(C=1, penalty="l1", solver='liblinear')
regsel = SelectFromModel(lr, max_features=5)
regsel.fit(X_train_enc, y_train.values.ravel())
selcols = X_train_enc.columns[regsel.get_support()]
selcols

lr.fit(regsel.transform(X_train_enc), y_train.values.ravel())
y_pred = lr.predict(regsel.transform(X_test_enc))

accuracy_score(y_test, y_pred)

# random forest classification for feature importance
rfc = RandomForestClassifier(n_estimators=100, max_depth=2, 
  n_jobs=-1, random_state=0)

rfcsel = SelectFromModel(rfc, max_features=5)
rfcsel.fit(X_train_enc, y_train.values.ravel())
selcols = X_train_enc.columns[rfcsel.get_support()]
selcols

rfc.fit(rfcsel.transform(X_train_enc), y_train.values.ravel())
y_pred = rfc.predict(rfcsel.transform(X_test_enc))

accuracy_score(y_test, y_pred)
