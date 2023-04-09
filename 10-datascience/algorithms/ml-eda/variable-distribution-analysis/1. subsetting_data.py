# import pandas and numpy, and load the nls97 data
import pandas as pd
import numpy as np
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)

# select the high school record columns
democols = ['gender','birthyear','maritalstatus',
 'weeksworked16','wageincome','highestdegree']

nls97demo = nls97[democols]
nls97demo.index.name

# use slicing to select a few rows
nls97demo[1000:1004].T
nls97demo[1000:1004:2].T

# select first 3 rows using head() and Python slicing
nls97demo[:3].T
nls97demo.head(3).T

# select last 3 rows using tail() and Python slicing
nls97demo[-3:].T
nls97demo.tail(3).T

# select a few rows using loc and iloc
nls97demo.loc[[195884,195891,195970]].T
nls97demo.loc[195884:195970].T
nls97demo.iloc[[0,1,2]].T
nls97demo.iloc[0:3].T
nls97demo.iloc[-3:].T

# select multiple rows conditionally
nls97.nightlyhrssleep.head()
lowsleepthreshold = nls97.nightlyhrssleep.quantile(0.33)
lowsleepthreshold
sleepcheckbool = nls97.nightlyhrssleep<=lowsleepthreshold
sleepcheckbool.head()
sleepcheckbool.index.equals(nls97.index)

lowsleep = nls97.loc[sleepcheckbool]
lowsleep.shape
lowsleep = nls97.loc[nls97.nightlyhrssleep<=lowsleepthreshold]
lowsleep.shape

# select rows based on multiple conditions
lowsleep3pluschildren = \
  nls97.loc[(nls97.nightlyhrssleep<=lowsleepthreshold)
    & (nls97.childathome>=3)]
lowsleep3pluschildren.shape

# select rows based on multiple conditions and also select columns
lowsleep3pluschildren = \
  nls97.loc[(nls97.nightlyhrssleep<=lowsleepthreshold)
    & (nls97.childathome>=3),
    ['nightlyhrssleep','childathome']]
lowsleep3pluschildren.shape

