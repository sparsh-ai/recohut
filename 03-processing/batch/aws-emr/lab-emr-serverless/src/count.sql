SET hive.cli.print.header=true;
SET hive.query.name=TaxiTrips;

Select count(*) as count from nytaxitrip;