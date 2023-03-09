# import pandas, numpy, and matplotlib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics.cluster import rand_score
from sklearn.impute import KNNImputer

import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.2f}'.format

# load the income gap data
un_income_gap = pd.read_csv("data/un_income_gap.csv")
un_income_gap.set_index('country', inplace=True)
un_income_gap['incomeratio'] = \
  un_income_gap.femaleincomepercapita / \
    un_income_gap.maleincomepercapita
un_income_gap['educratio'] = \
  un_income_gap.femaleyearseducation / \
     un_income_gap.maleyearseducation
un_income_gap['laborforcepartratio'] = \
  un_income_gap.femalelaborforceparticipation / \
     un_income_gap.malelaborforceparticipation
un_income_gap['humandevratio'] = \
  un_income_gap.femalehumandevelopment / \
     un_income_gap.malehumandevelopment
     
num_cols = ['educratio','laborforcepartratio','humandevratio',
  'genderinequality','maternalmortality','incomeratio',
  'adolescentbirthrate', 'femaleperparliament','incomepercapita']

gap = un_income_gap[num_cols]

gap.agg(['count','min','median','max']).T

# look at some correlations
corrmatrix = gap.corr(method="pearson")

sns.heatmap(corrmatrix, xticklabels=corrmatrix.columns,
  yticklabels=corrmatrix.columns, cmap="coolwarm")
plt.title('Heat Map of Correlation Matrix')
plt.tight_layout()
plt.show()


# instantiate a kmeans object and fit the model
pipe1 = make_pipeline(MinMaxScaler(), KNNImputer(n_neighbors=5))

gap_enc = pd.DataFrame(pipe1.fit_transform(gap),
  columns=num_cols, index=gap.index)

kmeans = KMeans(n_clusters=3, random_state=0)

kmeans.fit(gap_enc)

silhouette_score(gap_enc, kmeans.labels_)

# get the cluster values
gap_enc['cluster'] = kmeans.labels_

gap_enc.cluster.value_counts().sort_index()

pred = pd.Series(kmeans.fit_predict(gap_enc))
pred.value_counts().sort_index()

gap_enc[['cluster'] + num_cols].\
  groupby(['cluster']).mean().T

# look at the centers
centers = kmeans.cluster_centers_
centers.shape
np.set_printoptions(precision=2)
centers

# plot the clusters against some of the features
fig = plt.figure()
plt.suptitle("Cluster for each Country")
ax = plt.axes(projection='3d')
ax.set_xlabel("Maternal Mortality")
ax.set_ylabel("Adolescent Birth Rate")
ax.set_zlabel("Income Ratio")
ax.scatter3D(gap_enc.maternalmortality,
  gap_enc.adolescentbirthrate,
  gap_enc.incomeratio, c=gap_enc.cluster, cmap="brg")
for j in range(3):
  ax.text(centers[j, num_cols.index('maternalmortality')],
  centers[j, num_cols.index('adolescentbirthrate')],
  centers[j, num_cols.index('incomeratio')],
  c='black', s=j, fontsize=20, fontweight=800)
plt.tight_layout()
plt.show()

gap_enc = gap_enc[num_cols]

kmeans2 = KMeans(n_clusters=5, random_state=0)

kmeans2.fit(gap_enc)

silhouette_score(gap_enc, kmeans2.labels_)

gap_enc['cluster2'] = kmeans2.labels_

gap_enc.cluster2.value_counts().sort_index()


rand_score(kmeans.labels_, kmeans2.labels_)

centers2 = kmeans2.cluster_centers_


fig = plt.figure()
plt.suptitle("Cluster for each Country")
ax = plt.axes(projection='3d')
ax.set_xlabel("Maternal Mortality")
ax.set_ylabel("Adolescent Birth Rate")
ax.set_zlabel("Income Ratio")
ax.scatter3D(gap_enc.maternalmortality,
  gap_enc.adolescentbirthrate,
  gap_enc.incomeratio, c=gap_enc.cluster2, cmap="brg")
for j in range(5):
  ax.text(centers2[j, num_cols.index('maternalmortality')],
  centers2[j, num_cols.index('adolescentbirthrate')],
  centers2[j, num_cols.index('incomeratio')],
  c='black', s=j, fontsize=20, fontweight=800)

plt.tight_layout()
plt.show()

gap_enc = gap_enc[num_cols]

iner_scores = []
sil_scores = []
for j in range(2,20):
  kmeans=KMeans(n_clusters=j, random_state=0)
  kmeans.fit(gap_enc)
  iner_scores.append(kmeans.inertia_)
  sil_scores.append(silhouette_score(gap_enc,
    kmeans.labels_))


plt.title('Elbow Plot')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.plot(range(2,20),iner_scores)


plt.title('Silhouette Score')
plt.xlabel('k')
plt.ylabel('Silhouette Score')
plt.plot(range(2,20),sil_scores)

