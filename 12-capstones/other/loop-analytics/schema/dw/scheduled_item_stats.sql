with sku_price as (
    select
        products.id as sku
        , avg(variants.price) as avg_price
    from shopify.products
    left join shopify.variants
        on products.id = variants.product_id
    group by 1
)
select
    count(*) as scheduled_items
    , count(distinct hubspot_customer_id) as customers_with_scheduled_items
    , sum(avg_price) as scheduled_mrr
from googlesheets.inventory_reporting_base
left join sku_price
    using(sku)
where delivery_date > CURRENT_DATE
