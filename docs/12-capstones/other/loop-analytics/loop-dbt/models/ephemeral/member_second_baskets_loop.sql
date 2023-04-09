SELECT *
from {{ ref('member_baskets_loop')}}
where dense_rank = 2