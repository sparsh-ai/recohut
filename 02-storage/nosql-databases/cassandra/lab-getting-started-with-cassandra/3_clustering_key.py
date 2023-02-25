# cd Desktop\SanmiLeeAI\Data_Eng\Codes\Cassandra
# clustering: apart from ensuring uniqueness in primary keys also does sorting

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


# create table with query impression
# query = all songs by a certain artist with album name in desc order and city in desc order
print('create table \n')

query = "CREATE TABLE IF NOT EXISTS songs_library "
query = query + \
    '(year int, artist_name text, album_name text, city text, PRIMARY KEY (artist_name, album_name, city))'
try:
    session.execute(query)
except Exception as e:
    print(e)


# Insert 5 rows
print('insert rows \n')

query = "INSERT INTO songs_library (year, artist_name, album_name, city)"
query = query + "values(%s, %s, %s, %s)"
try:
    session.execute(query, (1965, "The Beatles", "Rubber Soul", 'Oxford'))
except Exception as e:
    print(e)

try:
    session.execute(query, (1970, "The Beatles", "Let It Be", 'Liverpool'))
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

try:
    session.execute(query, (1964, "The Beatles", "Beatles For Sale", 'London'))
except Exception as e:
    print(e)


# validate that data was inserted
print('view data \n')

query = "SELECT * FROM songs_library"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.artist_name, row.album_name, row.city)


# validate our original query
# query = select * where artist_name = The Beatles
print('\n view query \n')

query = "SELECT * FROM songs_library WHERE artist_name='The Beatles'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.artist_name, row.album_name, row.city, row.year)


# drop table
print('\n drop table \n')

query = "DROP TABLE songs_library"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)


# close session & cluster connection
print('close session & connection  \n')

session.shutdown()
cluster.shutdown()
