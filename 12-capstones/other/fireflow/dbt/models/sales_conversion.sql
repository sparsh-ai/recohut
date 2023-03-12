{{ config(materialized='table') }}

with sales_count as (
  select f.sales_id, count(*) as total_sales
  from {{ source('staging', 'Fact_Table') }} f 
  group by f.sales_id
)
select f.sales_id, s.name, s.age, s.sex, count(f.sales_id) / sc.total_sales as sales_conversion
from {{ source('staging', 'Fact_Table') }} f
join sales_count sc
on sc.sales_id = f.sales_id
join {{ source('staging', 'salesperson') }} s
on f.sales_id = CAST(s.id AS STRING)
where f.y = 'yes'
group by 1, 2, 3, 4, sc.total_sales
order by 2 desc
