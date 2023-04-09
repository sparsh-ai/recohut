with cart_abandoners AS (
    select
        session_id
        , session_start_ts
        , max((src_tbl = 'checkout_started')::int) as started_checkout
        , max((src_tbl = 'order_completed')::int) as order_completed
    from {{ref('web_activity')}} as fwa
    where not is_internal
    group by 1, 2
)
select
    products.product_name
    , products.sku
    , prod.timestamp
    , prod.session_start_ts
    , prod.master_user_id as user_id
    , prod.context_page_url
    , prod.session_id
    , prod.user_first_session_channel_id
    , prod.session_channel_id
from cart_abandoners
inner join (
    select *
    from {{ref('web_activity')}} as fwa
    where src_tbl = 'product_added'
) as prod
    using(session_id)
inner join {{ref('products')}}
    on product_id = products.sku
where started_checkout = 1
    and order_completed = 0