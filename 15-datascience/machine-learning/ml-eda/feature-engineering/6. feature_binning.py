# import pandas, numpy, and matplotlib
import pandas as pd
from feature_engine.discretisation import EqualFrequencyDiscretiser as efd
from feature_engine.discretisation import EqualWidthDiscretiser as ewd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import KBinsDiscretizer
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.3f}'.format

covidtotals = pd.read_csv("data/covidtotals.csv")

feature_cols = ['location','population',
    'aged_65_older','diabetes_prevalence','region']
covidtotals = covidtotals[['total_cases'] + feature_cols].dropna()

# Separate into train and test sets
X_train, X_test, y_train, y_test =  \
  train_test_split(covidtotals[feature_cols],\
  covidtotals[['total_cases']], test_size=0.3, random_state=0)

# use qcut for bins
y_train['total_cases_group'] = pd.qcut(y_train.total_cases, q=10, labels=[0,1,2,3,4,5,6,7,8,9])
y_train.total_cases_group.value_counts().sort_index()

# set up function to run the transform
def runtransform(bt, dftrain, dftest):
  bt.fit(dftrain)
  train_bins = bt.transform(dftrain)
  test_bins = bt.transform(dftest)
  return train_bins, test_bins

# set up bins based on equal frequency
y_train.drop(['total_cases_group'], axis=1, inplace=True)
bintransformer = efd(q=10, variables=['total_cases'])
y_train_bins, y_test_bins = runtransform(bintransformer, y_train, y_test)
y_train_bins.total_cases.value_counts().sort_index()

# set up bins based on equal width
bintransformer = ewd(bins=10, variables=['total_cases'])
y_train_bins, y_test_bins = runtransform(bintransformer, y_train, y_test)
y_train_bins.total_cases.value_counts().sort_index()

pd.options.display.float_format = '{:,.0f}'.format
y_train_bins = y_train_bins.\
  rename(columns={'total_cases':'total_cases_group'}).\
  join(y_train)
y_train_bins.groupby("total_cases_group")["total_cases"].agg(['min','max'])

# use k means clustering
kbins = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='kmeans')
y_train_bins = \
  pd.DataFrame(kbins.fit_transform(y_train),
  columns=['total_cases'])
y_train_bins.total_cases.value_counts().sort_index()


y_train.total_cases.agg(['skew','kurtosis'])
y_train_bins.total_cases.agg(['skew','kurtosis'])
