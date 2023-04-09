select
    min(date_diff('d', delivery_date, pick_up_date)) as min_duration
    , max(date_diff('d', delivery_date, pick_up_date)) as max_duration
    , avg(date_diff('d', delivery_date, pick_up_date)) as avg_duration
    , median(date_diff('d', delivery_date, pick_up_date)) as median_duration
    , count(*) as observations
from dw.fact_loop
where sku = '6650335723691'
    and pick_up_date is not null

select
    delivery_date
    , date_diff('d', delivery_date, CURRENT_DATE)
    , count(*)
from dw.fact_loop
where sku = '6650335723691'
    and pick_up_date is  null
group by 1, 2
order by 1
