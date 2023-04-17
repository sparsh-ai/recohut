# Lab: Step Function Athena SNS

Objective: Execute multiple queries (Amazon Athena, Amazon SNS)

This lab demonstrates how to run Athena queries in succession and then in parallel, handle errors and then send an Amazon SNS notification based on whether the queries succeed or fail. Deploying this lab will create an AWS Step Functions state machine, Amazon Athena queries, and an Amazon SNS topic.

![](https://user-images.githubusercontent.com/62965911/214565067-21963523-65e6-4c80-89c3-0347661cb490.png)

In this lab, Step Functions uses a state machine to run Athena queries synchronously. After the query results are returned, enter parallel state with two Athena queries executing in parallel. It then waits for the job to succeed or fail, and it sends an Amazon SNS topic with a message about whether the job succeeded or failed.