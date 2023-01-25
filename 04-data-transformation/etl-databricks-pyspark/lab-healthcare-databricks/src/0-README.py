# Databricks notebook source
# MAGIC %md
# MAGIC # Health LakeHouse on Databricks: Real World Data

# COMMAND ----------

slides_html="""
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vTW-9ujZFs-FEhZbc1_abK9cK-sEwKCmZvDjmz2mhEjHeMf91LEK9i9V9LF1jMS-dsakCfXswGiIvvt/embed?start=true&loop=true&delayms=3000" frameborder="0" width="640" height="375" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
"""
displayHTML(slides_html)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Solution Overview
# MAGIC The healthcare industry is one of the biggest producers of data. In fact, the average healthcare organization is sitting on nearly 9 petabytes of medical data. <br>
# MAGIC The rise of electronic health records (EHR), digital medical imagery, and wearables are contributing to this data explosion. For example, an EHR system at a large <br>
# MAGIC provider can catalogue millions of medical tests, clinical interactions, and prescribed treatments. Such data assets, collectively referred to as the Real World Data <br>
# MAGIC or RWD, are at the center of observational studies. They are used to inform new treatments, monitor adverse drug effects or perform synthetic trials. <br>
# MAGIC However, observational databases are designed to primarily empower longitudinal studies and differ in both purpose and design from Electronic Medical Records <br>
# MAGIC (aimed at supporting clinical practice at the point of care), or claims data that are built for the insurance reimbursement processes. The Common Data Model is designed to address this problem:
# MAGIC 
# MAGIC >The Common Data Model (CDM) can accommodate both administrative claims and EHR, allowing users to generate evidence from a wide variety of sources.<br>
# MAGIC It would also support collaborative research across data sources both within and outside the United States, in addition to being manageable for data<br>
# MAGIC owners and useful for data users. 
# MAGIC 
# MAGIC One of the most widely used CDMs for observational research is The OMOP Common Data Model.
# MAGIC 
# MAGIC > The OMOP Common Data Model allows for the systematic analysis of disparate observational databases. The concept behind this approach is to transform data<br>
# MAGIC contained within those databases into a common format (data model) as well as a common representation (terminologies, vocabularies, coding schemes), and then <br>
# MAGIC perform systematic analyses using a library of standard analytic routines that have been written based on the common format. 
# MAGIC 
# MAGIC OMOP CDM is now been adopted by more than 30 countires with more than 600M unique patient records.
# MAGIC 
# MAGIC For more information and training on OMOP CDM, we recommned watching:
# MAGIC [2017 Tutorials – OMOP Common Data Model and Standardized Vocabularies](https://www.ohdsi.org/past-events/2017-tutorials-omop-common-data-model-and-standardized-vocabularies/)
# MAGIC 
# MAGIC [<img src="https://drive.google.com/uc?export=view&id=1E73uO2_x9fj-7-3-yUokiOAqSxTuiQP1" width=500>](https://www.youtube.com/embed/BExsHYxkvTw)
# MAGIC 
# MAGIC ### _Why lakehouse_?
# MAGIC The complexity of such healthcare data, data variety, volume and varried data quality, pose computational and organizational challenges. For example, performing cohort <br>
# MAGIC studies on longitudinal data requires complex ETL of the raw data to transofrm the data into a data model that is optimized for such studies and then to perform statistical<br>
# MAGIC analysis on the resulting cohorts. Each step of this process currently requires using different technolgies for ETL, storage, governance and analysis of the data.<br>
# MAGIC Each additional technology adds a new layer of complexity to the process, which reduces efficieny and inhibits colaboration.
# MAGIC 
# MAGIC The lakehouse paradigm, addresses such complexities: It is an architecture that by design brings the best of the two worlds of data warehousing and data lakes together:<br>
# MAGIC Data lakes meet the top requirement for healthcare and life sciences organizations to store and manage different data modalities and allow advanced analytics methods to be performed<br>
# MAGIC directly on the data where it sits in the cloud. However, datalakes lack the ability for regulatory-grade audits and data versioning. In contrast, data warehouses, <br>
# MAGIC which allow for quick access to data and support simple prescriptive analytics (such as simple aggregate statistics on the data), do not support unstructured data nor performing <br>
# MAGIC advanced analytics and ML. The lakehouse architecture allows organizations to perform descriptive and predictive analytics on the vast amounts of healthcare data directly on cloud <br>
# MAGIC storage where data sits while ensuring regulatory-grade compliance and security.
# MAGIC 
# MAGIC #### _What is included_?
# MAGIC In this solution accelerator, we provide an example of an end-to-end workflow for building a complete solution for observational studies on top of delta lake. <br>
# MAGIC This solution covers the following workloads:
# MAGIC 
# MAGIC   0. Configure your environment (`rwe-lakehouse/00-config/1-config`) 
# MAGIC   1. Simulating synthetic EHR records using synthea:(optional)
# MAGIC   
# MAGIC      1.1. in a distributed fashion (`rwe-lakehouse/000-data-gen/2-run-synthea`)
# MAGIC      
# MAGIC      1.2. or single-node simulation with a given disease module (`rwe-lakehouse/000-data-gen/3-run-synthea-singlenode`)
# MAGIC       
# MAGIC   2. Ingesting raw EHR data in CSV format (`rwe-lakehouse/001-ingest/3-synthea-ingest`)
# MAGIC   3. Definitions of OMOP 5.3.1 (`rwe-lakehouse/002-omop-cdm/4-a_omop531_cdm_setup`) and 6.0.0 (`rwe-lakehouse/002-omop-cdm/4-a_omop600_cdm_setup`)common data model for delta.
# MAGIC   4. OMOP Vocabulary tables (`rwe-lakehouse/002-omop-cdm/5-omop_vocab_setup`)
# MAGIC   5. Creating delta silver tables and database for OMOP 5.3.1
# MAGIC   6. Example ETL for transforming synthea resources into OMOP 5.3.1 (`rwe-lakehouse/003-etl/6-a_omop531_etl_synthea`)
# MAGIC   7. Example notebooks for analysis of records (`rwe-lakehouse/004-analysis/0-example-drug-analysis`) and OMOP sample queires (`rwe-lakehouse/004-analysis/1-sample-omop_queries`)
# MAGIC   8. Example notebooks for cohort creation and workflows for reproducible cohort analysis (`rwe-lakehouse/004-analysis/2-example-CHF-cohort`)
# MAGIC   
# MAGIC # 🤖 
# MAGIC In addition, you can run the end-to-end workflow with `0-RUNME` notebook and when your OMOP Lakehouse is ready you can start exploring the dataset using the provided starter notebooks <br>for exploratory analysis of the data.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Package Overview

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Data Ingest (bronze) 
# MAGIC To simulate health records, we used [Synthea](https://github.com/synthetichealth/synthea) to generate synthetic patients, from accross the US. You can also access sample raw `csv` files in `/databricks-datasets/ehr/rwe/csv` for 10K patinets.
# MAGIC 
# MAGIC Note: If you set the parameter for downloading pre-simulated raw samples (recommended) in `rwe-lakehouse/00-config/1-config` notebook, a sample of `90K` patients from accross the US will be downloaded to your environment which subsequently is used throughout this solution accelerator. The dataset also includes simulated data based on [Chronic Heart Failour](https://github.com/synthetichealth/synthea/blob/master/src/main/resources/modules/congestive_heart_failure.json) and [Covid-19](https://github.com/synthetichealth/synthea/blob/master/src/main/resources/modules/covid19/diagnose_blood_clot.json) disease modules from Synthea.
# MAGIC To run this step run `rwe-lakehouse/001-ingest/3-synthea-ingest` notebook.
# MAGIC 
# MAGIC <img align="right" width="400"  src="https://drive.google.com/uc?export=view&id=1vwoJVa87j0lN9CfUFpJJrY7LdSRmUg2u">

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. ETL to OMOP (silver) 
# MAGIC In the next step we construct our OMOP tables and transform synthea resources into the OMOP Common Data Model. This step also inlcludes constructing OMOP Vocabulary tables and creating an OMOP Delta Lake.

