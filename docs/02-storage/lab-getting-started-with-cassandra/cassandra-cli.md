# Working with Cassandra and CLI

## Cassandra and Shell

### Run server

`cassandra -f`

### Activate CQL shell

Run `cqlsh`

### Create a keyspace

A keyspace is a namespace for a set of tables sharing a data replication strategy and some options. It is conceptually similar to a "database" in a relational database management system.

Create the keyspace:

```sql
CREATE KEYSPACE killr_video
WITH replication = {
  'class': 'SimpleStrategy', 
  'replication_factor': 1 }; 
```

Our keyspace name is killr_video. Any data in this keyspace will be replicated using replication strategy SimpleStrategy and replication factor 1 . In production, however, we strongly recommend multiple datacenters and at least three replicas per datacenter for higher availability.

### Set a working keyspace

Many CQL statements work with tables, indexes and other objects defined within a specific keyspace. For example, to refer to a table, we have to either use a fully-qualified name consisting of a keyspace name and a table name, or set a working keyspace and simply refer to the table by its name. For convenience, we go with the second option.

Set the current working keyspace:

```sql
USE killr_video;
```

### Create a table

A Cassandra table has named columns with data types, rows with values, and a primary key to uniquely identify each row. As an example, let's create table users with four columns and primary key email .

Create the table:

```sql
CREATE TABLE users (
  email TEXT PRIMARY KEY,
  name TEXT,
  age INT,
  date_joined DATE
);
```

Example:

![](/img/tutorials/cassandra/killrvideo.png)

### Insert a row

Add the row into our table using the CQL INSERT statement:

```sql
INSERT INTO users (email, name, age, date_joined) 
VALUES ('joe@datastax.com', 'Joe', 25, '2020-01-01');
```

Insert another row into the table:

```sql
INSERT INTO users (email, name, age, date_joined) 
VALUES ('jen@datastax.com', 'Jen', 27, '2020-01-01');
```

### Retrieve a row

Now, retrieve the row using the CQL SELECT statement:

```sql
SELECT * FROM users
WHERE email = 'joe@datastax.com';
```

Retrieve a different row from the table:

```sql
SELECT * FROM users
WHERE email = 'jen@datastax.com';
```

### Update a row

Next, update the row using the CQL UPDATE statement:

```sql
UPDATE users SET name = 'Joseph' 
WHERE email = 'joe@datastax.com';

SELECT * FROM users;
```

Update another row in the table:

```sql
UPDATE users SET name = 'Jennifer' 
WHERE email = 'jen@datastax.com';

SELECT * FROM users;
```

### Delete a row

Finally, delete the row using the CQL DELETE statement:

```sql
DELETE FROM users 
WHERE email = 'joe@datastax.com';

SELECT * FROM users;
```

Delete another row from the table:

```sql
DELETE FROM users 
WHERE email = 'jen@datastax.com';

SELECT * FROM users;
```

### Test Your Understanding

Here is a short quiz for you.

Q1. Which CQL statement can be used to add rows into a table?

- [ ] A. SELECT
- [ ] B. DELETE
- [ ] C. INSERT

<details>
    <summary>Show me the Answer! </summary>
    C
</details>

Q2. Which CQL statement can be used to retrieve rows from a table?

- [ ] A. SELECT
- [ ] B. DELETE
- [ ] C. INSERT

<details>
    <summary>Show me the Answer! </summary>
    A
</details>

Q3. Which CQL statement can be used to remove rows from a table?

- [ ] A. SELECT
- [ ] B. DELETE
- [ ] C. INSERT

<details>
    <summary>Show me the Answer! </summary>
    B
</details>

## CQL Shell Commands

