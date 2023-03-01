# import pandas, numpy, and matplotlib
import pandas as pd
from feature_engine.encoding import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
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
treesel = RFE(estimator=rfc, n_features_to_select=5)
treesel.fit(X_train_enc, y_train.values.ravel())
selcols = X_train_enc.columns[treesel.get_support()]
selcols
pd.DataFrame({'ranking': treesel.ranking_,
  'feature': X_train_enc.columns},
   columns=['feature','ranking']).\
   sort_values(['ranking'], ascending=True)
   
# evaluate the accuracy of the random forest classifier model
rfc.fit(treesel.transform(X_train_enc), y_train.values.ravel())
y_pred = rfc.predict(treesel.transform(X_test_enc))

confusion = pd.DataFrame(y_pred, columns=['pred'],
  index=y_test.index).\
  join(y_test)
confusion.loc[confusion.pred==confusion.completedba].shape[0]\
  /confusion.shape[0]

accuracy_score(y_test, y_pred)
