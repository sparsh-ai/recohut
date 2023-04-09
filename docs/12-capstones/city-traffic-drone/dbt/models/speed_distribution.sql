select 
    speed,
    count(*) 
from 
    {{ source('source', 'endpoints_trafficinfo') }}
group by 
    speed