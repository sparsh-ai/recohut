select 
    type,
    max(traveled_d) 
from 
    {{ source('source', 'endpoints_trafficinfo') }}
group by 
    type