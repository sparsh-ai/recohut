# Data Engineering Take Home - ETL off a SQS Qeueue

This challenge will focus on your ability to write a small application that can read from an AWS SQS Qeueue, transform that data, then write to a Postgres database. Your objective is to read JSON data containing user login behavior from an AWS SQS Queue. Fetch wants to hide personal identifiable information (PII). The fields device_id and ip should be masked, but in a way where it is easy for data analysts to identify duplicate values in those fields. Once you have flattened the JSON data object and masked those two fields, write each record to a Postgres database. 

The target table's DDL is:

```
-- Creation of user_logins table

CREATE TABLE IF NOT EXISTS user_logins(
    user_id             varchar(128),
    device_type         varchar(32),
    masked_ip           varchar(256),
    masked_device_id    varchar(256),
    locale              varchar(32),
    app_version         integer,
    create_date         date
);
```

You will have to make a number of decisions as you develop this solution:

- How will you read messages from the queue?
- What type of data structures should be used?
- How will you mask the PII data so that duplicate values can be identified?
- What will be your strategy for connecting and writing to Postgres?
- Where and how will your application run?

For this assignment an ounce of communication and organization is worth a pound of execution. Please answer the following questions:

- How would you deploy this application in production?
- What other components would you want to add to make this production ready?
- How can this application scale with a growing data set.
- How can PII be recovered later on?

## Infra Setup

The following docker compose setup the infra:

```yml title="docker-compose.yml"
version: "3.9"
services:
  localstack:
    image: localstack/localstack:0.14.3
    network_mode: bridge
    ports:
      - "127.0.0.1:443:443"              # only required for Pro (LocalStack HTTPS Edge Proxy)
      - "127.0.0.1:4510-4559:4510-4559"  # external service port range
      - "127.0.0.1:4566:4566"            # LocalStack Edge Proxy
    environment:
      - DEBUG=${DEBUG-}
      - LAMBDA_EXECUTOR=${LAMBDA_EXECUTOR-}
      - HOST_TMP_FOLDER=${TMPDIR:-/tmp/}localstack
      - DOCKER_HOST=unix:///var/run/docker.sock
      - HOSTNAME_EXTERNAL=localstack
    volumes:
      - "${TMPDIR:-/tmp}/localstack:/tmp/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
      - ${PWD}/data/sample_data.json.gz:/tmp/data/sample_data.json.gz
      - ${PWD}/scripts/create_and_write_to_queue.py:/tmp/scripts/create_and_write_to_queue.py
      - ${PWD}/scripts/transformation.py:/tmp/scripts/transformation.py
      - ${PWD}/scripts/01_call_python_scripts.sh:/docker-entrypoint-initaws.d/01_call_python_scripts.sh
  postgres:
    image: postgres:10
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - 5432:5432
    expose:
      - 5432
    volumes:
      - ${PWD}/scripts/create_table.sql:/docker-entrypoint-initdb.d/create_table.sql
```

-   An AWS SQS Queue is created
-   A script is run to write 100 JSON records to the queue
-   A Postgres database will be stood up
-   A user_logins table will be created in the public schema


## Implementation Steps

1. Flattened the JSON data file and stored the processed data in a dataframe
2. Masked 'device_id' and 'ip' columns in such a way where it is easy for data analysts to identify duplicate values in those fields
3. The transformed dataframe is then stored in a postgresql table called user_logins using python script

## Implementation Procedure

We can read messages from the queue using boto3 client function. This helps us to connect to the AWS account and create a queue and pull the json file. I masked the columns using label encoder. I used this method because this is an excellent way to also identify duplicate values from the masked the data. The unmasking process is also easy, just use inverse_transform function at the receiver side and the data is decrypted back to its original form. 
The application will run on the AWS server since the SQS data queue is hosted on AWS. 
The transformed data is stored in a postgresql table. PostgreSql server is hosted on Docker desktop. All the connection details were taken from there. 


## Future scope

1. How would you deploy this application in production?

--> While deploying the application in production one should endure that the database is configured. Security is configured to avoid data breach issues. The application should be pushed to a package.

