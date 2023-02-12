# Databricks notebook source
# MAGIC %md
# MAGIC # Congestive Heart Failure cohort study
# MAGIC <img src="https://upload.wikimedia.org/wikipedia/commons/f/fb/Blausen_0463_HeartAttack.png" width=300>
# MAGIC 
# MAGIC In this example we create at table to hold the target and outcome cohort data for our study on Congestive Heart Failure. In this hypothetical study, we would like to calcuate the rates of ER admissions between different age groups and genders, for a cohort who has been diagnosed with chronic congestive heart failure. This example is based on an example study from [The Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/SqlAndR.html#designing-a-simple-study).
# MAGIC 
# MAGIC >Heart failure, sometimes known as congestive heart failure, occurs when your heart muscle doesn't pump blood as well as it should. Certain conditions, such as narrowed arteries in your heart (coronary artery disease) or high blood pressure, gradually leave your heart too weak or stiff to fill and pump efficiently.
# MAGIC >
# MAGIC >Not all conditions that lead to heart failure can be reversed, but treatments can improve the signs and symptoms of heart failure and help you live longer. Lifestyle changes — such as exercising, reducing sodium in your diet, managing stress and losing weight — can improve your quality of life.
# MAGIC >
# MAGIC >One way to prevent heart failure is to prevent and control conditions that cause heart failure, such as coronary artery disease, high blood pressure, diabetes or obesity.
# MAGIC >
# MAGIC [www.mayoclinic.org](https://www.mayoclinic.org/diseases-conditions/heart-failure/symptoms-causes/syc-20373142#:~:text=Heart%20failure%2C%20sometimes%20known%20as,to%20fill%20and%20pump%20efficiently.)
# MAGIC 
# MAGIC The main purpose of this excercise is to show users how they can build cohorts based on OMOP using standard SQL directly on delta tables
# MAGIC and to perform analytics directly on OMOP tables using their language of choice. 

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Explore disease model module
# MAGIC In this example, we use simulated data generated based on Synthea's [congestive heart failure module](https://github.com/synthetichealth/synthea/blob/master/src/main/resources/modules/congestive_heart_failure.json) to smiluate patients to be inlcuded in our dataset.  The example case study is to look at the rate of first let's take a look at the "ground truth" disease model.

# COMMAND ----------

# MAGIC %pip install pyvis

# COMMAND ----------

import urllib.request, json 
import pandas as pd
module_url="https://raw.githubusercontent.com/synthetichealth/synthea/master/src/main/resources/modules/congestive_heart_failure.json"
with urllib.request.urlopen(module_url) as url:
    data = json.loads(url.read().decode())

# COMMAND ----------

import pprint
pprint.pprint(data['states'])

# COMMAND ----------

# MAGIC %md
# MAGIC In a synthea diease modulde, `states` are at the core of the module which can be of the control cathegory for the simulation, for example delay disease onset, or clinical for example first symptom, or encounters.  State transitions can be, direct, distributed, conditional or complex transitions. For more details on the structure of a module see: [Generic-Module-Framework](https://github.com/synthetichealth/synthea/wiki/Generic-Module-Framework)
# MAGIC transitions are cathegorised into four cathegory of `direct_transitions`,``
# MAGIC Let's construct a graph of all direct and distributed transitions:

# COMMAND ----------

l1=[[[m[0],k['transition'],k['distribution']] for k in m[1]['distributed_transition']] for m in data['states'].items() if m[1].get('distributed_transition')]
distributed_transitions=[item for sublist in l1 for item in sublist]
direct_transitions=[[m[0],m[1]['direct_transition'],1] for m in data['states'].items() if m[1].get('direct_transition')]
CHF_model_transition_graph=pd.DataFrame(distributed_transitions+direct_transitions,columns=['Source','Target','Weight']).dropna()

# COMMAND ----------

from pyvis.network import Network
import pandas as pd

got_net = Network(height='750px', width='80%', bgcolor='#222222', font_color='white', directed=True)

