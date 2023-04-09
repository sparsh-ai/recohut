with base as (
    select
        customers.email
        , mim.member_id
        , orders.id as order_id
        , orders.created_at
        , products.title as membership_product_name
        , products.id as product_id
        , sku_price.avg_price as membership_price
        , row_number() over(partition by mim.member_id order by orders.created_at) as rn
    from shopify.line_items
    left join shopify.orders
        on line_items.order_id = orders.id
    left join shopify.products
        on line_items.product_id = products.id
    left join shopify.customers
        on customers.id = json_extract_path_text(orders.customer, 'id')
	LEFT JOIN {{ ref('member_id_map')}} as mim	
        on json_extract_path_text(orders.customer, 'id') = mim.src_id
        and src='shopify'
    left join {{ ref('sku_avg_price') }} as sku_price
          on sku_price.sku = products.id
    where products.title ilike '%member%'
        or products.title ilike '%plan'
)
select
    email
    , member_id
    , created_at
    , membership_product_name
    , order_id
    , product_id
    , membership_price
from base
where rn = 1
