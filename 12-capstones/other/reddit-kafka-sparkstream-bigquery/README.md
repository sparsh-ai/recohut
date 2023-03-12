# reddit-data-engineering of r/FedEx

- Create Kafka cluster using docker-compose hosted on GCP VM
- Used PRAW API to stream both comments and posts data from r/FedEx into Kafka
- Consumes streaming data from Kafka using Spark Streaming
- Saves data into Google Cloud Storage Bucket (Data Lake) -> Batch load data into BigQuery (Data Warehouse) using Cloud Functions
- Visualization of Data in Google Data Studio

### Purpose + Goal:

Learn technologies like (Kafka, Spark Streaming, Cloud Functions, Data Studio), NOT producing the best/optimal architecture

### Pipeline Diagram

![pipeline_diagram](https://user-images.githubusercontent.com/62965911/224531394-c37e0fcf-11fc-42e0-987b-0f3428f2cffb.png)

Currently, Spark Stream writes a new file every 4 hours -> which triggers the Cloud Function to load to BigQuery 

#### Confluent Kafka UI:

![kafka_topics](https://user-images.githubusercontent.com/62965911/224531392-5a93ce58-6483-4ab8-af9d-c534a5a17a7d.png)

#### Sample Data:

![submissions_data](https://user-images.githubusercontent.com/62965911/224531397-650fc6ec-c25f-4626-a630-126409258680.png)

![comments_data](https://user-images.githubusercontent.com/62965911/224531380-8288bfec-7679-4d6c-9de6-d9c0c4432df7.png)

#### Dashboard UI:

![dashboard_1](https://user-images.githubusercontent.com/62965911/224531387-5e334e2d-f4ad-4bce-a8ab-30be1367ce37.png)

![dashboard_2](https://user-images.githubusercontent.com/62965911/224531391-d49da467-f6b2-491e-96d5-abec387c1418.png)


#### Dashboard Link: https://datastudio.google.com/reporting/afbed74b-8f18-4012-bc91-ddbc66e4574c

### Tools/Framework Used:

- Terraform: To create and standardize GCP resources (ex: storage bucket, VM, dataproc cluster, etc.)
- Docker: Used docker compose to create Kafka cluster hosted on GCP VM
- Python + PRAW: Extract data from reddit
- Kafka: Message broker to handle stream data
- Spark Streaming: Consumer of Streaming data from Kafka
- Google Cloud Storage Bucket: Data Lake to store files produced by Spark Streaming
- Google Cloud Function: To batch load data from GCS to BigQuery because streaming insets are expensive!
- Google BigQuery: Data Warehouse to store data so that it can be queried
- Google Data Studio: Visualization Tool to create dashboard

### Procedure/General Setup

1. Create resources with Terraform
2. Kafka
    - Reserve Static External IP address for Kafka VM
    - Install Dependencies in Kafka VM (Docker, PRAW python library)
    - Set "KAFKA_ADDRESS" env variable to exeternal IP of Kafka VM
    - Utilize "screen" command to run docker compose command to start Kafka cluster
    - Utilize "screen" command to run both python producer programs
3. Spark Streaming
    - Use SparkStreaming.py file to submit PySpark job to cluster
4. Cloud Functions
    - Use "Create/Finializing" Trigger event in GCS bucket to execute Cloud Function to upload new Parquet file to BigQuery
5. Data Studio
    - Connect to BigQuery

## Wordcloud 

![fedex-reddit-wordcloud](https://user-images.githubusercontent.com/62965911/224531408-98822cba-f206-493c-9741-58adfa070842.png)

![submission-wordcloud](https://user-images.githubusercontent.com/62965911/224531413-9c26a318-f8cd-4b79-bfe6-d66f0c979a5d.png)
