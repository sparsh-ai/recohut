{% macro create_udf_collect_ec_products_map() -%}

    CREATE OR REPLACE FUNCTION udf_collect_ec_products_map(MP variant)
        RETURNS array
        LANGUAGE JAVASCRIPT
    AS
    $$
        const toString = v => (v ? `${v}`.trim() : null) || null;
        const toFloat = v => Math.trunc(parseFloat(toString(v)) * 1000) / 1000;
        const toInt = v => parseInt(toString(v));
        const db = {
            id: ['id', toString],
            va: ['variant', toString],
            nm: ['name', toString],
            br: ['brand', toString],
            qt: ['quantity', toFloat],
            pr: ['price', toFloat],
            ps: ['position', toInt],
            ca: ['category', toString],
        };

        const products = [];
        for (let [ek, ev] of Object.entries(MP)) {
            const res = ek.toLowerCase().trim().match(/^pr(?<idx>\d+)(?<key>.*)/);
            if (res) {
                const { idx, key } = res.groups;
                const [ map_k, map_fn ] = db[key] || [idx, toString];
                const value = map_fn(ev);
                if (value !== null) {
                    products[idx] = products[idx] || {};
                    if (db[key]) { // Standard field
                        products[idx][map_k] = value;
                    }
                    products[idx].raw = products[idx].raw || {};
                    products[idx].raw[key] = value;
                }
            }
        }
        return products.filter(i => i);
    $$
    ;

{%- endmacro %}
