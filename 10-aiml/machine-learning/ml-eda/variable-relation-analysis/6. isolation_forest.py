# import pandas, matplotlib, and scikit learn
import pandas as pd
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
pd.set_option('display.width', 70)
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 7)
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

# create a standardized analysis data frame
analysisvars = ['location','total_cases_mill','total_deaths_mill',
  'population_density','aged_65_older','gdp_per_capita']
standardizer = StandardScaler()
covidanalysis = covidtotals.loc[:, analysisvars].dropna()
covidanalysisstand = standardizer.fit_transform(covidanalysis.iloc[:, 1:])

# run an isolation forest model to detect outliers
clf=IsolationForest(n_estimators=50, max_samples='auto',
  contamination=.1, max_features=1.0)
clf.fit(covidanalysisstand)
covidanalysis['anomaly'] = clf.predict(covidanalysisstand)
covidanalysis['scores'] = clf.decision_function(covidanalysisstand)
covidanalysis.anomaly.value_counts()

# view the outliers
inlier, outlier = covidanalysis.loc[covidanalysis.anomaly==1],\
  covidanalysis.loc[covidanalysis.anomaly==-1]
outlier[['location','total_cases_mill','total_deaths_mill',
  'scores']].sort_values(['scores']).head(10)

# plot the inliers and outliers
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title('Isolation Forest Anomaly Detection')
ax.set_zlabel("Cases Per Million (thous.)")
ax.set_xlabel("GDP Per Capita (thous.)")
ax.set_ylabel("Aged 65 Plus %")
ax.scatter3D(inlier.gdp_per_capita/1000, inlier.aged_65_older, inlier.total_cases_mill/1000, label="inliers", c="blue")
ax.scatter3D(outlier.gdp_per_capita/1000, outlier.aged_65_older, outlier.total_cases_mill/1000, label="outliers", c="red")
ax.legend()
plt.show()
