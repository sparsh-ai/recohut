# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from imblearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTENC

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

