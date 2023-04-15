# Lab: Cybersecurity Databricks

## Objective

Building a Cybersecurity Lakehouse for CrowdStrike Falcon Events

## Introduction

Endpoint data is required by security teams for threat detection, threat hunting, incident investigations and to meet compliance requirements. The data volumes can be terabytes per day or petabytes per year. Most organizations struggle to collect, store and analyze endpoint logs because of the costs and complexities associated with such large data volumes. But it doesn’t have to be this way.

In this lab, we will learn how to operationalize petabytes of endpoint data with Databricks to improve the organizations's security posture with advanced analytics in a cost-effective way. 

We will use CrowdStrike’s Falcon logs as our example. To access Falcon logs, one can use the Falcon Data Replicator (FDR) to push raw event data from CrowdStrike’s platform to cloud storage such as Amazon S3. This data can be ingested, transformed, analyzed and stored using the Databricks Lakehouse Platform alongside the rest of their security telemetry. Customers can ingest CrowdStrike Falcon data, apply Python-based real-time detections, search through historical data with Databricks SQL, and query from SIEM tools like Splunk with Databricks Add-on for Splunk.

## Architecture

Auto Loader and Delta Lake simplify the process of reading raw data from cloud storage and writing to a Delta table at low cost and with minimal DevOps work. In this architecture, semi-structured CrowdStrike data is loaded to the customer’s cloud storage in the landing zone. Then Auto Loader uses cloud notification services to automatically trigger the processing and ingestion of new files into the customer’s Bronze tables, which will act as the single source of truth for all downstream jobs. Auto Loader will track processed and unprocessed files using checkpoints in order to prevent duplicate data processing. 

![](https://user-images.githubusercontent.com/62965911/214503749-fa3a5650-4dd6-4820-89d9-3a9bb7a72b19.png)

As we move from the Bronze to the Silver stage, schema will be added to provide structure to the data. Since we are reading from a single source of truth, we are able to process all of the different event types and enforce the correct schema as they are written to their respective tables. The ability to enforce schemas at the Silver layer provides a solid foundation for building ML and analytical workloads.

The Gold stage, which aggregates data for faster query and performance in dashboards and BI tools, is optional, depending on the use case and data volumes. Alerts can be set to trigger when unexpected trends are observed. 

Another optional feature is the Databricks Add-on for Splunk, which allows security teams to take advantage of Databricks cost-effective model and the power of AI without having to leave the comforts of Splunk. Customers can run ad hoc queries against Databricks from within a Splunk dashboard or search bar with the add-on. Users can also launch notebooks or jobs in Databricks through a Splunk dashboard or in response to a Splunk search. The Databricks integration is bidirectional, letting customers summarize noisy data or run detections in Databricks that show up in Splunk Enterprise Security. Customers can even run Splunk searches from within a Databricks notebook to prevent the need to duplicate data.

The Splunk and Databricks integration allows customers to reduce costs, expand the data sources they analyze and provide the results of a more robust analytics engine, all without changing the tools used by their staff day-to-day.