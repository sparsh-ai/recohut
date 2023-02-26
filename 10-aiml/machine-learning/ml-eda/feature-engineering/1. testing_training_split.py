# import pandas, numpy, and matplotlib
import pandas as pd
from sklearn.model_selection import train_test_split
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 25)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

feature_cols = ['satverbal','satmath','gpascience',
  'gpaenglish','gpamath','gpaoverall']

# separate NLS data into train and test datasets
X_train, X_test, y_train, y_test =  \
  train_test_split(nls97[feature_cols],\
  nls97[['wageincome']], test_size=0.3, random_state=0)

# remove a feature highly correlated with another
nls97.shape[0]
X_train.info()
y_train.info()
X_test.info()
y_test.info()

