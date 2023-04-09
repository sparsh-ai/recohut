/* 
line_item_id
order_id
product_id
product_description
price
discount_amount
quantity
subscription_id
subscription_item_id
customer_id
*/

--stripe
select ili.id as line_item_id,
    ili.invoice_id as order_id,
    coalesce(p.sku, sp.product_id) as sku,
    ili.description,
    ili.amount as price,
    0 as discount_amount,
    ili.quantity,
    ili.subscription_id,
    ili.subscription_item_id,
    'stripe' as src,
    cim.loop_customer_id
from {{source('stripe_fivetran', 'invoice_line_item')}} ili left join
    {{source('stripe_fivetran', 'invoice')}} i on ili.invoice_id = i.id left join
    {{ref('customer_id_map')}} cim on i.customer_id = cim.stripe_customer_id left join
    {{source('stripe_fivetran', 'price')}} sp on ili.price_id = sp.id left join
    {{ref('products')}} p on sp.product_id = p.stripe_product_id
where i.created > '2022-08-10' or i.created is null

union
--bigcommerce
select li.id::text as line_item_id,
    li.order_id::text,
    coalesce(p.sku, li.product_id::text) as sku,
    li.name as description,
    li.price_inc_tax as price,
    case when applied_discounts != '[]' then replace(split_part(split_part(applied_discounts, ',', 2), ':', 2), '\'', '')::decimal else 0.00 end as discount_amount,
    li.quantity,
    null as subscription_id,
    null as subscription_item_id,
    'bigcommerce' as src,
    cim.loop_customer_id
from {{source('bigcommerce', 'line_items')}} li left join
    {{source('bigcommerce', 'orders')}} o on li.order_id = o.id left join
    {{ref('customer_id_map')}} cim on o.customer_id = cim.bigcommerce_customer_id left join
    {{ref('products')}} p on li.product_id = p.bigcommerce_product_id
where o.status != 'Incomplete'

union
--shopify
select li.id as line_item_id,
    li.order_id,
    li.product_id as sku,
    li.title as product_name,
    li.price,
    case when discount_allocations != '[]' then JSON_EXTRACT_PATH_TEXT(json_extract_array_element_text(discount_allocations, 0), 'amount')::decimal else 0.00 end as discount_amount,
    li.quantity,
    null as subscription_id,
    null as subscription_item_id,
    'shopify' as src,
    cim.loop_customer_id
from {{source('shopify', 'line_items')}} li left join
    {{source('shopify', 'orders')}} o on li.order_id = o.id left join
    {{ref('customer_id_map')}} cim on json_extract_path_text(o.customer, 'id') = cim.shopify_customer_id