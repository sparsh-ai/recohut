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

