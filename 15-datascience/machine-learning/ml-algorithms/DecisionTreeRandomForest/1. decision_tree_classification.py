# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from imblearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import RandomizedSearchCV
from imblearn.over_sampling import SMOTENC
from sklearn.tree import DecisionTreeClassifier, plot_tree
from scipy.stats import randint
import sklearn.metrics as skmet

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import MakeOrdinal,\
  ReplaceVals

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.3f}'.format

# load the health information data
healthinfo = pd.read_csv("data/healthinfosample.csv")
healthinfo.set_index("personid", inplace=True)

# take a look at some of the data
healthinfo.heartdisease.value_counts()

healthinfo['heartdisease'] = \
  np.where(healthinfo.heartdisease=='No',0,1).\
  astype('int')

healthinfo.heartdisease.value_counts()

healthinfo.agecategory.value_counts().\
  sort_index().reset_index()

# identify numeric and categorical data
num_cols = ['bmi','physicalhealthbaddays',
   'mentalhealthbaddays','sleeptimenightly']
binary_cols = ['smoking','alcoholdrinkingheavy',
  'stroke','walkingdifficult','physicalactivity',
  'asthma','kidneydisease','skincancer']
cat_cols = ['gender','ethnicity']
spec_cols1 = ['agecategory']
spec_cols2 = ['genhealth','diabetic']

rep_dict = {
  'genhealth': {'Poor':0,'Fair':1,'Good':2,
    'Very good':3,'Excellent':4},
  'diabetic': {'No':0,
    'No, borderline diabetes':0,'Yes':1,
    'Yes (during pregnancy)':1}           
}


# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(healthinfo[num_cols + 
    binary_cols + cat_cols + spec_cols1 +
    spec_cols2],\
  healthinfo[['heartdisease']], test_size=0.2,
    random_state=0)


# setup column transformations
ohe = OneHotEncoder(drop='first', sparse=False)

spectrans1 = make_pipeline(MakeOrdinal())
spectrans2 = make_pipeline(ReplaceVals(rep_dict))
bintrans = make_pipeline(ohe)
cattrans = make_pipeline(ohe)
coltrans = ColumnTransformer(
  transformers=[
    ("bin", bintrans, binary_cols),
    ("cat", cattrans, cat_cols),
    ("spec1", spectrans1, spec_cols1),
    ("spec2", spectrans2, spec_cols2),
  ],
    remainder = 'passthrough'
)

coltrans.fit(X_train.sample(1000))

new_binary_cols = \
  coltrans.\
  named_transformers_['bin'].\
  named_steps['onehotencoder'].\
  get_feature_names(binary_cols)
new_cat_cols = \
  coltrans.\
  named_transformers_['cat'].\
  named_steps['onehotencoder'].\
  get_feature_names(cat_cols)

new_cols = np.concatenate((new_binary_cols, 
  new_cat_cols, np.array(spec_cols1 + spec_cols2 +
  num_cols)))

np.set_printoptions(linewidth=55)
new_cols

# construct a pipeline with preprocessing, feature selection, and logistic model
catcolscnt = new_binary_cols.shape[0] + \
  new_cat_cols.shape[0]

SMOTENC(categorical_features=np.arange(0,catcolscnt),
  random_state=0)
smotenc = \
  SMOTENC(categorical_features=np.arange(0,catcolscnt),
  random_state=0)

dtc_example = DecisionTreeClassifier(min_samples_leaf=30,
  max_depth=2)

pipe0 = make_pipeline(coltrans, smotenc, dtc_example)

pipe0.fit(X_train, y_train.values.ravel())

pipe0.named_steps['smotenc']

# get feature importances
feature_imp = \
  pipe0.named_steps['decisiontreeclassifier'].\
  tree_.compute_feature_importances(normalize=False)
feature_impgt0 = feature_imp>0
feature_implabs = np.column_stack((feature_imp.\
  ravel(), new_cols))
feature_implabs[feature_impgt0]

plot_tree(pipe0.named_steps['decisiontreeclassifier'],
  feature_names=new_cols, 
  class_names=['No Disease','Disease'], fontsize=10)


pred = pipe0.predict(X_test)

print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred,
    pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))

# do some hyperparameter tuning
dtc = DecisionTreeClassifier(random_state=0)

pipe1 = make_pipeline(coltrans, smotenc, dtc)

dtc_params = {
 'decisiontreeclassifier__min_samples_leaf': randint(100, 1200),
 'decisiontreeclassifier__max_depth': randint(2, 11)
}

rs = RandomizedSearchCV(pipe1, dtc_params, cv=5,
  n_iter=20, scoring="roc_auc")
rs.fit(X_train, y_train.values.ravel())

rs.best_params_
rs.best_score_


results = \
  pd.DataFrame(rs.cv_results_['mean_test_score'], \
    columns=['meanscore']).\
  join(pd.DataFrame(rs.cv_results_['params'])).\
  sort_values(['meanscore'], ascending=False).\
  rename(columns=\
    {'decisiontreeclassifier__max_depth':'maxdepth',
     'decisiontreeclassifier__min_samples_leaf':\
     'samples'})

results

pred2 = rs.predict(X_test)

cm = skmet.confusion_matrix(y_test, pred2)
cmplot = \
  skmet.ConfusionMatrixDisplay(confusion_matrix=cm,
  display_labels=['Negative', 'Positive'])
cmplot.plot()
cmplot.ax_.\
  set(title='Heart Disease Prediction Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')


print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred2),
  skmet.recall_score(y_test.values.ravel(), pred2),
  skmet.recall_score(y_test.values.ravel(), pred2,
    pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred2)))

# this can be used to save the transformed data; it is not in the chapter text
healthinfosample_enc = pd.DataFrame(coltrans.fit_transform(healthinfo[num_cols + 
  binary_cols + cat_cols + spec_cols1 + spec_cols2]), columns=new_cols, index=healthinfo.index).join(healthinfo[['heartdisease']])

healthinfosample_enc.to_csv('data/healthinfosample_enc.csv', index=False)

