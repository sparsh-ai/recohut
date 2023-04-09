# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from feature_engine.encoding import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.2f}'.format

# load the NLS data
nls97compba = pd.read_csv("data/nls97compba.csv")

feature_cols = ['satverbal','satmath','gpascience',
  'gpaenglish','gpamath','gpaoverall','gender',
  'motherhighgrade',  'fatherhighgrade','parentincome']

# separate NLS data into train and test datasets
X_train, X_test, y_train, y_test =  \
  train_test_split(nls97compba[feature_cols],\
  nls97compba[['completedba']], test_size=0.3,
  random_state=0)

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


# instantiate a pca object and fit the model
pca = PCA(n_components=5)
pca.fit(X_train_enc)

# take a closer look at the components
pd.DataFrame(pca.components_,
  columns=X_train_enc.columns).T

pca.explained_variance_ratio_
np.cumsum(pca.explained_variance_ratio_)

# create numpy arrays transformed values based on components
X_train_pca = pca.transform(X_train_enc)
X_train_pca.shape
np.round(X_train_pca[0:6],2)
X_test_pca = pca.transform(X_test_enc)

# evaluate the accuracy of the random forest classifier model
rfc = RandomForestClassifier(n_estimators=100, 
  max_depth=2, n_jobs=-1, random_state=0)

rfc.fit(X_train_pca, y_train.values.ravel())
y_pred = rfc.predict(X_test_pca)

accuracy_score(y_test, y_pred)
