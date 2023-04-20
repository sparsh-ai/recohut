# Lab: Create a Data Model for a Digital Music Library

## Conceptual Data Model

A conceptual data model is designed with the goal of understanding data in a particular domain. In this example, the model is captured using an Entity-Relationship Diagram (ERD) that documents entity types, relationship types, attribute types, and cardinality and key constraints.

![](https://user-images.githubusercontent.com/62965911/214248175-dac60d1b-68f8-4b8d-9ebd-dbbbbdcc9bfa.png)

The conceptual data model for the digital music library features performers, albums, album tracks and users. A performer has a unique name and is usually classified as a musician or a band. While any performer can have a country affiliation, only a musician can have born and died years and only a band can have a year of when it was founded. An album is uniquely identified by its title and release year, and also features genre information. A track has a number, title and length, and is uniquely identified by a combination of an album title, album year and track number. A user has a unique id and may have other attributes like name. While a performer can release many albums, each album can only belong to one performer. Similarly, an album can have many tracks, but a track always belongs to exactly one album. Finally, a user can listen to many tracks and each track can be played by many users.

## Application workflow

An application workflow is designed with the goal of understanding data access patterns for a data-driven application. Its visual representation consists of application tasks, dependencies among tasks, and data access patterns. Ideally, each data access pattern should specify what attributes to search for, search on, order by, or do aggregation on.

![](https://user-images.githubusercontent.com/62965911/214248044-741b8e20-f4af-4500-9df2-89ba62df2112.png)

The application workflow diagram has five tasks and nine data access patterns. Four out of five tasks are entry-point tasks. In addition, there can be many different paths in this workflow to explore. One possible scenario is described as follows. First, an application shows a user information and her recent music listening history by retrieving data using data access patterns Q8 and Q9. Second, the user searches for a performer with a specific name, which is supported by Q1. Third, the next task retrieves all albums of the found performer using Q2. The resulting list of albums should be sorted using release years, showing the most recent albums first. Finally, the user picks an album and the application retrieves all the album tracks sorted in the ascending order of their track numbers, which requires data access pattern Q7. At this point, the user may decide to listen to a specific track or the whole album, which would be reflected in her listening history. Alternatively, the user may go back to the album selection task or start a new path by looking for performers, albums or tracks. Take a look at the remaining data access patterns and additional paths in this workflow.

## Logical Data model

A logical data model results from a conceptual data model by organizing data into Cassandra-specific data structures based on data access patterns identified by an application workflow. Logical data models can be conveniently captured and visualized using Chebotko Diagrams that can feature tables, materialized views, indexes and so forth.

![](https://user-images.githubusercontent.com/62965911/214248226-dd14a733-1f0d-4ba1-9ccc-dfb44230451a.png)

The logical data model for digital library data is represented by the shown Chebotko Diagram. There are eight tables that are designed to support nine data access patterns. Table performers has single-row partitions with column name being a partition key. This table can efficiently satisfy Q1 by retrieving one partition with one row. Tables albums_by_performer, albums_by_title and albums_by_genre have multi-row partitions. While these tables store the same data about albums, they organize it differently and support different data access patterns. Table albums_by_performer stores one partition per performer with rows representing albums, such that all albums released by a specific performer can be always retrieved from a single partition using Q2. Table albums_by_title supports two data access patterns Q3 and Q4 to retrieve albums based on only album title or both title and year. Q3 may return multiple rows and Q4 may return at most one row. Both Q3 and Q4 only access one partition. Table albums_by_genre is designed to support Q5 that retrieves all albums from a known genre in the descending order of their release years. Next, tables tracks_by_title and tracks_by_album are designed to efficiently support data access patterns Q6 and Q7, respectively. Given a track title, Q6 can retrieve all matching tracks and their information from a single partition of table tracks_by_title. Given an album title and year, Q7 can retrieve all album tracks from a single partition of table tracks_by_album. In case of Q7, returned album tracks are always ordered in the ascending order of track numbers, which is directly supported by the table clustering order. Also, notice that column genre in table tracks_by_album is a static column whose value is shared by all rows in the same partition. This works because genre is an album descriptor and the partition key in this table uniquely identifies an album. Finally, tables users and tracks_by_user are designed to support Q8 and Q9. While the former has single-row partitions and the latter has multi-row partitions, partitions from both tables can be retrieved based on user ids.

## Physical Data Model
A physical data model is directly derived from a logical data model by analyzing and optimizing for performance. The most common type of analysis is identifying potentially large partitions. Some common optimization techniques include splitting and merging partitions, data indexing, data aggregation and concurrent data access optimizations.

![](https://user-images.githubusercontent.com/62965911/214248245-efbe747b-7e8e-4c4c-ae9d-f8ca56d8b3db.png)

The physical data model for digital library data is visualized using the Chebotko Diagram. This time, all table columns have associated data types. In addition, table tracks_by_user has a new column as part of its partition key. The optimization here is to split potentially large partitions by introducing column month, which represents the first day of a month, as a partition key column. Consider that a user who plays music non-stop generates a new row for table tracks_by_user every 3 minutes, where 3 minutes is an average track length estimate. The old design allows partitions to grow over time: 20 rows in an hour, 480 rows in a day, 3360 rows in a week, 13440 rows in 4 weeks, 175200 rows in a non-leap year, and so forth. The new design restricts each partition to only contain at most 14880 rows that can be generated in a month. Our final blueprint is ready to be instantiated in Cassandra.

## Hands-on

### Create Keyspace

```sql
CREATE KEYSPACE music_data
WITH replication = {
  'class': 'SimpleStrategy', 
  'replication_factor': 1 }; 

USE music_data;
```

### Create Tables

Create tables performers, albums_by_performer, albums_by_title, albums_by_genre, tracks_by_title, tracks_by_album, users and tracks_by_user:

```sql
USE music_data;

CREATE TABLE IF NOT EXISTS performers (
  name TEXT,
  type TEXT,
  country TEXT,
  born INT,
  died INT,
  founded INT,
  PRIMARY KEY ((name))
);

CREATE TABLE IF NOT EXISTS albums_by_performer (
  performer TEXT,
  year INT,
  title TEXT,
  genre TEXT,
  PRIMARY KEY ((performer),year,title)
) WITH CLUSTERING ORDER BY (year DESC, title ASC);

CREATE TABLE IF NOT EXISTS albums_by_title (
  title TEXT,
  year INT,
  performer TEXT,
  genre TEXT,
  PRIMARY KEY ((title),year)
) WITH CLUSTERING ORDER BY (year DESC);

CREATE TABLE IF NOT EXISTS albums_by_genre (
  genre TEXT,
  year INT,
  title TEXT,
  performer TEXT,
  PRIMARY KEY ((genre),year,title)
) WITH CLUSTERING ORDER BY (year DESC, title ASC);

CREATE TABLE IF NOT EXISTS tracks_by_title (
  title TEXT,
  album_year INT,
  album_title TEXT,
  number INT,
  length INT,
  genre TEXT,
  PRIMARY KEY ((title),album_year,album_title,number)
) WITH CLUSTERING ORDER BY (album_year DESC, album_title ASC, number ASC);

CREATE TABLE IF NOT EXISTS tracks_by_album (
  album_title TEXT,
  album_year INT,
  number INT,
  title TEXT,
  length INT,
  genre TEXT STATIC,
  PRIMARY KEY ((album_title,album_year),number)
);

CREATE TABLE IF NOT EXISTS users (
  id UUID,
  name TEXT,
  PRIMARY KEY ((id))
);

CREATE TABLE IF NOT EXISTS tracks_by_user (
  id UUID,
  month DATE,
  timestamp TIMESTAMP,
  album_title TEXT,
  album_year INT,
  number INT,
  title TEXT,
  length INT,
  PRIMARY KEY ((id,month),timestamp,album_title,album_year,number)
) WITH CLUSTERING ORDER BY (timestamp DESC, album_title ASC, album_year ASC, number ASC);
```
Verify that the eight tables have been created:

`cqlsh -k music_data -e "DESCRIBE TABLES;"`

### Populate tables using DSBulk

Load data into table performers:

```sh
dsbulk load -url performers.csv  \
            -k music_data               \
            -t performers               \
            -header true                \
            -logDir /tmp/logs
```

Retrieve some rows from table performers:

`cqlsh -e "SELECT * FROM music_data.performers LIMIT 10;" `

Load data into tables albums_by_performer, albums_by_title and albums_by_genre:

```sh
dsbulk load -url assets/albums.csv      \
            -k music_data               \
            -t albums_by_performer      \
            -header true                \
            -logDir /tmp/logs

dsbulk load -url assets/albums.csv      \
            -k music_data               \
            -t albums_by_title          \
            -header true                \
            -logDir /tmp/logs

dsbulk load -url assets/albums.csv      \
            -k music_data               \
            -t albums_by_genre          \
            -header true                \
            -logDir /tmp/logs
```

Retrieve some rows from tables albums_by_performer, albums_by_title and albums_by_genre:

```sh
cqlsh -e "SELECT * FROM music_data.albums_by_performer LIMIT 5;"   
cqlsh -e "SELECT * FROM music_data.albums_by_title LIMIT 5;"   
cqlsh -e "SELECT * FROM music_data.albums_by_genre LIMIT 5;"
```

Load data into tables tracks_by_title and tracks_by_album:

```sh
dsbulk load -url assets/tracks.csv      \
            -k music_data               \
            -t tracks_by_title          \
            -header true                \
            -m "0=album_title,          \
                1=album_year,           \
                2=genre,                \
                3=number,               \
                4=title"                \
            -logDir /tmp/logs

dsbulk load -url assets/tracks.csv      \
            -k music_data               \
            -t tracks_by_album          \
            -header true                \
            -m "0=album_title,          \
                1=album_year,           \
                2=genre,                \
                3=number,               \
                4=title"                \
            -logDir /tmp/logs
```

Retrieve some rows from tables tracks_by_title and tracks_by_album:

```sh
cqlsh -e "SELECT * FROM music_data.tracks_by_title LIMIT 5;"   
cqlsh -e "SELECT * FROM music_data.tracks_by_album LIMIT 5;" 
```

### Insert rows using the CQL shell

```sh
cqlsh -k music_data
```

```sql
INSERT INTO users (id, name)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, 'Joe'); 
INSERT INTO users (id, name)
VALUES (UUID(), 'Jen'); 
INSERT INTO users (id, name)
VALUES (UUID(), 'Jim'); 

SELECT * FROM users;
```

```sql
INSERT INTO tracks_by_user (id, month, timestamp, album_title, album_year, number, title)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, '2020-01-01', '2020-01-05T11:22:33', '20 Greatest Hits', 1982, 16, 'Hey Jude');

INSERT INTO tracks_by_user (id, month, timestamp, album_title, album_year, number, title)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, '2020-09-01', '2020-09-15T09:00:00', '20 Greatest Hits', 1982, 16, 'Hey Jude');

INSERT INTO tracks_by_user (id, month, timestamp, album_title, album_year, number, title)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, '2020-09-01', '2020-09-15T16:41:10', 'Legendary Concert Performances', 1978, 6, 'Johnny B. Goode');

INSERT INTO tracks_by_user (id, month, timestamp, album_title, album_year, number, title)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, '2020-09-01', '2020-09-15T16:44:56', 'The Beatles 1967-1970', 1973, 17, 'Come Together');

INSERT INTO tracks_by_user (id, month, timestamp, album_title, album_year, number, title)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, '2020-09-01', '2020-09-15T21:13:13', 'Dark Side Of The Moon', 1973, 3, 'Time');

SELECT * FROM tracks_by_user;
```

### Design query Q1

Find a performer with name The Beatles:

<details>
    <summary>Show me the Answer! </summary>
    ```sql
    SELECT *
    FROM performers
    WHERE name = 'The Beatles';
    ```
</details>
<br/>

### Design query Q2

Find albums of performer The Beatles; order by year (desc):

<details>
    <summary>Show me the Answer! </summary>
    SELECT * 
    FROM albums_by_performer 
    WHERE performer = 'The Beatles';
</details>
<br/>

### Design query Q3

Find an album with title Magical Mystery Tour and year 1967:

<details>
    <summary>Show me the Answer! </summary>
    SELECT *
    FROM albums_by_title
    WHERE title = 'Magical Mystery Tour'
    AND year  = 1967;
</details>
<br/>

### Design query Q4

Find albums with title 20 Greatest Hits; order by year (desc):

<details>
    <summary>Show me the Answer! </summary>
    SELECT *
    FROM albums_by_title
    WHERE title = '20 Greatest Hits'; 
</details>
<br/>

### Design query Q5

Find albums from genre Classical; order by year (desc):

<details>
    <summary>Show me the Answer! </summary>
    SELECT *
    FROM albums_by_genre
    WHERE genre = 'Classical';
</details>
<br/>

### Design query Q6

Find tracks with title Let It Be:

<details>
    <summary>Show me the Answer! </summary>
    SELECT *
    FROM tracks_by_title
    WHERE title = 'Let It Be';
</details>
<br/>

### Design query Q7

Find tracks from album Magical Mystery Tour of 1967; order by track number (asc):

<details>
    <summary>Show me the Answer! </summary>
    SELECT *
    FROM tracks_by_album
    WHERE album_title = 'Magical Mystery Tour'
    AND album_year  = 1967;
</details>
<br/>

### Design query Q8

Find a user with id 12345678-aaaa-bbbb-cccc-123456789abc:

<details>
    <summary>Show me the Answer! </summary>
    SELECT *
    FROM users
    WHERE id = 12345678-aaaa-bbbb-cccc-123456789abc; 
</details>
<br/>

### Design query Q9

Find all tracks played by the user in September 2020; order by timestamp (desc):

<details>
    <summary>Show me the Answer! </summary>
    SELECT timestamp, album_title, album_year, number, title
    FROM tracks_by_user
    WHERE id = 12345678-aaaa-bbbb-cccc-123456789abc 
    AND month = '2020-09-01';
</details>
<br/>

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/04-data-modeling/lab-cassandra-digital-music-library)
