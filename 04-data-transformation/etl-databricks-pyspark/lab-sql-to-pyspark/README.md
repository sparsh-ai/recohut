# SQL to PySpark Code Conversion

```sh
pip install databathing
```

```py
from databathing import Pipeline
pipeline = Pipeline("SELECT * FROM Test WHERE info = 1")
x = pipeline.parse()
print(x)
```

Output:
```
final_df = Test\
.filter("info = 1")\
.selectExpr("*")
```