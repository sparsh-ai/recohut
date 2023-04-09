SELECT
    (ROW_NUMBER() OVER () - 1)::int AS ordinal
FROM
    stl_scan
LIMIT 50