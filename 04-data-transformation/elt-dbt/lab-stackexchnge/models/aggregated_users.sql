with aggregated_posts_by_user_with_country as (
    with aggregated_posts_by_user as (
        select
            user_poster_id as user_id,
            case
                when sum(comment_count)=0 then 0
                else round(count(distinct post_id) / sum(comment_count), 4)
            end as post_to_comment_ratio,
            round(avg(score),4) as average_post_score,
            current_datetime() as last_updated
        from {{ source('stackoverflow', 'posts') }}
        group by user_poster_id )
    select
        a.user_id,
        u.displayname,
        a.post_to_comment_ratio,
        a.average_post_score,
        u.location,
        lower(trim(regexp_extract(u.location, '([^,]+$)'))) as country,
        a.last_updated
    from aggregated_posts_by_user as a
    left join {{ source('stackoverflow', 'users') }} as u on a.user_id = u.user_id
)
select
    a2.user_id,
    a2.displayname,
    a2.post_to_comment_ratio,
    a2.average_post_score,
    a2.location,
    l.code,
    a2.last_updated
from aggregated_posts_by_user_with_country as a2
inner join {{ ref('country_codes') }} as l on a2.country = lower(trim(l.name))
order by a2.post_to_comment_ratio desc