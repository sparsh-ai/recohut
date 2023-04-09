# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectFromModel
from scipy.stats import randint
from scipy.stats import uniform
import matplotlib.pyplot as plt
import seaborn as sns

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans


pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

# load the land temperatures data
housing = pd.read_csv("data/kc_house_data.csv")
housing.set_index('id', inplace=True)

num_cols = ['bedrooms','bathrooms','sqft_living','sqft_lot',
  'floors','view','condition','sqft_above','sqft_basement',
  'yr_built','yr_renovated','sqft_living15','sqft_lot15']
cat_cols = ['waterfront']

housing[['price'] + num_cols + cat_cols].\
  head(3).T

housing[['price'] + num_cols].\
  agg(['count','min','median','max']).T
  

plt.hist(housing.price/1000)
plt.title("Housing Price (in thousands)")
plt.xlabel('Price')
plt.ylabel("Frequency")
plt.show()

housing['price_log'] = np.log(housing['price'])

plt.hist(housing.price_log)
plt.title("Housing Price Log")
plt.xlabel('Price Log')
plt.ylabel("Frequency")
plt.show()

housing[['price','price_log']].agg(['kurtosis','skew'])

# look at some correlations
corrmatrix = housing[['price_log'] + num_cols].\
   corr(method="pearson")

sns.heatmap(corrmatrix, xticklabels=corrmatrix.columns,
  yticklabels=corrmatrix.columns, cmap="coolwarm")
plt.title('Heat Map of Correlation Matrix')
plt.tight_layout()
plt.show()


# generate some summary statistics
target = housing[['price_log']]
features = housing[num_cols + cat_cols]

X_train, X_test, y_train, y_test =  \
  train_test_split(features,\
  target, test_size=0.2, random_state=0)
      
# setup pipelines for column transformation
ohe = OneHotEncoder(drop='first', sparse=False)

standtrans = make_pipeline(OutlierTrans(2),
  SimpleImputer(strategy="median"),
  MinMaxScaler())
cattrans = make_pipeline(ohe)
coltrans = ColumnTransformer(
  transformers=[
    ("stand", standtrans, num_cols),
    ("cat", cattrans, cat_cols)
  ]
)

# construct a gradient boosted regressor
gbr = GradientBoostingRegressor(random_state=0)

feature_sel = SelectFromModel(LinearRegression(),
  threshold="0.6*mean")

gbr_params = {
 'gradientboostingregressor__learning_rate': uniform(loc=0.01, scale=0.5),
 'gradientboostingregressor__n_estimators': randint(500, 2000),
 'gradientboostingregressor__max_depth': randint(2, 20),
 'gradientboostingregressor__min_samples_leaf': randint(5, 11)
}

pipe1 = make_pipeline(coltrans, feature_sel, gbr)

rs1 = RandomizedSearchCV(pipe1, gbr_params, cv=5, n_iter=20,
  scoring='neg_mean_squared_error', n_jobs=-1, random_state=0)

rs1.fit(X_train, y_train.values.ravel())

rs1.best_params_
rs1.best_score_

y_test.mean()

print("fit time: %.3f, score time: %.3f"  %
  (np.mean(rs1.cv_results_['mean_fit_time']),\
  np.mean(rs1.cv_results_['mean_score_time'])))

# construct an XGBoost model    
xgb = XGBRegressor()

xgb_params = {
 'xgbregressor__learning_rate': uniform(loc=0.01, scale=0.5),
 'xgbregressor__n_estimators': randint(500, 2000),
 'xgbregressor__max_depth': randint(2, 20)
}

pipe2 = make_pipeline(coltrans, feature_sel, xgb)

rs2 = RandomizedSearchCV(pipe2, xgb_params, cv=5, n_iter=20,
  scoring='neg_mean_squared_error', n_jobs=-1, random_state=0)

rs2.fit(X_train, y_train.values.ravel())

rs2.best_params_
rs2.best_score_

print("fit time: %.3f, score time: %.3f"  %
  (np.mean(rs2.cv_results_['mean_fit_time']),\
  np.mean(rs2.cv_results_['mean_score_time'])))


