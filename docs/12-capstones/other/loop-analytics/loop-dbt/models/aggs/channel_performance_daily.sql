
with
fwa_agg as (
	select
		fwa.session_start_ts::date as "date"
		, count(distinct session_id) as sessions
		, COUNT(distinct case when src_tbl = 'product_added' then session_id end) as adds_to_cart
		, COUNT(distinct case when src_tbl = 'product_viewed' then session_id end) as product_viewed
		, COUNT(distinct case when src_tbl = 'checkout_started' then session_id end) as checkout_started
		, COUNT(distinct case when src_tbl = 'order_completed' then session_id end) as order_completed
	from {{ref('web_activity')}} fwa
	where fwa.is_internal != True 
	and fwa.membership_state = 'new'
	group by 1
),
ad_perf as (
	select
		CASE 
			WHEN ad_source = 'facebook' AND ny = 'yes' THEN 'facebook - NY'
			WHEN ad_source = 'facebook' AND (ny = 'no' or ny is null) then 'facebook - SF'
			ELSE ad_source
		END as ad_source
		, "date"::date as "date"
		, SUM(spend) as spend
		, SUM(impressions) as impressions
		, SUM(clicks) as clicks
	from {{ref('fact_ad_performance')}} fap 
	left join {{ref('dim_ad')}} da
		using(ad_id)
	left join (
		select distinct 
			ad_name
		from {{source('googlesheets', 'fb_ad_key')}}
		where 
			(snoop = 'yes')
			and nullif(ad_name, '') is not null
	) fb_filter
	on fb_filter.ad_name = da.ad_name
	and da.ad_source = 'facebook'
	where fb_filter.ad_name is null
	group by 1, 2
	order by 2
), 
ad_agg as (
	select
		*
		, spend / nullif((impressions / 1000.00), 0) as CPM
		, spend / nullif(clicks, 0) as CPC
		, clicks / nullif(impressions, 0) as CTR
	from ad_perf
),
pivoted_agg as (
	select
		dd.daydate as "date"
		, SUM(case when ad_source = 'facebook - SF' then spend else 0 end) as facebook_SF_spend
		, SUM(case when ad_source = 'facebook - SF' then impressions else 0  end) as facebook_SF_impressions
		, SUM(case when ad_source = 'facebook - SF' then clicks else 0  end) as facebook_SF_clicks
		, SUM(case when ad_source = 'facebook - SF' then CPM else 0  end) as facebook_SF_CPM
		, SUM(case when ad_source = 'facebook - SF' then CPC else 0  end) as facebook_SF_CPC
		, SUM(case when ad_source = 'facebook - SF' then CTR else 0  end) as facebook_SF_ctr
		, SUM(case when ad_source = 'facebook - NY' then spend else 0 end) as facebook_NY_spend
		, SUM(case when ad_source = 'facebook - NY' then impressions else 0  end) as facebook_NY_impressions
		, SUM(case when ad_source = 'facebook - NY' then clicks else 0  end) as facebook_NY_clicks
		, SUM(case when ad_source = 'facebook - NY' then CPM else 0  end) as facebook_NY_CPM
		, SUM(case when ad_source = 'facebook - NY' then CPC else 0  end) as facebook_NY_CPC
		, SUM(case when ad_source = 'facebook - NY' then CTR else 0  end) as facebook_NY_ctr
		, SUM(case when ad_source = 'adwords_search' then spend else 0  end) as google_search_spend
		, SUM(case when ad_source = 'adwords_search' then impressions else 0  end) as google_search_impressions
		, SUM(case when ad_source = 'adwords_search' then clicks else 0  end) as google_search_clicks
		, SUM(case when ad_source = 'adwords_search' then CPM else 0  end) as google_search_CPM
		, SUM(case when ad_source = 'adwords_search' then CPC else 0  end) as google_search_CPC
		, SUM(case when ad_source = 'adwords_search' then CTR else 0  end) as google_search_CTR
		, SUM(case when ad_source = 'adwords_display' then spend else 0  end) as google_display_spend
		, SUM(case when ad_source = 'adwords_display' then impressions else 0  end) as google_display_impressions
		, SUM(case when ad_source = 'adwords_display' then clicks else 0  end) as google_display_clicks
		, SUM(case when ad_source = 'adwords_display' then CPM else 0  end) as google_display_CPM
		, SUM(case when ad_source = 'adwords_display' then CPC else 0  end) as google_display_CPC
		, SUM(case when ad_source = 'adwords_display' then CTR else 0  end) as google_display_CTR
	from (
		select daydate
		from 
		{{ref('dim_date')}} 
		where daydate BETWEEN '2021-09-21' AND CURRENT_DATE
	) dd
	left join fwa_agg fwa
		on fwa.date = dd.daydate
    left join ad_agg
        on ad_agg.date = dd.daydate
	group by 1
)
select 
	pivoted_agg.*
	, facebook_NY_spend + facebook_SF_spend as facebook_total_spend
	, facebook_NY_clicks + facebook_SF_clicks as facebook_total_clicks
	, facebook_NY_impressions + facebook_SF_impressions as facebook_total_impressions
	, (facebook_total_spend * 1.00) / (nullif((facebook_total_impressions / 1000.00), 0) * 1.00) as facebook_total_CPM		
	, (facebook_total_spend * 1.00) / (nullif(facebook_total_clicks, 0) * 1.00) as facebook_total_CPC
	, (facebook_total_clicks * 1.00) / ( nullif(facebook_total_impressions, 0) * 1.00) as facebook_total_CTR
    , facebook_NY_spend + facebook_SF_spend + google_search_spend + google_display_spend as paid_marketing_spend
    , (facebook_NY_spend + facebook_SF_spend + google_search_spend + google_display_spend) / NULLIF(fwa_agg.adds_to_cart, 0) as cost_per_atc
	, kbd.new_members 
	, dc.order_discounts
    , (facebook_NY_spend + facebook_SF_spend + google_search_spend + google_display_spend) / NULLIF(kbd.new_members, 0) as paid_marketing_CAC
    , (facebook_NY_spend + facebook_SF_spend + google_search_spend + google_display_spend) / NULLIF(kbd.new_members, 0) + coalesce(dc.order_discounts, 0) as CAC
	, kbd.new_annual_members 
	, kbd.new_monthly_members
	, COALESCE(snoo.first_order_snoo_only, 0) as first_order_snoo_only
	, fwa_agg.sessions
	, fwa_agg.adds_to_cart
    , fwa_agg.product_viewed
    , fwa_agg.checkout_started
    , fwa_agg.order_completed
from pivoted_agg
left join {{ref('kpis_by_day')}} kbd 
	using("date")
left join fwa_agg
	using("date")
left join (
	select
	membership_start_dt::date as "date"
	, SUM(first_order_snoo_only) as first_order_snoo_only
	from {{ref('member_agg_shopify')}} ma
	group by 1
) snoo
	using("date")
left join (
	select
		order_ts::DATE as order_date
		, SUM(order_discounts) as order_discounts
	from {{ref('fact_order_shopify')}}
	group by 1
) dc
	on dc.order_date = pivoted_agg.date
order by "date"