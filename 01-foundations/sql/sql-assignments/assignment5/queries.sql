/* --------------------
   Case Study Questions
   --------------------*/

-- 1. What is the total amount each customer spent at the restaurant?
-- 2. How many days has each customer visited the restaurant?
-- 3. What was the first item from the menu purchased by each customer?
-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?
-- 5. Which item was the most popular for each customer?
-- 6. Which item was purchased first by the customer after they became a member?
-- 7. Which item was purchased just before the customer became a member?
-- 8. What is the total items and amount spent for each member before they became a member?
-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?


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