# set the physics layout of the network
got_net.barnes_hut()
got_data = CHF_model_transition_graph

sources = got_data['Source']
targets = got_data['Target']
weights = got_data['Weight']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w)

neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
for node in got_net.nodes:
    node['title'] += ' Neighbors:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])
    
got_net.write_html('CHF.html')
CHF_html= open("CHF.html", "r").read()
displayHTML(CHF_html)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Simple cohort design
# MAGIC Now let's design a simple cohort study. In our example, we are going to create a target cohort of individuals  
# MAGIC who have at least 3 years of histroical records and we then calculate the rate of ER admitions within the cohort.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2.1 Target Cohort
# MAGIC T : patients who are newly 
# MAGIC - diagnosed with chronic congestive heart failure (CCHF)
# MAGIC - persons with a condition occurrence record of CCHF or any descendants, indexed at the first diagnosis
# MAGIC - who have >1095 days of prior observation before their first diagnosis
# MAGIC - and have no Furosemide exposure any time prior to first CCHF diagnosis

# COMMAND ----------

# MAGIC %sql
# MAGIC USE OMOP531

# COMMAND ----------

target_condition_concept_id=4229440  #Chronic congestive heart failure (disorder)
target_drug_concept_id=1719286       #10 ML Furosemide 10 MG/ML Injection

