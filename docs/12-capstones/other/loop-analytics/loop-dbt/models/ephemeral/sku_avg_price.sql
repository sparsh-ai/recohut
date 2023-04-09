select
    products.id as sku
    -- changed to min despite name being the same...
    -- basically people started entering different variants for the
    -- number of months one can rent so this was messnig everything up
    -- this was a hack to get around it until we can do things based on
    -- the actual subscription. See LOOP-69
    , min(variants.price) as avg_price
from {{ source('shopify', 'products') }}
left join {{ source('shopify', 'variants') }}
    on products.id = variants.product_id
group by 1
