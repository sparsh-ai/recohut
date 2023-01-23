
"""
!apt install unixodbc-dev
!pip install pyodbc

%%sh
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get -q -y install msodbcsql17
"""

import os
import pyodbc
import urllib
import pandas as pd
from sqlalchemy import create_engine

driver = [item for item in pyodbc.drivers()][-1]
conn_string = f'Driver={driver};Server=tcp:server.<domain>.com,<port>;Database=<db>;Uid=<userid>;Pwd=<pass>;Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;'
conn = pyodbc.connect(conn_string)
cursor = conn.cursor()

# params = urllib.parse.quote_plus(conn_string)
# conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
# engine_feat = create_engine(conn_str, echo=True)
# print(engine_feat.table_names())

tname = 'tbl_Final_Lable_Data_18_n_19'
query = f'select count(*) from {tname}'

cursor.execute(query)
cursor.fetchall()

query = f'select top 5 * from {tname}'
df = pd.read_sql(query, conn)
df.info()