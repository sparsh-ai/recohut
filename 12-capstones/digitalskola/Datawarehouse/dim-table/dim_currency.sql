create table if not exists dwh_final.dim_currency (
	id uuid unique,
	currency_name varchar,
	currency_code varchar unique,
	primary key(id)
);

insert into dwh_final.dim_currency (
  id, 
  currency_name,
  currency_code
)
(
select 
	gen_random_uuid() as id, currency_name, currency_code 
from(
	select distinct currency_name , currency_id as currency_code
	from dwh_final.topic_currency 
	) tc
)
on conflict (currency_code) do nothing
;
