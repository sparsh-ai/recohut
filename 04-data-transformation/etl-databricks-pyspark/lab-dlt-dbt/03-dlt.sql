-- Databricks notebook source
-- MAGIC %md
-- MAGIC 
-- MAGIC ## Using Delta Live Tables

-- COMMAND ----------

-- create bronze tables
CREATE LIVE TABLE games_raw
COMMENT "Games data from a SQL source"
TBLPROPERTIES ("quality" = "bronze")
AS SELECT * FROM default.zzz_games;

CREATE LIVE TABLE teams_raw
COMMENT "Teams data from a SQL source"
TBLPROPERTIES ("quality" = "bronze")
AS SELECT * FROM default.zzz_teams;

CREATE LIVE TABLE game_opponents_raw
COMMENT "Game opponents data from a SQL source"
TBLPROPERTIES ("quality" = "bronze")
AS SELECT * FROM default.zzz_game_opponents;

CREATE LIVE TABLE game_scores_raw
COMMENT "Games score data from a SQL source"
TBLPROPERTIES ("quality" = "bronze")
AS SELECT * FROM default.zzz_game_scores;

-- COMMAND ----------

-- create silver table
CREATE LIVE TABLE cleaned_game_details (
  CONSTRAINT valid_game_id EXPECT (game_id IS NOT NULL) ON VIOLATION DROP ROW
  )
  COMMENT "The cleaned and merged game score data" TBLPROPERTIES ("quality" = "silver") AS
  SELECT
    game_id,
    home,
    t.team_city AS visitor,
    home_score,
    visitor_score,
    -- Step 3 of 4: Display the city name for each game's winner.
    CASE
      WHEN home_score > visitor_score THEN home
      WHEN visitor_score > home_score THEN t.team_city
    END AS winner,
    game_date AS date
  FROM
    (
      -- Step 2 of 4: Replace the home team IDs with their actual city names.
      SELECT
        game_id,
        t.team_city AS home,
        home_score,
        visitor_team_id,
        visitor_score,
        game_date
      FROM
        (
          -- Step 1 of 4: Combine data from various tables (for example, game and team IDs, scores, dates).
          SELECT
            g.game_id,
            gop.home_team_id,
            gs.home_team_score AS home_score,
            gop.visitor_team_id,
            gs.visitor_team_score AS visitor_score,
            g.game_date
          FROM
            LIVE.games_raw as g,
            LIVE.game_opponents_raw as gop,
            LIVE.game_scores_raw as gs
          WHERE
            g.game_id = gop.game_id
            AND g.game_id = gs.game_id
        ) AS all_ids,
        LIVE.teams_raw as t
      WHERE
        all_ids.home_team_id = t.team_id
    ) AS visitor_ids,
    LIVE.teams_raw as t
  WHERE
    visitor_ids.visitor_team_id = t.team_id
  ORDER BY
    game_date DESC

-- COMMAND ----------

-- create gold table
CREATE LIVE TABLE final_score_data COMMENT "Aggregate game record data" TBLPROPERTIES ("quality" = "gold") AS
SELECT
  winner AS team,
  count(winner) AS wins,
  -- Each team played in 4 games.
  (4 - count(winner)) AS losses
FROM
  (
    -- Step 1 of 2: Determine the winner and loser for each game.
    SELECT
      game_id,
      winner,
      CASE
        WHEN home = winner THEN visitor
        ELSE home
      END AS loser
    FROM
      LIVE.cleaned_game_details
  )
GROUP BY
  winner
ORDER BY
  wins DESC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC 
-- MAGIC - Click on Workflows in the sidebar > Delta Live Tables > Create pipeline
-- MAGIC - Select this notebook
-- MAGIC - Select Triggered for the pipeline mode and hit Create
-- MAGIC - Click Start on top bar of the pipeline window
-- MAGIC - Databricks would now start creating the pipeline, populate your medallion tables, and generate a dependency graph. You can modify the pipeline any time including the schedule and target tables.

-- COMMAND ----------


