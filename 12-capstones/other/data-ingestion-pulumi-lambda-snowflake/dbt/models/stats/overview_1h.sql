{{
    select_stats_overview(
        alias='overview_1h',
        date_agg='DATE_TRUNC(''HOUR'', request_timestamp)',
        cluster_by='TO_DATE(timestamp)'
    )
}}
