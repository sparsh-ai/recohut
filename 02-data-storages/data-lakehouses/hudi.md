---
title: Apache Hudi
description: Bring transactions, record-level updates/deletes and change streams to data lakes!
tags: [hudi]
---

Apache Hudi is an open-source data management framework used to simplify incremental data processing and data pipeline development by providing record-level insert, update, upsert, and delete capabilities. Upsert refers to the ability to insert records into an existing dataset if they do not already exist or to update them if they do. By efficiently managing how data is laid out in Amazon S3, Hudi allows data to be ingested and updated in near real time. Hudi carefully maintains metadata of the actions performed on the dataset to help ensure that the actions are atomic and consistent.

Hudi is a rich platform to build streaming data lakes with incremental data pipelines
on a self-managing database layer, while being optimized for lake engines and regular batch processing.

![](https://user-images.githubusercontent.com/62965911/213927494-a34ab9fe-0bdb-4b7e-a39a-23e8275e196d.png)