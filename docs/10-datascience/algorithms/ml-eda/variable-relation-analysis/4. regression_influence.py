# import pandas, numpy, matplotlib, statsmodels, and load the covid totals data
import pandas as pd
import numpy as np
import statsmodels.api as sm
pd.set_option('display.width', 70)
pd.options.display.float_format = '{:,.3f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

# take a look at the distribution of some key features
xvars = ['population_density','aged_65_older',
 'gdp_per_capita','diabetes_prevalence']

covidtotals[['total_cases_mill'] + xvars].\
  quantile(np.arange(0.0,1.05,0.25))

# fit a linear regression model
# return the influence of each observation
# also return model coefficients
def getlm(df, ycolname, xcolnames):
  df = df[[ycolname] + xcolnames].dropna()
  y = df[ycolname]
  X = df[xcolnames]
  X = sm.add_constant(X)
  lm = sm.OLS(y, X).fit()
  influence = lm.get_influence().summary_frame()
  coefficients = pd.DataFrame(zip(['constant'] + xcolnames,
    lm.params, lm.pvalues), columns=['features','params',
    'pvalues'])
  return coefficients, influence, lm

coefficients, influence, lm = getlm(covidtotals, 'total_cases_mill', xvars)
coefficients

# identify countries with an outsized influence on the model
influencethreshold = 3*influence.cooks_d.mean()
covidtotals = covidtotals.join(influence[['cooks_d']])
covidtotalsoutliers = \
  covidtotals.loc[covidtotals.cooks_d>influencethreshold]
covidtotalsoutliers.shape

covidtotalsoutliers[['location','total_cases_mill','cooks_d'] + \
  xvars].sort_values(['cooks_d'], ascending=False).head()

coefficients, influence, lm2 = \
  getlm(covidtotals.drop(['HKG','SGP']),
  'total_cases_mill', xvars)
coefficients

