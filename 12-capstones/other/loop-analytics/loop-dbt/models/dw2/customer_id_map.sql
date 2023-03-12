select
    a.loopcustomerid as loop_customer_id,
    a.authprovidercustomerid as auth_provider_customer_id,
    a.bigcommercecustomerid as bigcommerce_customer_id,
    a.stripeCustomerId as stripe_customer_id,
    case when a.shopifyCustomerId = '' then s.id else a.shopifyCustomerId end as shopify_customer_id,
    a.boldCustomerId as bold_customer_id,
    a.hubspotCustomerId as hubspot_customer_id,
    coalesce(shopify_customer_id, a.bigcommercecustomerid, a.stripeCustomerId, a.hubspotCustomerId) as quickbase_customer_id,
    md5(lower(coalesce(de.primary_email, a.emailAddress))) as member_id,
    a.emailAddress as email
from {{source ('dw2', 'account')}} a left join
    {{source('shopify', 'customers')}} s on a.emailaddress = s.email left join
    {{ref('_duplicate_emails')}} de on a.emailaddress = de.secondary_email 