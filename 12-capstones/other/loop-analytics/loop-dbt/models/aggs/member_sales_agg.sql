select
    ft.member_id
    , dm.first_name || ' ' || dm.last_initial as short_name
    , dm.ops_location
    , dm.membership_type
    , dm.member_status
    , dm.membership_start_dt
    , dm.membership_end_dt
    , date_trunc('month', transaction_ts)::date as month
    , sum(net_sales) as net_sales
from {{ref('fact_transaction')}} as ft
left join {{ref('dim_members')}} as dm
using(member_id)
group by 1, 2, 3, 4, 5, 6, 7, 8
order by 1, 2, 3, 4, 5, 6, 7, 8