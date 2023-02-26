# import pandas and feature_engine
import pandas as pd
import feature_engine.selection as fesel
from sklearn.model_selection import train_test_split
pd.set_option('display.width', 80)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 25)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)
ltpoland = pd.read_csv("data/ltpoland.csv")
ltpoland.set_index("station", inplace=True)
ltpoland.dropna(inplace=True)

feature_cols = ['satverbal','satmath','gpascience',
  'gpaenglish','gpamath','gpaoverall']

# separate NLS data into train and test datasets
X_train, X_test, y_train, y_test =  \
  train_test_split(nls97[feature_cols],\
  nls97[['wageincome']], test_size=0.3, random_state=0)

# remove a feature highly correlated with another
X_train.corr()
tr = fesel.DropCorrelatedFeatures(variables=None, method='pearson', threshold=0.75)
tr.fit(X_train)
X_train_tr = tr.transform(X_train)
X_test_tr = tr.transform(X_test)
X_train_tr.info()

feature_cols = ['year','month','latabs','latitude','elevation',
  'longitude','country']

# separate temperature data into train and test datasets
X_train, X_test, y_train, y_test =  \
  train_test_split(ltpoland[feature_cols],\
  ltpoland[['temperature']], test_size=0.3, random_state=0)
X_train.sample(5, random_state=99)
X_train.year.value_counts()
X_train.country.value_counts()
(X_train.latitude!=X_train.latabs).sum()

# drop features with same values throughout dataset
tr = fesel.DropConstantFeatures()
tr.fit(X_train)
X_train_tr = tr.transform(X_train)
X_test_tr = tr.transform(X_test)
X_train_tr.head()

# drop features that have the same values as another feature
tr = fesel.DropDuplicateFeatures()
tr.fit(X_train_tr)
X_train_tr = tr.transform(X_train_tr)
X_train_tr.head()

