# Snowflake Getting Started

## Connect to Snowflake using Python

Installation:

```sh
pip install --upgrade snowflake-connector-python snowflake-connector-python[pandas]
```

```py
import snowflake.connector

ACCOUNT = ''
USERID = ''
PASSWORD = ''
WAREHOUSE = ''
DATABASE = ''
SCHEMA = ''

conn = snowflake.connector.connect(
                user=USERID,
                password=PASSWORD,
                account=ACCOUNT,
                warehouse=WAREHOUSE,
                database=DATABASE,
                schema=SCHEMA
                )
curs = conn.cursor()
result = curs.execute("SELECT * FROM CUSTOMER LIMIT 10")

result.fetchall()
result.fetch_pandas_all()
```

## Transformation in Local compute vs in Warehouse

:::tip
Local compute is comparative to an ETL process and Snowflake compute is comparative to an ELT process.
:::

**Local compute**

```py
import pandas as pd

%%time
query = "SELECT * FROM LINEITEM"
lineitem_df = pd.read_sql(query, conn)
lineitem_df.groupby('L_SHIPMODE')['L_SHIPINSTRUCT'].count().plot()
```

**Compute in Snowflake

```py
import pandas as pd

%%time
query = "SELECT L_SHIPMODE, COUNT(*) FROM LINEITEM GROUP BY L_SHIPMODE;"
lineitem_df = pd.read_sql(query, conn)
lineitem_df.set_index('L_SHIPMODE').plot()
```

:::note
Local compute would take ~1 min because the main bottleneck is data transfer of 6M+ records from warehouse to staging/compute environment. In contrast to this, Snowflake compute would take 1-2 secs only because we removed this bottleneck and the data is being transformed directly in the warehouse.
:::