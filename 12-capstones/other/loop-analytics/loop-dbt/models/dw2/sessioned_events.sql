
with compiled_user_id_frontend as (
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'checkout_started')}}
    union
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'page_viewed')}}
    union
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'zip_code_validation')}}
    union
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'product_list_viewed')}}
    union
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'product_clicked')}}
    union
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'checkout_completed')}}
    union 
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'order_completed')}}
    union
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'be_signed_up')}}
    union
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'checkout_delivery_address')}}
    union
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'checkout_completion_failed')}}
    union
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'checkout_membership_selection')}}
    union
    select id,
        coalesce(loop_customer_id, user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'password_changed')}}
),
add_loop_id_to_tracks_frontend as (
    select tr.*,
        coalesce(cuif.loop_customer_id, tr.user_id) as loop_customer_id
    from {{source('loop_baby_prod', 'tracks')}} tr left join
        compiled_user_id_frontend cuif on tr.id = cuif.id
),
add_loop_id_to_records_frontend as (
	select distinct x.anonymous_id,
		y.loop_customer_id
	from add_loop_id_to_tracks_frontend x inner join
		add_loop_id_to_tracks_frontend y on x.anonymous_id = y.anonymous_id and y.loop_customer_id is not null
    where x.loop_customer_id is null
), 
all_events_frontend AS (
    SELECT 
        tr.*
        , coalesce(product_clicked.product_id::text, product_removed.product_id::text, case when right(tr.context_page_url, 3) between 0 and 999 then right(tr.context_page_url, 3) else null end) as product_id
        , COALESCE(tr.loop_customer_id, alitrf.loop_customer_id, tr.anonymous_id) AS master_user_id
    FROM add_loop_id_to_tracks_frontend tr
    left join {{source('loop_baby_prod','product_clicked')}} product_clicked using(id)
    left join {{source('loop_baby_prod','product_removed')}} product_removed using(id)
    left join add_loop_id_to_records_frontend alitrf on tr.anonymous_id = alitrf.anonymous_id
), 
full_tracks as (
    select anonymous_id,
        context_campaign_content,
        context_campaign_medium,
        context_campaign_name,
        context_campaign_source,
        context_ip,
        context_library_name,
        context_library_version,
        context_locale,
        context_page_path,
        context_page_referrer,
        context_page_search,
        context_page_title,
        context_page_url,
        null as context_traits_address_city,
        null as context_traits_address_postal_code,
        null as context_traits_address_state,
        null as context_traits_email,
        null as context_traits_first_name,
        null as context_traits_last_name,
        null as context_traits_phone,
        null as context_traits_timestamp,
        null as context_traits_user_id,
        context_user_agent,
        event,
        event_text,
        id,
        original_timestamp,
        received_at,
        sent_at,
        "timestamp",
        user_id,
        uuid,
        uuid_ts,
        product_id,
        master_user_id,
        'frontend' as frontend_backend
    from all_events_frontend
    where event not in ('customer_created', 'order_completed', 'order_created', 'be_signed_up')    
    union
    select null as anonymous_id,
        null as context_campaign_content,
        null as context_campaign_medium,
        null as context_campaign_name,
        null as context_campaign_source,
        context_traits_ip as context_ip,
        context_library_name,
        context_library_version,
        null as context_locale,
        null as context_page_path,
        null as context_page_referrer,
        null as context_page_search,
        null as context_page_title,
        context_page_url,
        context_traits_address_city,
        context_traits_address_postal_code,
        context_traits_address_state,
        context_traits_email,
        context_traits_first_name,
        context_traits_last_name,
        context_traits_phone,
        context_traits_timestamp,
        context_traits_user_id,
        context_user_agent,
        event,
        event_text,
        id,
        original_timestamp,
        received_at,
        sent_at,
        "timestamp",
        user_id,
        uuid,
        uuid_ts,
        null as product_id,
        user_id as master_user_id,
        'backend' as frontend_backend
    from {{source('loop_server_prod', 'tracks')}} 
    where event != 'checkout_started'
),
session_maker as (
    select *
        , case
            when datediff('s',
                    lag(timestamp) over(
                        partition by master_user_id
                        order by timestamp
                    ),
                    timestamp
                ) > 60 * 30
                OR lag(timestamp) over(
                        partition by master_user_id
                        order by timestamp
                    ) IS NULL
            then id end as session_id_tmp
    from full_tracks
), 
sessioned_events as (
    select sm.*
        , coalesce(bu.email_address, fu.email, m.email) as email
        , last_value(sm.session_id_tmp IGNORE NULLS) over (order by sm.master_user_id, timestamp rows unbounded preceding) as session_id
    from session_maker sm left join
        {{source('loop_baby_prod', 'users')}} fu on sm.user_id = fu.id and sm.frontend_backend = 'frontend' left join
        {{source('loop_server_prod', 'users')}} bu on sm.user_id = bu.id and sm.frontend_backend = 'backend' left join
        {{ref('members')}} m on sm.master_user_id = m.loop_customer_id
)
select *
from sessioned_events

