-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Drug Usage Trends
-- MAGIC <img src="https://upload.wikimedia.org/wikipedia/commons/7/76/Medicine_Drugs.svg" width=300>
-- MAGIC 
-- MAGIC In this notebook we provide examples for exploring trends in drug usage within our data. For example, how different segments of the population use a particular drug,
-- MAGIC or what are the drugs that are most commonly prescribed together. We also take a deeper look into drug combinations: For example, pairwise correlation between prescription drugs and most frequent drug prescription patterns.

-- COMMAND ----------

USE omop531;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Example 1. Drug usage by different population segments
-- MAGIC In the following example we are looking at trends in usage of a given drug over time. Specifically how different population segments 
-- MAGIC are using a given drug. In this example we stratify results by age and gender.

-- COMMAND ----------

-- DBTITLE 1,Usage of Oxycodone stratified by gender
SELECT
  tt.drug_concept_name,
  tt.drug_concept_id,
  count(1) as s_count,
  tt.age_band,
  tt.year_of_Era,
  tt.gender
from
  (
    SELECT
      floor(
        (
          extract(
            year
            from
              t.drug_era_start_date
          ) - p.year_of_birth
        ) / 10
      ) as age_band,
      extract(
        year
        from
          t.drug_era_start_date
      ) as year_of_era,
      p.gender_concept_id,
      t.drug_concept_id,
      c.concept_name as drug_concept_name,
      c1.concept_name as gender
    FROM
      drug_era t,
      person p,
      concept c,
      concept c1
    where
      t.person_id = p.person_id
      and c.concept_id = t.drug_concept_id
      and c1.concept_id = p.gender_concept_id
      and c.concept_id =  1124957 -- Oxycodone
  ) tt
  where tt.year_of_era > 2000
group by
  tt.age_band,
  tt.year_of_Era,
  tt.gender,
  tt.drug_concept_name,
  tt.drug_concept_id
order by
  tt.age_band,
  tt.year_of_Era,
  tt.drug_concept_id;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Example 2. top drugs prescribed in the past 5 years
-- MAGIC Now let's take a look at the top drugs prescribed in the past five years.

-- COMMAND ----------

with tt as 
(
    SELECT
        extract(year from t.drug_era_start_date) as year_of_era,
        t.drug_concept_id,
        c.concept_name as drug_concept_name
    FROM
      drug_era t,
      concept c
    where
      t.drug_concept_id = c.concept_id
)
SELECT
  tt.drug_concept_name,
  tt.drug_concept_id,
  tt.year_of_Era,
  count(1) as drug_count
from
   tt
  where year(current_date) - tt.year_of_Era <= 5
group by
  tt.drug_concept_name,
  tt.drug_concept_name,
  tt.year_of_Era,
  tt.drug_concept_id
order by
  tt.year_of_Era, count(1) DESC
  

-- COMMAND ----------

-- MAGIC %md
-- MAGIC for example we notice a consistent trend in reduction of the number of instances where Oxycodone is being prescribed. 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Example 3. Comparing age distribution between two groups
-- MAGIC Now let's take a look at the distribution of ages between two drugs of interest, in this case Hydrocodone and Oxycodone.

-- COMMAND ----------

