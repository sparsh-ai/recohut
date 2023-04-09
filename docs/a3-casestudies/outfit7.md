# Outfit7

> Multinational video game developer

## The Billion Events Infrastructure

With 430 million monthly active users, it can be a challenge to get a clear picture of how our games and company are performing. The data we gather helps us understand how we perform in the fast-paced mobile gaming market. Getting fast feedback is key. Because of this, we need infrastructure that is scalable and reliable, and which, ideally, doesn’t hurt the company’s wallet too much. Over the past decade we’ve continuously improved our infrastructure to accommodate our growing user base. Today, we handle half a million row inserts per second — let me show you how. Welcome to the Billion Events Infrastructure.

![](https://miro.medium.com/max/4800/0*Zek8d75_0P4uhYkI)

Let’s start with an overview of our infrastructure. We receive data from various data sources, like game usage data, third party services, etc., which we save in persistent storage. Here, we’ll focus only on data sent by our games, because this is what forms the backbone of our analyses. From data gathering endpoints to persistent storage, all is hosted on the Google Cloud Platform. Let’s start with the first layer, at our API endpoints:

### API endpoints

We run our data-gathering endpoints on different managed services (App Engine, Cloud Run and Kubernetes Engine). Our main endpoint, where we gather usage data, runs on Kubernetes Engine. We chose Kubernetes because it offers a nice balance between performance and cost. Because we have a global player base, we run three clusters, each in different regions (US, EU and Asia). Our main cluster resides in the US, where we get the most traffic, while the Asia cluster serves as the endpoint for our users in China. We also set up one cluster in Europe which is our backfall endpoint in the event of endpoint failures in US and Asia clusters. All data is validated and pushed to our data delivery layer.

### Data delivery

This second layer is a middleware between our API endpoints and data processing workloads. It provides asynchronous delivery of messages with the benefit of keeping our data safe until it’s written to persistent storage. We use Pub/Sub (similar to Apache Kafka) which provides a simple, reliable and scalable message delivery service.

### Data processing

In this layer, we do some light data transformation (unbatching the client data) and streaming data into persistent storage. Our main framework to do this is Apache Beam which runs on managed cloud infrastructure called Dataflow. This is a tried and tested way to do ETL pipelines because it provides a reliable way of inserting data into persistent storage.

### Data storage

After all this, the data is finally written into BigQuery. It’s our main data warehouse, which powers all of our analytics workload. It’s fast, reliable and just what we need to store and analyze our data.

All these layers combined create a scalable and reliable infrastructure that can receive, process and ingest more than half a million rows of data per second, or five terabytes of new data per day. Our data teams query 60 petabytes per year with zero downtime and zero maintenance from the core engineering team, just by using BigQuery. By using a simple approach and managed services a single person can maintain this infrastructure. This enables us to focus on developing new solutions that add value to our company.

Read more [here](https://medium.com/outfit7/the-billion-events-infrastructure-c5fa1610d786).

## Resolving Big Data Challenges: Why We Use BigQuery at Outfit7

In just a few years, Outfit7’s portfolio has grown to include 19 games with over 8 billion downloads. But big numbers bring big challenges. One of them is how to deal with such huge amounts of data in a timely and cost-effective manner. Our games hit the backend infrastructure with around 8 billion rows of data per day that take up 2.5 TB of space – and those numbers grow daily. This data is in a raw form and, to be useful, it needs to be processed, aggregated, extracted, and transformed. Above all, it has to be treated securely.

If we were to use normal relational database solutions, building a system that would be able to ingest and operationally function with such amount of data – not to mention handling the explosion of hardware storage space and related costs – would be a daunting task. It would require an army of sysops/devops/DB engineers.

So, to find a way around this, we decided to look at cloud platforms. Google’s solution, the Google Cloud Platform (“GCP”) is steadily becoming one of the best. Outfit7 Group heavily leverages one of the GCP’s flagship services, BigQuery; a serverless, highly scalable, low cost enterprise data warehouse. The service has no problems ingesting the data Outfit7 deals with. In fact, the querying power is just astonishing.

BigQuery Across Different Departments
We use BigQuery in numerous ways across the company. Our backend department  has a special data team that – complying with all laws including GDPR – takes care of data ingestion, transformation, and delivery to appropriate stakeholders. To give you an example, we generate around 50 aggregates that form the basis for further analysis in the Analytics and Controlling departments. The main aggregates we prepare for the Analytics team are the retention and user segments, while the Controlling team is more focused on the daily and monthly revenue aggregates, user live time values, and daily active users aggregates.

We also closely collaborate with the Ad Ops and App Sales teams. In this part of the company, daily ad sales, ad mediation and paid user acquisition reports and aggregates need to be calculated. The data is then consumed and evaluated with the preferred tool of choice for each department. The Analytics department relies heavily on iPython and R, Controlling is mainly focused on Tableau reports and the visual representation of data, and the Ad Ops and Ad Sales departments rely on custom made dashboards, Google DataStudio reports, and ad-hoc analysis with Excel/Sheets.

### BigQuery’s Capabilities

To illustrate the point further, consider the following query. Anyone can run it on the publicly available BQ datasets that come bundled out of the box with a free GCP account.

![Query example on BQ](https://cdn-o7.outfit7.com/wp-content/uploads/2018/06/Screen_Shot_2018-06-27_at_12.31.40.png)

The underlying “trips” table contains 130GB and more than 1.1 billion rows of data that represent yellow taxi fares in New York City from 2009 to 2015. The query included a yearly breakdown of vendors operating in the NYC area, their revenue, average fare cost, the distance traveled, and the total number of fares. It took 4.5 seconds to produce 16 rows of a high level report, which could then be downloaded as a csv or JSON file, saved to a new table, or a Google Sheets document, etc.

![High level aggregation report from a table containing more than 1.1 billion rows of data, which took 4.5 seconds to produce](https://cdn-o7.outfit7.com/wp-content/uploads/2018/06/bigQuery_example.png)

Imagine that: it took BigQuery less time to scan 130GB of data and spit out a condensed report than it would take you to say “Where’s the star schema and other data warehousing buzzword shenanigans?” If that isn’t impressive for a data guy, I don’t know what is. All the upsides aside, however, there’s no such thing as free lunch. If that wasn’t a test, the above query would cost $0.15, excluding the cost of storage, which would bring the amount up to $2.60 per month, decreasing to $1.30 per month after three months.

But the days of a data backend engineer aren’t just filled with writing and running BigQuery jobs in one of the various language flavours we’re using, like Bash, Python, Java, etc. They’re also filled with other engineering tasks that are necessary to hold the whole infrastructure together. Nevertheless, if, at the end of the day, we had to choose and point to one of the tools in the GCP arsenal that currently saves the Data and Backend teams the most amount of time, we’d probably say it’s BigQuery. In a competitive industry such as gaming, you need to have a reliable support system that continues to pave the way forward and, for us, that’s BigQuery.