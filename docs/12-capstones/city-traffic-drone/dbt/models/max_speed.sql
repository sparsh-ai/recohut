select 
    type,
    max(speed) 
from 
    {{ source('source', 'endpoints_trafficinfo') }}
group by 
    type