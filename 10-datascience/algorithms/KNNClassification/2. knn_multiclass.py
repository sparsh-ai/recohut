# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from imblearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
from imblearn.over_sampling import SMOTENC
from sklearn.feature_selection import SelectKBest, chi2

import sklearn.metrics as skmet
import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format

# load the machine failure data
machinefailuretype = pd.read_csv("data/machinefailuretype.csv")
machinefailuretype.info()
machinefailuretype.head()
machinefailuretype.failtype.value_counts(dropna=False).sort_index()
machinefailuretype.machinetype.\
  value_counts(dropna=False).sort_index()

def setcode(typetext):
  if (typetext=="No Failure"):
    typecode = 1
  elif (typetext=="Heat Dissipation Failure"):
    typecode = 2
  elif (typetext=="Power Failure"):
    typecode = 3
  elif (typetext=="Overstrain Failure"):
    typecode = 4
  else:
    typecode = 5
  return typecode

machinefailuretype["failtypecode"] = \
  machinefailuretype.apply(lambda x: setcode(x.failtype), axis=1)

machinefailuretype.groupby(['failtypecode','failtype']).size().\
  reset_index()
  
# take a look at some of the data

# identify numeric and categorical data
num_cols = ['airtemp','processtemperature','rotationalspeed',
  'torque','toolwear']
cat_cols = ['machinetype']

machinefailuretype[num_cols].agg(['min','median','max']).T

# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(machinefailuretype[num_cols + cat_cols],\
  machinefailuretype[['failtypecode']], test_size=0.2, random_state=0)


# setup column transformations
ohe = OneHotEncoder(drop='first', sparse=False)

cattrans = make_pipeline(ohe)
standtrans = make_pipeline(OutlierTrans(3),SimpleImputer(strategy="median"),
  MinMaxScaler())
coltrans = ColumnTransformer(
  transformers=[
    ("cat", cattrans, cat_cols),
    ("stand", standtrans, num_cols),
  ]
)

coltrans.fit(X_train.sample(1000))

new_cat_cols = \
  coltrans.\
  named_transformers_['cat'].\
  named_steps['onehotencoder'].\
  get_feature_names(cat_cols)

new_cols = np.concatenate((new_cat_cols, np.array(num_cols)))

print(new_cols)

# construct a pipeline with preprocessing, feature selection, and logistic model
catcolscnt = new_cat_cols.shape[0]
smotenc = SMOTENC(categorical_features=np.arange(0,catcolscnt), random_state=0)

knn = KNeighborsClassifier(n_jobs=-1)

pipe1 = make_pipeline(coltrans, smotenc, SelectKBest(score_func=chi2), knn)

knn_params = {
 'selectkbest__k': np.arange(1, len(new_cols)),
 'kneighborsclassifier__n_neighbors': np.arange(5, 175, 2),
 'kneighborsclassifier__metric': ['euclidean','manhattan','minkowski']
}

rs = RandomizedSearchCV(pipe1, knn_params, cv=5, scoring="roc_auc_ovr_weighted")

rs.fit(X_train, y_train.values.ravel())

rs.best_params_
rs.best_score_


selected = rs.best_estimator_['selectkbest'].get_support()
selected.sum()
new_cols[selected]
rs.best_params_
rs.best_score_

new_cols[rs.best_estimator_['selectkbest'].get_support()]

pred = rs.predict(X_test)

cm = skmet.confusion_matrix(y_test, pred)
cmplot = skmet.ConfusionMatrixDisplay(confusion_matrix=cm,
   display_labels=['None', 'Heat','Power','Overstrain','Other'])
cmplot.plot()
cmplot.ax_.set(title='Machine Failure Type Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')

print(skmet.classification_report(y_test, pred,
  target_names=['None', 'Heat','Power','Overstrain','Other']))

