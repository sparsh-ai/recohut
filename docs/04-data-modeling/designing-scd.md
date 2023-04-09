# Designing SCDs

Whereas operational source systems contain only the latest version of [master data](https://en.wikipedia.org/wiki/Master_data), the star schema enables time travel queries to reproduce dimension attribute values on past dates when the fact transaction or event actually happened. The star schema data model allows analytical users to query historical data tying metrics to corresponding dimensional attribute values over time. Time travel is possible because dimension tables contain the exact version of the associated attributes at different time ranges. Relative to the metrics data that keeps changing on a daily or even hourly basis, the dimension attributes change less frequently. Therefore, dimensions in a star schema that keeps track of changes over time are referred to as [slowly changing dimensions](https://en.wikipedia.org/wiki/Slowly_changing_dimension) (SCDs).

SCDs refer to data in dimension tables that changes slowly over time and not at a regular cadence. A common example for SCDs is customer profiles—for example, an email address or the phone number of a customer doesn't change that often, and these are perfect candidates for SCD.

Here are some of the main aspects we will need to consider while designing an SCD:

- Should we keep track of the changes? If yes, how much of the history should we maintain?
- Or, should we just overwrite the changes and ignore the history?

Based on our requirements for maintaining the history, there are about seven ways in which we can accomplish keeping track of changes. They are named SCD1, SCD2, SCD3, and so on, up to SCD7.

Among these, SCD1, SCD2, SCD3, SCD4, and SCD6 are the most important ones.

## Designing SCD1

In SCD type 1, the values are overwritten and no history is maintained, so once the data is updated, there is no way to find out what the previous value was. The new queries will always return the most recent value. Here is an example of an SCD1 table:

| Customer ID | Name | City     | Email | ... |
|-------------|------|----------|-------|-----|
| 1           | Adam | New York | Adam  | ... |

| Customer ID | Name | City       | Email | ... |
|-------------|------|------------|-------|-----|
| 1           | Adam | New Jersey | Adam  | ... |

In this example, the value of the City column is changing from New York to New Jersey. The value just gets overwritten.

## Designing SCD2

In SCD2, we maintain a complete history of changes. Every time there is a change, we add a new row with all the details without deleting the previous values. There are multiple ways in which we can accomplish this. Let's take a look at the most common approaches.

**Using a flag**

In this approach, we use a flag to indicate if a particular value is active or if it is current. Here is an example of this:

| SurrogateID | CustomerID | Name | City     | isActive | ... |
|-------------|------------|------|----------|----------|-----|
| 1           | 1          | Adam | New York | True     | ... |

| SurrogateID | CustomerID | Name | City       | isActive | ... |
|-------------|------------|------|------------|----------|-----|
| 1           | 1          | Adam | New York   | False    | ... |
| 2           | 1          | Adam | New Jersey | False    | ... |
| 3           | 1          | Adam | Miami      | True     | ... |

In the second table, every time there is a change, we add a new row and update the isActive column of the previous rows to False. That way, we can easily query the active values by filtering on the isActive=True criteria.

NOTE

> Surrogate keys are secondary row identification keys. They are added in all SCD2 cases because the primary identification key will not be unique anymore with newly added rows.

**Using version numbers**

In this approach, we use version numbers to keep track of changes. The row with the highest version is the most current value. Here is an example of this:

| SurrogateID | CustomerID | Name | City     | Version | ... |
|-------------|------------|------|----------|---------|-----|
| 1           | 1          | Adam | New York | 0       | ... |

| SurrogateID | CustomerID | Name | City       | Version | ... |
|-------------|------------|------|------------|---------|-----|
| 1           | 1          | Adam | New York   | 0       | ... |
| 2           | 1          | Adam | New Jersey | 1       | ... |
| 3           | 1          | Adam | Miami      | 2       | ... |

In the previous example, we need to filter on the MAX(Version) column to get the current values.

**Using date ranges**

In this approach, we use date ranges to show the period a particular record (row) was active, as illustrated in the following example:

| SurrogateID | CustomerID | Name | City     | StartDate   | EndDate | ... |
|-------------|------------|------|----------|-------------|---------|-----|
| 1           | 1          | Adam | New York | 01-Jan-2020 | NULL    | ... |

| SurrogateID | CustomerID | Name | City       | StartDate   | EndDate     | ... |
|-------------|------------|------|------------|-------------|-------------|-----|
| 1           | 1          | Adam | New York   | 01-Jan-2020 | 25-Mar-2020 | ... |
| 2           | 1          | Adam | New Jersey | 25-Mar-2020 | 01-Dec-2020 | ... |
| 3           | 1          | Adam | Miami      | 01-Dec-2020 | NULL        | ... |

In the previous example, every time we change a field, we add a new record to the table. Along with that, we update the EndDate column of the previous record and the StartDate column for the new record with today's date. In order to fetch the current record, we have to filter on the EndDate=NULL criteria, or, instead, we could just fill in a very futuristic date instead of NULL—something such as 31-Dec-2100.

As a variation to the date-range approach, we could also add a flag column to easily identify active or current records. The following example shows this approach:

| SurrogateID | CustomerID | Name | City       | StartDate   | EndDate     | isActive | ... |
|-------------|------------|------|------------|-------------|-------------|----------|-----|
| 1           | 1          | Adam | New York   | 01-Jan-2020 | 25-Mar-2020 | False    | ... |
| 2           | 1          | Adam | New Jersey | 25-Mar-2020 | 01-Dec-2020 | False    | ... |
| 3           | 1          | Adam | Miami      | 01-Dec-2020 | NULL        | True     | ... |

## Designing SCD3

In SCD3, we maintain only a partial history and not a complete history. Instead of adding additional rows, we add an extra column that stores the previous value, so only one version of historic data will be preserved. As with the SCD2 option, here again, we can choose to add date columns to keep track of modified dates, but we don't need surrogate keys in this case as the identification key of the record doesn't change. Here is an example of this:

| CustomerID | Name | City     | PrevCity | ... |
|------------|------|----------|----------|-----|
| 1          | Adam | New York | NULL     | ... |

| CustomerID | Name | City       | PrevCity | ... |
|------------|------|------------|----------|-----|
| 1          | Adam | New Jersey | New York | ... |

In the previous example, we have added a new column called PrevCity. Every time the value of City changes, we add the previous value to PrevCity and update the City column with the current city.

## Designing SCD4

SCD4 was introduced for dimension attributes that change relatively frequently. In type 4, we split the fast-changing attributes of the dimension table into another smaller dimension table and also reference the new dimension table directly from the fact table.

For example, in the following diagram, if we assume that the carpool (also known as High occupancy vehicles) pass needs to be purchased every month, we can move that field to a smaller mini-dimension and reference it directly from the fact table:

![B17525_04_009](https://user-images.githubusercontent.com/62965911/218293241-5d41063b-5dc9-45ac-bcf7-77c9fc41532b.jpeg)

We can split the table into a mini DimCarPool dimension, as in the following diagram:

![B17525_04_010](https://user-images.githubusercontent.com/62965911/218293244-d9892da4-f4cf-4010-8188-f040f0d5d784.jpeg)

This sub-division helps in modifying only a smaller amount of data frequently instead of the complete row.

## Designing SCD5, SCD6, and SCD7

The rest of the SCDs—SCD5, SCD6, and SCD7—are derivatives of the previous four SCDs. Among these derived ones, SCD6 is a relatively important one, so we will be exploring that as part of the next sub-section.

**Designing SCD6**

Type 6 is a combination of 1, 2, and 3. In this type, along with the addition of new rows, we also update the latest value in all the rows, as illustrated below:

| SurrogateID | CustomerID | Name | CurrCity | PrevCity   | StartDate   | EndDate     | isActive | ... |
|-------------|------------|------|----------|------------|-------------|-------------|----------|-----|
| 1           | 1          | Adam | Miami    | NULL       | 01-Jan-2020 | 25-Mar-2020 | False    | ... |
| 2           | 1          | Adam | Miami    | New York   | 25-Mar-2020 | 01-Dec-2020 | False    | ... |
| 3           | 1          | Adam | Miami    | New Jersey | 01-Dec-2020 | NULL        | True     | ... |

In the previous example, you would have noticed that the CurrCity value for all the records belonging to customer Adam has been updated. This is just another benefit of extracting the latest values.

That explains SCD type 6. If you are interested in learning about SCDs 5 and 7, you can find more information at the following links:

SCD5: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-5/

SCD7: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-7