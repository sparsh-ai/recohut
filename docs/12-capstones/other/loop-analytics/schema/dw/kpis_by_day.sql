with numbers AS (
    SELECT
      (ROW_NUMBER() OVER () - 1)::int AS ordinal
    FROM
      stl_scan
    LIMIT 750
)
, days as (
    select
        dateadd('day', ordinal, '2020-12-01'::date)::date as date
    from numbers
)
, membership_orders as (
    select
        customers.email
        , orders.created_at
        , products.title as membership_product_name
        , row_number() over(partition by customers.email order by orders.created_at) as rn
    from shopify.line_items
    left join shopify.orders
        on line_items.order_id = orders.id
    left join shopify.products
        on line_items.product_id = products.id
    left join shopify.customers
        on customers.id = trim(substring(orders.customer, strpos(orders.customer, ' '), strpos(orders.customer, ',') - strpos(orders.customer, ' ')))
    where products.title ilike '%member%'
)
, sku_price as (
    select
        products.id as sku
        , avg(variants.price) as avg_price
    from shopify.products
    left join shopify.variants
        on products.id = variants.product_id
    group by 1
)
, membership_stats as (
    select
        hs_lifecyclestage_customer_date::date as date
        , count(*) as new_members
        , sum(case
                when membership_type ilike '%annual%'
                or membership_type ilike '%149%'
                or membership_product_name ilike '%annual%'
            then 1
            else 0
            end) as new_annual_members
        , sum(case
                when membership_type ilike '%month%'
                or membership_product_name ilike '%month%'
            then 1
            else 0
            end) as new_monthly_members
        , sum(case
                when membership_type ilike '%item%'
                or membership_product_name ilike '%item%'
            then 1
            else 0
            end) as new_per_item_members
        , new_members - new_annual_members - new_monthly_members - new_per_item_members AS new_pending_members
        , new_annual_members * (149.0 / 12.0) as new_annual_mrr
        , new_monthly_members * 18.0 as new_monthly_mrr
        , new_annual_mrr + new_monthly_mrr as new_membership_mrr
    from hubspot.contacts
    left join membership_orders
    on lower(trim(contacts.email)) = lower(trim(membership_orders.email))
    where nullif(hs_lifecyclestage_customer_date, '') is not null
    group by 1
)
, delivery_stats as (
    select
        delivery_date as date
        , count(*) as delivered_items
        , sum(avg_price) as delivered_mrr
    from googlesheets.inventory_reporting_base
    left join sku_price
        using(sku)
    where delivery_date is not null
    group by 1
    order by 2 desc
)
, pickup_stats as (
    select
        pick_up_date as date
        , count(*) as picked_up_items
        , sum(avg_price) as picked_up_mrr
    from googlesheets.inventory_reporting_base
    left join sku_price
        using(sku)
    where pick_up_date is not null
    group by 1
    order by 2 desc
)
, all_stats_base as (
    select
        days.date
        , NVL(membership_stats.new_members, 0) AS new_members
        , NVL(membership_stats.new_annual_members, 0) AS new_annual_members
        , NVL(membership_stats.new_monthly_members, 0) AS new_monthly_members
        , NVL(membership_stats.new_per_item_members, 0) AS new_per_item_members
        , NVL(membership_stats.new_pending_members, 0) AS new_pending_members
        , NVL(membership_stats.new_annual_mrr, 0) AS new_annual_mrr
        , NVL(membership_stats.new_monthly_mrr, 0) AS new_monthly_mrr
        , new_annual_mrr + new_monthly_mrr as new_membership_mrr
        , NVL(delivery_stats.delivered_items, 0) AS delivered_items
        , NVL(delivery_stats.delivered_mrr, 0) AS delivered_mrr
        , NVL(pickup_stats.picked_up_items, 0) AS picked_up_items
        , NVL(pickup_stats.picked_up_mrr, 0) AS picked_up_mrr
    from days
    left join membership_stats
        on days.date = membership_stats.date
    left join delivery_stats
        on days.date = delivery_stats.date
    left join pickup_stats
        on days.date = pickup_stats.date
)
select *
    , SUM(new_members) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS new_members_cum
    , SUM(new_annual_members) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS new_annual_members_cum
    , SUM(new_monthly_members) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS new_monthly_members_cum
    , SUM(new_per_item_members) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS new_per_item_members_cum
    , SUM(new_pending_members) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS new_pending_members_cum
    , SUM(delivered_items) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS delivered_items_cum
    , SUM(picked_up_items) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS picked_up_items_cum
    , delivered_items_cum - picked_up_items_cum as active_items
    , SUM(delivered_mrr) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS delivered_mrr_cum
    , SUM(picked_up_mrr) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS picked_up_mrr_cum
    , delivered_mrr_cum - picked_up_mrr_cum as active_rental_mrr
    , SUM(new_annual_mrr) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS new_annual_mrr_cum
    , SUM(new_monthly_mrr) OVER(ORDER BY date ROWS UNBOUNDED PRECEDING) AS new_monthly_mrr_cum
    , new_annual_mrr_cum + new_monthly_mrr_cum as membership_mrr
    , active_rental_mrr + membership_mrr as total_mrr
from all_stats_base
