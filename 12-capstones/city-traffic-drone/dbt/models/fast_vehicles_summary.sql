{{ config(materialzied='view')}}

with fast_v as (select * from {{ref('fast_vehicles')}})

SELECT 
type as "Vehicle type",
count(type) as "vehicle count"
from fast_v 
GROUP BY type ORDER BY "vehicle count" ASC