//  Parse & Analyse Raw JSON 

   // Selecting attribute/column

SELECT RAW_FILE:city FROM ADAM_DB.PUBLIC.JSON_RAW //Use of colon //

SELECT $1:first_name FROM ADAM_DB.PUBLIC.JSON_RAW //


   // Selecting attribute/column - formattted

SELECT RAW_FILE:first_name::string as first_name  FROM ADAM_DB.PUBLIC.JSON_RAW; // Remove Qoutes and convert to string //

SELECT RAW_FILE:id::int as id  FROM ADAM_DB.PUBLIC.JSON_RAW; // Again converting to int //

SELECT 
    RAW_FILE:id::int as id,  
    RAW_FILE:first_name::STRING as first_name,
    RAW_FILE:last_name::STRING as last_name,
    RAW_FILE:gender::STRING as gender

FROM ADAM_DB.PUBLIC.JSON_RAW;



   // Handling nested data
   
SELECT RAW_FILE:job as job  FROM ADAM_DB.PUBLIC.JSON_RAW;



SELECT 
      RAW_FILE:job.salary::INT as salary // Nested Pointing //Double :: //
FROM ADAM_DB.PUBLIC.JSON_RAW;



SELECT 
    RAW_FILE:first_name::STRING as first_name,
    RAW_FILE:job.salary::INT as salary,
    RAW_FILE:job.title::STRING as title
FROM ADAM_DB.PUBLIC.JSON_RAW;


// Handling arreys

SELECT
    RAW_FILE:prev_company as prev_company
FROM ADAM_DB.PUBLIC.JSON_RAW;

SELECT
    RAW_FILE:prev_company[1]::STRING as prev_company
FROM ADAM_DB.PUBLIC.JSON_RAW;


SELECT
    ARRAY_SIZE(RAW_FILE:prev_company) as prev_company //Useful syntax to aggregate //
FROM ADAM_DB.PUBLIC.JSON_RAW;

// Use Union COmmand //


SELECT 
    RAW_FILE:id::int as id,  
    RAW_FILE:first_name::STRING as first_name,
    RAW_FILE:prev_company[0]::STRING as prev_company
FROM ADAM_DB.PUBLIC.JSON_RAW
UNION ALL 
SELECT 
    RAW_FILE:id::int as id,  
    RAW_FILE:first_name::STRING as first_name,
    RAW_FILE:prev_company[1]::STRING as prev_company
FROM ADAM_DB.PUBLIC.JSON_RAW
ORDER BY id
