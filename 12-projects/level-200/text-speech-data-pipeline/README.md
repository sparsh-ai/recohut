# Data Pipeline for Text to Speech translation model

## Problem Statement

The objective is to build a data engineering pipeline that allows recording millions of Amharic and Swahili speakers reading digital texts on web platforms. We will design and build a Kafka cluster that can be used to post a sentence and receive an audio file. We will then deploy the system to process posting and receiving text and audio files from and into a data lake, apply transformation in a distributed manner, and load it into a warehouse in a suitable format to train a speech-to-text model.

## Architecture

A Front-end user interface will be developed to consume the text that is not transcribed from the Kafka topic and display it to the user. The user will record the transcription of the text and produce audio that will be published to Kafka again. To communicate with the Kafka connector Flask API will be used for back-end programming. Spark is used to prepossess the audio by consuming the raw audio from the Kafka topic. S3Bucket is used as a data lake to store the unprocessed audio, text, and processed audio. Furthermore, Airflow will be used to automate the data pipeline.

![arch](https://user-images.githubusercontent.com/62965911/215314028-bc0cb301-564f-4105-afbb-756dbd8b7668.png)

![arch2](https://user-images.githubusercontent.com/62965911/215314030-68e045bf-f1c3-4eb0-bbea-eb6327727efb.jpg)

- Front-end — created with Reactjs, is how we interact with users to upload an audio file or validate audio file submissions.
- Back-end (micro-service API) — Flask will be used to build the back-end (micro-service API), which will make it easier to facilitate communication between the front-end and Kafka for a seamless connection.
- Airflow — Airflow must orchestrate messages of Kafka while also starting the transformation and loading of data onto Spark.
- Spark — Spark will be utilized to convert and load the data as we standardize it to ensure consistency and dependability.
- Kafka cluster — This will be the brain of the entire system as it facilitates the production of messages (ex. Audio files) on a topic to publishing it to the consumers.
- S3 bucket — is used as a data lake for storing the unprocessed text-corpus and processed audio-text pair.

## Data

For this project, we have an Amharic news text corpus with six columns: categories, headlines, articles, dates, views, and links. The articles are categorized into six groups: Country, Sport, Politics, World, Business, and Entertainment. The data contains articles that have a large number of words. So we did simple preprocessing to split those articles into sentences and ensure the spacing between the words is correct.

## Front end

![frontend](https://user-images.githubusercontent.com/62965911/215314035-ac677f8c-0ce0-4603-9999-cb68083dadb7.png)

## Output

![output](https://user-images.githubusercontent.com/62965911/215314037-8c0aba6e-452d-4339-ab3c-c67d5edd2279.png)

## Project Structure

```
├── [ 61K]  01-sa-main.ipynb
├── [ 34K]  02-sa-preprocessing.ipynb
├── [ 37K]  03-sa-twitter-couchdb.ipynb
├── [4.1K]  README.md
├── [ 17K]  airflow
│   ├── [ 11K]  dags
│   │   ├── [3.5K]  __pycache__
│   │   │   └── [3.4K]  dag.cpython-39.pyc
│   │   └── [7.2K]  dag.py
│   ├── [ 326]  run.sh
│   └── [6.0K]  sql
│       ├── [2.6K]  create_tables.sql
│       ├── [ 347]  happiness_insert.sql
│       ├── [ 369]  sources_insert.sql
│       ├── [ 748]  temperature_insert.sql
│       ├── [ 882]  time_insert.sql
│       ├── [ 808]  tweets_insert.sql
│       └── [  70]  users_insert.sql
├── [6.5K]  assets
│   └── [6.4K]  _DATADICT.md
├── [ 471]  config.cfg
├── [ 141]  data
│   └── [  45]  download.sh
├── [ 250]  download.sh
└── [1.7K]  requirements.txt

 332K used in 7 directories, 22 files
```