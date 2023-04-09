# SQL Danny's Diner Assignment

Danny seriously loves Japanese food so in the beginning of 2021, he decides to embark upon a risky venture and opens up a cute little restaurant that sells his 3 favourite foods: sushi, curry and ramen.

Danny’s Diner is in need of your assistance to help the restaurant stay afloat - the restaurant has captured some very basic data from their few months of operation but have no idea how to use their data to help them run the business.

Danny wants to use the data to answer a few simple questions about his customers, especially about their visiting patterns, how much money they’ve spent and also which menu items are their favourite. Having this deeper connection with his customers will help him deliver a better and more personalised experience for his loyal customers.

He plans on using these insights to help him decide whether he should expand the existing customer loyalty program - additionally he needs help to generate some basic datasets so his team can easily inspect the data without needing to use SQL.

Danny has provided you with a sample of his overall customer data due to privacy issues - but he hopes that these examples are enough for you to write fully functioning SQL queries to help him answer his questions!

Danny has shared with you 3 key datasets for this case study:

- sales
- menu
- members

You can inspect the entity relationship diagram and example data below.

![](https://user-images.githubusercontent.com/62965911/214232256-4c26d883-a538-4a83-851e-ccc2e605976d.png)

## Seed

Use the following seed code to populate the data in your database:

```sql
CREATE SCHEMA IF NOT EXISTS dannys_diner;
USE SCHEMA dannys_diner;

DROP TABLE IF EXISTS sales;
CREATE TABLE sales (
  "customer_id" VARCHAR(1),
  "order_date" DATE,
  "product_id" INTEGER
);
INSERT INTO sales
  ("customer_id", "order_date", "product_id")
VALUES
  ('A', '2021-01-01', '1'),
  ('A', '2021-01-01', '2'),
  ('A', '2021-01-07', '2'),
  ('A', '2021-01-10', '3'),
  ('A', '2021-01-11', '3'),
  ('A', '2021-01-11', '3'),
  ('B', '2021-01-01', '2'),
  ('B', '2021-01-02', '2'),
  ('B', '2021-01-04', '1'),
  ('B', '2021-01-11', '1'),
  ('B', '2021-01-16', '3'),
  ('B', '2021-02-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-01', '3'),
  ('C', '2021-01-07', '3');
 
DROP TABLE IF EXISTS menu;
CREATE TABLE menu (
  "product_id" INTEGER,
  "product_name" VARCHAR(5),
  "price" INTEGER
);
INSERT INTO menu
  ("product_id", "product_name", "price")
VALUES
  ('1', 'sushi', '10'),
  ('2', 'curry', '15'),
  ('3', 'ramen', '12');
  
DROP TABLE IF EXISTS members;
CREATE TABLE members (
  "customer_id" VARCHAR(1),
  "join_date" DATE
);
INSERT INTO members
  ("customer_id", "join_date")
VALUES
  ('A', '2021-01-07'),
  ('B', '2021-01-09');
```

## Questions

Answer the following questions:

1. What is the total amount each customer spent at the restaurant?
2. How many days has each customer visited the restaurant?
3. What was the first item from the menu purchased by each customer?
4. What is the most purchased item on the menu and how many times was it purchased by all customers?
5. Which item was the most popular for each customer?
6. Which item was purchased first by the customer after they became a member?
7. Which item was purchased just before the customer became a member?
8. What is the total items and amount spent for each member before they became a member?
9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?

## Answers

```sql
-- How many days each customer spent at restaurent 
SELECT
    "customer_id",
    COUNT(DISTINCT "order_date") AS total_days_spent
FROM sales
GROUP BY "customer_id"
ORDER BY total_days_spent DESC
;

-- What was the first item from the menu purchased by each customer?
SELECT
    DISTINCT s."customer_id",
    s."order_date",	
    m."product_name"
FROM dannys_diner.sales as s
INNER JOIN dannys_diner.menu as m 
	ON s."product_id" = m."product_id"
ORDER BY s."order_date"
LIMIT 3
;

-- What is the most purchased item on the menu and how many times 
 SELECT 
      m.product_name as product_name,
      count(m.product_id) as Total_no_of_times_purc
  FROM dannys_diner.sales s
  INNER JOIN dannys_diner.menu m
      ON s.product_id = m.product_id
  GROUP BY m.product_name
  ORDER BY Total_no_of_times_purc DESC
;

-- Which item was the most popular for each customer?
WITH fav_item_cte AS
(
 SELECT 
  	s.customer_id as customer_id,
  	m.product_name as product_name, 
    COUNT(m.product_id) AS order_count,
    DENSE_RANK() OVER(
          PARTITION BY s.customer_id
          ORDER BY COUNT(s.customer_id) DESC
          ) AS rank
FROM dannys_diner.menu AS m
JOIN dannys_diner.sales AS s
 	ON m.product_id = s.product_id
GROUP BY s.customer_id, m.product_name
)

SELECT 
	customer_id,
    product_name,
    order_count
FROM fav_item_cte
WHERE rank =1
;

-- Which item was purchased first by the customer after they became a member?
WITH ordered_after_member AS
(
  SELECT 
      s.customer_id as ID
      ,m.product_name as name
      ,s.order_date as ordered_date
      ,DENSE_RANK() OVER(
          PARTITION BY s.customer_id
          ORDER BY s.order_date
      ) as rank
  FROM dannys_diner.sales s
  INNER JOIN dannys_diner.menu m
      ON s.product_id  = m.product_id
  INNER JOIN dannys_diner.members mem
      ON s.customer_id = mem.customer_id
  WHERE s.order_date >= mem.join_date
)

SELECT 
	*
FROM ordered_after_member
WHERE rank = 1
;

--  What is the total items and amount spent for each member before they became a member?
SELECT 
      s.customer_id as ID
      ,COUNT(m.product_id) as total_item
  FROM dannys_diner.sales s
  INNER JOIN dannys_diner.menu m
      ON s.product_id  = m.product_id
  INNER JOIN dannys_diner.members mem
      ON s.customer_id = mem.customer_id
  WHERE s.order_date < mem.join_date
  group by ID
;

SELECT 
      s.customer_id as ID
      ,CONCAT(SUM(m.price),'$') as total_price
  FROM dannys_diner.sales s
  INNER JOIN dannys_diner.menu m
      ON s.product_id  = m.product_id
  INNER JOIN dannys_diner.members mem
      ON s.customer_id = mem.customer_id
  WHERE s.order_date < mem.join_date
  group by ID
  
-- If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
SELECT 
	s.customer_id,
    SUM(
      CASE
        	WHEN m.product_name = 'sushi'
            THEN m.price*20
      		ELSE m.price*10
    	END 
    ) AS Total_points
FROM dannys_diner.sales s 
INNER JOIN dannys_diner.menu m
	ON s.product_id  = m.product_id
GROUP BY s.customer_id
;

-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?
SELECT 
	s.customer_id as ID
  	,(SUM(m.price)*20) As Total_points
    
FROM dannys_diner.sales s
INNER JOIN dannys_diner.menu m
    ON s.product_id  = m.product_id
INNER JOIN dannys_diner.members mem
     ON s.customer_id = mem.customer_id
WHERE s.order_date >= mem.join_date AND s.order_date BETWEEN '2021-01-01' AND '2021-01-31'
GROUP BY  ID
;
```