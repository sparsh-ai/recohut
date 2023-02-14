-- Databricks notebook source
-- MAGIC %md
-- MAGIC # ETL: Synthea to OMOP531

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dbutils.widgets.text('root_path','/FileStore/health-lakehouse/')
-- MAGIC root_path=dbutils.widgets.get('root_path')

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Load synthea tables from Bronze layer

-- COMMAND ----------

-- MAGIC %python
-- MAGIC omop_version="OMOP531"
-- MAGIC delta_root_path = f"{root_path}delta/"
-- MAGIC print(f"Using OMOP version {omop_version}")
-- MAGIC print(f"Reading synthea delta tables from {delta_root_path}bronze")
-- MAGIC spark.sql(f"USE {omop_version}");

-- COMMAND ----------

-- MAGIC %python
-- MAGIC import pandas as pd
-- MAGIC 
-- MAGIC table_names =['allergies','careplans','conditions','devices','encounters','imaging_studies',\
-- MAGIC               'immunizations','medications','observations','organizations','patients',\
-- MAGIC               'payer_transitions','payers','procedures','providers','supplies']
-- MAGIC dataframes=[]
-- MAGIC for table_name in table_names:
-- MAGIC   df = spark.read.format('delta').load("{}/bronze/{}".format(delta_root_path,table_name))
-- MAGIC   df.createOrReplaceTempView(table_name)
-- MAGIC   dataframes+=[[table_name,df.count()]]
-- MAGIC 
-- MAGIC # Display number of records in each table
-- MAGIC pdf=pd.DataFrame(dataframes,columns=['table_name','n_records'])
-- MAGIC display(pdf.sort_values(by='n_records',ascending=False))

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Create temporary views

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### IP_VISITS

-- COMMAND ----------

CREATE OR REPLACE TEMPORARY VIEW IP_VISITS AS (
WITH CTE_END_DATES AS (
  SELECT
    patient,
    encounterclass,
    DATE_ADD(EVENT_DATE, -1) AS END_DATE
  FROM
    (
      SELECT
        patient,
        encounterclass,
        EVENT_DATE,
        EVENT_TYPE,
        MAX(START_ORDINAL) OVER (
          PARTITION BY patient,
          encounterclass
          ORDER BY
            EVENT_DATE,
            EVENT_TYPE ROWS UNBOUNDED PRECEDING
        ) AS START_ORDINAL,
        ROW_NUMBER() OVER (
          PARTITION BY patient,
          encounterclass
          ORDER BY
            EVENT_DATE,
            EVENT_TYPE
        ) AS OVERALL_ORD
      FROM
        (
          SELECT
            patient,
            encounterclass,
            start AS EVENT_DATE,
            -1 AS EVENT_TYPE,
            ROW_NUMBER () OVER (
              PARTITION BY patient,
              encounterclass
              ORDER BY
                start,
                stop
            ) AS START_ORDINAL
          FROM
            encounters
          WHERE
            encounterclass = 'inpatient'
          UNION ALL
          SELECT
            patient,
            encounterclass,
            DATE_ADD(stop, 1),
            1 AS EVENT_TYPE,
            NULL
          FROM
            encounters
          WHERE
            encounterclass = 'inpatient'
        ) RAWDATA
    ) E
  WHERE
    (2 * E.START_ORDINAL - E.OVERALL_ORD = 0)
),
CTE_VISIT_ENDS AS (
  SELECT
    MIN(V.id) AS encounter_id,
    V.patient,
    V.encounterclass,
    V.start AS VISIT_START_DATE,
    MIN(E.END_DATE) AS VISIT_END_DATE
  FROM
    encounters V
    INNER JOIN CTE_END_DATES E ON V.patient = E.patient
    AND V.encounterclass = E.encounterclass
    AND E.END_DATE >= V.start
  GROUP BY
    V.patient,
    V.encounterclass,
    V.start
)
SELECT
  T2.encounter_id,
  T2.patient,
  T2.encounterclass,
  T2.VISIT_START_DATE,
  T2.VISIT_END_DATE
FROM
  (
    SELECT
      encounter_id,
      patient,
      encounterclass,
      MIN(VISIT_START_DATE) AS VISIT_START_DATE,
      VISIT_END_DATE
    FROM
      CTE_VISIT_ENDS
    GROUP BY
      encounter_id,
      patient,
      encounterclass,
      VISIT_END_DATE
  ) T2
);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### ER_VISITS

-- COMMAND ----------

CREATE OR REPLACE TEMPORARY VIEW ER_VISITS AS
SELECT
  T2.encounter_id,
  T2.patient,
  T2.encounterclass,
  T2.VISIT_START_DATE,
  T2.VISIT_END_DATE
