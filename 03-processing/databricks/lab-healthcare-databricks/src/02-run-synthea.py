# Databricks notebook source
# MAGIC %md
# MAGIC # Simulating patient records with <img src="https://synthetichealth.github.io/synthea/assets/img/logo/synthea_sprites-1-long-trans.png", width=300 >[...](https://synthetichealth.github.io/synthea/)
# MAGIC 
# MAGIC 
# MAGIC `Synthea(TM) is a Synthetic Patient Population Simulator. The goal is to output synthetic, realistic (but not real), patient data and associated health records in a variety of formats.`
# MAGIC In this notebook, we show how to simulate patient records in parallele for patients accross the US. You can modify the code for your experiments

# COMMAND ----------

dbutils.widgets.text('synth_out','/FileStore/hls/synthea/data/')
synth_out=dbutils.widgets.get('synth_out')

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Cluster setup
# MAGIC In order to be able to distribute the simulation accross many states, you first need to make sure that the synthea simulator is installed on all workers. To do this, you need to specify the [init script](https://docs.databricks.com/clusters/init-scripts.html#cluster-node-initialization-scripts) path created during the configuration (`./0-config/config.py`) to your cluster. 
# MAGIC We recommned chosing a medium size cluster, depending on the total number of patients you need to simulate.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Run synthea simulations in parallele

# COMMAND ----------

# MAGIC %md
# MAGIC specify total number of samples to generate accross states

# COMMAND ----------

n_samples=50e3
synth_out=global_paths['synth_out']['value']
print(synth_out)

# COMMAND ----------

try:
  dbutils.fs.ls(synth_out)
except:
  dbutils.fs.mkdirs(synth_out)

# COMMAND ----------

# MAGIC %md
# MAGIC We use demographics file from synthea to sample population size for each state. You can specify your own demographics information and read it the same way into a spark dataframe.

# COMMAND ----------

import pandas as pd
df=pd.read_csv("/synthea/src/main/resources/geography/demographics.csv")[['STNAME','TOT_POP']].groupby('STNAME').sum()
df['STATE']=df.index
df.head()

# COMMAND ----------

scale=int(df['TOT_POP'].sum()//n_samples)

# COMMAND ----------

# MAGIC %md
# MAGIC Next step is to define a python wrapper function to run synthea. This function takes state and population size as parameter. `run-parameters` can be modified based on synthea configurations.

# COMMAND ----------

import subprocess
from subprocess import PIPE
import os

def run_synthea(state,pop_size):
  
  run_params={"-p": str(pop_size),
   "--exporter.fhir.export":"false",
   "--exporter.csv.export": "true",
   "--exporter.baseDirectory":f'/dbfs{synth_out}/{state}',
   "--exporter.csv.folder_per_run": "true",
   "--generate.log_patients.detail": "none",
   "--exporter.clinical_note.export" : "false"
  }

  command=["./run_synthea", state]
  options=[param for params in run_params.items() for param in params]
  
  p1=subprocess.Popen(command+options,stdout=PIPE,stderr=PIPE,cwd="/synthea")
  stdout, stderr = p1.communicate()
  return(stdout)

# COMMAND ----------

# MAGIC %md
# MAGIC Finally, you can distribute simulations using spark udf.

# COMMAND ----------

from pyspark.sql.functions import udf, col
@udf
def run_synthea_udf(s,p):
  return(run_synthea(s,p//scale))
              
spark.createDataFrame(df).repartition(50).select(run_synthea_udf('STATE','TOT_POP')).collect()

# COMMAND ----------

# MAGIC %md
# MAGIC Copyright / License info of the notebook. Copyright Databricks, Inc. [2021].  The source in this notebook is provided subject to the [Databricks License](https://databricks.com/db-license-source).  All included or referenced third party libraries are subject to the licenses set forth below.
# MAGIC 
# MAGIC |Library Name|Library License|Library License URL|Library Source URL| 
# MAGIC | :-: | :-:| :-: | :-:|
# MAGIC |Smolder |Apache-2.0 License| https://github.com/databrickslabs/smolder | https://github.com/databrickslabs/smolder/blob/master/LICENSE|
# MAGIC |Synthea|Apache License 2.0|https://github.com/synthetichealth/synthea/blob/master/LICENSE| https://github.com/synthetichealth/synthea|
# MAGIC | OHDSI/CommonDataModel| Apache License 2.0 | https://github.com/OHDSI/CommonDataModel/blob/master/LICENSE | https://github.com/OHDSI/CommonDataModel |
# MAGIC | OHDSI/ETL-Synthea| Apache License 2.0 | https://github.com/OHDSI/ETL-Synthea/blob/master/LICENSE | https://github.com/OHDSI/ETL-Synthea |
# MAGIC |OHDSI/OMOP-Queries|||https://github.com/OHDSI/OMOP-Queries|
# MAGIC |The Book of OHDSI | Creative Commons Zero v1.0 Universal license.|https://ohdsi.github.io/TheBookOfOhdsi/index.html#license|https://ohdsi.github.io/TheBookOfOhdsi/|