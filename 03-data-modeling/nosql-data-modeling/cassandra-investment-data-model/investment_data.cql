-- Populate table accounts_by_user:
---------------------------
INSERT INTO accounts_by_user (username,account_number,cash_balance,name)
VALUES ('joe','joe001',10000.10,'Joseph');
INSERT INTO accounts_by_user (username,account_number,cash_balance,name)
VALUES ('joe','joe002',99999.99,'Joseph');
INSERT INTO accounts_by_user (username,account_number,cash_balance,name)
VALUES ('jen','jen001',1000000.00,'Jennifer');
INSERT INTO accounts_by_user (username,account_number,cash_balance,name)
VALUES ('jim','jim001',0.00,'James');


-- Populate table positions_by_account:
---------------------------
INSERT INTO positions_by_account (account,symbol,quantity)
VALUES ('joe001','AAPL',12.33);
INSERT INTO positions_by_account (account,symbol,quantity)
VALUES ('joe001','MSFT',12.50);
INSERT INTO positions_by_account (account,symbol,quantity)
VALUES ('joe001','GOOGL',30);
INSERT INTO positions_by_account (account,symbol,quantity)
VALUES ('joe002','TSLA',15);
INSERT INTO positions_by_account (account,symbol,quantity)
VALUES ('joe002','AMZN',1);
INSERT INTO positions_by_account (account,symbol,quantity)
VALUES ('jen001','MSFT',4.3333);
INSERT INTO positions_by_account (account,symbol,quantity)
VALUES ('jen001','GOOGL',4.9995);


-- Populate table trades_by_a_d:
-------------------------------------
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',2d0a8800-ec5d-11ea-8080-808080808080,'buy','GOOGL',10,1388.22,13882.20);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',c8186600-ed20-11ea-8080-808080808080,'buy','MSFT',12.50,180.00,2250.00);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',89f17400-edfe-11ea-8080-808080808080,'buy','AAPL',3.33,110.00,366.30);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',a2b99c80-f112-11ea-8080-808080808080,'buy','GOOGL',10,1400.00,14000.00);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',bd8c1100-f112-11ea-8080-808080808080,'buy','MSFT',5,180.50,902.50);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',1a62f680-f1fb-11ea-8080-808080808080,'buy','AAPL',10,112.50,1125.00);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',6d45b800-f2a6-11ea-8080-808080808080,'sell','AAPL',1,120.00,120.00);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',fe348780-f2d6-11ea-8080-808080808080,'sell','MSFT',5,200.00,1000.00);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',8b2f1d80-f377-11ea-8080-808080808080,'sell','GOOGL',10,1501.45,15014.50);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',808dc480-f6a6-11ea-8080-808080808080,'buy','GOOGL',10,1400.00,14000.00);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',6c81c880-f848-11ea-8080-808080808080,'buy','GOOGL',10,1350.00,13500.00);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',60813c80-f9e9-11ea-8080-808080808080,'buy','MSFT',10,198.00,1980.00);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',39f11a80-fc10-11ea-8080-808080808080,'sell','MSFT',10,220.00,2200.00);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe002',e24cf500-f440-11ea-8080-808080808080,'buy','TSLA',15,424.23,6363.45);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe002',3450c600-f9bf-11ea-8080-808080808080,'buy','AMZN',1,3128.99,3128.99);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('jen001',9ff83800-edf0-11ea-8080-808080808080,'buy','MSFT',4.3333,200.00,866.66);
INSERT INTO trades_by_a_d (account,trade_id,type,symbol,shares,price,amount)
VALUES ('jen001',eb720c80-ee17-11ea-8080-808080808080,'buy','GOOGL',4.9995,1459.82,7298.37);     


-- Populate table trades_by_a_td:
-------------------------------------
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',2d0a8800-ec5d-11ea-8080-808080808080,'buy','GOOGL',10,1388.22,13882.20);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',c8186600-ed20-11ea-8080-808080808080,'buy','MSFT',12.50,180.00,2250.00);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',89f17400-edfe-11ea-8080-808080808080,'buy','AAPL',3.33,110.00,366.30);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',a2b99c80-f112-11ea-8080-808080808080,'buy','GOOGL',10,1400.00,14000.00);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',bd8c1100-f112-11ea-8080-808080808080,'buy','MSFT',5,180.50,902.50);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',1a62f680-f1fb-11ea-8080-808080808080,'buy','AAPL',10,112.50,1125.00);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',6d45b800-f2a6-11ea-8080-808080808080,'sell','AAPL',1,120.00,120.00);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',fe348780-f2d6-11ea-8080-808080808080,'sell','MSFT',5,200.00,1000.00);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',8b2f1d80-f377-11ea-8080-808080808080,'sell','GOOGL',10,1501.45,15014.50);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',808dc480-f6a6-11ea-8080-808080808080,'buy','GOOGL',10,1400.00,14000.00);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',6c81c880-f848-11ea-8080-808080808080,'buy','GOOGL',10,1350.00,13500.00);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',60813c80-f9e9-11ea-8080-808080808080,'buy','MSFT',10,198.00,1980.00);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',39f11a80-fc10-11ea-8080-808080808080,'sell','MSFT',10,220.00,2200.00);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe002',e24cf500-f440-11ea-8080-808080808080,'buy','TSLA',15,424.23,6363.45);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe002',3450c600-f9bf-11ea-8080-808080808080,'buy','AMZN',1,3128.99,3128.99);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('jen001',9ff83800-edf0-11ea-8080-808080808080,'buy','MSFT',4.3333,200.00,866.66);
INSERT INTO trades_by_a_td (account,trade_id,type,symbol,shares,price,amount)
VALUES ('jen001',eb720c80-ee17-11ea-8080-808080808080,'buy','GOOGL',4.9995,1459.82,7298.37);


