with base as (
    select c.id,
         row_number() over(partition by s.id order by c.received_at) as rn
    from {{ source('stripe', 'charges') }} c inner join
        {{ source('stripe', 'invoices')}} i on c.invoice_id = i.id inner join
        {{ source('stripe', 'subscriptions') }} s on s.id = i.subscription_id
)

select c.*
from base b inner join
    {{ source('stripe', 'charges') }} c on b.id = c.id
where b.rn != 1