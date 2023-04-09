with members_with_membership_refunds as (
    select distinct member_id
    from {{ ref('fact_transaction_shopify') }}
    where quantity < 0
        and (
            product_name ilike '%membership%'
            or product_name ilike '%plan'
        )
)
select distinct ft.member_id
from {{ ref('fact_transaction_shopify') }} ft
inner join members_with_membership_refunds mwmr
using(member_id)
where sales_type = 'return'
    and quantity = 0
    and product_name is null
    and gross_sales >= 80