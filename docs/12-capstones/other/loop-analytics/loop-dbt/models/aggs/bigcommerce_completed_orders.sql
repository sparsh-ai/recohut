select * 
from {{source('bigcommerce', 'orders')}}
where status_id > 1