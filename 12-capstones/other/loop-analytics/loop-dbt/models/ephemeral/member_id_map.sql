With segment_source as (
	select
		anonymous_id as src_id
		, 'segment' as src
		, email_key 
		, member_id 
		, timestamp
	from  (
		select 
			anonymous_id
			, user_id
			, md5(lower(trim(customers.email))) as email_key
			, coalesce(_duplicates.member_id, md5(lower(trim(customers.email)))) as member_id
			, timestamp
		from shopify_littledata_prod.identifies i 
		inner join shopify.customers
			on customers.id  = i.user_id
		LEFT JOIN {{ ref('_duplicates') }}
			on src = 'shopify' and customers.id = src_id
	)

	union all

	select
		anonymous_id as src_id
		, 'segment' as src
		, md5(lower(trim(email))) as email_key 
		, md5(lower(trim(email))) as member_id 
		, timestamp
	from  loop_baby_prod.identifies
	
	union all

	select
		anonymous_id as src_id
		, 'segment' as src
		, email_key 
		, member_id 
		, timestamp
	from  (
		select 
			pages.anonymous_id
			, pages.user_id
			, md5(lower(trim(customers.email))) as email_key
			, coalesce(_duplicates.member_id, md5(lower(trim(customers.email)))) as member_id
			, timestamp
		from landing_pages.pages 
		inner join shopify.customers
			on customers.id  = pages.user_id
		LEFT JOIN {{ ref('_duplicates') }}
			on src = 'shopify' and customers.id = src_id
	)

	union all 

	select
		anonymous_id as src_id
		, 'segment' as src
		, email_key 
		, member_id 
		, timestamp
	from  (
		select 
			pages.anonymous_id
			, pages.user_id
			, md5(lower(trim(customers.email))) as email_key
			, coalesce(_duplicates.member_id, md5(lower(trim(customers.email)))) as member_id
			, timestamp
		from landing_pages.pages 
		inner join bigcommerce.customers
			on customers.id  = pages.user_id
		LEFT JOIN {{ ref('_duplicates') }}
			on src = 'shopify' and customers.id = src_id
	)
), segment_row as (
	select
		*
        , row_number() over(
            partition by src_id
            ORDER BY timestamp
        ) AS rn
	FROM segment_source
)

SELECT
	src_id::text
	, src
	, email_key 
	, member_id 
FROM segment_row
where rn = 1

UNION ALL

select
    id::text as src_id
    , 'shopify' as src
    , md5(lower(trim(customers.email))) as email_key
    , coalesce(_duplicates.member_id, md5(lower(trim(customers.email)))) as member_id
from shopify.customers
  LEFT JOIN {{ ref('_duplicates') }}
    on src = 'shopify' and id = src_id

union all

select
    id::text as src_id
    , 'hubspot' as src
    , md5(lower(trim(contacts.email))) as email_key
    , coalesce(_duplicates.member_id, md5(lower(trim(contacts.email)))) as member_id
from hubspot.contacts
  LEFT JOIN {{ ref('_duplicates') }}
    on src = 'hubspot' and id = src_id

union all

select
    id::text as src_id
    , 'bigcommerce' as src
    , md5(lower(trim(customers.email))) as email_key
    , coalesce(_duplicates.member_id, md5(lower(trim(customers.email)))) as member_id
from bigcommerce.customers
  LEFT JOIN {{ ref('_duplicates') }}
    on src = 'bigcommerce' and id = src_id

union all

select
    id::text as src_id
    , 'stripe' as src
    , md5(lower(trim(customers.email))) as email_key
    , coalesce(_duplicates.member_id, md5(lower(trim(customers.email)))) as member_id
from stripe.customers
  LEFT JOIN {{ ref('_duplicates') }}
    on src = 'stripe' and id = src_id