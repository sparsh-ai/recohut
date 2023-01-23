
--- Load JSON ----

 
create or replace file format ADAM_DB.public.fileformat_azure_json
    TYPE = JSON;
  
 
 
 
  
create or replace stage  ADAM_DB.public.stage_azure
    STORAGE_INTEGRATION = azure_integration
    URL = 'azure://storageaccountsnow.blob.core.windows.net/snowflakejson'
    FILE_FORMAT = fileformat_azure_json; 
  
LIST  @ ADAM_DB.public.stage_azure;

-- Query from stage  
SELECT * FROM @ ADAM_DB.public.stage_azure;  


-- Query one attribute/column
SELECT $1:"Car Model" FROM @ ADAM_DB.public.stage_azure; 
  
-- Convert data type  
SELECT $1:"Car Model"::STRING FROM @ ADAM_DB.public.stage_azure; 

-- Query all attributes  
SELECT 
$1:"Car Model"::STRING, 
$1:"Car Model Year"::INT,
$1:"car make"::STRING, 
$1:"first_name"::STRING,
$1:"last_name"::STRING
FROM @ ADAM_DB.public.stage_azure;   
  
-- Query all attributes and use aliases 
SELECT 
$1:"Car Model"::STRING as car_model, 
$1:"Car Model Year"::INT as car_model_year,
$1:"car make"::STRING as "car make", 
$1:"first_name"::STRING as first_name,
$1:"last_name"::STRING as last_name
FROM @ ADAM_DB.public.stage_azure;     


Create or replace table car_owner (
    car_model varchar, 
    car_model_year int,
    car_make varchar, 
    first_name varchar,
    last_name varchar)
 
COPY INTO car_owner
FROM
(SELECT 
$1:"Car Model"::STRING as car_model, 
$1:"Car Model Year"::INT as car_model_year,
$1:"car make"::STRING as "car make", 
$1:"first_name"::STRING as first_name,
$1:"last_name"::STRING as last_name
FROM @ ADAM_DB.public.stage_azure);

SELECT * FROM CAR_OWNER;


-- Alternative: Using a raw file table step
truncate table car_owner;
select * from car_owner;

create or replace table car_owner_raw (
  raw variant);

COPY INTO car_owner_raw
FROM @ ADAM_DB.public.stage_azure;

SELECT * FROM car_owner_raw;

    
INSERT INTO car_owner  
(SELECT 
$1:"Car Model"::STRING as car_model, 
$1:"Car Model Year"::INT as car_model_year,
$1:"car make"::STRING as car_make, 
$1:"first_name"::STRING as first_name,
$1:"last_name"::STRING as last_name
FROM car_owner_raw)  
  
  
select * from car_owner;
  