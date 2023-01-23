// First step: Load Raw JSON

CREATE OR REPLACE stage MANAGE_DB.EXTERNAL_STAGES.JSONSTAGE
     url='s3://bucketsnowflake-jsondemo';

CREATE OR REPLACE file format MANAGE_DB.FILE_FORMATS.JSONFORMAT
    TYPE = JSON;
    
    
CREATE OR REPLACE table ADAM_DB.PUBLIC.JSON_RAW (
    raw_file variant);
    
COPY INTO ADAM_DB.PUBLIC.JSON_RAW
    FROM @MANAGE_DB.EXTERNAL_STAGES.JSONSTAGE
    file_format= MANAGE_DB.FILE_FORMATS.JSONFORMAT
    files = ('HR_data.json');
    
   
SELECT * FROM ADAM_DB.PUBLIC.JSON_RAW;