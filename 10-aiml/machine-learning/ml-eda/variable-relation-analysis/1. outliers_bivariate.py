# import pandas, numpy, and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.0f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

# set up the cumulative and demographic columns
covidtotals.info()

totvars = ['location','total_cases_mill','total_deaths_mill']
demovars = ['population_density','aged_65_older',
   'gdp_per_capita','life_expectancy','diabetes_prevalence']

covidkeys = covidtotals.loc[:, totvars + demovars]

# generate a correlation matrix of the cumulative and demographic data
corrmatrix = covidkeys.corr(method="pearson")
corrmatrix

sns.heatmap(corrmatrix, xticklabels=corrmatrix.columns,
  yticklabels=corrmatrix.columns, cmap="coolwarm")
plt.title('Heat Map of Correlation Matrix')
plt.tight_layout()
plt.show()

# see if some countries have unexpected low or high death rates given number of cases
covidkeys['total_cases_q'] = \
  pd.qcut(covidkeys['total_cases_mill'],
  labels=['very low','low','medium','high','very high'],
  q=5, precision=0)
covidkeys['total_deaths_q'] = \
  pd.qcut(covidkeys['total_deaths_mill'],
  labels=['very low','low','medium','high','very high'],
  q=5, precision=0)

pd.crosstab(covidkeys.total_cases_q, covidkeys.total_deaths_q)
covidkeys[['total_cases_mill','total_deaths_mill','population_density']].mean()
covidkeys.mean()

covidtotals.loc[(covidkeys. \
  total_cases_q=="very high") & \
  (covidkeys.total_deaths_q=="medium")].T

covidtotals.loc[(covidkeys. \
  total_cases_q=="medium") & \
  (covidkeys.total_deaths_q=="very high")].T
  




