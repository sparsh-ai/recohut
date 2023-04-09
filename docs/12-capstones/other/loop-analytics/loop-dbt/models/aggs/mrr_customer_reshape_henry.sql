-- UGGGGHHH... I'm even more sorry than last time. See LOOP-36 for why this is happening. Hacking a UI format that doesn't exist in any BI tool I know of.
{% set months = ['mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep'] %}

with base as (
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
        , '1. ITEM MRR' AS monthly_metric_type
        {% for month in months %}
        , item_mrr_{{ month }} as {{ month }}
        {% endfor %}
    from {{ ref('mrr_by_customer_month_transpose') }}

    UNION ALL

    select
        member_id
        , '' as first_name
        , '' as last_name
        , '' as membership_type
        , null as member_monthly_avg_mrr
        , null as member_monthly_avg_item_mrr
        , null as member_monthly_sum_mrr
        , null as member_monthly_sum_item_mrr
        , null as membership_mrr
        , '2. ITEM QTY' AS monthly_metric_type
        {% for month in months %}
        , items_{{ month }} as {{ month }}
        {% endfor %}
    from {{ ref('mrr_by_customer_month_transpose') }}

    UNION ALL

    select
        member_id
        , '' as first_name
        , '' as last_name
        , '' as membership_type
        , null as member_monthly_avg_mrr
        , null as member_monthly_avg_item_mrr
        , null as member_monthly_sum_mrr
        , null as member_monthly_sum_item_mrr
        , null as membership_mrr
        , '3. MRR/ITEM' AS monthly_metric_type
        {% for month in months %}
        , avg_item_mrr_{{ month }} as {{ month }}
        {% endfor %}
    from {{ ref('mrr_by_customer_month_transpose') }}
)
, customer_rank AS (
    select member_id, row_number() over(order by member_monthly_sum_item_mrr desc) as cust_rank
    from {{ ref('mrr_by_customer_month_transpose') }}
)
select *
    , row_number() over(order by cust_rank, monthly_metric_type) as row_order
from base
left join customer_rank using(member_id)

