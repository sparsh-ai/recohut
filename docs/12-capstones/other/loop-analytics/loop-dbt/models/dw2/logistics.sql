/*
Event
Member ID
SKU 
BIN
Requested
Scheduled Date
Completed
Subscription id
Subscription Item Id
Order line Id
*/

select loop_customer_id,
    sku,
    line_item_id,
    orig_line_item_id,
    bin,
    date_delivery_requested as date_requested,
    scheduled_delivery_date as scheduled_date,
    delivery_date as event_date,
    subscription_id,
    subscription_item_id,
    'delivery' as event_type
from {{ref('deliveries')}}

union

select loop_customer_id,
    sku,
    line_item_id,
    orig_line_item_id,
    bin,
    date_pickup_requested as date_requested,
    scheduled_pickup_date as scheduled_date,
    pick_up_date as event_date,
    subscription_id,
    subscription_item_id,
    'pickup' as event_type
from {{ref('pickups')}}

