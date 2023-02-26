# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold, \
  GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics as skmet

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.3f}'.format

# load the health information data
letterrecognition = pd.read_csv("data/letterrecognition.csv")
letterrecognition.shape
letterrecognition.head().T

# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(letterrecognition.iloc[:,1:],\
  letterrecognition.iloc[:,0:1], test_size=0.2, 
  random_state=0)

# construct a pipeline with preprocessing, feature selection, and logistic model
knn = KNeighborsClassifier(n_jobs=-1)

kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)

knn_params = {
  'n_neighbors': np.arange(3, 41, 2),
  'metric': ['euclidean','manhattan','minkowski']
}

# do a grid search for the best k value
gs = GridSearchCV(knn, knn_params, cv=kf, scoring='accuracy')
gs.fit(X_train, y_train.values.ravel())

gs.best_params_
gs.best_score_

pred = gs.best_estimator_.predict(X_test)

letters = np.sort(letterrecognition.letter.unique())

cm = skmet.confusion_matrix(y_test, pred)
cmplot = \
  skmet.ConfusionMatrixDisplay(confusion_matrix=cm,
  display_labels=letters)
cmplot.plot()
cmplot.ax_.set(title='Letters', 
  xlabel='Predicted Value', ylabel='Actual Value')
