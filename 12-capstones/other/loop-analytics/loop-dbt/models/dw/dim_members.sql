-- things i need to know
-- x when did they first pay for a membership, and membership type
-- x when did they last pay for a membership, and membership type
-- x are they paying for a product? the number of products they've paid for in the last 30 days
-- x next pickup date


with transaction_agg as (
    select
        member_id
        , min(
            case 
                when nrli.product_name ilike '%month%' 
                    and (nrli.product_name ilike '%member%' or nrli.product_name ilike '%plan')
                then order_ts 
            end
        ) as min_month_payment_ts
        , min(
            case 
                when nrli.product_name ilike '%annual%' 
                    and (nrli.product_name ilike '%member%' or nrli.product_name ilike '%plan')
                then order_ts 
            end
        ) as min_annual_payment_ts
        , min(
            case 
                when nrli.product_name ilike '%per%item%' 
                    and (nrli.product_name ilike '%member%' or nrli.product_name ilike '%plan')
                then order_ts 
            end
        ) as min_per_item_payment_ts
        , max(
            case 
                when nrli.product_name ilike '%month%' 
                    and (nrli.product_name ilike '%member%' or nrli.product_name ilike '%plan')
                then order_ts 
            end
        ) as max_month_payment_ts
        , max(
            case 
                when nrli.product_name ilike '%annual%' 
                    and (nrli.product_name ilike '%member%' or nrli.product_name ilike '%plan')
                then order_ts 
            end
        ) as max_annual_payment_ts
        , max(
            case 
                when nrli.product_name ilike '%per%item%' 
                    and (nrli.product_name ilike '%member%' or nrli.product_name ilike '%plan')
                then order_ts 
            end
        ) as max_per_item_payment_ts
        , max(
            case 
                when not (nrli.product_name ilike '%member%' or nrli.product_name ilike '%plan')
                then order_ts 
            end
        ) as max_product_payment_ts
        , count(distinct 
            case 
                when order_ts >= DATEADD('d', -35, CURRENT_DATE)
                    and not (nrli.product_name ilike '%member%' or nrli.product_name ilike '%plan')
                then nrli.sku
            end
        ) AS active_sku_ct
    from {{ref('non_refunded_line_items')}} nrli left join
        {{ref('fact_order')}} fo on nrli.order_id = fo.order_id left join
        {{ref('dim_product')}} dp on nrli.sku = dp.sku
    group by 1
)
, contact_data as (
    select
      mim.member_id
        , email
        , created_at as contact_created_ts
        , first_conversion_date as first_conversion_ts
        , hs_analytics_source
        , hs_analytics_last_visit_timestamp as hs_analytics_last_visit_ts
        , hs_analytics_source_data_1 AS hs_analytics_source_data
        , membership_type as hs_membership_type
        , COALESCE(
            nullif(hs_lifecyclestage_customer_date, '')::timestamp,
            -- fills a few nulls that seem to pre-date this status
            case when NULLIF(membership_type, '') is not null then created_at end
        )  as hs_membership_date
        , firstname as first_name
        , lastname as last_name
        , child_1_dob
        , child_2_dob
        , child_3_dob
        , least(child_1_dob, child_2_dob, child_3_dob) as youngest_child_dob
        , case when child_1_dob is not null then 1 else 0 end + case when child_2_dob is not null then 1 else 0 end + case when child_3_dob is not null then 1 else 0 end as number_of_children
        , expecting_at_sign_up
        , city
        , address
        , zip
        , state
        , monthly_membership_end_date
        , reason_for_canceling
    , row_number() OVER (PARTITION BY mim.member_id ORDER BY mim.email_key = mim.member_id DESC) AS rn
    -- chose descending because true is > false in the ordering. I could explicitly map these to be sure that it doesn't arbitrarily re-order them.
    FROM
      {{ source('hubspot', 'contacts') }} hc
        LEFT JOIN {{ ref( 'member_id_map') }} AS mim
    ON hc.id = mim.src_id
      AND mim.src = 'hubspot'
    WHERE
      1 = 1
    AND hc.email NOT ILIKE '%loop.baby%'
    AND hc.email NOT ILIKE '%dvx.ventures%'
    AND hc.email != 'armin.m.garcia+loop3@gmail.com'
)
, loopshare_customers as (
    select
      c.email
      , mim.member_id
      , min(o.created_at) as loop_share_ts
    from {{ source('shopify', 'orders') }} o
    left join {{ source('shopify', 'customers') }} c
        on c.id = json_extract_path_text(o.customer, 'id')
    left join {{ ref('member_id_map') }} as mim
      on c.id = mim.src_id
         and mim.src = 'shopify'
    where discount_codes ilike '%loopshare%'
  group by 1, 2
), 
first_order AS (
    select
        member_id
        , min(case when not is_membership_order then order_ts end)::date as _first_item_order_dt
        , min(case when is_membership_order then order_ts end)::date as _first_membership_order_dt
    from {{ ref('fact_order') }}
    where not is_gift_card_order and 
        financial_status != 'refunded'
    group by 1
)
, deliver_pickup_dates AS (
    select
        member_id
        , min(NVL(delivery_date, '9999-12-31')) as _first_delivery_dt
        , max(NVL(pick_up_date, '9999-12-31')) as _last_pick_up_dt
        , max(case when pick_up_date is not null and pick_up_date >= CURRENT_DATE then pick_up_date end) as next_pickup_date
    from {{ ref('fact_loop') }}
    group by 1
)
, base AS (
    select
        cd.*
        , lc.email is not null as is_loopshare
        , lc.loop_share_ts

        , LEAST (
            NVL(mo2.membership_first_purchase_dt::date, '9999-12-31'),
            NVL(o1._first_item_order_dt, '9999-12-31'),
            NVL(dpd._first_delivery_dt, '9999-12-31'),
            NVL(o1._first_membership_order_dt, '9999-12-31')
        ) AS first_membership_order_dt

        , LEAST(
            NVL(o1._first_item_order_dt, '9999-12-31'),
            NVL(dpd._first_delivery_dt, '9999-12-31')
        ) AS first_item_order_dt

        , NVL(dpd._first_delivery_dt, '9999-12-31') AS first_delivery_dt
        , NVL(dpd._last_pick_up_dt, '9999-12-31') AS last_pick_up_dt
        
        , LEAST(
            NVL(mo2.membership_first_purchase_dt::date, '9999-12-31'),
            NVL(ta.min_month_payment_ts::date, '9999-12-31'),
            NVL(ta.min_annual_payment_ts::date, '9999-12-31'),
            NVL(ta.min_per_item_payment_ts::date, '9999-12-31'), 
            NVL(CASE 
                    WHEN mwham.member_id IS NOT NULL
                    THEN o1._first_item_order_dt
                    END,
                '9999-12-31'),
            -- hack for "non-membership members"
            NVL(CASE 
                    WHEN mti.ct_active_product_payments > 0 AND mti.avg_purchased_gift_card < 1 AND mti.avg_purchased_registry_product < 1
                    THEN o1._first_item_order_dt
                    END,
                '9999-12-31')
        ) AS membership_start_dt

        , case 
            when ta.max_annual_payment_ts is not null and ta.max_month_payment_ts is not null
                then 
                    case 
                        when ta.max_annual_payment_ts >=ta.max_month_payment_ts
                        then 'annual'
                        else 'monthly'
                    end
            when ta.max_annual_payment_ts is not null and ta.max_month_payment_ts is null
                then 'annual'
            when ta.max_annual_payment_ts is null and ta.max_month_payment_ts is not null
                then 'monthly'
            when ta.max_per_item_payment_ts is not null
                then 'per-item'
        end as billing_membership_type

        , case
            when mwham.member_id is not null
                then 'annual'
            when mti.is_influencer = 1
                then 'influencer'
            when mti.avg_purchased_gift_card = 1
                then 'gift-card-buyer'
            when mti.avg_purchased_registry_product = 1
                then 'registry-product-buyer'
            when membership_start_dt > CURRENT_DATE
                then 
                case 
                    -- 2022.06.07 meeting determined people products and not memberships should be treated as per-item
                    when mti.ct_active_product_payments > 0
                        then 'per-item'
                    else 'lead'
                end
            WHEN billing_membership_type is not null
                then billing_membership_type
            when cd.hs_membership_type ilike '%item%' or mo.membership_product_name ilike '%item%'
                then 'per-item'
            -- 2021.07.14 meeting determined TBDs should be treated as per-item
            when cd.hs_membership_date is not null or nullif(cd.hs_membership_type, '') is not null
                then 'per-item'
            else 'lead'
        end as membership_type        
        , o1._first_membership_order_dt AS src_first_membership_order_dt
        , o1._first_item_order_dt AS src_first_item_order_dt
        , dpd._first_delivery_dt AS src_first_delivery_dt
        , dpd._last_pick_up_dt AS src_last_pickup_dt
        , mti.first_membership_purchase_ts
        , mti.last_membership_payment_ts
        , mti.last_product_payment_ts
        , mti.ct_active_product_payments
        , mti.ct_purchased_skus
        , mti.is_ever_purchased_snoo
        , mti.ct_active_products_loops
        , mti.ct_items_with_scheduled_delivery
        , mti.ct_items_with_scheduled_pickup
        , mti.ct_skus_in_loop_master
        , mti.is_only_has_snoo_loop
        , mti.first_delivery_date
        , mti.is_only_has_snoo_payments
        , CASE
            WHEN
                -- intentionally ignore per-item membership payments, don't really know when they came through or if they even have one
                (first_membership_purchase_ts::date <= CURRENT_DATE or membership_type = 'per-item')
                -- for pre-active, don't care if they're current on membership payments because they may be a delayed start
                -- AND (
                --     (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                --     OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                -- )
                AND coalesce(ct_items_with_scheduled_delivery, 0) = 0
                AND coalesce(ct_active_products_loops, 0) = 0
                AND coalesce(ct_skus_in_loop_master, 0) = 0
            THEN 1
            WHEN
                -- intentionally ignore per-item membership payments, don't really know when they came through or if they even have one
                (first_membership_purchase_ts::date <= CURRENT_DATE or membership_type = 'per-item')
                -- for pre-active, don't care if they're current on membership payments because they may be a delayed start
                -- AND (
                --    (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                --     OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                -- )
                AND coalesce(ct_items_with_scheduled_delivery, 0) > 0
                AND coalesce(ct_active_products_loops, 0) = 0
                AND coalesce(ct_skus_in_loop_master, 0) = 0
            THEN 2
            WHEN
                -- intentionally ignore per-item membership payments, don't really know when they came through or if they even have one
                (first_membership_purchase_ts::date <= CURRENT_DATE or membership_type = 'per-item')
                AND (
                    (
                        (
                            (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                            OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                        OR membership_type = 'per-item'
                    )
                    OR (
                        (
                        (last_membership_payment_ts <= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts <= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                    AND (
                        last_product_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly'
                        OR (last_product_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                )
                )
                AND coalesce(ct_items_with_scheduled_delivery, 0) - coalesce(ct_items_with_scheduled_pickup, 0) <= 0
                AND coalesce(ct_active_products_loops, 0) > 1
                AND coalesce(ct_active_products_loops, 0) + coalesce(ct_items_with_scheduled_delivery, 0) > coalesce(ct_items_with_scheduled_pickup, 0)
            THEN 3
            WHEN
                -- intentionally ignore per-item membership payments, don't really know when they came through or if they even have one
                (first_membership_purchase_ts::date <= CURRENT_DATE or membership_type = 'per-item')
                AND (
                    (
                        (
                            (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                            OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                        OR membership_type = 'per-item'
                    )
                    OR (
                        (
                        (last_membership_payment_ts <= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts <= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                    AND (
                        last_product_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly'
                        OR (last_product_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                )
                )
                AND coalesce(ct_items_with_scheduled_delivery, 0) - coalesce(ct_items_with_scheduled_pickup, 0)  > 0
                AND coalesce(ct_active_products_loops, 0) > 1
                AND coalesce(ct_active_products_loops, 0) + coalesce(ct_items_with_scheduled_delivery, 0) > coalesce(ct_items_with_scheduled_pickup, 0)
            THEN 4
            WHEN
                -- intentionally ignore per-item membership payments, don't really know when they came through or if they even have one
                (first_membership_purchase_ts::date <= CURRENT_DATE or membership_type = 'per-item')
                AND (
                    (
                        (
                            (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                            OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                        OR membership_type = 'per-item'
                    )
                    OR (
                        (
                        (last_membership_payment_ts <= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts <= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                    AND (
                        last_product_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly'
                        OR (last_product_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                )
                )
                AND coalesce(ct_items_with_scheduled_delivery, 0) - coalesce(ct_items_with_scheduled_pickup, 0) = 0
                AND coalesce(ct_active_products_loops, 0) = 1
                AND coalesce(ct_active_products_loops, 0) + coalesce(ct_items_with_scheduled_delivery, 0) > coalesce(ct_items_with_scheduled_pickup, 0)
                AND is_only_has_snoo_loop = 1
                AND first_delivery_date < DATEADD('d', -90, CURRENT_DATE)
            THEN 12
            WHEN
                -- intentionally ignore per-item membership payments, don't really know when they came through or if they even have one
                (first_membership_purchase_ts::date <= CURRENT_DATE or membership_type = 'per-item')
                AND (
                    (
                        (
                            (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                            OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                        OR membership_type = 'per-item'
                    )
                    OR (
                        (
                        (last_membership_payment_ts <= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts <= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                    AND (
                        last_product_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly'
                        OR (last_product_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                )
                )
                AND coalesce(ct_items_with_scheduled_delivery, 0) - coalesce(ct_items_with_scheduled_pickup, 0) > 0
                AND coalesce(ct_active_products_loops, 0) = 1
                AND coalesce(ct_active_products_loops, 0) + coalesce(ct_items_with_scheduled_delivery, 0) > coalesce(ct_items_with_scheduled_pickup, 0)
            THEN 5
            WHEN
                -- intentionally ignore per-item membership payments, don't really know when they came through or if they even have one
                (first_membership_purchase_ts::date <= CURRENT_DATE or membership_type = 'per-item')
                AND (
                    (
                        (
                            (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                            OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                        OR membership_type = 'per-item'
                    )
                    OR (
                        (
                        (last_membership_payment_ts <= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts <= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                    AND (
                        last_product_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly'
                        OR (last_product_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                )
                )
                AND ( coalesce(ct_items_with_scheduled_delivery, 0) = 0 OR coalesce(ct_items_with_scheduled_delivery, 0) - coalesce(ct_items_with_scheduled_pickup, 0) = 0) 
                AND coalesce(ct_active_products_loops, 0) = 1
                AND (coalesce(ct_items_with_scheduled_pickup, 0) = 0 OR coalesce(ct_items_with_scheduled_delivery, 0) - coalesce(ct_items_with_scheduled_pickup, 0) = 0) 
            THEN 6
            WHEN
                -- intentionally ignore per-item membership payments, don't really know when they came through or if they even have one
                (first_membership_purchase_ts::date <= CURRENT_DATE or membership_type = 'per-item')
                AND (
                    (
                        (
                            (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                            OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                        OR membership_type = 'per-item'
                    )
                    OR (
                        (
                        (last_membership_payment_ts <= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts <= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                    AND (
                        last_product_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly'
                        OR (last_product_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                )
                )
                AND coalesce(ct_items_with_scheduled_delivery, 0) > 0
                AND coalesce(ct_active_products_loops, 0) = 0
                AND coalesce(ct_skus_in_loop_master, 0) > 0
            THEN 7
            WHEN
                -- intentionally ignore per-item membership payments, don't really know when they came through or if they even have one
                (first_membership_purchase_ts::date <= CURRENT_DATE or membership_type = 'per-item')
                AND NOT (
                    (
                    (
                        (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                    AND
                    membership_type != 'per-item'
                )
                    OR (
                        (
                        (last_membership_payment_ts <= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts <= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                    AND (
                        last_product_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly'
                        OR (last_product_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                )
                )
                AND coalesce(ct_items_with_scheduled_delivery, 0) - coalesce(ct_items_with_scheduled_pickup, 0) <= 0
                AND coalesce(ct_active_products_loops, 0) > 0
            THEN 9
            WHEN
                -- intentionally ignore per-item membership payments, don't really know when they came through or if they even have one
                (first_membership_purchase_ts::date <= CURRENT_DATE or membership_type = 'per-item')
                AND (
                    (
                        (
                            (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                            OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                        OR membership_type = 'per-item'
                    )
                    OR (
                        (
                        (last_membership_payment_ts <= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts <= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                    AND (
                        last_product_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly'
                        OR (last_product_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                )
                )
                AND coalesce(ct_items_with_scheduled_delivery, 0) = 0
                AND coalesce(ct_active_products_loops, 0) = coalesce(ct_items_with_scheduled_pickup, 0)
                AND coalesce(ct_active_products_loops, 0) > 0
            THEN 8
            WHEN
                membership_type != 'per-item'  -- per-item folks can't have a membership lapse, when they return all their items they're done
                AND first_membership_purchase_ts::date < CURRENT_DATE
                AND (
                    (
                        (
                            (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                            OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                        )
                        OR membership_type = 'per-item'
                    )
                    OR (
                        (
                        (last_membership_payment_ts <= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts <= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                    AND (
                        last_product_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly'
                        OR (last_product_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                )
                )
                AND coalesce(ct_items_with_scheduled_delivery, 0) = 0
                AND coalesce(ct_active_products_loops, 0) = 0
                AND coalesce(ct_skus_in_loop_master, 0) > 0
            THEN 10
            WHEN
                -- intentionally ignore per-item membership payments, don't really know when they came through or if they even have one
                (first_membership_purchase_ts::date <= CURRENT_DATE or membership_type = 'per-item')
                AND NOT (
                    (
                    (
                        (last_membership_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                    AND
                    membership_type != 'per-item'
                )
                    OR (
                        (
                        (last_membership_payment_ts <= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly')
                        OR (last_membership_payment_ts <= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                    AND (
                        last_product_payment_ts >= DATEADD('d', -35, CURRENT_DATE) and membership_type = 'monthly'
                        OR (last_product_payment_ts >= DATEADD('d', -370, CURRENT_DATE) and membership_type = 'annual')
                    )
                )
                )
                AND coalesce(ct_items_with_scheduled_delivery, 0) = 0
                AND coalesce(ct_active_products_loops, 0) = 0
            THEN 11
        END as cases
        , CASE cases
            WHEN 1
            THEN 'Pre Active'
            WHEN 2
            THEN 'Pre Active'
            WHEN 3
            THEN 'Active'
            WHEN 4
            THEN 'Active'
            WHEN 5
            THEN 'Active'
            WHEN 6
            THEN 'Active'
            WHEN 7
            THEN 'Active'
            WHEN 8
            THEN 'Active'
            WHEN 9
            THEN 'Active'
            WHEN 10
            THEN 'Active'
            WHEN 11
            THEN 'Churned'
            WHEN 12
            THEN 'Active'
            WHEN 13
            THEN 'Active'
        END AS member_status
        , CASE cases
            WHEN 1
            THEN 'Unscheduled'
            WHEN 2
            THEN 'Scheduled'
            WHEN 3
            THEN 'Engaged'
            WHEN 4
            THEN 'Engaged'
            WHEN 5
            THEN '1 Item only'
            WHEN 6
            THEN '1 Item only'
            WHEN 7
            THEN 'Re-engaging'
            WHEN 8
            THEN 'At Risk'
            WHEN 9
            THEN 'Churn Pending'
            WHEN 10
            THEN 'Churn Pending'
            WHEN 11
            THEN 'Churned'
            WHEN 12
            THEN 'At Risk'
            WHEN 13
            THEN 'Active'
        END AS member_sub_status
        , CASE cases
            WHEN 1
            THEN 'Pre Active - Unscheduled'
            WHEN 2
            THEN 'Pre Active - Scheduled'
            WHEN 3
            THEN 'Multiple Items'
            WHEN 4
            THEN 'Growing basket'
            WHEN 5
            THEN 'Growing basket'
            WHEN 6
            THEN 'Maintaining'
            WHEN 7
            THEN 'No active items, but active membership'
            WHEN 8
            THEN 'Pickups scheduled'
            WHEN 9
            THEN 'Payments Stopped'
            WHEN 10
            THEN 'Pickups made'
            WHEN 11
            THEN 'Churned'
            WHEN 12
            THEN 'Snoo only >3mo'
        END AS member_status_detail
    from contact_data cd
    left join transaction_agg ta
        ON cd.member_id = ta.member_id
    left join {{ ref('membership_orders') }} mo
        ON cd.member_id = mo.member_id
    left join loopshare_customers lc 
        ON cd.member_id = lc.member_id
    left join {{ ref('_member_overrides') }} mo2
        on cd.member_id = mo2.member_id
    left join (
        select
            member_id
            , MAX(COALESCE(pick_up_date, '9999-12-31')) as last_pickup
        from {{ ref('fact_loop') }}
        where delivery_date <= CURRENT_DATE
        group by 1
        ) as lp --last_pickup
        ON cd.member_id = lp.member_id
    left join first_order o1
        ON cd.member_id = o1.member_id
    left join deliver_pickup_dates dpd
        ON cd.member_id = dpd.member_id
    left join {{ref('_member_type_inputs')}} mti
        on cd.member_id = mti.member_id
    left join {{ ref('members_with_hacked_annual_membership') }} as mwham
        on cd.member_id = mwham.member_id
    where COALESCE(mo2.is_blacklist_member, 0) != 1 and 
        cd.rn = 1
)
select
    base.member_id
    , mim.hubspot_customer_id
    , email
    , first_name
    , last_name
    , substring(last_name, 1, 1) AS last_initial
    , membership_start_dt
    , CASE
        WHEN member_status = 'Churned' and membership_type = 'annual' THEN DATEADD('d', 370, last_membership_payment_ts)
        WHEN member_status = 'Churned' and membership_type = 'monthly' THEN DATEADD('d', 35, last_membership_payment_ts)
        WHEN member_status = 'Churned' THEN src_last_pickup_dt
    END as membership_end_dt
    , membership_type
    , contact_created_ts
    , hs_analytics_source
    , hs_analytics_source_data
    , child_1_dob
    , child_2_dob
    , child_3_dob
    , youngest_child_dob
    , number_of_children
    , expecting_at_sign_up
    , city
    , address
    , zip
    , state
    , is_loopshare
    , loop_share_ts
    , first_item_order_dt
    , first_delivery_dt
    , last_pick_up_dt
    , CASE
        when state ilike '%ca%' then 'SF'
        when state ilike '%ny%' or state ilike '%new%'  or state ilike '%connecticut%' then 'NYC'
        else 'Other'
    END as ops_location
    , reason_for_canceling
    , first_membership_purchase_ts
    , last_membership_payment_ts
    , last_product_payment_ts
    , ct_active_product_payments
    , ct_purchased_skus
    , is_ever_purchased_snoo
    , ct_active_products_loops
    , ct_items_with_scheduled_delivery
    , ct_items_with_scheduled_pickup
    , ct_skus_in_loop_master
    , is_only_has_snoo_loop
    , first_delivery_date
    , is_only_has_snoo_payments
    , member_status
    , member_sub_status
    , member_status_detail
from base
LEFT JOIN (
    select 
        member_id, 
        MAX(src_id) as hubspot_customer_id
    from {{ref('member_id_map')}}
    where src = 'hubspot'
    group by 1
) mim
    on mim.member_id = base.member_id 
