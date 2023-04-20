# Lab: Create Fact and Dimension Tables from Denormalized Raw Data

In data warehousing world there are occasions where developers have to reverse engineer model from flat csv files. We will understand this with simple example.

## Login to Postgresql using psql

```sh
psql --host=database-1.cy8ltogyfgas.us-east-1.rds.amazonaws.com --port=5432 --username=postgres --password --dbname=sparsh
```

## Create Schema & Rawdata table

This step is the dump the entire CSV into a ProstgreSQL table so its easier to clean or create Dimension tables.

Here we will be creating 3 schemas called landing, dim and fact. Schemas are very useful in grouping the tables logically.

```sh
create schema elt_landing;
create schema elt_dim;
create schema elt_fact;
```

```sh
create table elt_landing.rawdata (
    name varchar(100)
    ,gender varchar(20)
    ,profession varchar(50)
    ,state varchar(2)
    ,asofdate date
    ,temperature float
    ,pulse int
);
```

Verify the table & schema creation:

```sh
\dt elt_*.*
```

## Import CSV data into Postgres table

```sh
\COPY elt_landing.rawdata FROM 'data.csv' DELIMITER ',' CSV HEADER;
```

Verify the data:

```sh
select count(*) from elt_landing.rawdata;
select * from elt_landing.rawdata limit 10;
```

## Add a surrogate ID colum

> surrogate column means, column with sequence of numbers, generally auto generated.

```sh
alter table elt_landing.rawdata add id serial;
select * from elt_landing.rawdata limit 10;
```

## Identify the possible Dimensions

In this sample we can choose Gender, Name, State, Profession as possible dimensions.

Using select statement generate Dimension tables based on Distinct values.

Creating Gender dimension. Here the sub query returns the distinct genders and using the Windowing Function (row_number()) we are generating a unique ID for each gender.

```sql
create table elt_dim.gender as 
select 
    row_number() Over(order by gender) as genderid
    ,gender 
from 
    (select distinct gender from elt_landing.rawdata) t;
```

Similarly creating other Dimension tables:

```sql
-- Second Query

create table elt_dim.person as
select 
    row_number() Over(order by name) as personid
   ,name 
from 
    (select distinct name from elt_landing.rawdata) t;

-- Third Query

create table elt_dim.profession as
select 
    row_number() Over(order by profession) as professionid
    ,profession 
from 
    (select distinct profession from elt_landing.rawdata) t;

-- Fourth Query

create table elt_dim.state as 
select 
    row_number() Over(order by state) as stateid
    ,state 
from 
    (select distinct state from elt_landing.rawdata) t;
```

Verify the Dimension tables:

```sql
select * from elt_dim.person;
select * from elt_dim.profession;
select * from elt_dim.state;
select * from elt_dim.gender;
```

## Build Fact table based on IDs from Dimension Table

This is the key step which will be generating the necessary Fact table. As the Dimensions are generated from landing data, JOIN will be used to build the fact table.

```sql
create table elt_fact.user
as
select
    r.id
    ,p.personid
    ,g.genderid
    ,pr.professionID
    ,s.stateID
    ,r.asofdate
    ,r.temperature
    ,r.pulse
from
    elt_landing.rawdata r
    JOIN elt_dim.person as p on r.name = p.name
    JOIN elt_dim.gender as g on r.gender = g.gender
    JOIN elt_dim.profession as pr on r.profession = pr.profession
    JOIN elt_dim.state as s on r.state = s.state;
```

In the above query r.id is the Original Surrogate key from elt_landing.rawdata.

Compare and verify the data between elt_landing.rawdata and elt_fact.user table:

```sql
select * from elt_landing.rawdata where id = 1;
```

```sql
select * from elt_fact.user where id = 1;
select * from elt_dim.person where personid = 4;
```

This is the basics, if needed the data can be normalized / modeled further.

Example : asofdate is used as part of Fact, if needed date can be normalized into Year, Month, Day for Snowflake Schema.

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/04-data-modeling/lab-postgres-elt-datamodel)

```
├── [4.1K]  README.md
└── [ 399]  data
    └── [ 303]  data.csv

 4.6K used in 1 directory, 2 files
```