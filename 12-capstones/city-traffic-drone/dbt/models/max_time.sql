select 
    type,
    max(time) 
from 
    {{ source('source', 'endpoints_trafficinfo') }}
group by 
    type