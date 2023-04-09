-- show data on checkout dropouts
with cart_abandoners AS (
    select
        session_id
        , session_start_ts as cart_session_start
        , max((src_tbl = 'checkout_started')::int) as started_checkout
        , max((src_tbl = 'order_completed')::int) as order_completed
    from {{ref('web_activity')}} as fwa
    where not is_internal
    group by 1, 2
    having started_checkout = 1 and order_completed = 0
), base_url as (
select
	fwa.session_id
	, fwa.session_start_ts as start_ts
	, row_number() over (partition by session_id, session_start_ts order by "timestamp" desc) as rk
	, context_page_url 
from {{ref('web_activity')}} fwa
join cart_abandoners using(session_id)
where context_page_url is not null
), final_url as (
	select * from base_url where rk = 1
)
select 
	fwa.session_id
	, fwa.session_start_ts
    , split_part(fu.context_page_url , '?', 1) as final_url 
	, fwa.membership_state
	, max(case when event = 'checkout_step_viewed' then "timestamp" else null end) as last_checkout_step_viewed_ts
	, max(case when event = 'checkout_step_completed' then "timestamp" else null end) as last_checkout_step_completed_ts
	, max("timestamp") as last_step_ts
	, sum(case when event = 'checkout_step_completed' then 1 else 0 end) as checkout_steps_completed
from {{ref('web_activity')}} fwa
join cart_abandoners using(session_id)
left join final_url fu using(session_id)
group by 1, 2, 3, 4