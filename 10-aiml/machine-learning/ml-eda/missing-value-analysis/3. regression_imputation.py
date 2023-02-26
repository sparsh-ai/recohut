# import pandas
import pandas as pd
import numpy as np
import statsmodels.api as sm
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format
nls97 = pd.read_csv("data/nls97b.csv")
nls97.set_index("personid", inplace=True)

# check correlations with wageincome

nls97[['wageincome','highestdegree','weeksworked16','parentincome']].info()
nls97['hdegnum'] = nls97.highestdegree.str[0:1].astype('float')
nls97.groupby(['highestdegree','hdegnum']).size()
nls97.parentincome.replace(list(range(-5,0)), np.nan, inplace=True)
nls97[['wageincome','hdegnum','weeksworked16','parentincome']].corr()

# check to see if folks with missing wage income data are different
nls97['missingwageincome'] = np.where(nls97.wageincome.isnull(),1,0)
nls97.groupby(['missingwageincome'])[['hdegnum','parentincome',\
  'weeksworked16']].agg(['mean','count'])

# prepare data to run regression
nls97.weeksworked16.fillna(nls97.weeksworked16.mean(), inplace=True)
nls97.parentincome.fillna(nls97.parentincome.mean(), inplace=True)
nls97['degltcol'] = np.where(nls97.hdegnum<=2,1,0)
nls97['degcol'] = np.where(nls97.hdegnum.between(3,4),1,0)
nls97['degadv'] = np.where(nls97.hdegnum>4,1,0)

# fit a linear regression model
# return the influence of each observation
# also return model coefficients
def getlm(df, ycolname, xcolnames):
  df = df[[ycolname] + xcolnames].dropna()
  y = df[ycolname]
  X = df[xcolnames]
  X = sm.add_constant(X)
  lm = sm.OLS(y, X).fit()
  coefficients = pd.DataFrame(zip(['constant'] + xcolnames,
    lm.params, lm.pvalues), columns=['features','params',
    'pvalues'])
  return coefficients, lm

xvars = ['weeksworked16','parentincome','degcol','degadv']
coefficients, lm = getlm(nls97, 'wageincome', xvars)
coefficients

# generate predictions
pred = lm.predict(sm.add_constant(nls97[xvars])).\
  to_frame().rename(columns= {0: 'pred'})
nls97 = nls97.join(pred)
nls97['wageincomeimp'] = np.where(nls97.wageincome.isnull(),\
  nls97.pred, nls97.wageincome)
pd.options.display.float_format = '{:,.0f}'.format
nls97[['wageincomeimp','wageincome'] + xvars].head(10)
nls97[['wageincomeimp','wageincome']].\
  agg(['count','mean','std'])

# add an error term
randomadd = np.random.normal(0, lm.resid.std(), nls97.shape[0])
randomadddf = pd.DataFrame(randomadd, columns=['randomadd'], index=nls97.index)
nls97 = nls97.join(randomadddf)
nls97['stochasticpred'] = nls97.pred + nls97.randomadd
nls97['wageincomeimpstoc'] = np.where(nls97.wageincome.isnull(),\
  nls97.stochasticpred, nls97.wageincome)



