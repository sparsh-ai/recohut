# Step Function Ecommerce SQL

Objective: Orchestrate Queue-based Microservices

In this lab, you will learn how to use AWS Step Functions and Amazon SQS to design and run a serverless workflow that orchestrates a message queue-based microservice. Step Functions is a serverless orchestration service that lets you easily coordinate multiple AWS services into flexible workflows that are easy to debug and easy to change. Amazon SQS is the AWS service that allows application components to communicate in the cloud.

![](https://user-images.githubusercontent.com/62965911/214565074-373805b7-af41-4686-94c5-0b11be69afc2.png)

This lab will simulate inventory verification requests from incoming orders in an e-commerce application as part of an order processing workflow. Step Functions will send inventory verification requests to a queue on SQS. An AWS Lambda function will act as your inventory microservice that uses a queue to buffer requests. When it retrieves a request, it will check inventory and then return the result to Step Functions. When a task in Step Functions is configured this way, it is called a callback pattern. Callback patterns allow you to integrate asynchronous tasks in your workflow, such as the inventory verification microservice of this lab.