{{ config(materialized='table') }}

select tc.id, tc.training_course, avg(date_diff(st.end_date, st.start_date, DAY)) avg_course_spend_days
from {{ source('staging', 'sales_training') }} st
join {{ source('staging', 'training_course') }} tc
on st.training_id = tc.id
where lower(st.status) = 'finished'
group by 1, 2
order by 3 desc