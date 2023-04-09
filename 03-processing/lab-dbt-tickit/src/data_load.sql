create table users(
	userid integer not null distkey sortkey,
	username char(8),
	firstname varchar(30),
	lastname varchar(30),
	city varchar(30),
	state char(2),
	email varchar(100),
	phone char(14),
	likesports boolean,
	liketheatre boolean,
	likeconcerts boolean,
	likejazz boolean,
	likeclassical boolean,
	likeopera boolean,
	likerock boolean,
	likevegas boolean,
	likebroadway boolean,
	likemusicals boolean);
            
create table venue(
	venueid smallint not null distkey sortkey,
	venuename varchar(100),
	venuecity varchar(30),
	venuestate char(2),
	venueseats integer);

create table category(
	catid smallint not null distkey sortkey,
	catgroup varchar(10),
	catname varchar(10),
	catdesc varchar(50));

create table date(
	dateid smallint not null distkey sortkey,
	caldate date not null,
	day character(3) not null,
	week smallint not null,
	month character(5) not null,
	qtr character(5) not null,
	year smallint not null,
	holiday boolean default('N'));

create table event(
	eventid integer not null distkey,
	venueid smallint not null,
	catid smallint not null,
	dateid smallint not null sortkey,
	eventname varchar(200),
	starttime timestamp);

create table listing(
	listid integer not null distkey,
	sellerid integer not null,
	eventid integer not null,
	dateid smallint not null  sortkey,
	numtickets smallint not null,
	priceperticket decimal(8,2),
	totalprice decimal(8,2),
	listtime timestamp);
    
create table sales(
	salesid integer not null,
	listid integer not null distkey,
	sellerid integer not null,
	buyerid integer not null,
	eventid integer not null,
	dateid smallint not null sortkey,
	qtysold smallint not null,
	pricepaid decimal(8,2),
	commission decimal(8,2),
	saletime timestamp);

copy users from 's3://wysde-datasets/tickitdb/allusers_pipe.txt' 
iam_role default
delimiter '|' region 'us-east-1';

copy venue from 's3://wysde-datasets/tickitdb/venue_pipe.txt' 
iam_role default
delimiter '|' region 'us-east-1';

copy category from 's3://wysde-datasets/tickitdb/category_pipe.txt' 
iam_role default
delimiter '|' region 'us-east-1';

copy date from 's3://wysde-datasets/tickitdb/date2008_pipe.txt' 
iam_role default
delimiter '|' region 'us-east-1';

copy event from 's3://wysde-datasets/tickitdb/allevents_pipe.txt' 
iam_role default
delimiter '|' timeformat 'YYYY-MM-DD HH:MI:SS' region 'us-east-1';

copy listing from 's3://wysde-datasets/tickitdb/listings_pipe.txt' 
iam_role default
delimiter '|' region 'us-east-1';

copy sales from 's3://wysde-datasets/tickitdb/sales_tab.txt'
iam_role default
delimiter '\t' timeformat 'MM/DD/YYYY HH:MI:SS' region 'us-east-1';