2) What other components would you want to add to make this production ready?

--> We can do automation testing on the application to ensure that the application is robust enough and does not break down more often. We can also add a user friendly website or dashboard where he/she can start and stop the entire ETL process or we can automate the entire process to run at regular intervals (daily/weekly,etc.) and the user can just invade in the process when there is an error in the process. 
There should also be a CI framework where new code can be integrated easily without much changes and user can also keep a track of the commit changes done to the framework. 

3) How can this application scale with a growing data set.

--> By using load balancers we can balance out the data. This would help scale the data and also avoid overloading issues when the dataset grows in size. Also, in order to avoid server downtime issues, we can use web proxy servers.

4) How can PII be recovered later on?

--> We can recover back the masked data using inverse_tranform function present in sklearn library.


### How will you read messages from the queue?

To read messages from the queue, I would use the receive_message method of the boto3 library, which is the AWS SDK for Python. This method allows me to specify the URL of the queue and the maximum number of messages to retrieve in a single request.

I would then use a loop to continually retrieve messages from the queue and process them as needed. After processing a message, I would use the delete_message method to remove it from the queue. This would ensure that the message is only processed once and that it does not clog up the queue.

In addition to these basic steps, I would also need to handle error cases such as the queue being empty or the request timing out. I would also need to implement retry logic to handle cases where the message processing fails due to temporary issues or network errors.

### What type of data structures should be used?

I will need to use a few different data structures for this project. A queue data structure will be useful for storing the messages that I retrieve from the AWS SQS queue. I will need to parse the JSON data contained in the messages, so I will use a dictionary or object data structure to store the data for each individual record. The data will need to be stored in a database, so I will use a database table data structure to represent the user_logins table in the Postgres database. I may also need to use additional data structures, such as lists or arrays, to store intermediate results or perform calculations on the data as I process it.

### How will you mask the PII data so that duplicate values can be identified?

In this code, the PII data is masked by encoding the ip and device_id fields using base64 encoding. This process converts the plaintext values of these fields into a series of ASCII characters, which can then be represented as a series of base64 characters.

The base64 encoding is done using the base64_encode function, which takes in a plain string as input and returns the base64 encoded version of that string. The ip and device_id fields are passed through this function and the resulting encoded strings are then stored back in the message_body dictionary, replacing the original values of these fields.

This method of masking allows data analysts to easily identify duplicate values in the ip and device_id fields, because even if two records have the same original values for these fields, they will have different encoded values. This means that analysts can still distinguish between different records and identify duplicates, even though the original PII data is not visible.

### What will be your strategy for connecting and writing to Postgres?

To connect to and write to Postgres, you can use a library such as psycopg2. This library provides a Python interface to PostgreSQL, allowing you to connect to a PostgreSQL database, create cursors for executing SQL queries, and commit transactions.

To use psycopg2, you will first need to install it using pip. Once you have psycopg2 installed, you can use it to connect to a PostgreSQL database by creating a connection object. For example:

```py
import psycopg2

# Connect to PostgreSQL
postgres_conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'postgres'
)
```

This will create a connection to a PostgreSQL database running on localhost, using the postgres database and the postgres user with the password postgres.

To execute SQL queries and write data to the database, you can create a cursor object using the connection object. You can then use the cursor to execute SQL queries and commit the results to the database. Once you are finished writing to the database, you should close the cursor and the connection to the database to release any resources being used.

### Where and how will your application run?

My application will run as a standalone script that can be executed from the command line. It will connect to the AWS SQS queue running on localhost, read the JSON data from the queue, mask the device_id and ip fields, and write the transformed data to the Postgres database running on localhost. The script can be run manually at any time by the user, or it can be set up to run on a schedule using a cron job or similar scheduling tool.

To run the script, the user will need to have the necessary dependencies installed, including python3, pip3, awslocal, docker, and docker-compose. The user will also need to start the localstack and Postgres docker containers using the provided docker-compose file. Once the containers are running, the user can execute the script using the appropriate command line arguments, such as the host and port for the SQS queue and the Postgres database. The script will then read from the SQS queue, transform the data, and write the transformed data to the Postgres database until all messages in the queue have been processed. Once the script has completed, the user can stop the docker containers and optionally clean up the docker resources using the provided make commands.

