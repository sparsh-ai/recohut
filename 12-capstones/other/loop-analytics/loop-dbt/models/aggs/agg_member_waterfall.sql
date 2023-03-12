with targets as (
    select
        date::date as date
        , 'SF' as location
        , {{ floatify('gross_new_bay') }} as target_new
        , {{ floatify('churn_bay') }} as target_churn
        , {{ floatify('net_new_bay') }} as target_net
        , {{ floatify('total_members_bay') }} as target_total
        , {{ floatify('active_bay') }} as target_active
        , {{ floatify('net_mrr_bay') }} as target_mrr
    from {{ source('googlesheets', 'loop_daily_targets') }}

    union all

    select
        date::date as date
        , 'NYC' as location
        , {{ floatify('gross_new_nyc') }} as target_new
        , {{ floatify('churn_nyc') }} as target_churn
        , {{ floatify('net_new_nyc') }} as target_net
        , {{ floatify('total_members_nyc') }} as target_total
        , {{ floatify('active_nyc') }} as targer_active
        , {{ floatify('net_mrr_nyc') }} as target_mrr
    from {{ source('googlesheets', 'loop_daily_targets') }}
)
, actual_new_cte as (
    select
        membership_start_dt::date as date
        , ops_location AS location
        , count(*) as actual_new
    from {{ ref('dim_members') }}
    group by 1, 2
)
, actual_churn_cte as (
    select
        membership_end_dt::date as date
        , ops_location AS location
        , -1 * count(*) as actual_churn
    from {{ ref('dim_members') }}
    group by 1, 2
)
, net_members_cte as (
    select 
        date
        , location
        , sum(members) as members
    from (
        select
            date
            , location
            , actual_new as members
        from actual_new_cte

        union all

        select
            date
            , location
            , actual_churn as members
        from actual_churn_cte
    ) as a
    group by 1, 2
)
, date_location_base as (
    select *
    from (
        select distinct location
        from net_members_cte
    ) as a
    cross join (
        select daydate as date
        from {{ ref('dim_date') }}
    ) as b
)
, actual_total_cte as (
    -- do this instead of window function so we get all-time actual data
    select
        date
        , location
        , sum(members) over(
            partition by location
            order by date
            rows between unbounded preceding and current row
        ) as actual_total
    from date_location_base
    left join net_members_cte
        using(date, location)
)
select
    targets.location
    , targets.date
    , NVL(actual_new, 0) as actual_new
    , NVL(actual_churn, 0) as actual_churn
    , NVL(actual_new, 0) + NVL(actual_churn, 0) as actual_net
    , target_new
    , target_churn
    , NVL(target_new, 0) + NVL(target_churn, 0) as target_net
    , actual_total
    , target_total
from targets
left join actual_new_cte
    using(date, location)
left join actual_churn_cte
    using(date, location)
left join actual_total_cte
    using(date, location)