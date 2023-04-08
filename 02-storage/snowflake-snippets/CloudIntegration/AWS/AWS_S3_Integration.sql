// Create storage integration object

// Using AWS s3 bucket trial to create an integration object //

create or replace storage integration s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE 
  STORAGE_AWS_ROLE_ARN = ''
  STORAGE_ALLOWED_LOCATIONS = ('s3://AdamSnowflakeBucket/csv/', 's3://AdamSnowflakeBucket/json/')

   
   

// See storage integration properties to fetch external_id so we can update it in S3 trust relationship on policy! //
DESC integration s3_int;