WITH base AS (
    select
        sessioned_events.*
        -- precision here is day instead of exact time because our historical member start date wasn't recorded in a real system
        , case
            when  m.member_start_date < sessioned_events.received_at - 1 and m.membership_status != 'Churned'
            then 'existing'
            else 'new'
        end as membership_state
        , anonymous_id not ilike '%little%' as is_client_trackable
        , CASE WHEN context_ip in (
                '201.191.218.0',
                '181.194.148.0',
                '99.47.182.26',
                '99.47.182.0',
                '181.194.203.0',
                '181.194.203.124',
                '72.48.253.143',
                '24.90.212.159',
                '65.244.125.2',
                '201.191.218.242',
                '201.191.218.171',
                '76.243.7.122',
                '50.237.220.98',
                '76.14.124.233',
                '96.237.110.193',
                '73.112.54.153',
                '73.92.171.62',
                '181.194.203.0',
                '181.194.204.132',
                '181.194.204.0'
        )
         OR sessioned_events.email ilike '%loop.baby%'
         OR sessioned_events.email ilike '%dvx.ventures%'
         OR sessioned_events.email = 'cherie.salonga@gmail.com'
         OR anonymous_id = '6bcbee53-07da-4e27-b1c3-3ffeed7d901f'
         THEN TRUE
         ELSE FALSE
        END
        AS is_internal
        -- session first value attributes
        , first_value(context_campaign_name ignore nulls) over(partition by session_id order by sessioned_events.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING ) as session_campaign_name
        , first_value(context_campaign_content ignore nulls) over(partition by session_id order by sessioned_events.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as session_campaign_content
        , first_value(context_campaign_source ignore nulls) over(partition by session_id order by sessioned_events.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as session_campaign_source
        , first_value(context_campaign_medium ignore nulls) over(partition by session_id order by sessioned_events.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as session_campaign_medium
        , first_value(context_page_referrer) over(partition by session_id order by sessioned_events.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as session_referrer
        , max(case when context_page_url ilike '%gclid%' then 1 else 0 end) over(partition by session_id) as session_has_gclid
        , first_value(NULLIF(json_extract_path_text(f_parse_url_query_string(coalesce(context_page_url, '')), 'gclid'), '') ignore nulls) over(partition by session_id order by sessioned_events.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as session_gcl_id
        , max(case when context_page_url ilike '%source=referral%' then 1 else 0 end) over(partition by session_id) as is_referral_session
        , min(sessioned_events.timestamp) over(partition by session_id) as session_start_ts
        , max(sessioned_events.timestamp) over(partition by session_id) as session_end_ts
        , min(sessioned_events.timestamp) over(partition by master_user_id) as user_first_visit_ts
        , max(case when context_page_url ilike '%loop-dev%' then 1 else 0 end) over(partition by session_id) as is_dev_session
        , sum(case when src_tbl in ('pages', 'page_viewed') then 1 else 0 end) over(partition by session_id rows between unbounded preceding and unbounded following) as session_page_views
        , CASE
            when regexp_replace(regexp_replace(sessioned_events.context_page_url::text, '.*products/'), '\\?.*') like '%/%' then null
            else regexp_replace(regexp_replace(sessioned_events.context_page_url::text, '.*products/'), '\\?.*')
        end as product_name
        , CASE
            WHEN context_user_agent ilike '%iPhone%' then 'iPhone'
            WHEN context_user_agent ilike '%Android%' then 'Android'
            WHEN context_user_agent ilike '%iPad%' then 'iPad'
            WHEN context_user_agent is not null then 'PC'
        END AS device_type
    from {{ ref('sessioned_events') }} AS sessioned_events
    left join {{ref('members')}} m on sessioned_events.master_user_id = m.loop_customer_id
),
campaigns as (
    select
        campaign_id
        , src_campaign_id 
        , channel_id
    from {{ref('dim_campaign')}} dc
)
select base.*
    , CASE -- need to update this instance
        WHEN session_has_gclid = 1 AND gads.channel_id is not null
        THEN gads.channel_id     
        WHEN session_has_gclid = 1 AND gads.channel_id is null
        THEN 'adwords_search'
        WHEN is_referral_session = 1
        THEN 'referral'
        WHEN session_campaign_source ilike '%facebook%' and session_campaign_medium = 'cpc' and session_referrer ilike '%insta%'
        THEN 'instagram_ads'
        WHEN session_campaign_source ilike '%facebook%' and session_campaign_medium = 'cpc'
        THEN 'facebook_ads'
        WHEN session_campaign_source = 'bayareaparent'
        THEN 'sc_bayareaparent'
        WHEN session_campaign_source = 'ironhorsemothersclub'
        THEN 'sc_ironhorsemothersclub'
        WHEN session_campaign_source = 'midpeninsulamultiples'
        THEN 'sc_midpeninsulamultiples'
        WHEN session_campaign_source = 'mtdiablomothersclub'
        THEN 'sc_mtdiablomothersclub'
        WHEN session_campaign_source = 'earthdiaper'
        THEN 'sc_earthdiaper'
        WHEN session_campaign_source = 'cvmc'
        THEN 'sc_cvmc'
        WHEN session_campaign_source = 'TAPJOY'
        THEN 'tapjoy_ads'
        WHEN session_campaign_source = 'sanmateoparentsclub'
        THEN 'sc_sanmateoparentsclub'
        WHEN session_campaign_source = 'liveintent' and session_campaign_medium = 'cpc'
        THEN 'liveintent'
        WHEN session_referrer ILIKE '%google%'
        THEN 'google_search'
        WHEN session_referrer ILIKE '%bing%'
        THEN 'bing_search'
        WHEN session_referrer ILIKE '%facebook%'
        THEN 'facebook_organic'
        WHEN session_referrer ILIKE '%instagram%'
        THEN 'instagram_organic'
        WHEN session_referrer ILIKE '%shareasale%'
        THEN 'shareasale'
        WHEN session_referrer ILIKE '%loop.baby%'
        THEN 'internal'
        ELSE 'direct'
    END AS session_channel_id
	, MAX(case when (regexp_replace(REGEXP_REPLACE(context_page_url, '.*(pf_c_collection=)', ''),'(&).*', '') = '266791190699' or right(context_page_url, 3) = '253') and context_page_referrer = 'https://loop.baby/' then 1 else 0 end) OVER(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as is_snoo_module
	, MAX(case when (regexp_replace(REGEXP_REPLACE(context_page_url, '.*(pf_c_collection=)', ''),'(&).*', '') = '280972066987' or bcp.categories ilike '%58%') and context_page_referrer = 'https://loop.baby/' then 1 else 0 end) OVER(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as is_looptoyboxes_module
	, MAX(case when (regexp_replace(REGEXP_REPLACE(context_page_url, '.*(pf_c_collection=)', ''),'(&).*', '') = '265671147691' or bcp.categories ilike '%40%') and context_page_referrer = 'https://loop.baby/' then 1 else 0 end) OVER(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as is_travel_module
	, MAX(case when (regexp_replace(REGEXP_REPLACE(context_page_url, '.*(pf_c_collection=)', ''),'(&).*', '') = '265670918315' or bcp.categories ilike '%26%') and context_page_referrer = 'https://loop.baby/' then 1 else 0 end) OVER(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as is_0_3month_module
	, MAX(case when regexp_replace(REGEXP_REPLACE(context_page_url, '.*(pf_c_collection=)', ''),'(&).*', '') = '280295047339' and context_page_referrer = 'https://loop.baby/' then 1 else 0 end) OVER(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as is_lovevery_module
	, MAX(case when regexp_replace(REGEXP_REPLACE(context_page_url, '.*(pf_c_collection=)', ''),'(&).*', '') = '266583212203' and context_page_referrer = 'https://loop.baby/' then 1 else 0 end) OVER(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as is_babybjorn_module
	, MAX(case when regexp_replace(REGEXP_REPLACE(context_page_url, '.*(pf_c_collection=)', ''),'(&).*', '') = '266583179435' and context_page_referrer = 'https://loop.baby/' then 1 else 0 end) OVER(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as is_stokke_module
	, MAX(case when regexp_replace(REGEXP_REPLACE(context_page_url, '.*(pf_c_collection=)', ''),'(&).*', '') = '280295211179' and context_page_referrer = 'https://loop.baby/' then 1 else 0 end) OVER(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as is_topprod_module
    , first_value(session_channel_id) over(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS user_first_session_channel_id
    , first_value(session_campaign_name) over(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS user_first_session_campaign_name
    , first_value(session_campaign_content) over(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS user_first_session_campaign_content
    , first_value(session_campaign_source) over(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS user_first_session_campaign_source
    , first_value(session_campaign_medium) over(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS user_first_session_campaign_medium
    , first_value(session_channel_id) over(partition by master_user_id order by base.timestamp desc ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS user_last_session_channel_id
    , first_value(session_campaign_name) over(partition by master_user_id order by base.timestamp desc ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS user_last_session_campaign_name
    , first_value(session_campaign_content) over(partition by master_user_id order by base.timestamp desc ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS user_last_session_campaign_content
    , first_value(session_campaign_source) over(partition by master_user_id order by base.timestamp desc ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS user_last_session_campaign_source
    , first_value(session_campaign_medium) over(partition by master_user_id order by base.timestamp desc ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS user_last_session_campaign_medium
    , coalesce(base.product_id, dp.sku::text) as product_id_raw
    , dp.sku as product_id_master
    , session_page_views = 1 AS is_bounce_session
    , first_value(device_type ignore nulls) OVER(partition by master_user_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as session_device_type
    , split_part(first_value(context_page_url IGNORE NULLS) over(partition by base.session_id order by base.timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING), '?', 1) AS session_first_url
    , CASE 
        WHEN lower(context_campaign_source) = 'facebook' and fb.campaign_id is not null THEN fb.campaign_id
        ELSE gads.campaign_id 
    END as campaign_id
    , ip.region as ip_region
    , ip.country as ip_country
    , ip.city as ip_city
from base
left join {{ref('dim_product')}} dp
    on LOWER(trim(dp.product_name)) = lower(trim(base.product_name))
left join campaigns fb
    on fb.src_campaign_id = base.context_campaign_name
    and fb.channel_id = 'facebook_ads'
left join {{ source('google_ads', 'click_performance_reports') }}
    on base.session_gcl_id = click_performance_reports.gcl_id
left join campaigns gads
    on gads.src_campaign_id = click_performance_reports.campaign_id
    and gads.channel_id in ('adwords_search', 'adwords_display')
left join {{source('ip_api', 'ip_location')}} ip
    on base.context_ip = ip.ip_id
left join {{source('bigcommerce','products')}} bcp 
    on right(base.context_campaign_content, 3) = bcp.id and base.replatform = true
where is_dev_session = 0