```sh
# Start the CQL shell
cqlsh

# To get help for cqlsh, type HELP or ? to see the list of available commands:
HELP

# To learn about the current cluster you’re working in, type:
DESCRIBE CLUSTER;

# To see which keyspaces are available in the cluster, issue the command below.
# What are these keyspaces for?
DESCRIBE KEYSPACES;

# Learn the client, server, and protocol versions in use
SHOW VERSION;

# View the default paging settings that will be used on reads
PAGING;

# View the default consistency level that will be used on all queries
CONSISTENCY

# View the default tracing options
TRACING

# Create your own keyspace. Try using tab completion as you enter this command
CREATE KEYSPACE my_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

# Describe the keyspace you just created.
# What additional information do you notice?
DESCRIBE KEYSPACE my_keyspace;

# Use the keyspace so you don't have to enter it on every data manipulation
# Note how the prompt changes after you do this
USE my_keyspace;

# Create a simple table
# What other syntax could you use to designate a single column primary key?
CREATE TABLE user ( first_name text, last_name text, PRIMARY KEY (first_name));

# Describe the table you just created
# What additional information do you notice?
DESCRIBE TABLE user;

# Write some data
INSERT INTO user (first_name, last_name) VALUES ('Bill', 'Nguyen');

# See how many rows have been written into this table
# Warning - row scans are expensive operations on large tables
SELECT COUNT (*) FROM user;

# Read the data we just wrote
SELECT * FROM user WHERE first_name='Bill';

# Remove a non-primary key column
DELETE last_name FROM USER WHERE first_name='Bill';

# Check to see the value was removed
SELECT * FROM user WHERE first_name='Bill';

# Delete an entire row
DELETE FROM USER WHERE first_name='Bill';

# Check to make sure it was removed
SELECT * FROM user WHERE first_name='Bill';

# Add a column to the table
ALTER TABLE user ADD title text;

# Check to see that the column was added
DESCRIBE TABLE user;

# Write a couple of rows, populate different columns for each, and view the results:
INSERT INTO user (first_name, last_name, title) VALUES ('Bill', 'Nguyen', 'Mr.');
INSERT INTO user (first_name, last_name) VALUES ('Mary', 'Rodriguez');
SELECT * FROM user;

# View the timestamps generated for previous writes
SELECT first_name, last_name, writetime(last_name) FROM user;

# Note that we’re not allowed to ask for the timestamp on primary key columns:
SELECT WRITETIME(first_name) FROM user;

# Set the timestamp on a write
# Note, you will probably want to change this value to be closer to your current time
#   (similar to timestamp from previous set)
UPDATE user USING TIMESTAMP 1434373756626000 SET last_name = 'Boateng' WHERE first_name = 'Mary' ;

# Verify the timestamp used
SELECT first_name, last_name, WRITETIME(last_name) FROM user WHERE first_name = 'Mary';

# View the time to live value for a column
SELECT first_name, last_name, TTL(last_name) FROM user WHERE first_name = 'Mary';

# Set the TTL on the  last name column to one hour
UPDATE user USING TTL 3600 SET last_name = 'McDonald' WHERE first_name = 'Mary' ;

# View the resulting TTL
# Note that it will already be counting down
SELECT first_name, last_name, TTL(last_name) FROM user WHERE first_name = 'Mary';

# Empty the contents of the table
TRUNCATE user;

# Show that the table is empty
SELECT * FROM user;

# Remove the entire table
DROP TABLE user;

# Clear the screen of output from previous commands
CLEAR

# Exit cqlsh
EXIT
```

## Learning CQL Data Types

