--If no discount is given it should be equal to zero 
--Otherwise it will be negative

select *
  from {{ ref('fct_orders') }}  
 where item_discount_amount > 0