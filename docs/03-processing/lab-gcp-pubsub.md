# Lab: Streaming Data Processing - Publish Streaming Data into PubSub

## Objective

Google Cloud Pub/Sub is a fully-managed real-time messaging service that allows you to send and receive messages between independent applications. Use Cloud Pub/Sub to publish and subscribe to data from multiple sources, then use Google Cloud Dataflow to understand your data, all in real time.

In this lab, you will simulate your traffic sensor data into a Pub/Sub topic for later to be processed by Dataflow pipeline before finally ending up in a BigQuery table for further analysis.

In this lab, you will perform the following tasks:

-   Create a Pub/Sub topic and subscription
-   Simulate your traffic sensor data into Pub/Sub

## Preparation

- Go to the Compute > VM > training-vm instance
- Connect via SSH
- Verify by listing our the files - `ls /training`
 
![](https://user-images.githubusercontent.com/62965911/211212971-f62f3c34-cec9-4969-821a-75a1b97cdb60.png)

- Next you will download a code repository for use in this lab:

```
git clone https://github.com/GoogleCloudPlatform/training-data-analyst
```

- Set the DEVSHELL_PROJECT_ID environment variable and export it so it will be available to other shells:

```
export DEVSHELL_PROJECT_ID=$(gcloud config get-value project)
```

## Create Pub/Sub topic and subscription

- On the training-vm SSH terminal, navigate to the directory for this lab:

```
cd ~/training-data-analyst/courses/streaming/publish
```

- Create your topic and publish a simple message:

```
gcloud pubsub topics create sandiego
```

- Publish a simple message:

```
gcloud pubsub topics publish sandiego --message "hello"
```

- Create a subscription for the topic:

```
gcloud pubsub subscriptions create --topic sandiego mySub1
```

- Pull the first message that was published to your topic:

```
gcloud pubsub subscriptions pull --auto-ack mySub1
```

Do you see any result? If not, why?

- Try to publish another message and then pull it using the subscription:

```
gcloud pubsub topics publish sandiego --message "hello again"
gcloud pubsub subscriptions pull --auto-ack mySub1
```

Did you get any response this time?

- In the training-vm SSH terminal, cancel your subscription:

```
gcloud pubsub subscriptions delete mySub1
```

![](https://user-images.githubusercontent.com/62965911/211212970-18a2c9ef-0725-422d-862d-2d88c4e38bc2.png)

## Simulate traffic sensor data into Pub/Sub

- Explore the python script to simulate San Diego traffic sensor data. Do not make any changes to the code.

```
cd ~/training-data-analyst/courses/streaming/publish
nano send_sensor_data.py
```

Look at the simulate function. This one lets the script behave as if traffic sensors were sending in data in real time to Pub/Sub. The speedFactor parameter determines how fast the simulation will go. Exit the file by pressing Ctrl+X.

- Download the traffic simulation dataset:

```
./download_data.sh
```

- Simulate streaming sensor data. Run the send_sensor_data.py:

```
./send_sensor_data.py --speedFactor=60 --project $DEVSHELL_PROJECT_ID
```

This command simulates sensor data by sending recorded sensor data via Pub/Sub messages. The script extracts the original time of the sensor data and pauses between sending each message to simulate realistic timing of the sensor data. The value speedFactor changes the time between messages proportionally. So a speedFactor of 60 means "60 times faster" than the recorded timing. It will send about an hour of data every 60 seconds.

Leave this terminal open and the simulator running.

![](https://user-images.githubusercontent.com/62965911/211212968-b34434d3-046a-486f-9f96-d98da24243dc.png)

## Verify that messages are received

- Open a second SSH terminal and connect to the training VM

- Change into the directory you were working in:

```
cd ~/training-data-analyst/courses/streaming/publish
```

- Create a subscription for the topic and do a pull to confirm that messages are coming in (note: you may need to issue the 'pull' command more than once to start seeing messages):

```
gcloud pubsub subscriptions create --topic sandiego mySub2
gcloud pubsub subscriptions pull --auto-ack mySub2
```

- Confirm that you see a message with traffic sensor information.

![](https://user-images.githubusercontent.com/62965911/211212961-0bdc468e-d6ea-4b16-8904-98c1ac231ebf.png)

- Cancel this subscription:

```
gcloud pubsub subscriptions delete mySub2
```

- Close the second terminal:

```
exit
```

- Stop the sensor simulator. Return to the first terminal.

- Interrupt the publisher by typing Ctrl+C to stop it.

- Close the first terminal:

```
exit
```