# Outliers Handling

## Remove categorical outliers

```py
from scipy import stats
import numpy as np

def remove_cat_outliers(df, col, sd=3):
    x = df[col].value_counts()
    valid_ids = list(set(x[(np.abs(stats.zscore(x)) < sd)].tolist()))
    valid_ids = [str(x) for x in valid_ids]
    df = df[df[col].isin(valid_ids)]
    return df
```