# COMMAND ----------

# MAGIC %md
# MAGIC #### 2.1. Setup CDM 
# MAGIC To construct OMOP tables, run `rwe-lakehouse/002-omop-cdm/4-a_omop531_cdm_setup` notebook, which creates `OMOP 5.3.1` tables.
# MAGIC 
# MAGIC <img align="right" width="400"  src="https://drive.google.com/uc?export=view&id=106WsAz6lvRKEld1DTLSR8V81L0zkXLEf">

# COMMAND ----------

# MAGIC %md
# MAGIC #### 2.2 Construct Vocabulary Tables 
# MAGIC Next we use `rwe-lakehouse/002-omop-cdm/5-omop_vocab_setup` to construct [OMOP vocabulary tables](https://ohdsi.github.io/TheBookOfOhdsi/StandardizedVocabularies.html#StandardizedVocabularies)
# MAGIC 
# MAGIC <img align="right" width="400"  src="https://drive.google.com/uc?export=view&id=13miRuD5HeR0TpLkyivI9v6ty2elUZ2Rs">

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Upload vocabularies to `dbfs`
# MAGIC In the environment cofiguartion notebook we also automatically download vocabulary resources into your cloud environment. However, to access more updated resources or customized
# MAGIC resources, you can download vocab files from [Athena](https://athena.ohdsi.org/search-terms/start) website, and use `databricks cli` utilities to upload downloaded vocabularies to `dbfs` under your `vocab_path`.
# MAGIC 
# MAGIC <img align="right" width="400"  src="https://drive.google.com/uc?export=view&id=16TU2l7XHjQLugmS_McXegBXKMglD--Fr">

