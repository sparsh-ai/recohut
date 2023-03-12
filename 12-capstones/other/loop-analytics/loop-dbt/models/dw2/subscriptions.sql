/* columns
Subscription id
Subscription Item Id
Order line Id
Item
Item Type
Customer
Order date
Delivery date
BIN delivered --difference between this and bin collected I am not sure about
Renewal Date
Cancelled date
Pick up date
BIN Collected
End Date
current_period_start
current_period_end
status
Subscription amount
Subsription Qty
Discount code
Discount $
Collection amount (pre Credit)
*/

with shipments_parse_item as (
    select id,  
        split_part(items,'},',point) as parsed_item 
    from {{source('bigcommerce', 'shipments')}} cross join
        {{ref('points')}}
    where split_part(items,'},',point) is not null and 
        split_part(items,'},',point) != ''
),

shipments as (
    select s.id,
        s.order_id,
        s.customer_id as bigcommerce_customer_id,
        s.date_created,
        json_extract_path_text(s.comments, 'subscriptionId') as subscription_id,
        json_extract_path_text(s.comments, 'subscriptionAction') as subscription_action,
        trim(replace(split_part(split_part(i.parsed_item, ',', 1), ':', 2), '\'', '')::text) as line_item_id,
        trim(replace(split_part(split_part(i.parsed_item, ',', 2), ':', 2), '\'', '')::text) as bigcommerce_product_id,
        left(replace(split_part(split_part(i.parsed_item, ',', 3), ':', 2), '\'', ''),1)::text as quantity,
        replace(split_part(split_part(i.parsed_item, ',', 1), ':', 2), '\'', '')::text as x --not used column just used to make syntax readable below
    from {{source('bigcommerce', 'shipments')}} s left join
        shipments_parse_item i on s.id = i.id
),

quant_group as (
    SELECT
        id
        , row_number() over(partition by id) as row_repeat
    from {{source('stripe_fivetran', 'subscription_item')}} si
    join (select row_number() over() as quantity from {{ref('points')}}) rpt
    on si.quantity>=rpt.quantity
), 

flattened_quants as (
SELECT
    CASE WHEN row_repeat > 1 THEN si.id || '_' || row_repeat::text ELSE si.id END as subscription_item_id
    , *
from {{source('stripe_fivetran', 'subscription_item')}} si
LEFT JOIN quant_group
    on si.id = quant_group.id and row_repeat < 9
),

base as (
    select si.subscription_id,
        si.subscription_item_id,
        cim.loop_customer_id,
        si.created as item_created_at,
        li.id as line_item_id,
        p.product_name,
        case when p.product_name ilike '%member%' or p.product_name ilike '%plan' then 'Membership' else 'Item' end as item_type,
        o.date_created as order_date,
        l.delivery_date,
        l.bin,
        sh.current_period_end as renewal_date,
        sh.current_period_start as current_period_start,
        sh.canceled_at,
        l.pick_up_date,
        sh.status,
        price.unit_amount::float/100.00 as subscription_item_price
    from flattened_quants si left join 
        {{source('stripe_fivetran', 'subscription_history')}} sh on si.subscription_id = sh.id and sh."_fivetran_active" = true left join
        {{source('stripe_fivetran', 'price')}} price on si.plan_id = price.id left join
        {{ref('products')}} p on price.product_id = p.stripe_product_id left join
        shipments s on p.bigcommerce_product_id = s.bigcommerce_product_id and sh.id = s.subscription_id left join
        {{source('bigcommerce', 'orders')}} o on s.order_id = o.id left join
        {{source('bigcommerce', 'line_items')}} li on s.line_item_id = li.id left join
        {{ref('customer_id_map')}} cim on sh.customer_id = cim.stripe_customer_id left join
        {{ref('loops')}} l on CASE WHEN si.row_repeat > 1 THEN (50000 + ((row_repeat-2)*10000) + li.id::int)::text ELSE li.id::text end = l.line_item_id
),

subscription_totals as (
    select subscription_id,
        sum(subscription_item_price) as total_subscription_price,
        count(subscription_item_id) as number_items_in_subscription
    from base
    where pick_up_date is null or pick_up_date >= sysdate
    group by subscription_id
)
    
select b.*,
    st.total_subscription_price,
    cou.id as discount_code,
    cou.name as discount_name,
    case when sd.id is null then null
        when cou.amount_off is not null then cou.amount_off::float/(100.00*st.number_items_in_subscription::float) 
        else cou.percent_off::float * b.subscription_item_price/100.00 end as discount_amount_item,
    case when sd.id is null then 'No Discount' 
        when cou.amount_off is null then 'Percent Off' 
        else 'Fixed' end as discount_type,
    coalesce(cou.amount_off, cou.percent_off) as discount_amount_or_percent_total
from base b left join
    subscription_totals st on b.subscription_id = st.subscription_id left join
    {{source('stripe_fivetran', 'subscription_discount')}} sd on b.subscription_id = sd.subscription_id left join
    {{source('stripe_fivetran', 'coupon')}} cou on sd.coupon_id = cou.id