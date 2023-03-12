select
  s.member_id
  , d.date
  , s.sku
  , null as membership_type
  , (net_price * 12.0) / 365.0 AS revenue
from {{ ref('dates') }} as d
left join {{ref('dim_subscriptions') }}  as s
  on d.date >= s.start_dt
  and d.date < NVL(s.end_dt, '9999-12-31')
WHERE d.date <= CURRENT_DATE

union all

select
  s.member_id
  , d.date
  , null as sku
  , membership_type
  , case
        when membership_type = 'annual'
        then price / 365.0
        else (price * 12.0) / 365.0
    end AS revenue
from {{ ref('dates') }} as d
left join {{ref('dim_membership') }}  as s
  on d.date >= s.start_dt
  and d.date < s.end_dt
where membership_type != 'per-item'
    and d.date <= CURRENT_DATE