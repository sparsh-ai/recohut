# import pandas, numpy, and matplotlib
import pandas as pd
from feature_engine.encoding import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as skmet
#import matplotlib.pyplot as plt
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

nls97compba = pd.read_csv("data/nls97compba.csv")

feature_cols = ['satverbal','satmath','gpaoverall',
  'parentincome','gender']

# separate NLS data into train and test datasets
X_train, X_test, y_train, y_test =  \
  train_test_split(nls97compba[feature_cols],\
  nls97compba[['completedba']], test_size=0.3, random_state=0)
      
# do one hot encoding and scaling
ohe = OneHotEncoder(drop_last=True, variables=['gender'])
ohe.fit(X_train)
X_train_enc, X_test_enc = \
  ohe.transform(X_train), ohe.transform(X_test)

scaler = StandardScaler()
standcols = X_train_enc.iloc[:,:-1].columns
scaler.fit(X_train_enc[standcols])
X_train_enc = \
  pd.DataFrame(scaler.transform(X_train_enc[standcols]),
  columns=standcols, index=X_train_enc.index).\
  join(X_train_enc[['gender_Female']])
X_test_enc = \
  pd.DataFrame(scaler.transform(X_test_enc[standcols]),
  columns=standcols, index=X_test_enc.index).\
  join(X_test_enc[['gender_Female']])


# k nearest neighbor classification
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train_enc, y_train.values.ravel())
pred = knn.predict(X_test_enc)

# show a confusion matrix
cm = skmet.confusion_matrix(y_test, pred, labels=knn.classes_)
cmplot = skmet.ConfusionMatrixDisplay(confusion_matrix=cm, \
 display_labels=['Negative--No BA', 'Positive--Completed BA'])
cmplot.plot()
cmplot.ax_.set(title='Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')

# calculate accuracy, sensitivity, specificity, and precision
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

print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred, pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))


# try this with a random forest classifier
rfc = RandomForestClassifier(n_estimators=100, max_depth=2, 
  n_jobs=-1, random_state=0)
rfc.fit(X_train_enc, y_train.values.ravel())
pred = rfc.predict(X_test_enc)
tn, fp, fn, tp = skmet.confusion_matrix(y_test.values.ravel(), pred).ravel()
tn, fp, fn, tp

print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred, pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))


