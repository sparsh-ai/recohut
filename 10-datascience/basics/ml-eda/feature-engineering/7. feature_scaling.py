# import pandas, numpy, and matplotlib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

covidtotals = pd.read_csv("data/covidtotals.csv")
feature_cols = ['population','total_deaths',
    'aged_65_older','diabetes_prevalence']
covidtotals = covidtotals[['total_cases'] + feature_cols].dropna()

# separate into train and test sets
X_train, X_test, y_train, y_test =  \
  train_test_split(covidtotals[feature_cols],\
  covidtotals[['total_cases']], test_size=0.3, random_state=0)

# do min-max scaling
scaler = MinMaxScaler()
X_train_mms = pd.DataFrame(scaler.fit_transform(X_train),
  columns=X_train.columns, index=X_train.index)
X_train_mms.describe()


# do standard scaling
scaler = StandardScaler()
X_train_ss = \
  pd.DataFrame(scaler.fit_transform(X_train),
  columns=X_train.columns, index=X_train.index)
X_train_ss.describe()

# use the robust scaler
scaler = RobustScaler()
X_train_rs = pd.DataFrame(scaler.fit_transform(X_train),
  columns=X_train.columns, index=X_train.index)
X_train_rs.describe()
