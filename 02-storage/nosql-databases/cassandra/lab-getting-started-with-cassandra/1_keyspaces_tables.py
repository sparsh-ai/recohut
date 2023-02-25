# cd Desktop\SanmiLeeAI\Data_Eng\Codes\Cassandra

import cassandra
from cassandra.cluster import Cluster

print('Libraries imported \n')


try:
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
except Exception as e:
    print(e)


# Lets create a keyspace
print('Creating a keyspace \n')

try:
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS wysde
    WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor': 1}"""
                    )
except Exception as e:
    print(e)


# connect to key space
print('connect to key space \n')
try:
    session.set_keyspace('wysde')
except Exception as e:
    print(e)


# creating table 1 - get all musci produced in 1970
# primary key = (year, artist_name) --> year=partition key, artist_name=clustering column
print('create table \n')

query = "CREATE TABLE IF NOT EXISTS music_library"
query = query + \
    '(year int, artist_name text, album_name text, PRIMARY KEY (year, artist_name))'
try:
    session.execute(query)
except Exception as e:
    print(e)


# lets check to see if our table was created
# though no rows inserted yet, so should show zero
query = "SELECT COUNT(*) FROM music_library"
try:
    count = session.execute(query)
except Exception as e:
    print(e)

print(count.one())


# Insert 2 rows
print('insert rows \n')
query = "INSERT INTO music_library (year, artist_name, album_name)"
query = query + "values(%s, %s, %s)"
try:
    session.execute(query, (1970, "The Beatle", "Let It Be"))
except Exception as e:
    print(e)

try:
    session.execute(query, (1965, "The Beatle", "Rubber Soul"))
except Exception as e:
    print(e)


# validate that data was inserted
print('view data \n')

query = "SELECT * FROM music_library"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.album_name, row.artist_name)


# creating table 2 - get all musci produced in 1970
# primary key = (year, artist_name) --> year=partition key, artist_name=clustering column
print('create table \n')

query = "CREATE TABLE IF NOT EXISTS songz"
query = query + \
    '(artist_name text, year int, album_name text, PRIMARY KEY (artist_name, year))'
try:
    session.execute(query)
except Exception as e:
    print(e)


# lets check to see if our table was created
# though no rows inserted yet, so should show zero
query = "SELECT COUNT(*) FROM songz"
try:
    count = session.execute(query)
except Exception as e:
    print(e)

print(count.one())


# Insert 2 rows
print('insert rows \n')
query = "INSERT INTO songz (artist_name, year, album_name)"
query = query + "values(%s, %s, %s)"
try:
    session.execute(query, ("The Beatle", 1970, "Let It Be"))
except Exception as e:
    print(e)

try:
    session.execute(query, ("The Beatle", 1965, "Rubber Soul"))
except Exception as e:
    print(e)


# validate our original query 1 in table 1
print('\n view query when year = 1970 in table 1\n')

query = "SELECT * FROM music_library WHERE year=1970"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.album_name, row.artist_name)


# validate our original query 2in table 2
print('\n view query when artist_name = The Beatle in table 2 \n')

query = "SELECT * FROM songz WHERE artist_name='The Beatle' "
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.album_name, row.year, row.artist_name)


# drop table 1
print('\n drop table 1\n')

query = "DROP TABLE music_library"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)


# drop table 2
print('drop table 2 \n')

query = "DROP TABLE songz"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)


# close session & cluster connection
session.shutdown()
cluster.shutdown()
