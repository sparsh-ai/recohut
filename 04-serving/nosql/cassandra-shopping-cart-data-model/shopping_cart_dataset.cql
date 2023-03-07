-- Populate table carts_by_user:
------------------------------------------
INSERT INTO carts_by_user (user_id,cart_name,cart_id,cart_is_active,user_email)
VALUES ('jen','Gifts for Mom',19925cc1-4f8b-4a44-b893-2a49a8434fc8,false,'jen@datastax.com');
INSERT INTO carts_by_user (user_id,cart_name,cart_id,cart_is_active,user_email)
VALUES ('jen','Gifts for Dad',5453bd52-8366-4776-aa7c-d8d827176493,false,'jen@datastax.com');
INSERT INTO carts_by_user (user_id,cart_name,cart_id,cart_is_active,user_email)
VALUES ('jen','My Birthday',4e66baf8-f3ad-4c3b-9151-52be4574f2de,true,'jen@datastax.com');
INSERT INTO carts_by_user (user_id,cart_name,cart_id,cart_is_active,user_email)
VALUES ('joe','Things Joe Likes',2ff01a3f-0b28-4894-bb3e-989f03412b06,true,'joe@datastax.com');
INSERT INTO carts_by_user (user_id,cart_name,cart_id,cart_is_active,user_email)
VALUES ('jim','My Shopping List',3ff4c697-ae75-449e-ab20-aac392f0bbf0,true,'jim@datastax.com');


-- Populate table items_by_id:
------------------------------------------
INSERT INTO items_by_id (id,name,description,price)
VALUES('Bouquet1','Red Roses','Red roses and white Calla lilies',26.50);
INSERT INTO items_by_id (id,name,description,price)
VALUES('Bouquet2','Red Roses','Two dozen red roses',22.50);
INSERT INTO items_by_id (id,name,description,price)
VALUES('Bouquet3','Pink Roses','Pink roses, carnations and daisy poms',27.50);
INSERT INTO items_by_id (id,name,description,price)
VALUES('Strawberries1','Strawberries','Strawberries dipped in milk chocolate',12.50);
INSERT INTO items_by_id (id,name,description,price)
VALUES('Strawberries2','Strawberries','Strawberries dipped in dark chocolate',12.50);
INSERT INTO items_by_id (id,name,description,price)
VALUES('Box1','Truffles','16 milk, dark and white chocolate truffles',40.00);
INSERT INTO items_by_id (id,name,description,price)
VALUES('Box2','Chocolates','25 gourmet chocolates from our collection',60.00);
INSERT INTO items_by_id (id,name,description,price)
VALUES('Basket1','Wine','Cheese and wine basket',100.00);
INSERT INTO items_by_id (id,name,description,price)
VALUES('Basket2','Cookies','24 buttercream frosted cookies',24.00);
INSERT INTO items_by_id (id,name,description,price)
VALUES('Cake1','Chocolate Cake','Buttercream frosted chocolate cake',80.00);
INSERT INTO items_by_id (id,name,description,price)
VALUES('Cake2','Chocolate Cake','Chocolate mousse cake',80.00);
INSERT INTO items_by_id (id,name,description,price)
VALUES('Cake3','Cheesecake','NY original cheesecake',75.00);


