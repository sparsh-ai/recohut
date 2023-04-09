select
    dateadd('day', ordinal, '2020-12-01'::date)::date as date
from {{ ref('numbers') }}