# COMMAND ----------

# MAGIC %md
# MAGIC #### 2.3. ETL for Synthea Dataset to OMOP CDM
# MAGIC Now we are ready to transform Synthea reources into OMOP. To do so, use `rwe-lakehouse/003-etl/6-a_omop531_etl_synthea` to tranform data to OMOP531 model.<br>
# MAGIC The ETL code is based on this repository: https://github.com/OHDSI/ETL-Synthea
# MAGIC 
# MAGIC <img align="right" width="400"  src="https://drive.google.com/uc?export=view&id=106WsAz6lvRKEld1DTLSR8V81L0zkXLEf">

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Analysis
# MAGIC Finally, when you create any cohorts and write your cohorts into `resultsSchema` which is an example of your Gold delat tables, see `rwe-lakehouse/004-analysis/2-example-CHF-cohort` for an example of cohort creation.<br>
# MAGIC It is also important to note that now that you have created your OMOP tables on Delta, you can your analytics language of choice (`SQL`, `Python` or `R`) to analyze your data. See `rwe-lakehouse/004-analysis/0-example-drug-analysis` for an example in python and `rwe-lakehouse/004-analysis/1-sample-omop_queries` for examples of OMOP queries from https://github.com/OHDSI/OMOP-Queries

# COMMAND ----------

# MAGIC %md
# MAGIC ### NOTE: 🤖 
# MAGIC To accelerate your work, you can simply run `./00-RUNME` notebook setup your environment and automatically create your the OMOP Delta Lake and jump to analysis.
# MAGIC Assuming you have done so, run the below example queries to make sure your data is ready.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Quey Example 1
# MAGIC 
# MAGIC patients with Non-small cell lung cancer. 

# COMMAND ----------

# MAGIC %sql
# MAGIC USE OMOP531

# COMMAND ----------

# DBTITLE 1,Patients with Non-small cell lung cancer by age and gender
# MAGIC %sql
# MAGIC SELECT gender, age, count(*) num_patients 
# MAGIC   FROM -- patient with Non-small cell lung cancer, age, gender 
# MAGIC     ( 
# MAGIC       SELECT DISTINCT condition.person_id , gender.concept_name As GENDER , EXTRACT( YEAR 
# MAGIC       FROM CONDITION_ERA_START_DATE ) - year_of_birth AS age 
# MAGIC       FROM condition_era condition 
# MAGIC       JOIN -- definition of Hip Fracture 
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
# MAGIC ## Quey Example 2
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
# MAGIC ## LICENSE

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

# COMMAND ----------

# MAGIC %md
# MAGIC ### Contributors:  
# MAGIC * [Philip Austin](https://www.linkedin.com/in/artofpossible/), Sr. Solutions Architect
# MAGIC * [Mark Lee](https://www.linkedin.com/in/leeconsultations/), Solutions Architect
# MAGIC * [Amir Kermany](https://www.linkedin.com/in/akermany/), Technical Director, Healthcare and Life Sciences