-- Populate table items_by_name:
------------------------------------------
INSERT INTO items_by_name (id,name,description,price)
VALUES('Bouquet1','Red Roses','Red roses and white Calla lilies',26.50);
INSERT INTO items_by_name (id,name,description,price)
VALUES('Bouquet2','Red Roses','Two dozen red roses',22.50);
INSERT INTO items_by_name (id,name,description,price)
VALUES('Bouquet3','Pink Roses','Pink roses, carnations and daisy poms',27.50);
INSERT INTO items_by_name (id,name,description,price)
VALUES('Strawberries1','Strawberries','Strawberries dipped in milk chocolate',12.50);
INSERT INTO items_by_name (id,name,description,price)
VALUES('Strawberries2','Strawberries','Strawberries dipped in dark chocolate',12.50);
INSERT INTO items_by_name (id,name,description,price)
VALUES('Box1','Truffles','16 milk, dark and white chocolate truffles',40.00);
INSERT INTO items_by_name (id,name,description,price)
VALUES('Box2','Chocolates','25 gourmet chocolates from our collection',60.00);
INSERT INTO items_by_name (id,name,description,price)
VALUES('Basket1','Wine','Cheese and wine basket',100.00);
INSERT INTO items_by_name (id,name,description,price)
VALUES('Basket2','Cookies','24 buttercream frosted cookies',24.00);
INSERT INTO items_by_name (id,name,description,price)
VALUES('Cake1','Chocolate Cake','Buttercream frosted chocolate cake',80.00);
INSERT INTO items_by_name (id,name,description,price)
VALUES('Cake2','Chocolate Cake','Chocolate mousse cake',80.00);
INSERT INTO items_by_name (id,name,description,price)
VALUES('Cake3','Cheesecake','NY original cheesecake',75.00);


-- Populate table items_by_cart:
------------------------------------------
INSERT INTO items_by_cart (cart_id,timestamp,item_id,item_name,item_description,item_price,quantity,cart_subtotal)
VALUES (19925cc1-4f8b-4a44-b893-2a49a8434fc8,'2020-10-21 11:45:03','Bouquet1','Red Roses','Red roses and white Calla lilies',26.50,1,51.50);
INSERT INTO items_by_cart (cart_id,timestamp,item_id,item_name,item_description,item_price,quantity,cart_subtotal)
VALUES (19925cc1-4f8b-4a44-b893-2a49a8434fc8,'2020-10-21 11:48:43','Strawberries1','Strawberries','Strawberries dipped in milk chocolate',12.50,2,51.50);

INSERT INTO items_by_cart (cart_id,timestamp,item_id,item_name,item_description,item_price,quantity,cart_subtotal)
VALUES (5453bd52-8366-4776-aa7c-d8d827176493,'2020-10-21 13:00:16','Cake3','Cheesecake','NY original cheesecake',75.00,1,87.50);
INSERT INTO items_by_cart (cart_id,timestamp,item_id,item_name,item_description,item_price,quantity,cart_subtotal)
VALUES (5453bd52-8366-4776-aa7c-d8d827176493,'2020-10-21 13:15:51','Strawberries2','Strawberries','Strawberries dipped in dark chocolate',12.50,1,87.50);

INSERT INTO items_by_cart (cart_id,timestamp,item_id,item_name,item_description,item_price,quantity,cart_subtotal)
VALUES (4e66baf8-f3ad-4c3b-9151-52be4574f2de,TOTIMESTAMP(NOW()),'Cake1','Chocolate Cake','Buttercream frosted chocolate cake',80.00,1,80.00);

INSERT INTO items_by_cart (cart_id,timestamp,item_id,item_name,item_description,item_price,quantity,cart_subtotal)
VALUES (2ff01a3f-0b28-4894-bb3e-989f03412b06,TOTIMESTAMP(NOW()),'Basket2','Cookies','24 buttercream frosted cookies',24.00,3,112.00);
INSERT INTO items_by_cart (cart_id,timestamp,item_id,item_name,item_description,item_price,quantity,cart_subtotal)
VALUES (2ff01a3f-0b28-4894-bb3e-989f03412b06,TOTIMESTAMP(NOW()),'Box1','Truffles','16 milk, dark and white chocolate truffles',40.00,1,112.00);

INSERT INTO items_by_cart (cart_id,timestamp,item_id,item_name,item_description,item_price,quantity,cart_subtotal)
VALUES (3ff4c697-ae75-449e-ab20-aac392f0bbf0,TOTIMESTAMP(NOW()),'Strawberries2','Strawberries','Strawberries dipped in dark chocolate',12.50,2,25.00);