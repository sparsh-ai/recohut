# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectFromModel
import matplotlib.pyplot as plt

from scipy.stats import randint
from scipy.stats import uniform

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

# load the land temperatures data
fftaxrate14 = pd.read_csv("data/fossilfueltaxrate14.csv")
fftaxrate14.set_index('countrycode', inplace=True)
fftaxrate14.info()

# setup the features and target
num_cols = ['fuel_income_dependence','national_income_per_cap',
  'VAT_Rate',  'gov_debt_per_gdp','polity','goveffect',
  'democracy_index']
dummy_cols = ['democracy_polity','autocracy_polity','democracy',
  'nat_oil_comp','nat_oil_comp_state']
spec_cols = ['motorization_rate']

# generate some summary statistics
fftaxrate14[['gas_tax_imp'] + num_cols + spec_cols].\
  agg(['count','min','median','max']).T
fftaxrate14[dummy_cols].apply(pd.value_counts, normalize=True).T

target = fftaxrate14[['gas_tax_imp']]
features = fftaxrate14[num_cols + dummy_cols + spec_cols]

X_train, X_test, y_train, y_test =  \
  train_test_split(features,\
  target, test_size=0.2, random_state=0)
      
# setup pipelines for column transformation
standtrans = make_pipeline(OutlierTrans(2), SimpleImputer(strategy="median"))
cattrans = make_pipeline(SimpleImputer(strategy="most_frequent"))
spectrans = make_pipeline(OutlierTrans(2))
coltrans = ColumnTransformer(
  transformers=[
    ("stand", standtrans, num_cols),
    ("cat", cattrans, dummy_cols),
    ("spec", spectrans, spec_cols)
  ]
)

# construct a decision tree model
gbr = GradientBoostingRegressor(random_state=0)

feature_sel = SelectFromModel(LinearRegression(),
  threshold="0.8*mean")

gbr_params = {
 'gradientboostingregressor__learning_rate': uniform(loc=0.1, scale=0.5),
 'gradientboostingregressor__n_estimators': randint(100, 1000),
 'gradientboostingregressor__max_depth': np.arange(2, 20),
 'gradientboostingregressor__min_samples_leaf': np.arange(5, 11)
}

pipe1 = make_pipeline(OutlierTrans(3),
  SimpleImputer(strategy="median"),
  feature_sel, gbr)

rs = RandomizedSearchCV(pipe1, gbr_params, cv=4, n_iter=20,
  scoring='neg_mean_absolute_error', random_state=1)
rs.fit(X_train, y_train.values.ravel())

rs.best_params_
rs.best_score_

# get predictions and residuals
pred = rs.predict(X_test)


preddf = pd.DataFrame(pred, columns=['prediction'],
  index=X_test.index).join(X_test).join(y_test)

preddf['resid'] = preddf.incomeratio-preddf.prediction


plt.hist(preddf.resid, color="blue", bins=5)
plt.axvline(preddf.resid.mean(), color='red', linestyle='dashed', linewidth=1)
plt.title("Histogram of Residuals for Income Ratio")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.xlim()
plt.show()


plt.scatter(preddf.prediction, preddf.resid, color="blue")
plt.axhline(0, color='red', linestyle='dashed', linewidth=1)
plt.title("Scatterplot of Predictions and Residuals")
plt.xlabel("Predicted Income Ratio")
plt.ylabel("Residuals")
plt.show()

preddf.loc[np.abs(preddf.resid)>=0.12,
  ['incomeratio','prediction','resid',
  'laborforcepartratio', 'humandevratio']].T
