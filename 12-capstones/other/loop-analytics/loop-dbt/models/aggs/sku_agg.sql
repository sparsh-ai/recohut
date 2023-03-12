with inventory_count as (
	select
		sku
		, count(bin) as inventory_count
		, avg(case when purchase_date > '2019-01-01' then datediff('d', purchase_date::date , fl.first_del_date::date) end) as dwell_time
        , sum(case when purchase_date > '2019-01-01' then datediff('d', purchase_date::date , fl.first_del_date::date) end) as total_dwell_time
		, sum(case when purchase_date > '2019-01-01' then datediff('d', purchase_date::date, CURRENT_DATE) end) as total_inventory_days
        , total_inventory_days - total_dwell_time as non_dwell_inventory_days
	from {{ref('dim_item')}} di
	left join (select bin, min(delivery_date) as first_del_date from {{ref('fact_loop_shopify')}} group by 1) fl
		using(bin)
	group by 1
),
active_count as (
	select
		sku
		, count(distinct case when current_date >= delivery_date and (current_date <= pick_up_date or pick_up_date is null) and bin != '' then bin end) as active_count
		, count(1) as loop_numbers
		, AVG(case when pick_up_date is not null then datediff('d', delivery_date, pick_up_date) end) as avg_completed_loop_duration
		, AVG(case when pick_up_date is null then datediff('d', delivery_date, current_date) end) as avg_active_loop_duration
		, count(distinct member_id) as total_members
		, SUM(case when current_date >= delivery_date and (current_date <= pick_up_date or pick_up_date is null) then avg_price else 0 end) as current_mrr
		, sum(case when delivery_date < current_date then datediff('d', delivery_date, COALESCE(fl.pick_up_date , CURRENT_DATE))end ) as total_rental_days
		from  {{ref('fact_loop_shopify')}} fl
	group by 1
), total_rev as (
	select
		sku
		, sum(revenue) as total_revenue
	from  {{ref('fact_daily_revenue_shopify')}}  fdr
	where fdr."date" < current_date
	group by 1
)
select
	ic.sku
	, dp.product_name
	, ic.inventory_count
	, ac.active_count
	, ac.loop_numbers
	, ac.avg_completed_loop_duration
	, ac.avg_active_loop_duration
	, ic.dwell_time
	, tr.total_revenue
	, total_members
	, current_mrr
	, total_inventory_days
	, total_rental_days
    , non_dwell_inventory_days
from (select distinct sku, product_name from {{ref('dim_product_shopify')}} ) dp
left join inventory_count ic using(sku)
left join active_count ac using(sku)
left join total_rev tr using(sku)