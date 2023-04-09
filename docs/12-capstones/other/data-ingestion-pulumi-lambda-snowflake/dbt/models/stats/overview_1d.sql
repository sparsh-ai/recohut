{{
    select_stats_overview(
        alias='overview_1d',
        date_agg='DATE_TRUNC(''DAY'', request_timestamp)',
        cluster_by=None
    )
}}
