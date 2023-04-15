# Lab: Generate Trips Data using Stored Procedure

- Step 1 - Connect to the database

```sh
psql --host=database-1.cy8ltogyfgas.us-east-1.rds.amazonaws.com --port=5432 --username=postgres --dbname=sparsh
```

- Step 2 - Run the following commands to create a schema and table for the fictional trip dataset:

```sql
create schema delta_emr_source;
create table delta_emr_source.travel_details (trip_id int PRIMARY KEY,tstamp timestamp, route_id varchar(2),destination varchar(50),source_location varchar(50));
```

- Step 3 - Create the following stored procedure to generate the records for the trip dataset and insert the records into the table:

```sql
create or replace procedure delta_emr_source.insert_records(records int)
language plpgsql
as $$
declare
max_trip_id integer;
begin
--get max trip_id
select coalesce(max(trip_id),1) into max_trip_id from delta_emr_source.travel_details;

--insert records
for i in max_trip_id+1..max_trip_id+records loop
INSERT INTO delta_emr_source.travel_details (trip_id, tstamp, route_id,destination,source_location) values (i, current_timestamp, chr(65 + (i % 10)),(array['Seattle', 'New York', 'New Jersey', 'Los Angeles', 'Las Vegas',
'Tucson', 'Washington DC', 'Philadelphia', 'Miami', 'San Francisco'])[(floor(random() * 10))+1],(array['Seattle', 'New York', 'New Jersey', 'Los Angeles', 'Las Vegas',
'Tucson', 'Washington DC', 'Philadelphia', 'Miami', 'San Francisco'])[(floor(random() * 10))+1]);
end loop;

commit;

raise notice 'Inserted record count - %', records;
end; $$;
```

- Step 4 - Call the preceding stored procedure to insert 20,000 records into the Aurora PostgreSQL database:

```sql
call delta_emr_source.insert_records(20000);
```

- Step 5 - After the stored procedure is complete, verify that the records have been inserted successfully:

```sql
select count(*) from delta_emr_source.travel_details;
```
