import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin

class OutlierTrans(BaseEstimator,TransformerMixin):
  def __init__(self,threshold=1.5):
    self.threshold = threshold
        
  def fit(self,X,y=None):
    return self

  def transform(self,X,y=None):
    Xnew = X.copy()
    for col in Xnew.columns:
      thirdq, firstq = Xnew[col].quantile(0.75),\
        Xnew[col].quantile(0.25)
      interquartilerange = self.threshold*(thirdq-firstq)
      outlierhigh, outlierlow = interquartilerange+thirdq,\
        firstq-interquartilerange
      Xnew.loc[(Xnew[col]>outlierhigh) | \
        (Xnew[col]<outlierlow),col] = np.nan
    return Xnew.values

class MakeOrdinal(BaseEstimator,TransformerMixin):
  def fit(self,X,y=None):
    return self
    
  def transform(self,X,y=None):
    Xnew = X.copy()
    for col in Xnew.columns:
      cats = np.sort(Xnew[col].unique())
      Xnew[col] = Xnew.\
        apply(lambda x: int(np.where(cats==\
        x[col])[0]), axis=1)
    return Xnew.values

class ReplaceVals(BaseEstimator,TransformerMixin):
  def __init__(self,repdict):
    self.repdict = repdict

  def fit(self,X,y=None):
    return self
    
  def transform(self,X,y=None):
    Xnew = X.copy().replace(self.repdict)
    return Xnew.values

