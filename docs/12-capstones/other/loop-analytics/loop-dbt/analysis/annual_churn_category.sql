with asc_membership_purchases as (
	select o.member_id, 
		o.order_id,
		o.order_ts,
		p.product_name,
		row_number() over(partition by member_id order by order_ts) as rn
	from dw.fact_order o inner join
		dw.fact_line_item li on o.order_id = li.order_id inner join 
		dw.dim_product p on li.sku = p.sku
	where (p.product_name ilike '%plan' or 
		p.product_name ilike '%membership' or 
		p.product_name ilike '%monthly%' or 
		p.product_name ilike '%annual%') 
),
desc_membership_purchases as (
	select 
		o.member_id, 
		o.order_id,
		o.order_ts,
		p.product_name,
		row_number() over(partition by member_id order by order_ts desc) as rn
	from dw.fact_order o inner join
		dw.fact_line_item li on o.order_id = li.order_id inner join 
		dw.dim_product p on li.sku = p.sku
	where (p.product_name ilike '%plan' or 
		p.product_name ilike '%membership' or 
		p.product_name ilike '%monthly%' or 
		p.product_name ilike '%annual%')
),
only_annual_membership_purchases as (
	select o.member_id, 
		min(o.order_ts) as initial_annual_membership_purchase_dt,
		max(o.order_ts) as most_recent_annual_membership_purchase_dt,
		count(distinct o.order_id) as number_annual_purchases
	from dw.fact_order o inner join
		dw.fact_line_item li on o.order_id = li.order_id inner join 
		dw.dim_product p on li.sku = p.sku
	where  p.product_name ilike '%annual%'
	group by 1
)
select 
	oamp.member_id,
	dm.first_name,
	dm.last_name,
	dm.email,
	dm.membership_start_dt,
	coalesce(dm.membership_end_dt, hc.annual_membership_end_date) as membership_end_dt,
	amp.order_ts as initial_membership_purchase_dt,
	case when amp.product_name ilike '%annual%' then 'Annual' 
		when amp.product_name ilike '%montly%' then 'Monthly'
		else 'Other' end as initial_membership_type,
	dmp.order_ts as most_recent_membership_purchase_dt,
	case when dmp.product_name ilike '%annual%' then 'Annual'
		when dmp.product_name ilike '%monthly%' then 'Monthly'
		else 'Other' end as most_recent_membership_type,
	oamp.initial_annual_membership_purchase_dt,
	oamp.most_recent_annual_membership_purchase_dt,
	case when most_recent_membership_purchase_dt < sysdate-370 and most_recent_membership_type = 'Annual' then 'Annual to Possible Churn'
		when most_recent_membership_purchase_dt < sysdate-33 and most_recent_membership_type = 'Monthly' then 'Annual to Monthly then Possible Churn'
		when most_recent_membership_purchase_dt >= sysdate-370 and most_recent_membership_type = 'Annual' then 'Annual Renewal'
		when most_recent_membership_purchase_dt >= sysdate-33 and most_recent_membership_type = 'Monthly' then 'Annual to Monthly Active'
		else 'Other' end as annual_churn_category
from only_annual_membership_purchases oamp inner join
	asc_membership_purchases amp on oamp.member_id = amp.member_id and amp.rn = 1 inner join 
	desc_membership_purchases dmp on oamp.member_id = dmp.member_id and dmp.rn = 1 inner join 
	dw.dim_members dm on oamp.member_id = dm.member_id left join 
    {{ref('member_id_map')}} mim on dm.member_id = mim.member_id and src='hubspot' left join
    hubspot.contacts hc on mim.src_id = hc.id
where oamp.initial_annual_membership_purchase_dt < sysdate-370