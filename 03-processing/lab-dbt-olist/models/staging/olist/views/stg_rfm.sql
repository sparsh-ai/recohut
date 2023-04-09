
with pure_rfm as (
select sc."customer_unique_id", count(distinct so."order_id") frequency, 
sum(sp."payment_value") monetary, CURRENT_DATE - MAX(DATE(so."order_purchase_timestamp")) recency,
MAX(DATE(so."order_purchase_timestamp")) last_order_date
from {{ ref('stg_orders') }} so left join {{ ref('stg_payments') }} sp  on so."order_id"=sp."order_id"
left join {{ ref('stg_customers') }} sc on so."customer_id" = sc."customer_id"
where so."order_status" != 'canceled'
group by sc."customer_unique_id"
having sum(sp."payment_value") > 0
),
transformed_rfm as (

select "customer_unique_id",
		ntile(5) over(order by "recency" desc) recency_score,
		ntile(5) over(order by "frequency") frequency_score
		from pure_rfm 
),
final as (
	select "customer_unique_id", "recency_score", "frequency_score",
	case
		when ("recency_score" = 1 or "recency_score" = 2) AND ("frequency_score" = 1 or "frequency_score" = 2) then 'Hibernating'
		when ("recency_score" = 1 or "recency_score" = 2) AND ("frequency_score" = 3 or "frequency_score" = 4)  then 'At_Risk'
		when ("recency_score" = 1 or "recency_score" = 2) AND ("frequency_score" = 5)  then 'Cant_Loose'
		when ("recency_score" = 3) AND ("frequency_score" = 1 or "frequency_score" = 2)  then 'About_to_Sleep'
		when ("recency_score" = 3) AND ("frequency_score" = 3) then 'Need_Attention'
		when ("recency_score" = 3 or "recency_score" = 4) AND ("frequency_score" = 4 or "frequency_score" = 5) then 'Loyal_Customers'
		when ("recency_score" = 4) AND ("frequency_score" = 1) then 'Promising'
		when ("recency_score" = 5) AND ("frequency_score" = 1) then 'New_Customers'
		when ("recency_score" = 4 or "recency_score" = 5) AND ("frequency_score" = 2 or "frequency_score" = 3) then 'Potential_Loyalists'
		when ("recency_score" = 5) AND ("frequency_score" = 4 or "frequency_score" = 5) then 'Champions'
		
	end segment
	from transformed_rfm 
)
select * from final