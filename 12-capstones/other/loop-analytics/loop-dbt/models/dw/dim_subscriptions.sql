select
    fl.member_id
    , fl.sku
    , fo.subscription_id
    , fl.avg_price AS gross_price
    , fl.avg_price as net_price
    , 1 AS quantity
    , fl.delivery_date as start_dt
    , fl.pick_up_date as end_dt
    , NULL as status
from {{ ref('fact_loop') }} fl 
    left join {{ ref('fact_line_item')}} fli on fl.line_item_id = fli.line_item_id
    left join {{ ref('fact_order') }} fo on fli.order_id = fo.order_id