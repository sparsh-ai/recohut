WITH ranked_loops as (
    select
        member_id
        , delivery_date
        , order_id
        , avg_price
        , sku
        , dense_rank() over(partition by member_id order by delivery_date) as dense_rank
    from {{ ref('fact_loop_shopify') }}
)
, member_first_dues as (
    select
        member_id
        , MIN(order_ts) as first_order_ts
        , SUM(price) as member_dues
    from {{ ref('fact_line_item_shopify') }} fli 
    left join {{ ref('fact_order_shopify') }} fo 
        using(order_id)
    left join {{ ref('dim_product_shopify') }} dp 
        using(sku)
    where product_name ilike '%annual%' or product_name ilike '%monthly%'
    group by 1
    having first_order_ts = MIN(order_ts)
)
select
    member_id
    , delivery_date
    , dense_rank
    , count(*) as initial_basket_ct
    , sum(avg_price) as initial_basekt_dollars
    , sum(member_first_dues.member_dues) as initial_membership_dollars
    , case
        when initial_basekt_dollars < 50 then '< 50'
        when initial_basekt_dollars >= 50 and initial_basekt_dollars < 100 then '50 - 100'
        when initial_basekt_dollars >= 100 and initial_basekt_dollars < 150 then '100 - 150'
        when initial_basekt_dollars >= 150 and initial_basekt_dollars < 200 then '150 - 200'
        when initial_basekt_dollars >= 200 then '200+'
    end as basket_bin
    , max((sku = '6650335723691')::int) AS initial_basket_has_snoo
    , listagg(product_name, ', ') within group (order by product_name) as initial_basket_products
    , SUM(fli.total_discount) as total_discounts
    , sum(avg_price) - SUM(fli.total_discount) as net_basket_size
from ranked_loops
left join {{ref('dim_product_shopify')}} dp 
	using(sku)
left join {{ref('fact_line_item_shopify')}} fli 
	using(order_id, sku)
left join member_first_dues
    using(member_id)
group by 1, 2, 3
