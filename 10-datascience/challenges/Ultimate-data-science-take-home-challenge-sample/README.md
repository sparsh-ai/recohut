# Ultimate Data Science Take Home Challenge Sample
A practice challenge for the DS interview process
## Part 1 ‑ Exploratory data analysis

[Part 1 - EDA](https://github.com/olsenben/Ultimate-data-science-take-home-challenge-sample/blob/master/Pt-1-ultimate-data-science-challenge.ipynb)

The attached logins.json file contains (simulated) timestamps of user logins in a particular geographic location. Aggregate these login counts based on 15minute time intervals, and visualize and describe the resulting time series of login counts in ways that best characterize the underlying patterns of the demand. Please report/illustrate important features of the demand, such as daily cycles. If there are data quality issues, please report them.

## Part 2 ‑ Experiment and metrics design
The neighboring cities of Gotham and Metropolis have complementary circadian rhythms: on weekdays, Ultimate Gotham is most active at night, and Ultimate Metropolis is most active during the day. On weekends, there is reasonable activity in both cities.

However, a toll bridge, with a two way toll, between the two cities causes driver partners to tend to be exclusive to each city. The Ultimate managers of city operations for the two cities have proposed an experiment to encourage driver partners to be available in both cities, by reimbursing all toll costs.
What would you choose as the key measure of success of this experiment in encouraging driver partners to serve both cities, and why would you choose this metric?
Describe a practical experiment you would design to compare the effectiveness of the proposed change in relation to the key measure of success. Please provide details on:
1. how you will implement the experiment
2. what statistical test(s) you will conduct to verify the significance of the observation
3. how you would interpret the results and provide recommendations to the city operations team along with any caveats.

### 1. Key Metric of Success
To measure the success of the experiment, there must be a metric which accurately captures the tendency of a driver to serve one city exclusively over the other. An easy way to do this would be to count the number of times a driver crosses the toll bridge in a direction away from the city the driver tends to serve most often. However, since the reimbursement program has not started yet I can’t assume that that data is available (it would be apparent in the reimbursement records, but would not separate drivers into a before and after group). In the assumed absence of this information, another metric can be designed which draws on geographical information that can be safely assumed to be available if properly collected: the starting and ending location of each trip. Using this information, the tendency for a driver to serve one city exclusively can be quantified by means of a ratio:

Exclusivity ratio - measure of tendency to serve one city exclusively

Let X represent the city in which a driver has the most trips that start and end in that city.

Let Y represent the city in which a driver has the least trips that start and end in that city.

A = number of trips that start and end in X city

B = number of trips that start in X city and end in Y city

C = number of trips that start in Y city and end in X city

D = number of trips that start and end in Y city

Exclusivity ratio = (A)/(A + B + C + D)

An exclusivity ratio of 1 indicates that a driver favors X city exclusively, while a ratio of .5 would indicate that a driver favors X city 50% of the time, and a ratio of .25 would indicate that they are equally likely to accept each of the 4 types of trips (A, B, C, and D). The variables must remain constant for the entire experiment. 

### 2. Experimental Design
#### Implementation
The hypothesis of this experiment is that the exclusivity ratio of drivers will be reduced after the reimbursement program is introduced. Drivers must have their discrete variables for X, Y, A, B, C, and D encoded using data-wrangling and feature engineering. Once this is done, the exclusivity ratio for each driver can be calculated. Next, drivers should be be subsetted into a testing group and a control group (weighting according to which city drivers are exclusive to must be controlled in order to ensure a representative control group). Next the reimbursement program can be implemented for the testing group. At its conclusion, the exclusivity ratio for the drivers must be calculated again using the same constant variables for the testing and control group. 
#### Testing
To test the null-hypothesis, we must assume that any difference in the mean of the ratio before and the ratio after are due to random chance. Testing the null-hypothesis should be as simple as comparing the before and after ratios of both the testing group and control group with a two-way z-test to compare the means of the group, provided that all results for all groups are normally distributed (in the event that they are not, a non-parametric test should be utilized instead according to the distribution and standard deviation of the samples). 
### 3. Recommendations
A statistically significant decrease in the ratio of the testing group will indicate that the experiment was successful, and would support the idea that reimbursing toll can encourage drivers against serving one city exclusively. For the control group, a statistically significant decrease in the ratio would indicate that there is another variable uncontrolled for, and that the experiment cannot be conclusively considered to be successful in terms of reimbursing for toll. No change in either may indicate that there is a stronger variable than the toll bridge at work affecting the exclusivity of the drivers.
#### Other Considerations
Since it is know that the cities have different circadian rhythms, it would be prudent to take into consideration the time of day of a trip, and apply a weighting system against the exclusivity ratio depending on the time of day and which city. This is because there may be a tendency of a driver to prefer driving during the day or night, which would directly influence which city they serve, especially during the weekdays (since weekends show relatively similar activity, they would be excluded from this weighting system). In other words, if a driver is exclusive to one city, but only drives during that city's most active times anyways (and not the other cities active hours), then the fact that the driver is exclusive should be downplayed. In the event that the null hypothesis is accepted, this is the first variable I would investigate (luckily it can be calculated after the fact and does not require extra data collection, provided that the time of the trips is recorded). 

## Part 3 ‑ Predictive modeling

[Part 3 - Modeling](https://github.com/olsenben/Ultimate-data-science-take-home-challenge-sample/blob/master/Pt-3-ultimate-data-science-challenge.ipynb)

Ultimate is interested in predicting rider retention. To help explore this question, we have
provided a sample dataset of a cohort of users who signed up for an Ultimate account in
January 2014. The data was pulled several months later; we consider a user retained if they
were “active” (i.e. took a trip) in the preceding 30 days.
We would like you to use this data set to help understand what factors are the best predictors
for retention, and offer suggestions to operationalize those insights to help Ultimate.
The data is in the attached file ultimate_data_challenge.json. See below for a detailed
description of the dataset. Please include any code you wrote for the analysis and delete the
dataset when you have finished with the challenge.
1. Perform any cleaning, exploratory analysis, and/or visualizations to use the provided
data for this analysis (a few sentences/plots describing your approach will suffice). What
fraction of the observed users were retained?
2. Build a predictive model to help Ultimate determine whether or not a user will be active
in their 6th month on the system. Discuss why you chose your approach, what
alternatives you considered, and any concerns you have. How valid is your model?
Include any key indicators of model performance.
3. Briefly discuss how Ultimate might leverage the insights gained from the model to
improve its longterm
rider retention (again, a few sentences will suffice).
### Data description
* city: city this user signed up in
* phone: primary device for this user
* signup_date: date of account registration; in the form ‘YYYY MM DD’
* last_trip_date: the last time this user completed a trip; in the form ‘YYYY MM DD’
* avg_dist: the average distance in miles per trip taken in the first 30 days after signup
* avg_rating_by_driver: the rider’s average rating over all of their trips
* avg_rating_of_driver: the rider’s average rating of their drivers over all of their trips
* surge_pct: the percent of trips taken with surge multiplier > 1
* avg_surge: The average surge multiplier over all of this user’s trips
* trips_in_first_30_days: the number of trips this user took in the first 30 days after
signing up
* ultimate_black_user: TRUE if the user took an Ultimate Black in their first 30 days;
FALSE otherwise
* weekday_pct: the percent of the user’s trips occurring during a weekday

