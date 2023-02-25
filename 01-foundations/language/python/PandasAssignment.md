# PandasAssignment

Q1. How do you load a CSV file into a Pandas DataFrame?
```
# Using read_csv() function

import pandas as pd
df = pd.read_csv('sample.csv')
```

Q2. How do you check the data type of a column in a Pandas DataFrame?
```
# Using dtype

import pandas as pd
my_dict = {"name": ['Vivek', 'Dave', 'Tom'], "age": [23, 40, 35]}
df = pd.DataFrame(my_dict)
print(df.dtypes)
```

Q3. How do you select rows from a Pandas DataFrame based on a condition?
```
import pandas as pd
my_dict = {"name": ['Vivek', 'Dave', 'Tom'], "age": [23, 40, 35]}
df = pd.DataFrame(my_dict)

# Selecting rows with age greater than 30
print(df[df['age'] > 30])
```

Q4. How do you rename columns in a Pandas DataFrame?
```
import pandas as pd
my_dict = {"name": ['Vivek', 'Dave', 'Tom'], "age": [23, 40, 35]}
df = pd.DataFrame(my_dict)
df.rename(columns = {'name': 'first name'}, inplace = True)
print(df)
```

Q5. How do you drop columns in a Pandas DataFrame?
```
import pandas as pd
my_dict = {"name": ['Vivek', 'Dave', 'Tom'], "age": [23, 40, 35]}
df = pd.DataFrame(my_dict)

# Using del
del df['age']
print(df)

df = pd.DataFrame(my_dict)

# Using pop
df.pop('age')
print(df)
```

Q6. How do you find the unique values in a column of a Pandas DataFrame?
```
import pandas as pd
my_dict = {"a": [1, 2, 3, 2, 1, 5], "b": [23, 40, 35, 40, 23, 26]}
df = pd.DataFrame(my_dict)
print(df['a'].unique())
```

Q7. How do you find the number of missing values in each column of a Pandas DataFrame?
```
import pandas as pd
my_dict = {"a": [1, 2, None, 2, 1, 5], "b": [None, 40, 35, None, 23, 26]}
df = pd.DataFrame(my_dict)
print(df.isnull().sum())
```

Q8. How do you fill missing values in a Pandas DataFrame with a specific value?
```
import pandas as pd
my_dict = {"a": [1, 2, None, 2, 1, 5], "b": [None, 40, 35, None, 23, 26]}
df = pd.DataFrame(my_dict)
df.fillna(999, inplace = True)
print(df)
```

Q9. How do you concatenate two Pandas DataFrames?
```
import pandas as pd
df1 = pd.DataFrame(data=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
df2 = pd.DataFrame(data=[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]])
df3 = pd.concat([df1, df2])
print(df3)
```

Q10. How do you merge two Pandas DataFrames on a specific column?
```
import pandas as pd
df1 = pd.DataFrame(data={'City': ['New York', 'Chicago', 'Los Angeles'], 'Temperature': [65, 70, 75]})
df2 = pd.DataFrame(data={'City': ['New York', 'Chicago', 'Los Angeles'], 'Humidity': [60, 50, 55]})
df3 = pd.merge(df1, df2, on = 'City')
print(df3)
```

Q11. How do you group data in a Pandas DataFrame by a specific column and apply an aggregation function?
```
import pandas as pd
df = pd.DataFrame({'Animal': ['Dog', 'Cat', 'Dog', 'Fish', 'Fish', 'Fish'],
                   'Age': [2, 3, 2, 1, 2, 3]})

print(df.groupby('Animal').sum())
print(df.groupby('Animal').max())
```

Q12. How do you pivot a Pandas DataFrame?
```
import pandas as pd
df = pd.DataFrame({'Animal': ['Dog', 'Cat', 'Dog', 'Fish', 'Fish', 'Fish'],
                   'Size': ['Small', 'Small', 'Medium', 'Small', 'Medium', 'Large'],
                   'Age': [2, 3, 2, 1, 2, 3]})

print(df.pivot(index = 'Animal', columns = ['Size']))
```

Q13. How do you change the data type of a column in a Pandas DataFrame?
```
import pandas as pd
df = pd.DataFrame({'Animal': ['Dog', 'Cat', 'Dog', 'Fish', 'Fish', 'Fish'],
                   'Size': ['Small', 'Small', 'Medium', 'Small', 'Medium', 'Large'],
                   'Age': [2, 3, 2, 1, 2, 3]})

df['Age'] = df['Age'].astype(float)
print(df.dtypes)
```

