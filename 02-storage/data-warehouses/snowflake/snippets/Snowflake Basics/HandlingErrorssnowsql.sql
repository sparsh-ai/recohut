 // Create new stage
 CREATE OR REPLACE STAGE MANAGE_DB.external_stages.aws_stage_errorex
    url='s3://bucketsnowflakes4'
 
 // List files in stage
 LIST @MANAGE_DB.external_stages.aws_stage_errorex;
 
 
 // Create example table
 CREATE OR REPLACE TABLE ADAM_DB.PUBLIC.ORDERS_EX (
    ORDER_ID VARCHAR(30),
    AMOUNT INT,
    PROFIT INT,
    QUANTITY INT,
    CATEGORY VARCHAR(30),
    SUBCATEGORY VARCHAR(30));
 
 // Demonstrating error message
 COPY INTO ADAM_DB.PUBLIC.ORDERS_EX
    FROM @MANAGE_DB.external_stages.aws_stage_errorex
    file_format= (type = csv field_delimiter=',' skip_header=1)
    files = ('OrderDetails_error.csv');
    

 // Validating table is empty    
SELECT * FROM ADAM_DB.PUBLIC.ORDERS_EX    
    

  // Error handling using the ON_ERROR option
COPY INTO ADAM_DB.PUBLIC.ORDERS_EX
    FROM @MANAGE_DB.external_stages.aws_stage_errorex
    file_format= (type = csv field_delimiter=',' skip_header=1)
    files = ('OrderDetails_error.csv')
    ON_ERROR = 'CONTINUE';
    
  // Validating results and truncating table 
SELECT * FROM ADAM_DB.PUBLIC.ORDERS_EX
SELECT COUNT(*) FROM ADAM_DB.PUBLIC.ORDERS_EX

TRUNCATE TABLE ADAM_DB.PUBLIC.ORDERS_EX;

// Error handling using the ON_ERROR option = ABORT_STATEMENT (default)
COPY INTO ADAM_DB.PUBLIC.ORDERS_EX
    FROM @MANAGE_DB.external_stages.aws_stage_errorex
    file_format= (type = csv field_delimiter=',' skip_header=1)
    files = ('OrderDetails_error.csv','OrderDetails_error2.csv')
    ON_ERROR = 'ABORT_STATEMENT';


  // Validating results and truncating table 
SELECT * FROM ADAM_DB.PUBLIC.ORDERS_EX
SELECT COUNT(*) FROM ADAM_DB.PUBLIC.ORDERS_EX

TRUNCATE TABLE ADAM_DB.PUBLIC.ORDERS_EX;

// Error handling using the ON_ERROR option = SKIP_FILE
COPY INTO ADAM_DB.PUBLIC.ORDERS_EX
    FROM @MANAGE_DB.external_stages.aws_stage_errorex
    file_format= (type = csv field_delimiter=',' skip_header=1)
    files = ('OrderDetails_error.csv','OrderDetails_error2.csv')
    ON_ERROR = 'SKIP_FILE';
    
    
  // Validating results and truncating table 
SELECT * FROM ADAM_DB.PUBLIC.ORDERS_EX
SELECT COUNT(*) FROM ADAM_DB.PUBLIC.ORDERS_EX

TRUNCATE TABLE ADAM_DB.PUBLIC.ORDERS_EX;    
    

// Error handling using the ON_ERROR option = SKIP_FILE_<number>
COPY INTO ADAM_DB.PUBLIC.ORDERS_EX
    FROM @MANAGE_DB.external_stages.aws_stage_errorex
    file_format= (type = csv field_delimiter=',' skip_header=1)
    files = ('OrderDetails_error.csv','OrderDetails_error2.csv')
    ON_ERROR = 'SKIP_FILE_3';    
    


TRUNCATE TABLE ADAM_DB.PUBLIC.ORDERS_EX;    

    
// Error handling using the ON_ERROR option = SKIP_FILE_<number>
COPY INTO ADAM_DB.PUBLIC.ORDERS_EX
    FROM @MANAGE_DB.external_stages.aws_stage_errorex
    file_format= (type = csv field_delimiter=',' skip_header=1)
    files = ('OrderDetails_error.csv','OrderDetails_error2.csv')
    ON_ERROR = 'SKIP_FILE_0.5%'; 
  
  
SELECT * FROM ADAM_DB.PUBLIC.ORDERS_EX


 CREATE OR REPLACE TABLE ADAM_DB.PUBLIC.ORDERS_EX (
    ORDER_ID VARCHAR(30),
    AMOUNT INT,
    PROFIT INT,
    QUANTITY INT,
    CATEGORY VARCHAR(30),
    SUBCATEGORY VARCHAR(30));





COPY INTO ADAM_DB.PUBLIC.ORDERS_EX
    FROM @MANAGE_DB.external_stages.aws_stage_errorex
    file_format= (type = csv field_delimiter=',' skip_header=1)
    files = ('OrderDetails_error.csv','OrderDetails_error2.csv')
    ON_ERROR = SKIP_FILE_3 
    SIZE_LIMIT = 30;
