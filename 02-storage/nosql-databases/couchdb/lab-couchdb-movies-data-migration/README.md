# Couchdb Movies Data Migration

## Objective

NoSQL Data Migration from flat files into Cassandra and CouchDB

## Introduction

Your company prides itself in being able to efficiently handle data in any format on any database on any platform. Analysts in the office need to work with data on different databases, and with data in diferent formats. While they ae good at analyzing dats, they count on you to be able to move data from external sources into various databases, move data from one type of database to another, and be able to run basic queries on various databases.

You need to do the following tasks:

- Replicate a remote database into your instance
- Create an index for key "director, on the movies database using the HTTP API
- Wites query to find all movies directed by Richard Gage using the HTTP API
- Create an index for key "title’ onthe database movies using the HTTP API
- Writes query to list only the keys year and director for the movie “Top Dog” using the HTTP API
- Export the data from movies database into a file named movies.json
- Import movies.json into mongodb server into a database named entertainment and collection named movies
- Writes mongodb query to find the year in which most number of movies were released
- Wites mongodb query to find the count of movies released after the year 1999
- Write a query to find out the average votes for movies released in 2007
- Export the fields_id, title, year, rating and director from movie collection into a file named partial_dats.csv
- Import partial.csv into cassandra server into a keyspace named entertainment and table named movies
- Write a cql query to count the number of rows in the movies table
- Create an index for the column rating in the movies table using cql
- Write a cql query to count the number of movies that are rated 'G'