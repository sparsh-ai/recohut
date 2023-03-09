
-- create file format
create or replace file format ADAM_DB.public.fileformat_gcp
    TYPE = CSV
    FIELD_DELIMITER = ','
    SKIP_HEADER = 1;

-- create stage object
create or replace stage ADAM_DB.public.stage_gcp
    STORAGE_INTEGRATION = gcp_integration
    URL = 'gcs://SFADAMgcpbucket'
    FILE_FORMAT = fileformat_gcp;

LIST @ADAM_DB.public.stage_gcp;
