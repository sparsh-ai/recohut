select
    member_id
    , order_ts::date as start_date
    , DATEADD('day', 90, start_date)::date as end_date
    , sum(-1 * order_discounts::float) as discount_mrr_offset
from {{ ref('fact_order_shopify') }}
where order_type = 'web'
    and order_discounts::float > 0
    and not is_membership_order
group by 1, 2, 3
order by 1, 2