### How would you deploy this application in production?

There are several ways to deploy this application in production, and the specific approach will depend on the requirements and constraints of the production environment. Below are some potential options for deploying the application:

Run the script as a standalone application on a dedicated server or virtual machine (VM). This would require installing the necessary dependencies (python3, boto3, psycopg2, AWS CLI) on the server, setting up the production Postgres database, and configuring the script to connect to the appropriate SQS queue and Postgres database. The script could be scheduled to run periodically using a cron job or similar scheduling tool.

Use a containerization platform such as Docker to package the application and its dependencies into a container image, and then run the container in a production environment. This would allow for easier deployment and scaling of the application, as well as consistent execution environments across different servers or VMs.

Use a serverless platform such as AWS Lambda to execute the application in response to specific events, such as messages being added to the SQS queue. This would eliminate the need to manage infrastructure and scale the application manually, as the serverless platform would handle these tasks automatically.

Regardless of the chosen deployment approach, it would be important to ensure that the production environment is secure and that the application is able to handle any errors or exceptions that may occur during execution. It may also be necessary to implement logging and monitoring to track the performance and health of the application.

### What other components would you want to add to make this production ready?

To make this application production-ready, I would recommend adding the following components:

Error handling: Add try-except blocks and/or error logging to handle exceptions that may occur during execution and ensure that the application does not crash.

Monitoring and alerting: Implement monitoring and alerting to track the performance and health of the application, and receive notifications if issues arise.

Security: Implement security measures such as encryption of sensitive data, secure connections to databases and other external resources, and access controls to prevent unauthorized access to the application and data.

Scalability: Add mechanisms to scale the application up or down based on workload, such as using a container orchestration platform or serverless functions.

Disaster recovery: Implement disaster recovery measures to ensure that the application can recover from failures or outages, such as backing up data and having a plan in place to restore the application in the event of a disaster.

Testing: Perform testing of the application to ensure that it is functioning correctly and meets the required specifications. This may include unit tests, integration tests, and end-to-end tests.

### How can this application scale with a growing data set?

There are several ways to scale this application to handle a growing data set:

Use a load balancer: Set up a load balancer to distribute incoming requests across multiple instances of the application, allowing the application to scale horizontally as the workload increases.

Use a distributed database: If the Postgres database becomes a bottleneck, consider using a distributed database system that can scale horizontally across multiple servers. This would allow the application to continue writing data to the database as the data set grows.

Use a serverless platform: Consider using a serverless platform such as AWS Lambda to execute the application in response to specific events, such as messages being added to the SQS queue. This would allow the application to scale automatically based on workload, without the need to manually provision and configure additional servers or VMs.

Use a queue-based architecture: Implement a queue-based architecture, where the application writes data to a queue instead of directly to the database. This would allow the application to scale independently of the database and decouple the data ingestion and processing stages, allowing them to scale separately.

Use a distributed cache: Consider using a distributed cache, such as Redis, to store frequently accessed data in memory, reducing the load on the database and improving the performance of the application.

Use a data lake: If the data set becomes too large to process in real-time, consider storing the data in a data lake and using batch processing or stream processing to analyze the data as needed. This would allow the application to scale to very large data sets by offloading the data

### How can PII be recovered later on?

Personal identifiable information (PII) can be recovered later on by reversing the process used to mask the PII data. For example, if the PII data was encoded using base64 encoding, it can be recovered by decoding the base64-encoded data back to its original form.

It is important to note that PII data should be treated with caution and handled in accordance with relevant laws and regulations, as well as any applicable privacy policies. If PII data is masked or encoded for security or privacy reasons, it may be necessary to have a secure process in place for accessing the original data when needed, such as requiring authentication and authorization from authorized personnel. It may also be necessary to have a secure and auditable process for storing and handling the original PII data to ensure that it is not accessed or modified by unauthorized individuals.