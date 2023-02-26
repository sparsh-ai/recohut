# import pandas, pyod, and sklearn
import pandas as pd
from pyod.models.knn import KNN
from sklearn.preprocessing import StandardScaler
pd.set_option('display.width', 85)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 20)
pd.options.display.float_format = '{:,.2f}'.format
covidtotals = pd.read_csv("data/covidtotals.csv")
covidtotals.set_index("iso_code", inplace=True)

# create a standardized dataset of the analysis variables

standardizer = StandardScaler()
analysisvars = ['location','total_cases_mill','total_deaths_mill',
  'population_density','diabetes_prevalence','aged_65_older',
  'gdp_per_capita']
covidanalysis = covidtotals.loc[:, analysisvars].dropna()
covidanalysisstand = standardizer.fit_transform(covidanalysis.iloc[:, 1:])

# run the KNN model and generate anomaly scores
clf_name = 'KNN'
clf = KNN(contamination=0.1)
clf.fit(covidanalysisstand)
y_pred = clf.labels_
y_scores = clf.decision_scores_

# show the predictions from the model
pred = pd.DataFrame(zip(y_pred, y_scores), 
  columns=['outlier','scores'], 
  index=covidanalysis.index)
pred.outlier.value_counts()
pred.groupby(['outlier'])[['scores']].\
  agg(['min','median','max'])

# show covid data for the outliers
covidanalysis = covidanalysis.join(pred).\
  loc[:,analysisvars + ['scores']].\
  sort_values(['scores'], ascending=False)
covidanalysis.head(10)

# show the score for Japan
covidanalysis.loc['JPN','scores']

