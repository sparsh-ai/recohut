# Databricks notebook source
# MAGIC %md
# MAGIC ## Running end-to-end workflow
# MAGIC <img src="https://drive.google.com/uc?export=view&id=1uqzzhMl148otHL399FRO1G8Sa9l_bohP", width=500>
# MAGIC 
# MAGIC By running this notebook, you will run the end-to-end pipeline and create OMOP 5.3.1 lakehouse from raw synthea records.

# COMMAND ----------

dbutils.widgets.text('root_path','/FileStore/health-lakehouse/')
dbutils.widgets.text('vocab_path','/FileStore/omopvocab/')
dbutils.widgets.text('synth_in','/FileStore/hls/synthea/data/')
dbutils.widgets.dropdown('download_records','Yes',['Yes','No'])
dbutils.widgets.dropdown('download_vocabs','Yes',['Yes','No'])
dbutils.widgets.text('min_timeout_minutes','600')

# COMMAND ----------

root_path=dbutils.widgets.get('root_path')
vocab_path=dbutils.widgets.get('vocab_path')
synth_in=dbutils.widgets.get('synth_in')

min_timeout=int(dbutils.widgets.get('min_timeout_minutes'))*60

download_records=dbutils.widgets.get('download_records')
download_vocabs=dbutils.widgets.get('download_vocabs')

# COMMAND ----------

# MAGIC %md
# MAGIC ### 0. Configure your environment

# COMMAND ----------

dbutils.notebook.run("./000-config/1-config", min_timeout, \
                     {"root_path": root_path, \
                      "vocab_path": vocab_path, \
                      "synth_in":synth_in,\
                      "download_records":download_records,\
                      "download_vocabs":download_vocabs\
                     })

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Ingest raw records

# COMMAND ----------

dbutils.notebook.run("./001-ingest/3-synthea-ingest", min_timeout, {"root_path": root_path,  "synth_in":synth_in})

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. OMOP 531 setup

# COMMAND ----------

dbutils.notebook.run("./002-omop-cdm/4-a_omop531_cdm_setup", min_timeout, {"root_path": root_path})

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. OMOP Vocab setup

# COMMAND ----------

dbutils.notebook.run("./002-omop-cdm/5-omop_vocab_setup", min_timeout, {"vocab_path": vocab_path})

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. ETL from Synthea to OMOP 5.3.1

# COMMAND ----------

dbutils.notebook.run("./003-etl/6-a_omop531_etl_synthea", min_timeout, {"root_path": root_path})

# COMMAND ----------

# MAGIC %md
# MAGIC # 5. Test your tables

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5.1 Quey Example 1
# MAGIC patients with Non-small cell lung cancer

# COMMAND ----------

# MAGIC %sql
# MAGIC USE OMOP531;
# MAGIC SELECT gender, age, count(*) num_patients 
# MAGIC   FROM -- patient with Non-small cell lung cancer, age, gender 
# MAGIC     ( 
# MAGIC       SELECT DISTINCT condition.person_id , gender.concept_name As GENDER , EXTRACT( YEAR 
# MAGIC       FROM CONDITION_ERA_START_DATE ) - year_of_birth AS age 
# MAGIC       FROM condition_era condition 
# MAGIC       JOIN 
# MAGIC       ( 
# MAGIC         SELECT DISTINCT descendant_concept_id 
# MAGIC         FROM relationship 
# MAGIC         JOIN concept_relationship rel 
# MAGIC         USING( relationship_id ) 
# MAGIC         JOIN concept concept1 ON concept1.concept_id = concept_id_1 
# MAGIC         JOIN concept_ancestor ON ancestor_concept_id = concept_id_2 
# MAGIC         WHERE concept1.concept_id=4115276 AND current_date() BETWEEN rel.valid_start_date 
# MAGIC         AND rel.valid_end_date 
# MAGIC       )
# MAGIC   ON descendant_concept_id = condition_concept_id 
# MAGIC   JOIN person ON person.person_id = condition.person_id 
# MAGIC   JOIN concept gender ON gender.concept_id = gender_concept_id ) 
# MAGIC   GROUP BY gender, age 
# MAGIC   ORDER BY gender, age;

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5.2 Quey Example 2
# MAGIC Cohort of patients with atrial fibrillation with 3 years of record and no exposure to warfarin

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 1 AS cohort_definition_id,
# MAGIC AFib.person_id AS subject_id,
# MAGIC AFib.condition_start_date AS cohort_start_date,
# MAGIC observation_period.observation_period_end_date AS cohort_end_date
# MAGIC FROM (
# MAGIC   SELECT person_id, min(condition_start_date) as condition_start_date
# MAGIC   FROM condition_occurrence
# MAGIC   WHERE condition_concept_id IN (SELECT descendant_concept_id FROM 
# MAGIC   concept_ancestor WHERE ancestor_concept_id IN 
# MAGIC   (313217 /*atrial fibrillation*/))
# MAGIC   GROUP BY person_id
# MAGIC ) AFib
# MAGIC   INNER JOIN observation_period
# MAGIC   ON AFib.person_id = observation_period.person_id
# MAGIC   AND AFib.condition_start_date >= date_add(observation_period.observation_period_start_date,1095)
# MAGIC   AND AFib.condition_start_date <= observation_period.observation_period_end_date
# MAGIC   LEFT JOIN
# MAGIC   (
# MAGIC   SELECT person_id, min(drug_exposure_start_date) as drug_exposure_start_date
# MAGIC   FROM drug_exposure
# MAGIC   WHERE drug_concept_id IN (SELECT descendant_concept_id FROM 
# MAGIC   concept_ancestor WHERE ancestor_concept_id IN 
# MAGIC   (1310149 /*warfarin*/))
# MAGIC   GROUP BY person_id
# MAGIC   ) warfarin
# MAGIC   ON Afib.person_id = warfarin.person_id
# MAGIC   AND Afib.condition_start_date > warfarin.drug_exposure_start_date
# MAGIC   WHERE warfarin.person_id IS NULL
# MAGIC   ;

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