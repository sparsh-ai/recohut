select
    MD5('google-' || ad_performance_reports.id) as ad_performance_id
    , MD5('google-' || ads.id) as ad_id
    , date_start as date
    , MD5('google-' || ad_groups.campaign_id) AS campaign_id
    , ads.type as ad_type
    , final_urls
    , cost / 1000000.0 AS spend
    , impressions
    , clicks
from {{source('google_ads', 'ad_performance_reports')}}
left join {{source('google_ads', 'ads')}}
    on ad_performance_reports.ad_id = ads.id
left join {{source('google_ads', 'ad_groups')}}
    on ads.ad_group_id = ad_groups.id

UNION ALL

select
    MD5('facebook-' || i.id) as ad_performance_id
    , MD5('facebook-' || a.id) as ad_id
    , date_start as date
    , MD5('facebook-' || a.campaign_id) AS campaign_id
    , NULL as ad_type
    , url_parameters as final_urls
    , spend
    , impressions
    , link_clicks AS clicks
from {{source('facebook_ads', 'insights')}} i
left join {{source('facebook_ads', 'ads')}} a
    on i.ad_id = a.id
where account_id = '378349750281931'