drop table if exists dwh_final.fact_daily_avg_currency; 

create table if not exists dwh_final.fact_daily_avg_currency (
	currency_id varchar,
	currency_name varchar,
	day date,
	avg_rate float
);

insert into dwh_final.fact_daily_avg_currency (
	currency_id,
	currency_name,
	day,
	avg_rate
)
(
select 
	currency_id,
	currency_name,
	"timestamp"::date as day,
	avg(rate) as avg_rate
from dwh_final.topic_currency
where "timestamp"::date = {{ macros.ds }}::date - interval '1 day'
group by currency_id , currency_name , "timestamp"::date
order by currency_id
)
;
