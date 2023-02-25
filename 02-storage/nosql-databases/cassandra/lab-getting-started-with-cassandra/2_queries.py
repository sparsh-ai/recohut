# cd Desktop\SanmiLeeAI\Data_Eng\Codes\Cassandra

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
# query = all songs by a certain artist released in a particular year
print('create table \n')

query = "CREATE TABLE IF NOT EXISTS songs "
query = query + \
    '(year int, song_title text, artist_name text, album_name text, single boolean, PRIMARY KEY (year, artist_name))'
try:
    session.execute(query)
except Exception as e:
    print(e)


# lets check to see if our table was created
# though no rows inserted yet, so should show zero
query = "SELECT COUNT(*) FROM songs"
try:
    count = session.execute(query)
except Exception as e:
    print(e)

print(count.one())


# Insert 2 rows
print('insert rows \n')

query = "INSERT INTO songs (year, song_title, artist_name, album_name, single)"
query = query + "values(%s, %s, %s, %s, %s)"
try:
    session.execute(query, (1970, "Across The Universe",
                            "The Beatles", "Let It Be", False))
except Exception as e:
    print(e)

try:
    session.execute(query, (1965, "Think For Yorself",
                            "The Beatles", "Rubber Soul", False))
except Exception as e:
    print(e)


# validate that data was inserted
print('view data \n')

query = "SELECT * FROM songs"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.album_name, row.artist_name)


# validate our original query
print('\n view query \n')

query = "SELECT * FROM songs WHERE year=1970 AND artist_name='The Beatles'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)

for row in rows:
    print(row.year, row.album_name, row.artist_name)


# drop table
print('\n drop table \n')

query = "DROP TABLE songs"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)


# close session & cluster connection
print('close session & connection  \n')

session.shutdown()
cluster.shutdown()
