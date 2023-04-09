with fct_orders as (
    select * from {{ ref('fct_orders') }}
)

select
    "order_id",
    sum("payment_value")
from fct_orders
group by "order_id"
having sum("payment_value") < 0