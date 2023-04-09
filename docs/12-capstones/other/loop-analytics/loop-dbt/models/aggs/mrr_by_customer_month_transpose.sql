-- UGGGGHHH... I'm so, so sorry
{% set months = ['2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01'] %}

{% set month_name_map = {
    '2021-03-01': 'mar',
    '2021-04-01': 'apr',
    '2021-05-01': 'may',
    '2021-06-01': 'jun',
    '2021-07-01': 'jul',
    '2021-08-01': 'aug',
    '2021-09-01': 'sep'
} %}

with base as (
    -- could just this but... formatting needs
    select
        dm.member_id
        , dm.first_name
        , dm.last_name
        , dm.membership_type
        , month
        , case when dm.membership_type = 'annual' then 149.0/12 when dm.membership_type = 'monthly' then 18.0 else 0 end as membership_mrr
        , sum(case when avg_price is not null then 1 else 0 end) AS item_count
        , AVG(avg_price) AS avg_item_price
        , SUM(NVL(avg_price, 0)) AS item_mrr
        , item_mrr + membership_mrr as total_mrr
    from {{ ref('fact_loop') }} fl
    inner join {{ ref('dim_members') }} dm
    using(member_id)
    cross join (
        select
            date as month
            , lead(date) over(order by date) as next_month
        from {{ ref('dates') }}
        where extract(day from date) = 1
            and date >= '2021-01-01'
            and date < CURRENT_DATE
    ) as months
    where LEAST(next_month, CURRENT_DATE) > fl.delivery_date
        AND LEAST(next_month, CURRENT_DATE) < NVL(fl.pick_up_date, '9999-12-31')
    group by 1, 2, 3, 4, 5, 6
    order by dm.member_id, month
)
, expansions as (
    select *
        , AVG(total_mrr) OVER(PARTITION BY member_id) AS member_monthly_avg_mrr
        , AVG(item_mrr) OVER(PARTITION BY member_id) AS member_monthly_avg_item_mrr
        , SUM(total_mrr) OVER(PARTITION BY member_id) AS member_monthly_sum_mrr
        , SUM(item_mrr) OVER(PARTITION BY member_id) AS member_monthly_sum_item_mrr
    from base
)
select
    member_id
    , first_name
    , last_name
    , membership_type
    , member_monthly_avg_mrr
    , member_monthly_avg_item_mrr
    , member_monthly_sum_mrr
    , member_monthly_sum_item_mrr
    , membership_mrr

    {% for month in months %}
    , SUM(case when month = '{{ month }}' then item_count end) AS items_{{ month_name_map[month] }}
    , SUM(case when month = '{{ month }}' then item_mrr end) AS item_mrr_{{ month_name_map[month] }}
    , item_mrr_{{ month_name_map[month] }} / nullif(items_{{ month_name_map[month] }}, 0)::float AS avg_item_mrr_{{ month_name_map[month] }}
    , SUM(case when month = '{{ month }}' then total_mrr end) AS total_mrr_{{ month_name_map[month] }}
    {% endfor %}
from expansions
group by 1,2,3,4,5,6,7,8,9