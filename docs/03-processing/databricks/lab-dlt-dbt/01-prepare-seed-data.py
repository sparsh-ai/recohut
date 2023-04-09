# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ## Prepare seed data in Databricks

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC To create some real transformations, we need to provide seed (raw) data to dbt. We'll manually create a few raw tables.

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW DATABASES;

# COMMAND ----------

# MAGIC %sql
# MAGIC USE default;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Drop tables if created already
# MAGIC DROP TABLE IF EXISTS zzz_game_opponents;
# MAGIC DROP TABLE IF EXISTS zzz_game_scores;
# MAGIC DROP TABLE IF EXISTS zzz_games;
# MAGIC DROP TABLE IF EXISTS zzz_teams;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create and populate game_opponents table
# MAGIC CREATE TABLE zzz_game_opponents (
# MAGIC game_id INT,
# MAGIC home_team_id INT,
# MAGIC visitor_team_id INT
# MAGIC ) USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO zzz_game_opponents VALUES (1, 1, 2);
# MAGIC INSERT INTO zzz_game_opponents VALUES (2, 1, 3);
# MAGIC INSERT INTO zzz_game_opponents VALUES (3, 2, 1);
# MAGIC INSERT INTO zzz_game_opponents VALUES (4, 2, 3);
# MAGIC INSERT INTO zzz_game_opponents VALUES (5, 3, 1);
# MAGIC INSERT INTO zzz_game_opponents VALUES (6, 3, 2);

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create and populate game_scores table
# MAGIC CREATE TABLE zzz_game_scores (
# MAGIC game_id INT,
# MAGIC home_team_score INT,
# MAGIC visitor_team_score INT
# MAGIC ) USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO zzz_game_scores VALUES (1, 4, 2);
# MAGIC INSERT INTO zzz_game_scores VALUES (2, 0, 1);
# MAGIC INSERT INTO zzz_game_scores VALUES (3, 1, 2);
# MAGIC INSERT INTO zzz_game_scores VALUES (4, 3, 2);
# MAGIC INSERT INTO zzz_game_scores VALUES (5, 3, 0);
# MAGIC INSERT INTO zzz_game_scores VALUES (6, 3, 1);

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create and populate games table
# MAGIC CREATE TABLE zzz_games (
# MAGIC game_id INT,
# MAGIC game_date DATE
# MAGIC ) USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO zzz_games VALUES (1, '2020-12-12');
# MAGIC INSERT INTO zzz_games VALUES (2, '2021-01-09');
# MAGIC INSERT INTO zzz_games VALUES (3, '2020-12-19');
# MAGIC INSERT INTO zzz_games VALUES (4, '2021-01-16');
# MAGIC INSERT INTO zzz_games VALUES (5, '2021-01-23');
# MAGIC INSERT INTO zzz_games VALUES (6, '2021-02-06');

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create and populate teams table
# MAGIC CREATE TABLE zzz_teams (
# MAGIC team_id INT,
# MAGIC team_city VARCHAR(15)
# MAGIC ) USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO zzz_teams VALUES (1, "San Francisco");
# MAGIC INSERT INTO zzz_teams VALUES (2, "Seattle");
# MAGIC INSERT INTO zzz_teams VALUES (3, "Amsterdam");
