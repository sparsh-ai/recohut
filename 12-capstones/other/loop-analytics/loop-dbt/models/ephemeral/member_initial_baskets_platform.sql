SELECT *
from {{ ref('member_baskets_platform')}}
where dense_rank = 1