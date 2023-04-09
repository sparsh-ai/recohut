# import libraries
import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3
import os
from dotenv import load_dotenv

# load_dotenv will look for a .env file and if it finds one, it will load the environment variables from it
load_dotenv()

# Spotify TOKEN generation:
# https://developer.spotify.com/console/get-recently-played/

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = os.getenv("SPOTIFY_ID")  # Spotify ID
TOKEN = os.getenv("SPOTIFY_TOKEN") # Spotify Token (needs to be re-generated when expired)

if __name__ == "__main__":

    # Extract part of the ETL process

    # Request structure
    # curl -X "GET" "https://api.spotify.com/v1/me/player/recently-played?limit=50&after={TIME}" -H 
    # "Accept: application/json" -H 
    # "Content-Type: application/json" -H 
    # "Authorization: Bearer TOKEN"

    # curl -X "GET" "https://api.spotify.com/v1/me/player/recently-played?limit=50" -H "
    # (...)

    # Headers for the Spotify API
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

    # Convert time to Unix timestamp in miliseconds 
    today                       = datetime.datetime.now()
    yesterday                   = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp    = int(yesterday.timestamp()) * 1000

    # Download all songs you've listened to "after yesterday", which means in the last 24 hours      
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=50&after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    # Spotify API, HTTP status code
    if r.status_code == 200:
        print(f"Spotify API Token up-to-date. Request status code: {r.status_code}. \n")
    else:
        print("Problem with Requests. Potential problem with Spotify API Token. \n")

    data = r.json()

    # Data checks
    def check_if_valid_data(df: pd.DataFrame) -> bool:

        # Check if DataFrame is empty
        if df.empty:
            print("No songs downloaded. Finishing execution.")
            return False

        # Primary Key Check
        if pd.Series(df["played_at"]).is_unique:
            pass
        else:
            raise Exception("Primary key check is violated.")

        # Check for null values
        if df.isnull().values.any():
            raise Exception("Null value found!")

        # Check if all timestamps are of yesterday's or today's date
        today = datetime.datetime.now()
        today = today.replace(hour=0, minute=0, second=0, microsecond=0)

        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

        timestamps = df["timestamp"].tolist()
        for timestamp in timestamps:
            if datetime.datetime.strptime(timestamp, '%Y-%m-%d') != yesterday and datetime.datetime.strptime(timestamp, '%Y-%m-%d') != today:
                print(timestamp, song["played_at"])
                raise Exception("At least one of the returned songs is not from the last 24h.")

        return True

    # Write json data to file
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Extracting only the relevant bits of data from the json object      
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    song_dict = {
        "song_name" : song_names,
        "artist_name" : artist_names,
        "played_at" : played_at_list,
        "timestamp" : timestamps
    }
   
   # Create song DataFrame
    song_df = pd.DataFrame(song_dict)

    # Validate
    if check_if_valid_data(song_df):
        print("Data valid, proceed to Load stage.")

    print("Recent songs (0-50):")
    print(song_df)
    print()

    # Load

    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    connection = sqlite3.connect('my_played_tracks.sqlite')
    cursor = connection.cursor()

    # SQL query (could be also achieved from sqlalchemy level)
    # Primary key on 'played_at' (always unique)
    sql_query = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        timestamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    """

    cursor.execute(sql_query)
    print("Opened database successfully")

    # Instert data directly from sql to the database
    try:
        song_df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
    except:
        print("Data already exists in the database. \n")

    # print current database overview
    print(pd.read_sql_query("SELECT * FROM my_played_tracks", connection))

    connection.close()
    print("Closed database successfully")

