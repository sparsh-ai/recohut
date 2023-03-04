# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from imblearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
import sklearn.metrics as skmet
import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
import healthinfo as hi

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.3f}'.format


X_train = hi.X_train
X_test = hi.X_test
y_train = hi.y_train
y_test = hi.y_test

# do some hyperparameter tuning
rfc = RandomForestClassifier(random_state=0)

pipe1 = make_pipeline(hi.coltrans, hi.smotenc, rfc)

rfc_params = {
 'randomforestclassifier__min_samples_leaf':
    randint(100, 1200),
 'randomforestclassifier__max_depth': 
    randint(2, 20),
 'randomforestclassifier__n_estimators': 
    randint(100, 3000),
 'randomforestclassifier__criterion': 
    ['gini','entropy']
}

rs = RandomizedSearchCV(pipe1, rfc_params, cv=5, 
  n_iter=20, scoring="roc_auc")

rs.fit(X_train, y_train.values.ravel())

rs.best_params_
rs.best_score_

rs.named_transformer['estimator']
rs.named_steps['randomforestclassifier']
rs.best_estimator_['randomforestclassifier'].feature_importances_


feature_imp = pd.Series(rs.\
  best_estimator_['randomforestclassifier'].\
  feature_importances_, index=hi.new_cols)
feature_imp.loc[feature_imp>0.01].\
    plot(kind='barh')
plt.tight_layout()    


pred = rs.predict(X_test)

print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred,
    pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))


cm = skmet.confusion_matrix(y_test, pred)
cmplot = skmet.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Negative', 'Positive'])
cmplot.plot()
cmplot.ax_.set(title='Heart Disease Prediction Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')
