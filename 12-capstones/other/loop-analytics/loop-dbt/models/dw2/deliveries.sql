with schedule_delivery as (
    select *,
       split_part(related_order_line_ref, '.', 1) as line_item_id
    from {{source('quickbase', 'schedule_delivery')}}
)
select cim.loop_customer_id,
    sd.order_line_item_sku as sku,
    sd.line_item_id,
    nsli.orig_line_item_id,
    l.bin,
    sd.date_created as date_delivery_requested,
    sd.scheduled_delivery_date,
    l.delivery_date,
    s.subscription_id,
    s.subscription_item_id
from schedule_delivery sd left join
    {{ref('non_subscription_line_items')}} nsli on sd.line_item_id = nsli.id left join
    {{ref('loops')}} l on sd.line_item_id = l.line_item_id left join
    {{ref('subscriptions')}} s on nsli.orig_line_item_id = s.line_item_id left join
    {{ref('non_subscription_orders')}} nso on nsli.order_id = nso.id left join
    {{ref('customer_id_map')}} cim on nso.customer_id = cim.quickbase_customer_id