FROM
  (
    SELECT
      MIN(encounter_id) AS encounter_id,
      patient,
      encounterclass,
      VISIT_START_DATE,
      MAX(VISIT_END_DATE) AS VISIT_END_DATE
    FROM
      (
        SELECT
          CL1.id AS encounter_id,
          CL1.patient,
          CL1.encounterclass,
          CL1.start AS VISIT_START_DATE,
          CL2.stop AS VISIT_END_DATE
        FROM
          encounters CL1
          INNER JOIN encounters CL2 ON CL1.patient = CL2.patient
          AND CL1.start = CL2.start
          AND CL1.encounterclass = CL2.encounterclass
        WHERE
          CL1.encounterclass in ('emergency', 'urgent')
      ) T1
    GROUP BY
      patient,
      encounterclass,
      VISIT_START_DATE
  ) T2;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### OP_VISITS

-- COMMAND ----------

CREATE
OR REPLACE TEMPORARY VIEW OP_VISITS AS WITH CTE_VISITS_DISTINCT AS (
  SELECT
    MIN(id) AS encounter_id,
    patient,
    encounterclass,
    start AS VISIT_START_DATE,
    stop AS VISIT_END_DATE
  FROM
    encounters
  WHERE
    encounterclass in ('ambulatory', 'wellness', 'outpatient')
  GROUP BY
    patient,
    encounterclass,
    start,
    stop
)
SELECT
  MIN(encounter_id) AS encounter_id,
  patient,
  encounterclass,
  VISIT_START_DATE,
  MAX(VISIT_END_DATE) AS VISIT_END_DATE
FROM
  CTE_VISITS_DISTINCT
GROUP BY
  patient,
  encounterclass,
  VISIT_START_DATE;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Create tables

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### all_visits

-- COMMAND ----------

DROP TABLE IF EXISTS all_visits;
CREATE TABLE all_visits
SELECT
  *,
  ROW_NUMBER() OVER(
    ORDER BY
      patient
  ) as visit_occurrence_id
FROM
  (
    SELECT
      *
    FROM
      IP_VISITS
    UNION ALL
    SELECT
      *
    FROM
      ER_VISITS
    UNION ALL
    SELECT
      *
    FROM
      OP_VISITS
  ) T1;


-- COMMAND ----------

SELECT
  *
FROM
  all_visits
LIMIT
  100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### assign_all_visit_ids

-- COMMAND ----------

DROP TABLE IF EXISTS assign_all_visit_ids;
CREATE TABLE assign_all_visit_ids
SELECT
  E.id AS encounter_id,
  E.patient as person_source_value,
  E.start AS date_service,
  E.stop AS date_service_end,
  E.encounterclass,
  AV.encounterclass AS VISIT_TYPE,
  AV.VISIT_START_DATE,
  AV.VISIT_END_DATE,
  AV.VISIT_OCCURRENCE_ID,
  CASE
    WHEN E.encounterclass = 'inpatient'
    and AV.encounterclass = 'inpatient' THEN VISIT_OCCURRENCE_ID
    WHEN E.encounterclass in ('emergency', 'urgent') THEN (
      CASE
        WHEN AV.encounterclass = 'inpatient'
        AND E.start > AV.VISIT_START_DATE THEN VISIT_OCCURRENCE_ID
        WHEN AV.encounterclass in ('emergency', 'urgent')
        AND E.start = AV.VISIT_START_DATE THEN VISIT_OCCURRENCE_ID
        ELSE NULL
      END
    )
    WHEN E.encounterclass in ('ambulatory', 'wellness', 'outpatient') THEN (
      CASE
        WHEN AV.encounterclass = 'inpatient'
        AND E.start >= AV.VISIT_START_DATE THEN VISIT_OCCURRENCE_ID
        WHEN AV.encounterclass in ('ambulatory', 'wellness', 'outpatient') THEN VISIT_OCCURRENCE_ID
        ELSE NULL
      END
    )
    ELSE NULL
  END AS VISIT_OCCURRENCE_ID_NEW
FROM
  ENCOUNTERS E
  INNER JOIN ALL_VISITS AV ON E.patient = AV.patient
  AND E.start >= AV.VISIT_START_DATE
  AND E.start <= AV.VISIT_END_DATE;


-- COMMAND ----------

SELECT * FROM assign_all_visit_ids LIMIT 100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### final_visit_ids

-- COMMAND ----------

