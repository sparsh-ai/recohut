select
    date::date as date
    , {{ floatify('gross_new_bay') }} AS gross_new_bay
    , {{ floatify('churn_bay') }} AS churn_bay
    , {{ floatify('net_new_bay') }} AS net_new_bay
    , {{ floatify('total_members_bay') }} AS total_members_bay
    , {{ floatify('active_bay') }} AS active_bay
    , {{ floatify('gross_new_nyc') }} AS gross_new_nyc
    , {{ floatify('churn_nyc') }} AS churn_nyc
    , {{ floatify('net_new_nyc') }} AS net_new_nyc
    , {{ floatify('total_members_nyc') }} AS total_members_nyc
    , {{ floatify('active_nyc') }} AS active_nyc
    , {{ floatify('net_mrr_bay') }} AS net_mrr_bay
    , {{ floatify('net_mrr_nyc') }} AS net_mrr_nyc
from {{ source('googlesheets', 'loop_daily_targets') }}
