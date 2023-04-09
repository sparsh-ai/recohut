# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from feature_engine.encoding import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as skmet
import matplotlib.pyplot as plt
import seaborn as sb
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.3f}'.format

# a playing cards example
numobs = 6
inclasscnt = 3
plt.yticks([1,2,3])
plt.plot([0, numobs], [0, inclasscnt], c = 'b', label = 'Random Model')
plt.plot([0, inclasscnt, numobs], [0, inclasscnt, inclasscnt], c = 'grey', linewidth = 2, label = 'Perfect Model')
plt.title("Cumulative Accuracy Profile")
plt.xlabel("Total Cards")
plt.ylabel("In-class (Red) Cards")
plt.legend()

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


# random forest classification for feature importance
knn = KNeighborsClassifier(n_neighbors = 5)
rfc = RandomForestClassifier(n_estimators=100, max_depth=2, 
  n_jobs=-1, random_state=0)

# plot random model and perfect model
numobs = y_test.shape[0]
inclasscnt = y_test.iloc[:,0].sum()

plt.plot([0, numobs], [0, inclasscnt], c = 'b', label = 'Random Model')
plt.plot([0, inclasscnt, numobs], [0, inclasscnt, inclasscnt], c = 'grey', linewidth = 2, label = 'Perfect Model')
plt.axvline(numobs/2, color='black', linestyle='dashed', linewidth=1)
plt.axhline(numobs/2, color='black', linestyle='dashed', linewidth=1)
plt.title("Cumulative Accuracy Profile")
plt.xlabel("Total Observations")
plt.ylabel("In-class Observations")
plt.legend()

# plot k nearest neighbor and random forest models
def addplot(model, X, Xtest, y, modelname, linecolor):
  model.fit(X, y.values.ravel())
  probs = model.predict_proba(Xtest)[:, 1]
  
  probdf = pd.DataFrame(zip(probs, y_test.values.ravel()),
    columns=(['prob','inclass']))
  probdf.loc[-1] = [0,0]
  probdf = probdf.sort_values(['prob','inclass'],
    ascending=False).\
    assign(inclasscum = lambda x: x.inclass.cumsum())
  inclassmidpoint = probdf.iloc[int(probdf.shape[0]/2)].\
    inclasscum
  plt.axhline(inclassmidpoint, color=linecolor,
    linestyle='dashed', linewidth=1)
  plt.plot(np.arange(0, probdf.shape[0]),
    probdf.inclasscum, c = linecolor,
    label = modelname, linewidth = 4)

addplot(knn, X_train_enc, X_test_enc, y_train,
  'KNN', 'red')
addplot(rfc, X_train_enc, X_test_enc, y_train,
  'Random Forest', 'green')
plt.legend()


# plot probability distribution
rfc.fit(X_train_enc, y_train.values.ravel())
pred = rfc.predict(X_test_enc)
pred_probs = rfc.predict_proba(X_test_enc)[:, 1]

probdf = pd.DataFrame(zip(pred_probs, pred, y_test.values.ravel()),
  columns=(['prob','pred','actual']))

probdf.groupby(['pred'])['prob'].agg(['min','max'])




sb.kdeplot(probdf.loc[probdf.actual==1].prob, shade=True, color='red',
  label="Completed BA")
sb.kdeplot(probdf.loc[probdf.actual==0].prob, shade=True, color='green',
  label="Did Not Complete")
plt.axvline(0.5, color='black', linestyle='dashed', linewidth=1)
plt.axvline(0.65, color='black', linestyle='dashed', linewidth=1)
plt.title("Predicted Probability Distribution")
plt.legend(loc="upper left")


# plot ROC curve
fpr, tpr, ths = skmet.roc_curve(y_test, pred_probs)
ths = ths[1:]
fpr = fpr[1:]
tpr = tpr[1:]
fig, ax = plt.subplots()
ax.plot(ths, fpr, label="False Positive Rate")
ax.plot(ths, tpr, label="Sensitivity")
ax.set_title('False Positive Rate and Sensitivity by Threshold')
ax.set_xlabel('Threshold')
ax.set_ylabel('False Positive Rate and Sensitivity')
ax.legend()


fig, ax = plt.subplots()
ax.plot(fpr, tpr, linewidth=4, color="black")
ax.set_title('ROC curve')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('Sensitivity')

tholdind = np.where((ths>0.499) & (ths<0.501))[0][0]
tholdindlow = np.where((ths>0.397) & (ths<0.404))[0][0]
tholdindhigh = np.where((ths>0.599) & (ths<0.601))[0][0]
plt.vlines((fpr[tholdindlow],fpr[tholdind],fpr[tholdindhigh]),
  0, 1, linestyles ="dashed", colors =["green","blue","purple"])
plt.hlines((tpr[tholdindlow],tpr[tholdind],tpr[tholdindhigh]),
  0, 1, linestyles ="dashed", colors =["green","blue","purple"])


# plot precision and sensitivity lines
prec, sens, ths = skmet.precision_recall_curve(y_test, pred_probs)

prec = prec[1:-10]
sens = sens[1:-10]
ths  = ths[:-10]

fig, ax = plt.subplots()
ax.plot(ths, prec, label='Precision')
ax.plot(ths, sens, label='Sensitivity')
ax.set_title('Precision and Sensitivity by Threshold')
ax.set_xlabel('Threshold')
ax.set_ylabel('Precision and Sensitivity')
ax.set_xlim(0.3,0.9)
ax.legend()


# plot precision and sensitivity curve
fig, ax = plt.subplots()
ax.plot(sens, prec)
ax.set_title('Precision-Sensitivity Curve')
ax.set_xlabel('Sensitivity')
ax.set_ylabel('Precision')
ax.set_ylim(0)
plt.yticks(np.arange(0.2, 0.9, 0.2))

temp = pd.DataFrame(zip(sens, prec, ths), columns=['sensitivity','precision','threshold'])
temp.describe()
temp.head(70)
temp.tail(70)

