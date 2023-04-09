/* FOR IF CUSTOM FIELDS IS FIXED IN API
with custom_fields as (
    select
        p.id,
        json_extract_array_element_text(p.custom_fields, numbers.ordinal::INT, true) AS item
    from {{ source('bigcommerce', 'products') }} p
    cross join {{ ref('numbers') }} as numbers
    where ordinal < json_array_length(p.custom_fields, true)
),
product_map as (
    select
        id,
        json_extract_path_text(item, 'value') as shopify_product_id
    from custom_fields
    where json_extract_path_text(item, 'name') = 'Shopify Product ID'
)*/ 

with stripe_products as (
    select *,
        json_extract_path_text(metadata, 'bigCommerceProductId') as bigcommerce_product_id,
        json_extract_path_text(metadata, 'bigCommerceVariantId') as variant_id
    from {{source('stripe_fivetran', 'product')}} sp 
),

base as (
    select
    case when sp.variant_id is null or sp.variant_id = '' then coalesce(pim.sku, p.id::text) 
        else concat(sp.bigcommerce_product_id, sp.variant_id) end as sku
    , pim.sku as shopify_product_id
    , p.id as bigcommerce_product_id
    , sp.id as stripe_product_id
    , case when sp.variant_id is null or sp.variant_id = '' then p.name 
        else sp.name end as product_name
    , p.price
    , p.date_created as product_created_ts
    , p.date_modified as product_updated_ts
    , null as product_published_ts
    --, json_extract_path_text(p.custom_url, 'url') as product_page_handle
    , case when sp.livemode = false then 'test'
        when sp.is_deleted = true then 'deleted'
        when sp.active = false then 'not_active' 
        else 'active' end as product_status 
    , null as product_tags
    , sp.variant_id
from {{ source('bigcommerce', 'products') }} as p left join
    stripe_products sp on p.id = sp.bigcommerce_product_id left join
    dw2.product_id_map pim on p.id = pim.bigcommerce_product_id --will change if custom fields are pulled correctly
)

select *
from base

union all 

select dp.sku,
    dp.sku as shopify_product_id,
    null as bigcommerce_product_id,
    null as stripe_product_id,
    dp.product_name,
    null as price,
    dp.product_created_ts,
    dp.product_updated_ts,
    dp.product_published_ts,
    dp.product_status,
    dp.product_tags,
    null as variant_id
from {{ref('dim_product_shopify')}} dp left join
    base b on dp.sku = b.sku
where b.sku is null