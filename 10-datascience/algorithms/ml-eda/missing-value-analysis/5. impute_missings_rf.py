# import pandas and scikit learn's KNNImputer module
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.1f}'.format
import os
import sys
import sklearn.neighbors._base
sys.modules['sklearn.neighbors.base'] = sklearn.neighbors._base
from missingpy import MissForest
nls97 = pd.read_csv("/data/nls97b.csv")
nls97.set_index("personid", inplace=True)

# clean the NLS wage data
nls97['hdegnum'] = nls97.highestdegree.str[0:1].astype('float')
nls97.parentincome.replace(list(range(-5,0)), np.nan, inplace=True)
nls97['degltcol'] = np.where(nls97.hdegnum<=2,1,0)
nls97['degcol'] = np.where(nls97.hdegnum.between(3,4),1,0)
nls97['degadv'] = np.where(nls97.hdegnum>4,1,0)

# load the wage income and associated data
wagedatalist = ['wageincome','weeksworked16','parentincome',
  'degltcol','degcol','degadv']
wagedata = nls97[wagedatalist]

# use miss forest to impute values
imputer = MissForest()
newvalues = imputer.fit_transform(wagedata)
wagedatalistimp = ['wageincomeimp','weeksworked16imp','parentincomeimp',
  'degltcol','degcol','degadv']
wagedataimp = pd.DataFrame(newvalues, columns=wagedatalistimp, index=wagedata.index)


# view imputed values
wagedataimp
wagedata = wagedata.join(wagedataimp[['wageincomeimp','weeksworked16imp']])
wagedata[['wageincome','weeksworked16','parentincome',
  'degcol','degadv','wageincomeimp']].head(10)

wagedata[['wageincome','wageincomeimp','weeksworked16','weeksworked16imp']].\
  agg(['count','mean','std'])

