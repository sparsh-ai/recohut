{{ config(materialized='table') }}

with sales_count as (
  select s.city, count(*) as total_sales_city
  from {{ source('staging', 'Fact_Table') }} f 
  join {{ source('staging', 'salesperson') }} s
  on f.sales_id = CAST(s.id AS STRING)
  group by 1
)
select s.city, total_sales_city, count(*) / sc.total_sales_city as sales_conversion
from {{ source('staging', 'Fact_Table') }} f
join {{ source('staging', 'salesperson') }} s
on f.sales_id = CAST(s.id AS STRING)
join sales_count sc
on sc.city = s.city
where f.y = 'yes'
group by 1, 2, sc.total_sales_city
order by 3 desc, 2 desc