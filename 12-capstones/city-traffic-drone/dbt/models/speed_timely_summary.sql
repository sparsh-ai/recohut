{{ config(materialzied='view')}}

with top_speed as (select * from {{ref('timely_summary')}})

SELECT 
*
from top_speed
ORDER BY "speed" ASC
LIMIT(100)