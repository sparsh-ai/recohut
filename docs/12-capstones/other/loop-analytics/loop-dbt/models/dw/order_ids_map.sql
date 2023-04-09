with invoice_rn as (
    select s.id as subscription_id,
        mim.member_id,
        s.customer_id,
        s.created as subscription_created,
        i.date as invoice_created,
        i.id as invoices_id,
        case when i.date > '2022-07-31' and datediff(min, s.created, i.date) between -5 and 5 then true else false end as initial_invoice
    from {{ source('stripe', 'subscriptions') }} s inner join
        {{ source('stripe', 'invoices') }} i on s.id = i.subscription_id left join
        {{ ref('member_id_map') }} mim on s.customer_id = mim.src_id and mim.src = 'stripe'
),
initial_order_map as (
    select bco.id as bigcommerce_order_id,
        ir.subscription_id
    from invoice_rn ir inner join 
        {{ ref('member_id_map') }} mim on mim.member_id = ir.member_id left join
        {{ ref('bigcommerce_completed_orders') }} bco on mim.src_id = bco.customer_id and 
            mim.src = 'bigcommerce' 
    where initial_invoice = true  and
        datediff(min, bco.date_created, ir.subscription_created) between -5 and 5
)
select ir.*,
    iom.bigcommerce_order_id as initial_bigcommerce_order_id
from invoice_rn ir left join
    initial_order_map iom on ir.subscription_id = iom.subscription_id