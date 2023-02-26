# import pandas, numpy, and matplotlib
import pandas as pd
from feature_engine.encoding import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import ExhaustiveFeatureSelector
from sklearn.metrics import accuracy_score
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.0f}'.format

# load the NLS data
nls97compba = pd.read_csv("data/nls97compba.csv")

feature_cols = ['satverbal','satmath','gpascience',
  'gpaenglish','gpamath','gpaoverall','gender','motherhighgrade',
  'fatherhighgrade','parentincome']

# separate NLS data into train and test datasets
X_train, X_test, y_train, y_test =  \
  train_test_split(nls97compba[feature_cols],\
  nls97compba[['completedba']], test_size=0.3, random_state=0)

# encode the data      
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


# Build RF classifier to use in feature selection
rfc = RandomForestClassifier(n_estimators=100, max_depth=2, 
  n_jobs=-1, random_state=0)

# Build exhaustive feature selection
efs = ExhaustiveFeatureSelector(rfc, max_features=5,
  min_features=1, scoring='accuracy', 
  print_progress=True, cv=5)

# Perform EFS
efs.fit(X_train_enc, y_train.values.ravel())
efs.best_feature_names_

# evaluate the accuracy of the random forest classifier model
X_train_efs = efs.transform(X_train_enc)
X_test_efs = efs.transform(X_test_enc)

rfc.fit(X_train_efs, y_train.values.ravel())
y_pred = rfc.predict(X_test_efs)

confusion = pd.DataFrame(y_pred, columns=['pred'],
  index=y_test.index).\
  join(y_test)
confusion.loc[confusion.pred==confusion.completedba].shape[0]\
  /confusion.shape[0]

accuracy_score(y_test, y_pred)

# build logistic classifier and redo the feature selection
lr = LogisticRegression(solver='liblinear')
efs = ExhaustiveFeatureSelector(lr, max_features=5,
  min_features=1, scoring='accuracy', 
  print_progress=True, cv=5)
efs.fit(X_train_enc, y_train.values.ravel())
efs.best_feature_names_


# evaluate the accuracy of the logistic model
X_train_efs = efs.transform(X_train_enc)
X_test_efs = efs.transform(X_test_enc)

lr.fit(X_train_efs, y_train.values.ravel())
y_pred = lr.predict(X_test_efs)

accuracy_score(y_test, y_pred)

