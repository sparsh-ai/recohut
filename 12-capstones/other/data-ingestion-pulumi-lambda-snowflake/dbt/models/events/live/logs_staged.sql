{% set threshold = get_events_threshold(ref('logs')) -%}


{{-
    select_logs(
        from_date=threshold,
        to_date=False,
        materialized='view',
        alias='logs_staged'
    )
}}