```sh
# Continue using the keyspace and table from cqlsh_intro.cql
# Note use of IF NOT EXISTS syntax to avoid errors if already present
CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1} ;
USE my_keyspace;
CREATE TABLE IF NOT EXISTS user ( first_name text, last_name text, title text, PRIMARY KEY (first_name));

# Write a couple of rows, but only if they don't exist already
INSERT INTO user (first_name, last_name, title) VALUES ('Bill', 'Nguyen', 'Mr.') IF NOT EXISTS;
INSERT INTO user (first_name, last_name) VALUES ('Mary', 'Rodriguez') IF NOT EXISTS;

#
# UUID examples
#

# Add a unique identifier using a uuid
ALTER TABLE user ADD id uuid;

# Allow Cassandra to auto-assign a uuid
UPDATE user SET id = uuid() WHERE first_name = 'Mary';

# View the id that was set
SELECT first_name, id FROM user WHERE first_name = 'Mary';

#
# Set examples
#

# Add a set to contain email addresses
ALTER TABLE user ADD emails set<text>;

# Add an email address and check that it was added successfully
UPDATE user SET emails = { 'mary@example.com' } WHERE first_name = 'Mary';
SELECT emails FROM user WHERE first_name = 'Mary';

# Add another email address using concatenation
UPDATE user SET emails = emails + {'mary.mcdonald.AZ@gmail.com' } WHERE first_name = 'Mary';
SELECT emails FROM user WHERE first_name = 'Mary';

#
# List examples
#

# Modify the user table to add a list of phone numbers
ALTER TABLE user ADD phone_numbers list<text>;

# Add a phone number for Mary and check that it was added successfully
UPDATE user SET phone_numbers = [ '1-800-999-9999' ] WHERE first_name = 'Mary';
SELECT phone_numbers FROM user WHERE first_name = 'Mary';

# Add a second number by appending it:
UPDATE user SET phone_numbers = phone_numbers + [ '480-111-1111' ] WHERE first_name = 'Mary';
SELECT phone_numbers FROM user WHERE first_name = 'Mary';

# Replace an individual item in the list referenced by its index
UPDATE user SET phone_numbers[1] = '480-111-1111' WHERE first_name = 'Mary';

# Use the subtraction operator to remove a list item matching a specified value
UPDATE user SET phone_numbers = phone_numbers - [ '480-111-1111' ] WHERE first_name = 'Mary';

# Delete a specific item directly using its index
DELETE phone_numbers[0] from user WHERE first_name = 'Mary';

#
# Map examples
#

# Add a map attribute to store information about user logins (timed in seconds) keyed by a timestamp (timeuuid)
ALTER TABLE user ADD login_sessions map<timeuuid, int>;

# Add a couple of login sessions for Mary and see the results
# Use the now() function to allow Cassandra to set the timestamp
UPDATE user SET login_sessions = { now(): 13, now(): 18} WHERE first_name = 'Mary';
SELECT login_sessions FROM user WHERE first_name = 'Mary';

#
# User Defined Type (UDT) examples
#

# Create a UDT for address information
CREATE TYPE address (street text, city text, state text, zip_code int);

# Can we use this UDT in a map?
ALTER TABLE user ADD addresses map<text, address>;

# Freeze the UDT so we can use it in a map
# freezing means we cannot access individual fields of the UDT but must select or insert the entire object at once
ALTER TABLE user ADD addresses map<text, frozen<address>>;

# Add a home address for Mary
UPDATE user SET addresses = addresses +  {'home': { street: '7712 E. Broadway', city: 'Tucson',
  state: 'AZ', zip_code: 85715} } WHERE first_name = 'Mary';

#
# Index examples
#

# Query based on a non-primary key column
# Why doesn't this work?
SELECT * FROM user WHERE last_name = 'Nguyen';

# Create a secondary index for the last_name column.
CREATE INDEX ON user ( last_name );

# Now try the query again
SELECT * FROM user WHERE last_name = 'Nguyen';

# View the output of the describe command to see the full index definition
# We didn't name the index, so Cassandra assigned a default name
DESCRIBE KEYSPACE;

# Create indexes on other attributes if desired, even collections
# Note that queries based on indexes are typically more expensive, as they involve talking to more nodes
CREATE INDEX ON user ( addresses );
CREATE INDEX ON user ( emails );
CREATE INDEX ON user ( phone_numbers );

# Drop indexes we no longer want maintained
DROP INDEX user_last_name_idx;
DROP INDEX user_addresses_idx;
DROP INDEX user_emails_idx;
DROP INDEX user_phone_numbers_idx;

# Create a SSTable Attached Secondary Index (SASI), which is a more performant index implementation
CREATE CUSTOM INDEX user_last_name_sasi_idx ON user (last_name) USING 'org.apache.cassandra.index.sasi.SASIIndex';

# SASI indexes allow us to perform inequality and text searches such as "like" searches
SELECT * FROM user WHERE last_name LIKE 'N%';
```

## Cassandra and Python

### Installation

```txt title="requirements.txt"
service-identity==21.1.0
cassandra-driver==3.25.0
```

### Creating a Table with Apache Cassandra

1. Create a table in Apache Cassandra.
2. Insert rows of data.
3. Run a simple SQL query to validate the information.

```py
from cassandra.cluster import Cluster

try: 
    cluster = Cluster(['127.0.0.1']) #If you have a locally installed Apache Cassandra instance
    session = cluster.connect()
except Exception as e:
    print(e)
 
try:
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS kspace WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
)
except Exception as e:
    print(e)

try:
    session.set_keyspace('kspace')
except Exception as e:
    print(e)

query = "CREATE TABLE IF NOT EXISTS music_library "
query = query + "(year int, artist_name text, song_title text,  album_name text, single Boolean, PRIMARY KEY (year, artist_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)

query = "INSERT INTO music_library (year, artist_name, song_title, album_name, single)" 
query = query + " VALUES (%s, %s, %s, %s, %s)"

try:
    session.execute(query, (1970, "The Beatles", "Across The Universe", "Let It Be", False))
except Exception as e:
    print(e)
    
try:
    session.execute(query, (1965 , "The Beatles", "Think For Yourself", "Rubber Soul", False))
except Exception as e:
    print(e)

query = 'SELECT * FROM music_library'
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)

query = "SELECT * FROM music_library WHERE YEAR=1970 AND artist_name='The Beatles'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)

session.shutdown()
cluster.shutdown()
```

## Three Queries Three Tables

Let's imagine we would like to start creating a Music Library of albums. 

We want to ask 3 questions of the data:

Query 1: Give every album in the music library that was released in a given year

