# Sales Datamodel

## Create dimension tables

To begin, we will create our three dimension tables: product, customer, and store location.

```sql
CREATE TABLE product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL
);

CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL
);

CREATE TABLE store_location (
    location_id INT PRIMARY KEY,
    location_name VARCHAR(255) NOT NULL
);
```

## Create fact table

Next, we will create our fact table, sales, and specify the foreign keys for the dimension tables.

```sql
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    customer_id INT,
    location_id INT,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (location_id) REFERENCES store_location(location_id)
);
```

## Data Ingestion

Now that our schema is set up, we can start inserting data into our tables.

```sql
INSERT INTO product (product_id, product_name)
VALUES (100, 'T-Shirt'), (101, 'Jeans'), (102, 'Jacket');

INSERT INTO customer (customer_id, customer_name)
VALUES (1, 'John Doe'), (2, 'Jane Smith'), (3, 'Bob Johnson');

INSERT INTO store_location (location_id, location_name)
VALUES (1, 'New York'), (2, 'Los Angeles'), (3, 'Chicago');

INSERT INTO sales (sale_id, product_id, customer_id, location_id, price)
VALUES (1, 100, 1, 1, 10.99), (2, 101, 2, 2, 5.99), (3, 102, 3, 3, 15.99);
```

## Query

With the data in place, we can now run queries to analyze the data in various ways. For example, we can find the total sales for a specific product:

```sql
SELECT product_name, SUM(price) as total_sales
FROM sales
JOIN product ON sales.product_id = product.product_id
WHERE product_name = 'Jeans'
GROUP BY product_name;
```

This query will return the total sales for the product “Jeans”

| product_name | total_sales|
| ------------ | ---------- |
| Jeans        | 5.99       |

In this example, we used a join between the sales table and the product dimension table to retrieve the product name and then used the WHERE clause to filter by the product name and finally used the GROUP BY clause to group by product_name and sum the price.