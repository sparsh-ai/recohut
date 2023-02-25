# SQL Assignment

**Learning goals**

- Perform analysis on data stored in relational and non-relational database systems to power strategic decision-making.
- Learn to determine, create, and execute SQL and NoSQL queries that manipulate and dissect large scale datasets.
- Leveraging the power of SQL commands, functions, and data cleaning methodologies to join, aggregate, and clean tables, as well as complete performance tune analysis to provide strategic business recommendations.
- Execute core SQL commands to define, select, manipulate, control access, aggregate and join data tables.
- Understand when and how to use subqueries, window functions as well as partitions to complete complex tasks.
- Clean data, optimize SQL queries and write select advanced JOINs to enhance analysis performance.

Following tables has been loaded for you in the shared rds postgres database (database: postgres, schema: default): `web_events`, `sales_reps`, `region`, `orders`, and `accounts`.

Note: Use LIMIT 10 in your answers to limit the output. LIMIT keyword must be the last one.

You have to write SQL queries to answer the following questions:

1. Displays all the data in the occurred_at, account_id, and channel columns of the web_events table.
2. Write a query to return the 10 earliest orders in the orders table. Include the id, occurred_at, and total_amt_usd.
3. Write a query to return the top 5 orders in terms of largest total_amt_usd. Include the id, account_id, and total_amt_usd.
4. Write a query to return the lowest 20 orders in terms of smallest total_amt_usd. Include the id, account_id, and total_amt_usd.
5. Write a query that displays the order ID, account ID, and total dollar amount for all the orders, sorted first by the account ID (in ascending order), and then by the total dollar amount (in descending order).
6. Write a query that again displays order ID, account ID, and total dollar amount for each order, but this time sorted first by total dollar amount (in descending order), and then by account ID (in ascending order).
7. Pulls the first 5 rows and all columns from the orders table that have a dollar amount of gloss_amt_usd greater than or equal to 1000.
8. Pulls the first 10 rows and all columns from the orders table that have a total_amt_usd less than 500.
9. Filter the accounts table to include the company name, website, and the primary point of contact (primary_poc) just for the Exxon Mobil company in the accounts table.
10. Using the orders table Create a column that divides the standard_amt_usd by the standard_qty to find the unit price for standard paper for each order. Limit the results to the first 10 orders, and include the id and account_id fields.
11. Write a query that finds the percentage of revenue that comes from poster paper for each order. Limit your calculations to the first 10 orders.
12. Use the accounts table to find All the companies whose names start with 'C'.
13. Use the accounts table to find All companies whose names contain the string 'one' somewhere in the name.
14. Use the accounts table to find All companies whose names end with 's'.
15. Use the accounts table to find the account name, primary_poc, and sales_rep_id for Walmart, Target, and Nordstrom.
16. Use the web_events table to find all information regarding individuals who were contacted via the channel of organic or adwords.
17. Use the accounts table to find the account name, primary poc, and sales rep id for all stores except Walmart, Target, and Nordstrom.
18. Use the web_events table to find all information regarding individuals who were contacted via any method except using organic or adwords methods.
19. Use the accounts table to find All the companies whose names do not start with 'C'.
20. All companies whose names do not contain the string 'one' somewhere in the name.
21. All companies whose names do not end with 's'.
22. Write a query that returns all the orders where the standard_qty is over 1000, the poster_qty is 0, and the gloss_qty is 0.
23. Using the accounts table, find all the companies whose names do not start with 'C' and end with 's'.
24. Write a query that displays the order date and gloss_qty data for all orders where gloss_qty is between 24 and 29.
25. Use the web_events table to find all information regarding individuals who were contacted via the organic or adwords channels, and started their account at any point in 2016, sorted from newest to oldest.
26. Find list of orders ids where either gloss_qty or poster_qty is greater than 4000. Only include the id field in the resulting table.
27. Write a query that returns a list of orders where the standard_qty is zero and either the gloss_qty or poster_qty is over 1000.
28. Find all the company names that start with a 'C' or 'W', and the primary contact contains 'ana' or 'Ana', but it doesn't contain 'eana'.
29. Show all the data from the accounts table, and all the data from the orders table.
30. Show standard_qty, gloss_qty, and poster_qty from the orders table, and the website and the primary_poc from the accounts table.
31. Join all three of these tables - web_events, orders and accounts.
32. Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for the Midwest region. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name.
33. Provide a table that provides the region for each sales_rep along with their associated accounts. This time only for accounts where the sales rep has a first name starting with S and in the Midwest region. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name.
34. Find the total amount spent on standard_amt_usd and gloss_amt_usd paper for each order in the orders table. This should give a dollar amount for each order in the table.
35. Find the standard_amt_usd per unit of standard_qty paper. Your solution should use both an aggregation and a mathematical operator.
36. Each company in the accounts table wants to create an email address for each primary_poc. The email address should be the first name of the primary_poc.last name primary_poc@companyname.com.
37. You may have noticed that in the previous question some of the company names include spaces, which will certainly not work in an email address. See if you can create an email address that will work by removing all of the spaces in the account name, but otherwise your solution should be just as above. Some helpful documentation is here: https://www.postgresql.org/docs/8.1/functions-string.html.
38. We would also like to create an initial password, which they will change after their first log in. The first password will be:
    1.  the first letter of the primary_poc's first name (lowercase), then
    2.  the last letter of their first name (lowercase),
    3.  the first letter of their last name (lowercase),
    4.  the last letter of their last name (lowercase),
    5.  the number of letters in their first name,
    6.  the number of letters in their last name, and then
    7.  the name of the company they are working with, all capitalized with no spaces.
