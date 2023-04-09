select
    MD5('facebook-' || id) as ad_id
    , MD5('facebook-' || account_id ) as ad_account_id
    , MD5('facebook-' || campaign_id) as campaign_id
    , MD5('facebook-' || adset_id) as audience_id
    , 'facebook' as ad_source
    , name as ad_name
    , status
    , id as source_ad_id
    , campaign_id as source_campaign_id
    , snoop
    , ny
from {{ source('facebook_ads', 'ads') }}
left join (
        select *
            , row_number() over(partition by ad_name) as rn
        from {{source('googlesheets', 'fb_ad_key')}} 
    ) AS fak
    on ads.name = fak.ad_name
    and rn = 1
where account_id = '378349750281931'

UNION ALL

select
    MD5('google-' || a.id) as ad_id
    , MD5('google-' || a.adwords_customer_id ) as ad_account_id
    , MD5('google-' || ag.campaign_id) as campaign_id
    , MD5('google-' || a.ad_group_id) as audience_id
    , CASE	
        when a."type" ilike '%search%' then 'adwords_search'
        when a."type" ilike '%image%' then 'adwords_display'
    end as ad_source
    , ag.name as ad_name -- name only on ag group or higher level
    , a.status
    , a.id as source_ad_id
    , ag.campaign_id as source_campaign_id
    , NULL as snoop
    , NULL as ny
from {{ source('google_ads', 'ads') }} a
left join {{ source('google_ads', 'ad_groups')}} ag
    on a.ad_group_id = ag.id