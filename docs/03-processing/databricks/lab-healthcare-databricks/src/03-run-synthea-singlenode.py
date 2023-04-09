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
# MAGIC Use a single node cluster

# COMMAND ----------

# MAGIC %sh
# MAGIC git clone https://github.com/synthetichealth/synthea.git
# MAGIC cd ./synthea
# MAGIC ./gradlew build check test

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Run synthea simulations with specified module

# COMMAND ----------

n_samples=20e3

module_url="https://raw.githubusercontent.com/synthetichealth/synthea/master/src/main/resources/modules/congestive_heart_failure.json"
# module_url="https://raw.githubusercontent.com/synthetichealth/synthea/master/src/main/resources/modules/covid19/diagnose_blood_clot.json"
module_name=module_url.split('/')[-1].replace('.json','')
synth_out=f"{synth_out}/{module_name}"
module_path=f"{synth_out}/{module_name}.json"
print(f"synth_out:{synth_out}\nmodule_name:{module_name}\nmodule_path:{module_path}")

# COMMAND ----------

try:
  dbutils.fs.ls(synth_out.replace('/dbfs',''))
except:
  dbutils.fs.mkdirs(synth_out.replace('/dbfs',''))

# COMMAND ----------

import os
os.environ['MODULE_URL']=module_url
os.environ['SYNTH_OUT']=synth_out
os.environ['MODULE_PATH']=module_path

# COMMAND ----------

# MAGIC %sh
# MAGIC ls $SYNTH_OUT

# COMMAND ----------

# MAGIC %sh
# MAGIC wget $MODULE_URL -O $MODULE_PATH
# MAGIC ls $MODULE_PATH

# COMMAND ----------

# MAGIC %md
# MAGIC Next step is to define a python wrapper function to run synthea. This function takes state and population size as parameter. `run-parameters` can be modified based on synthea configurations.

# COMMAND ----------

import subprocess
from subprocess import PIPE
import os

def run_synthea(state,pop_size,module):
  
  run_params={"-p": str(pop_size),
   "--exporter.fhir.export":"false",
   "--exporter.csv.export": "true",
   "--exporter.baseDirectory":f'{synth_out}',
   "--exporter.csv.folder_per_run": "true",
   "--generate.log_patients.detail": "none",
   "--exporter.clinical_note.export" : "false",
   "--m": module
  }

  command=["./run_synthea", state]
  options=[param for params in run_params.items() for param in params]
  
  p1=subprocess.Popen(command+options,stdout=PIPE,stderr=PIPE,cwd="./synthea")
  stdout, stderr = p1.communicate()
  return(stdout)
#  return(command+options)

# COMMAND ----------

run_synthea("Massachusetts",20000,module_path)

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