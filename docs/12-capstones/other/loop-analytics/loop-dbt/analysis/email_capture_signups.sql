with emails as (
    select distinct email
    from shopify_littledata_prod.identifies
    where email is not null
        and nullif(user_id, '') is null
)
select distinct
    identifies.email
    , user_id
    , membership_start_dt
from shopify_littledata_prod.identifies
inner join emails
using(email)
left join dw.dim_members
on identifies.email = dim_members.email
where user_id is not null
