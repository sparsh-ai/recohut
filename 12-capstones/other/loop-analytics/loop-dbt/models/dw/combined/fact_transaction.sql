select 	
    order_id
	, order_number
	, subscription_id
	, transaction_id
	, refund_id
	, connection_id
    , member_id
	, transaction_ts
	, order_type
	, sales_type
	, sales_channel
	, gross_sales
	, discounts
	, returns
	, net_sales
	, taxes
	, total_sales
    , true as replatform 
from {{ ref('fact_transaction_rp') }}

union

select 
	t.order_id::text
	, t.order_number::text
	, null as subscription_id
	, t.transaction_id::text
	, t.refund_id
	, t.connection_id
    , t.member_id
	, t.transaction_ts
	, t.order_type
	, t.sales_type
	, t.sales_channel
	, t.gross_sales
	, t.discounts
	, t.returns
	, t.net_sales
	, t.taxes
	, t.total_sales
    , false as replatform 
from {{ref('fact_transaction_shopify')}} t 