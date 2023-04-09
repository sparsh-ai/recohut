# NHLAPI - SQL and Python Assignment

## Objective

Use the publicly accessible portions of the NHL API (https://gitlab.com/dword4/nhlapi/-/blob/master/stats-api.md) to query for historical Florida Panthers statistics, createtables consistent with instructions, and then use SQL to write queries and answer questions using those tables.

## Python

A. Make sure you have the necessary packages installed, or similar.

```bash
pip install pandas
pip install requests
```

B. Create an .ipynb file and import them.

```python
import requests
import pandas as pd
```

C. Write one or more function(s) that queries the /teams and the /people endpoints for all Panthers players, starting in the 2014-15 season, and ending in the 2021-22 season. Should return a pandas data frame where every row is an individual player’s season (only seasons where they played for the Panthers), where player id is the first field, season is the second, then descriptive player information (age, height, weight), and finally all of their season averages/totals playing for the Panthers. Calculate their age during that season using this logic: https://www.hockey-reference.com/about/glossary.html

```python
def create_panthers_players_table():

    return panthers_players_table
```

D. Write one or more function(s) that queries the /schedule and /game endpoints for all Panthers games, starting in the 2014-15 season, and ending in the 2021-22 season. Should return a data frame where every row is an individual game, with the game id as the first field, whether the Panthers were home or away as the second field, the result for the Panthers as the third (win, loss, overtime loss), and finally the team stats for both the Panthers and their opponent.

```python
def create_panthers_game_boxscores_table():
  
    return panthers_game_boxscores_table
```

E. Write one or more function(s) that queries the /game endpoint for every Panthers player’s individual game box score, using the game id’s you gathered from above. Should return a data frame where every row is a Panthers player that played in the game, where
the first two fields are player id and game id, and the rest of the fields are all of the player’s individual statistics for the game.

```python
def create_panthers_player_boxscores_table():

    return panthers_player_boxscores_table
```

F. Write all final data frames as csv’s to a local directory to attach later.

## SQL

*A.* Make sure you have pandas sql installed

```bash
pip install pandasql
```

B. Import sqldf from the pandas sql package

```python
from pandasql import sqldf
```

*C.* Create a quick function to facilitate the queries

```python
pysqldf = lambda q: sqldf(q, globals())
```

D. Load in your three tables and give them clearly defined names. Answer questions in the following format

```python
q = """

"""
q1_answer = pysqldf(q)
print(q1_answer)
```

1. Which five players have played the most full seasons for the Panthers in the time frame we pulled?
2. Which player had the highest plus-minus in an individual game and what was the result for the Panthers?
3. Who were the youngest players to play for the Panthers in this time period, that were also on the team in
   2021-22, and what were the first games they played for the Panthers?
4. Who had the most total penalty minutes in a season for the panthers, and what season did this take place
   in?
5. Rank Panthers seasons by number of total home shutouts.
