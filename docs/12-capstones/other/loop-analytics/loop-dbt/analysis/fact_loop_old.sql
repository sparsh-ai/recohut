with first_user_sku_price as (
select
	row_number() OVER(partition by member_id, sku order by order_ts) as rk
	, * 
from {{ref('fact_order_shopify')}} fo 
left join {{ref('fact_line_item_shopify')}} fli 
	using(order_id)
), loop_master as (
    select
        bin
        , hubspot_customer_id
        , shopify_order_id
        , item_id
        , delivery_date
        , pick_up_date
        , restocking_clean_repair_time
        , 'SF' as ops_location
    FROM {{ source('googlesheets', 'loop_master') }}

    UNION ALL 
    
    select
        bin
        , hubspot_customer_id
        , shopify_order_id
        , item_id
        , delivery_date
        , pick_up_date
        , restocking_clean_repair_time
        , 'NYC' as ops_location
    FROM {{ source('googlesheets', 'nyc_loop_master') }}    
)
select
    mim.member_id
    , bin
    , item_id AS sku
    , orders.id as order_id
    , NULLIF(delivery_date, '')::DATE as delivery_date
    , NULLIF(pick_up_date, '')::DATE AS pick_up_date
    , restocking_clean_repair_time
    , COALESCE(fsu.price, sku_avg_price.avg_price) AS avg_price
    , loop_master.ops_location
from loop_master
left join {{ ref('member_id_map_shopify') }} AS mim
    on loop_master.hubspot_customer_id = mim.src_id
    and mim.src = 'hubspot'
left join {{ source('shopify', 'orders') }}
    on loop_master.shopify_order_id::text = orders.order_number::text
left join {{ ref('sku_avg_price') }} AS sku_avg_price
    on loop_master.item_id = sku_avg_price.sku
left join first_user_sku_price fsu
	on fsu.member_id = mim.member_id and fsu.sku = sku_avg_price.sku and fsu.rk=1
