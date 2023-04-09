-- most stripe transactions
select bt.id as transaction_id,
    case when bt.type = 'charge' and ch.invoice_id is null then 'order'
        when bt.type = 'charge' and ch.invoice_id is not null then 'subscription' 
        when bt.type = 'refund' then 'refund'
        end as transacation_type,
    case when bt.type = 'charge' and ch.invoice_id is null then 'order'
        when bt.type = 'charge' and ch.invoice_id is not null and i.status != 'draft' then 'subscription' 
        when bt.type = 'charge' and ch.invoice_id is not null and i.status != 'draft' then 'draft_subscription' 
        when bt.type = 'refund' and rch.invoice_id is null then 'order_refund'
        when bt.type = 'refund' and rch.invoice_id is not null then 'subscription_refund'
        end as transacation_sub_type,
    case when ch.invoice_id is null and ch.metadata is not null then 'bigcommerce' else 'stripe' end as orig_system,
    cim.loop_customer_id,
    case when bt.type = 'charge' and ch.invoice_id is null then json_extract_path_text(ch.metadata, 'bigCommerceOrderId')::text
        when bt.type = 'charge' and ch.invoice_id is not null then ch.invoice_id
        when bt.type = 'refund' and rch.invoice_id is null then json_extract_path_text(rch.metadata, 'bigCommerceOrderId')::text
        when bt.type = 'refund' and rch.invoice_id is not null then rch.invoice_id
        end as order_id,
    r.id as refund_id,
    bt.amount::float/100.00 as transaction_amount,
    coalesce(i.subtotal::float/100.00, bco.total_inc_tax) as order_total,
    case when bt.type = 'charge' and ch.invoice_id is null then bco.discount_amount + bco.coupon_discount
        when bt.type = 'charge' and ch.invoice_id is not null then (i.subtotal - i.total)::float/100.00 end as discount_amount,
    case when bt.type = 'charge' and ch.invoice_id is not null then -1.00*(i.starting_balance-i.ending_balance)::float/100.00 else null end as credit_amount_used,
    i.subscription_id,
    bt.created as created_at,
    'stripe' as src
from {{source('stripe_fivetran', 'balance_transaction')}} bt left join
    {{source('stripe_fivetran', 'charge')}} ch on bt.source = ch.id left join
    {{source('stripe_fivetran', 'invoice')}} i on ch.invoice_id = i.id left join
    {{source('bigcommerce', 'orders')}} bco on json_extract_path_text(ch.metadata, 'bigCommerceOrderId') = bco.id left join
    {{source('stripe_fivetran', 'refund')}} r on bt.source = r.id left join
    {{source('stripe_fivetran', 'charge')}} rch on r.charge_id = rch.id left join 
    {{ref('customer_id_map')}} cim on coalesce(ch.customer_id, rch.customer_id) = cim.stripe_customer_id 
where bt.type in ('charge', 'refund') and bt.created > '2022-08-01'

union

-- stripe credit transactions
select i.id as transaction_id,
    'subscription' as transaction_type,
    case when i.total = 0 then 'fully_discounted_subscription' when i.total != 0 then 'credit_subscription' end as transaction_sub_type,
    'stripe' as orig_system,
    cim.loop_customer_id,
    i.id as order_id,
    null as refund_id,
    0 as transaction_amount,
    i.subtotal::float/100.00 as order_total,
    (i.subtotal - i.total)::float/100.00 as discount_amount,
    -1.00*(i.starting_balance-i.ending_balance)::float/100.00 as credit_amount_used,
    i.subscription_id,
    i.created as created_at,
    'stripe' as src
from {{source('stripe_fivetran', 'invoice')}} i left join
    {{ref('customer_id_map')}} cim on i.customer_id = cim.stripe_customer_id
where i.amount_paid <= 0 and 
	i.amount_due <= 0 and 
    i.status != 'draft' and 
	i.created > '2022-08-10'and 
    (total > 0 or subtotal > 0) 

union
-- bigcommerce credit transactions
select o.id::text as transaction_id,
    'order' as transaction_type,
    'credited_order' as transaction_sub_type,
    'bigcommerce' as orig_system,
    cim.loop_customer_id,
    o.id::text as order_id,
    null as refund_id,
    0 as transaction_amount,
    o.total_inc_tax as order_total,
    o.discount_amount + o.coupon_discount as discount_amount,
    o.total_inc_tax as credit_amount_used,
    null as subscription_id,
    o.date_created as created_at,
    'bigcommerce' as src
from {{source('bigcommerce', 'orders')}} o left join
    {{ref('customer_id_map')}} cim on o.customer_id = cim.bigcommerce_customer_id
where o.external_source = 'loop_credit' and 
    o.status != 'Incomplete'

union
-- shopify orders
select o.id::text as transaction_id,
    case when o.source_name = 'subscription_contract' then 'subscription' else 'order' end as transaction_type,
    case
		when o.source_name = 'shopify_draft_order' then 'draft_orders'
		when o.source_name = 'subscription_contract' then 'subscriptions'
		when o.source_name = 'web' then 'order'
		when o.source_name = '3890849' then 'order'
		when o.source_name = '580111' then 'registry_order'
        end as transaction_sub_type,
    'shopify' as orig_system,
    cim.loop_customer_id,
    o.id::text as order_id,
    json_extract_path_text(json_extract_array_element_text(o.refunds,0), 'id')::text as refund_id,
    o.total_price::float as transaction_amount,
    o.total_price::float as order_total,
    o.total_discounts::float as discount_amount,
    0 as credit_amount_used,
    null as subscription_id,
    o.created_at,
    'shopify' as src
from {{source('shopify', 'orders')}} o left join
    {{ref('customer_id_map')}} cim on json_extract_path_text(customer, 'id') = cim.shopify_customer_id

union
-- shopify refunds
select r.refund_id::text as transaction_id,
    'refund' as transaction_type,
    case
		when o.source_name = 'shopify_draft_order' then 'draft_order_refund'
		when o.source_name = 'subscription_contract' then 'subscription_refund'
		when o.source_name = 'web' then 'order_refund'
		when o.source_name = '3890849' then 'order_refund'
		when o.source_name = '580111' then 'registry_order_refund'
        end as transaction_sub_type,
    'shopify' as orig_system,
    cim.loop_customer_id,
    o.id::text as order_id,
    r.refund_id,
    case when r.order_adjustments is null then rli.line_item_total_refund::decimal * -1.00
		when r.refund_line_items = '[]' then r.order_adjustments::decimal 
		else rli.line_item_total_refund::decimal * -1.00 + r.order_adjustments::decimal end as transaction_amount,
    o.total_price::float as order_total,
    o.total_discounts::float as discount_amount,
    0 as credit_amount_used,
    null as subscription_id,
    r.created_ts as created_at,
    'shopify' as src
from {{ref('fact_refund_shopify')}} r left join
    {{source('shopify', 'orders')}} o on r.order_id = o.id left join
    (select refund_id, 
        sum(subtotal) as line_item_total_refund
        from {{ref('fact_refund_line_item_shopify')}}
        group by 1) rli on r.refund_id = rli.refund_id left join
    {{ref('customer_id_map')}} cim on json_extract_path_text(customer, 'id') = cim.shopify_customer_id
