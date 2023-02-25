# Since NoSQL has no JOINs, where becomes imperative

import cassandra
from cassandra.cluster import Cluster


print('create connection to database \n')
try:
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
except Exception as e:
    print(e)


print('create keyspace/database \n')
try:
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS wysde
    WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor': 1}""")
except Exception as e:
    print(e)


# connect to key space
print('connect to key space \n')
try:
    session.set_keyspace('wysde')
except Exception as e:
    print(e)


# create table with query impression : 4 queries
# query 1 = all albums in a given year
# query 2 = album realeased by 'The Beatles'
# query 3 = select city from year=1970 & artist_name=The Beatles


print('create table \n')

query = "CREATE TABLE IF NOT EXISTS songs_library "
query = query + \
    '(year int, artist_name text, album_name text, city text, PRIMARY KEY (year, artist_name, album_name))'
try:
    session.execute(query)
except Exception as e:
    print(e)


# Insert 5 rows
print('insert rows \n')

query = "INSERT INTO songs_library (year, artist_name, album_name, city)"
query = query + "values(%s, %s, %s, %s)"


try:
    session.execute(query, (1970, "The Beatles", "Let It Be", 'Liverpool'))
except Exception as e:
    print(e)

try:
    session.execute(query, (1965, "The Beatles", "Rubber Soul", 'Oxford'))
except Exception as e:
    print(e)

try:
    session.execute(query, (1965, "The Who", "My Generation", 'London'))
except Exception as e:
    print(e)

try:
    session.execute(query, (1966, "The Monkees", "The Monkees", 'Los Angeles'))
except Exception as e:
    print(e)

try:
    session.execute(query, (1970, "The Carpenters",
                            "Close To You", 'San Diego'))
except Exception as e:
    print(e)


# validate that data was inserted
print('query 1 = all albums in a given year=1970 \n')

query = "SELECT * FROM songs_library WHERE year=1970"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.artist_name, row.album_name, row.city)


print("\n query 2 = album realeased by 'The Beatles' where year=1970 \n")

query = "SELECT * FROM songs_library WHERE year=1970 AND artist_name='The Beatles' "
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.artist_name, row.album_name, row.city)


print("\n query 3 = album released year=1970 AND artist_name='The Beatles' AND album_name='Let IT BE' \n ")

query = "SELECT city FROM songs_library WHERE year = 1970 AND artist_name = 'The Beatles' AND album_name = 'Let It Be' "
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.city)


# drop table
print("\n drop table \n")

query = "DROP TABLE songs_library"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)


# close session & cluster connection
print('close session & connection  \n')

session.shutdown()
cluster.shutdown()
