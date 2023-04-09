with membership_amounts_before as (	
    select rmi.member_id,
		sum(fli.price) as membership_price,
        count(distinct dp.sku) as membership_distinct_product_count,
		count(*) as membership_line_item_count
	from dbarnes_dev.rebate_member_ids rmi inner join
		dw.fact_order fo on rmi.member_id = fo.member_id inner join
		dw.fact_line_item fli on fo.order_id = fli.order_id inner join 
		dw.dim_product dp on fli.sku = dp.sku	
	where 
		(dp.product_name ilike '%membership%' or
		dp.product_name ilike '%plan') and 
		fo.order_ts >= '2022-01-07' and 
		fo.order_ts <= '2022-04-07'
    group by 1
),
membership_amounts_after as (	
    select rmi.member_id,
		sum(fli.price) as membership_price,
        count(distinct dp.sku) as membership_distinct_product_count,
		count(*) as membership_line_item_count
	from dbarnes_dev.rebate_member_ids rmi inner join
		dw.fact_order fo on rmi.member_id = fo.member_id inner join
		dw.fact_line_item fli on fo.order_id = fli.order_id inner join 
		dw.dim_product dp on fli.sku = dp.sku	
	where 
		(dp.product_name ilike '%membership%' or
		dp.product_name ilike '%plan') and 
		fo.order_ts >= '2022-04-07' and 
		fo.order_ts <= '2022-07-07'
    group by 1
),
orders_before_base as (
	select fo.member_id,
		(datediff(month, min(fo.order_ts)::date - 6, max(fo.order_ts::date)-6))+1 as num_months_before,
		sum(fli.price) as total_order_gross_before,
		count(distinct fli.sku) as distinct_skus_before,
		count(fli.sku) as total_line_items_before
	from dbarnes_dev.rebate_member_ids rmi left join 
		dw.fact_order fo on rmi.member_id = fo.member_id and order_ts <= '2022-04-07' and order_ts >= '2022-01-07' left join 
		dw.fact_line_item fli on fo.order_id = fli.order_id
	group by 1
),
orders_before as (
	select obb.member_id,
        (total_order_gross_before - coalesce(membership_price, 0))/nullif(num_months_before,0) as mrr_before,
        distinct_skus_before - coalesce(membership_distinct_product_count, 0) as number_items_before,
        mrr_before/nullif(number_items_before,0) as avg_mrr_item_before,
		num_months_before
	from orders_before_base obb left join
        membership_amounts_before mab on obb.member_id = mab.member_id	
),
orders_after_base as (
	select fo.member_id,
		(datediff(month, min(fo.order_ts)::date - 6, max(fo.order_ts::date)-6))+1 as num_months_after,
		sum(fli.price) as total_order_gross_after,
		count(distinct fli.sku) as distinct_skus_after,
		count(fli.sku) as total_line_items_after
	from dbarnes_dev.rebate_member_ids rmi left join 
		dw.fact_order fo on rmi.member_id = fo.member_id and order_ts <= '2022-07-07' and order_ts > '2022-04-07' left join 
		dw.fact_line_item fli on fo.order_id = fli.order_id
	group by 1
),
orders_after as (
	select oab.member_id,
        (total_order_gross_after - coalesce(membership_price, 0))/nullif(num_months_after,0) as mrr_after,
        distinct_skus_after - coalesce(membership_distinct_product_count, 0) as number_items_after,
        mrr_after/nullif(number_items_after,0) as avg_mrr_item_after,
		num_months_after
	from orders_after_base oab left join
        membership_amounts_after maa on oab.member_id = maa.member_id 
),
final as (select coalesce (ob.member_id, oa.member_id),
	num_months_before,
	num_months_after,
	mrr_before,
	mrr_after,
	number_items_before,
	number_items_after,
	avg_mrr_item_before,
	avg_mrr_item_after
from orders_before ob full outer join 
	orders_after oa on ob.member_id = oa.member_id)

select * from final