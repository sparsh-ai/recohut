           
// Setting up table

CREATE OR REPLACE STAGE MANAGE_DB.external_stages.time_travel_stage
    URL = 's3://data-snowflake-fundamentals/time-travel/'
    file_format = MANAGE_DB.file_formats.csv_file;
    

CREATE OR REPLACE TABLE ADAM_DB.public.customers (
   id int,
   first_name string,
  last_name string,
  email string,
  gender string,
  Job string,
  Phone string);
    

COPY INTO ADAM_DB.public.customers
from @MANAGE_DB.external_stages.time_travel_stage
files = ('customers.csv');

SELECT * FROM ADAM_DB.public.customers;


// UNDROP command - Tables

DROP TABLE ADAM_DB.public.customers;

SELECT * FROM ADAM_DB.public.customers;

UNDROP TABLE ADAM_DB.public.customers;


// UNDROP command - Schemas

DROP SCHEMA ADAM_DB.public;

SELECT * FROM ADAM_DB.public.customers;

UNDROP SCHEMA ADAM_DB.public;


// UNDROP command - Database

DROP DATABASE ADAM_DB;

SELECT * FROM ADAM_DB.public.customers;

UNDROP DATABASE ADAM_DB;





// Restore replaced table 


UPDATE ADAM_DB.public.customers
SET LAST_NAME = 'Tyson';


UPDATE ADAM_DB.public.customers
SET JOB = 'Data Analyst';



// // // Undroping a with a name that already exists

CREATE OR REPLACE TABLE ADAM_DB.public.customers as
SELECT * FROM ADAM_DB.public.customers before (statement => '01a595d5-3201-b9d6-0001-295a000130f6')


SELECT * FROM ADAM_DB.public.customers

UNDROP table ADAM_DB.public.customers;

ALTER TABLE ADAM_DB.public.customers
RENAME TO ADAM_DB.public.customers_wrong;


DESC table ADAM_DB.public.customers
    