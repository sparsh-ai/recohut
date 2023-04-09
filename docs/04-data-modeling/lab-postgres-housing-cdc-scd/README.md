# Housing Data Model with CDC and SCD Type 2

A critical aspect of data engineering is dealing with data change from one date to the next. In this case, we want both the current and historical value. There are many techniques and patterns to create a historical-friendly model during the ingestion and modeling phases. In this lab, we will build a data model that uses Change Data Capture and Slowly Changing Dimension Type 2 modelization to track housing prices. The code is written in Python. `pandas` and `sqlalchemy` library is used to load data from CSV files and execute SQL queries against the data warehouse.

The model will answer three following questions:

- How many offers are currently available?
- The average price.
- The average cost per m2.

Each KPI will be analyzed by the time dimension. The time dimension will be granular by day. In addition, we will consider two other factors: the type of accommodation (apartment or house) and whether or not the house already has furniture. You can change these configurations according to your needs.

To know the average price of all available offers on any day, we need to analyze not only the offers published on that day but also those that were published before and are still active. In addition, a price of an offer may change over time. This obliges us to detect changes in data and store all historical versions in the database. For example, if a property cost `500$` yesterday but only `480$` today. The value used to compute the average price for yesterday should be `500$`. But to run the same calculation for today, we should use `480$` instead.

Change Data Capture refers to the technique we used to detect changes in the data source. Slowly Changing Dimension is the way we structure and store data to keep both historical and current data in the data warehouse.

## Data ingestion

After collecting data from the website, we'll load the new data to the data warehouse. Suppose we already have some data in the warehouse, we won't need the same data again. Otherwise, the statistics won't be correct. Here is what we need to implement:

- Add new data to the warehouse
- For data that has been changed on the website (for example, the price drops), we'll mark them as expired and add the new version to the warehouse.
- If the offer is no longer available on the website, we mark it as "expired" in the warehouse.

To determine whether a property is "new", we can use the technique described [here](https://www.sspaeti.com/blog/data-engineering-project-in-twenty-minutes). We'll add a new field called `fingerprint` that will be used to differentiate properties. We already have the "prop_id" field, which is a unique identifier, in the data source. Since we also want to track the price, we will add that information to the `fingerprint`. As a result, the fingerprint is created by joining `prop_id` and `price`. We can have many rows for the same property in the database, as long as the price is different.

We create a table called `housing_staging` for pre-aggregation data and `housing_model` for aggregated data. In the staging table, we use `valid_from` and `expired` fields to track the offer. We will see how these fields are used in the BackFill and Recompute Data part.

Now suppose you loaded the data collected to a table `tmp_housing`. Thanks to the field `fingerprint` , we can identify offers that have been changed or removed from the website.

```sql
SELECT h.id
FROM housing_staging h
LEFT JOIN tmp_housing t
ON h.prop_id = t.prop_id
AND h.expired IS NULL
WHERE t.prop_id IS NULL
OR h.fingerprint != t.fingerprint
```

We update those lines in the `housing_staging` table by setting the `expired` value to the previous day (recall that we're using day-granularity).

Symmetrically, we can use the query below to find the new-or-updated offers:

```sql
SELECT t.id
FROM tmp_housing t
LEFT JOIN housing_staging h
ON h.prop_id = t.prop_id
AND h.expired IS NULL
WHERE h.prop_id IS NULL
OR h.fingerprint != t.fingerprint
```

We add new-or-updated data in the warehouse. The `valid_from` field is set to the beginning of the date for the same reason as the `expired` field above.

## Data Modeling

We can compute the 3 KPIs mentioned in the Introduction section from the `housing_staging` table. The idea is to filter out expired data.

## Backfill and Recompute Data

Sometimes, we need to backfill and recompute data for a day in the past. For instance, when you discover corrupted data in the warehouse and decide to reload the staging data and recalculate the KPI. Another example is that our pipeline failed to load data to the warehouse due to an error.

The tricky part is when we reload data for a day, the data of later dates will be affected. To illustrate that, consider this scenario:

We have the following rows in the `housing_staging` table:

| prop_id | valid_from          | expired |
|---------|---------------------|---------|
| 4       | 2023-02-18 00:00:00 | NULL    |
| 6       | 2023-02-18 00:00:00 | NULL    |
| 8       | 2023-02-18 00:00:00 | NULL    |
| 9       | 2023-02-18 00:00:00 | NULL    |
| 10      | 2023-02-18 00:00:00 | NULL    |

Now if we want to load data in the file 02_01_2023.csv, we should have this result:

| prop_id | valid_from          | expired             |
|---------|---------------------|---------------------|
|       1 | 2023-01-02 00:00:00 | 2023-02-17 23:59:59 |
|       4 | 2023-01-02 00:00:00 | 2023-02-17 23:59:59 |
|       4 | 2023-02-18 00:00:00 |                     |
|       5 | 2023-01-02 00:00:00 | 2023-02-17 23:59:59 |
|       6 | 2023-01-02 00:00:00 |                     |
|       7 | 2023-01-02 00:00:00 | 2023-02-17 23:59:59 |
|       8 | 2023-01-02 00:00:00 | 2023-02-17 23:59:59 |
|       8 | 2023-02-18 00:00:00 |                     |
|       9 | 2023-02-18 00:00:00 |                     |
|      10 | 2023-02-18 00:00:00 |                     |

The following modifications are made:

- Property with id 1,5 and 7 are added. It is valid from 02 January 2023 to the end of 17 February 2023. Because it was in `02_01_2023.csv` but not `today.csv`
- A new line for properties 4 and 8 is added. Because the price of this property changes between `02_01_2023.csv`and `today.csv`
- For property 6, the value of `valid_from` is modified from `2023--02--18 00:00:00` to `2023--01--02 00:00:00` . Because this property appears in 2 files and its price is unchanged, we should take the more ancient timestamp.
- Property 9 and 10 data remain unchanged.

Given this complexity, we have 2 options:

- We remove data from the date we want to reload. Then reload data from that date. This is easier to do but can take longer time to finish if you have a lot of data.
- We load only data for the date and update data for later days.

In this lab, we take the first option. To load data in `02_01_2023.csv`, we first need to remove data from that date. Then rerun the load function for `02_01_2023.csv` and `today.csv`.

In the previous section, we only run the ingestion and transformation steps for the current date. We need to modify those functions by including a new parameter `for_date`. Then, we set the value of `valid_from` and `expired` field according to `for_date`.

For the transformation step, we will need to adjust the condition. In the previous version, we take the rows where the `expired` field is `NULL` because we were running for the current day.

If we recompute data in the `housing_model` table for day D given the following days' data has been loaded in the `housing_staging` table, we will only take rows that are valid until day D and are expired from the end of day D or are still active.

And that's it, you have the data ingestion and transformation necessary to analyze housing price data over time.

## Conclusion

In this lab, we applied change data capture and slowly changing dimension type 2 modelization to build a model for housing price analysis.
