select 
    id,
    member_id,
    order_id,
    created_ts,
    refund_amount,
    transactions,
    refund_line_items,
    src_name,
    true as replatform
from {{ ref('fact_refund_rp') }}

union

select 
    r.refund_id::text,
    r.member_id,
    r.order_id::text,
    r.created_ts,
    abs(r.order_adjustments) as refund_amount,
    r.transactions,
    r.refund_line_items,
    'shopify' as src_name,
    false as replatform
from {{ ref('fact_refund_shopify') }} r 

