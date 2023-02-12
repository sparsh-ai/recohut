# Data Governance

## Data Quality

Testing code is part of the software engineering discipline. In the data engineering world, the equivalent is testing data. While conceptually similar, there is a major difference between the two. Once the code gets written and tested, we can expect the tests to keep passing unless the code is modified. On the other hand, in a data platform, data keeps moving. We might ingest bad data due to an issue upstream, or we might output corrupt data due to a processing issue. Data quality tests need to run all the time, as data moves, to uncover such issues.

### Availability tests

The simplest type of data test is an availability test, which checks that data is available for a certain date. This is a basic test we can run before running more complicated tests. It doesn't tell us whether the data we ingested is correct or even if we ingested all the data we were expecting to ingest. What it does tell us is that we have at least some data available for the date we are querying for, which means some ingestion happened. Knowing this, we can run more comprehensive tests.

### Correctness tests

Ensuring data is available is just the first step. We also need to validate that the data is valid. What *valid* means depends on the dataset. We can make one check to ensure that some value is always present in a column. A *correctness test* ensures that data is valid by checking that values are within allowed ranges. Allowed values are specific to each dataset and require domain knowledge to identify.

### Completeness tests

Availability tests check that some data is present. Completeness tests check that all data is present. Like correctness tests, a completeness test depends on the dataset and what it means to be complete. A *completeness test* ensures that all the data is loaded by checking that the volume of data is what we would expect. If possible, we can check for an exact row count. If not, we can check that volume is above a certain threshold.

### Detecting anomalies

Anomaly detection is a deep topic, so we'll just dip our toes here. An *anomaly detection* test looks for statistical anomalies in the data. This type of test is more flexible than other types and can automatically adjust to changes over time. For example, online shopping spikes during the holiday season, while job searches drop. For this, we can use AI-powered anomaly detection, which automatically learns from historical data and identifies anomalies, taking into account spikes and drops like weekends and holidays.
