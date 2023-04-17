# Lab: GCP Dataprep

> Creating a Data Transformation Pipeline with Cloud Dataprep

![](https://user-images.githubusercontent.com/62965911/214003279-5d213b3a-935f-4f7a-b652-372bd7a967a2.png)

Cloud Dataprep by Alteryx is an intelligent data service for visually exploring, cleaning, and preparing structured and unstructured data for analysis. In this lab you explore the Cloud Dataprep UI to build a data transformation pipeline that outputs results into BigQuery.

The dataset you'll use is an [ecommerce dataset](https://www.en.advertisercommunity.com/t5/Articles/Introducing-the-Google-Analytics-Sample-Dataset-for-BigQuery/ba-p/1676331#) that has millions of Google Analytics session records for the Google Merchandise Store loaded into BigQuery. You have a copy of that dataset for this lab and will explore the available fields and row for insights.

In this lab, you will learn how to perform these tasks:

- Connect BigQuery datasets to Cloud Dataprep
- Explore dataset quality with Cloud Dataprep
- Create a data transformation pipeline with Cloud Dataprep
- Run transformation jobs outputs to BigQuery

### Step 1: Enable DataPrep

Search for DataPrep in GCP console search box and go to the DataPrep product page. Access and enable the product.

### Step 2: Creating a BigQuery dataset

You need BigQuery as an endpoint for dataset ingestion to the pipeline and as a destination for the output when the pipeline is completed.

1. Search for BigQuery in GCP console search box and Go to BigQuery
2. In the left pane, under Explorer section, click on the View actions icon to the right of your project ID, then click Create dataset.
3. For Dataset ID, type `ecommerce`.
4. Leave the other values at their defaults.
5. Click CREATE DATASET. You will now see your dataset under your project in the left pane.
6. Copy and paste the following SQL query into the Query Editor:
    ```sql
    #standardSQL
    CREATE OR REPLACE TABLE ecommerce.all_sessions_raw_dataprep
    OPTIONS(
    description="Raw data from analyst team to ingest into Cloud Dataprep"
    ) AS
    SELECT * FROM `data-to-insights.ecommerce.all_sessions_raw`
    WHERE date = '20170801'; # limiting to one day of data 56k rows for this lab
    ```
7.  Click RUN. This query copies over a subset of the public raw ecommerce dataset (one day's worth of session data, or about 56 thousand records) into a new table named `all_sessions_raw_dataprep`, which has been added to your ecommerce dataset for you to explore and clean in Cloud Dataprep.
8.  Confirm that the new table exists in your `ecommerce` dataset

### Step 3: Connecting BigQuery data to Cloud Dataprep

In this step, you will connect Cloud Dataprep to your BigQuery data source. On the Cloud Dataprep page:

1. Click Create a new flow in the left corner.
2. Rename the Untitled Flow and specify these details:
    1. For Flow Name, type `Ecommerce Analytics Pipeline`
    2. For Flow Description, type `Revenue reporting table`
3. Click Ok.
4. If prompted with a `What's a flow?` popup, select Don't show me any helpers.
5. Click the Add Icon in the Dataset box.
6. In the Add Datasets to Flow dialog box, select Import Datasets.
7. In the left pane, click BigQuery.
8. When your ecommerce dataset is loaded, click on it.
9. Click on the Create dataset icon (+ sign) on the left of the `all_sessions_raw_dataprep` table.
10. Click Import & Add to Flow in the bottom right corner.

The data source automatically updates. You are ready to go to the next step.

### Step 4: Exploring ecommerce data fields with the UI

In this step, you will load and explore a sample of the dataset within Cloud Dataprep.

1. Click the Recipe icon and then select Edit Recipe.
2. Cloud Dataprep loads a sample of your dataset into the Transformer view. This process might take a few seconds. You are now ready to start exploring the data!

Answer the following questions:

1. How many columns are there in the dataset?
    1. Answer: 32 columns.
2. How many rows does the sample contain?
    1. Answer: About 12 thousand rows.
3. What is the most common value in the `channelGrouping` column?
    1. Hint: Find out by hovering your mouse cursor over the histogram under the `channelGrouping` column title.
    2. Answer: Referral.
    3. Note: A [referring site](https://support.google.com/analytics/answer/1011811?hl=en) is typically any other website that has a link to your content. An example here is a different website reviewed a product on our ecommerce website and linked to it. This is considered a different acquisition channel than if the visitor came from a search engine.
4. What are the top three countries from which sessions are originated?
    1. Answer: United States, India, United Kingdom
5. What does the grey bar under totalTransactionRevenue represent?
    1. Answer: Missing values for the `totalTransactionRevenue` field.
    2. This means that a lot of sessions in this sample did not generate revenue. Later, we will filter out these values so our final table only has customer transactions and associated revenue.
6. What is the maximum `timeOnSite` in seconds, maximum `pageviews`, and maximum `sessionQualityDim` for the data sample?
    1. Hint: Open the menu to the right of the `timeOnSite` column by clicking the Column Details menu
    2. To close the details window, click the Close Column Details (X) button in the top right corner. Then repeat the process to view details for the `pageviews` and `sessionQualityDim` columns.
    3. Answers:
        1. Maximum Time On Site: 5,561 seconds (or 92 minutes)
        2. Maximum Pageviews: 155 pages
        3. Maximum Session Quality Dimension: 97
    4. Note: Your answers for maximums may vary slightly due to the data sample used by Cloud Dataprep.
    5. Note on averages: Use extra caution when performing aggregations like averages over a column of data. We need to first ensure fields like `timeOnSite` are only counted once per session. We'll explore the uniqueness of visitor and session data in a later lab.
7. Looking at the histogram for `sessionQualityDim`, are the data values evenly distributed?
    1. Answer: No, they are skewed to lower values (low quality sessions), which is expected.
8. What is the date range for the dataset? Hint: Look at date field
    1. Answer: 8/1/2017 (one day of data)
9. You might see a red bar under the `productSKU` column. If so, what might that mean?
    1. Answer: A red bar indicates mismatched values.
    2. While sampling data, Cloud Dataprep attempts to automatically identify the type of each column. If you do not see a red bar for the `productSKU` column, then this means that Cloud Dataprep correctly identified the type for the column (i.e. the String type). If you do see a red bar, then this means that Cloud Dataprep found enough number values in its sampling to determine (incorrectly) that the type should be Integer. Cloud Dataprep also detected some non-integer values and therefore flagged those values as mismatched. In fact, the `productSKU` is not always an integer (for example, a correct value might be "GGOEGOCD078399"). So in this case, Cloud Dataprep incorrectly identified the column type: it should be a string, not an integer. You will fix that later in this lab.
10. Looking at the `v2ProductName` column, what are the most popular products?
    1.  Answer: Nest products
11. Looking at the `v2ProductCategory` column, what are some of the most popular product categories?
    1.  Answers: The most popular product categories are: Nest, Bags, (not set) (which means that some sessions are not associated with a category)
12. True or False? The most common `productVariant` is `COLOR`.
    1.  Answer: False. It's (not set) because most products do not have variants (80%+)
13. What are the two values in the type column?
    1.  Answer: `PAGE` and `EVENT`
    2.  A user can have many different interaction types when browsing your website. Types include recording session data when viewing a PAGE or a special EVENT (like "clicking on a product") and other types. Multiple hit types can be triggered at the exact same time so you will often filter on type to avoid double counting. We'll explore this more in a later analytics lab.
14. What is the maximum `productQuantity`?
    1.  Answer: 100 (your answer may vary)
    2.  `productQuantity` indicates how many units of that product were added to cart. 100 means 100 units of a single product was added.
15. What is the dominant `currencyCode` for transactions?
    1.  Answer: USD (United States Dollar)
16. Are there valid values for `itemQuantity` or `itemRevenue`?
    1.  Answer: No, they are all `NULL` (or missing) values.
    2.  Note: After exploration, in some datasets you may find duplicative or deprecated columns. We will be using `productQuantity` and `productRevenue` fields instead and dropping the `itemQuantity` and `itemRevenue` fields later in this lab to prevent confusion for our report users.
17. What percentage of `transactionId` values are valid? What does this represent for our `ecommerce` dataset?
    1.  Answer: About 4.6% of transaction IDs have a valid value, which represents the average conversion rate of the website (4.6% of visitors transact).
18. How many `eCommerceAction_type` values are there, and what is the most common value?
    1.  Hint: Count the distinct number of histogram columns.
    2.  Answers: There are seven values found in our sample. The most common value is zero `0` which indicates that the type is unknown. This makes sense as the majority of the web sessions on our website will not perform any ecommerce actions as they are just browsing.
19. Using the [schema](https://support.google.com/analytics/answer/3437719?hl=en), what does `eCommerceAction_type = 6` represent?
    1.  Hint: Search for `eCommerceAction` type and read the description for the mapping
    2.  Answer: 6 maps to "Completed purchase". Later in this lab we will ingest this mapping as part of our data pipeline.

### Step 5: Cleaning the data

In this task, you will clean the data by deleting unused columns, eliminating duplicates, creating calculated fields, and filtering out unwanted rows.

**Converting the productSKU column data type**

1. To ensure that the productSKU column type is a string data type, open the menu to the right of the productSKU column by clicking, then click Change type > String.
1. Verify that the first step in your data transformation pipeline was created by clicking on the Recipe icon:

**Deleting unused columns**

As we mentioned earlier, we will be deleting the itemQuantity and itemRevenue columns as they only contain NULL values and are not useful for the purpose of this lab.

1. Open the menu for the itemQuantity column, and then click Delete.
1. Repeat the process to delete the itemRevenue column.

**Deduplicating rows**

Your team has informed you there may be duplicate session values included in the source dataset. Let's remove these with a new deduplicate step.

1. Click the Filter rows icon in the toolbar, then click Remove duplicate rows.
1. Click Add in the right-hand panel.

**Filtering out sessions without revenue**

Your team has asked you to create a table of all user sessions that bought at least one item from the website. Filter out user sessions with NULL revenue.

1. Under the totalTransactionRevenue column, click the grey Missing values bar. All rows with a missing value for totalTransactionRevenue are now highlighted in red.
2. In the Suggestions panel, in Delete rows, click Add.

This step filters your dataset to only include transactions with revenue (where totalTransactionRevenue is not NULL).

**Filtering sessions for PAGE views**

The dataset contains sessions of different types, for example PAGE (for page views) or EVENT (for triggered events like "viewed product categories" or "added to cart"). To avoid double counting session pageviews, add a filter to only include page view related hits.

1. In the histogram below the type column, click the bar for PAGE. All rows with the type PAGE are now highlighted in green.
2. In the Suggestions panel, in Keep rows, and click Add.

### Step 6: Enriching the data

Search your [schema documentation](https://support.google.com/analytics/answer/3437719?hl=en/) for visitId and read the description to determine if it is unique across all user sessions or just the user.

-  `visitId`: an identifier for this session. This is part of the value usually stored as the `utmb` cookie. This is only unique to the user. For a completely unique ID, you should use a combination of fullVisitorId and visitId.

As we see, `visitId` is not unique across all users. We will need to create a unique identifier.

**Creating a new column for a unique session ID**

As you discovered, the dataset has no single column for a unique visitor session. Create a unique ID for each session by concatenating the fullVisitorID and visitId fields.

1. Click on the Merge columns icon in the toolbar.
1. For Columns, select `fullVisitorId` and `visitId`.
2. For Separator type a single hyphen character: `-`.
3. For the New column name, type `unique_session_id`.
1. Click Add.

The `unique_session_id` is now a combination of the `fullVisitorId` and `visitId`. We will explore in a later lab whether each row in this dataset is at the unique session level (one row per user session) or something even more granular.

**Creating a case statement for the ecommerce action type**

As you saw earlier, values in the `eCommerceAction_type` column are integers that map to actual ecommerce actions performed in that session. For example, 3 = "Add to Cart" or 5 = "Check out". This mapping will not be immediately apparent to our end users so let's create a calculated field that brings in the value name.

1. Click on Conditions in the toolbar, then click `Case on single column`.
1. For Column to evaluate, specify `eCommerceAction_type`.
2. Next to Cases (1), click Add 8 times for a total of 9 cases.
1. For each Case, specify the following mapping values (including the single quote characters):
    | Comparison | New value                          |
    | ---------- | ---------------------------------- |
    | `0`        | `'Unknown'`                        |
    | `1`        | `'Click through of product lists'` |
    | `2`        | `'Product detail views'`           |
    | `3`        | `'Add product(s) to cart'`         |
    | `4`        | `'Remove product(s) from cart'`    |
    | `5`        | `'Check out'`                      |
    | `6`        | `'Completed purchase'`             |
    | `7`        | `'Refund of purchase'`             |
    | `8`        | `'Checkout options'`               |
1. For New column name, type `eCommerceAction_label`. Leave the other fields at their default values.
2. Click Add.

**Adjusting values in the totalTransactionRevenue column**

As mentioned in the [schema](https://support.google.com/analytics/answer/3437719?hl=en), the totalTransactionRevenue column contains values passed to Analytics multiplied by 10^6 (e.g., 2.40 would be given as 2400000). You now divide the contents of that column by 10^6 to get the original values.

1.  Open the menu to the right of the totalTransactionRevenue column by clicking the dropdown arrow, then select Calculate > Custom formula.
1. For Formula, type: `DIVIDE(totalTransactionRevenue,1000000)` and for New column name, type: `totalTransactionRevenue1`. Notice the preview for the transformation.
1. Click Add.
2. Note: You might see a red bar under the `totalTransactionRevenue1` column. Open the menu to the right of the `totalTransactionRevenue1` column, then click Change type > Decimal.
3. Review the full list of steps in your recipe.
1. You can now click Run.

![](https://user-images.githubusercontent.com/62965911/214003293-f447729f-e008-4742-a04e-58aa0281189a.png)

### Step 7: Running Cloud Dataprep jobs to BigQuery

1. In the Run Job page, select Dataflow for your Running Environment.
2. Under Publishing Actions, click on Edit on the right of Create-CSV.
3. In the following page, select BigQuery from the left hand menu.
4. Select your ecommerce dataset.
5. Click Create a New Table from the panel on the right.
6. Name your table revenue_reporting.
7. Select Drop the Table every run.
8. Click on Update.
9. Click RUN.

Once your Cloud Dataprep job is completed, refresh your BigQuery page and confirm that the output table revenue_reporting exists.

![](https://user-images.githubusercontent.com/62965911/214003287-a54770f5-76bc-4953-b1c9-9564fee171a6.png)

![](https://user-images.githubusercontent.com/62965911/214003160-35926333-1eb8-4493-b6c1-9ea64c46e20a.png)

Note: If your job fails, try waiting a minute, pressing the back button on your browser, and running the job again with the same settings.

Congratulations!

You've successfully explored your ecommerce dataset and created a data transformation pipeline with Cloud Dataprep.