```sql
select * from music_library WHERE YEAR=1970
```

Query 2: Give every album in the music library that was created by a given artist  

```sql
select * from artist_library WHERE artist_name="The Beatles"
```

Query 3: Give all the information from the music library about a given album

```sql
select * from album_library WHERE album_name="Close To You"
```

Because we want to do three different queries, we will need different tables that partition the data differently. 

**Create the tables**

```py
query = "CREATE TABLE IF NOT EXISTS music_library "
query = query + "(year int, artist_name text, album_name text, PRIMARY KEY (year, artist_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)
    
query1 = "CREATE TABLE IF NOT EXISTS artist_library "
query1 = query1 + "(artist_name text, year int, album_name text, PRIMARY KEY (artist_name, year))"
try:
    session.execute(query1)
except Exception as e:
    print(e)

query2 = "CREATE TABLE IF NOT EXISTS album_library "
query2 = query2 + "(album_name text, artist_name text, year int, PRIMARY KEY (album_name, artist_name))"
try:
    session.execute(query2)
except Exception as e:
    print(e)
```

**Insert data into the tables**

```sql
query = "INSERT INTO music_library (year, artist_name, album_name)"
query = query + " VALUES (%s, %s, %s)"

query1 = "INSERT INTO artist_library (artist_name, year, album_name)"
query1 = query1 + " VALUES (%s, %s, %s)"

query2 = "INSERT INTO album_library (album_name, artist_name, year)"
query2 = query2 + " VALUES (%s, %s, %s)"

try:
    session.execute(query, (1970, "The Beatles", "Let it Be"))
except Exception as e:
    print(e)
    
try:
    session.execute(query, (1965, "The Beatles", "Rubber Soul"))
except Exception as e:
    print(e)
    
try:
    session.execute(query, (1965, "The Who", "My Generation"))
except Exception as e:
    print(e)

try:
    session.execute(query, (1966, "The Monkees", "The Monkees"))
except Exception as e:
    print(e)

try:
    session.execute(query, (1970, "The Carpenters", "Close To You"))
except Exception as e:
    print(e)
    
try:
    session.execute(query1, ("The Beatles", 1970, "Let it Be"))
except Exception as e:
    print(e)
    
try:
    session.execute(query1, ("The Beatles", 1965, "Rubber Soul"))
except Exception as e:
    print(e)
    
try:
    session.execute(query1, ("The Who", 1965, "My Generation"))
except Exception as e:
    print(e)

try:
    session.execute(query1, ("The Monkees", 1966, "The Monkees"))
except Exception as e:
    print(e)

try:
    session.execute(query1, ("The Carpenters", 1970, "Close To You"))
except Exception as e:
    print(e)
    
try:
    session.execute(query2, ("Let it Be", "The Beatles", 1970))
except Exception as e:
    print(e)
    
try:
    session.execute(query2, ("Rubber Soul", "The Beatles", 1965))
except Exception as e:
    print(e)
    
try:
    session.execute(query2, ("My Generation", "The Who", 1965))
except Exception as e:
    print(e)

try:
    session.execute(query2, ("The Monkees", "The Monkees", 1966))
except Exception as e:
    print(e)

try:
    session.execute(query2, ("Close To You", "The Carpenters", 1970))
except Exception as e:
    print(e)
```

:::tip
This might have felt unnatural to insert duplicate data into the tables. If I just normalized these tables, I wouldn't have to have extra copies! While this is true, remember there are no `JOINS` in Apache Cassandra. For the benefit of high availibity and scalabity, denormalization must be how this is done.
:::

**Validate the Data Model**

```py
query = "select * from music_library WHERE year=1970"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
for row in rows:
    print (row.year, row.artist_name, row.album_name)

query = "select * from artist_library WHERE artist_name='The Beatles'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
for row in rows:
    print (row.artist_name, row.album_name, row.year)

query = "select * from album_library WHERE album_name='Close To You'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
for row in rows:
    print (row.artist_name, row.year, row.album_name)
```

## Using the WHERE Clause

In this exercise we are going to walk through the basics of using the WHERE clause in Apache Cassandra.

Let's imagine we would like to start creating a new Music Library of albums. 

We want to ask 4 question of our data:

1. Give me every album in my music library that was released in a 1965 year
2. Give me the album that is in my music library that was released in 1965 by "The Beatles"
3. Give me all the albums released in a given year that was made in London 
4. Give me the city that the album "Rubber Soul" was recorded

How should we model this data? What should be our Primary Key and Partition Key? Since our data is looking for the YEAR let's start with that. From there we will add clustering columns on Artist Name and Album Name.

