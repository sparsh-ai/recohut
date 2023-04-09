# Window Functions in Spark

```python
from pyspark.sql.window import Window
from pyspark.sql import functions as F

w = Window.partitionBy('deptid').orderBy('salary')
df = df.withColumn('sum', F.sum('salary').over(w))
```