Q14. How do you sort a Pandas DataFrame by a specific column?
```
import pandas as pd
df = pd.DataFrame({'Animal': ['Dog', 'Cat', 'Dog', 'Fish', 'Fish', 'Fish'],
                   'Size': ['Small', 'Small', 'Medium', 'Small', 'Medium', 'Large'],
                   'Age': [2, 3, 2, 1, 2, 3]})

df.sort_values(by = ['Age'], inplace = True)
print(df)
```

Q15. How do you create a copy of a Pandas DataFrame?
```
import pandas as pd
df = pd.DataFrame({'Animal': ['Dog', 'Cat', 'Dog', 'Fish', 'Fish', 'Fish'],
                   'Size': ['Small', 'Small', 'Medium', 'Small', 'Medium', 'Large'],
                   'Age': [2, 3, 2, 1, 2, 3]})

df2 = df.copy()
print(df2)
```

Q16. How do you filter rows of a Pandas DataFrame by multiple conditions?
```
import pandas as pd
df = pd.DataFrame({'Name': ['John', 'Jane', 'Bob', 'Alice', 'Mike', 'Carol', 'Steve', 'Kate', 'Adam', 'Tom'],
                   'Age': [35, 25, 55, 46, 32, 35, 30, 30, 26, 27],
                   'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M']})

new_df = df.loc[(df['Age'] > 30) & (df['Gender'] == 'M')]
print(new_df)
```

Q17. How do you calculate the mean of a column in a Pandas DataFrame?
```
import pandas as pd
df = pd.DataFrame({'Name': ['John', 'Jane', 'Bob', 'Alice', 'Mike', 'Carol', 'Steve', 'Kate', 'Adam', 'Tom'],
                   'Age': [35, 25, 55, 46, 32, 35, 30, 30, 26, 27],
                   'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M']})

print(df['Age'].mean())
```

Q18. How do you calculate the standard deviation of a column in a Pandas DataFrame?
```
import pandas as pd
df = pd.DataFrame({'Name': ['John', 'Jane', 'Bob', 'Alice', 'Mike', 'Carol', 'Steve', 'Kate', 'Adam', 'Tom'],
                   'Age': [35, 25, 55, 46, 32, 35, 30, 30, 26, 27],
                   'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M']})

print(df['Age'].std())
```

Q19. How do you calculate the correlation between two columns in a Pandas DataFrame?
```
import pandas as pd
df = pd.DataFrame({'X': [1, 2, 3, 4, 5],
                   'Y': [2, 4, 6, 8, 10]})

corr = df['X'].corr(df['Y'])
print(corr)
```

Q20. How do you select specific columns in a DataFrame using their labels?
```
import pandas as pd
df = pd.DataFrame({'Name': ['John', 'Jane', 'Bob', 'Alice', 'Mike', 'Carol', 'Steve', 'Kate', 'Adam', 'Tom'],
                   'Age': [35, 25, 55, 46, 32, 35, 30, 30, 26, 27],
                   'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M']})

print(df.loc[:, ['Name', 'Gender']])
```

Q21. How do you select specific rows in a DataFrame using their indexes?
```
import pandas as pd
df = pd.DataFrame({'Name': ['John', 'Jane', 'Bob', 'Alice', 'Mike', 'Carol', 'Steve', 'Kate', 'Adam', 'Tom'],
                   'Age': [35, 25, 55, 46, 32, 35, 30, 30, 26, 27],
                   'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M']})

print(df.iloc[3:9])
```

Q22. How do you sort a DataFrame by a specific column?
```
import pandas as pd
df = pd.DataFrame({'Animal': ['Dog', 'Cat', 'Dog', 'Fish', 'Fish', 'Fish'],
                   'Size': ['Small', 'Small', 'Medium', 'Small', 'Medium', 'Large'],
                   'Age': [2, 3, 2, 1, 2, 3]})

df.sort_values(by = ['Age'], inplace = True)
print(df)
```

Q23. How do you create a new column in a DataFrame based on the values of another column?
```
import pandas as pd
df = pd.DataFrame({'Age': [35, 25, 10, 46, 32, 12, 30, 30, 5, 27],
                   'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M']})
df['Eligible'] = df['Age'] > 18
print(df)
```

Q24. How do you remove duplicates from a DataFrame?
```
import pandas as pd
df = pd.DataFrame({'ID': [1, 2, 2, 3, 3, 4, 4, 5],
                   'Name': ['John', 'Jane', 'Jane', 'Bob', 'Bob', 'Alice', 'Alice', 'Mike']})
                   
df = df.drop_duplicates()
print(df)
```

Q25. What is the difference between .loc and .iloc in Pandas?
- ***.loc[]*** is used to select rows and columns by their labels
- ***.iloc[]*** is used to select rows and columns by their position. It uses an integer index.
