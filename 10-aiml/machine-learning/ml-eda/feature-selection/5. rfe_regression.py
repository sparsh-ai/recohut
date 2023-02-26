# import pandas, numpy, and matplotlib
import pandas as pd
from feature_engine.encoding import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.3f}'.format

# load the NLS data
nls97wages = pd.read_csv("data/nls97wages.csv")

feature_cols = ['satverbal','satmath','gpascience',
  'gpaenglish','gpamath','gpaoverall','motherhighgrade',
  'fatherhighgrade','parentincome','gender','completedba']

X_train, X_test, y_train, y_test =  \
  train_test_split(nls97wages[feature_cols],\
  nls97wages[['weeklywage']], test_size=0.3, random_state=0)
      
# standardize and scale the data      
ohe = OneHotEncoder(drop_last=True, variables=['gender'])
ohe.fit(X_train)
X_train_enc, X_test_enc = \
  ohe.transform(X_train), ohe.transform(X_test)

scaler = StandardScaler()
standcols = feature_cols[:-2]
scaler.fit(X_train_enc[standcols])
X_train_enc = \
  pd.DataFrame(scaler.transform(X_train_enc[standcols]),
  columns=standcols, index=X_train_enc.index).\
  join(X_train_enc[['gender_Male','completedba']])
X_test_enc = \
  pd.DataFrame(scaler.transform(X_test_enc[standcols]),
  columns=standcols, index=X_test_enc.index).\
  join(X_test_enc[['gender_Male','completedba']])

scaler.fit(y_train)
y_train, y_test = \
  pd.DataFrame(scaler.transform(y_train),
  columns=['weeklywage'], index=y_train.index),\
  pd.DataFrame(scaler.transform(y_test),
  columns=['weeklywage'], index=y_test.index)


# use decision trees for recursive feature elimination
rfr = RandomForestRegressor(max_depth=2)

treesel = RFE(estimator=rfr, n_features_to_select=5)
treesel.fit(X_train_enc, y_train.values.ravel())
selcols = X_train_enc.columns[treesel.get_support()]
selcols
pd.DataFrame({'ranking': treesel.ranking_,
  'feature': X_train_enc.columns},
   columns=['feature','ranking']).\
   sort_values(['ranking'], ascending=True)
   
rfr.fit(treesel.transform(X_train_enc), y_train.values.ravel())
rfr.score(treesel.transform(X_train_enc), y_train.values.ravel())
rfr.score(treesel.transform(X_test_enc), y_test)


# use linear regression for recursive feature elimination
lr = LinearRegression()

lrsel = RFE(estimator=lr, n_features_to_select=5)
lrsel.fit(X_train_enc, y_train)
selcols = X_train_enc.columns[lrsel.get_support()]
selcols
pd.DataFrame({'ranking': lrsel.ranking_,
  'feature': X_train_enc.columns},
   columns=['feature','ranking']).\
   sort_values(['ranking'], ascending=True)
   
lr.fit(lrsel.transform(X_train_enc), y_train)
lr.score(lrsel.transform(X_train_enc), y_train)
lr.score(lrsel.transform(X_test_enc), y_test)


