select
    id as line_item_id
    , order_id
    , case when applied_discounts != '[]' then replace(split_part(split_part(applied_discounts, ',', 4), ':', 2), '\'', '') else null end as discount_code
    , case when applied_discounts != '[]' then replace(split_part(split_part(applied_discounts, ',', 2), ':', 2), '\'', '')::decimal else 0.00 end as discount_amount
    , case when applied_discounts != '[]' then replace(split_part(split_part(applied_discounts, ',', 3), ':', 2), '\'', '') else null end as discount_name
    , case when applied_discounts != '[]' then replace(replace(replace(split_part(split_part(applied_discounts, ',', 5), ':', 2), '\'', ''), ']', ''), '}', '')  else null end as discount_target
from {{source('bigcommerce', 'line_items')}} 