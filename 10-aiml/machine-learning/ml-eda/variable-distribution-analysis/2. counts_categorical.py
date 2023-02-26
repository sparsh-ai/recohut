# import pandas, numpy
import pandas as pd
import numpy as np
pd.set_option('display.width', 53)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)

nls97abb = nls97.iloc[:,:20]
nls97abb.dtypes

# show frequencies for marital status
nls97abb.maritalstatus.value_counts(dropna=False)
nls97abb.maritalstatus.isnull().sum()

# sort by values alphabetically
marstatcnt = nls97abb.maritalstatus.value_counts(dropna=False)
type(marstatcnt)
marstatcnt.index
marstatcnt.sort_index()

# show percentages instead of counts
nls97.maritalstatus.\
  value_counts(normalize=True, dropna=False).\
     sort_index()

# convert object columns to category
catcols = nls97abb.select_dtypes(include=["object"]).columns
for col in nls97abb[catcols].columns:
  nls97abb[col] = nls97abb[col].astype('category')

nls97abb[catcols].dtypes

# show the names of columns with category data type and check for number of missings
nls97abb[catcols].isnull().sum()

# do percentages for all government responsibility variables
nls97abb.filter(like="gov").apply(pd.value_counts, normalize=True)

# do percentages for all government responsibility variables for people who are married
nls97abb.loc[nls97abb.maritalstatus=="Married"].\
  filter(like="gov").\
  apply(pd.value_counts, normalize=True)

nls97abb.loc[nls97abb.maritalstatus=="Married",
  ['govprovidejobs','govpricecontrols']].\
  apply(pd.value_counts, normalize=True)

# create a completed 12th grade column
nls97abb.highestgradecompleted.\
  replace(95, np.nan, inplace=True)
nls97abb['highschoolgrad'] = \
  np.where(nls97abb.highestgradecompleted.isnull(),np.nan, \
  np.where(nls97abb.highestgradecompleted<12,0,1))
nls97abb.groupby(['highschoolgrad'], dropna=False) \
  ['highestgradecompleted'].agg(['min','max','size'])
nls97abb['highschoolgrad'] = \
  nls97abb['highschoolgrad'].astype('category')

# create quintiles for gpamath
nls97abb.highestgradecompleted.value_counts(dropna=False).sort_index()
nls97abb['highgradegroup'] = \
  pd.qcut(nls97abb['highestgradecompleted'], 
  q=6, labels=[1,2,3,4,5,6])
nls97abb.groupby(['highgradegroup'])['highestgradecompleted'].\
  agg(['min','max','size'])
nls97abb['highgradegroup'] = \
  nls97abb['highgradegroup'].astype('category')


# do frequencies and percentages for all category variables in data frame
freqout = open('views/frequencies.txt', 'w') 
for col in nls97abb.\
  select_dtypes(include=["category"]):
    print(col, "----------------------",
      "frequencies",
    nls97abb[col].value_counts(dropna=False).sort_index(),
      "percentages",
    nls97abb[col].value_counts(normalize=True).\
      sort_index(),
    sep="\n\n", end="\n\n\n", file=freqout)

freqout.close()

