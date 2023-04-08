# import pandas, matplotlib, and seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 70)
pd.set_option('display.max_columns', 9)
pd.set_option('display.max_rows', 25)
pd.options.display.float_format = '{:,.0f}'.format
nls97 = pd.read_csv("data/nls97.csv")
nls97.set_index("personid", inplace=True)
nls97.info()


# view some descriptive statistics
def gettots(x):
  out = {}
  out['min'] = x.min()
  out['qr1'] = x.quantile(0.25)
  out['med'] = x.median()
  out['qr3'] = x.quantile(0.75)
  out['max'] = x.max()
  out['count'] = x.count()
  return pd.Series(out)

nls97.groupby(['highestdegree'])['weeksworked17'].\
  apply(gettots).unstack()
  

# do boxplots for weeks worked by highest degree earned
myplt = sns.boxplot(x='highestdegree',y='weeksworked17', data=nls97,
  order=sorted(nls97.highestdegree.dropna().unique()))
myplt.set_title("Boxplots of Weeks Worked by Highest Degree")
myplt.set_xlabel('Highest Degree Attained')
myplt.set_ylabel('Weeks Worked 2017')
myplt.set_xticklabels(myplt.get_xticklabels(), rotation=60, horizontalalignment='right')
plt.tight_layout()
plt.show()

# view minimum, maximum, median, and first and third quartile values
covidtotals = pd.read_csv("data/covidtotals.csv", parse_dates=["lastdate"])
covidtotals.set_index("iso_code", inplace=True)

# do boxplots for cases per million by region
sns.boxplot(x='total_cases_mill', y='region', data=covidtotals)
sns.swarmplot(y="region", x="total_cases_mill", data=covidtotals, size=1.5, color=".3", linewidth=0)
plt.title("Boxplots of Total Cases Per Million by Region")
plt.xlabel("Cases Per Million")
plt.ylabel("Region")
plt.tight_layout()
plt.show()

