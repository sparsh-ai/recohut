# Create a Data Model for Online Shopping Carts

## Conceptual Data Model

A conceptual data model is designed with the goal of understanding data in a particular domain. In this example, the model is captured using an Entity-Relationship Diagram (ERD) that documents entity types, relationship types, attribute types, and cardinality and key constraints.

![](https://user-images.githubusercontent.com/62965911/214248084-c55a2e87-7b08-437c-bee7-8beb025fa702.png)

The conceptual data model for shopping cart data features users, items and shopping carts. A user has a unique id and may have other attributes like email. An item has a unique id, name, description and price. A shopping cart is uniquely identified by an id and can be either an active shopping cart or a saved shopping cart. Other shopping cart attribute types include a name and subtotal. The latter is a derived attribute type whose value is computed based on prices and quantities of all items in a cart. In general, a derived attribute value can be stored in a database or dynamically computed by an application. While a user can create many shopping carts, each cart must belong to exactly one user. At any time, a user can have at most one active shopping cart and many saved carts. Finally, a shopping cart can have many items and a catalog item can be added to many carts. An item entry in a cart is further described by a timestamp and desired quantity.

## Application workflow

An application workflow is designed with the goal of understanding data access patterns for a data-driven application. Its visual representation consists of application tasks, dependencies among tasks, and data access patterns. Ideally, each data access pattern should specify what attributes to search for, search on, order by, or do aggregation on.

![](https://user-images.githubusercontent.com/62965911/214248072-2d8c7da1-d000-4042-a778-cc7d28fbb2e4.png)

The application workflow has six tasks, of which three tasks are possible entry-point tasks. Based on this workflow, an application should be able to:

- show an active shopping cart of a user, which requires Q1;
- search for items by id or name, which requires Q2 and Q3, respectively;
- show all shopping carts of a user, which requires Q4;
- display items in a shopping cart, which requires Q5;
- add an item into an active shopping cart, which requires U1;
- designate a cart to be an active cart, which requires U2.

All in all, there are seven data access patterns for a database to support. While Q1, Q2, Q3, Q4 and Q5 are needed to query data, U1 and U2 are intended to update data. In this example, updates are especially interesting because they require updating multiple rows and may involve race conditions.

## Logical Data model

A logical data model results from a conceptual data model by organizing data into Cassandra-specific data structures based on data access patterns identified by an application workflow. Logical data models can be conveniently captured and visualized using Chebotko Diagrams that can feature tables, materialized views, indexes and so forth.

![](https://user-images.githubusercontent.com/62965911/214248090-d10a31b1-3c1c-4a60-942d-43d7bdbf53f6.png)

The logical data model for shopping cart data is represented by the shown Chebotko Diagram. Table active_carts_by_user is designed to support data access pattern Q1. It has single-row partitions since each user can only have one active shopping cart at any time. Table items_by_id is designed to support data access pattern Q2. Similarly, it is a table with single-row partitions and a simple primary key. The remaining three tables have multi-row partitions and compound primary keys that consist of both partition and clustering keys. Table items_by_name enables data access pattern Q3. To retrieve all items with a given name, at most one partition needs to be accessed. Next, table all_carts_by_user is designed to support data access pattern Q4. It features one multi-row partition per user, where each row represents a different shopping cart. Rows within each partition are ordered using cart names and cart ids. Column user_email is a static column as it describes a user who is uniquely identified by the table partition key. Again, only one partition in this table needs to be accessed to answer Q4. Finally, table items_by_cart covers data access pattern Q5. In this table, each partition corresponds to a shopping cart and each row represents an item. Column subtotal is a static column and is a descriptor of a shopping cart. Once again, this very efficient design requires retrieving only one partition to satisfy Q5.

Note that, in this example, updates U1 and U2 do not directly affect the table design process. The diagram simply documents which tables need to be accessed to satisfy these data access patterns.

## Physical Data Model
A physical data model is directly derived from a logical data model by analyzing and optimizing for performance. The most common type of analysis is identifying potentially large partitions. Some common optimization techniques include splitting and merging partitions, data indexing, data aggregation and concurrent data access optimizations.

![](https://user-images.githubusercontent.com/62965911/214248106-436b6daf-a395-4ee8-91de-b51afeccf75a.png)

The physical data model for shopping cart data is visualized using the Chebotko Diagram. This time, all table columns have associated data types. It should be evident that none of the tables can have very large partitions. Otherwise, some reasonable limits can be enforced by an application, such as at most 100 shopping carts per user, at most 1000 items per cart and at most 10000 items with the same name. The first optimization that this physical data model implements is the elimination of table active_carts_by_user completely and renaming of table all_carts_by_user to simply carts_by_user. The huge advantage of the new design is that U2 becomes much simpler and more efficient to implement because this data access pattern no longer needs to update rows in two tables. In fact, U2 only needs to update two rows in the same partition of table carts_by_user, which can be done efficiently using a batch and a lightweight transaction (see the Skill Building section for a concrete example). The minor disadvantage is that Q1 is not fully supported by table carts_by_user. An application has to retrieve all carts that belong to a user as in Q4 and further scan the result to find an active cart. Assuming that an average user only has a few carts, this should not be a problem at all. Alternatively, it is also possible to create a secondary index on column cart_is_active to fully support Q1 in Cassandra. But using an index to find one row in a partition with only a few rows is likely to be less efficient than simply scanning those few rows (and avoiding index maintenance costs, too). The second and last optimization is the replacement of table items_by_name with a materialized view items_by_name. This is done for convenience rather than efficiency. Our final blueprint is ready to be instantiated in Cassandra.

## Hands-on

In this lab, you will:

- Create tables for a shopping cart data use case
- Populate tables with sample shopping cart data
- Design and execute CQL queries over shopping cart data

### Create Keyspace

```sql
CREATE KEYSPACE shopping_cart_data
WITH replication = {
  'class': 'SimpleStrategy', 
  'replication_factor': 1 }; 

USE shopping_cart_data;
```

### Create Tables

```sql
CREATE TABLE IF NOT EXISTS carts_by_user (
  user_id TEXT,
  cart_name TEXT,
  cart_id UUID,
  cart_is_active BOOLEAN,
  user_email TEXT STATIC,
  PRIMARY KEY ((user_id),cart_name,cart_id)
);

CREATE TABLE IF NOT EXISTS items_by_id (
  id TEXT,
  name TEXT,
  description TEXT,
  price DECIMAL,
  PRIMARY KEY ((id))
);

CREATE MATERIALIZED VIEW IF NOT EXISTS items_by_name 
  AS 
    SELECT * FROM items_by_id
    WHERE name IS NOT NULL 
      AND id IS NOT NULL
  PRIMARY KEY ((name), id);

CREATE TABLE IF NOT EXISTS items_by_cart (
  cart_id UUID,
  timestamp TIMESTAMP,
  item_id TEXT,
  item_name TEXT,
  item_description TEXT,
  item_price DECIMAL,
  quantity INT,
  cart_subtotal DECIMAL STATIC,
  PRIMARY KEY ((cart_id),timestamp,item_id)
) WITH CLUSTERING ORDER BY (timestamp DESC, item_id ASC);

DESCRIBE TABLES;
```

### Populate tables

```sql
SOURCE 'shopping_cart_data.cql'
```

Retrieve some rows from tables:

```sql
SELECT user_id, cart_name, 
       cart_id, cart_is_active
FROM carts_by_user;        
SELECT * FROM items_by_id;
SELECT * FROM items_by_name;                    
SELECT cart_id, timestamp, item_id 
FROM items_by_cart; 
SELECT cart_id, item_id, item_price, 
       quantity, cart_subtotal 
FROM items_by_cart; 
```

### Design query Q1

Find id and name of an active shopping cart that belongs to user jen:

<details>
    <summary>Show me the Answer! </summary>
    -- Retrieve all carts for jen
    -- and scan the result set
    -- within an application
    -- to find an active cart.
    SELECT user_id, cart_name, 
          cart_id, cart_is_active
    FROM carts_by_user
    WHERE user_id = 'jen'; 
</details>
<br/>

<details>
    <summary>Show me the Answer! </summary>
    -- Retrieve all carts for jen
    -- and scan the result set
    -- within Cassandra
    -- to find an active cart.
    -- Note that this is a rare case of
    -- scanning within a small partition
    -- when ALLOW FILTERING 
    -- might be acceptable. 
    SELECT user_id, cart_name, 
          cart_id, cart_is_active
    FROM carts_by_user
    WHERE user_id = 'jen'
      AND cart_is_active = true 
    ALLOW FILTERING;
</details>
<br/>

### Design query Q2

Find ids and names of all shopping carts that belong to user jen; order by cart name (asc):

<details>
    <summary>Show me the Answer! </summary>
    SELECT user_id, cart_name, 
          cart_id, cart_is_active
    FROM carts_by_user
    WHERE user_id = 'jen';
</details>
<br/>

### Design query Q3

Save an active shopping cart with name My Birthday and id 4e66baf8-f3ad-4c3b-9151-52be4574f2de, and designate a different cart with name Gifts for Mom and id 19925cc1-4f8b-4a44-b893-2a49a8434fc8 to be a new active shopping cart for user jen:

<details>
    <summary>Show me the Answer! </summary>
    BEGIN BATCH
      UPDATE carts_by_user 
      SET cart_is_active = false
      WHERE user_id = 'jen'
        AND cart_name = 'My Birthday'
        AND cart_id = 4e66baf8-f3ad-4c3b-9151-52be4574f2de
      IF cart_is_active = true;
      UPDATE carts_by_user 
      SET cart_is_active = true
      WHERE user_id = 'jen'
        AND cart_name = 'Gifts for Mom'
        AND cart_id = 19925cc1-4f8b-4a44-b893-2a49a8434fc8;
    APPLY BATCH;

    SELECT user_id, cart_name, 
          cart_id, cart_is_active
    FROM carts_by_user
    WHERE user_id = 'jen';
</details>
<br/>

### Design query Q4

Find all information about an item with id Box2:

<details>
    <summary>Show me the Answer! </summary>
    SELECT * 
    FROM items_by_id
    WHERE id = 'Box2';
</details>
<br/>

### Design query Q5

Find all information about items with name Chocolate Cake:

<details>
    <summary>Show me the Answer! </summary>
    SELECT * 
    FROM items_by_name
    WHERE name = 'Chocolate Cake';
</details>
<br/>

### Design query Q6

Find all items and their subtotal for a cart with id 19925cc1-4f8b-4a44-b893-2a49a8434fc8; order items by timestamp (desc):

<details>
    <summary>Show me the Answer! </summary>
    SELECT timestamp, item_id, item_price, 
          quantity, cart_subtotal 
    FROM items_by_cart
    WHERE cart_id = 19925cc1-4f8b-4a44-b893-2a49a8434fc8; 
</details>
<br/>

### Design query Q7

Add item Box2 into active cart 19925cc1-4f8b-4a44-b893-2a49a8434fc8 and update the cart subtotal to 111.50:

<details>
    <summary>Show me the Answer! </summary>
    BEGIN BATCH
      INSERT INTO items_by_cart (
        cart_id,
        timestamp,
        item_id,
        item_name,
        item_description,
        item_price,
        quantity)
      VALUES (
        19925cc1-4f8b-4a44-b893-2a49a8434fc8,
        TOTIMESTAMP(NOW()),
        'Box2',
        'Chocolates',
        '25 gourmet chocolates from our collection',
        60.00,
        1);
      UPDATE items_by_cart 
      SET cart_subtotal = 111.50
      WHERE cart_id = 19925cc1-4f8b-4a44-b893-2a49a8434fc8
      IF cart_subtotal = 51.50;
    APPLY BATCH;

    SELECT timestamp, item_id, item_price, 
          quantity, cart_subtotal 
    FROM items_by_cart
    WHERE cart_id = 19925cc1-4f8b-4a44-b893-2a49a8434fc8; 
</details>
<br/>