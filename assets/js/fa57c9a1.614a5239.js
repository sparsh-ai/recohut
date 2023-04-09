"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[48207],{3905:(e,t,n)=>{n.d(t,{Zo:()=>d,kt:()=>p});var a=n(67294);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function r(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,a,i=function(e,t){if(null==e)return{};var n,a,i={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(i[n]=e[n]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}var l=a.createContext({}),u=function(e){var t=a.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):r(r({},t),e)),n},d=function(e){var t=u(e.components);return a.createElement(l.Provider,{value:t},e.children)},c={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},m=a.forwardRef((function(e,t){var n=e.components,i=e.mdxType,o=e.originalType,l=e.parentName,d=s(e,["components","mdxType","originalType","parentName"]),m=u(n),p=i,h=m["".concat(l,".").concat(p)]||m[p]||c[p]||o;return n?a.createElement(h,r(r({ref:t},d),{},{components:n})):a.createElement(h,r({ref:t},d))}));function p(e,t){var n=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var o=n.length,r=new Array(o);r[0]=m;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:i,r[1]=s;for(var u=2;u<o;u++)r[u]=n[u];return a.createElement.apply(null,r)}return a.createElement.apply(null,n)}m.displayName="MDXCreateElement"},18382:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>r,default:()=>c,frontMatter:()=>o,metadata:()=>s,toc:()=>u});var a=n(87462),i=(n(67294),n(3905));const o={},r="GCP Bigquery Query Optimization",s={unversionedId:"storage/lab-bigquery-query-optimization/README",id:"storage/lab-bigquery-query-optimization/README",title:"GCP Bigquery Query Optimization",description:"Objective",source:"@site/docs/02-storage/lab-bigquery-query-optimization/README.md",sourceDirName:"02-storage/lab-bigquery-query-optimization",slug:"/storage/lab-bigquery-query-optimization/",permalink:"/docs/storage/lab-bigquery-query-optimization/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"BigQuery Optimization",permalink:"/docs/storage/lab-bigquery-optimization/"},next:{title:"Building a BigQuery Data Warehouse",permalink:"/docs/storage/lab-biqeury-building-warehouse/"}},l={},u=[{value:"Objective",id:"objective",level:2},{value:"Task 1. Minimize I/O",id:"task-1-minimize-io",level:2},{value:"Be purposeful in SELECT",id:"be-purposeful-in-select",level:3},{value:"Reduce data being read",id:"reduce-data-being-read",level:3},{value:"Reduce number of expensive computations",id:"reduce-number-of-expensive-computations",level:3},{value:"Task 2. Cache results of previous queries",id:"task-2-cache-results-of-previous-queries",level:2},{value:"Cache intermediate results",id:"cache-intermediate-results",level:3},{value:"Accelerate queries with BI Engine",id:"accelerate-queries-with-bi-engine",level:3},{value:"Task 3. Efficient joins",id:"task-3-efficient-joins",level:2},{value:"Denormalization",id:"denormalization",level:3},{value:"Avoid self-joins of large tables",id:"avoid-self-joins-of-large-tables",level:3},{value:"Reduce data being joined",id:"reduce-data-being-joined",level:3},{value:"Use a window function instead of a self-join",id:"use-a-window-function-instead-of-a-self-join",level:3},{value:"Join with precomputed values",id:"join-with-precomputed-values",level:3},{value:"Task 4. Avoid overwhelming a worker",id:"task-4-avoid-overwhelming-a-worker",level:2},{value:"Limiting large sorts",id:"limiting-large-sorts",level:3},{value:"Data skew",id:"data-skew",level:3},{value:"Task 5. Approximate aggregation functions",id:"task-5-approximate-aggregation-functions",level:2},{value:"Approximate count",id:"approximate-count",level:3}],d={toc:u};function c(e){let{components:t,...n}=e;return(0,i.kt)("wrapper",(0,a.Z)({},d,n,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"gcp-bigquery-query-optimization"},"GCP Bigquery Query Optimization"),(0,i.kt)("h2",{id:"objective"},"Objective"),(0,i.kt)("p",null,"Optimizing your BigQuery Queries for Performance"),(0,i.kt)("p",null,"Performance tuning of BigQuery is usually carried out because we wish to reduce query execution times or cost. In this lab, we will look at a number of performance optimizations that might work for your use case. Performance tuning should be carried out only at the end of the development stage, and only if it is observed that typical queries take too long."),(0,i.kt)("p",null,"It is far better to have flexible table schemas and elegant, readable, and maintainable queries than to obfuscate table layouts and queries in search of a tiny bit of performance. However, there will be instances where you do need to improve the performance of your queries, perhaps because they are carried out so often that small improvements are meaningful. Another aspect is that knowledge of performance tradeoffs can help you in deciding between alternative designs."),(0,i.kt)("p",null,"In this lab, you learn about the following techniques for reducing BigQuery execution times and costs:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Minimizing I/O"),(0,i.kt)("li",{parentName:"ul"},"Caching results of previous queries"),(0,i.kt)("li",{parentName:"ul"},"Performing efficient joins"),(0,i.kt)("li",{parentName:"ul"},"Avoid overwhelming single workers"),(0,i.kt)("li",{parentName:"ul"},"Using approximate aggregation functions")),(0,i.kt)("h2",{id:"task-1-minimize-io"},"Task 1. Minimize I/O"),(0,i.kt)("p",null,"A query that computes the sum of three columns will be slower than a query that computes the sum of two columns, but most of the performance difference will be due to reading more data, not the extra addition. Therefore, a query that computes the mean of a column will be nearly as fast as a query whose aggregation method is to compute the variance of the data (even though computing variance requires BigQuery to keep track of both the sum and the sum of the squares) because most of the overhead of simple queries is caused by I/O, not by computation."),(0,i.kt)("h3",{id:"be-purposeful-in-select"},"Be purposeful in SELECT"),(0,i.kt)("p",null,"Because BigQuery uses columnar file formats, the fewer the columns that are read in a SELECT, the less the amount of data that needs to be read. In particular, doing a SELECT * reads every column of every row in the table, making it quite slow and expensive."),(0,i.kt)("p",null,"The exception is when you use a SELECT * in a subquery, then only reference a few fields in an outer query; the BigQuery optimizer will be smart enough to only read the columns that are absolutely required."),(0,i.kt)("p",null,"Execute the following query in the BigQuery EDITOR window:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  bike_id,\n  duration\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire\nORDER BY\n  duration DESC\nLIMIT\n  1\n")),(0,i.kt)("p",null,"In the Query results window notice that the query completed in ~1.2s and processed ~372MB of data."),(0,i.kt)("p",null,"Execute the following query in the BigQuery EDITOR window:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  *\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire\nORDER BY\n  duration DESC\nLIMIT\n  1\n")),(0,i.kt)("p",null,"In the Query results window notice that this query completed in ~4.5s and consumed ~2.6GB of data. Much longer!"),(0,i.kt)("p",null,"If you require nearly all the columns in a table, consider using SELECT * EXCEPT so as to not read the ones you don\u2019t require."),(0,i.kt)("admonition",{type:"note"},(0,i.kt)("p",{parentName:"admonition"},"BigQuery will cache query results to speed up repeat queries. Turn off this cache to see actual query processing performance by clicking More > Query settings and un-checking Use cached results.")),(0,i.kt)("h3",{id:"reduce-data-being-read"},"Reduce data being read"),(0,i.kt)("p",null,"When tuning a query, it is important to start with the data that is being read and consider whether it is possible to reduce this. Suppose we wish to find the typical duration of the most common one-way rentals."),(0,i.kt)("p",null,"Execute the following query into the BigQuery editor window:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  MIN(start_station_name) AS start_station_name,\n  MIN(end_station_name) AS end_station_name,\n  APPROX_QUANTILES(duration, 10)[OFFSET (5)] AS typical_duration,\n  COUNT(duration) AS num_trips\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire\nWHERE\n  start_station_id != end_station_id\nGROUP BY\n  start_station_id,\n  end_station_id\nORDER BY\n  num_trips DESC\nLIMIT\n  10\n")),(0,i.kt)("p",null,"Click on the Execution details tab of the Query results window."),(0,i.kt)("p",null,"The details of the query indicate that the sorting (for the approximate quantiles for every station pair) required a repartition of the outputs of the input stage but most of the time is spent during computation."),(0,i.kt)("p",null,"We can reduce the I/O overhead of the query if we do the filtering and grouping using the station name rather than the station id since we will need to read fewer columns. Execute the following query:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  start_station_name,\n  end_station_name,\n  APPROX_QUANTILES(duration, 10)[OFFSET(5)] AS typical_duration,\n  COUNT(duration) AS num_trips\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire\nWHERE\n  start_station_name != end_station_name\nGROUP BY\n  start_station_name,\n  end_station_name\nORDER BY\n  num_trips DESC\nLIMIT\n  10\n")),(0,i.kt)("p",null,"The above query avoids the need to read the two id columns and finishes in 10.8 seconds. This speedup is caused by the downstream effects of reading less data."),(0,i.kt)("p",null,"The query result remains the same since there is a 1:1 relationship between the station name and the station id."),(0,i.kt)("h3",{id:"reduce-number-of-expensive-computations"},"Reduce number of expensive computations"),(0,i.kt)("p",null,"Suppose we wish to find the total distance traveled by each bicycle in our dataset."),(0,i.kt)("p",null,"A naive way to do this would be to find the distance traveled in each trip undertaken by each bicycle and sum them up:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"WITH\n  trip_distance AS (\nSELECT\n  bike_id,\n  ST_Distance(ST_GeogPoint(s.longitude,\n      s.latitude),\n    ST_GeogPoint(e.longitude,\n      e.latitude)) AS distance\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire,\n  `bigquery-public-data`.london_bicycles.cycle_stations s,\n  `bigquery-public-data`.london_bicycles.cycle_stations e\nWHERE\n  start_station_id = s.id\n  AND end_station_id = e.id )\nSELECT\n  bike_id,\n  SUM(distance)/1000 AS total_distance\nFROM\n  trip_distance\nGROUP BY\n  bike_id\nORDER BY\n  total_distance DESC\nLIMIT\n  5\n")),(0,i.kt)("p",null,"The above query takes 9.8 seconds (55 seconds of slot time) and shuffles 1.22 MB. The result is that some bicycles have been ridden nearly 6000 kilometers."),(0,i.kt)("p",null,"Computing the distance is a pretty expensive operation and we can avoid joining the cycle_stations table against the cycle_hire table if we precompute the distances between all pairs of stations:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"WITH\n  stations AS (\nSELECT\n  s.id AS start_id,\n  e.id AS end_id,\n  ST_Distance(ST_GeogPoint(s.longitude,\n      s.latitude),\n    ST_GeogPoint(e.longitude,\n      e.latitude)) AS distance\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_stations s,\n  `bigquery-public-data`.london_bicycles.cycle_stations e ),\ntrip_distance AS (\nSELECT\n  bike_id,\n  distance\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire,\n  stations\nWHERE\n  start_station_id = start_id\n  AND end_station_id = end_id )\nSELECT\n  bike_id,\n  SUM(distance)/1000 AS total_distance\nFROM\n  trip_distance\nGROUP BY\n  bike_id\nORDER BY\n  total_distance DESC\nLIMIT\n  5\n")),(0,i.kt)("p",null,"This query only makes 600k geo-distance calculations vs. 24M previously. Now it takes 31.5 seconds of slot time (a 30% speedup), despite shuffling 33.05MB of data."),(0,i.kt)("h2",{id:"task-2-cache-results-of-previous-queries"},"Task 2. Cache results of previous queries"),(0,i.kt)("p",null,"The BigQuery service automatically caches query results in a temporary table. If the identical query is submitted within approximately 24 hours, the results are served from this temporary table without any recomputation. Cached results are extremely fast and do not incur charges."),(0,i.kt)("p",null,"There are, however, a few caveats to be aware of. Query caching is based on exact string comparison. So even whitespaces can cause a cache miss. Queries are never cached if they exhibit non-deterministic behavior (for example, they use CURRENT_TIMESTAMP or RAND), if the table or view being queried has changed (even if the columns/rows of interest to the query are unchanged), if the table is associated with a streaming buffer (even if there are no new rows), if the query uses DML statements, or queries external data sources."),(0,i.kt)("h3",{id:"cache-intermediate-results"},"Cache intermediate results"),(0,i.kt)("p",null,"It is possible to improve overall performance at the expense of increased I/O by taking advantage of temporary tables and materialized views."),(0,i.kt)("p",null,"For example, suppose you have a number of queries that start out by finding the typical duration of trips between a pair of stations. The WITH clause (also called a Common Table Expression) improves readability but does not improve query speed or cost since results are not cached. The same holds for views and subqueries as well. If you find yourself using a WITH clause, view, or a subquery often, one way to potentially improve performance is to store the result into a table (or materialized view)."),(0,i.kt)("p",null,"First you will need to create a dataset named mydataset in the eu (multiple regions in European Union) region (where the bicycle data resides) under your project in BigQuery."),(0,i.kt)("p",null,"In the left pane in the Explorer section, click on the View action icon (three dots) near your BigQuery project (qwiklabs-gcp-xxxx) and select Create dataset."),(0,i.kt)("p",null,"In the Create dataset dialog:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Set the Dataset ID to mydataset."),(0,i.kt)("li",{parentName:"ul"},"Set the Data location to eu (multiple regions in European Union)."),(0,i.kt)("li",{parentName:"ul"},"Leave all other options at their default values.")),(0,i.kt)("p",null,"To finish, click the blue CREATE DATASET button."),(0,i.kt)("p",null,"Now you may execute the following query:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"CREATE OR REPLACE TABLE\n  mydataset.typical_trip AS\nSELECT\n  start_station_name,\n  end_station_name,\n  APPROX_QUANTILES(duration, 10)[OFFSET (5)] AS typical_duration,\n  COUNT(duration) AS num_trips\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire\nGROUP BY\n  start_station_name,\n  end_station_name\n")),(0,i.kt)("p",null,"Use the table created to find days when bicycle trips are much longer than usual:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  EXTRACT (DATE\n  FROM\n    start_date) AS trip_date,\n  APPROX_QUANTILES(duration / typical_duration, 10)[OFFSET(5)] AS ratio,\n  COUNT(*) AS num_trips_on_day\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire AS hire\nJOIN\n  mydataset.typical_trip AS trip\nON\n  hire.start_station_name = trip.start_station_name\n  AND hire.end_station_name = trip.end_station_name\n  AND num_trips > 10\nGROUP BY\n  trip_date\nHAVING\n  num_trips_on_day > 10\nORDER BY\n  ratio DESC\nLIMIT\n  10\n")),(0,i.kt)("p",null,"Use the WITH clause to find days when bicycle trips are much longer than usual:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"WITH\ntypical_trip AS (\nSELECT\n  start_station_name,\n  end_station_name,\n  APPROX_QUANTILES(duration, 10)[OFFSET (5)] AS typical_duration,\n  COUNT(duration) AS num_trips\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire\nGROUP BY\n  start_station_name,\n  end_station_name )\nSELECT\n  EXTRACT (DATE\n  FROM\n    start_date) AS trip_date,\n  APPROX_QUANTILES(duration / typical_duration, 10)[\nOFFSET\n  (5)] AS ratio,\n  COUNT(*) AS num_trips_on_day\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire AS hire\nJOIN\n  typical_trip AS trip\nON\n  hire.start_station_name = trip.start_station_name\n  AND hire.end_station_name = trip.end_station_name\n  AND num_trips > 10\nGROUP BY\n  trip_date\nHAVING\n  num_trips_on_day > 10\nORDER BY\n  ratio DESC\nLIMIT\n10\n")),(0,i.kt)("p",null,"Notice the ~50% speedup since the average trip duration computation is avoided. Both queries return the same result, that trips on Christmas take longer than usual. Note, the table mydataset.typical_trip is not refreshed when new data is added to the cycle_hire table."),(0,i.kt)("p",null,"One way to solve this problem of stale data is to use a materialized view or to schedule queries to update the table periodically. You should measure the cost of such updates to see whether the improvement in query performance makes up for the extra cost of maintaining the table or materialized view up-to-date."),(0,i.kt)("h3",{id:"accelerate-queries-with-bi-engine"},"Accelerate queries with BI Engine"),(0,i.kt)("p",null,"If there are tables that you access frequently in Business Intelligence (BI) settings such as dashboards with aggregations and filters, one way to speed up your queries is to employ BI Engine. It will automatically store relevant pieces of data in memory (either actual columns from the table or derived results), and will use a specialized query processor tuned for working with mostly in-memory data. You can reserve the amount of memory (up to a current maximum of 10 GB) that BigQuery should use for its cache from the BigQuery Admin Console, under BI Engine."),(0,i.kt)("p",null,"Make sure to reserve this memory in the same region as the dataset you are querying. Then, BigQuery will start to cache tables, parts of tables, and aggregations in memory and serve results faster."),(0,i.kt)("p",null,"A primary use case for BI Engine is for tables that are accessed from dashboard tools such as Google Data Studio. By providing memory allocation for a BI Engine reservation, we can make dashboards that rely on a BigQuery backend much more responsive."),(0,i.kt)("h2",{id:"task-3-efficient-joins"},"Task 3. Efficient joins"),(0,i.kt)("p",null,"Joining two tables requires data coordination and is subject to limitations imposed by the communication bandwidth between slots. If it is possible to avoid a join, or reduce the amount of data being joined, do so."),(0,i.kt)("h3",{id:"denormalization"},"Denormalization"),(0,i.kt)("p",null,"One way to improve the read performance and avoid joins is to give up on storing data efficiently, and instead add redundant copies of data. This is called denormalization."),(0,i.kt)("p",null,"Thus, instead of storing the bicycle station latitudes and longitudes separately from the cycle hire information, we could create a denormalized table:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"CREATE OR REPLACE TABLE\n  mydataset.london_bicycles_denorm AS\nSELECT\n  start_station_id,\n  s.latitude AS start_latitude,\n  s.longitude AS start_longitude,\n  end_station_id,\n  e.latitude AS end_latitude,\n  e.longitude AS end_longitude\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire AS h\nJOIN\n  `bigquery-public-data`.london_bicycles.cycle_stations AS s\nON\n  h.start_station_id = s.id\nJOIN\n  `bigquery-public-data`.london_bicycles.cycle_stations AS e\nON\n  h.end_station_id = e.id\n")),(0,i.kt)("p",null,"Then, all subsequent queries will not need to carry out the join because the table will contain the necessary location information for all trips."),(0,i.kt)("p",null,"In this case, you are trading off storage and reading more data against the computational expense of a join. It is quite possible that the cost of reading more data from disk will outweigh the cost of the join -- you should measure whether denormalization brings performance benefits."),(0,i.kt)("h3",{id:"avoid-self-joins-of-large-tables"},"Avoid self-joins of large tables"),(0,i.kt)("p",null,"Self-joins happen when a table is joined with itself. While BigQuery supports self-joins, they can lead to performance degradation if the table being joined with itself is very large. In many cases, you can avoid the self-join by taking advantage of SQL features such as aggregation and window functions."),(0,i.kt)("p",null,"Let\u2019s look at an example. One of the BigQuery public datasets is the dataset of baby names published by the US Social Security Administration."),(0,i.kt)("p",null,"It is possible to query the dataset to find the most common male names in 2015 in the state of Massachusetts (Make sure your query is running in the us (multiple regions in United States) region. Click Compose New Query then select More > Query settings > Additional settings > Data location):"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  name,\n  number AS num_babies\nFROM\n  `bigquery-public-data`.usa_names.usa_1910_current\nWHERE\n  gender = 'M'\n  AND year = 2015\n  AND state = 'MA'\nORDER BY\n  num_babies DESC\nLIMIT\n  5\n")),(0,i.kt)("p",null,"Similarly, query the dataset to find the most common female names in 2015 in the state of Massachusetts."),(0,i.kt)("p",null,"What are the most common names assigned to both male and female babies in the country over all the years in the dataset? A naive way to solve this problem involves reading the input table twice and doing a self-join:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"WITH\nmale_babies AS (\nSELECT\n  name,\n  number AS num_babies\nFROM\n  `bigquery-public-data`.usa_names.usa_1910_current\nWHERE\n  gender = 'M' ),\nfemale_babies AS (\nSELECT\n  name,\n  number AS num_babies\nFROM\n  `bigquery-public-data`.usa_names.usa_1910_current\nWHERE\n  gender = 'F' ),\nboth_genders AS (\nSELECT\n  name,\n  SUM(m.num_babies) + SUM(f.num_babies) AS num_babies,\n  SUM(m.num_babies) / (SUM(m.num_babies) + SUM(f.num_babies)) AS frac_male\nFROM\n  male_babies AS m\nJOIN\n  female_babies AS f\nUSING\n  (name)\nGROUP BY\n  name )\nSELECT\n  *\nFROM\n  both_genders\nWHERE\n  frac_male BETWEEN 0.3\n  AND 0.7\nORDER BY\n  num_babies DESC\nLIMIT\n  5\n")),(0,i.kt)("p",null,"To add insult to injury, the answer is also wrong -- as much as we like the name Jordan, the entire US population is only 300 million, so there cannot have been 982 million babies with that name. The self-JOIN unfortunately joins across state and year boundaries."),(0,i.kt)("p",null,"A faster, more elegant (and correct!) solution is to recast the query to read the input only once and avoid the self-join completely:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"WITH\nall_babies AS (\nSELECT\n  name,\n  SUM(\n  IF\n    (gender = 'M',\n      number,\n      0)) AS male_babies,\n  SUM(\n  IF\n    (gender = 'F',\n      number,\n      0)) AS female_babies\nFROM\n  `bigquery-public-data.usa_names.usa_1910_current`\nGROUP BY\n  name ),\nboth_genders AS (\nSELECT\n  name,\n  (male_babies + female_babies) AS num_babies,\n  SAFE_DIVIDE(male_babies,\n    male_babies + female_babies) AS frac_male\nFROM\n  all_babies\nWHERE\n  male_babies > 0\n  AND female_babies > 0 )\nSELECT\n  *\nFROM\n  both_genders\nWHERE\n  frac_male BETWEEN 0.3\n  AND 0.7\nORDER BY\n  num_babies DESC\nLIMIT\n  5\n")),(0,i.kt)("p",null,"This took only 2.4 seconds, a 30x speedup."),(0,i.kt)("h3",{id:"reduce-data-being-joined"},"Reduce data being joined"),(0,i.kt)("p",null,"It is possible to carry out the query above with an efficient join as long as we reduce the amount of data being joined by grouping the data by name and gender early on:"),(0,i.kt)("p",null,"Try the following query:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"WITH\nall_names AS (\nSELECT\n  name,\n  gender,\n  SUM(number) AS num_babies\nFROM\n  `bigquery-public-data`.usa_names.usa_1910_current\nGROUP BY\n  name,\n  gender ),\nmale_names AS (\nSELECT\n  name,\n  num_babies\nFROM\n  all_names\nWHERE\n  gender = 'M' ),\nfemale_names AS (\nSELECT\n  name,\n  num_babies\nFROM\n  all_names\nWHERE\n  gender = 'F' ),\nratio AS (\nSELECT\n  name,\n  (f.num_babies + m.num_babies) AS num_babies,\n  m.num_babies / (f.num_babies + m.num_babies) AS frac_male\nFROM\n  male_names AS m\nJOIN\n  female_names AS f\nUSING\n  (name) )\nSELECT\n  *\nFROM\n  ratio\nWHERE\n  frac_male BETWEEN 0.3\n  AND 0.7\nORDER BY\n  num_babies DESC\nLIMIT\n  5\n")),(0,i.kt)("p",null,"The early grouping served to trim the data early in the query, before the query performs a JOIN. That way, shuffling and other complex operations are only executed on the much smaller data and remain quite efficient. The query above finished in 2 seconds and returned the correct result."),(0,i.kt)("h3",{id:"use-a-window-function-instead-of-a-self-join"},"Use a window function instead of a self-join"),(0,i.kt)("p",null,"Suppose you wish to find the duration between a bike being dropped off and it being rented again, i.e., the duration that a bicycle stays at the station. This is an example of a dependent relationship between rows. It might appear that the only way to solve this is to join the table with itself, matching the end_date of one trip against the start_date of the next. (Make sure your query is running in the eu (multiple regions in European Union) region. Click Compose New Query and then select More > Query settings > Additional settings > Data location"),(0,i.kt)("p",null,"You can, however, avoid a self-join by using a window function:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  bike_id,\n  start_date,\n  end_date,\n  TIMESTAMP_DIFF( start_date, LAG(end_date) OVER (PARTITION BY bike_id ORDER BY start_date), SECOND) AS time_at_station\nFROM\n  `bigquery-public-data`.london_bicycles.cycle_hire\nLIMIT\n  5\n")),(0,i.kt)("p",null,"Notice that the first row has a null for time_at_station since we don\u2019t have a timestamp for the previous dropoff. After that, the time_at_station tracks the difference between the previous dropoff and the current pickup."),(0,i.kt)("p",null,"Using this, we can compute the average time that a bicycle is unused at each station and rank stations by that measure:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"WITH\n  unused AS (\n  SELECT\n    bike_id,\n    start_station_name,\n    start_date,\n    end_date,\n    TIMESTAMP_DIFF(start_date, LAG(end_date) OVER (PARTITION BY bike_id ORDER BY start_date), SECOND) AS time_at_station\n  FROM\n    `bigquery-public-data`.london_bicycles.cycle_hire )\nSELECT\n  start_station_name,\n  AVG(time_at_station) AS unused_seconds\nFROM\n  unused\nGROUP BY\n  start_station_name\nORDER BY\n  unused_seconds ASC\nLIMIT\n  5\n")),(0,i.kt)("h3",{id:"join-with-precomputed-values"},"Join with precomputed values"),(0,i.kt)("p",null,"Sometimes, it can be helpful to precompute functions on smaller tables, and then join with the precomputed values rather than repeat an expensive calculation each time."),(0,i.kt)("p",null,"For example, suppose we wish to find the pair of stations between which our customers ride bicycles at the fastest pace. To compute the pace (minutes per kilometer) at which they ride, we need to divide the duration of the ride by the distance between stations."),(0,i.kt)("p",null,"We could create a denormalized table with distances between stations and then compute the average pace:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"WITH\n  denormalized_table AS (\n  SELECT\n    start_station_name,\n    end_station_name,\n    ST_DISTANCE(ST_GeogPoint(s1.longitude,\n        s1.latitude),\n      ST_GeogPoint(s2.longitude,\n        s2.latitude)) AS distance,\n    duration\n  FROM\n    `bigquery-public-data`.london_bicycles.cycle_hire AS h\n  JOIN\n    `bigquery-public-data`.london_bicycles.cycle_stations AS s1\n  ON\n    h.start_station_id = s1.id\n  JOIN\n    `bigquery-public-data`.london_bicycles.cycle_stations AS s2\n  ON\n    h.end_station_id = s2.id ),\n  durations AS (\n  SELECT\n    start_station_name,\n    end_station_name,\n    MIN(distance) AS distance,\n    AVG(duration) AS duration,\n    COUNT(*) AS num_rides\n  FROM\n    denormalized_table\n  WHERE\n    duration > 0\n    AND distance > 0\n  GROUP BY\n    start_station_name,\n    end_station_name\n  HAVING\n    num_rides > 100 )\nSELECT\n  start_station_name,\n  end_station_name,\n  distance,\n  duration,\n  duration/distance AS pace\nFROM\n  durations\nORDER BY\n  pace ASC\nLIMIT\n  5\n")),(0,i.kt)("p",null,"The above query invokes the geospatial function ST_DISTANCE once for each row in the cycle_hire table (24 million times), takes 14.7 seconds and processes 1.9 GB."),(0,i.kt)("p",null,"Alternately, we can use the cycle_stations table to precompute the distance between every pair of stations (this is a self-join) and then join it with the reduced-size table of average duration between stations:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"WITH\n  distances AS (\n  SELECT\n    a.id AS start_station_id,\n    a.name AS start_station_name,\n    b.id AS end_station_id,\n    b.name AS end_station_name,\n    ST_DISTANCE(ST_GeogPoint(a.longitude,\n        a.latitude),\n      ST_GeogPoint(b.longitude,\n        b.latitude)) AS distance\n  FROM\n    `bigquery-public-data`.london_bicycles.cycle_stations a\n  CROSS JOIN\n    `bigquery-public-data`.london_bicycles.cycle_stations b\n  WHERE\n    a.id != b.id ),\n  durations AS (\n  SELECT\n    start_station_id,\n    end_station_id,\n    AVG(duration) AS duration,\n    COUNT(*) AS num_rides\n  FROM\n    `bigquery-public-data`.london_bicycles.cycle_hire\n  WHERE\n    duration > 0\n  GROUP BY\n    start_station_id,\n    end_station_id\n  HAVING\n    num_rides > 100 )\nSELECT\n  start_station_name,\n  end_station_name,\n  distance,\n  duration,\n  duration/distance AS pace\nFROM\n  distances\nJOIN\n  durations\nUSING\n  (start_station_id,\n    end_station_id)\nORDER BY\n  pace ASC\nLIMIT\n  5\n")),(0,i.kt)("p",null,"The recast query with the more efficient joins takes only 8.2 seconds, a 1.8x speedup and processes 554 MB, a nearly 4x reduction in cost."),(0,i.kt)("h2",{id:"task-4-avoid-overwhelming-a-worker"},"Task 4. Avoid overwhelming a worker"),(0,i.kt)("p",null,"Some operations (e.g. ordering) have to be carried out on a single worker. Having to sort too much data can overwhelm a worker\u2019s memory and result in a \u201cresources exceeded\u201d error. Avoid overwhelming the worker with too much data. As the hardware in Google data centers is upgraded, what \u201ctoo much\u201d means in this context expands over time. Currently, this is on the order of one GB."),(0,i.kt)("h3",{id:"limiting-large-sorts"},"Limiting large sorts"),(0,i.kt)("p",null,"Let\u2019s say that we wish to go through the rentals and number them 1, 2, 3, etc. in the order that the rental ended. We could do that using the ROW_NUMBER() function:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  rental_id,\n  ROW_NUMBER() OVER(ORDER BY end_date) AS rental_number\nFROM\n  `bigquery-public-data.london_bicycles.cycle_hire`\nORDER BY\n  rental_number ASC\nLIMIT\n  5\n")),(0,i.kt)("p",null,"It takes 34.5 seconds to process just 372 MB because it needs to sort the entirety of the London bicycles dataset on a single worker. Had we processed a larger dataset, it would have overwhelmed that worker."),(0,i.kt)("p",null,"We might want to consider whether it is possible to limit the large sorts and distribute them. Indeed, it is possible to extract the date from the rentals and then sort trips within each day:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"WITH\n  rentals_on_day AS (\n  SELECT\n    rental_id,\n    end_date,\n    EXTRACT(DATE\n    FROM\n      end_date) AS rental_date\n  FROM\n    `bigquery-public-data.london_bicycles.cycle_hire` )\nSELECT\n  rental_id,\n  rental_date,\n  ROW_NUMBER() OVER(PARTITION BY rental_date ORDER BY end_date) AS rental_number_on_day\nFROM\n  rentals_on_day\nORDER BY\n  rental_date ASC,\n  rental_number_on_day ASC\nLIMIT\n  5\n")),(0,i.kt)("p",null,"This takes 15.1 seconds (a 2x speedup) because the sorting can be done on just a single day of data at a time."),(0,i.kt)("h3",{id:"data-skew"},"Data skew"),(0,i.kt)("p",null,"The same problem of overwhelming a worker (in this case, overwhelm the memory of the worker) can happen during an ARRAY_AGG with GROUP BY if one of the keys is much more common than the others."),(0,i.kt)("p",null,"Because there are more than 3 million GitHub repositories and the commits are well distributed among them, this query succeeds (make sure you execute the query in the us (multiple regions in United States) processing center):"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  repo_name,\n  ARRAY_AGG(STRUCT(author,\n      committer,\n      subject,\n      message,\n      trailer,\n      difference,\n      encoding)\n  ORDER BY\n    author.date.seconds)\nFROM\n  `bigquery-public-data.github_repos.commits`,\n  UNNEST(repo_name) AS repo_name\nGROUP BY\n  repo_name\n")),(0,i.kt)("p",null,"Note, while this query will succeed, it can take upwards of 30 minutes to do so. If you understand the query, move on in the lab."),(0,i.kt)("p",null,"Most of the people using GitHub live in only a few time zones, so grouping by the timezone fails -- we are asking a single worker to sort a significant fraction of 750GB:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  author.tz_offset,\n  ARRAY_AGG(STRUCT(author,\n      committer,\n      subject,\n      message,\n      trailer,\n      difference,\n      encoding)\n  ORDER BY\n    author.date.seconds)\nFROM\n  `bigquery-public-data.github_repos.commits`\nGROUP BY\n  author.tz_offset\n")),(0,i.kt)("p",null,"If you do require sorting all the data, use more granular keys (i.e. distribute the group\u2019s data over more workers) and then aggregate the results corresponding to the desired key. For example, instead of grouping only by the time zone, it is possible to group by both timezone and repo_name and then aggregate across repos to get the actual answer for each timezone:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  repo_name,\n  author.tz_offset,\n  ARRAY_AGG(STRUCT(author,\n      committer,\n      subject,\n      message,\n      trailer,\n      difference,\n      encoding)\n  ORDER BY\n    author.date.seconds)\nFROM\n  `bigquery-public-data.github_repos.commits`,\n  UNNEST(repo_name) AS repo_name\nGROUP BY\n  repo_name,\n  author.tz_offset\n")),(0,i.kt)("p",null,"Note, while this query will succeed, it can take upwards of 15 minutes to do so. If you understand the query, move on in the lab."),(0,i.kt)("h2",{id:"task-5-approximate-aggregation-functions"},"Task 5. Approximate aggregation functions"),(0,i.kt)("p",null,"BigQuery provides fast, low-memory approximations of aggregate functions. Instead of using COUNT(DISTINCT \u2026), we can use APPROX_COUNT_DISTINCT on large data streams when a small statistical uncertainty in the result is tolerable."),(0,i.kt)("h3",{id:"approximate-count"},"Approximate count"),(0,i.kt)("p",null,"We can find the number of unique GitHub repositories using:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  COUNT(DISTINCT repo_name) AS num_repos\nFROM\n  `bigquery-public-data`.github_repos.commits,\n  UNNEST(repo_name) AS repo_name\n")),(0,i.kt)("p",null,"The above query takes 8.3 seconds to compute the correct result of 3347770."),(0,i.kt)("p",null,"Using the approximate function:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  APPROX_COUNT_DISTINCT(repo_name) AS num_repos\nFROM\n  `bigquery-public-data`.github_repos.commits,\n  UNNEST(repo_name) AS repo_name\n")),(0,i.kt)("p",null,"The above query takes 3.9 seconds (a 2x speedup) and returns an approximate result of 3399473, which overestimates the correct answer by 1.5%."),(0,i.kt)("p",null,"The approximate algorithm is much more efficient than the exact algorithm only on large datasets and is recommended in use-cases where errors of approximately 1% are tolerable. Before using the approximate function, measure your use case!"),(0,i.kt)("p",null,"Other available approximate functions include APPROX_QUANTILES to compute percentiles, APPROX_TOP_COUNT to find the top elements and APPROX_TOP_SUM to compute top elements based on the sum of an element."),(0,i.kt)("p",null,"Congratulations!"),(0,i.kt)("p",null,"You've learned about a number of techniques to potentially improve your query performance. While considering some of these techniques, remember the legendary computer scientist Donald Knuth's quote, \"Premature optimization is the root of all evil.\""))}c.isMDXComponent=!0}}]);