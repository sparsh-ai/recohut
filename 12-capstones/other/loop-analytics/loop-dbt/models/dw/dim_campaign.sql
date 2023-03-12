select
    MD5('google-' || id) as campaign_id
    , id as src_campaign_id
    , name as campaign_name
    , start_date as start_dt
    , end_date as end_dt
    , status
    , b.ad_source_type as channel_id
from {{ source('google_ads', 'campaigns') }} a
left join (
	select
		c.id campaign_id
		, MAX(case 
			when a."type" ilike '%search%' then 'adwords_search'
			when a."type" ilike '%image%' then 'adwords_display'
		end) as ad_source_type
	from {{source('google_ads','campaigns')}} c
	left join {{source('google_ads','ad_groups')}} ag 
		on c.id  = ag.campaign_id 
	left join {{source('google_ads','ads')}} a 
		on a.ad_group_id = ag.id 
	group by 1
) b
on a.id = b.campaign_id

union all

select
    md5('facebook-' || id) as campaign_id
    , id as src_campaign_id
    , name as campaign_name
    , start_time as start_dt
    , stop_time as end_dt
    , effective_status as status
    , 'facebook_ads' as channel_id
from {{ source('facebook_ads', 'campaigns') }}
