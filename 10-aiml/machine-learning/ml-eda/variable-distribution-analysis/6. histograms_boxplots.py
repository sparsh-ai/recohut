# import pandas, matplotlib, and statsmodels
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 53)
pd.set_option('display.max_columns', 6)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
landtemps = pd.read_csv("data/landtemps2019avgs.csv")
covidtotals = pd.read_csv("data/covidtotals.csv", parse_dates=["lastdate"])
covidtotals.set_index("iso_code", inplace=True)

# show histogram of cases per million
plt.hist(covidtotals['total_cases_mill'], bins=7)
plt.axvline(covidtotals.total_cases_mill.mean(), color='red',
   linestyle='dashed', linewidth=1, label='mean')
plt.axvline(covidtotals.total_cases_mill.median(), color='black',
   linestyle='dashed', linewidth=1, label='median')
plt.title("Total Covid Cases")
plt.xlabel('Cases per Million')
plt.ylabel("Number of Countries")
plt.legend()
plt.show()

plt.hist(landtemps['avgtemp'])
plt.axvline(landtemps.avgtemp.mean(), color='red', linestyle='dashed', linewidth=1, label='mean')
plt.axvline(landtemps.avgtemp.median(), color='black', linestyle='dashed', linewidth=1, label='median')
plt.title("Average Land Temperatures")
plt.xlabel('Average Temperature')
plt.ylabel("Number of Weather Stations")
plt.legend()
plt.show()

landtemps.loc[landtemps.avgtemp<-25,['station','country','avgtemp']].\
  sort_values(['avgtemp'], ascending=True)


plt.boxplot(covidtotals.total_cases_mill.dropna(), labels=['Total Cases per Million'])
plt.annotate('extreme value threshold', xy=(1.05,157000), xytext=(1.15,157000), size=7, arrowprops=dict(facecolor='black', headwidth=2, width=0.5, shrink=0.02))
plt.annotate('3rd quartile', xy=(1.08,64800), xytext=(1.15,64800), size=7, arrowprops=dict(facecolor='black', headwidth=2, width=0.5, shrink=0.02))
plt.annotate('median', xy=(1.08,19500), xytext=(1.15,19500), size=7, arrowprops=dict(facecolor='black', headwidth=2, width=0.5, shrink=0.02))
plt.annotate('1st quartile', xy=(1.08,2500), xytext=(1.15,2500), size=7, arrowprops=dict(facecolor='black', headwidth=2, width=0.5, shrink=0.02))
plt.title("Boxplot of Total Cases")
plt.show()

plt.boxplot(landtemps.avgtemp.dropna(), labels=['Boxplot of Average Temperature'])
plt.title("Average Temperature")
plt.show()


fig = plt.figure()
fig.suptitle("Violin Plots of Covid Cases and Land Temperatures")
ax1 = plt.subplot(2,1,1)
ax1.set_xlabel("Cases per Million")
sns.violinplot(data=covidtotals.total_cases_mill, color="lightblue", orient="h")
ax1.set_yticklabels([])
ax2 = plt.subplot(2,1,2)
ax2.set_xlabel("Average Temperature")
sns.violinplot(data=landtemps.avgtemp, color="wheat",  orient="h")
ax2.set_yticklabels([])
plt.tight_layout()
plt.show()

