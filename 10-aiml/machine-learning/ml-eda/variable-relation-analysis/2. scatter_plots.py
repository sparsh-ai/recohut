# import pandas, matplotlib, and seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 53)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)
landtemps = pd.read_csv("data/landtemps2019avgs.csv")

# do a scatterplot of total_cases by total_deaths
ax = sns.regplot(x="total_cases_mill", y="total_deaths_mill", data=covidtotals)
ax.set(xlabel="Cases Per Million", ylabel="Deaths Per Million", title="Total Covid Cases and Deaths by Country")
plt.show()

fig, axes = plt.subplots(1,2, sharey=True)
sns.regplot(x=covidtotals.aged_65_older, y=covidtotals.total_cases_mill, ax=axes[0])
sns.regplot(x=covidtotals.gdp_per_capita, y=covidtotals.total_cases_mill, ax=axes[1])
axes[0].set_xlabel("Aged 65 or Older")
axes[0].set_ylabel("Cases Per Million")
axes[1].set_xlabel("GDP Per Capita")
axes[1].set_ylabel("")
plt.suptitle("Age 65 Plus and GDP with Cases Per Million")
plt.tight_layout()
fig.subplots_adjust(top=0.92)
plt.show()


# show the high elevation points in a different color
low, high = landtemps.loc[landtemps.elevation<=1000], landtemps.loc[landtemps.elevation>1000]
low.shape[0], low.avgtemp.mean()
high.shape[0], high.avgtemp.mean()

plt.scatter(x="latabs", y="avgtemp", c="blue", data=low)
plt.scatter(x="latabs", y="avgtemp", c="red", data=high)
plt.legend(('low elevation', 'high elevation'))
plt.xlabel("Latitude (N or S)")
plt.ylabel("Average Temperature (Celsius)")
plt.title("Latitude and Average Temperature in 2019")
plt.show()

# show scatter plot with different regression lines by elevation group
landtemps['elevation_group'] = np.where(landtemps.elevation<=1000,'low','high')
sns.lmplot(x="latabs", y="avgtemp", hue="elevation_group", palette=dict(low="blue", high="red"), legend_out=False, data=landtemps)
plt.xlabel("Latitude (N or S)")
plt.ylabel("Average Temperature")
plt.legend(('low elevation', 'high elevation'), loc='lower left')
plt.yticks(np.arange(-60, 40, step=20))
plt.title("Latitude and Average Temperature in 2019")
plt.tight_layout()
plt.show()

# show this as a 3D plot
fig = plt.figure()
plt.suptitle("Latitude, Temperature, and Elevation in 2019")
ax = plt.axes(projection='3d')
ax.set_xlabel("Elevation")
ax.set_ylabel("Latitude")
ax.set_zlabel("Avg Temp")
ax.scatter3D(landtemps.elevation, landtemps.latabs, landtemps.avgtemp)
plt.show()
