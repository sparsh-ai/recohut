create table if not exists dwh_final.dim_state (
	id uuid unique,
	country_id varchar,
	state_code varchar,
	primary key(id),
	foreign key(country_id) references dwh_final.dim_country(country_code),
	constraint country_state unique (country_id, state_code)
);

insert into dwh_final.dim_state (
  id, 
  country_id,
  state_code
)
(
select 
	gen_random_uuid() as id, 
	case when country_id is null then 'others' else country_id end as country_id,
	state_code
from (
	-- get data from companies
	select distinct 
		offices_country_code as country_id,
		offices_state_code as state_code
	from dwh_final.companies
	
	union
	
	-- get data from zips
	select distinct 
		'others' as country_id,
		state as state_code
	from dwh_final.zips
	) stu
where state_code is not null and state_code != ''
)
on conflict (country_id, state_code) do nothing 
;
