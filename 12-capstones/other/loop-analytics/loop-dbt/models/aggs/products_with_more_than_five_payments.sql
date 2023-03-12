with valid_line_items as (
    select
        line_item_id
        , sum(net_sales)
    from dw.fact_transaction
    group by 1
    having sum(net_sales) > 0
)
, base as (
    select
        member_id
        , sku
        , min(transaction_ts) as first_payment_ts
        , max(transaction_ts) as last_payment_ts
        , count(*) as times_paid
    from dw.fact_transaction
    inner join valid_line_items
        using(line_item_id)
    where product_name not ilike '%membership%'
        and product_name not ilike '%plan%'
    group by 1, 2
)
, bin_lookup as (
    select
        member_id
        , sku
        , min(bin) as bin_best_guess
        , count(distinct bin) as distinct_bins
    from dw.fact_loop
    group by 1, 2
)
select
    dim_members.member_id
    , dim_members.first_name
    , dim_members.last_initial
    , dim_members.membership_type
    , dim_members.member_status
    , dim_members.member_status_detail
    , product_name
    , first_payment_ts
    , last_payment_ts
    , times_paid
    , bin_best_guess
    , distinct_bins
from base
inner join dw.dim_product
using(sku)
inner join dw.dim_members
using(member_id)
left join bin_lookup
    on base.member_id = bin_lookup.member_id
    and base.sku = bin_lookup.sku
where times_paid >= 5
order by times_paid desc, last_payment_ts desc