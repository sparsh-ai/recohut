SELECT * FROM trials;

SELECT * FROM tickets limit 10;

SELECT * FROM parking_tickets_count limit 10;

SELECT * FROM tickets_transformd limit 10;

DROP TABLE `tickets_transformd_new`;

CREATE EXTERNAL TABLE `tickets_transformd_new` (
    ticket_date STRING,
    infraction_description STRING,
    officer_name FLOAT,
    set_fine_amount FLOAT
)
STORED AS PARQUET
LOCATION 's3://glue-studio-blog-684199068947/parking_tickets_count/'
tblproperties ("parquet.compression"="SNAPPY");

SELECT * FROM tickets_transformd_new LIMIT 10;