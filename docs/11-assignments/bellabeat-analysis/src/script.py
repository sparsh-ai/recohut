# IMPORT REQUIRED LIBRARIES
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

# READ-IN DATA

# Activity data
activity_df = pd.read_csv("./data/dailyActivity_merged.csv")
print(activity_df.info())
print(activity_df.columns)
print(f"Activity Dataframe \n {activity_df}")

# Sleep data
sleep_per_day_df = pd.read_csv("./data/sleepDay_merged.csv")
print(f"Sleep Per Day Dataframe \n {sleep_per_day_df}")

# Steps data
steps_per_day = pd.read_csv("./data/dailySteps_merged.csv")
print(f"Steps per Day Dataframe \n {steps_per_day}")

# Calories data
# calories per day
calories_per_day = pd.read_csv("./dailyCalories_merged.csv")
print(f"Daily Calories Dataframe \n {calories_per_day}")

# calories per hour
calories_per_hour = pd.read_csv("./hourlyCalories_merged.csv")
