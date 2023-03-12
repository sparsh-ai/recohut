/*select h.id as hubspot_contact_id,
    h.email,
    md5(lower(trim(coalesce(sh.email, bc.email)))) as email_key,
    dm.member_id,
    st.id as stripe_customer_id,
    bc.id as bigcommerce_customer_id,
    sh.id as shopify_id,
    case when d.email is null then false else true end as duplicate,
    d.member_id as duplicate_member_id
from {{ source('hubspot', 'contacts') }} h left join
    {{ ref('dim_members') }} dm on h.email = dm.email left join
    {{ source('stripe', 'customers') }} st on h.email = st.email left join
    {{ source('bigcommerce', 'customers') }} bc on h.email = bc.email left join
    {{ source('shopify', 'customers') }} sh on h.email = sh.email left join
    {{ ref('_duplicates') }} d on h.email = d.email*/

with max_bigc as (
    select max(id) as id
    from {{ source('bigcommerce', 'customers') }}
    group by email
)

select hc.id as hubspot_id,
    shc.id as shopify_id,
    bcc.id as bigcommerce_id,
    stc.id as stripe_id,
    coalesce(shopify_id, bigcommerce_id::text) as quickbase_id,
    dm.member_id,
    hc.email
from {{ref('dim_members')}} dm left join 
    {{ref('member_id_map')}} hmim on dm.member_id = hmim.member_id and hmim.src = 'hubspot' left join
    {{ source('hubspot', 'contacts') }} hc on hmim.src_id = hc.id left join
    {{ref('member_id_map')}} shmim on dm.member_id = shmim.member_id and shmim.src = 'shopify' left join
    {{ source('shopify', 'customers') }} shc on shmim.src_id = shc.id left join
    {{ref('member_id_map')}} bcmim on dm.member_id = bcmim.member_id and bcmim.src = 'bigcommerce' left join
    max_bigc bcc on bcmim.src_id = bcc.id left join
    {{ref('member_id_map')}} stmim on dm.member_id = stmim.member_id and stmim.src = 'stripe' left join
    stripe_fivetran.customer stc on stmim.src_id = stc.id 