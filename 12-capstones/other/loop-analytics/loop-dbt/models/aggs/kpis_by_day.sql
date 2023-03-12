-- maybe this should be on kpis by day
{% set membership_type_prefixes = ['', '_annual', '_monthly', '_per_item'] %}
{% set membership_status_prefixes = ['new', 'scheduled', 'active', 'inactive', 'lapsed'] %}

with new_member_stats as (
    select
        membership_start_dt::date as date
        , sum((membership_type in ('annual', 'monthly'))::int) as new_members  -- don't call per item members now
        , sum((membership_type = 'annual')::int) as new_annual_members
        , sum((membership_type = 'monthly')::int) as new_monthly_members
        , sum((membership_type = 'per-item')::int) as new_per_item_members
        , new_annual_members * (149.0 / 12.0) as new_annual_mrr
        , new_monthly_members * 18.0 as new_monthly_mrr
        , new_annual_mrr + new_monthly_mrr as new_membership_mrr
    from {{ ref('dim_members') }}
    where membership_start_dt is not null
    group by 1
)
, scheduled_member_stats AS (
    select
        first_item_order_dt::date as date
        , sum((membership_type in ('annual', 'monthly'))::int) as scheduled_members
        , sum((membership_type = 'annual')::int) as scheduled_annual_members
        , sum((membership_type = 'monthly')::int) as scheduled_monthly_members
        , sum((membership_type = 'per-item')::int) as scheduled_per_item_members
        , scheduled_annual_members * (149.0 / 12.0) as scheduled_annual_mrr
        , scheduled_monthly_members * 18.0 as scheduled_monthly_mrr
        , scheduled_annual_mrr + scheduled_monthly_mrr as scheduled_membership_mrr
    from {{ ref('dim_members') }}
    where member_status != 'lead'
        and membership_start_dt <= first_item_order_dt
    group by 1
)
, active_member_stats AS (
    select
        first_delivery_dt::date as date
        , sum((membership_type in ('annual', 'monthly'))::int) as active_members
        , sum((membership_type = 'annual')::int) as active_annual_members
        , sum((membership_type = 'monthly')::int) as active_monthly_members
        , sum((membership_type = 'per-item')::int) as active_per_item_members
        , active_annual_members * (149.0 / 12.0) as active_annual_mrr
        , active_monthly_members * 18.0 as active_monthly_mrr
        , active_annual_mrr + active_monthly_mrr as active_membership_mrr
    from {{ ref('dim_members') }}
    where member_status != 'lead'
        and first_item_order_dt <= first_delivery_dt
    group by 1
)
, inactive_member_stats AS (
    select
        last_pick_up_dt::date as date
        , sum((membership_type in ('annual', 'monthly'))::int)  as inactive_members
        , sum((membership_type = 'annual')::int) as inactive_annual_members
        , sum((membership_type = 'monthly')::int) as inactive_monthly_members
        , sum((membership_type = 'per-item')::int) as inactive_per_item_members
        , inactive_annual_members * (149.0 / 12.0) as inactive_annual_mrr
        , inactive_monthly_members * 18.0 as inactive_monthly_mrr
        , inactive_annual_mrr + inactive_monthly_mrr as inactive_membership_mrr
    from {{ ref('dim_members') }}
    where member_status != 'lead'
        and first_delivery_dt <= last_pick_up_dt
    group by 1
)
, lapsed_member_stats as (
    select
        membership_end_dt::date as date
        , sum((membership_type in ('annual', 'monthly'))::int) as lapsed_members
        , sum((membership_type = 'annual')::int) as lapsed_annual_members
        , sum((membership_type = 'monthly')::int) as lapsed_monthly_members
        , sum((membership_type = 'per-item')::int) as lapsed_per_item_members
        , lapsed_annual_members * (149.0 / 12.0) as lapsed_annual_mrr
        , lapsed_monthly_members * 18.0 as lapsed_monthly_mrr
        , lapsed_annual_mrr + lapsed_monthly_mrr as lapsed_membership_mrr

        -- special fields to hack lapsed customers out of histogram data
        , sum((membership_type in ('annual', 'monthly') and member_status = '1. new')::int) as lapsed_new_members
        , sum((membership_type = 'annual' and member_status = '1. new')::int) as lapsed_new_annual_members
        , sum((membership_type = 'monthly' and member_status = '1. new')::int) as lapsed_new_monthly_members
        , sum((membership_type = 'per-item' and member_status = '1. new')::int) as lapsed_new_per_item_members
        , sum((membership_type in ('annual', 'monthly') and member_status = '2. scheduled')::int) as lapsed_scheduled_members
        , sum((membership_type = 'annual' and member_status = '2. scheduled')::int) as lapsed_scheduled_annual_members
        , sum((membership_type = 'monthly' and member_status = '2. scheduled')::int) as lapsed_scheduled_monthly_members
        , sum((membership_type = 'per-item' and member_status = '2. scheduled')::int) as lapsed_scheduled_per_item_members
        , sum((membership_type in ('annual', 'monthly') and member_status = '3. active')::int) as lapsed_active_members
        , sum((membership_type = 'annual' and member_status = '3. active')::int) as lapsed_active_annual_members
        , sum((membership_type = 'monthly' and member_status = '3. active')::int) as lapsed_active_monthly_members
        , sum((membership_type = 'per-item' and member_status = '3. active')::int) as lapsed_active_per_item_members
        , sum((membership_type in ('annual', 'monthly') and member_status = '4. inactive')::int) as lapsed_inactive_members
        , sum((membership_type = 'annual' and member_status = '4 inactive')::int) as lapsed_inactive_annual_members
        , sum((membership_type = 'monthly' and member_status = '4. inactive')::int) as lapsed_inactive_monthly_members
        , sum((membership_type = 'per-item' and member_status = '4. inactive')::int) as lapsed_inactive_per_item_members

    from {{ ref('dim_members') }}
    where membership_end_dt is not null
    group by 1
)
, delivery_stats as (
    select
        delivery_date as date
        , sum((membership_type in ('annual', 'monthly'))::int)  as delivered_items
        , sum((membership_type = 'annual')::int) as delivered_annual_items
        , sum((membership_type = 'monthly')::int) as delivered_monthly_items
        , sum((membership_type = 'per-item')::int) as delivered_per_item_items

        , sum(avg_price) as delivered_mrr
        , sum(case when membership_type = 'annual' then avg_price end) as delivered_annual_mrr
        , sum(case when membership_type = 'monthly' then avg_price end) as delivered_monthly_mrr
        , sum(case when membership_type = 'per-item' then avg_price end) as delivered_per_item_mrr

    from {{ ref('fact_loop') }}
    left join {{ ref('dim_members') }}
        using(member_id)
    where delivery_date is not null
    group by 1
    order by 2 desc
)
, pickup_stats as (
    select
        pick_up_date as date
        , sum((membership_type in ('annual', 'monthly'))::int) as picked_up_items
        , sum((membership_type = 'annual')::int) as picked_up_annual_items
        , sum((membership_type = 'monthly')::int) as picked_up_monthly_items
        , sum((membership_type = 'per-item')::int) as picked_up_per_item_items

        , sum(avg_price) as picked_up_mrr
        , sum(case when membership_type = 'annual' then avg_price end) as picked_up_annual_mrr
        , sum(case when membership_type = 'monthly' then avg_price end) as picked_up_monthly_mrr
        , sum(case when membership_type = 'per-item' then avg_price end) as picked_up_per_item_mrr
    from {{ ref('fact_loop') }}
    left join {{ ref('dim_members') }}
        using(member_id)
    where pick_up_date is not null
    group by 1
    order by 2 desc
)
, hack_loop_share_mrr_start as (
    select
        start_date::date as date
        , SUM(discount_mrr_offset) AS start_discount_mrr_offset
        , SUM(CASE WHEN dm.membership_type = 'annual' then discount_mrr_offset END) AS start_discount_mrr_offset_annual
        , SUM(CASE WHEN dm.membership_type = 'monthly' then discount_mrr_offset END) AS start_discount_mrr_offset_monthly
        , SUM(CASE WHEN dm.membership_type = 'per-item' then discount_mrr_offset END) AS start_discount_mrr_offset_per_item
    from {{ ref('loopshare_discount_hack') }}
    left join {{ ref('dim_members') }} dm
        using(member_id)
    group by 1
)
, hack_loop_share_mrr_end as (
    select
        end_date::date as date
        , SUM(discount_mrr_offset) AS end_discount_mrr_offset
        , SUM(CASE WHEN dm.membership_type = 'annual' then discount_mrr_offset END) AS end_discount_mrr_offset_annual
        , SUM(CASE WHEN dm.membership_type = 'monthly' then discount_mrr_offset END) AS end_discount_mrr_offset_monthly
        , SUM(CASE WHEN dm.membership_type = 'per-item' then discount_mrr_offset END) AS end_discount_mrr_offset_per_item
    from {{ ref('loopshare_discount_hack') }}
    left join {{ ref('dim_members') }} dm
        using(member_id)
    group by 1
)
, all_stats_base as (
    select
        dates.date

        {% for mstatus in membership_status_prefixes %}

        , NVL({{ mstatus }}_member_stats.{{ mstatus }}_members, 0) AS {{ mstatus }}_members
        , NVL({{ mstatus }}_member_stats.{{ mstatus }}_annual_members, 0) AS {{ mstatus }}_annual_members
        , NVL({{ mstatus }}_member_stats.{{ mstatus }}_monthly_members, 0) AS {{ mstatus }}_monthly_members
        , NVL({{ mstatus }}_member_stats.{{ mstatus }}_per_item_members, 0) AS {{ mstatus }}_per_item_members
        , NVL({{ mstatus }}_member_stats.{{ mstatus }}_annual_mrr, 0) AS {{ mstatus }}_annual_mrr
        , NVL({{ mstatus }}_member_stats.{{ mstatus }}_monthly_mrr, 0) AS {{ mstatus }}_monthly_mrr
        , {{ mstatus }}_annual_mrr + {{ mstatus }}_monthly_mrr as {{ mstatus }}_membership_mrr

        {% endfor %}


        {% for mtype in membership_type_prefixes %}
        , NVL(delivery_stats.delivered{{ mtype }}_items, 0) AS delivered{{ mtype }}_items
        , NVL(delivery_stats.delivered{{ mtype }}_mrr, 0) AS delivered{{ mtype }}_mrr

        , NVL(pickup_stats.picked_up{{ mtype }}_items, 0) AS picked_up{{ mtype }}_items
        , NVL(pickup_stats.picked_up{{ mtype }}_mrr, 0) AS picked_up{{ mtype }}_mrr

        , NVL(hack_loop_share_mrr_start.start_discount_mrr_offset{{ mtype }}, 0) - NVL(hack_loop_share_mrr_end.end_discount_mrr_offset{{ mtype }}, 0) AS discount_mrr_offset{{ mtype }}
        {% endfor %}

        , lapsed_new_members
        , lapsed_new_annual_members
        , lapsed_new_monthly_members
        , lapsed_new_per_item_members
        , lapsed_scheduled_members
        , lapsed_scheduled_annual_members
        , lapsed_scheduled_monthly_members
        , lapsed_scheduled_per_item_members
        , lapsed_active_members
        , lapsed_active_annual_members
        , lapsed_active_monthly_members
        , lapsed_active_per_item_members
        , lapsed_inactive_members
        , lapsed_inactive_annual_members
        , lapsed_inactive_monthly_members
        , lapsed_inactive_per_item_members

    from {{ ref('dates') }} AS dates
    left join new_member_stats
        on dates.date = new_member_stats.date
    left join scheduled_member_stats
        on dates.date = scheduled_member_stats.date
    left join active_member_stats
        on dates.date = active_member_stats.date
    left join inactive_member_stats
        on dates.date = inactive_member_stats.date
    left join lapsed_member_stats
        on dates.date = lapsed_member_stats.date
    left join delivery_stats
        on dates.date = delivery_stats.date
    left join pickup_stats
        on dates.date = pickup_stats.date
    left join hack_loop_share_mrr_start
        on dates.date = hack_loop_share_mrr_start.date
    left join hack_loop_share_mrr_end
        on dates.date = hack_loop_share_mrr_end.date
    WHERE dates.date <= CURRENT_DATE
)
, all_but_lags AS (
    select *

        {% for mstatus in membership_status_prefixes %}
            {% for mtype in membership_type_prefixes %}
            , SUM({{ mstatus }}{{ mtype }}_members) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS {{ mstatus }}{{ mtype }}_members_cum
            {% if mstatus != 'lapsed' %}
            , SUM(lapsed_{{ mstatus }}{{ mtype }}_members) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS lapsed_{{ mstatus }}{{ mtype }}_members_cum
            {% endif %}
            {% endfor %}
        {% endfor %}

        {% for mtype in membership_type_prefixes %}
        , inactive{{ mtype }}_members_cum - NVL(lapsed_inactive{{ mtype }}_members_cum, 0) as current_inactive{{ mtype }}_members
        , active{{ mtype }}_members_cum - inactive{{ mtype }}_members_cum  - NVL(lapsed_active{{ mtype }}_members_cum, 0) as current_active{{ mtype }}_members
        , scheduled{{ mtype }}_members_cum - active{{ mtype }}_members_cum - NVL(lapsed_scheduled{{ mtype }}_members_cum, 0) as current_scheduled{{ mtype }}_members
        , new{{ mtype }}_members_cum - scheduled{{ mtype }}_members_cum - NVL(lapsed_new{{ mtype }}_members_cum, 0) as current_new{{ mtype }}_members
        , SUM(discount_mrr_offset{{ mtype }}) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS discount_mrr_offset{{ mtype }}_cum

        , SUM(delivered{{ mtype }}_items) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS delivered{{ mtype }}_items_cum
        , SUM(picked_up{{ mtype }}_items) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS picked_up{{ mtype }}_items_cum
        , delivered{{ mtype }}_items_cum - picked_up{{ mtype }}_items_cum as active{{ mtype }}_items

        , SUM(delivered{{ mtype }}_mrr) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS delivered{{ mtype }}_mrr_cum

        , SUM(picked_up{{ mtype }}_mrr) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS picked_up{{ mtype }}_mrr_cum
        , delivered{{ mtype }}_mrr_cum - picked_up{{ mtype }}_mrr_cum as active{{ mtype }}_rental_mrr
        , delivered{{ mtype }}_mrr_cum - picked_up{{ mtype }}_mrr_cum + discount_mrr_offset{{ mtype }}_cum as active{{ mtype }}_rental_mrr_net

        {% endfor %}

        -- TODO: What about churn members??
        , SUM(new_annual_mrr) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS new_annual_mrr_cum
        , SUM(new_monthly_mrr) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS new_monthly_mrr_cum
        , new_annual_mrr_cum + new_monthly_mrr_cum as membership_mrr

        , active_rental_mrr + membership_mrr as total_mrr
        , active_rental_mrr_net + membership_mrr as total_mrr_net
        , active_annual_rental_mrr + new_annual_mrr_cum as total_annual_mrr
        , active_annual_rental_mrr_net + new_annual_mrr_cum as total_annual_mrr_net
        , active_monthly_rental_mrr + new_monthly_mrr_cum as total_monthly_mrr
        , active_monthly_rental_mrr_net + new_monthly_mrr_cum as total_monthly_mrr_net
        , active_per_item_rental_mrr as total_per_item_mrr
        , active_per_item_rental_mrr_net as total_per_item_mrr_net

        , new_members_cum - NVL(lapsed_members_cum, 0) AS current_members
        , new_annual_members_cum - NVL(lapsed_annual_members_cum, 0) AS current_annual_members
        , new_monthly_members_cum - NVL(lapsed_monthly_members_cum, 0) AS current_monthly_members
        , new_per_item_members_cum - NVL(lapsed_per_item_members_cum, 0) AS current_per_item_members

    from all_stats_base
)
select *
    , (current_members / NULLIF(LAG(current_members, 7) OVER(ORDER BY date), 0)::float) - 1 AS current_member_7d_growth_pct
    , (current_annual_members / NULLIF(LAG(current_annual_members, 7) OVER(ORDER BY date), 0)::float) - 1 AS current_annual_member_7d_growth_pct
    , (current_monthly_members / NULLIF(LAG(current_monthly_members, 7) OVER(ORDER BY date), 0)::float) - 1 AS current_monthly_member_7d_growth_pct
    , (current_per_item_members / NULLIF(LAG(current_per_item_members, 7) OVER(ORDER BY date), 0)::float) - 1 AS current_per_item_member_7d_growth_pct

    , (current_members / NULLIF(LAG(current_members, 30) OVER(ORDER BY date), 0)::float) - 1 AS current_member_30d_growth_pct
    , (current_annual_members / NULLIF(LAG(current_annual_members, 30) OVER(ORDER BY date), 0)::float) - 1 AS current_annual_member_30d_growth_pct
    , (current_monthly_members / NULLIF(LAG(current_monthly_members, 30) OVER(ORDER BY date), 0)::float) - 1 AS current_monthly_member_30d_growth_pct
    , (current_per_item_members / NULLIF(LAG(current_per_item_members, 30) OVER(ORDER BY date), 0)::float) - 1 AS current_per_item_member_30d_growth_pct
from all_but_lags
