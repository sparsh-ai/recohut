-- param `field`: The name of the field you want zeroed out for manual orders

-- see LOOP-238 for context
-- basically there's a way to manually mark orders as paid when no money changes hands
-- rob & ops determined that the correct treatment for these was zeroing them out
-- using hardcoded order_numbers because rob had to provide them
{% macro manual_order_zeroing(field) %}
CASE
    WHEN order_number in (
            '5134',
            '5136',
            '5359',
            '5366',
            '5367',
            '5368',
            '5370',
            '5482',
            '5484',
            '5485',
            '5486',
            '5532',
            '5535',
            '5537',
            '5539',
            '5568',
            '5569',
            '5572',
            '5598',
            '5693',
            '5694',
            '5695',
            '5702',
            '5704',
            '5705',
            '5738',
            '5765',
            '5827',
            '5829',
            '5963',
            '5992',
            '5993',
            '5996',
            '5998',
            '6007',
            '6036',
            '6069',
            '6071',
            '6072',
            '6076',
            '6147',
            '6157',
            '6162',
            '6163',
            '6167',
            '6186',
            '6187',
            '6218',
            '6222',
            '6256',
            '6388',
            '6390',
            '6391',
            '6419'
        )
    THEN 0
    ELSE {{ field }}
    END 
{% endmacro %}
