with terms AS (
    select
        id
        , monthly_membership_end_date
        , monthly_membership_start_date
    from hubspot.contacts
    where monthly_membership_end_date is not null
)
, first_touch_channels AS (
    select
        member_id
        , channel_id
    from dw_aggs.member_attribution_agg
    where first_touch_weighting = 1
)
, products as (
    select
        fact_order.member_id
    --     , sum(price) as ordered_mrr
    --     , count(distinct sku) as ordered_product_count
        , listagg(dim_product.product_name, ',') as products
    from dw.fact_line_item
    inner join dw.dim_product
        using(sku)
    inner join dw.fact_order
        using(order_id)
    where product_name not ilike '%membership%'
        and product_name not ilike '%plan%'
        and order_type != 'subscription_contract'
    group by 1
)
, stats as (
    select
        fact_order.member_id
        , sum(price) as ordered_mrr
        , count(distinct sku) as ordered_product_count
        -- , listagg(dim_product.product_name, ',') as products
    from dw.fact_line_item
    inner join dw.dim_product
        using(sku)
    inner join dw.fact_order
        using(order_id)
    where product_name not ilike '%membership%'
        and product_name not ilike '%plan%'
        and order_type != 'subscription_contract'
    group by 1
)
select
    dm.member_id
    , dm.first_name
    , substring(dm.last_name, 1, 1) as last_initial
    , ftc.channel_id as first_touch_channel
    , dm.membership_start_dt
    , dm.first_delivery_dt
    , dm.last_pick_up_dt
    , terms.monthly_membership_end_date AS membership_end_dt
    , dm.city
    , dm.child_1_dob
    , dm.child_2_dob
    , dm.child_3_dob
    , stats.ordered_mrr
    , stats.ordered_product_count
    , products.products
from terms
inner join dw.dim_members as dm
    on terms.id = dm.hubspot_customer_id
left join first_touch_channels as ftc
    on dm.member_id = ftc.member_id
left join products
    on dm.member_id = products.member_id
left join stats
    on dm.member_id = stats.member_id
order by membership_start_dt
