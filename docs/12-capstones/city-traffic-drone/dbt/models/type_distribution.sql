select 
    type,
    count(*) 
from 
    {{ source('source', 'endpoints_trafficinfo') }}
group by 
    type