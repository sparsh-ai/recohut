with base as (
  select
    dim_item.bin
    , dim_item.actual_purchase_price AS purchase_amt
    , purchase_amt / (30.0 * 24.0) AS daily_depreciaton_amount
    , min(fl.delivery_date) as first_delivery_date
    , date_add('d', 30*24, first_delivery_date) as last_depreciation_date
  from {{ ref('dim_item') }}
  left join {{ ref('fact_loop') }} fl
  using(bin)
  group by 1, 2, 3
)
select
  d.date
  , b.bin
  , b.purchase_amt
  , daily_depreciaton_amount as depreciation_expense
  , row_number() over(
    partition by b.bin
    order by d.date
  ) * b.daily_depreciaton_amount AS depreciated_amount
  , b.purchase_amt - depreciated_amount as remaining_value
from {{ ref('dates') }} d
left join base as b
  on d.date >= b.first_delivery_date
  and d.date < b.last_depreciation_date
where first_delivery_date <= CURRENT_DATE
  and first_delivery_date IS NOT NULL