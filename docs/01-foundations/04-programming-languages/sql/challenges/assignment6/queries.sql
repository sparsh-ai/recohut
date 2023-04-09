-- Data Cleaning and Transformation
CREATE TEMPORARY TABLE temp_customer_orders AS
SELECT "order_id", "customer_id", "pizza_id", 
  CASE 
    WHEN "exclusions" IS null OR "exclusions" LIKE 'null' THEN ' '
    ELSE "exclusions"
    END AS "exclusions",
  CASE 
    WHEN "extras" IS NULL or "extras" LIKE 'null' THEN ' '
    ELSE "extras"
    END AS "extras", 
  "order_time"
FROM customer_orders;

-- Data Cleaning and Transformation
CREATE TEMPORARY TABLE temp_runner_orders AS
SELECT "order_id", "runner_id",
  CASE 
    WHEN "pickup_time" LIKE 'null' THEN ' '
    ELSE "pickup_time" 
    END AS "pickup_time",
  CASE 
    WHEN "distance" LIKE 'null' THEN ' '
    WHEN "distance" LIKE '%km' THEN TRIM('km', "distance") 
    ELSE "distance"
    END AS "distance",
  CASE 
    WHEN "duration" LIKE 'null' THEN ' ' 
    WHEN "duration" LIKE '%mins' THEN TRIM('mins', "duration") 
    WHEN "duration" LIKE '%minute' THEN TRIM('minute', "duration")        
    WHEN "duration" LIKE '%minutes' THEN TRIM('minutes', "duration")       
    ELSE "duration"
    END AS "duration",
  CASE 
    WHEN "cancellation" IS NULL or "cancellation" LIKE 'null' THEN ''
    ELSE "cancellation"
    END AS "cancellation"
FROM runner_orders;

-- How many pizzas were ordered?
SELECT COUNT(*) AS pizza_order_count
FROM temp_customer_orders;

-- How many unique customer orders were made?
SELECT COUNT(DISTINCT "order_id") AS unique_order_count
FROM temp_customer_orders;

-- How many successful orders were delivered by each runner?
