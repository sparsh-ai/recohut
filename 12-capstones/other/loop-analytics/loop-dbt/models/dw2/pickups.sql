with schedule_pickup as (
    select *,
       split_part(delivery_performance_picking_scheduled_delivery_related_order_line_ref2, '.', 1) as line_item_id
    from {{source('quickbase', 'schedule_pickup')}}
)
select cim.loop_customer_id,
    sp.delivery_performance_picking_scheduled_delivery_order_line_item_sku as sku,
    sp.line_item_id,
    nsli.orig_line_item_id,
    sp.delivery_performance_picking_asset_tag_association_asset_tag as bin,
    sp.date_created as date_pickup_requested,
    sp.scheduled_pickup_date,
    l.pick_up_date,
    s.subscription_id,
    s.subscription_item_id
from schedule_pickup sp left join
    {{ref('non_subscription_line_items')}} nsli on sp.line_item_id = nsli.id left join
    {{ref('loops')}} l on sp.line_item_id = l.line_item_id left join
    {{ref('subscriptions')}} s on nsli.orig_line_item_id = s.line_item_id left join
    {{ref('non_subscription_orders')}} nso on nsli.order_id = nso.id left join
    {{ref('customer_id_map')}} cim on nso.customer_id = cim.quickbase_customer_id


    
