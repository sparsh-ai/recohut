with member_dates as (
    select
        first_txn_ts::date as dt
        , sum(case when membership_type = 'annual' then 1 else 0 end) as annual_members
        , sum(case when membership_type = 'monthly' then 1 else 0 end) as monthly_members
        , sum(case when membership_type in ('per-item', 'influencer') then 1 else 0 end) as other_members
        , sum(case when membership_type = 'gift-card-buyer' then 1 else 0 end) as gifters
        , sum(case when membership_type = 'registry-product-buyer' then 1 else 0 end) as registry_buyers
    from {{ ref('dim_members') }}
    left join (
        select 
            member_id
            , min(transaction_ts) as first_txn_ts
        from {{ ref('fact_transaction') }}
        group by 1
    ) as txns
    using(member_id)
    group by 1
)
select
    dim_date.daydate
    , nvl(annual_members, 0) as annual_members
    , nvl(monthly_members, 0) as monthly_members
    , nvl(other_members, 0) as other_members
    , nvl(gifters, 0) as gifters
    , nvl(registry_buyers, 0) as registry_buyers
from {{ ref('dim_date') }}
left join member_dates
    on dim_date.daydate = member_dates.dt
where dim_date.daydate >= '2021-05-01'
    and dim_date.daydate <= CURRENT_DATE
order by 1
