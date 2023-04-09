select 
    locationid,
    borough,
    zone,
    service_zone
from {{ source('source', 'taxi_zone_lookup') }}
