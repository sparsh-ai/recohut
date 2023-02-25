# Databricks notebook source
# MAGIC %md
# MAGIC # Configuration
# MAGIC In this notebook we setup your environment for creating OMOP CDM LakeHouse with Delta.
# MAGIC By default this notebook downloads both OMOP Vocabs as well as sample synthetic dataset of ~90K patients.
# MAGIC If you do not want to download the records change the `download_records` parameter to `No`.
# MAGIC 
# MAGIC Note: All notebooks for this solution accelerator have been tested to work on databricks runtime `8.0ML`.

# COMMAND ----------

dbutils.widgets.text('root_path','/FileStore/health-lakehouse/')
dbutils.widgets.text('vocab_path','/FileStore/omopvocab/')
dbutils.widgets.text('synth_in','/FileStore/hls/synthea/data/')
dbutils.widgets.dropdown('download_records','No',['Yes','No'])
dbutils.widgets.dropdown('download_vocabs','No', ['Yes','No'])

# COMMAND ----------

root_path=dbutils.widgets.get('root_path')
vocab_path=dbutils.widgets.get('vocab_path')
synth_in=dbutils.widgets.get('synth_in')
download_records=dbutils.widgets.get('download_records')
download_vocabs=dbutils.widgets.get('download_vocabs')

# COMMAND ----------

print(f"You selected {download_records} for downloading databricks-hosted synthea records and {download_vocabs} for downloading OMOP vocabs")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 0. Create init Script for Simulating Patient Records (optional)
# MAGIC If you are planning to create your own synthetics patients (using `./data-gen/run-synthea.py` notebook), then in order to be able to distribute simulations you need to create an init script

# COMMAND ----------

dbutils.fs.put("dbfs:/FileStore/scripts/synthea-install.sh","""
#!/bin/bash
git clone https://github.com/synthetichealth/synthea.git
cd ./synthea
./gradlew build check test""", overwrite=True)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Setup paths
# MAGIC First let's create all paths that will be used for this solultion accelerator

# COMMAND ----------

import os
os.environ["root_path"]=f"/dbfs{root_path}"
os.environ["vocab_path"]=f"/dbfs{vocab_path}"
os.environ["synth_in"]=f"/dbfs{synth_in}"
os.environ["download_records"]=download_records
os.environ["download_vocabs"]=download_vocabs

# COMMAND ----------

dbutils.fs.mkdirs(root_path)
dbutils.fs.mkdirs(vocab_path)
dbutils.fs.mkdirs(synth_in)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Download vocabularies
# MAGIC Now we download OMOP CDM vocabularies. To accelerate the process, this notebook automatically downloads vocabulary tables and configures paths. You can also download vocabularies from [Athena](https://athena.ohdsi.org/search-terms/start) website.

# COMMAND ----------

if download_vocabs=='Yes':
  dbutils.fs.cp('s3://hls-eng-data-public/omop/OMOP-VOCAB.tar.gz',vocab_path)

# COMMAND ----------

# MAGIC %sh
# MAGIC if [ $download_vocabs == 'Yes' ]
# MAGIC then
# MAGIC   cd $vocab_path
# MAGIC   tar -xf OMOP-VOCAB.tar.gz
# MAGIC   ls
# MAGIC fi

# COMMAND ----------

# DBTITLE 1,List of all downloaded vocabulary tables
if dbutils.fs.ls(vocab_path):
  display(dbutils.fs.ls(vocab_path))
else:
  print('No vocabulary tables were found. Try again running with download_vocabs=Yes')

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Download pre-simulated synthetic records
# MAGIC We have also included synthetic patient records for this analysis. In the following cell, we downoad the dataset and copy it into the default path for synthetic data. Note that if you are using your own dataset - or generate your own data - you can skip this step.

# COMMAND ----------

if download_records=='Yes':
  dbutils.fs.cp('s3://hls-eng-data-public/synthea/dbxsynthea.tar.gz',synth_in)

# COMMAND ----------

# MAGIC %md
# MAGIC Now let's take a look at the dataset

# COMMAND ----------

if dbutils.fs.ls(synth_in):
  display(dbutils.fs.ls(f"{synth_in}/data"))
else:
  print('No records tables were found. Try again running with download_records=Yes')

# COMMAND ----------

# MAGIC %md
# MAGIC We have also included synthetic data based on `chronic heart failiour` and `covid-19` modules:

# COMMAND ----------

if dbutils.fs.ls(synth_in):
  display(dbutils.fs.ls(f"{synth_in}/data/Massachusetts/csv"))
else:
  print('No records tables were found. Try again running with download_records=Yes')

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