# Snippets

> Google Cloud BigQuery Warehouse Snippets

## Connect to BigQuery from Google Colab

```py
from google.colab import auth
auth.authenticate_user()
print('Authenticated')

############################################

query = """SELECT
    source_year AS year,
    COUNT(is_male) AS birth_count
FROM `bigquery-public-data.samples.natality`
GROUP BY year
ORDER BY year DESC
LIMIT 15""" 

project_id = 'silken-psyxxx-xxxxxx'

import pandas as pd
df = pd.read_gbq(query, project_id=project_id, dialect='standard')
df.head()

from google.cloud import bigquery
client = bigquery.Client(project=project_id)
df = client.query(query).to_dataframe()
df.head()
```