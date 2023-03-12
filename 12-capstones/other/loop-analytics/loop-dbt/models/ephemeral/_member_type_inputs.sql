--member_type_inputs
-- Section 1: Getting all the transaction parts together
with updated_non_refunded_line_items as (
    select 
        nrli.line_item_id
        , nrli.order_id
        , nrli.price
        , nrli.quantity
        , nrli.sku
        , nrli.total_discount
        , fo.member_id
        , fo.order_ts
        -- TODO make this part of the table
        , case
            when dp.product_name ilike '%membership%'
                or dp.product_name ilike '%plan'
                or (
                    -- these are hacks where we've fully refunded somebody's membership and then 
                    -- manually gone in there and put in a "positive refund" to account for their membership
                    mwham.member_id is not null
                    AND fts.sales_type = 'return'
                    AND fts.quantity = 0
                    AND fts.product_name is null
                    AND fts.gross_sales >= 80
                )
            then true
            else false
          end as is_membership
        , CASE 
            WHEN dp.product_name ILIKE '%gift card%' 
            THEN TRUE 
            WHEN NULLIF(dp.product_name, '') IS NOT NULL  -- don't set one way or another when product isn't known (e.g. draft orders)
            THEN FALSE 
          END AS is_gift_card
        , false AS is_registry_product
        -- this logic is so that we exclude items that were refunded
        -- i.e. if a membership transactions was refunded, the last relevant one was the preceding one
    from {{ ref('non_refunded_line_items') }} nrli
    left join {{ref('fact_order')}} fo on 
        nrli.order_id = fo.order_id
    left join {{ref('dim_product')}} dp on 
        nrli.sku = dp.sku
    left join {{ ref('fact_transaction_shopify') }} fts
        on nrli.line_item_id = fts.line_item_id
    left join {{ ref('members_with_hacked_annual_membership') }} as mwham
        on fo.member_id = mwham.member_id
)
, snoo_group_snoos as (
    select distinct sku
    from {{ ref('dim_product') }}
    where product_name ilike '%snoo%'
)
, snoo_collapsed_ft AS (
    -- Collapse "snoo group" products; replace sku as SNOOGROUP
    select distinct
        member_id
        , is_membership
        , 'SNOOGROUP' as sku
        , order_ts
        , is_gift_card
        , is_registry_product
    from updated_non_refunded_line_items unrli
    inner join snoo_group_snoos sgs
        on unrli.sku::text = sgs.sku::text

    union all

    select distinct
        member_id
        , is_membership
        , unrli.sku::text
        , order_ts
        , is_gift_card
        , is_registry_product
    from updated_non_refunded_line_items as unrli
    left join snoo_group_snoos sgs
        on unrli.sku::text = sgs.sku::text
    where sgs.sku is null

)
, influencers as (
    select distinct member_id
    from {{ ref('fact_order') }}
    where discount_code ilike '%MOMCREATORS%'
)
, transaction_base as (
    select
        member_id
        , min(case when is_membership then order_ts end) as first_membership_purchase_ts
        , max(case when is_membership then order_ts end) as last_membership_payment_ts
        , max(case when not is_membership then order_ts end) as last_product_payment_ts
        , count(distinct
                case
                    when not is_membership and order_ts >= DATEADD('d', -35, CURRENT_DATE)
                    then sku
                end
            ) as ct_active_product_payments
        , count(distinct
                case
                    when not is_membership
                    then sku
                end
            ) as ct_purchased_skus
        , max((sku = 'SNOOGROUP')::int) as is_ever_purchased_snoo
        , avg(sct.is_gift_card::int) as avg_purchased_gift_card
        , avg(is_registry_product::int) as avg_purchased_registry_product
        , max(case when i.member_id is not null then 1 else 0 end) as is_influencer
    from snoo_collapsed_ft sct
    left join influencers i
        using(member_id)
    group by 1
)
--- Section 2: Getting all the loop stats together
, loop_snoo_sku as (
    -- collapse to snoo group
    select
        member_id
        , delivery_date
        , pick_up_date
        , case
            when sgs.sku is not null
            then 'SNOOGROUP'
            else fl.sku
          end as sku
    from  {{ ref('fact_loop') }} fl
    left join snoo_group_snoos sgs
        on fl.sku::text = sgs.sku::text
)
, loop_base as (
    select
        member_id
        , count(
            distinct
            case
                when delivery_date <= CURRENT_DATE
                    and coalesce(pick_up_date, '9999-12-31') >= CURRENT_DATE
                then sku
            end
        ) as ct_active_products_loops
        , count(
            distinct
            case
                when delivery_date > CURRENT_DATE
                then sku
            end
        ) as ct_items_with_scheduled_delivery
        , count(
            distinct
            case
                when pick_up_date > CURRENT_DATE
                then sku
            end
        ) as ct_items_with_scheduled_pickup
        , count(
            distinct
            case
                when delivery_date <= CURRENT_DATE
                then sku
            end
        ) as ct_skus_in_loop_master
        , min(
            case
                when sku = 'SNOOGROUP' then 1
                else 0
            END
        ) AS is_only_has_snoo_loop
        , min(delivery_date) as first_delivery_date
    from loop_snoo_sku
    group by 1
)
-- Step 3: Combine 'em
, base as (
    select 
        *
        , (is_ever_purchased_snoo = 1 and ct_purchased_skus = 1)::int is_only_has_snoo_payments
    from transaction_base
    full outer join loop_base
    using(member_id)
)
select *
from base