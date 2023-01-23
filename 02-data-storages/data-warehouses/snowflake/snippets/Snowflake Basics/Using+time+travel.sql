// Setting up table

CREATE OR REPLACE TABLE ADAM_DB.public.test (
   id int,
   first_name string,
  last_name string,
  email string,
  gender string,
  Job string,
  Phone string)
    


CREATE OR REPLACE FILE FORMAT MANAGE_DB.file_formats.csv_file
    type = csv
    field_delimiter = ','
    skip_header = 1
    
CREATE OR REPLACE STAGE MANAGE_DB.external_stages.time_travel_stage
    URL = 's3://data-snowflake-fundamentals/time-travel/'
    file_format = MANAGE_DB.file_formats.csv_file;
    


LIST @MANAGE_DB.external_stages.time_travel_stage



COPY INTO ADAM_DB.public.test
from @MANAGE_DB.external_stages.time_travel_stage
files = ('customers.csv')


SELECT * FROM ADAM_DB.public.test

// Use-case: Update data (by mistake)

UPDATE ADAM_DB.public.test
SET FIRST_NAME = 'Joyen' 



// // // Using time travel: Method 1 - 2 minutes back
SELECT * FROM ADAM_DB.public.test at (OFFSET => -60*2)







select current_timestamp 
// // // Using time travel: Method 2 - before timestamp
SELECT * FROM ADAM_DB.public.test before (timestamp => '2022-07-13 12:03:17.346 -0700'::timestamp)


-- Setting up table
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



-- Setting up UTC time for convenience


ALTER SESSION SET TIMEZONE ='UTC'
SELECT DATEADD(DAY, 1, CURRENT_TIMESTAMP)



UPDATE ADAM_DB.public.test
SET Job = 'Data Scientist'


SELECT * FROM ADAM_DB.public.test;

SELECT * FROM ADAM_DB.public.test before (timestamp => '2021-04-16 07:30:47.145'::timestamp)








// // // Using time travel: Method 3 - before Query ID

// Preparing table
CREATE OR REPLACE TABLE ADAM_DB.public.test (
   id int,
   first_name string,
  last_name string,
  email string,
  gender string,
  Phone string,
  Job string)

COPY INTO ADAM_DB.public.test
from @MANAGE_DB.external_stages.time_travel_stage
files = ('customers.csv')


SELECT * FROM ADAM_DB.public.test


// Altering table (by mistake)
UPDATE ADAM_DB.public.test
SET EMAIL = null



SELECT * FROM ADAM_DB.public.test

SELECT * FROM ADAM_DB.public.test before (statement => '019b9ee5-0500-8473-0043-4d8300073062')