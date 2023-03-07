select
    t.vendor_id,
    t.pickup_datetime
from {{ ref('stage_yellow_taxi_trips_model') }} t
