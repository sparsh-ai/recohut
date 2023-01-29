# Yammer Analytics

Yammer is a social network for communicating with coworkers. Individuals share documents, updates, and ideas by posting them in groups. Yammer is free to use indefinitely, but companies must pay license fees if they want access to administrative controls, including integration with user management systems like ActiveDirectory.

Yammer has a centralized Analytics team, which sits in the Engineering organization. Their primary goal is to drive better product and business decisions using data. They do this partially by providing tools and education that make other teams within Yammer more effective at using data to make better decisions. They also perform ad-hoc analysis to support specific decisions.

## The Yammer analytics philosophy

Yammer analysts are trained to constantly consider the value of each individual project; they seek to maximize the return on their time. Analysts typically opt for less precise solutions to problems if it means investing substantially less time as well.

They are also taught to consider the impact of everything on the company at large. This includes high-level decision making like choosing which projects to prioritize. It also influences the way analysts think about metrics. Product decisions are always evaluated against core engagement, retention, and growth metrics in addition to product-specific usage metrics (like, for example, the number of times someone views another user's profile).

## The cases

- A Drop in Engagement: Engagement dips—you figure out the source of the problem.
- Understanding Search: The product team is thinking about revamping search. Your job is to figure out whether they should change it at all, and if so, what should be changed.
- The Best A/B Test Ever: A new feature tests off the charts. Your job is to determine the validity of the experiment.

## Investigating a Drop in User Engagement

Yammer's Analysts are responsible for triaging product and business problems as they come up. In many cases, these problems surface through key metric dashboards that execs and managers check daily.

### The problem

You show up to work Tuesday morning, September 2, 2014. The head of the Product team walks over to your desk and asks you what you think about the latest activity on the user engagement dashboards. You fire them up, and something immediately jumps out:


The above chart shows the number of engaged users each week. Yammer defines engagement as having made some type of server call by interacting with the product (shown in the data as events of type "engagement"). Any point in this chart can be interpreted as "the number of users who logged at least one engagement event during the week starting on that date."

You are responsible for determining what caused the dip at the end of the chart shown above and, if appropriate, recommending solutions for the problem.

### Getting oriented

Before you even touch the data, come up with a list of possible causes for the dip in retention shown in the chart above. Make a list and determine the order in which you will check them. Make sure to note how you will test each hypothesis. Think carefully about the criteria you use to order them and write down the criteria as well.

Also, make sure you understand what the above chart shows and does not show.

Making hypotheses and evaluating them is often the most important part of this problem. If you do this well, you can save yourself a lot of time spent digging through data. It's impossible to provide an exhaustive list of possibilities for this kind of problem, but here are some things we came up with in our brainstorming session:

-   Holiday: It's likely that people using a work application like Yammer might engage at a lower rate on holidays. If one country has much lower engagement than others, it's possible that this is the cause.
-   Broken feature: It is possible that something in the application is broken, and therefore impossible for people to use. This is a little harder to pinpoint because different parts of the application would show differently in the metrics. For example, if something in the signup flow broke, preventing new users from joining Yammer, growth would also be down. If a mobile app was unstable and crashed, engagement would be down for only that device type.
-   Broken tracking code: It's possible that the code that logs events is, itself, broken. If you see a drop to absolutely zero events of a certain type and you rule out a broken feature, then this is a possibility.
-   Traffic anomalies from bots: Most major website see a lot of activity from bots. A change in the product or infrastructure that might make it harder for bots to interact with the site could decrease engagement (assuming bots look like real users). This is tricky to determine because you have to identify bot-like behavior through patterns or specific events.
-   Traffic shutdown to your site: It is possible for internet service providers to block your site. This is pretty rare for professional applications, but nevertheless possible.
-   Marketing event: A Super Bowl ad, for example, might cause a massive spike in sign-ups for the product. But users who enter through one-time marketing blitzes often retain at lower rates than users who are referred by friends, for example. Because the chart uses a rolling 7-day period, this will register as high engagement for one week, then almost certainly look like a big drop in engagement the following week. Most often, the best way to determine this is to simply ask someone in the Marketing department if anything big happened recently.
-   Bad data: There are lots of ways to log bad data. For example, most large web apps separate their QA data from production data. One way or another, QA data can make its way into the production database. This is not likely to be the problem in this particular case, as it would likely show up as additional data logged from very few users.
-   Search crawler changes: For a website that receives a lot of traffic, changes in the way search engines index them could cause big swings in traffic.

That's a lot of possibilities, so it's important to move through them in the most efficient order possible. Here are some suggestions for how to sort them so that you don't waste time:

-   Experience: This isn't particularly relevant for those of you who have not worked in industry before, but once you have seen these problems a couple time, you will get a sense for the most frequent problems.
-   Communication: It's really easy to ask someone about marketing events, so there's very little reason not to do that. Unfortunately, this is also irrelevant for this example, but it's certainly worth mentioning.
-   Speed: Certain scenarios are easier to test than others, sometimes because the data is cleaner or easier to understand or query, sometimes because you've done something similar in the past. If two possibilities seem equally likely, test the faster one first.
-   Dependency: If a particular scenario will be easy to understand after testing a different scenario, then test them in the order that makes sense.

### Digging in

Once you have an ordered list of possible problems, it's time to investigate.

For this problem, you will need to use four tables. The tables names and column definitions are listed below—click a table name to view information about that table. Note: this data is fake and was generated for the purpose of this case study. It is similar in structure to Yammer's actual data, but for privacy and security reasons it is not real.

**Table 1: Users**

This table includes one row per user, with descriptive information about that user's account.

| user\_id:      | A unique ID per user. Can be joined to user\_id in either of the other tables. |
| -------------- | ------------------------------------------------------------------------------ |
| created\_at:   | The time the user was created (first signed up)                                |
| state:         | The state of the user (active or pending)                                      |
| activated\_at: | The time the user was activated, if they are active                            |
| company\_id:   | The ID of the user's company                                                   |
| language:      | The chosen language of the user                                                |

**Table 2: Events**

This table includes one row per event, where an event is an action that a user has taken on Yammer. These events include login events, messaging events, search events, events logged as users progress through a signup funnel, events around received emails.

| user\_id:     | The ID of the user logging the event. Can be joined to user\\\_id in either of the other tables.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| occurred\_at: | The time the event occurred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| event\_type:  | The general event type. There are two values in this dataset: "signup\_flow", which refers to anything occuring during the process of a user's authentication, and "engagement", which refers to general product usage after the user has signed up for the first time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| event\_name:  | The specific action the user took. Possible values include: create\_user: User is added to Yammer's database during signup process enter\_email: User begins the signup process by entering her email address enter\_info: User enters her name and personal information during signup process complete\_signup: User completes the entire signup/authentication process home\_page: User loads the home page like\_message: User likes another user's message login: User logs into Yammer search\_autocomplete: User selects a search result from the autocomplete list search\_run: User runs a search query and is taken to the search results page search\_click\_result\_X: User clicks search result X on the results page, where X is a number from 1 through 10. send\_message: User posts a message view\_inbox: User views messages in her inbox |
| location:     | The country from which the event was logged (collected through IP address).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| device:       | The type of device used to log the event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

**Table 3: Email Events**

This table contains events specific to the sending of emails. It is similar in structure to the events table above.

| user\_id:     | The ID of the user to whom the event relates. Can be joined to user\_id in either of the other tables.                                                                                                                                                                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| occurred\_at: | The time the event occurred.                                                                                                                                                                                                                                                                  |
| action:       | The name of the event that occurred. "sent\_weekly\_digest" means that the user was delivered a digest email showing relevant conversations from the previous day. "email\_open" means that the user opened the email. "email\_clickthrough" means that the user clicked a link in the email. |

**Table 4: Rollup Periods**

The final table is a lookup table that is used to create rolling time periods. Though you could use the INTERVAL() function, creating rolling time periods is often easiest with a table like this. You won't necessarily need to use this table in queries that you write, but the column descriptions are provided here so that you can understand the query that creates the chart shown above.

| period\_id: | This identifies the type of rollup period. The above dashboard uses period 1007, which is rolling 7-day periods.                                                                                                                                                                                         |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| time\_id:   | This is the identifier for any given data point — it's what you would put on a chart axis. If time\_id is 2014-08-01, that means that is represents the rolling 7-day period leading up to 2014-08-01.                                                                                                   |
| pst\_start: | The start time of the period in PST. For 2014-08-01, you'll notice that this is 2014-07-25 — one week prior. Use this to join events to the table.                                                                                                                                                       |
| pst\_end:   | The start time of the period in PST. For 2014-08-01, the end time is 2014-08-01. You can see how this is used in conjunction with pst\_start to join events. |
| utc\_start: | The same as pst\_start, but in UTC time.                                                                                                                                                                                                                                                                 |
| pst\_start: | The same as pst\_end, but in UTC time.                                                                                                                                                                                                                                                                   |

### Making a recommendation

Start to work your way through your list of hypotheses in order to determine the source of the drop in engagement. As you explore, make sure to save your work. It may be helpful to start with the code that produces the above query, which you can find by clicking the link in the footer of the chart and navigating to the "query" tab.

Answer the following questions:

-   Do the answers to any of your original hypotheses lead you to further questions?
-   If so, what are they and how will you test them?
-   If they are questions that you can't answer using data alone, how would you go about answering them (hypothetically, assuming you actually worked at this company)?
-   What seems like the most likely cause of the engagement dip?
-   What, if anything, should the company do in response?

The answers to the first three questions depend heavily on the individual's approach. It would be impossible to list answers for all possible hypotheses, but here's an example of how a solid thought process might look, all the way from the beginning to the solution.

One of the easiest things to check is growth, both because it's easy to measure and because most companies (Yammer included) track this closely already. In this case, you have to make it yourself, though. You'll notice that nothing has really changed about the growth rate—it continues to be high during the week, low on weekends:


[Download query](./src/daily-signups.sql)

Since growth is normal, it's possible that the dip in engagement is coming from existing users as opposed to new ones. One of the most effective ways to look at this is to cohort users based on when they signed up for the product. This chart shows a decrease in engagement among users who signed up more than 10 weeks prior:


[Download query](./src/user-age-cohort.sql)

The understanding that the problem is localized to older users leads us to believe that the problem probably isn't related to a one-time spike from marketing traffic or something that is affecting new traffic to the site like being blocked or changing rank on search engines. Now let's take a look at various device types to see if the problem is localized to any particular product:


[Download query](./src/weekly-device.sql)

If you filter the above chart down to phones, you will see that there's a pretty steep drop in phone engagement rates. So it's likely that there's a problem with the mobile app related to long-time user retention. At this point, you're in a good position to ask around and see if anything changed recently with the mobile app to try to figure out the problem. You might also think about what causes people to engage with the product. The purpose of the digest email mentioned above is to bring users back into the product. Since we know this problem relates to the retention of long-time users, it's worth checking out whether the email has something to do with it:


[Download query](./src/weekly-emails.sql)

If you filter to clickthroughs, you'll see that clickthroughs are way down. This next chart shows in greater detail clickthrough and open rates of emails, indicating clearly that the problem has to do with digest emails in addition to mobile apps.

![](https://user-images.githubusercontent.com/62965911/215314459-8794b660-2095-4b4d-a5ce-ae60c3640261.png)

[Download query](./src/ct-rates.sql)

### Follow through

After investigation, it appears that the problem has to do with mobile use and digest emails. The intended action here should be clear: notify the head of product (who approached you in the first place) that the problem is localized in these areas and that it's worth checking to make sure something isn't broken or poorly implemented. It's not clear from the data exactly what the problem is or how it should be solved, but the above work can save other teams a lot of time in figuring out where to look.

## Understanding Search Functionality

The product team is determining priorities for the next development cycle and they are considering improving the site's search functionality. It currently works as follows:

There is a search box in the header the persists on every page of the website. It prompts users to search for people, groups, and conversations.

When the user hits enter or selects “view all results” from the dropdown, she is taken to a results page, with results separated by tabs for different categories (people, conversations, etc.). Each tab is order by relevance and chronology (more recent posts surface higher).


The search results page also has an “advanced search” box that allows the user to search again within a specific Yammer group or date range.

### The problem

Before tackling search, the product team wants to make sure that the engineering team's time will be well-spent in doing so. After all, each new feature comes at the expense of some other potential feature(s). The product team is most interested in determining whether they should even work on search in the first place and, if so, how they should modify it.

### Getting oriented

Before looking at the data, develop some hypotheses about how users might interact with search. What is the purpose of search? How would you know if it is fulfilling that purpose? How might you (quantitatively) understand the general quality of an individual user's search experience?

Framing problems simply and correctly can often save time later on. Thinking about the ultimate purpose of search right off the bat can make it easier to evaluate other parts of them problem. Search, at the most basic level, is about helping people find what they're looking for easily. A great search product achieves this quickly and with minimal work on behalf of the user.

To understand whether search is fulfilling that purpose, consider some possibilities:

-   Search use: The first thing to understand is whether anyone even uses search at all
-   Search frequency: If users search a lot, it's likely that they're getting value out of the feature ‐ with a major exception. If users search repeatedly within a short timeframe, it's likely that they're refining their terms because they were unable to find what they wanted initially.
-   Repeated terms: A better way to understand the above would be to actually compare similarity of search terms. That's much slower and more difficult to actually do than counting the number of searches a user performs in a short timeframe, so best to ignore this option.
-   Clickthroughs: If a user clicks many links in the search results, it's likely that she isn't having a great experience. However, the inverse is not necessarily true---clicking only one result does *not* imply a success. If the user clicks through one result, then refines her search, that's certainly not a great experience, so search frequency is probably a better way to understand that piece of the puzzle. Clickthroughs are, however, very useful in determining whether search rankings are good. If users frequently click low results or scroll to additional pages, then the ranking algorithm should probably be adjusted.
-   Autocomplete Clickthroughs: The autocomplete feature is certainly part of the equation, though its success should be measured separately to understand its role.

### The data

There are two tables that are relevant to this problem. Most critically, there are certain events that you will want to look into in the events table below:

-   search_autocomplete: This is logged when a user clicks on a search option from autocomplete
-   search_run: This is logged when a user runs a search and sees the search results page.
-   search_click_X: This is logged when a user clicks on a search result. X, which ranges from 1 to 10, describes which search result was clicked.

The tables names are listed below:

**Table 1: Users**

This table includes one row per user, with descriptive information about that user's account.

Same as earlier.

**Table 2: Events**

This table includes one row per event, where an event is an action that a user has taken on Yammer. These events include login events, messaging events, search events, events logged as users progress through a signup funnel, events around received emails.

Same as earlier.

### Making a recommendation

Once you have an understanding of the data, try to validate some of the hypotheses you formed earlier. In particular, you should seek to answer the following questions:

-   Are users' search experiences generally good or bad?
-   Is search worth working on at all?
-   If search is worth working on, what, specifically, should be improved?

Come up with a brief presentation describing the state of search at Yammer. Display your findings graphically. You should be prepared to recommend what, if anything, should be done to improve search. If you determine that you do not have sufficient information to test anything you deem relevant, discuss the caveats.

Finally, determine a way to understand whether your feature recommendations are actually improvements over the old search (assuming that anything you recommend will be completed).

The criteria above suggest that understanding search on a session by session basis is going to be important for this problem. So before seeking to understand whether search is good or bad, it would be wise to define a session for the purposes of this problem, both practically and in terms of the data. For the following solution, a session is defined as a string of events logged by a user without a 10-minute break between any two events. So if a user goes 10 minutes without logging an event, the session is ended and her next engagement will be considered a new session.

First, take a look at how often people search and whether that changes over time. Users take advantage of the autocomplete function more frequently than they actually run searches that take them to the search results page:

![](https://user-images.githubusercontent.com/62965911/215314452-34e395a1-fe1b-448c-92c5-22178ba6ac0e.png)

[Download query](./src/autocompletes.sql)

To be more precise, autocomplete gets used in approximately 25% of sessions, while search is only used in 8% or so. Autocomplete's 25% use indicates that there is a need for users to find information on their Yammer networks. In other words, it's a feature that people use and is worth some attention.

As you can see below, autocomplete is typically used once or twice per session:


[Download query](./src/autocompletes-session.sql)

When users do run full searches, they typically run multiple searches in a single session. Considering full search is a more rarely used feature, this suggests that either the search results are not very good or that there is a very small group of users who like search and use it all the time:


[Download query](./src/session-runs.sql)

Digging in a bit deeper, it's clear that search isn't performing particularly well. In sessions during which users do search, they almost never click any of the results:


[Download query](./src/search-run.sql)

Furthermore, more searches in a given session do not lead to many more clicks, on average:


[Download query](./src/session-search.sql)

When users do click on search results, their clicks are fairly evenly distributed across the result order, suggesting the ordering is not very good. If search were performing well, this would be heavily weighted toward the top two or three results:

![](https://user-images.githubusercontent.com/62965911/215314472-54b659d5-8dbb-47a8-9f77-f2f2bee678da.png)

[Download query](./src/search-result.sql)

Finally, users who run full searches rarely do so again within the following month:


[Download query](./src/first-search.sql)

Users who use the autocomplete feature, by comparison, continue to use it at a higher rate:


[Download query](./src/first-autocomplete.sql)

### Follow through

This all suggests that autocomplete is performing reasonably well, while search runs are not. The most obvious place to focus is on the ordering of search results. It's important to consider that users likely run full searches when autocomplete does not provide the things they are looking for, so maybe changing the search ranking algorithm to provide results that are a bit different from the autocomplete results would help. Of course, there are many ways to approach the problem—the important thing is that the focus should be on improving full search results.

## Validating A/B Test Results

Yammer not only develops new features, but is continuously looking for ways to improving existing ones. Like many software companies, Yammer frequently tests these features before releasing them to all of their customers. These A/B tests help analysts and product managers better understand a feature's effect on user behavior and the overall user experience.

This case focuses on an improvement to Yammer's core “publisher”—the module at the top of a Yammer feed where users type their messages. To test this feature, the product team ran an A/B test from June 1 through June 30. During this period, some users who logged into Yammer were shown the old version of the publisher (the “control group”), while other other users were shown the new version (the “treatment group”).


### The problem

On July 1, you check the results of the A/B test. You notice that message posting is 50% higher in the treatment group—a huge increase in posting. The table below summarizes the results:


[Download query](./src/msg-sent.sql)

The chart shows the average number of messages posted per user by treatment group. The table below provides additional test result details:

-   users: The total number of users shown that version of the publisher.
-   total_treated_users: The number of users who were treated in either group.
-   treatment_percent: The number of users in that group as a percentage of the total number of treated users.
-   total: The total number of messages posted by that treatment group.
-   average: The average number of messages per user in that treatment group (total/users).
-   rate_difference: The difference in posting rates between treatment groups (group average - control group average).
-   rate_lift: The percent difference in posting rates between treatment groups ((group average / control group average) - 1).
-   stdev: The standard deviation of messages posted per user for users in the treatment group. For example, if there were three people in the control group and they posted 1, 4, and 8 messages, this value would be the standard deviation of 1, 4, and 8 (which is 2.9).
-   t_stat: A [test statistic](http://en.wikipedia.org/wiki/Student's_t-test) for calculating if average of the treatment group is statistically different from the average of the control group. It is calculated using the averages and standard deviations of the treatment and control groups.
-   p_value: Used to determine the test's statistical significance.

The test above, which compares average posting rates between groups, uses a simple [Student's t-test](http://en.wikipedia.org/wiki/Student's_t-test) for determining statistical signficance. For testing on averages, t-tests are common, though other, more advanced statistical techniques are sometimes used. Furthermore, the test above uses a two-tailed test because the treatment group could perform either better or worse than the control group. ([Some argue](https://help.optimizely.com/hc/en-us/articles/200133789-How-long-to-run-a-test#calculating_significance) that one-tailed tests are better, however.) You can read more about the differences between one- and two-tailed t-tests [here](http://www.ats.ucla.edu/stat/mult_pkg/faq/general/tail_tests.htm).

Once you're comfortable with A/B testing, your job is to determine whether this feature is the real deal or too good to be true. The product team is looking to you for advice about this test, and you should try to provide as much information about what happened as you can.

### Getting oriented

Before doing anything with the data, develop some hypotheses about why the result might look the way it does, as well as methods for testing those hypotheses. As a point of reference, such dramatic changes in user behavior—like the 50% increase in posting—are extremely uncommon.

A/B tests can alter user behavior in a lot of ways, and sometimes these changes are unexpected. Before digging around test data, it's important to hypothesize how a feature might change user behavior, and why. If you identify changes in the data first, it can be very easy to rationalize why these changes should be obvious, even if you never would have have thought of them before the experiment.

It's similarly important to develop hypotheses for explaining test results before looking further into the data. These hypotheses focus your thinking, provide specific conclusions to validate, and keep you from always concluding that the first potential answer you find is the right one.

For this problem, a number of factors could explain the anomalous test. Here are a few examples:

-   This metric is incorrect or irrelevant: Posting rates may not be the correct metric for measuring overall success. It describes how Yammer's customers *use* the tool, but not necessarily if they're getting value out of it. For example, while a giant "Post New Message" button would probably increase posting rates, it's likely not a great feature for Yammer. You may want to make sure the test results hold up for other metrics as well.
-   The test was calculated incorrectly: A/B tests are statistical tests. People calculate results using different methods---sometimes that method is incorrect, and sometimes the arithmetic is done poorly.
-   The users were treated incorrectly: Users are supposed to be assigned to test treatments randomly, but sometimes bugs interfere with this process. If users are treated incorrectly, the experiment may not actually be random.
-   There is a confounding factor or interaction effect: These are the trickiest to identify. Experiment treatments could be affecting the product in some other way---for example, it could make some other feature harder to find or create incongruous mobile and desktop experiences. These changes might affect user behavior in unexpected ways, or amplify changes beyond what you would typically expect.

### The data

For this problem, you will need to use four tables. The tables names and column definitions are listed below—click a table name to view information about that table. Note: This data is fake and was generated for the purpose of this case study. It is similar in structure to Yammer's actual data, but for privacy and security reasons, it is not real.

**Table 1: Users**

This table includes one row per user, with descriptive information about that user's account.

Same as earlier.

**Table 2: Events**

This table includes one row per event, where an event is an action that a user has taken on Yammer. These events include login events, messaging events, search events, events logged as users progress through a signup funnel, events around received emails.

Same as earlier.

**Table 3: Experiments**

This table shows which groups users are sorted into for experiments. There should be one row per user, per experiment (a user should not be in both the test and control groups in a given experiment).

| user\_id:          | The ID of the user logging the event. Can be joined to user\_id in either of the other tables.                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| occurred\_at:      | The time the user was treated in that particular group.                                                                         |
| experiment:        | The name of the experiment. This indicates what actually changed in the product during the experiment.                          |
| experiment\_group: | The group into which the user was sorted. "test\_group" is the new version of the feature; "control\_group" is the old version. |
| location:          | The country in which the user was located when sorted into a group (collected through IP address).                              |
| device:            | The type of device used to log the event.                                                                                       |

**Table 4: Normal Distribution**

This table is purely a lookup table, similar to what you might find in the back of a statistics textbook. It is equivalent to using the leftmost column [in this table](https://www.stat.tamu.edu/~lzhou/stat302/standardnormaltable.pdf), though it omits negative Z-Scores.

| score: | Z-score. Note that this table only contains values >= 0, so you will need to join the absolute value of the Z-score against it. |
| ------ | ------------------------------------------------------------------------------------------------------------------------------- |
| value: | The area on a normal distribution below the Z-Score.                                                                            |

### Validating the results

Work through your list of hypotheses to determine whether the test results are valid. We suggest following the steps (and answer the questions) below:

-   Check to make sure that this test was run correctly. Is the query that calculates lift and p-value correct? It may be helpful to start with the code that produces the above query, which you can find by clicking the link in the footer of the chart and navigating to the "query" tab.
-   Check other metrics to make sure that this outsized result is not isolated to this one metric. What other metrics are important? Do they show similar improvements? This will require writing additional SQL queries to test other metrics.
-   Check that the data is correct. Are there problems with the way the test results were recorded or the way users were treated into test and control groups? If something is incorrect, determine the steps necessary to correct the problem.
-   Make a final recommendation based on your conclusions. Should the new publisher be rolled out to everyone? Should it be re-tested? If so, what should be different? Should it be abandoned entirely?

The number of messages sent shouldn't be the only determinant of this test's success, so dig into a few other metrics to make sure that their outcomes were also positive. In particular, we're interested in metrics that determine if a user is getting value out of Yammer. (Yammer typically uses login frequency as a core value metric.)

First, the average number of logins per user is up. This suggests that not only are users sending more messages, but they're also signing in to Yammer more.


[Download query](./src/avg-logins.sql)

Second, users are logging in on more days as well (days engaged the distinct number of days customers use Yammer). If this metric were flat and logins were up, it might imply that people were logging in and logging out in quick succession, which could mean the new feature introduced a login bug. But both metrics are up, so it appears that the problem with this tests isn't cherry-picking metrics---things look good across the board.


[Download query](./src/avg-days.sql)

Reasonable people can debate which mathematical methods are best for an A/B test, and arguments can be made for some changes (1-tailed vs. 2-tailed tests, required sample sizes, assumptions about sample distributions, etc.). Nontheless, these other methods don't materially affect the test results here. For more on the math behind A/B testing, this [brief Amazon primer](https://developer.amazon.com/sdk/ab-testing/reference/ab-math.html) offers good information, as does [Evan Miller's blog](http://www.evanmiller.org/index.html).

The test, however, does suffer from a methodological error. The test lumps new users and existing users into the same group, and measures the number of messages they post during the testing window. This means that a user who signed up in January would be considered the same way as a user who signed up a day before the test ended, even though the second user has much less time to post messages. It would make more sense to consider new and existing users separately. Not only does this make comparing magnitudes more appropriate, be it also lets you test for novelty effects. Users familiar with Yammer might try out a new feature just because it's new, temporarily boosting their overall engagement. For new users, the feature isn't "new," so they're much less likely to use it just because it's different.

Investigating user treatments (or splitting users out into new and existing cohorts) reveals the heart of the problem---all new users were treated in the control group.


[Download query](./src/month-active.sql)

This creates a number of problems for the test. Because these users have less time to post than existing users, all else equal, they would be expected to post less than existing users given their shorter exposure to Yammer. Including all of them in the control group lowers that group's overall posting rate. Because of this error, you may want to analyze the test in a way that ignores new users. As you can see from below, when only looking at posts from new users, the test results narrow considerably.

![](https://user-images.githubusercontent.com/62965911/215314458-9518abfb-8d9d-444d-8d41-5b8a4da781ee.png)

[Download query](./src/avg-msg.sql)

Though we've identified one problem, it's usually a good idea to explore other possibilities as well. There can be multiple problems, and frequently, these problems are related. When recommending what to next to product teams, it's important to have a complete understanding of what happened during a test---both the expected results and unexpected ones.

Interaction effects can appear in many ways, so it's not possible to list all of the possibilities here. However, a few cohorts---new vs. existing users, usage by device, usage by user type (i.e., content producers vs. readers)---are usually good to check.

### Follow through

Overall, the test results are still strong. But given the above result, we should validate that change across different cohorts and fix the logging error that treated all new users in one group.

## Conclusion

Congratulations on finishing this SQL Tutorial! You're more than ready to apply your skills to real analytical problems. Of course, the tricky part comes in applying these tools in unfamiliar situations, so expect to get stumped every now and again.

## Solution

```
.
├── [ 24M]  data
│   ├── [6.3M]  dimension_rollup_periods.csv
│   ├── [4.6M]  yammer_emails.csv
│   ├── [1.5M]  yammer_events_user_type_1.csv
│   ├── [5.3M]  yammer_events_user_type_2.csv
│   ├── [4.4M]  yammer_events_user_type_3.csv
│   ├── [244K]  yammer_experiments.csv
│   └── [1.2M]  yammer_users.csv
├── [ 45K]  README.md
└── [ 31K]  src
    ├── [2.1K]  autocompletes-session.sql
    ├── [2.3K]  autocompletes.sql
    ├── [2.3K]  avg-days.sql
    ├── [2.3K]  avg-logins.sql
    ├── [2.4K]  avg-msg.sql
    ├── [1.7K]  ct-rates.sql
    ├── [ 292]  daily-signups.sql
    ├── [2.4K]  first-autocomplete.sql
    ├── [2.3K]  first-search.sql
    ├── [ 391]  month-active.sql
    ├── [2.3K]  msg-sent.sql
    ├── [ 194]  search-result.sql
    ├── [2.1K]  search-run.sql
    ├── [2.1K]  session-runs.sql
    ├── [2.1K]  session-search.sql
    ├── [1.9K]  user-age-cohort.sql
    ├── [ 961]  weekly-device.sql
    └── [ 521]  weekly-emails.sql

  25M used in 3 directories, 25 files
```