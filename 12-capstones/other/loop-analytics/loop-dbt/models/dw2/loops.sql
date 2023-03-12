with loop_master as (
    select
        pd.asset_tag_association_asset_tag as bin
        , cim.loop_customer_id
        , SPLIT_PART(ol.id, '.', 1) AS line_item_id
        , ol.qb_item_sku as sku
        , dp.bigcommerce_product_id
        , SUBSTRING(ol.order_id,0, CHARINDEX('.',ol.order_id)) as order_id
        , NULLIF(sd.scheduled_delivery_date, '')::DATE delivery_date
        , NULLIF(sp.scheduled_pickup_date, '')::DATE AS pick_up_date
        -- , inventory_reporting_base.restocking_time as restocking_time
        , dp.price AS avg_price
        , CASE 
            WHEN ol.order_id_qb_inventory_location_inventory_location_name ilike 'bay %' then 'SF'
            WHEN ol.order_id_qb_inventory_location_inventory_location_name ilike 'ny %' then 'NYC'
        END as ops_location
        FROM {{source('quickbase', 'order_lines')}} ol
        LEFT JOIN {{ ref('products') }} dp
            ON ol.qb_item_sku = dp.sku
        LEFT JOIN 
            (   select
                    *
                    , row_number() OVER (partition by related_order_line order by date_modified desc) as rn
                FROM {{source('quickbase', 'schedule_delivery')}}
                WHERE schedule_delivery.delivery_status != 'Scheduled Delivery Cancelled'     
            ) sd
            ON sd.related_order_line_ref = ol.id
            AND sd.rn = 1
        LEFT JOIN (
            SELECT DISTINCT
                asset_tag_association_asset_tag, scheduled_delivery_related_order_line
            FROM {{source('quickbase', 'pick_deliveries')}}
        ) pd
            ON pd.scheduled_delivery_related_order_line = sd.related_order_line
        LEFT JOIN 
            (   select
                    *
                    , row_number() OVER (partition by delivery_performance_picking_scheduled_delivery_related_order_line_ref order by date_modified desc) as rn
                FROM {{source('quickbase', 'schedule_pickup')}}
                WHERE scheduled_pickup_status != 'Scheduled Pickup Cancelled'     
            ) sp
            ON sp.delivery_performance_picking_scheduled_delivery_related_order_line_ref = ol.id
            AND sp.rn = 1
        LEFT JOIN {{source('quickbase', 'customers')}} c
            ON SUBSTRING(ol.qb_order_related_customer,0, CHARINDEX('.',ol.qb_order_related_customer)) = c.id::TEXT
        left join {{ ref('customer_id_map') }} AS cim
            on c.id = cim.quickbase_customer_id
        where ol.qb_ol_status not in (
          'Closed-Refunded',
          'Closed-Non-inventory',
          'Closed-Duplicate',
          'Closed-Registry',
          'Closed-Test',
          'Closed-Trial',
          'Closed'
        ) 
        AND product_name NOT ILIKE '% plan'
        AND product_name NOT ILIKE '%membership%'
)  

select 
    *
from loop_master