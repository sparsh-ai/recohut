/*
SKU
BIN
Purchase Date
Received Date
Current Status
Warehouse Location
# of Loops
Disposal Date
Sale amount
*/

with number_deliveries as (
    select split_part(asset_tag_association_related_asset, '.', 1) as asset_id,
        count(*) as number_deliveries
    from {{source('quickbase', 'pick_deliveries')}}
    where pick_status != 'Pick Cancelled'
    group by 1
)

select i.quickbase_asset_id,
    i.item_sku as sku,
    i.asset_tag as bin,
    i.date_created,
    i.date_asset_received as received_date,
    i.purchase_date,
    i.inventory_status as status,
    i.inventory_location_inventory_location_name as warehouse_location,
    nd.number_deliveries as number_loops,
    coalesce(scrap.scrap_date, sell.asset_sale_date) as disposal_date,
    case when scrap.scrap_date is not null then 'scrap' when sell.asset_sale_date is not null then 'sale' else null end as disposal_type,
    sell.sale_amount
from {{source('quickbase', 'inventory')}} i left join
    number_deliveries nd on i.quickbase_asset_id = nd.asset_id left join
    {{source('quickbase', 'scrap_asset')}} scrap on i.quickbase_asset_id = split_part(scrap.asset_tag_association_related_asset, '.', 1) left join
    {{source('quickbase', 'sell_asset')}} sell on i.quickbase_asset_id = split_part(sell.asset_tag_association_related_asset, '.', 1)
    

    