-- MAGIC %python
-- MAGIC d1_concept_id=1124957
-- MAGIC d2_concept_id=1174888
-- MAGIC import plotly.express as px
-- MAGIC query=f"""
-- MAGIC SELECT
-- MAGIC      extract(year from (min(t.drug_era_start_date) over(partition by t.person_id, t.drug_concept_id) )) - p.year_of_birth as age,
-- MAGIC      c.concept_name d_concept_name
-- MAGIC      FROM drug_era t, person p, concept c
-- MAGIC      WHERE t.person_id = p.person_id
-- MAGIC        AND t.drug_concept_id = c.concept_id
-- MAGIC        AND t.drug_concept_id in ({d1_concept_id},{d2_concept_id})
-- MAGIC """
-- MAGIC 
-- MAGIC df = sql(query).groupBy('age','d_concept_name').count().toPandas()
-- MAGIC fig = px.histogram(df, x="age", y="count", color="d_concept_name",
-- MAGIC                    marginal="box", # or violin, rug
-- MAGIC                    hover_data=df.columns)
-- MAGIC fig.update_layout(
-- MAGIC     autosize=False,
-- MAGIC     width=700,
-- MAGIC     height=700,
-- MAGIC     margin=dict(
-- MAGIC         l=50,
-- MAGIC         r=50,
-- MAGIC         b=100,
-- MAGIC         t=100,
-- MAGIC         pad=4
-- MAGIC     ),
-- MAGIC     paper_bgcolor="LightSteelBlue",
-- MAGIC )
-- MAGIC fig.show()

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Example 4. Finding drugs that are commonly prescribed together
-- MAGIC In this example, let's take a look at the association between drugs. For example, in an study of prescription drugs, we might be interested in learning which drugs are more likely prescribed together compared to what would be expected at random. For this analysis, we use two apporaches: first we apply a simple probabilistic approach, which uses the [cosine measure](https://michael.hahsler.net/research/association_rules/measures.html#support) to quantify the degree of association between a pair of events (in this case, `drug1` and `drug2` being used during the same drug era). Next, we use the FP-Growth alogorithm from [spark mlLib](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html#frequent-pattern-mining) to identify frequent patterns for prescription drugs. This is a similar approach to market basket analysis (or affinity analytics).

-- COMMAND ----------

-- MAGIC %md
-- MAGIC 
-- MAGIC ### 4.1 Pairwise association
-- MAGIC First we need to define a criteria for considering two drugs being prescribed together. 
-- MAGIC For simplicity, let's first define a time interval \\(\Delta\\) and consider two drugs being prescribed together if:
-- MAGIC $$ |t_1-t_2| < \Delta$$ and $$|s_1-s_2|<\Delta$$
-- MAGIC in which \\(t_i,s_i\\) are the start and end times for taking drug \\(i\\) by a patient respectively. Using this criteria, we can then compile a list of drug pairs that have been associated with eachother based on being prescribed within the same time period.
-- MAGIC First let's create a dataset of drug pairs, paired according to the above criteria, and relevant summary statistics such as [support](https://michael.hahsler.net/research/association_rules/measures.html#support) that we then will use to calculate the cosine metrics for association. 

-- COMMAND ----------

CREATE OR REPLACE TEMPORARY VIEW COPRESCRIBED AS (
  with drugs_and_names as (
    select PERSON_ID,c.concept_name as drug_concept_name, DRUG_CONCEPT_ID,DRUG_ERA_START_DATE,DRUG_ERA_END_DATE
    from drug_era
    join concept c
    where DRUG_CONCEPT_ID=c.concept_id
  ),
  drugs as (
  select d1.PERSON_ID,
         d1.DRUG_CONCEPT_ID as drug_id1,
         d2.DRUG_CONCEPT_ID as drug_id2,
         d1.drug_concept_name as drug1,
         d2.drug_concept_name as drug2,
         d1.DRUG_ERA_START_DATE as d1_start,
         d1.DRUG_ERA_END_DATE as d1_end,
         d2.DRUG_ERA_START_DATE as d2_start,
         d2.DRUG_ERA_END_DATE as d2_end
  from drugs_and_names d1
  join drugs_and_names d2
  where 
    d1.PERSON_ID=d2.PERSON_ID
    AND
    ABS(datediff(d1.DRUG_ERA_START_DATE,d2.DRUG_ERA_START_DATE)) <=5  -- drugs that have been taken during the same time period +/-5 days 
    AND 
    ABS(datediff(d1.DRUG_ERA_END_DATE, d2.DRUG_ERA_END_DATE)) <=5
  ),
  counts as (
    select drug1,drug2, count(*) as count_d1d2
    from drugs
    group by 1,2
    order by 3 desc
  ),
  pairwise_sums as (
    select drug1, drug2, count_d1d2,
    sum(count_d1d2) over (partition by drug1) as sum_d1,
    sum(count_d1d2) over (partition by drug2) as sum_d2,
    sum(count_d1d2) over () as sum_all
    from counts
  )
  select drug1,drug2, count_d1d2,
    count_d1d2/sum_d1 as supp_d1d2,
    count_d1d2/sum_d2 as supp_d2d1,
    sum_d1/sum_all as supp_d1,
    sum_d2/sum_all as supp_d2
  from pairwise_sums
)
-- limit 100