DROP TABLE IF EXISTS final_visit_ids;
CREATE TABLE final_visit_ids
SELECT encounter_id, VISIT_OCCURRENCE_ID_NEW
FROM(
	SELECT *, ROW_NUMBER () OVER (PARTITION BY encounter_id ORDER BY PRIORITY) AS RN
	FROM (
		SELECT *,
			CASE
				WHEN encounterclass in ('emergency','urgent')
					THEN (
						CASE
							WHEN VISIT_TYPE = 'inpatient' AND VISIT_OCCURRENCE_ID_NEW IS NOT NULL
								THEN 1
							WHEN VISIT_TYPE in ('emergency','urgent') AND VISIT_OCCURRENCE_ID_NEW IS NOT NULL
								THEN 2
							ELSE 99
						END
					)
				WHEN encounterclass in ('ambulatory', 'wellness', 'outpatient')
					THEN (
						CASE
							WHEN VISIT_TYPE = 'inpatient' AND VISIT_OCCURRENCE_ID_NEW IS NOT NULL
								THEN  1
							WHEN VISIT_TYPE in ('ambulatory', 'wellness', 'outpatient') AND VISIT_OCCURRENCE_ID_NEW IS NOT NULL
								THEN 2
							ELSE 99
						END
					)
				WHEN encounterclass = 'inpatient' AND VISIT_TYPE = 'inpatient' AND VISIT_OCCURRENCE_ID_NEW IS NOT NULL
					THEN 1
				ELSE 99
			END AS PRIORITY
	FROM ASSIGN_ALL_VISIT_IDS
	) T1
) T2
WHERE RN=1;


-- COMMAND ----------

SELECT * FROM final_visit_ids LIMIT 100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### person

-- COMMAND ----------

INSERT
  OVERWRITE person
SELECT
  ROW_NUMBER() OVER(
    ORDER BY
      p.id
  ),
  case
    upper(p.gender)
    when 'M' then 8507
    when 'F' then 8532
  end,
  YEAR(p.birthdate),
  MONTH(p.birthdate),
  DAY(p.birthdate),
  p.birthdate,
  case
    upper(p.race)
    when 'WHITE' then 8527
    when 'BLACK' then 8516
    when 'ASIAN' then 8515
    else 0
  end,
  case
    when upper(p.race) = 'HISPANIC' then 38003563
    else 0
  end,
  NULL,
  0,
  NULL,
  p.id,
  p.gender,
  0,
  p.race,
  0,
  p.ethnicity,
  0
from
  patients p
where
  p.gender is not null;


-- COMMAND ----------

SELECT
  *
FROM
  person
LIMIT
  100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### observation_period

-- COMMAND ----------

INSERT
  OVERWRITE observation_period
SELECT
  ROW_NUMBER() OVER(
    ORDER BY
      person_id
  ),
  person_id,
  start_date,
  end_date,
  44814724 AS period_type_concept_id
FROM
  (
    SELECT
      p.person_id,
      MIN(e.start) AS start_date,
      MAX(e.stop) AS end_date
    FROM
      person p
      INNER JOIN encounters e ON p.person_source_value = e.patient
    GROUP BY
      p.person_id
  ) tmp;


-- COMMAND ----------

SELECT
  *
FROM
  observation_period
LIMIT
  100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### visit_occurrence

-- COMMAND ----------

INSERT
  OVERWRITE visit_occurrence
select
  av.visit_occurrence_id,
  p.person_id,
  case
    lower(av.encounterclass)
    when 'ambulatory' then 9202
    when 'emergency' then 9203
    when 'inpatient' then 9201
    when 'wellness' then 9202
    when 'urgentcare' then 9203
    when 'outpatient' then 9202
    else 0
  end,
  av.visit_start_date,
  av.visit_start_date,
  av.visit_end_date,
  av.visit_end_date,
  44818517,
  0,
  null,
  av.encounter_id,
  0,
  0,
  NULL,
  0,
  NULL,
  lag(visit_occurrence_id) over(
    partition by p.person_id
    order by
      av.visit_start_date
  )
from
  all_visits av
  join person p on av.patient = p.person_source_value
where
  av.visit_occurrence_id in (
    select
      distinct visit_occurrence_id_new
    from
      final_visit_ids
  );


-- COMMAND ----------

SELECT
  *
FROM
  visit_occurrence
LIMIT
  100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### condition_occurrence

-- COMMAND ----------

INSERT OVERWRITE condition_occurrence
select
  row_number()over(order by p.person_id),
  p.person_id,
  coalesce(srctostdvm.target_concept_id,0) AS target_concept_id,
  c.start,
  c.start,
  c.stop,
  c.stop,
  32020,
  null,
  0,
  fv.visit_occurrence_id_new AS visit_occurrence_id,
  0,
  c.code,
  coalesce(srctosrcvm.source_concept_id,0),
  NULL,
  0
from conditions c
inner join source_to_standard_vocab_map srctostdvm
on srctostdvm.source_code             = c.code
 and srctostdvm.target_domain_id        = 'Condition'
 and srctostdvm.source_vocabulary_id    = 'SNOMED'
 and srctostdvm.target_standard_concept = 'S'
 and (srctostdvm.target_invalid_reason IS NULL OR srctostdvm.target_invalid_reason = '')
left join source_to_source_vocab_map srctosrcvm
  on srctosrcvm.source_code             = c.code
 and srctosrcvm.source_vocabulary_id    = 'SNOMED'
