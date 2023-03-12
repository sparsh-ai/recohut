select
    id as event_id
    , coalesce(member_id_by_email.member_id, md5(lower(trim(context_traits_email)))) as member_id
    , context_traits_email AS email
    , email_opened.timestamp as event_ts
    , campaign_id
    , campaign_name
from {{ source('klaviyo', 'email_opened') }}
left join {{ref('member_id_by_email')}} as member_id_by_email
  on member_id_by_email.email_key = md5(lower(trim(context_traits_email)))
