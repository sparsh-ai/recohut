# import necessary libraries
import pandas as pd
from feature_engine.encoding import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from mlxtend.feature_selection import SequentialFeatureSelector
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
X_train_enc = ohe.fit_transform(X_train)
scaler = StandardScaler()
standcols = X_train_enc.iloc[:,:-1].columns
X_train_enc = \
  pd.DataFrame(scaler.fit_transform(X_train_enc[standcols]),
  columns=standcols, index=X_train_enc.index).\
  join(X_train_enc[['gender_Female']])

# Build RF classifier to use in feature selection
rfc = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=0)

# Build step forward feature selection
sfs = SequentialFeatureSelector(rfc, k_features=5,
  forward=True, floating=False, verbose=2,
  scoring='accuracy', cv=5)

# Perform SFFS
sfs.fit(X_train_enc, y_train.values.ravel())
selcols = X_train_enc.columns[list(sfs.k_feature_idx_)]
selcols

# Build step forward feature selection
rfc = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=0)
sfs = SequentialFeatureSelector(rfc, k_features=5,
  forward=False, floating=False, verbose=2,
  scoring='accuracy', cv=5)

# Perform SFFS
sfs.fit(X_train_enc, y_train.values.ravel())
selcols = X_train_enc.columns[list(sfs.k_feature_idx_)]
selcols

