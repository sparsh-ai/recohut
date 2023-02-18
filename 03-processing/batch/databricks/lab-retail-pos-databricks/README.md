# Real-Time Point-of-Sale Analytics With the Data Lakehouse

## Introduction

Disruptions in the supply chain — from reduced product supply and diminished warehouse capacity — coupled with rapidly shifting consumer expectations for seamless omnichannel experiences are driving retailers to rethink how they use data to manage their operations. Prior to the pandemic, 71% of retailers named lack of real-time visibility into inventory as a top obstacle to achieving their omnichannel goals. The pandemic only increased demand for integrated online and in-store experiences, placing even more pressure on retailers to present accurate product availability and manage order changes on the fly. Better access to real-time information is the key to meeting consumer demands in the new normal.

In this lab, we’ll address the need for real-time data in retail, and how to overcome the challenges of moving real-time streaming of point-of-sale data at scale with a data lakehouse.

The point-of-sale (POS) system has long been the central piece of in-store infrastructure, recording the exchange of goods and services between retailer and customer. To sustain this exchange, the POS typically tracks product inventories and facilitates replenishment as unit counts dip below critical levels. The importance of the POS to in-store operations cannot be overstated, and as the system of record for sales and inventory operations, access to its data is of key interest to business analysts.

Historically, limited connectivity between individual stores and corporate offices meant the POS system (not just its terminal interfaces) physically resided within the store. During off-peak hours, these systems might phone home to transmit summary data, which when consolidated in a data warehouse, provide a day-old view of retail operations performance that grows increasingly stale until the start of the next night’s cycle.

![img1](https://user-images.githubusercontent.com/62965911/211191370-cddd3f56-980d-444f-b4b3-ac425971d876.png)

Modern connectivity improvements have enabled more retailers to move to a centralized, cloud-based POS system, while many others are developing near real-time integrations between in-store systems and the corporate back office. Near real-time availability of information means that retailers can continuously update their estimates of item availability. No longer is the business managing operations against their knowledge of inventory states as they were a day prior but instead is taking actions based on their knowledge of inventory states as they are now.

Modern connectivity improvements have enabled more retailers to move to a centralized, cloud-based POS system, while many others are developing near real-time integrations between in-store systems and the corporate back office. Near real-time availability of information means that retailers can continuously update their estimates of item availability. No longer is the business managing operations against their knowledge of inventory states as they were a day prior but instead is taking actions based on their knowledge of inventory states as they are now.

![img2](https://user-images.githubusercontent.com/62965911/211191373-0a0c2281-8494-41cf-91af-d061c885ec24.png)

To illustrate how the lakehouse architecture can be applied to POS data, we’ve developed a demonstration workflow within which we calculate a near real-time inventory. In it, we envision two separate POS systems transmitting inventoryrelevant information associated with sales, restocks and shrinkage data along with buy-online, pickup in-store (BOPIS) transactions (initiated in one system and fulfilled in the other) as part of a streaming inventory change feed. Periodic (snapshot) counts of product units on-shelf are captured by the POS and transmitted in bulk. These data are simulated for a one-month period and played back at 10x speed for greater visibility into inventory changes.

![img3](https://user-images.githubusercontent.com/62965911/211191375-a1a62cb0-a898-4456-b464-e9efb53d8672.png)

The ETL processes (as pictured above in Figure 3) represent a mixture of streaming and batch techniques. A two-staged approach with minimally transformed data captured in Delta tables representing our Silver layer separates our initial, more technically aligned ETL approach with the more business-aligned approach required for current inventory calculations. The second stage has been implemented using traditional structured streaming capabilities, something we may revisit with the new Delta Live Tables functionality as it makes its way toward general availability.