# import pandas, numpy, and matplotlib
import pandas as pd
from feature_engine import transformation as vt
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from scipy import stats
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format

covidtotals = pd.read_csv("data/covidtotals.csv")

feature_cols = ['location','population',
    'aged_65_older','diabetes_prevalence','region']
covidtotals = covidtotals[['total_cases'] + feature_cols].dropna()

# separate into train and test sets
X_train, X_test, y_train, y_test =  \
  train_test_split(covidtotals[feature_cols],\
  covidtotals[['total_cases']], test_size=0.3, random_state=0)

# show a histogram of total cases
y_train.total_cases.skew()
plt.hist(y_train.total_cases/1000000)
plt.title("Total Covid Cases (in millions)")
plt.xlabel('Cases')
plt.ylabel("Number of Countries")
plt.show()

# do a log transformation on total cases
tf = vt.LogTransformer(variables = ['total_cases'])
y_train_tf = tf.fit_transform(y_train)

y_train_tf.total_cases.skew()
plt.hist(y_train_tf.total_cases)
plt.title("Total Covid Cases (log transformation)")
plt.xlabel('Cases')
plt.ylabel("Number of Countries")
plt.show()


# do a Box Cox transformation on total cases
tf = vt.BoxCoxTransformer(variables = ['total_cases'])
y_train_tf = tf.fit_transform(y_train)

y_train_tf.total_cases.skew()
plt.hist(y_train_tf.total_cases)
plt.title("Total Covid Cases (Box Cox transformation)")
plt.xlabel('Cases')
plt.ylabel("Number of Countries")
plt.show()

stats.boxcox(y_train.total_cases)[1]
