#!/usr/bin/env python
# coding: utf-8

# ## Notebook 1
# 
# 
# 

# In[1]:


df = spark.read.load('abfss://synapse@sparshstorage1.dfs.core.windows.net/CSV/covid-data.csv',
format='csv',
header=True
)
display(df.limit(10))


# In[3]:


df.createOrReplaceTempView("v1")


# In[4]:


get_ipython().run_cell_magic('sql', '', 'Describe v1;\n')


# In[5]:


get_ipython().run_cell_magic('sql', '', 'Create database sparksqldb;\nCreate or replace table sparksqldb.covid\nUSING Delta\nAS\nSelect date, continent,location, CAST(new_cases as int) as new_cases,\nCAST(new_deaths as int) as new_deaths from v1\n')


# In[6]:


get_ipython().run_cell_magic('sql', '', 'Describe table sparksqldb.covid;\n')


# In[7]:


get_ipython().run_cell_magic('sql', '', 'Delete from sparksqldb.covid where continent is NULL\n')


# In[8]:


get_ipython().run_cell_magic('sql', '', 'DESCRIBE DETAIL sparksqldb.covid\n')


# In[9]:


df2 =  spark.read.format("delta").option("versionAsOf", 0).load("/synapse/workspaces/sparshadesynapse/warehouse/sparksqldb.db/covid")
df2.createOrReplaceTempView("old_Data")


# In[11]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM old_Data WHERE continent IS NULL LIMIT 10\n')


# In[ ]:




