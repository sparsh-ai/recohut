# import pandas
import pandas as pd
import numpy as np
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 12)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

# set up school record and demographic data frames from the NLS data
schoolrecordlist = ['satverbal','satmath','gpaoverall','gpaenglish',
  'gpamath','gpascience','highestdegree','highestgradecompleted']

schoolrecord = nls97[schoolrecordlist]
schoolrecord.shape

# check the school record data for missings
schoolrecord.isnull().sum(axis=0)
misscnt = schoolrecord.isnull().sum(axis=1)
misscnt.value_counts().sort_index()
schoolrecord.loc[misscnt>=7].head(4).T

# remove rows with almost all missing data
schoolrecord = schoolrecord.dropna(thresh=2)
schoolrecord.shape
schoolrecord.isnull().sum(axis=1).value_counts().sort_index()

# assign mean values to missings
schoolrecord.gpaoverall.agg(['mean','std','count'])
schoolrecord.gpaoverall.\
  fillna(schoolrecord.gpaoverall.\
  mean(), inplace=True)
schoolrecord.gpaoverall.isnull().sum()
schoolrecord.gpaoverall.agg(['mean','std','count'])

# use forward fill
wageincome = nls97.wageincome.copy(deep=True)
wageincome.isnull().sum()
wageincome.agg(['mean','std','count'])
wageincome.head().T

wageincome.fillna(method='ffill', inplace=True)
wageincome.head().T
wageincome.isnull().sum()
wageincome.agg(['mean','std','count'])

wageincome = nls97.wageincome.copy(deep=True)
wageincome.fillna(method='bfill', inplace=True)
wageincome.head().T
wageincome.agg(['mean','std','count'])


# fill missings with the average by group
nls97.weeksworked17.mean()
nls97.groupby(['highestdegree'])['weeksworked17'].mean()
nls97.loc[~nls97.highestdegree.isnull(), 'weeksworked17imp'] = \
  nls97.loc[~nls97.highestdegree.isnull()].\
  groupby(['highestdegree'])['weeksworked17'].\
  apply(lambda group: group.fillna(np.mean(group)))

nls97[['weeksworked17imp','weeksworked17','highestdegree']].\
  head(10)
nls97[['weeksworked17imp','weeksworked17']].\
  agg(['mean','count'])
