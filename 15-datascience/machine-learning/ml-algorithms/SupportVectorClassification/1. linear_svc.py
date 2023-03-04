# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import LinearSVC
from scipy.stats import uniform
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import RFECV

from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.model_selection import cross_validate, \
  RandomizedSearchCV, RepeatedStratifiedKFold
import sklearn.metrics as skmet
import matplotlib.pyplot as plt
import seaborn as sns


import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
from preprocfunc import OutlierTrans

pd.set_option('display.width', 120)
pd.set_option('display.max_columns', 40)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

# setup the features and target
nbagames = pd.read_csv("data/nbagames2017plus.csv",
  parse_dates=['GAME_DATE'])
nbagames = nbagames.loc[nbagames.WL_HOME.isin(['W','L'])]
nbagames.shape

nbagames['WL_HOME'] = \
  np.where(nbagames.WL_HOME=='L',0,1).astype('int')
  
nbagames.WL_HOME.value_counts(dropna=False)

# take a look at some of the data

# identify numeric and categorical data
num_cols = ['FG_PCT_HOME','FTA_HOME','FG3_PCT_HOME',
  'FTM_HOME','FT_PCT_HOME','OREB_HOME','DREB_HOME',
  'REB_HOME','AST_HOME','STL_HOME','BLK_HOME','TOV_HOME',
  'FG_PCT_AWAY','FTA_AWAY','FG3_PCT_AWAY',
  'FT_PCT_AWAY','OREB_AWAY','DREB_AWAY','REB_AWAY',
  'AST_AWAY','STL_AWAY','BLK_AWAY','TOV_AWAY']
cat_cols = ['SEASON']

# create training and testing DataFrames
nbagames[['WL_HOME'] + num_cols].\
  agg(['count','min','median','max']).T

# look at some correlations
corrmatrix = nbagames[['WL_HOME'] + \
  num_cols].corr(method="pearson")

sns.heatmap(corrmatrix, xticklabels=corrmatrix.columns,
  yticklabels=corrmatrix.columns, cmap="coolwarm")
plt.title('Heat Map of Correlation Matrix')
plt.tight_layout()
plt.show()

X_train, X_test, y_train, y_test =  \
  train_test_split(nbagames[num_cols + cat_cols],\
  nbagames[['WL_HOME']], test_size=0.2, random_state=0)

# setup column transformations
ohe = OneHotEncoder(drop='first', sparse=False)

cattrans = make_pipeline(ohe)
standtrans = make_pipeline(OutlierTrans(2),
  SimpleImputer(strategy="median"), StandardScaler())
coltrans = ColumnTransformer(
  transformers=[
    ("cat", cattrans, cat_cols),
    ("stand", standtrans, num_cols)
  ]
)


# show a decision bondary for a Linear SVC model
pipe0 = make_pipeline(OutlierTrans(2),
  SimpleImputer(strategy="median"), StandardScaler())

X_train_enc = pipe0.\
  fit_transform(X_train[['FG_PCT_HOME','DREB_HOME']])

def dispbound(model, X, xvarnames, y, title):
  dispfit = model.fit(X,y)
  disp = DecisionBoundaryDisplay.from_estimator(
    dispfit, X, response_method="predict",
    xlabel=xvarnames[0], ylabel=xvarnames[1],
    alpha=0.5,
  )
  scatter = disp.ax_.scatter(X[:,0], X[:,1],
    c=y, edgecolor="k")
  
  disp.ax_.set_title(title)
  legend1 = disp.ax_.legend(*scatter.legend_elements(),
    loc="lower left", title="Home Win")
  disp.ax_.add_artist(legend1)

dispbound(LinearSVC(max_iter=1000000,loss='hinge'),
  X_train_enc, ['FG_PCT_HOME','DREB_HOME'],
  y_train.values.ravel(),
  'Linear SVC Decision Bondary')


# fit a Linear SVC model
svc = LinearSVC(max_iter=10000000, loss='hinge',
   random_state=0)

rfecv = RFECV(estimator=svc, cv=5)

pipe1 = make_pipeline(coltrans, rfecv, svc)

pipe1.fit(X_train, y_train.values.ravel())

new_cat_cols = \
  pipe1.named_steps['columntransformer'].\
  named_transformers_['cat'].\
  named_steps['onehotencoder'].\
  get_feature_names(cat_cols)

new_cols = np.concatenate((new_cat_cols, np.array(num_cols)))
sel_cols = new_cols[pipe1['rfecv'].get_support()]
np.set_printoptions(linewidth=55)
sel_cols

pd.Series(pipe1['linearsvc'].\
  coef_[0], index=sel_cols).\
  sort_values(ascending=False)

# let's look at the predictions
pred = pipe1.predict(X_test)

print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred, pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))


# do kfold cross validation
kf = RepeatedStratifiedKFold(n_splits=7, n_repeats=10,\
   random_state=0)

scores = cross_validate(pipe1, X_train, \
  y_train.values.ravel(), \
  scoring=['accuracy','precision','recall','f1'], \
  cv=kf, n_jobs=-1)


print("accuracy: %.2f, precision: %.2f, sensitivity: %.2f, f1: %.2f"  %
  (np.mean(scores['test_accuracy']),\
  np.mean(scores['test_precision']),\
  np.mean(scores['test_recall']),\
  np.mean(scores['test_f1'])))

# do a grid search to find the best value of alpha

svc_params = {
 'linearsvc__C': uniform(loc=0, scale=100)
}

rs = RandomizedSearchCV(pipe1, svc_params, cv=10, 
  scoring='accuracy', n_iter=20, random_state=0)
rs.fit(X_train, y_train.values.ravel())

rs.best_params_
rs.best_score_

results = \
  pd.DataFrame(rs.cv_results_['mean_test_score'], \
    columns=['meanscore']).\
  join(pd.DataFrame(rs.cv_results_['params'])).\
  sort_values(['meanscore'], ascending=False)

results

pred = rs.predict(X_test)

print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred, pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))


cm = skmet.confusion_matrix(y_test, pred)
cmplot = \
  skmet.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Loss', 'Won'])
cmplot.plot()
cmplot.ax_.set(title='Home Team Win Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')