left join final_visit_ids fv
  on fv.encounter_id = c.encounter
inner join person p
  on c.patient = p.person_source_value;


-- COMMAND ----------

SELECT
  *
FROM
  condition_occurrence
LIMIT
  100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### measurement

-- COMMAND ----------

INSERT OVERWRITE measurement
SELECT row_number()over(order by person_id) AS measurement_id,
person_id,
measurement_concept_id,
measurement_date,
measurement_datetime,
measurement_time,
measurement_type_concept_id,
operator_concept_id,
value_as_number,
value_as_concept_id,
unit_concept_id,
range_low,
range_high,
provider_id,
visit_occurrence_id,
visit_detail_id,
measurement_source_value,
measurement_source_concept_id,
unit_source_value,
value_source_value
from (
select
  p.person_id,
  coalesce(srctostdvm.target_concept_id,0) AS measurement_concept_id,
  pr.start AS measurement_date,
  pr.start AS measurement_datetime,
  pr.start AS measurement_time,
  5001 AS measurement_type_concept_id,
  0 as operator_concept_id,
  null as value_as_number,
  0 as value_as_concept_id,
  0 as unit_concept_id,
  null as range_low,
  null as range_high,
  0 as provider_id,
  fv.visit_occurrence_id_new AS visit_occurrence_id,
  0 as visit_detail_id,
  pr.code AS measurement_source_value,
  coalesce(srctosrcvm.source_concept_id,0) AS measurement_source_concept_id,
  null as unit_source_value,
  null as value_source_value
from procedures pr
inner join source_to_standard_vocab_map  srctostdvm
  on srctostdvm.source_code             = pr.code
 and srctostdvm.target_domain_id        = 'Measurement'
 and srctostdvm.source_vocabulary_id    = 'SNOMED'
 and srctostdvm.target_standard_concept = 'S'
 and (srctostdvm.target_invalid_reason IS NULL or srctostdvm.target_invalid_reason = '')
left join source_to_source_vocab_map srctosrcvm
  on srctosrcvm.source_code             = pr.code
 and srctosrcvm.source_vocabulary_id    = 'SNOMED'
left join final_visit_ids fv
  on fv.encounter_id = pr.encounter
join person p
  on p.person_source_value              = pr.patient
union all
select
  p.person_id,
  coalesce(srctostdvm.target_concept_id,0) AS target_concept_id,
  o.date,
  o.date,
  o.date,
  5001,
  0,
  nanvl(cast(o.value as float), null) as value_as_number,
  coalesce(srcmap2.target_concept_id,0) AS value_as_concept_id,
  coalesce(srcmap1.target_concept_id,0) AS unit_concept_id,
  null ,
  null ,
  0 as provider_id,
  fv.visit_occurrence_id_new AS visit_occurrence_id,
  0 as visit_detail_id,
  o.code AS measurement_source_value,
  coalesce(srctosrcvm.source_concept_id,0) AS measurement_source_concept_id,
  o.units AS unit_source_value,
  o.value AS value_source_value
from observations o
inner join source_to_standard_vocab_map  srctostdvm
  on srctostdvm.source_code             = o.code
 and srctostdvm.target_domain_id        = 'Measurement'
 and srctostdvm.source_vocabulary_id    = 'LOINC'
 and srctostdvm.target_standard_concept = 'S'
 and (srctostdvm.target_invalid_reason IS NULL OR srctostdvm.target_invalid_reason = '')
left join source_to_standard_vocab_map  srcmap1
  on srcmap1.source_code                = o.units
 and srcmap1.target_vocabulary_id       = 'UCUM'
 and srcmap1.target_standard_concept    = 'S'
 and (srcmap1.target_invalid_reason IS NULL OR srcmap1.target_invalid_reason = '')
left join source_to_standard_vocab_map  srcmap2
  on srcmap2.source_code                = o.value
 and srcmap2.target_domain_id           = 'Meas value'
 and srcmap2.target_standard_concept    = 'S'
 and (srcmap2.target_invalid_reason IS NULL OR srcmap2.target_invalid_reason = '')
left join source_to_source_vocab_map srctosrcvm
  on srctosrcvm.source_code             = o.code
 and srctosrcvm.source_vocabulary_id    = 'LOINC'
left join final_visit_ids fv
  on fv.encounter_id                    = o.encounter
inner join person p
  on p.person_source_value              = o.patient
  ) tmp;

-- COMMAND ----------

SELECT
  *
FROM
  measurement
LIMIT
  100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### procedure_occurrence

-- COMMAND ----------

INSERT OVERWRITE procedure_occurrence
SELECT
  row_number()over(order by p.person_id),
  p.person_id,
  coalesce(srctostdvm.target_concept_id, 0) as target_concept_id,
  pr.start,
  pr.start,
  38000275,
  0,
  null,
  0,
  fv.visit_occurrence_id_new AS visit_occurrence_id,
  0,
  pr.code,
  coalesce(srctosrcvm.source_concept_id,0),
  NULL
from procedures pr
inner join source_to_standard_vocab_map  srctostdvm
  on srctostdvm.source_code             = pr.code
 and srctostdvm.target_domain_id        = 'Procedure'
 and srctostdvm.source_vocabulary_id    = 'SNOMED'
 and srctostdvm.target_standard_concept = 'S'
 and (srctostdvm.target_invalid_reason IS NULL OR srctostdvm.target_invalid_reason = '')
left join source_to_source_vocab_map srctosrcvm
  on srctosrcvm.source_code             = pr.code
 and srctosrcvm.source_vocabulary_id    = 'SNOMED'
left join final_visit_ids fv
  on fv.encounter_id = pr.encounter
inner join person p
  on p.person_source_value    = pr.patient;


-- COMMAND ----------

SELECT
  *
FROM
  procedure_occurrence
LIMIT
  100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### drug_exposure

-- COMMAND ----------

INSERT OVERWRITE drug_exposure
SELECT row_number()over(order by person_id) AS drug_exposure_id,
person_id,
drug_concept_id,
drug_exposure_start_date,
drug_exposure_start_datetime,
drug_exposure_end_date,
drug_exposure_end_datetime,
verbatim_end_date,
drug_type_concept_id,
stop_reason,
refills,
quantity,
days_supply,
sig,
route_concept_id,
lot_number,
provider_id,
visit_occurrence_id,
visit_detail_id,
drug_source_value,
drug_source_concept_id,
route_source_value,
dose_unit_source_value
  from (
select
  p.person_id,
  coalesce(srctostdvm.target_concept_id,0) as drug_concept_id,
  c.start AS drug_exposure_start_date,
  c.start AS drug_exposure_start_datetime,
  coalesce(c.stop,c.start) AS drug_exposure_end_date,
  coalesce(c.stop,c.start) AS drug_exposure_end_datetime,
  c.stop AS verbatim_end_date,
  581452 as drug_type_concept_id,
  null as  stop_reason,
  0 as refills,
  0 as quantity,
  coalesce(datediff(c.stop,c.start),0) as days_supply,
  null as  sig,
  0 as route_concept_id,
  0 as lot_number,
  0 as provider_id,
  fv.visit_occurrence_id_new AS visit_occurrence_id,
  0 as visit_detail_id,
  c.code AS drug_source_value,
  coalesce(srctosrcvm.source_concept_id,0) AS drug_source_concept_id,
  null as  route_source_value,
  null as  dose_unit_source_value
from conditions c
 join source_to_standard_vocab_map   srctostdvm
on srctostdvm.source_code             = c.code
 and srctostdvm.target_domain_id        = 'Drug'
 and srctostdvm.source_vocabulary_id    = 'RxNorm'
 and srctostdvm.target_standard_concept = 'S'
 and (srctostdvm.target_invalid_reason IS NULL OR srctostdvm.target_invalid_reason = '')
left join source_to_source_vocab_map srctosrcvm
  on srctosrcvm.source_code             = c.code
 and srctosrcvm.source_vocabulary_id    = 'RxNorm'
left join final_visit_ids fv
  on fv.encounter_id = c.encounter
join person p
  on p.person_source_value              = c.patient
union all
select
  p.person_id,
  coalesce(srctostdvm.target_concept_id,0) as drug_concept_id,
  m.start,
  m.start,
  coalesce(m.stop,m.start),
  coalesce(m.stop,m.start),
  m.stop,
  38000177,
  null,
  0,
  0,
  coalesce(datediff(m.stop,m.start),0),
  null,
  0,
  0,
  0,
  fv.visit_occurrence_id_new AS visit_occurrence_id,
  0,
  m.code,
  coalesce(srctosrcvm.source_concept_id,0),
  null,
  null 
from medications m
  join source_to_standard_vocab_map   srctostdvm
on srctostdvm.source_code             = m.code
 and srctostdvm.target_domain_id        = 'Drug'
 and srctostdvm.source_vocabulary_id    = 'RxNorm'
 and srctostdvm.target_standard_concept = 'S'
 and (srctostdvm.target_invalid_reason IS  NULL OR srctostdvm.target_invalid_reason = '')
left join source_to_source_vocab_map srctosrcvm
  on srctosrcvm.source_code             = m.code
 and srctosrcvm.source_vocabulary_id    = 'RxNorm'
left join final_visit_ids fv
  on fv.encounter_id = m.encounter
join person p
  on p.person_source_value              = m.patient
union all
select
  p.person_id,
  coalesce(srctostdvm.target_concept_id,0) as drug_concept_id,
  i.date,
  i.date,
  i.date,
  i.date,
  i.date,
  581452,
  null,
  0,
  0,
  0,
  null,
  0,
  0,
  0,
  fv.visit_occurrence_id_new AS visit_occurrence_id,
  0,
  i.code,
  coalesce(srctosrcvm.source_concept_id,0),
  null,
  null
from immunizations i
  left join source_to_standard_vocab_map   srctostdvm
on srctostdvm.source_code             = i.code
 and srctostdvm.target_domain_id        = 'Drug'
 and srctostdvm.source_vocabulary_id    = 'CVX'
 and srctostdvm.target_standard_concept = 'S'
 and (srctostdvm.target_invalid_reason IS NULL OR srctostdvm.target_invalid_reason = '')
left join source_to_source_vocab_map srctosrcvm
  on srctosrcvm.source_code             = i.code
 and srctosrcvm.source_vocabulary_id    = 'CVX'
left join final_visit_ids fv
  on fv.encounter_id = i.encounter
join person p
  on p.person_source_value              = i.patient
  ) tmp;

-- COMMAND ----------

SELECT
  *
FROM
  drug_exposure
LIMIT
  100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### condition_era

-- COMMAND ----------

INSERT OVERWRITE condition_era (
WITH cteConditionTarget (condition_occurrence_id, person_id, condition_concept_id, condition_start_datetime, condition_end_datetime) AS
(
	SELECT
		co.condition_occurrence_id
		, co.person_id
		, co.condition_concept_id
		, co.condition_start_datetime
		, COALESCE(co.condition_end_datetime, date_add(condition_start_datetime,1)) AS condition_end_datetime
	FROM condition_occurrence co
	/* Depending on the needs of your data, you can put more filters on to your code. We assign 0 to our unmapped condition_concept_id's,
	 * and since we don't want different conditions put in the same era, we put in the filter below.
 	 */
	---WHERE condition_concept_id != 0
),
--------------------------------------------------------------------------------------------------------------
cteEndDates (person_id, condition_concept_id, end_date) AS -- the magic
(
	SELECT
		person_id
		, condition_concept_id
		, date_add(event_date,-30) AS end_date -- unpad the end date
	FROM
	(
		SELECT
			person_id
			, condition_concept_id
			, event_date
			, event_type
			, MAX(start_ordinal) OVER (PARTITION BY person_id, condition_concept_id ORDER BY event_date, event_type ROWS UNBOUNDED PRECEDING) AS start_ordinal -- this pulls the current START down from the prior rows so that the NULLs from the END DATES will contain a value we can compare with
			, ROW_NUMBER() OVER (PARTITION BY person_id, condition_concept_id ORDER BY event_date, event_type) AS overall_ord -- this re-numbers the inner UNION so all rows are numbered ordered by the event date
		FROM
		(
			-- select the start dates, assigning a row number to each
			SELECT
				person_id
				, condition_concept_id
				, condition_start_datetime AS event_date
				, -1 AS event_type
				, ROW_NUMBER() OVER (PARTITION BY person_id, condition_concept_id ORDER BY condition_start_datetime) AS start_ordinal
			FROM cteConditionTarget
			UNION ALL
			-- pad the end dates by 30 to allow a grace period for overlapping ranges.
			SELECT
				person_id
			    , condition_concept_id
				, date_add(condition_end_datetime,30)
				, 1 AS event_type
				, NULL
			FROM cteConditionTarget
		) RAWDATA
	) e
	WHERE (2 * e.start_ordinal) - e.overall_ord = 0
),
--------------------------------------------------------------------------------------------------------------
cteConditionEnds (person_id, condition_concept_id, condition_start_datetime, era_end_datetime) AS
(
SELECT
        c.person_id
	, c.condition_concept_id
	, c.condition_start_datetime
	, MIN(e.end_date) AS era_end_datetime
FROM cteConditionTarget c
INNER JOIN cteEndDates e ON c.person_id = e.person_id AND c.condition_concept_id = e.condition_concept_id AND e.end_date >= c.condition_start_datetime
GROUP BY
        c.condition_occurrence_id
	, c.person_id
	, c.condition_concept_id
	, c.condition_start_datetime
)
--------------------------------------------------------------------------------------------------------------
SELECT
    row_number()over(order by person_id) AS condition_era_id
	, person_id
	, condition_concept_id
	, MIN(condition_start_datetime) AS condition_era_start_datetime
	, era_end_datetime AS condition_era_end_datetime
	, COUNT(*) AS condition_occurrence_count
FROM cteConditionEnds
GROUP BY person_id, condition_concept_id, era_end_datetime)
;

-- COMMAND ----------

SELECT
  *
FROM
  condition_era
LIMIT
  100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### drug_era

-- COMMAND ----------

INSERT OVERWRITE drug_era (
WITH
ctePreDrugTarget(drug_exposure_id, person_id, ingredient_concept_id, drug_exposure_start_datetime, days_supply, drug_exposure_end_datetime) AS
(-- Normalize DRUG_EXPOSURE_END_DATE to either the existing drug exposure end date, or add days supply, or add 1 day to the start date
	SELECT
		d.drug_exposure_id
		, d.person_id
		, c.concept_id AS ingredient_concept_id
		, d.drug_exposure_start_datetime AS drug_exposure_start_datetime
		, d.days_supply AS days_supply
		, COALESCE(
			---NULLIF returns NULL if both values are the same, otherwise it returns the first parameter
			ifnull(drug_exposure_end_datetime, NULL),
			---If drug_exposure_end_date != NULL, return drug_exposure_end_date, otherwise go to next case
			ifnull(date_add(drug_exposure_start_datetime,cast(days_supply as int)), drug_exposure_start_datetime),
			---If days_supply != NULL or 0, return drug_exposure_start_date + days_supply, otherwise go to next case
			date_add(drug_exposure_start_datetime,1)
			---Add 1 day to the drug_exposure_start_date since there is no end_date or INTERVAL for the days_supply
		) AS drug_exposure_end_datetime
	FROM drug_exposure d
		INNER JOIN concept_ancestor ca ON ca.descendant_concept_id = d.drug_concept_id
		INNER JOIN concept c ON ca.ancestor_concept_id = c.concept_id
		WHERE c.vocabulary_id = 'RxNorm' ---8 selects RxNorm from the vocabulary_id
		AND c.concept_class_id = 'Ingredient'
		AND d.drug_concept_id != 0 ---Our unmapped drug_concept_id's are set to 0, so we don't want different drugs wrapped up in the same era
		AND coalesce(d.days_supply,0) >= 0 ---We have cases where days_supply is negative, and this can set the end_date before the start_date, which we don't want. So we're just looking over those rows. This is a data-quality issue.
)

, cteSubExposureEndDates (person_id, ingredient_concept_id, end_datetime) AS --- A preliminary sorting that groups all of the overlapping exposures into one exposure so that we don't double-count non-gap-days
(
	SELECT person_id, ingredient_concept_id, event_date AS end_datetime
	FROM
	(
		SELECT person_id, ingredient_concept_id, event_date, event_type,
		MAX(start_ordinal) OVER (PARTITION BY person_id, ingredient_concept_id ORDER BY event_date, event_type ROWS unbounded preceding) AS start_ordinal,
		-- this pulls the current START down from the prior rows so that the NULLs
		-- from the END DATES will contain a value we can compare with
		ROW_NUMBER() OVER (PARTITION BY person_id, ingredient_concept_id ORDER BY event_date, event_type) AS overall_ord
			-- this re-numbers the inner UNION so all rows are numbered ordered by the event date
		FROM (
			-- select the start dates, assigning a row number to each
			SELECT person_id, ingredient_concept_id, drug_exposure_start_datetime AS event_date,
			-1 AS event_type,
			ROW_NUMBER() OVER (PARTITION BY person_id, ingredient_concept_id ORDER BY drug_exposure_start_datetime) AS start_ordinal
			FROM ctePreDrugTarget
			UNION ALL
			SELECT person_id, ingredient_concept_id, drug_exposure_end_datetime, 1 AS event_type, NULL
			FROM ctePreDrugTarget
		) RAWDATA
	) e
	WHERE (2 * e.start_ordinal) - e.overall_ord = 0
)

, cteDrugExposureEnds (person_id, drug_concept_id, drug_exposure_start_datetime, drug_sub_exposure_end_datetime) AS
(
SELECT
	dt.person_id
	, dt.ingredient_concept_id
	, dt.drug_exposure_start_datetime
	, MIN(e.end_datetime) AS drug_sub_exposure_end_datetime
FROM ctePreDrugTarget dt
INNER JOIN cteSubExposureEndDates e ON dt.person_id = e.person_id AND dt.ingredient_concept_id = e.ingredient_concept_id AND e.end_datetime >= dt.drug_exposure_start_datetime
GROUP BY
      	dt.drug_exposure_id
      	, dt.person_id
	, dt.ingredient_concept_id
	, dt.drug_exposure_start_datetime
)
--------------------------------------------------------------------------------------------------------------
, cteSubExposures(row_number, person_id, drug_concept_id, drug_sub_exposure_start_datetime, drug_sub_exposure_end_datetime, drug_exposure_count) AS
(
	SELECT ROW_NUMBER() OVER (PARTITION BY person_id, drug_concept_id, drug_sub_exposure_end_datetime ORDER BY person_id)
		, person_id, drug_concept_id, MIN(drug_exposure_start_datetime) AS drug_sub_exposure_start_datetime, drug_sub_exposure_end_datetime, COUNT(*) AS drug_exposure_count
	FROM cteDrugExposureEnds
	GROUP BY person_id, drug_concept_id, drug_sub_exposure_end_datetime
	--ORDER BY person_id, drug_concept_id
)
--------------------------------------------------------------------------------------------------------------
/*Everything above grouped exposures into sub_exposures if there was overlap between exposures.
 *So there was no persistence window. Now we can add the persistence window to calculate eras.
 */
--------------------------------------------------------------------------------------------------------------
, cteFinalTarget(row_number, person_id, ingredient_concept_id, drug_sub_exposure_start_datetime, drug_sub_exposure_end_datetime, drug_exposure_count, days_exposed) AS
(
	SELECT row_number, person_id, drug_concept_id, drug_sub_exposure_start_datetime, drug_sub_exposure_end_datetime, drug_exposure_count
		, datediff(drug_sub_exposure_end_datetime,drug_sub_exposure_start_datetime) AS days_exposed
	FROM cteSubExposures
)
--------------------------------------------------------------------------------------------------------------
, cteEndDates (person_id, ingredient_concept_id, end_datetime) AS -- the magic
(
	SELECT person_id, ingredient_concept_id, date_add(event_date,-30) AS end_datetime -- unpad the end date
	FROM
	(
		SELECT person_id, ingredient_concept_id, event_date, event_type,
		MAX(start_ordinal) OVER (PARTITION BY person_id, ingredient_concept_id ORDER BY event_date, event_type ROWS UNBOUNDED PRECEDING) AS start_ordinal,
		-- this pulls the current START down from the prior rows so that the NULLs
		-- from the END DATES will contain a value we can compare with
		ROW_NUMBER() OVER (PARTITION BY person_id, ingredient_concept_id ORDER BY event_date, event_type) AS overall_ord
			-- this re-numbers the inner UNION so all rows are numbered ordered by the event date
		FROM (
			-- select the start dates, assigning a row number to each
			SELECT person_id, ingredient_concept_id, drug_sub_exposure_start_datetime AS event_date,
			-1 AS event_type,
			ROW_NUMBER() OVER (PARTITION BY person_id, ingredient_concept_id ORDER BY drug_sub_exposure_start_datetime) AS start_ordinal
			FROM cteFinalTarget
			UNION ALL
			-- pad the end dates by 30 to allow a grace period for overlapping ranges.
			SELECT person_id, ingredient_concept_id, date_add(drug_sub_exposure_end_datetime,30), 1 AS event_type, NULL
			FROM cteFinalTarget
		) RAWDATA
	) e
	WHERE (2 * e.start_ordinal) - e.overall_ord = 0

)
, cteDrugEraEnds (person_id, drug_concept_id, drug_sub_exposure_start_datetime, drug_era_end_datetime, drug_exposure_count, days_exposed) AS
(
SELECT
	ft.person_id
	, ft.ingredient_concept_id
	, ft.drug_sub_exposure_start_datetime
	, MIN(e.end_datetime) AS era_end_datetime
	, drug_exposure_count
	, days_exposed
FROM cteFinalTarget ft
JOIN cteEndDates e ON ft.person_id = e.person_id AND ft.ingredient_concept_id = e.ingredient_concept_id AND e.end_datetime >= ft.drug_sub_exposure_start_datetime
GROUP BY
      	ft.person_id
	, ft.ingredient_concept_id
	, ft.drug_sub_exposure_start_datetime
	, drug_exposure_count
	, days_exposed
)
SELECT
    row_number()over(order by person_id) drug_era_id
	, person_id
	, drug_concept_id
	, MIN(drug_sub_exposure_start_datetime) AS drug_era_start_datetime
	, drug_era_end_datetime
	, SUM(drug_exposure_count) AS drug_exposure_count
	, datediff(date_add(drug_era_end_datetime,cast(-(datediff(drug_era_end_datetime,MIN(drug_sub_exposure_start_datetime))-SUM(days_exposed)) as int)),'1970-01-01') as gap_days
FROM cteDrugEraEnds dee
GROUP BY person_id, drug_concept_id, drug_era_end_datetime
);


-- COMMAND ----------

SELECT * FROM drug_era LIMIT 100;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### cdm_source

-- COMMAND ----------

INSERT OVERWRITE cdm_source 
SELECT
'Synthea synthetic health database',
'Synthea',
'Databricks HLS',
'SyntheaTM is a Synthetic Patient Population Simulator. The goal is to output synthetic, realistic (but not real), patient data and associated health records in a variety of formats.',
'https://synthetichealth.github.io/synthea/',
'https://github.com/databricks/hls-solution-accelerators/',
current_date(), -- NB: Set this value to the day the source data was pulled
current_date(), 
'v5.3.1',
vocabulary_version
from vocabulary 
where vocabulary_id = 'None';

-- COMMAND ----------

SELECT * FROM cdm_source LIMIT 100;

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