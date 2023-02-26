# import pandas and scikit learn's KNNImputer module
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

# prepare the NLS data

nls97['hdegnum'] = nls97.highestdegree.str[0:1].astype('float')
nls97['degltcol'] = np.where(nls97.hdegnum<=2,1,0)
nls97['degcol'] = np.where(nls97.hdegnum.between(3,4),1,0)
nls97['degadv'] = np.where(nls97.hdegnum>4,1,0)
nls97.parentincome.replace(list(range(-5,0)), np.nan, inplace=True)

wagedatalist = ['wageincome','weeksworked16',
   'parentincome','degltcol','degcol','degadv']
wagedata = nls97[wagedatalist]

# initialize a KNN imputation model and fill values
impKNN = KNNImputer(n_neighbors=47)
newvalues = impKNN.fit_transform(wagedata)
wagedatalistimp = ['wageincomeimp','weeksworked16imp',
  'parentincomeimp','degltcol','degcol','degadv']
wagedataimp = pd.DataFrame(newvalues,
  columns=wagedatalistimp, index=wagedata.index)

# view imputed values
wagedata = wagedata.\
  join(wagedataimp[['wageincomeimp','weeksworked16imp']])
wagedata[['wageincome','weeksworked16','parentincome',
  'degcol','degadv','wageincomeimp']].head(10)

wagedata[['wageincome','wageincomeimp']].\
  agg(['count','mean','std'])

