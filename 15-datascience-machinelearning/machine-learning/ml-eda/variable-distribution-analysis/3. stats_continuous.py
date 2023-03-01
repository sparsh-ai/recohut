# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
import scipy.stats as scistat
import matplotlib.pyplot as plt
pd.set_option('display.width', 70)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv",
  parse_dates=['lastdate'])
covidtotals.set_index("iso_code", inplace=True)

# look at a few rows of the covid cases data
covidtotals.shape
covidtotals.index.nunique()
covidtotals.sample(2, random_state=6).T
covidtotals.info()

# get descriptive statistics on the cumulative values
keyvars = ['location','total_cases_mill','total_deaths_mill',
  'aged_65_older','diabetes_prevalence']
covidkeys = covidtotals[keyvars]
covidkeys.describe()
covidkeys.quantile(np.arange(0.0, 1.1, 0.1))

# get skew and kurtosis
covidkeys.skew()
covidkeys.kurtosis()

# do a test of normality
for var in keyvars[1:]:
  stat, p = scistat.shapiro(covidkeys[var].dropna())
  print("feature=", var, "     p-value=", '{:.6f}'.format(p))


# view the distribution of total cases
plt.hist(covidtotals['total_cases']/1000, bins=12)
plt.title("Total Covid Cases (in thousands)")
plt.xlabel('Cases')
plt.ylabel("Number of Countries")
plt.show()

