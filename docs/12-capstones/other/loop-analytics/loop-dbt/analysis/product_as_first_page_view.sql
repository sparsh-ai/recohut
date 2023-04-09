with tmp as (
    select distinct
        session_id
        , session_start_ts
        , session_channel_id
        , first_value(url) over (
            partition by session_id
            order by fwa.timestamp
            rows between unbounded preceding  and unbounded following
        ) as first_url
    from dw.fact_web_activity as fwa
    where src_tbl = 'pages'
)
, tmp2 as (
    select
        date_trunc('week', session_start_ts)::date as week
        , case
            when first_url ilike '%products/%'
            then 1
            else 0
          end as is_product
        , session_channel_id
        , session_id
    from tmp
)
select
    week
    , avg(is_product::float) as direct_to_product_pct
from tmp2
group by 1
order by 1 desc;
