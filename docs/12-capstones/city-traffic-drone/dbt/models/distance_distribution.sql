select 
    traveled_d,
    count(*) 
from 
    {{ source('source', 'endpoints_trafficinfo') }}
group by 
    traveled_d