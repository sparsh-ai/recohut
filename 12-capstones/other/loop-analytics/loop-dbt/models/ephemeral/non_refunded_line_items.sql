select fli.* 
from {{ref('fact_line_item')}} fli left join
    {{ref('fact_order')}} fo on fli.order_id = fo.order_id left join
    {{ref('fact_refund_line_item')}} frli on frli.line_item_id = fli.line_item_id 
where 
    fo.order_id not in (
        select order_id 
        from {{ref('fact_refund')}}
        where refund_amount is not null
    ) and 
    (frli.line_item_id is null or frli.quantity < fli.quantity)
