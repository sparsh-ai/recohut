-- Populate table networks:
---------------------------
INSERT INTO networks 
(bucket,name,description,region,num_sensors)
VALUES ('all','forest-net',
        'forest fire detection network',
        'south',3);
INSERT INTO networks 
(bucket,name,description,region,num_sensors)
VALUES ('all','volcano-net',
        'volcano monitoring network',
        'north',2);   


-- Populate table sensors_by_network:
-------------------------------------
INSERT INTO sensors_by_network 
(network,sensor,latitude,longitude,characteristics)
VALUES ('forest-net','s1001',30.526503,-95.582815,
       {'accuracy':'medium','sensitivity':'high'});
INSERT INTO sensors_by_network 
(network,sensor,latitude,longitude,characteristics)
VALUES ('forest-net','s1002',30.518650,-95.583585,
       {'accuracy':'medium','sensitivity':'high'});     
INSERT INTO sensors_by_network 
(network,sensor,latitude,longitude,characteristics)
VALUES ('forest-net','s1003',30.515056,-95.556225,
       {'accuracy':'medium','sensitivity':'high'});     
INSERT INTO sensors_by_network 
(network,sensor,latitude,longitude,characteristics)
VALUES ('volcano-net','s2001',44.460321,-110.828151,
       {'accuracy':'high','sensitivity':'medium'});    
INSERT INTO sensors_by_network 
(network,sensor,latitude,longitude,characteristics)
VALUES ('volcano-net','s2002',44.463195,-110.830124,
       {'accuracy':'high','sensitivity':'medium'});      


-- Populate table temperatures_by_network:
------------------------------------------
INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-06-28','2020-07-04 00:00:00','s1001',79.5,30.526503,-95.582815);
INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-06-28','2020-07-04 12:00:00','s1001',97.5,30.526503,-95.582815);

INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-06-28','2020-07-04 00:00:00','s1002',81,30.518650,-95.583585);
INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-06-28','2020-07-04 12:00:00','s1002',100,30.518650,-95.583585);

INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-06-28','2020-07-04 00:00:00','s1003',80.5,30.515056,-95.556225);
INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-06-28','2020-07-04 12:00:00','s1003',98.5,30.515056,-95.556225);

INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-05 00:00:00','s1001',80.5,30.526503,-95.582815);
INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-05 12:00:00','s1001',98.5,30.526503,-95.582815);

INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-05 00:00:00','s1002',82,30.518650,-95.583585);
INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-05 12:00:00','s1002',99.5,30.518650,-95.583585);

INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-05 00:00:00','s1003',82.5,30.515056,-95.556225);
INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-05 12:00:00','s1003',101.5,30.515056,-95.556225);

INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-06 00:00:00','s1001',90.5,30.526503,-95.582815);
INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-06 12:00:00','s1001',106.5,30.526503,-95.582815);

INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-06 00:00:00','s1002',90,30.518650,-95.583585);
INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-06 12:00:00','s1002',109,30.518650,-95.583585);

INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-06 00:00:00','s1003',90.5,30.515056,-95.556225);
INSERT INTO temperatures_by_network 
(network,week,date_hour,sensor,avg_temperature,latitude,longitude) 
VALUES ('forest-net','2020-07-05','2020-07-06 12:00:00','s1003',1372,30.515056,-95.556225);


-- Populate table temperatures_by_sensor:
-----------------------------------------
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-04','2020-07-04 00:00:01',80);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-04','2020-07-04 00:59:59',79);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-04','2020-07-04 12:00:01',97);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-04','2020-07-04 12:59:59',98);

INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-04','2020-07-04 00:00:01',82);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-04','2020-07-04 00:59:59',80);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-04','2020-07-04 12:00:01',100);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-04','2020-07-04 12:59:59',100);

INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-04','2020-07-04 00:00:01',81);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-04','2020-07-04 00:59:59',80);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-04','2020-07-04 12:00:01',99);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-04','2020-07-04 12:59:59',98);


INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-05','2020-07-05 00:00:01',81);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-05','2020-07-05 00:59:59',80);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-05','2020-07-05 12:00:01',98);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-05','2020-07-05 12:59:59',99);

INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-05','2020-07-05 00:00:01',82);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-05','2020-07-05 00:59:59',82);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-05','2020-07-05 12:00:01',100);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-05','2020-07-05 12:59:59',99);

INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-05','2020-07-05 00:00:01',83);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-05','2020-07-05 00:59:59',82);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-05','2020-07-05 12:00:01',101);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-05','2020-07-05 12:59:59',102);


INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-06','2020-07-06 00:00:01',90);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-06','2020-07-06 00:59:59',90);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-06','2020-07-06 12:00:01',106);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1001','2020-07-06','2020-07-06 12:59:59',107);

INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-06','2020-07-06 00:00:01',90);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-06','2020-07-06 00:59:59',90);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-06','2020-07-06 12:00:01',108);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1002','2020-07-06','2020-07-06 12:59:59',110);

INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-06','2020-07-06 00:00:01',90);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-06','2020-07-06 00:59:59',90);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-06','2020-07-06 12:00:01',1315);
INSERT INTO temperatures_by_sensor 
(sensor,date,timestamp,value)
VALUES ('s1003','2020-07-06','2020-07-06 12:59:59',1429);



