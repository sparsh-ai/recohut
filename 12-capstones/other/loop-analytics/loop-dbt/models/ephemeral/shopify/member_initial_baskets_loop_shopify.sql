SELECT *
from {{ ref('member_baskets_loop_shopify')}}
where dense_rank = 1
