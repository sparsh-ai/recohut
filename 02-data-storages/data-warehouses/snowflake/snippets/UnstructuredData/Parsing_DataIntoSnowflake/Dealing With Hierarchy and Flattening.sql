


SELECT 
    RAW_FILE:spoken_languages as spoken_languages
FROM ADAM_DB.PUBLIC.JSON_RAW;

SELECT * FROM ADAM_DB.PUBLIC.JSON_RAW;


SELECT 
     array_size(RAW_FILE:spoken_languages) as spoken_languages
FROM ADAM_DB.PUBLIC.JSON_RAW


SELECT 
     RAW_FILE:first_name::STRING as first_name,
     array_size(RAW_FILE:spoken_languages) as spoken_languages // Useful to count Lanuages by Name
FROM ADAM_DB.PUBLIC.JSON_RAW



SELECT 
    RAW_FILE:spoken_languages[0] as First_language
FROM ADAM_DB.PUBLIC.JSON_RAW;


SELECT 
    RAW_FILE:first_name::STRING as first_name,
    RAW_FILE:spoken_languages[0] as First_language
FROM ADAM_DB.PUBLIC.JSON_RAW;


SELECT 
    RAW_FILE:first_name::STRING as First_name,
    RAW_FILE:spoken_languages[0].language::STRING as First_language,
    RAW_FILE:spoken_languages[0].level::STRING as Level_spoken
FROM ADAM_DB.PUBLIC.JSON_RAW




SELECT 
    RAW_FILE:id::int as id,
    RAW_FILE:first_name::STRING as First_name,
    RAW_FILE:spoken_languages[0].language::STRING as First_language,
    RAW_FILE:spoken_languages[0].level::STRING as Level_spoken
FROM ADAM_DB.PUBLIC.JSON_RAW
UNION ALL 
SELECT 
    RAW_FILE:id::int as id,
    RAW_FILE:first_name::STRING as First_name,
    RAW_FILE:spoken_languages[1].language::STRING as First_language,
    RAW_FILE:spoken_languages[1].level::STRING as Level_spoken
FROM ADAM_DB.PUBLIC.JSON_RAW
UNION ALL 
SELECT 
    RAW_FILE:id::int as id,
    RAW_FILE:first_name::STRING as First_name,
    RAW_FILE:spoken_languages[2].language::STRING as First_language,
    RAW_FILE:spoken_languages[2].level::STRING as Level_spoken
FROM ADAM_DB.PUBLIC.JSON_RAW
ORDER BY ID

// Useful//
// Flatten Table Function//

select
      RAW_FILE:first_name::STRING as First_name,
    f.value:language::STRING as First_language,
   f.value:level::STRING as Level_spoken
from ADAM_DB.PUBLIC.JSON_RAW, table(flatten(RAW_FILE:spoken_languages)) f;





// Option 1: CREATE TABLE AS

CREATE OR REPLACE TABLE Languages AS
select
      RAW_FILE:first_name::STRING as First_name,
    f.value:language::STRING as First_language,
   f.value:level::STRING as Level_spoken
from ADAM_DB.PUBLIC.JSON_RAW, table(flatten(RAW_FILE:spoken_languages)) f;

SELECT * FROM Languages;

truncate table languages;

// Option 2: INSERT INTO

INSERT INTO Languages
select
      RAW_FILE:first_name::STRING as First_name,
    f.value:language::STRING as First_language,
   f.value:level::STRING as Level_spoken
from ADAM_DB.PUBLIC.JSON_RAW, table(flatten(RAW_FILE:spoken_languages)) f;


SELECT * FROM Languages;