# Inmon versus the Kimball data model

If you look at the internet, there will be many references to data modeling, but two of the most famous approaches are the **Inmon** method (data-driven) and the **Kimball** method (user-driven).

We will take a quick look at these methods, but we won't spend much time or go into too much detail in this note since there are so many details to explain regarding the framework. I suggest you do some more in-depth research from other resources regarding these two methods to better understand the step-by-step approaches and the frameworks. What we want to learn from them are the differences and the thinking processes behind them.

At a very high level, the Inmon method focuses on building a central data warehouse or single source of truth. To achieve that, the data model must be highly normalized to the lowest level, so the data can be highly consistent. The Inmon data model follows a top-down approach, which means the data warehouse is built as the central data source for all the downstream data marts, sometimes referred to as the **Enterprise Data Warehouse**. The downstream data marts need to follow the rules from the data warehouse, as in this figure. Imagine the gray boxes are tables. 

![B16851_03_41](https://user-images.githubusercontent.com/62965911/219542336-5dc33337-2996-4feb-abc7-89b178c9ec9d.jpg)

Compared to the Inmon method, the Kimball method focuses on answering user questions and follows a bottom-up approach. This method keeps end user questions in mind and uses the questions as a basis to build necessary tables. The goal is to ease end user accessibility and provide a high level of performance improvement.

The tables may contain the entity's basic information and its measurements. This is what are now known as fact and dimension tables. A **fact table** is a collection of measurements or metrics in a predefined granularity. A **dimension table** is a collection of entity attributes that support the fact tables. This collection of fact and dimension tables will later be the data warehouse. 

Here is an example of a fact table. The fact table has two measurements that measure customers in daily granularity:

![B16851_03_42](https://user-images.githubusercontent.com/62965911/219542340-a84d6156-e7ed-49d8-b97a-85644f3de1f9.jpg)

Here is an example of a dimension table with **Customer ID** as the primary key and the attributes:

![B16851_03_43](https://user-images.githubusercontent.com/62965911/219542343-d63c8ffc-d3b7-4409-99c1-788025412491.jpg)

As you can see from the examples, the facts and dimension tables are different. So how do they relate together as a data model?

One of the most well-known data models for the Kimball method is the star schema. The star schema follows the fact and dimension table relations. There is a rule of thumb regarding the star schema that a dimension table can't have parent tables, which means the dimension is a denormalized table. Check the following diagram, which provides a high-level illustration of a data warehouse using the Kimball approach. Imagine that all the gray boxes are tables:

![B16851_03_44](https://user-images.githubusercontent.com/62965911/219542344-c9fcd477-c631-451c-b0f9-ed8b17b731dc.jpg)

The pros and cons of both methods are summarized as follows:

![B16851_03_45](https://user-images.githubusercontent.com/62965911/219542350-d8a15c63-644d-4dac-8032-3c321258265b.jpg)

Use the table comparison as your reference when deciding between the Inmon or Kimball methods. This is usually not a straightforward and quick decision to make. It's a difficult decision because choosing one of them means your entire organization needs to commit to the data model for the long term. An experienced data modeler is usually the best person to decide this.