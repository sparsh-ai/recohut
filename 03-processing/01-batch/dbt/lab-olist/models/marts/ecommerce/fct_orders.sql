with fct as (

    select 
        sr."customer_unique_id" , sr."segment", 
        sg."geolocation_lat", sg."geolocation_lng", sg."geolocation_city", sg."geolocation_state", 
        so."order_id", date(so."order_purchase_timestamp") order_date,
        sp."payment_value", sp."payment_installments", sp."payment_type" 
    from {{ ref('stg_rfm') }} sr
    left join {{ ref('stg_customers') }} sc on sr."customer_unique_id" = sc."customer_unique_id"  
    left join {{ ref('stg_geolocation') }} sg on sc."customer_zip_code_prefix" = sg."geolocation_zip_code_prefix"
    left join {{ ref('stg_customers') }} sc2 on sr."customer_unique_id" = sc2."customer_unique_id" 
    left join {{ ref('stg_orders') }} so on sc2."customer_id" = so."customer_id" 
    left join {{ ref('stg_payments') }} sp on so."order_id" = sp."order_id"  
)

select * from fct