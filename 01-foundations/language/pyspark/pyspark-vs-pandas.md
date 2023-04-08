# PySpark vs Pandas

Spark DataFrames were inspired by pandas, which also provides an abstraction on top of the data called a DataFrame. pandas is a widely adopted library for data manipulation and analytics. Many developers use it to extrapolate data using Python.

It may seem easy to confuse the two at the beginning, but there are many key differences between pandas and Spark. Most importantly, pandas was not built for scale; it was built to operate on data that fits into one machine’s memory. Consequently, it does not have the distributed Spark architecture. It also does not adhere to functional programming principles: pandas DataFrames are mutable.

|                           | Spark DataFrame | pandas DataFrame   |
|---------------------------|-----------------|--------------------|
| **Operation in parallel** | Yes             | Not out of the box |
| **Lazy evaluation**       | Yes             | No                 |
| **Immutable**             | Yes             | No                 |

Although, as you can see, there is no out-of-the-box way to operate in parallel over a pandas DataFrame, that does not mean it is entirely impossible. It simply means that you have to create a solution and consider the possible problems you might encounter (thread locks, race conditions, etc.) and their impact on the end result. Other differences are that Spark supports lazy evaluation, while in pandas, operations take place immediately as soon as the Python code line is executed, and DataFrames in pandas are not immutable. This makes it easy to operate on pandas DataFrames, as you don’t need to remember or be aware of the lazy execution approach—when you call a function, it is executed immediately and you can interact with the results right away. However, it also makes it challenging to scale using parallel or distributed computing.