-- COMMAND ----------

-- MAGIC %md
-- MAGIC let's take a look at this dataset:

-- COMMAND ----------

select * from COPRESCRIBED

-- COMMAND ----------

-- MAGIC %python
-- MAGIC import pandas as pd
-- MAGIC import plotly.express as px
-- MAGIC 
-- MAGIC df = sql("""
-- MAGIC             select drug1,drug2, supp_d1d2,  log(supp_d1d2/sqrt(supp_d1*supp_d2)) as lod_cosine_d1d2, log(supp_d1d2)-log(supp_d1) as lod_d1d2
-- MAGIC             from COPRESCRIBED order by lod_cosine_d1d2 desc
-- MAGIC           """)
-- MAGIC 
-- MAGIC pdf=df.toPandas()
-- MAGIC pdf_matx=pd.crosstab(pdf.drug1,pdf.drug2,values=pdf.lod_cosine_d1d2,aggfunc='sum')
-- MAGIC fig = px.imshow(pdf_matx)
-- MAGIC fig.update_layout(
-- MAGIC     autosize=False,
-- MAGIC     width=700,
-- MAGIC     height=700,
-- MAGIC     margin=dict(
-- MAGIC         l=50,
-- MAGIC         r=50,
-- MAGIC         b=100,
-- MAGIC         t=100,
-- MAGIC         pad=4
-- MAGIC     ),
-- MAGIC     paper_bgcolor="LightSteelBlue",
-- MAGIC )
-- MAGIC 
-- MAGIC fig.show()

-- COMMAND ----------

with drugs_and_names as (
select PERSON_ID,c.concept_name as drug_concept_name, DRUG_CONCEPT_ID,DRUG_ERA_START_DATE,DRUG_ERA_END_DATE
from drug_era
join concept c
where DRUG_CONCEPT_ID=c.concept_id
),
drugs as (
select de1.PERSON_ID,
       de1.DRUG_CONCEPT_ID as drug_id1,
       de2.DRUG_CONCEPT_ID as drug_id2,
       de1.drug_concept_name as drug1,
       de2.drug_concept_name as drug2,
       de1.DRUG_ERA_START_DATE as d1_start,
       de1.DRUG_ERA_END_DATE as d1_end,
       de2.DRUG_ERA_START_DATE as d2_start,
       de2.DRUG_ERA_END_DATE as d2_end
from drugs_and_names de1
join drugs_and_names de2
where 
  de1.PERSON_ID=de2.PERSON_ID
  AND
  ABS(datediff(de1.DRUG_ERA_START_DATE,de2.DRUG_ERA_START_DATE)) <=5  -- drugs that have been taken during the same time period +/-5 days 
  AND 
  ABS(datediff(de1.DRUG_ERA_END_DATE, de2.DRUG_ERA_END_DATE)) <=5
),
counts as (
select drug1,drug2, count(*) as count
from drugs
group by 1,2
order by 3 desc
)
select *, unix_timestamp('DRUG_ERA_START_DATE') from drugs_and_names

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### 4.2 Frequent Pattern Mining
-- MAGIC Now let's take a deeper look into frequent patterns. We use the FP-Growth alogorithm from [spark mlLib](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html#frequent-pattern-mining) to identify frequent patterns for prescription drugs. This is a similar approach to market basket analysis (or affinity analytics), in which items linked to a given transaction are analyzed to identify affinity patterns. In our case, a transaction corresponds to a given drug era record and we consider two items (drugs in this case) to have co-occured together based on our definition provided in the first part of this example. 
-- MAGIC In the following cell, we switch to python to create a dataset which each row of the dataset corresponds to drugs that have co-occured within the same time interval 
-- MAGIC \\( t+\Delta; \Delta=\pm 5 \\) days.

-- COMMAND ----------

