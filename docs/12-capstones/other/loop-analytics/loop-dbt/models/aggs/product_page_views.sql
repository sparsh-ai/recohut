with member_views as (
	select 
		master_user_id
		, count(1) page_views
	from {{ref('web_activity')}}
	where src_tbl = 'pages'
	and master_user_id is not null
	group by master_user_id 
)
select 
	fwa.master_user_id
	, session_id 
	, product_id_master
	, original_timestamp::date as created_at
	, case when context_page_referrer like '%loop%' then true else false end as loop_referred
	, member_views.page_views
from {{ref('web_activity')}} fwa
left join member_views
	on member_views.master_user_id = fwa.master_user_id 
