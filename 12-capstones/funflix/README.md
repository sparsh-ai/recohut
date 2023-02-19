# Funflix

You are working as a data engineer in an Australian media company Funflix. You got the following requirements and tasks to solve.

1. Design the data warehouse for Funflix
2. Build and deploy the data pipeline for Funflix's multi-region business
3. Build a data lake

## Data Warehousing 1

Funflix recently acquired a medical company named Gluewell clinic which provided various medical therapies. The data engineering integration process is going on and you are part of the integration team.

Your analyst team is busy in some other part and needs your help in getting some insights, as it requires some bit of data modeling work, from Gluewell datasets. You have to perform the following steps:

1. In Postgres database, create a schema named `funflix_datamodel`.
2. Upload the 4 raw files in this schema. Table names will be same as file names.
3. Create a star schema (Entity-Relation Diagram). Use [https://dbdiagram.io/](https://dbdiagram.io/) to create it. Once created, export the diagram as png and save it in your system.
4. Write SQL queries to answer the following questions. For each of these queries, create a view in the same schema.| Query                                                                             | View name            |
   | --------------------------------------------------------------------------------- | -------------------- |
   | How many customers visited the clinic in february 2022?                           | customer_feb22       |
   | What was the most booked service in march 2022?                                   | service_mar22        |
   | Who were the top-5 customers who visited the most in Q1 2022 (i.e. Jan-Mar 2022)? | customer_top5_q122   |
   | What are the top-3 most booked services by the most visited customer?             | service_top3         |
   | Which therapist is most experienced in physiotherapy?                             | therapist_experience |
5. Generate a Markdown report of your work and submit it in your branch named `<your git username>/assignment-funflix`. You need to put the report in `/assignments/funflix/modeling/your git username` folder. Make sure to include schema diagram, explanations of your work and other key details in the report.
6. Create PR and notify the instructor for review.

## Data Warehousing 2

Customers comes to Funflix’s platform and subscribe to become a subscribed user. Funflix content experts then hand picks a collection of movies as per user’s taste and sends these recommendations to the user via email. Things are going well so far but Funflix’s executive team do not see potential growth into future with the existing IT arrangements and asked you to innovate their company’s IT processes to enable Funflix’s future growth.

Ele is Funflix’s IT expert and she knows all about the current systems and she is also your POC (point-of-contact) in this project. Here are the key points of the 1st meeting between you and Ele:

```
You: I would like to know about the state of data. How it looks, where it is, Who does what?

Ele: We have a user data in which we store our subscribers’ details, a movie data to store movie details and we also collect our user’s feedback on movies. All the data is in 3 files that we maintain in MS-Excel on our local server.

You: How can I get access this data?

Ele: I can email you these 3 files or share them via pen-drive? The file size is not much.

You: Okay, you can email them then.
```

You got the data via email (email is archived for you in the git repo) and now it’s time to start the innovative work. You will perform the following steps:

1. Create a schema named `funflix_warehouse`.
2. Now, as you got 3 files in mail — for each file, do the following:
   1. Load into a dataframe (pandas or Pyspark dataframe e.g.)
   2. Add column names. You can find the list of columns here:
      - cols
        - ['userid','age','gender','occupation',"zipcode"]
        - ["movieid", "movie_title", "release_date", "video_release_date", "imdb_url", "unknown", "action", "adventure", "animation", "children", "comedy", "crime", "documentary", "drama", "fantasy", "film_noir", "horror", "musical", "mystery", "romance", "scifi", "thriller", "war", "western"]
        - ['userid','itemid','rating','timestamp']
   3. Push the dataframe to database with correct schema.
3. Go to RedShift query editor in AWS and verify if data has been updated corrrectly. e.g. In case of John Doe, it would look like this:
   ![data-ingestion-redshift-example-1](https://user-images.githubusercontent.com/62965911/215305042-35cd1b73-d793-42fe-a97e-44182ddf88ca.png)
4. Analyze the DDLs in Redshift and use this analysis to create a schema diagram (Entity-Relation Diagram). Use [https://dbdiagram.io/](https://dbdiagram.io/) to create it.
5. Generate a Markdown report of your work and submit it in your branch named `<your git username>/assignment-funflix`. You need to put the report in `/assignments/funflix/warehousing/your git username` folder. Make sure to include schema diagram, explanations of your work and other key details in the report.
6. Create PR and notify the instructor for review.

## Data Pipelining

> An online retailer has a website where you can purchase widgets in a variety of colours. The website is backed by a relational database. Every transaction is stored in the database. How many blue widgets did the retailer sell in the last quarter?

To answer this question, you could run a SQL query on the database. This doesn't rise to the level of needing a data engineer. But as the site grows, running queries on the production database is no longer practical. Furthermore, there may be more than one database that records transactions. There may be a database at different geographical locations – for example, the retailers in North America may have a different database than the retailers in Asia, Africa, and Europe.

Now you have entered the realm of data engineering. To answer the preceding question, a data engineer would create connections to all of the transactional databases for each region, extract the data, and load it into a data warehouse. From there, you could now count the number of all the blue widgets sold.

Rather than finding the number of blue widgets sold, companies would prefer to find the answer to the following questions:

- How do we find out which locations sell the most widgets?
- How do we find out the peak times for selling widgets?
- How many users put widgets in their carts and remove them later?
- How do we find out the combinations of widgets that are sold together?

Answering these questions requires more than just extracting the data and loading it into a single system. There is a transformation required in between the extract and load. There is also the difference in times zones in different regions. For instance, the United States alone has four time zones. Because of this, you would need to transform time fields to a standard. You will also need a way to distinguish sales in each region. This could be accomplished by adding a location field to the data. Should this field be spatial – in coordinates or as well-known text – or will it just be text that could be transformed in a data engineering pipeline?

Here, the data engineer would need to extract the data from each database, then transform the data by adding an additional field for the location. To compare the time zones, the data engineer would need to be familiar with data standards. For the time, the International Organization for Standardization (ISO) has a standard – ISO 8601.

Let's now answer the questions in the preceding list one by one:

- Extract the data from each database.
- Add a field to tag the location for each transaction in the data.
- Transform the date from local time to ISO 8601.
- Load the data into the data warehouse.

The combination of extracting, loading, and transforming data is accomplished by the creation of a data pipeline. The data comes into the pipeline raw, or dirty in the sense that there may be missing data or typos in the data, which is then cleaned as it flows through the pipe. After that, it comes out the other side into a data warehouse, where it can be queried. The following diagram shows the pipeline required to accomplish the task:

![data-pipe-example-1](https://user-images.githubusercontent.com/62965911/215305336-d033411c-ddf3-4ecd-a04f-fb1fc7f5ede1.png)

Funflix runs its business globally in two regions - American and European. Mitch is the Sales Head of American region and Shiva is Sales Head of European region. Funflix needs your help in doing something similar to the above use case (the reading material) to collect their data from these regions and load them in their Warehouse. They also expecting to get some answers related to their overall sales that Mitch and Shiva can not answer at the moment because they don’t have the global data. (💡 Data is in Silos!).

Mitch shared the american region data.

Shiva on the other hand wants you to pull the data directly from the database. The credentials are in the AWS Secret Manager.

You got the data related information and now it’s time to start the work. You will perform the following steps:

1. Pull the data for both regions and store in your system.
2. Create a schema in the database. Schema name should be like `funflix_pipeline`.
3. It’s time to follow the instructions that you read during the case study and apply them here. To summarize those again, this is what you need to do:

   1. Read the data from raw layer for both regions in separate tables.
   2. Add a field to tag the location for each transaction in the data.
   3. Transform the date from local time to ISO 8601.
   4. Merge the data into a single table named `sales`.
   5. Load the data into the data warehouse.

   The combination of extracting, loading, and transforming data is accomplished by the creation of a data pipeline. The data comes into the pipeline raw, or dirty in the sense that there may be missing data or typos in the data, which is then cleaned as it flows through the pipe. After that, it comes out the other side into a data warehouse, where it can be queried.
4. Go to DBeaver, setup the warehouse connection and verify if data has been updated corrrectly.
5. Generate a Markdown report of your work and submit it in your branch named `<your git username>/assignment-funflix`. You need to put the report in `/assignments/funflix/pipeline/your git username` folder. Make sure to include explanations of your work and other key details in the report.
6. Create PR and notify the instructor for review.

## Data Lake

Your goal is to build a data lake pipeline with Python and AWS. Follow this architecture:

![process_flow drawio](https://user-images.githubusercontent.com/62965911/215305348-4381282a-5770-4dbf-9d0d-36c719fadb38.svg)
