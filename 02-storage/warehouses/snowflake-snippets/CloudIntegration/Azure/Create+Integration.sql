
USE DATABASE ADAM_DB;
-- create integration object that contains the access information
CREATE STORAGE INTEGRATION azure_integration
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = AZURE
  ENABLED = TRUE
  AZURE_TENANT_ID = '9ecede0b-0e07-4da4-8047-e0672d6e403e'
  STORAGE_ALLOWED_LOCATIONS = ('azure://storageaccountsnow.blob.core.windows.net/snowflakecsv', 'azure://storageaccountsnow.blob.core.windows.net/snowflakejson');

  
-- Describe integration object to provide access
DESC STORAGE integration azure_integration;