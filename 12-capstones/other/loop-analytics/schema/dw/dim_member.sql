with contact_data as (
    select
        id as hubspot_customer_id
        , email
        , created_at as contact_created_ts
        , first_conversion_date as first_conversion_ts
        , hs_analytics_source
        , hs_analytics_last_visit_timestamp as hs_analytics_last_visit_ts
        , hs_analytics_source_data_1 AS hs_analytics_source_data
        , membership_type
    from hubspot.contacts
)
, membership_orders as (
    select
        customers.email
        , orders.created_at
        , products.title as membership_product_name
        , products.id as product_id
        , sku_price.avg_price as membership_price
        , row_number() over(partition by customers.email order by orders.created_at) as rn
    from shopify.line_items
    left join shopify.orders
        on line_items.order_id = orders.id
    left join shopify.products
        on line_items.product_id = products.id
    left join shopify.customers
        on customers.id = trim(substring(orders.customer, strpos(orders.customer, ' '), strpos(orders.customer, ',') - strpos(orders.customer, ' ')))
    left join sku_price on
        sku_price.sku = products.id
    where products.title ilike '%member%'
)
, loopshare_customers as (
    select distinct customers.email
    from shopify.orders
    left join shopify.customers
        on customers.id = json_extract_path_text(orders.customer, 'id')
)
, item_level_base as (
    select
        , contact_data.*
        , case
            when contact_data.membership_type ilike '%annual%'
                then 149.0/12
            when membership_product_name ilike '%annual%'
                then membership_price / 12.0
            else membership_price
          end as membership_mrr
        , loopshare_customers.email is not null as is_loopshare
    from membership_orders
        on lower(trim(contact_data.email)) = lower(trim(membership_orders.email))
        and membership_orders.rn = 1
    left join loopshare_customers
        on lower(trim(contact_data.email)) = lower(trim(loopshare_customers.email))
)
