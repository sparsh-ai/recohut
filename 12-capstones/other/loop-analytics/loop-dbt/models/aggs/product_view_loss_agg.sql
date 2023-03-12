-- shows the product view mix of sessions that looked at products but didn't start checkout
with cart_abandoners AS (
    select
        session_id
        , session_start_ts
        , max((src_tbl = 'product_viewed')::int) as product_viewed
        , max((src_tbl = 'checkout_started')::int) as checkout_started
    from {{ref('web_activity')}} as fwa
    where not is_internal
    group by 1, 2
)
select
    dim_product.product_name
    , dim_product.sku
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
    where src_tbl = 'product_viewed'
) as prod
    using(session_id)
inner join {{ref('dim_product')}}
    on product_id = dim_product.sku

