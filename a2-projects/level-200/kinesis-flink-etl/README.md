# Streaming ETL pipeline with Apache Flink and Amazon Kinesis Data Analytics

We will create an Amazon Kinesis Data Analytics for Apache Flink application with Amazon Kinesis Data Streams as a source and a Amazon S3 bucket as a sink. Random data is ingested using Amazon Kinesis Data Generator. The Apache Flink application code performs a word count on the streaming random data using a tumbling window of 5 minutes. The generated word count is then stored in the specified Amazon S3 bucket. Amazon Athena is used to query data generated in the Amazon S3 bucket to validate the end results.

## Create an Amazon Kinesis Data Stream

Open the https://console.aws.amazon.com/kinesis/ and create an amazon Kinesis Data Stream `kinesisDataStream1` with on-demand capacity.

## Set up Amazon Kinesis Data Generator

Go to https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html and follow the instructions to create a new Kinesis Data Generator via CloudFormation. On the CloudFormation outputs tab, You will get a URL. Go there and login with the user id and password that you provided in CloudFormation.

## Send sample data to an Amazon Kinesis Data Stream

In the Kinesis Data Generator, select contant as 1 and use the below template in Template 1:

```
{{random.arrayElement([
    "Hi",
    "Hello there",
    "How are you",
    "Hi how are you"
])}}
```

Click on `Send data`. To verify, go to your KDS Monitoring tab and in the Stream metrics section, find the `Put records successful records - average (Percent)` and `Put records – sum (bytes)` metrics to validate record ingestion.

## Create Amazon S3 buckets

Run the `create-buckets.sh` script.

## Modify the code for Amazon Kinesis Data Analytics application

In [this](./S3Sink/src/main/java/com/amazonaws/services/kinesisanalytics/S3StreamingSinkJob.java) file, you will the find the code that we will use. 

The incoming stream of records from Kinesis Data Stream, converts each record to lowercase and splits the record body at tab or spaces. For each word retrieved after the split, it creates a two dimensional tuple with word string and its count.

For example :
- “Hi” becomes (Hi,1)
- “Hi how are you” becomes (Hi,1) (how,1) (are, 1) (you,1)

Then, it partitions the stream of tuples using the first key (i.e. the word string) and performs a sum on second key (i.e. the count) for each partition under a tumbling window of one minute.

In the previous example, if no new records come up in the stream after 1 minute then the output of sum method would be :

- (Hi,2) (how,1) (are, 1) (you,1)

Then, a map is created using the sum output and send it to S3Sink. This means that if the record ingestion is sustained then a file in the `kda-word-count-tutorial-bucket-<unique-name>` S3 bucket is created every minute with new-line separated character strings of following format:

- Hi count: 824 
- how count: 124 
- are count: 210 
- you count: 100 

We will modify the following variables:

- region
- inputStreamName
- s3SinkPath, type the string `s3a://kda-word-count-tutorial-bucket-<unique>/wordCount` where bucket-palceholder is the name of S3 bucket created in the previous step.

## Compile the application code

In the step, you will compile the application code to create a .jar file of the modified code. This .jar is a required input for Kinesis Data Analytics.

```
cd S3Sink/
mvn package -Dflink.version=1.11.1
```

If Maven is not installed locally (confirm with `mnv -v`), you can use Colab to install and compile with Maven.

```
apt-get install maven
apt-get install openjdk-8-jdk
apt-get install openjfx
update-alternatives --config java
mvn -v
```

The previous command creates a .jar file of the application at target/aws-kinesis-analytics-java-apps-1.0.jar.

## Upload the Apache Flink Streaming Java Code to an Amazon S3 bucket

Upload the jar file to `kda-word-count-ka-app-code-location-<unique-name>` S3 bucket.

## Create, configure, and start the Kinesis Data Analytics application

In that same Kinesis console, create an analytics streaming application `kda-word-count`. After creation, configure the code path and select the S3 Jar file that you uploaded.

Now go to the Role and edit its policy to add the S3 buckets and the Kinesis Data Streams to the list of resources.

Go back to the Kinesis application and run without snapshot.

Open the Flink dashboard and check the running jobs.

## Project Structure

```
├── [4.3K]  README.md
├── [ 155]  create-buckets.sh
├── [6.4K]  dependency-reduced-pom.xml
├── [  58]  download.sh
├── [5.1K]  pom.xml
└── [4.1K]  src
    └── [4.0K]  main
        └── [3.9K]  java
            └── [3.8K]  com
                └── [3.7K]  amazonaws
                    └── [3.6K]  services
                        └── [3.6K]  kinesisanalytics
                            └── [3.5K]  S3StreamingSinkJob.java

  20K used in 7 directories, 6 files
```