create table if not exists dwh_final.dim_city (
	id uuid unique,
	country_id varchar,
	state_id varchar,
	city_name varchar,
	zip_code varchar,
	primary key(id),
	foreign key(country_id, state_id) references dwh_final.dim_state(country_id, state_code),
	constraint city_zip unique (city_name, zip_code)
);

insert into dwh_final.dim_city (
  id, 
  country_id,
  state_id,
  city_name,
  zip_code
)
(
select 
	gen_random_uuid() as id, 
	case when country_id is null then 'others' else country_id end as country_id,
	case when state_id is null or state_id = '' then 'others' else state_id end as state_id,
	city_name,
	zip_code
from (
	-- get data from companies
	select distinct 
		offices_country_code as country_id,
		offices_state_code as state_id,
		offices_city as city_name,
		offices_zip_code as zip_code
	from dwh_final.companies
	
	union
	
	-- get data from zips
	select distinct 
		'others' as country_id,
		state as state_id,
		city as city_name,
		zip as zip_code
	from dwh_final.zips
	) stu
	where (city_name is not null and city_name != '')
		and (zip_code is not null and zip_code != '')
)
on conflict (city_name, zip_code) do nothing 
;
