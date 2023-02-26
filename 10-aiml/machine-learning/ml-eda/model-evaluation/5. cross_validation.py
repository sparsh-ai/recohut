# import pandas, numpy, and matplotlib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
import pprint
pd.set_option('display.width', 150)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 100)
pd.options.display.float_format = '{:,.3f}'.format

# load the NLS data
landtemps = pd.read_csv("data/landtemps2019avgs.csv")

feature_cols = ['latabs','elevation']

X_train, X_test, y_train, y_test =  \
  train_test_split(landtemps[feature_cols],\
  landtemps[['avgtemp']], test_size=0.1, random_state=0)

kf = KFold(n_splits=5, shuffle=True, random_state=0)
      
# use linear regression for recursive feature elimination
def getscores(model):
  pipeline = make_pipeline(StandardScaler(), model)
  scores = cross_validate(pipeline, X=X_train, y=y_train,
    cv=kf, scoring=['r2'], n_jobs=1)
  scorelist.append(dict(model=str(model),
    fit_time=scores['fit_time'].mean(),
    r2=scores['test_r2'].mean()))


scorelist = []
getscores(LinearRegression())
getscores(RandomForestRegressor(max_depth=2))
getscores(KNeighborsRegressor(n_neighbors=5))

scorelist

pipeline = make_pipeline(StandardScaler(), LinearRegression())
scores = cross_validate(pipeline, X=X_train, y=y_train,
  cv=kf, scoring=['r2'], n_jobs=1)
scores