-- Populate table trades_by_a_std:
-------------------------------------
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',2d0a8800-ec5d-11ea-8080-808080808080,'buy','GOOGL',10,1388.22,13882.20);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',c8186600-ed20-11ea-8080-808080808080,'buy','MSFT',12.50,180.00,2250.00);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',89f17400-edfe-11ea-8080-808080808080,'buy','AAPL',3.33,110.00,366.30);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',a2b99c80-f112-11ea-8080-808080808080,'buy','GOOGL',10,1400.00,14000.00);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',bd8c1100-f112-11ea-8080-808080808080,'buy','MSFT',5,180.50,902.50);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',1a62f680-f1fb-11ea-8080-808080808080,'buy','AAPL',10,112.50,1125.00);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',6d45b800-f2a6-11ea-8080-808080808080,'sell','AAPL',1,120.00,120.00);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',fe348780-f2d6-11ea-8080-808080808080,'sell','MSFT',5,200.00,1000.00);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',8b2f1d80-f377-11ea-8080-808080808080,'sell','GOOGL',10,1501.45,15014.50);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',808dc480-f6a6-11ea-8080-808080808080,'buy','GOOGL',10,1400.00,14000.00);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',6c81c880-f848-11ea-8080-808080808080,'buy','GOOGL',10,1350.00,13500.00);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',60813c80-f9e9-11ea-8080-808080808080,'buy','MSFT',10,198.00,1980.00);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',39f11a80-fc10-11ea-8080-808080808080,'sell','MSFT',10,220.00,2200.00);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe002',e24cf500-f440-11ea-8080-808080808080,'buy','TSLA',15,424.23,6363.45);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe002',3450c600-f9bf-11ea-8080-808080808080,'buy','AMZN',1,3128.99,3128.99);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('jen001',9ff83800-edf0-11ea-8080-808080808080,'buy','MSFT',4.3333,200.00,866.66);
INSERT INTO trades_by_a_std (account,trade_id,type,symbol,shares,price,amount)
VALUES ('jen001',eb720c80-ee17-11ea-8080-808080808080,'buy','GOOGL',4.9995,1459.82,7298.37);


-- Populate table trades_by_a_sd:
-------------------------------------
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',2d0a8800-ec5d-11ea-8080-808080808080,'buy','GOOGL',10,1388.22,13882.20);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',c8186600-ed20-11ea-8080-808080808080,'buy','MSFT',12.50,180.00,2250.00);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',89f17400-edfe-11ea-8080-808080808080,'buy','AAPL',3.33,110.00,366.30);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',a2b99c80-f112-11ea-8080-808080808080,'buy','GOOGL',10,1400.00,14000.00);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',bd8c1100-f112-11ea-8080-808080808080,'buy','MSFT',5,180.50,902.50);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',1a62f680-f1fb-11ea-8080-808080808080,'buy','AAPL',10,112.50,1125.00);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',6d45b800-f2a6-11ea-8080-808080808080,'sell','AAPL',1,120.00,120.00);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',fe348780-f2d6-11ea-8080-808080808080,'sell','MSFT',5,200.00,1000.00);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',8b2f1d80-f377-11ea-8080-808080808080,'sell','GOOGL',10,1501.45,15014.50);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',808dc480-f6a6-11ea-8080-808080808080,'buy','GOOGL',10,1400.00,14000.00);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',6c81c880-f848-11ea-8080-808080808080,'buy','GOOGL',10,1350.00,13500.00);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',60813c80-f9e9-11ea-8080-808080808080,'buy','MSFT',10,198.00,1980.00);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe001',39f11a80-fc10-11ea-8080-808080808080,'sell','MSFT',10,220.00,2200.00);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe002',e24cf500-f440-11ea-8080-808080808080,'buy','TSLA',15,424.23,6363.45);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('joe002',3450c600-f9bf-11ea-8080-808080808080,'buy','AMZN',1,3128.99,3128.99);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('jen001',9ff83800-edf0-11ea-8080-808080808080,'buy','MSFT',4.3333,200.00,866.66);
INSERT INTO trades_by_a_sd (account,trade_id,type,symbol,shares,price,amount)
VALUES ('jen001',eb720c80-ee17-11ea-8080-808080808080,'buy','GOOGL',4.9995,1459.82,7298.37);