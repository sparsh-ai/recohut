# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression

import sklearn.metrics as skmet
import matplotlib.pyplot as plt
import seaborn as sns

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans,\
  MakeOrdinal, ReplaceVals

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

# load the health information data
healthinfo = pd.read_csv("data/healthinfosample.csv")
healthinfo.set_index("personid", inplace=True)
healthinfo.head(2).T
healthinfo.shape
healthinfo.isnull().sum()


# take a look at some of the data
healthinfo.heartdisease.value_counts()

healthinfo['heartdisease'] = \
  np.where(healthinfo.heartdisease=='No',0,1).\
  astype('int')

healthinfo.heartdisease.value_counts()

# identify numeric and categorical data
num_cols = ['bmi','physicalhealthbaddays',
   'mentalhealthbaddays','sleeptimenightly']
binary_cols = ['smoking','alcoholdrinkingheavy',
  'stroke','walkingdifficult','physicalactivity',
  'asthma','kidneydisease','skincancer']
cat_cols = ['gender','ethnicity']
spec_cols1 = ['agecategory']
spec_cols2 = ['genhealth']
spec_cols3 = ['diabetic']

rep_dict = {
  'genhealth': {'Poor':0,'Fair':1,'Good':2,
    'Very good':3,'Excellent':4},
  'diabetic': {'No':0,
    'No, borderline diabetes':0,'Yes':1,
    'Yes (during pregnancy)':1}           
}

# generate some counts and descriptive data
healthinfo[binary_cols].\
  apply(pd.value_counts, normalize=True).T

for col in healthinfo[cat_cols + 
['genhealth','diabetic']].columns:
  print(col, "----------------------",
  healthinfo[col].value_counts(normalize=True).\
    sort_index(), sep="\n", end="\n\n")

healthinfo[num_cols].\
  agg(['count','min','median','max']).T

# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(healthinfo[num_cols + 
    binary_cols + cat_cols + spec_cols1 +
    spec_cols2 + spec_cols3],\
  healthinfo[['heartdisease']], test_size=0.2,
    random_state=0)


# setup column transformations
ohe = OneHotEncoder(drop='first', sparse=False)

standtrans = make_pipeline(OutlierTrans(3),
  SimpleImputer(strategy="median"),
  StandardScaler())
spectrans1 = make_pipeline(MakeOrdinal(),
  StandardScaler())
spectrans2 = make_pipeline(ReplaceVals(rep_dict),
  StandardScaler())
spectrans3 = make_pipeline(ReplaceVals(rep_dict))
bintrans = make_pipeline(ohe)
cattrans = make_pipeline(ohe)
coltrans = ColumnTransformer(
  transformers=[
    ("stand", standtrans, num_cols),
    ("spec1", spectrans1, spec_cols1),
    ("spec2", spectrans2, spec_cols2),
    ("spec3", spectrans3, spec_cols3),
    ("bin", bintrans, binary_cols),
    ("cat", cattrans, cat_cols),
  ]
)



# construct a pipeline with preprocessing, feature selection, and logistic model
lrsel = LogisticRegression(random_state=1, 
  max_iter=1000)

kf = StratifiedKFold(n_splits=5, shuffle=True)

rfecv = RFECV(estimator=lrsel, cv=kf)

lr = LogisticRegression(random_state=1,
  class_weight='balanced', max_iter=1000)

pipe1 = make_pipeline(coltrans, rfecv, lr)

pipe1.fit(X_train, y_train.values.ravel())

# get the columnn names from the onehotencoder
new_binary_cols = \
  pipe1.named_steps['columntransformer'].\
  named_transformers_['bin'].\
  named_steps['onehotencoder'].\
  get_feature_names(binary_cols)
new_cat_cols = \
  pipe1.named_steps['columntransformer'].\
  named_transformers_['cat'].\
  named_steps['onehotencoder'].\
  get_feature_names(cat_cols)

new_cols = np.concatenate((np.array(num_cols +
  spec_cols1 + spec_cols2 + spec_cols3),
  new_binary_cols, new_cat_cols))

np.set_printoptions(linewidth=55)
new_cols


