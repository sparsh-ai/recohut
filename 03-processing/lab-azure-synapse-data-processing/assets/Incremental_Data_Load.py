#!/usr/bin/env python
# coding: utf-8

# ## Incremental_Data_Load
# 
# 
# 

# In[2]:


get_ipython().run_cell_magic('spark', '', 'val date = java.time.LocalDate.now\nval transaction_today = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/transaction-data/TransDtls-" + date +".csv")\ndisplay(transaction_today)\n')


# In[7]:


get_ipython().run_cell_magic('spark', '', 'transaction_today.createOrReplaceTempView("transaction_today")\n')


# In[5]:


get_ipython().run_cell_magic('sql', '', 'CREATE DATABASE IF NOT EXISTS DataLoad;\nCREATE TABLE IF NOT EXISTS DataLoad.transaction_data(transaction_id int, order_id int, Order_dt Date,customer_id varchar(100),product_id varchar(100),quantity int,cost int)\nUSING DELTA\n')


# In[8]:


get_ipython().run_cell_magic('sql', '', 'Merge into DataLoad.transaction_data source\nUsing transaction_today target on source.transaction_id = target.transaction_id\nWHEN MATCHED THEN UPDATE SET *\nWHEN NOT MATCHED AND (target.transaction_id is not null or target.order_id is not null or target.customer_id is not null)\nTHEN INSERT *\n')


# In[ ]:




