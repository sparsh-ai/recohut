// Setting up table

CREATE OR REPLACE TABLE ADAM_DB.public.test (
   id int,
   first_name string,
  last_name string,
  email string,
  gender string,
  Job string,
  Phone string);
    

COPY INTO ADAM_DB.public.test
from @MANAGE_DB.external_stages.time_travel_stage
files = ('customers.csv');

SELECT * FROM ADAM_DB.public.test;

// Use-case: Update data (by mistake)


UPDATE ADAM_DB.public.test
SET LAST_NAME = 'Tyson';


UPDATE ADAM_DB.public.test
SET JOB = 'Data Analyst';

SELECT * FROM ADAM_DB.public.test before (statement => '019b9eea-0500-845a-0043-4d830007402a')



// // // Bad method

CREATE OR REPLACE TABLE ADAM_DB.public.test as
SELECT * FROM ADAM_DB.public.test before (statement => '019b9eea-0500-845a-0043-4d830007402a')


SELECT * FROM ADAM_DB.public.test


CREATE OR REPLACE TABLE ADAM_DB.public.test as
SELECT * FROM ADAM_DB.public.test before (statement => '019b9eea-0500-8473-0043-4d830007307a')





// // // Good method

CREATE OR REPLACE TABLE ADAM_DB.public.test_backup as
SELECT * FROM ADAM_DB.public.test before (statement => '019b9ef0-0500-8473-0043-4d830007309a')

TRUNCATE ADAM_DB.public.test

INSERT INTO ADAM_DB.public.test
SELECT * FROM ADAM_DB.public.test_backup



SELECT * FROM ADAM_DB.public.test 