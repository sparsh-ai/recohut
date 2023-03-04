# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from imblearn.pipeline import make_pipeline
from sklearn.model_selection import RandomizedSearchCV,\
  RepeatedStratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest, chi2
from scipy.stats import randint
import sklearn.metrics as skmet
from sklearn.model_selection import cross_validate

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
import healthinfo as hi

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.3f}'.format

# load the health information data
X_train = hi.X_train
X_test = hi.X_test
y_train = hi.y_train
y_test = hi.y_test
new_cols = hi.new_cols

new_cols

# run a knn model with 5 nearest neighbors
knn_example = KNeighborsClassifier(n_neighbors=5, n_jobs=-1)

kf = RepeatedStratifiedKFold(n_splits=10, n_repeats=10, random_state=0)

pipe0 = make_pipeline(hi.coltrans, hi.smotenc, knn_example)

scores = cross_validate(pipe0, X_train,
  y_train.values.ravel(), \
  scoring=['accuracy','precision','recall','f1'], \
  cv=kf, n_jobs=-1)

print("accuracy: %.2f, sensitivity: %.2f, precision: %.2f, f1: %.2f"  %
  (np.mean(scores['test_accuracy']),\
  np.mean(scores['test_recall']),\
  np.mean(scores['test_precision']),\
  np.mean(scores['test_f1'])))

# do some hyperparameter tuning
knn = KNeighborsClassifier(n_jobs=-1)

pipe1 = make_pipeline(hi.coltrans, hi.smotenc,
   SelectKBest(score_func=chi2), knn)

knn_params = {
 'selectkbest__k':
    randint(1, len(new_cols)),
 'kneighborsclassifier__n_neighbors':
    randint(5, 300),
 'kneighborsclassifier__metric':
    ['euclidean','manhattan','minkowski']
}

rs = RandomizedSearchCV(pipe1, knn_params, cv=5, scoring="roc_auc")
rs.fit(X_train, y_train.values.ravel())

selected = rs.best_estimator_['selectkbest'].\
  get_support()
selected.sum()
new_cols[selected]
rs.best_params_
rs.best_score_


pred = rs.predict(X_test)

print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred, pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))


cm = skmet.confusion_matrix(y_test, pred)
cmplot = skmet.ConfusionMatrixDisplay(confusion_matrix=cm,
  display_labels=['Negative', 'Positive'])
cmplot.plot()
cmplot.ax_.set(title='Heart Disease Prediction Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')

