select 
    line_item_id
    , order_id
    , is_gift_card::int::bool
    , price
    , quantity
    , bigcommerce_product_id
    , sku
    , product_name
    , variant_id::text
	, total_discount
    , vendor
    , src
    , true as replatform
from {{ ref('fact_line_item_rp') }}

union 

select 
    li.line_item_id::text
    , li.order_id::text
    , li.is_gift_card
    , li.price
    , li.quantity
    , null as bigcommerce_product_id
    , li.sku
    , p.title as product_name
    , li.variant_id::text
	, li.total_discount
    , li.vendor
    , 'shopify' as src
    , false as replatform
from {{ref('fact_line_item_shopify')}} li left join
    shopify.products p on li.sku = p.id 