target_cohort_query=f"""
with targetConditionSet AS
(
  SELECT person_id, min(condition_start_date) as condition_start_date
  FROM condition_occurrence
  WHERE condition_concept_id IN
    ( SELECT descendant_concept_id FROM concept_ancestor WHERE ancestor_concept_id IN ({target_condition_concept_id}) )
  GROUP BY person_id
),
targetDrugExposure as (
SELECT person_id, min(drug_exposure_start_date) as drug_exposure_start_date
  FROM drug_exposure
  WHERE drug_concept_id IN (SELECT descendant_concept_id FROM concept_ancestor WHERE ancestor_concept_id IN ({target_drug_concept_id}))
  GROUP BY person_id
)

SELECT 1 AS cohort_definition_id,
targetConditionSet.person_id AS subject_id,
targetConditionSet.condition_start_date AS cohort_start_date,
observation_period.observation_period_end_date AS cohort_end_date
from targetConditionSet
INNER JOIN observation_period
  ON targetConditionSet.person_id = observation_period.person_id
  AND targetConditionSet.condition_start_date >= date_add(observation_period.observation_period_start_date,1095)
  AND targetConditionSet.condition_start_date <= observation_period.observation_period_end_date
  LEFT JOIN targetDrugExposure
  ON targetConditionSet.person_id = targetDrugExposure.person_id
  AND targetConditionSet.condition_start_date > targetDrugExposure.drug_exposure_start_date
WHERE targetDrugExposure.person_id IS NULL
  ;
"""
target_cohort_df=sql(target_cohort_query)
target_cohort_df.createOrReplaceTempView('targetCohort')
display(target_cohort_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2.2 Outcome cohort
# MAGIC In this case, we are simply intersted in all ER visits and would like to caluclate the incident rate of such visits among the target cohort.

# COMMAND ----------

# MAGIC %py
# MAGIC outcome_concept_id=9203  #Emergency Room Visit
# MAGIC outcome_cohort_query=f"""  
# MAGIC   SELECT 2 AS cohort_definition_id,
# MAGIC   visit_occurrence.person_id AS subject_id,
# MAGIC   visit_occurrence.visit_start_date AS cohort_start_date,
# MAGIC   visit_occurrence.visit_end_date AS cohort_end_date
# MAGIC   FROM  visit_occurrence
# MAGIC   WHERE visit_occurrence.visit_concept_id IN ({outcome_concept_id})
# MAGIC   GROUP BY visit_occurrence.person_id, visit_occurrence.visit_start_date, 
# MAGIC   visit_occurrence.visit_end_date"""
# MAGIC outcome_cohort_df=sql(outcome_cohort_query)
# MAGIC outcome_cohort_df.createOrReplaceTempView('outcomeCohort')
# MAGIC display(outcome_cohort_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ###  2.3. Incidence Rate Calculation
# MAGIC Now that our cohorts are in place, we can compute the incidence rate, stratified by age and gender:

# COMMAND ----------

target_cohort_df.union(outcome_cohort_df).createOrReplaceTempView('CHF_cohort')

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMPORARY VIEW INCIDENT_RATE AS (
# MAGIC WITH tar AS (
# MAGIC   SELECT concept_name AS gender,
# MAGIC     FLOOR((YEAR(cohort_start_date) - year_of_birth) / 10)*10 AS age,
# MAGIC     subject_id,
# MAGIC     cohort_start_date,
# MAGIC     CASE WHEN DATE_ADD(cohort_start_date,7) > observation_period_end_date
# MAGIC     THEN observation_period_end_date
# MAGIC     ELSE DATE_ADD(cohort_start_date,7)
# MAGIC     END AS cohort_end_date
# MAGIC   FROM CHF_cohort
# MAGIC   INNER JOIN observation_period
# MAGIC     ON subject_id = observation_period.person_id
# MAGIC       AND observation_period_start_date < cohort_start_date
# MAGIC       AND observation_period_end_date > cohort_start_date
# MAGIC   INNER JOIN person
# MAGIC     ON subject_id = person.person_id
# MAGIC   INNER JOIN concept
# MAGIC     ON gender_concept_id = concept_id
# MAGIC   WHERE cohort_definition_id = 1 -- Target
# MAGIC )
# MAGIC SELECT days.gender,
# MAGIC     days.age,
# MAGIC     days,
# MAGIC     CASE WHEN events IS NULL THEN 0 ELSE events END AS events
# MAGIC FROM (
# MAGIC   SELECT gender,
# MAGIC     age,
# MAGIC     SUM(DATEDIFF(cohort_end_date,cohort_start_date)) AS days
# MAGIC   FROM tar
# MAGIC   GROUP BY gender,
# MAGIC     age
# MAGIC ) days
# MAGIC LEFT JOIN (
# MAGIC   SELECT gender,
# MAGIC       age,
# MAGIC       COUNT(*) AS events
# MAGIC   FROM tar
# MAGIC   INNER JOIN CHF_cohort chf
# MAGIC     ON tar.subject_id = chf.subject_id
# MAGIC       AND tar.cohort_start_date <= chf.cohort_start_date
# MAGIC       AND tar.cohort_end_date >= chf.cohort_start_date
# MAGIC   WHERE cohort_definition_id = 2 -- Outcome
# MAGIC   GROUP BY gender,
# MAGIC     age
# MAGIC ) events
# MAGIC ON days.gender = events.gender
# MAGIC   AND days.age = events.age
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC select *, 1000*events/days/7 as ir
# MAGIC from INCIDENT_RATE

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Write Cohorts to Results Schema

# COMMAND ----------

# MAGIC %sql
# MAGIC USE OMOP531Results;
# MAGIC CREATE
# MAGIC OR REPLACE TABLE CHFCohort (
# MAGIC   cohort_definition_id LONG,
# MAGIC   subject_id LONG,
# MAGIC   cohort_start_date DATE,
# MAGIC   cohort_end_date DATE
# MAGIC ) USING DELTA;
# MAGIC 
# MAGIC INSERT OVERWRITE CHFCohort
# MAGIC   Select cohort_definition_id, 
# MAGIC          subject_id, 
# MAGIC          cohort_start_date, 
# MAGIC          cohort_end_date
# MAGIC          from targetCohort

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO CHFCohort
# MAGIC   Select cohort_definition_id, 
# MAGIC          subject_id, 
# MAGIC          cohort_start_date, 
# MAGIC          cohort_end_date
# MAGIC          from targetCohort

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from CHFCohort

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