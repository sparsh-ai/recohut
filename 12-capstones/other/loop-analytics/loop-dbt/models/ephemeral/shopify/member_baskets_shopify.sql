WITH ranked_loops_shopify as (
    select
        member_id
        , fo.order_ts
        , (price * quantity) as price
        , total_discount as total_discount
        , product_name
        , sku
        , dense_rank() over(partition by member_id order by order_ts) as dense_rank
    from {{ ref('fact_order_shopify') }} as fo
    left join {{ ref('fact_line_item_shopify') }} fli using(order_id)
    left join {{ ref('dim_product_shopify') }} as dp using(sku)
    where fo.order_type not in ('subscription_contract')
)
select
    member_id
    , order_ts
    , dense_rank
    , count(*) as initial_basket_ct
    , sum(CASE WHEN product_name not ilike '%plan' AND product_name not ilike '%membership' THEN price END) as initial_basekt_dollars
    , sum(CASE WHEN product_name ilike '%plan' OR product_name ilike '%membership' THEN price END) as initial_membership_dollars
    , case
        when initial_basekt_dollars < 50 then '< 50'
        when initial_basekt_dollars >= 50 and initial_basekt_dollars < 100 then '50 - 100'
        when initial_basekt_dollars >= 100 and initial_basekt_dollars < 150 then '100 - 150'
        when initial_basekt_dollars >= 150 and initial_basekt_dollars < 200 then '150 - 200'
        when initial_basekt_dollars >= 200 then '200+'
    end as basket_bin
    , max((sku = '6650335723691')::int) AS initial_basket_has_snoo
    , listagg(product_name, ', ') within group (order by product_name) as initial_basket_products
    , COALESCE(SUM(total_discount), 0) as total_discounts
    , sum(price) - SUM(total_discount) as net_basket_size
from ranked_loops_shopify
group by 1, 2, 3