-- MAGIC %py
-- MAGIC from pyspark.sql.functions import *
-- MAGIC drugs_and_names=sql("""
-- MAGIC 
-- MAGIC select PERSON_ID,c.concept_name as drug_concept_name, DRUG_CONCEPT_ID,DRUG_ERA_START_DATE,DRUG_ERA_END_DATE
-- MAGIC from drug_era
-- MAGIC join concept c
-- MAGIC where DRUG_CONCEPT_ID=c.concept_id
-- MAGIC """)
-- MAGIC 
-- MAGIC def get_date_key(d,delta_days=5):
-- MAGIC   days_to_sec=delta_days*24*60*60
-- MAGIC   t1=days_to_sec*((d+days_to_sec)//days_to_sec)
-- MAGIC   t2=days_to_sec*((d-days_to_sec)//days_to_sec)
-- MAGIC   return(f"{t1}:{t2}")
-- MAGIC 
-- MAGIC get_key_udf = udf(lambda d:get_date_key(d))
-- MAGIC 
-- MAGIC df=drugs_and_names\
-- MAGIC .withColumn('start_key',get_key_udf(unix_timestamp('DRUG_ERA_START_DATE')))\
-- MAGIC .withColumn('end_key',get_key_udf(unix_timestamp('DRUG_ERA_END_DATE')))\
-- MAGIC .orderBy('DRUG_ERA_START_DATE')\
-- MAGIC .groupBy(['PERSON_ID','start_key','end_key'])\
-- MAGIC .agg(collect_set('drug_concept_name').alias('drug_items'))\
-- MAGIC .select(udf(lambda x: ",".join(x))(col('drug_items')).alias('drug_items'))

-- COMMAND ----------

-- MAGIC %md
-- MAGIC now we use FPGrowth algorithm from `spark.mllib` to find the most frequent patterns. Note that we are using `rdd` api to feed data to the algroithm. In addition to the dataset
-- MAGIC we also need to specify a minimum threshold for a particular pattern to be considered significant. 

-- COMMAND ----------

-- MAGIC %py
-- MAGIC from pyspark.mllib.fpm import FPGrowth
-- MAGIC 
-- MAGIC transactions = df.rdd.map(lambda row: row['drug_items'].strip().split(','))
-- MAGIC model = FPGrowth.train(transactions, minSupport=0.02, numPartitions=10)
-- MAGIC result = model.freqItemsets().collect()

-- COMMAND ----------

-- MAGIC %py
-- MAGIC display(spark.createDataFrame(result).orderBy(col('freq').desc()))

-- COMMAND ----------

-- MAGIC %md
-- MAGIC Copyright / License info of the notebook. Copyright Databricks, Inc. [2021].  The source in this notebook is provided subject to the [Databricks License](https://databricks.com/db-license-source).  All included or referenced third party libraries are subject to the licenses set forth below.
-- MAGIC 
-- MAGIC |Library Name|Library License|Library License URL|Library Source URL| 
-- MAGIC | :-: | :-:| :-: | :-:|
-- MAGIC |Smolder |Apache-2.0 License| https://github.com/databrickslabs/smolder | https://github.com/databrickslabs/smolder/blob/master/LICENSE|
-- MAGIC |Synthea|Apache License 2.0|https://github.com/synthetichealth/synthea/blob/master/LICENSE| https://github.com/synthetichealth/synthea|
-- MAGIC | OHDSI/CommonDataModel| Apache License 2.0 | https://github.com/OHDSI/CommonDataModel/blob/master/LICENSE | https://github.com/OHDSI/CommonDataModel |
-- MAGIC | OHDSI/ETL-Synthea| Apache License 2.0 | https://github.com/OHDSI/ETL-Synthea/blob/master/LICENSE | https://github.com/OHDSI/ETL-Synthea |
-- MAGIC |OHDSI/OMOP-Queries|||https://github.com/OHDSI/OMOP-Queries|
-- MAGIC |The Book of OHDSI | Creative Commons Zero v1.0 Universal license.|https://ohdsi.github.io/TheBookOfOhdsi/index.html#license|https://ohdsi.github.io/TheBookOfOhdsi/|