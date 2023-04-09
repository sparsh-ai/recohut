# import pandas, numpy, and matplotlib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.cluster import DBSCAN
from sklearn.impute import KNNImputer
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

import os
import sys
sys.path.append(os.getcwd() + "/helperfunctions")
import incomegap as ig

# get income gap data
gap = ig.gap
num_cols = ig.num_cols

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

# setup the pipeline and instantiate a DBSCAN object and fit the model
pipe1 = make_pipeline(MinMaxScaler(),
  KNNImputer(n_neighbors=5))

gap_enc = pd.DataFrame(pipe1.fit_transform(gap),
  columns=num_cols, index=gap.index)

dbscan = DBSCAN(eps=0.35, min_samples=5)

dbscan.fit(gap_enc)

silhouette_score(gap_enc, dbscan.labels_)

# take a closer look at the clusters
gap_enc['cluster'] = dbscan.labels_

gap_enc.cluster.value_counts().sort_index()

gap_enc = \
 gap_enc.loc[gap_enc.cluster!=-1]

gap_enc[['cluster'] + num_cols].\
  groupby(['cluster']).mean().T


# plot the points by cluster
fig = plt.figure()
plt.suptitle("Cluster for each Country")
ax = plt.axes(projection='3d')
ax.set_xlabel("Maternal Mortality")
ax.set_ylabel("Adolescent Birth Rate")
ax.set_zlabel("Gender Inequality")
ax.scatter3D(gap_enc.maternalmortality,
  gap_enc.adolescentbirthrate,
  gap_enc.genderinequality, c=gap_enc.cluster, 
  cmap="brg")
plt.tight_layout()
plt.show()


