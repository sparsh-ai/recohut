select
    asset_tag as bin
    , item_sku as sku
    , item_category as category
    , item_name as shopify_item_name
    , merchant as store
    , payment_method as purchase_method
    , nullif(purchase_date, '')::date
    , nullif(cost_pretax_price, '')::float as retail_price
    , nullif(cost_pretax_price, '')::float as actual_purchase_price
    , nullif(cost_sales_tax, '')::float as actual_tax_cost
    , nullif(cost_shipping, '')::float as actual_shipping_cost
    , nullif(cost_total, '')::float as actual_total_cost
    , nullif(asset_build_time_actual, '')::float as assembly_time
    , i.inventory_status as bin_status
    , i.inventory_location_inventory_location_name as location
    , nullif(date_asset_received, '') is not null as received
    , nullif(estimated_arrival_date, '')::date as estimated_actual_arrival
    , receipt_document as tracking_info -- not sure here
    , case when sa.record_id is not null then TRUE else FALSE end as asset_sold
    , nullif(sa.asset_sale_date, '')::date
    , nullif(sa.sale_amount, '') as asset_sale_amount
    , case when sca.record_id is not null then TRUE else FALSE end as asset_scrapped
    , nullif(sca.scrap_date, '')::date
    , CASE 
        WHEN i.inventory_location_inventory_location_name ilike '%bay%' THEN 'SF'
        WHEN i.inventory_location_inventory_location_name ilike 'NY %' THEN 'NY'
    END as ops_location
    , i.price_paid_variance
    , i.total_cost_including_store_credit
    , i.pretax_price_net_of_discount
    , i.oem__of_retail_price
    , i.store_credit_issued
    , i.oem_discount_flatno_discountqty_tiering
    , i.oem_vendor_name
    , i.order_ as purchase_order
from {{source('quickbase', 'inventory')}} i
LEFT JOIN {{source('quickbase', 'associate_asset_tag')}} aat 
    using(asset_tag)
LEFT JOIN {{source('quickbase', 'sell_asset')}} sa 
   on i.asset_tag = sa.asset_tag_association_asset_tag
LEFT JOIN {{source('quickbase', 'scrap_asset')}} sca 
   on i.asset_tag = sca.asset_tag_association_asset_tag