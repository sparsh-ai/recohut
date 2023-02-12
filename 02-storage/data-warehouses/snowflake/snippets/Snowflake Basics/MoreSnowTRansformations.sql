//Example 3 - Table

CREATE OR REPLACE TABLE ADAM_DB.PUBLIC.ORDERS_EX (
    ORDER_ID VARCHAR(30),
    AMOUNT INT,
    PROFIT INT,
    PROFITABLE_FLAG VARCHAR(30)
  
    )

// Useful to Create an ID COlumn AutoIncremented 

//Example 4 - Using subset of columns  Keep other columns NULL 

COPY INTO ADAM_DB.PUBLIC.ORDERS_EX (ORDER_ID,PROFIT)
    FROM (select 
            s.$1,
            s.$3
          from @MANAGE_DB.external_stages.aws_stage s)
    file_format= (type = csv field_delimiter=',' skip_header=1)
    files=('OrderDetails.csv');

SELECT * FROM ADAM_DB.PUBLIC.ORDERS_EX;



//Example 5 - Table Auto increment

CREATE OR REPLACE TABLE ADAM_DB.PUBLIC.ORDERS_EX (
    ORDER_ID number autoincrement start 1 increment 1,
    AMOUNT INT,
    PROFIT INT,
    PROFITABLE_FLAG VARCHAR(30)
  
    )



//Example 5 - Auto increment ID

COPY INTO ADAM_DB.PUBLIC.ORDERS_EX (PROFIT,AMOUNT)
    FROM (select 
            s.$2,
            s.$3
          from @MANAGE_DB.external_stages.aws_stage s)
    file_format= (type = csv field_delimiter=',' skip_header=1)
    files=('OrderDetails.csv');


SELECT * FROM ADAM_DB.PUBLIC.ORDERS_EX WHERE ORDER_ID > 15;


    
DROP TABLE ADAM_DB.PUBLIC.ORDERS_EX