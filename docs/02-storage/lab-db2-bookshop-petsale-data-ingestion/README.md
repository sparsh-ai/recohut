# db2

> db2 BookShop and PetSale Data Ingestion and Stored Procedure

## BookShop

### Insert data in IBM db2

![](https://user-images.githubusercontent.com/62965911/214214836-e0bdf10d-0c22-4d84-9016-5d830a532954.png)

## PetSale

### Insert PetSale data into IBM db2

Same as above, but use `./PETSALE-CREATE-v2.sql` script.

### Create Stored Procedure

-   You will create a stored procedure routine named RETRIEVE_ALL.
-   This RETRIEVE_ALL routine will contain an SQL query to retrieve all the records from the PETSALE table, so you don't need to write the same query over and over again. You just call the stored procedure routine to execute the query everytime.
-   To create the stored procedure routine, copy the code below and paste it to the textbox of the Run SQL page. Click Run all.

```sql
--#SET TERMINATOR @
CREATE PROCEDURE RETRIEVE_ALL       -- Name of this stored procedure routine

LANGUAGE SQL                        -- Language used in this routine 
READS SQL DATA                      -- This routine will only read data from the table

DYNAMIC RESULT SETS 1               -- Maximum possible number of result-sets to be returned to the caller query

BEGIN 

    DECLARE C1 CURSOR               -- CURSOR C1 will handle the result-set by retrieving records row by row from the table
    WITH RETURN FOR                 -- This routine will return retrieved records as a result-set to the caller query
    
    SELECT * FROM PETSALE;          -- Query to retrieve all the records from the table
    
    OPEN C1;                        -- Keeping the CURSOR C1 open so that result-set can be returned to the caller query

END
@                                   -- Routine termination character
```

To call the RETRIEVE_ALL routine, copy the code below in a new blank script and paste it to the textbox of the Run SQL page. Click Run all. You will have all the records retrieved from the PETSALE table.

```sql
CALL RETRIEVE_ALL;      -- Caller query
```

If you wish to drop the stored procedure routine RETRIEVE_ALL, copy the code below and paste it to the textbox of the Run SQL page. Click Run all.

```sql
DROP PROCEDURE RETRIEVE_ALL;

CALL RETRIEVE_ALL;
```