# look at the rankings from the recursive featue elimination
rankinglabs = \
 np.column_stack((pipe1.named_steps['rfecv'].ranking_,
 new_cols))
pd.DataFrame(rankinglabs,
 columns=['rank','feature']).\
 sort_values(['rank','feature']).\
 set_index("rank")

# get the coefficients from the logistic regression
oddsratios = np.exp(pipe1.\
  named_steps['logisticregression'].coef_)
oddsratios.shape
selcols = new_cols[pipe1.\
  named_steps['rfecv'].get_support()]
oddswithlabs = np.column_stack((oddsratios.\
  ravel(), selcols))
pd.DataFrame(oddswithlabs, 
  columns=['odds','feature']).\
  sort_values(['odds'], ascending=False).\
  set_index('odds')


# get predictions and residuals
pred = pipe1.predict(X_test)

cm = skmet.confusion_matrix(y_test, pred)
cmplot = skmet.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Negative', 'Positive'])
cmplot.plot()
cmplot.ax_.set(title='Heart Disease Prediction Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')


tn, fp, fn, tp = skmet.confusion_matrix(y_test.values.ravel(), pred).ravel()
tn, fp, fn, tp
accuracy = (tp + tn) / pred.shape[0]
accuracy
sensitivity = tp / (tp + fn)
sensitivity
specificity = tn / (tn+fp)
specificity
precision = tp / (tp + fp)
precision


# another way to calculate the metrics
print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred,
    pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))


falsepositiverate = fp / (tn + fp)
falsepositiverate

# do a density plot
pred_probs = pipe1.predict_proba(X_test)[:, 1]

probdf = \
  pd.DataFrame(zip(pred_probs, pred,
  y_test.values.ravel()),
  columns=(['prob','pred','actual']))

probdf.groupby(['pred'])['prob'].\
  agg(['min','max','count'])


# do a density plot
sns.kdeplot(probdf.loc[probdf.actual==1].prob,
  shade=True, color='red',label="Heart Disease")
sns.kdeplot(probdf.loc[probdf.actual==0].prob,
  shade=True,color='green',label="No Heart Disease")
plt.axvline(0.25, color='black', linestyle='dashed',
  linewidth=1)
plt.axvline(0.5, color='black', linestyle='dashed',
  linewidth=1)
plt.title("Predicted Probability Distribution")
plt.legend(loc="upper left")


# plot precision and sensitivity lines
prec, sens, ths = skmet.precision_recall_curve(y_test, pred_probs)

prec = prec[1:-20]
sens = sens[1:-20]
ths  = ths[:-20]

fig, ax = plt.subplots()
ax.plot(ths, prec, label='Precision')
ax.plot(ths, sens, label='Sensitivity')
ax.set_title('Precision and Sensitivity by Threshold')
ax.set_xlabel('Threshold')
ax.set_ylabel('Precision and Sensitivity')
ax.legend()

# plot ROC curve
fpr, tpr, ths = skmet.roc_curve(y_test, pred_probs)
ths = ths[1:]
fpr = fpr[1:]
tpr = tpr[1:]

fig, ax = plt.subplots()
ax.plot(fpr, tpr, linewidth=4, color="black")
ax.set_title('ROC curve')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('Sensitivity')

fig, ax = plt.subplots()
ax.plot(ths, fpr, label="False Positive Rate")
ax.plot(ths, tpr, label="Sensitivity")
ax.set_title('False Positive Rate and Sensitivity by Threshold')
ax.set_xlabel('Threshold')
ax.set_ylabel('False Positive Rate and Sensitivity')
ax.legend()


# calculate Youden J statistic
jthresh = ths[np.argmax(tpr - fpr)]
jthresh


pred2 = np.where(pred_probs>=jthresh,1,0)
cm = skmet.confusion_matrix(y_test, pred2)
cmplot = skmet.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Negative', 'Positive'])
cmplot.plot()
cmplot.ax_.set(title='Heart Disease Prediction Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')

skmet.recall_score(y_test.values.ravel(), pred)
skmet.recall_score(y_test.values.ravel(), pred2)
