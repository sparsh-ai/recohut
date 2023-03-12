# IMPORT REQUIRED LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn theme
# sns.set_style("darkgrid")
sns.set_palette("hls")

## READ-IN DATA
activity_df = pd.read_csv("./data/dailyActivity_merged.csv")
print(activity_df.info())
print(activity_df.columns)
print(f"Activity Dataframe \n {activity_df}")


# PROCESS DATA

# Convert the ActivityDate column into  a datetime
activity_df["ActivityDate"] = pd.to_datetime(activity_df["ActivityDate"])
print(activity_df.info())

## Check for null values

print(activity_df.isnull().sum())

### From the output, the activity dataframe does not have null values.

## Next, check for duplicated rows

print(activity_df.duplicated().sum())

### The activity dataframe does not have duplicated rows.

## Next, get summary of the data

print(activity_df.describe())

## Key stats from the summary

### Average number of steps is 7637.91steps, with a maximum of 36019.00
### Average distance by an individual is 5.49km with a min of 0 and a maximum of 28.03
### Average amount of calories burned is 2303.61 with a minimum of 0 and a maximum of 4900.00

# ANALYZE DATA

## Establish the relationship between Total Steps and Total Distance
### The purpose of this step is to determine if Total Steps variable can be used in place of Total Distance and vice versa

steps_distance_corr = activity_df["TotalSteps"].corr(activity_df["TotalDistance"])
print(f"Total Distance-Total Steps Corr is {steps_distance_corr}")

### This yields a pearson correlation of 0.9853
### This shows a very high positive relationship between Total Distance and Total Steps taken.
### Given the high correlation and that distance is derived from steps, Total Steps shall be used for analysis.

## Establish the relationship between Total Steps and Calories burned

### First, get the correlation

total_steps_calories_corr = activity_df["TotalSteps"].corr(activity_df["Calories"])
print(f"Total Stpes-Calories Corr is {total_steps_calories_corr}")

### pearson correlation is 0.5916
### This shows that there is a large positive correlation between total steps taken and calories burned.

## Plot data in a scatterplot
plt.figure(figsize=(8, 4.21), dpi=100)
plt.title("Calories Burned vs Total Steps", pad=20, loc="left")
sns.scatterplot(data=activity_df, x="TotalSteps", y="Calories")
plt.show()

### Total Steps and Calories exhibit a linear relationship as shown above.


## Establish the relationship between very active minutes and calories burned

active_caloris_corr = activity_df["VeryActiveMinutes"].corr(activity_df["Calories"])
print(f"Active Minutes-Calories Corr is {active_caloris_corr}")

### pearson correlation is  0.6158.
### This indicates a large positive correlation between the two variables.

## Plot data in a scatterplot
plt.figure(figsize=(8, 4.21), dpi=100)
plt.title("Calories Burned vs Very Active Minutes", pad=20, loc="left")
sns.scatterplot(data=activity_df, x="VeryActiveMinutes", y="Calories")
plt.show()

# Establish the relationship between Sedentary minutes and Calories

sedentary_calories_corr = activity_df["SedentaryMinutes"].corr(activity_df["Calories"])
print(f"Sedentary-Calories Corr is {sedentary_calories_corr}")

### pearson correlation is -0.1069.
### This shows a small negative relationship between time spend sitting/inactive and alories burned

## Plot data in a scatterplot
plt.figure(figsize=(8, 4.21), dpi=100)
plt.title("Calories Burned vs Sedentary Minutes", pad=20, loc="left")
sns.scatterplot(data=activity_df, x="SedentaryMinutes", y="Calories")
plt.show()


## Establish the days of the week when individuals are most active

## First, create a new column with ActivityDate represented as day of the week

activity_df["day_of_week"] = activity_df["ActivityDate"].dt.day_name()
activity_df["day_number"] = activity_df["ActivityDate"].dt.weekday
print(activity_df)

## A list with days of the week
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sartuday", "Sunday"]

## Groupby operation
active_minutes_per_day = activity_df.groupby(["day_number"])["VeryActiveMinutes"]

## Total Active Minutes
sum_of_active_minutes_per_day = (
    active_minutes_per_day.sum().rename_axis("Day").reset_index(name="Minutes")
)
print(sum_of_active_minutes_per_day)

# Visualize the data
plt.figure(figsize=(8, 4.21), dpi=100)
plt.title("Total Active Minutes per Day", pad=20, loc="left")
sns.barplot(data=sum_of_active_minutes_per_day, x=week, y="Minutes")
plt.show()

### From this visualization, Tuesday and Wednesday have the most active minutes.

## Average active minutes per day
mean_of_active_minutes_per_day = (
    active_minutes_per_day.mean().rename_axis("Day").reset_index(name="Minutes")
)
print(mean_of_active_minutes_per_day)

## Visualize the data
plt.figure(figsize=(8, 4.21), dpi=100)
plt.title("Average Active Minutes per Day", pad=20, loc="left")
sns.barplot(data=mean_of_active_minutes_per_day, x=week, y="Minutes")
plt.show()

### From this analysis, Monday and Tuesday have the highest mean indicating that on average people are more active.

### Why is there a difference between the sum and mean visualizations?
### To explore the difference, find the count of each day in the dataframe.

print(activity_df["day_number"].value_counts())

### This indicates a variation in the count of days and thus the differences in mean.
### This means that we cannot say for sure which day are people most active using the sum.
### To get a fair conclusion, we shall rely on the mean.


# Find out how movement (measured by total steps) varies per day

steps_per_day = activity_df.groupby(["day_number"])["TotalSteps"]
average_steps_per_day = (
    steps_per_day.mean().rename_axis("Day").reset_index(name="Steps")
)
print(average_steps_per_day)

## Visualize the data
plt.figure(figsize=(8, 4.21), dpi=100)
plt.title("Average Steps per Day", pad=20, loc="left")
sns.barplot(data=average_steps_per_day, x=week, y="Steps")
plt.show()