39. Suppose the company wants to assess the performance of all the sales representatives. Each sales representative is assigned to work in a particular region. To make it easier to understand for the HR team, display the concatenated sales_reps.id, ‘_’ (underscore), and region.name as EMP_ID_REGION for each sales representative.
40. From the accounts table, display:
    1.  the name of the client,
    2.  the coordinate as concatenated (latitude, longitude),
    3.  email id of the primary point of contact as first letter of the primary_poc last letter of the primary_poc@extracted name and domain from the website.
41. From the web_events table, display the concatenated value of account_id, '' , channel, '', count of web events of the particular channel.
42. Create a running total of standard_amt_usd (in the orders table) over order time with no date truncation. Your final table should have two columns: one with the amount being added for each new row, and a second with the running total.
43. Now, modify your query from the previous question to include partitions. Still create a running total of standard_amt_usd (in the orders table) over order time, but this time, date truncate occurred_at by year and partition by that same year-truncated occurred_at variable. Your final table should have three columns: One with the amount being added for each row, one for the truncated date, and a final column with the running total within each year.
44. Show the num events for each day for each channel using the web_events table.
45. Show the avg events for each day for each channel using the web_events table.
46. Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.
47. For the region with the largest (sum) of sales total_amt_usd, how many total (count) orders were placed?
48. How many accounts had more total purchases than the account name which has bought the most standard_qty paper throughout their lifetime as a customer?
49. For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?
50. What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?

## Scores

|    | Ideal |
| -- | ----- |
| 1  | 1     |
| 2  | 1     |
| 3  | 1     |
| 4  | 1     |
| 5  | 1     |
| 6  | 1     |
| 7  | 1     |
| 8  | 1     |
| 9  | 1     |
| 10 | 1     |
| 11 | 2     |
| 12 | 1     |
| 13 | 1     |
| 14 | 1     |
| 15 | 1     |
| 16 | 1     |
| 17 | 1     |
| 18 | 1     |
| 19 | 1     |
| 20 | 1     |
| 21 | 1     |
| 22 | 1     |
| 23 | 1     |
| 24 | 1     |
| 25 | 1     |
| 26 | 1     |
| 27 | 1     |
| 28 | 3     |
| 29 | 1     |
| 30 | 1     |
| 31 | 1     |
| 32 | 2     |
| 33 | 2     |
| 34 | 1     |
| 35 | 1     |
| 36 | 3     |
| 37 | 2     |
| 38 | 4     |
| 39 | 2     |
| 40 | 3     |
| 41 | 3     |
| 42 | 2     |
| 43 | 3     |
| 44 | 3     |
| 45 | 3     |
| 46 | 5     |
| 47 | 5     |
| 48 | 3     |
| 49 | 5     |
| 50 | 5     |