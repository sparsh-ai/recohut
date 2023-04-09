with base as (
select 
    refund_line_item_id
    , refund_id
    , order_id
    , line_item_id
    , -1 * quantity as quantity
    , total
    , reason
    , true as replatform
from {{ ref('fact_refund_line_items_rp') }}

union

select 
    rli.refund_line_item_id::text
    , rli.refund_id::text
    , rli.order_id::text
    , rli.line_item_id::text
    , -1 * rli.quantity as quantity
    , rli.price as total
    , null as reason
    , false as replatform
from {{ref('fact_refund_line_item_shopify')}} rli )

select b.*,
    fli.sku,
    fli.product_name
from base b left join 
    {{ref('fact_line_item')}} fli on b.line_item_id = fli.line_item_id