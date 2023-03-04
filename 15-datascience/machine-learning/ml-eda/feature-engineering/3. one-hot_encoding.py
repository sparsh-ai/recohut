# import pandas, numpy, and matplotlib
import pandas as pd
from feature_engine.encoding import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)


feature_cols = ['gender','maritalstatus','colenroct99']
nls97demo = nls97[['wageincome'] + feature_cols].dropna()

# separate NLS data into train and test datasets
X_demo_train, X_demo_test, y_demo_train, y_demo_test =  \
  train_test_split(nls97demo[feature_cols],\
  nls97demo[['wageincome']], test_size=0.3, random_state=0)

# use get dummies to create dummies features
pd.get_dummies(X_demo_train, columns=['gender','maritalstatus']).head(2).T
pd.get_dummies(X_demo_train, columns=['gender','maritalstatus'],
  drop_first=True).head(2).T

# use the one hot encoder to create encoded features for gender and marital status
ohe = OneHotEncoder(drop_last=True, variables=['gender','maritalstatus'])
ohe.fit(X_demo_train)
X_demo_train_ohe = ohe.transform(X_demo_train)
X_demo_test_ohe = ohe.transform(X_demo_test)
X_demo_train_ohe.filter(regex='gen|mar', axis="columns").head(2).T


# use the ordinal encoder for college enrollment
X_demo_train.colenroct99.unique()
X_demo_train.head()

oe = OrdinalEncoder(categories=\
  [X_demo_train.colenroct99.unique()])
colenr_enc = \
  pd.DataFrame(oe.fit_transform(X_demo_train[['colenroct99']]),
    columns=['colenroct99'], index=X_demo_train.index)
X_demo_train_enc = \
  X_demo_train[['gender','maritalstatus']].\
  join(colenr_enc)
X_demo_train_enc.head()
X_demo_train.colenroct99.value_counts().sort_index()
X_demo_train_enc.colenroct99.value_counts().sort_index()

