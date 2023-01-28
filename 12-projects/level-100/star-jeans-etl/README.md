# ETL Building for an E-commerce Jeans Company

*Obs: The company and business problem are both fictitious, although the data is real.*

We managed to create an ETL process that extracts data from H&M, a Star Jeans competitor, cleans it, and saves it to a PostgreSQL database on a weekly basis. Then, the database can be added and displayed with filters in a Streamlit App, where it can be accessed from anywhere by Star Jeans' owners, so they can have a better understanding on how the USA male jeans market works.

# Star Jeans and Business Problem

Michael, Franklin and Trevor, after several successful businesses, are starting new a company called Star Jeans. For now, their plan is to enter the USA fashion market through an E-commerce. The initial idea is to sell one product for a specific audience, which is male jeans. Their goal is to keep prices low and slowly increase them, as they get new clients. However, this market already has strong competitors, such as H&M for instance. In addition to that, the three businessmen aren't familiar with this segment in particular. Therefore, in order to better understand how this market works they hired a Data Science/Engineering freelancer, to gather information regarding H&M. They want to know the following information about H&M male jeans:

- Product Name
- Product Type
- Product Fit
- Product Color
- Product Composition
- Product Price

## Solution

| Job | Task Name                  | Task Description                                                                  | Script                                                                                                                               |
| --- | -------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 01  | Data Showroom Extraction   | Scraping product\_id and product\_type in showroom page                           | [webscraping-hm.py](./src/webscraping-hm.py) |
| 02  | Data Attributes Extraction | Getting other attributes from each product and saving it all in Pandas DataFrame  | [webscraping-hm.py](./src/webscraping-hm.py) |
| 03  | Data Cleaning              | Renaming and rearranging columns, dealing with data types, NaN's, duplicates, etc | [webscraping-hm.py](./src/webscraping-hm.py) |
| 04  | Data Inserting             | Inserting data in PostgreSQL Database                                             | [webscraping-hm.py](./src/webscraping-hm.py) |
| 05  | Streamlit App Data Loading | Loading Database in Streamlit App                                                 | [star-jeans-app.py](./streamlit-app/star-jeans-app.py)                                     |
| 06  | Streamlit App Data Display | Displaying data and adding filters in Streamlit App                               | [star-jeans-app.py](./streamlit-app/star-jeans-app.py)                                     |

![arch](https://user-images.githubusercontent.com/62965911/215284786-e08ac928-bdba-46e9-9393-0e973c55ba80.png)