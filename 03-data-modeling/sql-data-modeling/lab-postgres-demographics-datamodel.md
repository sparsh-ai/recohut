**Create Fact and Dimension Tables from Denormalized Raw Data**

In data warehousing world there are occasions where developers have to reverse engineer model from flat csv files. We will understand this with simple example.

**Login to RDS Postgres using psql**

```sh

psql --host=database-1.cy8ltogyfgas.us-east-1.rds.amazonaws.com --port=5432 --username=postgres --password --dbname=sparsh

```

**Create Schema & Rawdata table**

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

**Import CSV data into Postgres table**

```csv

Name,Gender,Profession,state,asOfDate,temperature,pulse

Rachel Green,Female,Designer,NY,2020-11-01,98.4,60

Sheldon Cooper,Male,Physicist,CA,2020-11-05,98.5,70

Penny,Female,Waitress,CA,2020-11-15,99.2,75

George Costanza,Male,Agent,NJ,2020-05-05,98.7,90

Jerry Seinfeld,Male,Comedian,NY,2020-01-01,98.6,65

```

```sh

\COPY elt_landing.rawdata FROM 'data.csv' DELIMITER ',' CSV HEADER;

```

Verify the data:

```sh

selectcount(*) from elt_landing.rawdata;

select* from elt_landing.rawdata limit 10;

```

**Add a surrogate ID column**

> surrogate column means, column with sequence of numbers, generally auto generated.

```sh

alter table elt_landing.rawdata add id serial;

select* from elt_landing.rawdata limit 10;

```

**Identify the possible Dimensions**

In this sample we can choose Gender, Name, State, Profession as possible dimensions.

Using select statement generate Dimension tables based on Distinct values.

Creating Gender dimension. Here the sub query returns the distinct genders and using the Windowing Function (row_number()) we are generating a unique ID for each gender.

```sql

createtableelt_dim.genderas

select

row_number() Over(order by gender) as genderid

    ,gender 

from

    (select distinct gender fromelt_landing.rawdata) t;

```

Similarly creating other Dimension tables:

```sql

-- Second Query


createtableelt_dim.personas

select

row_number() Over(order byname) as personid

   ,name

from

    (select distinctnamefromelt_landing.rawdata) t;


-- Third Query


createtableelt_dim.professionas

select

row_number() Over(order by profession) as professionid

    ,profession 

from

    (select distinct profession fromelt_landing.rawdata) t;


-- Fourth Query


createtableelt_dim.stateas

select

row_number() Over(order bystate) as stateid

    ,state

from

    (select distinctstatefromelt_landing.rawdata) t;

```

Verify the Dimension tables:

```sql

select * fromelt_dim.person;

select * fromelt_dim.profession;

select * fromelt_dim.state;

select * fromelt_dim.gender;

```

**Build Fact table based on IDs from Dimension Table**

This is the key step which will be generating the necessary Fact table. As the Dimensions are generated from landing data, JOIN will be used to build the fact table.

```sql

createtableelt_fact.user

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

JOINelt_dim.personas p onr.name=p.name

JOINelt_dim.genderas g onr.gender=g.gender

JOINelt_dim.professionas pr onr.profession=pr.profession

JOINelt_dim.stateas s onr.state=s.state;

```

In the above query r.id is the Original Surrogate key from elt_landing.rawdata.

Compare and verify the data between elt_landing.rawdata and elt_fact.user table:

```sql

select * fromelt_landing.rawdatawhere id =1;

```

```sql

select * fromelt_fact.userwhere id =1;

select * fromelt_dim.personwhere personid =4;

```

This is the basics, if needed the data can be normalized / modeled further.

Example : asofdate is used as part of Fact, if needed date can be normalized into Year, Month, Day for Snowflake Schema.
