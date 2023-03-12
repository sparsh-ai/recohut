with base as (
    select
        c.email
        , mim.member_id
        , o.id::text as order_id
        , o.date_created as created_at
        , p.product_name as membership_product_name
        , p.sku as product_id
        , p.price as membership_price
    from {{ source('bigcommerce', 'line_items') }} li
    left join {{ ref('bigcommerce_completed_orders') }} o
        on li.order_id = o.id
    left join {{ ref('dim_product') }} p
        on li.product_id = p.bigcommerce_product_id
    left join {{ source('bigcommerce', 'customers') }} c
        on c.id = o.customer_id
    left join {{ref('member_id_map')}} mim
        on o.customer_id = mim.src_id
      and src='bigcommerce'
    where p.product_name ilike '%member%'
        or p.product_name ilike '%plan'

    union all

    select
        customers.email
        , mim.member_id
        , orders.id as order_id
        , orders.created_at
        , products.title as membership_product_name
        , products.id as product_id
        , sku_price.avg_price as membership_price
    from shopify.line_items
    left join shopify.orders
        on line_items.order_id = orders.id
    left join shopify.products
        on line_items.product_id = products.id
    left join shopify.customers
        on customers.id = json_extract_path_text(orders.customer, 'id')
    LEFT JOIN {{ ref('member_id_map')}} as mim
        on customers.id = mim.src_id
      and src='shopify'
    left join {{ ref('sku_avg_price') }} as sku_price
          on sku_price.sku = products.id
    where products.title ilike '%member%'
        or products.title ilike '%plan'
),
base_with_rn as (
    select *,
        row_number() over(partition by member_id order by created_at) as rn
    from base
)

select
    email
    , member_id
    , created_at
    , membership_product_name
    , order_id
    , product_id
    , membership_price
from base_with_rn
where rn = 1
