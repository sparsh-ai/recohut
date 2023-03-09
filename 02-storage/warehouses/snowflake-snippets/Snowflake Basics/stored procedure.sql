// Create a stored procedure
USE ADAM_DB;

SELECT * FROM CUSTOMERS


## Use of Java for Sproc ##


CREATE OR REPLACE PROCEDURE CUSTOMERS_INSERT_PROCEDURE (CREATE_DATE varchar)
    RETURNS STRING NOT NULL
    LANGUAGE JAVASCRIPT
    AS
        $$
        var sql_command = 'INSERT INTO CUSTOMERS(CREATE_DATE) VALUES(:1);'
        snowflake.execute(
            {
            sqlText: sql_command,
            binds: [CREATE_DATE]
            });
        return "Successfully executed.";
        $$;
        
        
    
CREATE OR REPLACE TASK CUSTOMER_TAKS_PROCEDURE
WAREHOUSE = COMPUTE_WH
SCHEDULE = '1 MINUTE'
AS CALL  CUSTOMERS_INSERT_PROCEDURE (CURRENT_TIMESTAMP);


SHOW TASKS;

ALTER TASK CUSTOMER_TAKS_PROCEDURE RESUME;


SELECT * FROM CUSTOMERS;