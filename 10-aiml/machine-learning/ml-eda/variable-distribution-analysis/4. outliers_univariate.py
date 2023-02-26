# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
pd.set_option('display.width', 70)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.1f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

keyvars = ['location','total_cases_mill','total_deaths_mill',
  'aged_65_older','diabetes_prevalence','gdp_per_capita']

covidkeys = covidtotals[keyvars]

# show outliers for total cases
thirdq, firstq = covidkeys.total_cases_mill.quantile(0.75), covidkeys.total_cases_mill.quantile(0.25)
interquartilerange = 1.5*(thirdq-firstq)
extvalhigh, extvallow = interquartilerange+thirdq, firstq-interquartilerange
print(extvallow, extvalhigh, sep=" <--> ")
covidtotals.loc[covidtotals.total_cases_mill>extvalhigh].T
covidtotals.mean()

covidkeys.info()

# generate a table of extreme values and save it to Excel
def getextremevalues(dfin):
  dfout = pd.DataFrame(columns=dfin.columns, data=None)
  for col in dfin.columns[1:]:
    thirdq, firstq = dfin[col].quantile(0.75),dfin[col].\
      quantile(0.25)
    interquartilerange = 1.5*(thirdq-firstq)
    extvalhigh, extvallow = \
      interquartilerange+thirdq, firstq-interquartilerange
    df = dfin.loc[(dfin[col]>extvalhigh) | (dfin[col]<extvallow)]
    df = df.assign(varname = col,
      threshlow = extvallow,
      threshhigh = extvalhigh)
    dfout = pd.concat([dfout, df])
  return dfout

extremevalues = getextremevalues(covidkeys)
extremevalues.varname.value_counts()
extremevalues.to_excel("views/extremevaluescases.xlsx")

# look a little more closely at outliers for deaths per million
extremevalues.loc[extremevalues.varname=="total_deaths_mill",
  'threshhigh'][0]
extremevalues.loc[extremevalues.varname=="total_deaths_mill",\
  keyvars].sort_values(['total_deaths_mill'], ascending=False)

# show a qqplot for total cases and total cases per million
sm.qqplot(covidtotals[['total_cases_mill']]. \
  sort_values(['total_cases_mill']).dropna(), line='s')
plt.title("QQ Plot of Total Cases Per Million")
plt.tight_layout()
plt.show()

# load the land temperatures data
landtemps = pd.read_csv("data/landtemps2019avgs.csv")
landtemps.avgtemp.describe(percentiles=[0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95])
landtemps.loc[landtemps.avgtemp<-25,'avgtemp'].count()
landtemps.avgtemp.skew()
landtemps.avgtemp.kurtosis()

# show a qqplot of average land temperatures
sm.qqplot(landtemps.avgtemp.sort_values().dropna(), line='s')
plt.title("QQ Plot of Average Temperatures")
plt.tight_layout()
plt.show()


