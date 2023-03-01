# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.pipeline import make_pipeline
from imblearn.over_sampling import SMOTE
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import sklearn.metrics as skmet

pd.set_option('display.width', 78)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.3f}'.format

# load the health information data
spamtext = pd.read_csv("data/spamtext.csv")
spamtext['spam'] = np.where(spamtext.category=='spam',1,0)
spamtext.groupby(['spam','category']).size()
spamtext.head()

# create training and testing DataFrames
X_train, X_test, y_train, y_test =  \
  train_test_split(spamtext[['message']],\
  spamtext[['spam']], test_size=0.2,\
  stratify=spamtext[['spam']], random_state=0)

countvectorizer = CountVectorizer(analyzer='word', \
 stop_words='english')
    
smallsample = X_train.loc[X_train.message.str.len()<50].\
  sample(2, random_state=35)
smallsample

ourvec = \
  pd.DataFrame(countvectorizer.\
    fit_transform(smallsample.values.ravel()).toarray(),\
    columns=countvectorizer.get_feature_names())
ourvec

#countvectorizer.fit(X_train.loc[X_train.message.str.len()<40].values.ravel())
nb = MultinomialNB()

smote = SMOTE(random_state=0)

pipe1 = make_pipeline(countvectorizer, smote, nb)

pipe1.fit(X_train.values.ravel(), y_train.values.ravel())

pred = pipe1.predict(X_test.values.ravel())

print("accuracy: %.2f, sensitivity: %.2f, specificity: %.2f, precision: %.2f"  %
  (skmet.accuracy_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred),
  skmet.recall_score(y_test.values.ravel(), pred, pos_label=0),
  skmet.precision_score(y_test.values.ravel(), pred)))

cm = skmet.confusion_matrix(y_test, pred)
cmplot = skmet.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Not Spam', 'Spam'])
cmplot.plot()
cmplot.ax_.set(title='Spam Prediction Confusion Matrix', 
  xlabel='Predicted Value', ylabel='Actual Value')


