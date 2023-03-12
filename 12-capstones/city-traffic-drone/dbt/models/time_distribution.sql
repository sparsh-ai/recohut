select 
    time,
    count(*) 
from 
    {{ source('source', 'endpoints_trafficinfo') }}
group by 
    time