```py
query = "CREATE TABLE IF NOT EXISTS music_library "
query = query + "(year int, artist_name text, album_name text, city text, PRIMARY KEY (year, artist_name, album_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)
```

Let's insert our data into of table:

```py
query = "INSERT INTO music_library (year, artist_name, album_name, city)"
query = query + " VALUES (%s, %s, %s, %s)"

try:
    session.execute(query, (1970, "The Beatles", "Let it Be", "Liverpool"))
except Exception as e:
    print(e)
    
try:
    session.execute(query, (1965, "The Beatles", "Rubber Soul", "Oxford"))
except Exception as e:
    print(e)
    
try:
    session.execute(query, (1965, "The Who", "My Generation", "London"))
except Exception as e:
    print(e)

try:
    session.execute(query, (1966, "The Monkees", "The Monkees", "Los Angeles"))
except Exception as e:
    print(e)

try:
    session.execute(query, (1970, "The Carpenters", "Close To You", "San Diego"))
except Exception as e:
    print(e)
```

Let's Validate our Data Model with our 4 queries:

**Query 1**

```py
query = "SELECT * FROM music_library WHERE year=1965"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
for row in rows:
    print (row.year, row.artist_name, row.album_name, row.city)
```

**Query 2**

```py
query = "SELECT * FROM music_library WHERE year=1965 AND artist_name='The Beatles'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
for row in rows:
    print (row.year, row.artist_name, row.album_name, row.city)
```

**Query 3**

```py
query = "SELECT * FROM music_library WHERE year=1965 AND city='London'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
for row in rows:
    print (row.year, row.artist_name, row.album_name, row.city)
```

:::caution
Did you get an error? You can not try to access a column or a clustering column if you have not used the other defined clustering column. Let's see if we can try it a different way. 
:::

**Query 4**

```py
query = "SELECT city FROM music_library WHERE year=1965 AND artist_name='The Beatles' AND album_name='Rubber Soul'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
for row in rows:
    print (row.city)
```

## Amazon Keyspaces for Apache Cassandra

### First Keyspace

Go to https://us-east-1.console.aws.amazon.com/keyspaces/home?region=us-east-1#dashboard and follow the getting started guide to create a new keyspace, a new table inside that keyspace, insert a record inside the table and run query to retrieve the results.

### Connect via Python/CQLSH client

Download the TLS certificate:

```sh
mkdir -p ~/.cassandra
curl https://certs.secureserver.net/repository/sf-class2-root.crt -O ~/.cassandra/sf-class2-root.crt
```

Configure the Cassandra settings:

```yaml title="~/.cassandra/cqlshrc"
[connection]
port = 9142
factory = cqlshlib.ssl.ssl_transport_factory

[ssl]
validate = true
certfile =  ~/.cassandra/sf-class2-root.crt
version = TLSv1_2

[copy]
NUMPROCESSES=16
MAXATTEMPTS=25

[copy-from]
CHUNKSIZE=30
INGESTRATE=1500
MAXINSERTERRORS=-1
MAXPARSEERRORS=-1
MINBATCHSIZE=1
MAXBATCHSIZE=10

[csv]
field_size_limit=999999
```

Use the following command to connect via CQL shell:

```sh
cqlsh cassandra.us-east-1.amazonaws.com 9142 -u $USERNAME -p $PASSWORD --ssl
```

Use the following command to connect via Python:

```py
from cassandra.cluster import Cluster
from ssl import SSLContext, PROTOCOL_TLSv1_2 , CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider

USERNAME = ''
PASSWORD = ''

ssl_context = SSLContext(PROTOCOL_TLSv1_2 )
ssl_context.load_verify_locations('sf-class2-root.crt')
ssl_context.verify_mode = CERT_REQUIRED
auth_provider = PlainTextAuthProvider(username=USERNAME, password=PASSWORD)
cluster = Cluster(['cassandra.us-east-1.amazonaws.com'], ssl_context=ssl_context, auth_provider=auth_provider, port=9142)
session = cluster.connect()
r = session.execute('select * from system_schema.keyspaces')
print(r.current_rows)
```

Follow this for Python - https://docs.aws.amazon.com/keyspaces/latest/devguide/using_python_driver.html

Follow this for CQLSH - https://docs.aws.amazon.com/keyspaces/latest/devguide/programmatic.cqlsh.html

:::note
No need to follow all the steps but minimal as per your system configuration.
:::

### Loading data into Amazon Keyspaces using cqlsh

Follow this - https://docs.aws.amazon.com/keyspaces/latest/devguide/bulk-upload.html

### Using NoSQL Workbench with Amazon Keyspaces

Follow this - https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.html

