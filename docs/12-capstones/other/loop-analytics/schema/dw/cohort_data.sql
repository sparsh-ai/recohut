with sku_price as (
    select
        products.id as sku
        , avg(variants.price) as avg_price
    from shopify.products
    left join shopify.variants
        on products.id = variants.product_id
    group by 1
)
, contact_data as (
    select
        id as hubspot_customer_id
        , email
        , created_at
        , first_conversion_date
        , hs_analytics_source
        , hs_analytics_last_visit_timestamp
        , hs_analytics_source_data_1
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
        loop_number
        , sku
        , hubspot_customer_id
        , delivery_date
        , pick_up_date
        , contact_data.email
        , contact_data.created_at
        , contact_data.first_conversion_date
        , contact_data.hs_analytics_source
        , contact_data.hs_analytics_last_visit_timestamp
        , contact_data.hs_analytics_source_data_1
        , contact_data.membership_type
        , sku_price.avg_price as item_price
        , case
            when contact_data.membership_type ilike '%annual%'
                then 149.0/12
            when membership_product_name ilike '%annual%'
                then membership_price / 12.0
            else membership_price
          end as membership_mrr
        , loopshare_customers.email is not null as is_loopshare
        , min(delivery_date) over(partition by inventory_reporting_base.hubspot_customer_id) as first_delivery_date
    from googlesheets.inventory_reporting_base
    left join sku_price using(sku)
    left join contact_data using(hubspot_customer_id)
    left join membership_orders
        on lower(trim(contact_data.email)) = lower(trim(membership_orders.email))
        and membership_orders.rn = 1
    left join loopshare_customers
        on lower(trim(contact_data.email)) = lower(trim(loopshare_customers.email))
    where loop_number != -1
        and delivery_date is not null
)
,
  numbers AS (
    SELECT
      (ROW_NUMBER() OVER () - 1)::int AS ordinal
    FROM
      stl_scan
    LIMIT 100
)
, months as (
    select
        dateadd('month', ordinal, '2020-12-01'::date)::date as month
    from numbers
    where ordinal < 8
)
, item_month_expansion as (
    select *
    from item_level_base
    inner join months
        on item_level_base.delivery_date < dateadd('month', 1, months.month)
        and coalesce(item_level_base.pick_up_date, '9999-12-31') >= months.month
)
select
    month
    , hubspot_customer_id
    , date_trunc('month', created_at)::date as contact_creation
    , date_trunc('month', first_delivery_date)::date as first_delivery
    , item_price
    , is_loopshare
    , case when row_number() over(partition by hubspot_customer_id, month order by sku) = 1 then membership_mrr else 0 end as membership_mrr
from item_month_expansion
