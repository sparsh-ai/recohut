select
    order_id
    , discount_code
    , discount_amount
    , discount_type
from {{ref('fact_order_shopify')}}
where discount_code is not null
