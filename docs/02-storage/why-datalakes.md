# Why we need Data Lakes?

## Before the cloud data lake architecture

To understand how cloud data lakes help with the growing data needs of an organization, its important for us to first understand how data processing and insights worked a few decades ago. Businesses often thought of data as something that supplemented a business problem that needs to be solved. The approach was business problem centric, and involved the following steps :-

1. Identify the problem to be solved.
2. Define a structure for data that can help solve the problem.
3. Collect or generate the data that adheres with the structure.
4. Store the data in an Online Transaction Processing (OLTP) database, such as SQL Servers.
5. Use another set of transformations (filtering, aggregations etc) to store data in Online Analytics Processing (OLAP) databases, SQL servers are used here as well.
6. Build dashboards and queries from these OLAP databases to solve your business problem.

For instance, when an organization wanted to understand the sales, they built an application for sales people to input their leads, customers, and engagements, along with the sales data, and this application was supported by one or more operational databases.For example, there could be one database storing customer information, another storing employee information for the sales force, and a third database that stored the sales information that referenced both the customer and the employee databases. On-premises (referred to as on-prem) have three layers:

1. Enterprise data warehouse - this is the component where the data is stored. It contains a database component to store the data, and a metadata component to describe the data stored in the database.
2. Data marts - data marts are a segment of the enteprise data warehouse, that contain a business/topic focused databases that have data ready to serve the application. Data in the warehouse goes through another set of transformations to be stored in the data marts.
3. Consumption/BI layer - this consists of the various visualization and query tools that are used by BI analysts to query the data in the data marts (or the warehouse) to generate insights.

![Traditional on-premises data warehouse](https://user-images.githubusercontent.com/62965911/213930653-e195afbb-1d65-4c41-8e47-b73bec31783c.png)

## On-premises Hadoop cluster vs Cloud data lakes

![On-premises versus cloud architectures](https://user-images.githubusercontent.com/62965911/213930652-1784028d-8974-46ed-9e7c-4924df84a5c2.png)

## Limitations of on-premises data warehouse solutions

While this works well for providing insights into the business, there are a few key limitations with this architecture, as listed below.

1. Highly structured data: This architecture expects data to be highly structured every step of the way. As we saw in the examples above, this assumption is not realistic anymore, data can come from any source such as IoT sensors, social media feeds, video/audio files, and can be of any format (JSON, CSV, PNG, fill this list with all the formats you know), and in most cases, a strict structure cannot be enforced.
2. Siloed data stores: There are multiple copies of the same data stored in data stores that are specialized for specific purposes. This proves to be a disadvantage because there is a high cost for storing these multiple copies of the same data, and the process of copying data back and forth is both expensive, error prone, and results in inconsistent versions of data across multiple data stores while the data is being copied.
3. Hardware provisioning for peak utilization: On-premises data warehouses requires organizations to install and maintain the hardware required to run these services. When you expect bursts in demand (think of budget closing for the fiscal year or projecting more sales over the holidays), you need to plan ahead for this peak utilization and buy the hardware, even if it means that some of your hardware needs to be lying around underutilized for the rest of the time. This increases your total cost of ownership. Do note that this is specifically a limitation with respect on on-premises hardware rather than a difference between data warehouse vs data lake architecture.