SELECT *
from {{ ref('member_baskets_shopify')}}
where dense_rank = 1
