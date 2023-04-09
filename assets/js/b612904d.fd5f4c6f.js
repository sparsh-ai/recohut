"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[34869],{3905:(e,a,t)=>{t.d(a,{Zo:()=>c,kt:()=>m});var n=t(67294);function r(e,a,t){return a in e?Object.defineProperty(e,a,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[a]=t,e}function s(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,n)}return t}function o(e){for(var a=1;a<arguments.length;a++){var t=null!=arguments[a]?arguments[a]:{};a%2?s(Object(t),!0).forEach((function(a){r(e,a,t[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):s(Object(t)).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(t,a))}))}return e}function i(e,a){if(null==e)return{};var t,n,r=function(e,a){if(null==e)return{};var t,n,r={},s=Object.keys(e);for(n=0;n<s.length;n++)t=s[n],a.indexOf(t)>=0||(r[t]=e[t]);return r}(e,a);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(n=0;n<s.length;n++)t=s[n],a.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(r[t]=e[t])}return r}var l=n.createContext({}),d=function(e){var a=n.useContext(l),t=a;return e&&(t="function"==typeof e?e(a):o(o({},a),e)),t},c=function(e){var a=d(e.components);return n.createElement(l.Provider,{value:a},e.children)},u={inlineCode:"code",wrapper:function(e){var a=e.children;return n.createElement(n.Fragment,{},a)}},p=n.forwardRef((function(e,a){var t=e.components,r=e.mdxType,s=e.originalType,l=e.parentName,c=i(e,["components","mdxType","originalType","parentName"]),p=d(t),m=r,y=p["".concat(l,".").concat(m)]||p[m]||u[m]||s;return t?n.createElement(y,o(o({ref:a},c),{},{components:t})):n.createElement(y,o({ref:a},c))}));function m(e,a){var t=arguments,r=a&&a.mdxType;if("string"==typeof e||r){var s=t.length,o=new Array(s);o[0]=p;var i={};for(var l in a)hasOwnProperty.call(a,l)&&(i[l]=a[l]);i.originalType=e,i.mdxType="string"==typeof e?e:r,o[1]=i;for(var d=2;d<s;d++)o[d]=t[d];return n.createElement.apply(null,o)}return n.createElement.apply(null,t)}p.displayName="MDXCreateElement"},96685:(e,a,t)=>{t.r(a),t.d(a,{assets:()=>l,contentTitle:()=>o,default:()=>u,frontMatter:()=>s,metadata:()=>i,toc:()=>d});var n=t(87462),r=(t(67294),t(3905));const s={},o="Create a Data Model for Investment Accounts or Portfolios",i={unversionedId:"data-modeling/lab-cassandra-investment-data-model/README",id:"data-modeling/lab-cassandra-investment-data-model/README",title:"Create a Data Model for Investment Accounts or Portfolios",description:"Conceptual Data Model",source:"@site/docs/04-data-modeling/lab-cassandra-investment-data-model/README.md",sourceDirName:"04-data-modeling/lab-cassandra-investment-data-model",slug:"/data-modeling/lab-cassandra-investment-data-model/",permalink:"/docs/data-modeling/lab-cassandra-investment-data-model/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Hotel Reservations Data Modeling with Cassandra",permalink:"/docs/data-modeling/lab-cassandra-hotel-reservations/"},next:{title:"Create a Data Model for Temperature Monitoring Sensor Networks",permalink:"/docs/data-modeling/lab-cassandra-sensor-data-model/"}},l={},d=[{value:"Conceptual Data Model",id:"conceptual-data-model",level:2},{value:"Application workflow",id:"application-workflow",level:2},{value:"Logical Data model",id:"logical-data-model",level:2},{value:"Physical Data Model",id:"physical-data-model",level:2},{value:"Hands-on",id:"hands-on",level:2},{value:"Create Keyspace",id:"create-keyspace",level:3},{value:"Create Tables",id:"create-tables",level:3},{value:"Populate tables",id:"populate-tables",level:3},{value:"Design query Q1",id:"design-query-q1",level:3},{value:"Design query Q2",id:"design-query-q2",level:3},{value:"Design query Q3",id:"design-query-q3",level:3},{value:"Design query Q4",id:"design-query-q4",level:3},{value:"Design query Q5",id:"design-query-q5",level:3},{value:"Design query Q6",id:"design-query-q6",level:3},{value:"Design query Q7",id:"design-query-q7",level:3}],c={toc:d};function u(e){let{components:a,...t}=e;return(0,r.kt)("wrapper",(0,n.Z)({},c,t,{components:a,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"create-a-data-model-for-investment-accounts-or-portfolios"},"Create a Data Model for Investment Accounts or Portfolios"),(0,r.kt)("h2",{id:"conceptual-data-model"},"Conceptual Data Model"),(0,r.kt)("p",null,"A conceptual data model is designed with the goal of understanding data in a particular domain. In this example, the model is captured using an Entity-Relationship Diagram (ERD) that documents entity types, relationship types, attribute types, and cardinality and key constraints."),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214248197-18c2b3f1-60e3-4852-aeb9-8115af72718b.png",alt:null})),(0,r.kt)("p",null,"The conceptual data model for investment portfolio data features users, accounts, trades and instruments. A user has a unique username and may have other attributes like name. An account has a unique number, cash balance, investment value and total value. A trade is uniquely identified by an id and can be either a buy transaction or a sell transaction. Other trade attribute types include a trade date, number of shares, price per share and total amount. An instrument has a unique symbol and a current quote. Stocks, mutual funds and exchange-traded funds (ETFs) are all types of instruments supported in this example. While a user can open many accounts, each account must belong to exactly one user. Similarly, an account can place many trades and an instrument can participate in many trades, but a trade is always associated with only one account and one instrument. Finally, an account may have many positions and an instrument can be owned by many accounts. Each position in a particular account is described by an instrument symbol, quantity and current value."),(0,r.kt)("p",null,"Note that the diagram has four derived attribute types, namely investment value, total value, current value and amount. Derived attribute values are computed based on other attribute values. For example, a current position value is computed by multiplying a quantity by a quote for a particular instrument. An account investment value is the sum of all current position values. And an account total value is the sum of a cash balance and an investment value. Last but not least, a trade amount is the product of a price and a number of shares. In general, while some derived attribute values can be stored in a database, others can be dynamically computed by an application."),(0,r.kt)("h2",{id:"application-workflow"},"Application workflow"),(0,r.kt)("p",null,"An application workflow is designed with the goal of understanding data access patterns for a data-driven application. Its visual representation consists of application tasks, dependencies among tasks, and data access patterns. Ideally, each data access pattern should specify what attributes to search for, search on, order by, or do aggregation on."),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214248186-5e276326-ee97-4f08-af42-f78b8bfafbdd.png",alt:null})),(0,r.kt)("p",null,"The application workflow has an entry-point task that shows all investment accounts of a user. This task requires data access pattern Q1 as shown on the diagram. Next, an application can either display current positions in a selected account, which requires data access pattern Q2, or display information about trade history for a selected account, which requires data access pattern Q3. Furthermore, Q3 is broken down into five more manageable data access patterns Q3.1, Q3.2, Q3.3, Q3.4 and Q3.5. All in all, there are seven data access patterns for a database to support."),(0,r.kt)("h2",{id:"logical-data-model"},"Logical Data model"),(0,r.kt)("p",null,"A logical data model results from a conceptual data model by organizing data into Cassandra-specific data structures based on data access patterns identified by an application workflow. Logical data models can be conveniently captured and visualized using Chebotko Diagrams that can feature tables, materialized views, indexes and so forth."),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214248206-3f27fa73-b0b8-44e0-8323-f58024640e8d.png",alt:null})),(0,r.kt)("p",null,"The logical data model for investment portfolio data is represented by the shown Chebotko Diagram. There are six tables that are designed to support seven data access patterns. All the tables have compound primary keys, consisting of partition and clustering keys, and therefore can store multiple rows per partition. Table accounts_by_user is designed to have one partition per user, where each row in a partition corresponds to a user account. Column name is a static column as it describes a user who is uniquely identified by the table partition key. Table positions_by_account is designed to efficiently support Q2. All positions in a particular account can be retrieved from one partition with multiple rows. Next, tables trades_by_a_d, trades_by_a_td, trades_by_a_std and trades_by_a_sd store the same data about trade transactions, but they organize rows differently and support different data access patterns. All four tables have the same partition keys, which represent account numbers, and are designed to retrieve and present trades in the descending order of their dates. Table trades_by_a_d supports two data access patterns Q3.1 and Q3.2, which are used to retrieve either all trades for a given account or only trades in a particular date range for a given account. Table trades_by_a_td also enables restricting a transaction type as in Q3.3. Furthermore, table trades_by_a_std supports querying using both an instrument symbol and transaction type as in Q3.4. Finally, table trades_by_a_sd supports Q3.5, which retrieves trades based on an account, instrument symbol and date range."),(0,r.kt)("p",null,"Note that not all information from the conceptual data model got transferred to the logical data model. Out of the four derived attribute types, only a trade amount will be stored in a database. Once a trade is completed, its amount is immutable and it makes sense to store it. In contrast, current position values, account investment values and account total values change frequently and it is better to compute them dynamically in an application. Also, the logical data model does not contain a catalog of all available instruments and their current quotes because this information is readily available from third-party systems."),(0,r.kt)("h2",{id:"physical-data-model"},"Physical Data Model"),(0,r.kt)("p",null,"A physical data model is directly derived from a logical data model by analyzing and optimizing for performance. The most common type of analysis is identifying potentially large partitions. Some common optimization techniques include splitting and merging partitions, data indexing, data aggregation and concurrent data access optimizations."),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214248217-76707e5c-bbbe-40f1-a5ae-a93b93f2cb4d.png",alt:null})),(0,r.kt)("p",null,"The physical data model for investment portfolio data is visualized using the Chebotko Diagram. This time, all table columns have associated data types. Assuming the use case does not cover robo-advisors and algorithmic trading, it should be evident that none of the tables will have very large partitions. Any given user will at most have a few accounts. An account will normally have at most dozens of positions and possibly hundreds or thousands of trades over its lifetime. The only optimization applied to this physical data model is the elimination of columns with the name date in the four trade tables. Since trade ids are defined as TIMEUUIDs, trades are ordered and can be queried based on the time components of TIMEUUIDs. Date values are also easy to extract from TIMEUUIDs. As a result, storing dates explicitly becomes unnecessary. Our final blueprint is ready to be instantiated in Cassandra."),(0,r.kt)("h2",{id:"hands-on"},"Hands-on"),(0,r.kt)("p",null,"In this lab, you will:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Create tables for an investment portfolio data use case"),(0,r.kt)("li",{parentName:"ul"},"Populate tables with sample investment portfolio data"),(0,r.kt)("li",{parentName:"ul"},"Design and execute CQL queries over investment portfolio data")),(0,r.kt)("h3",{id:"create-keyspace"},"Create Keyspace"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"CREATE KEYSPACE investment_data\nWITH replication = {\n  'class': 'SimpleStrategy', \n  'replication_factor': 1 }; \n\nUSE investment_data;\n")),(0,r.kt)("h3",{id:"create-tables"},"Create Tables"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"CREATE TABLE IF NOT EXISTS accounts_by_user (\n  username TEXT,\n  account_number TEXT,\n  cash_balance DECIMAL,\n  name TEXT STATIC,\n  PRIMARY KEY ((username),account_number)\n);\n\nCREATE TABLE IF NOT EXISTS positions_by_account (\n  account TEXT,\n  symbol TEXT,\n  quantity DECIMAL,\n  PRIMARY KEY ((account),symbol)\n);\n\nCREATE TABLE IF NOT EXISTS trades_by_a_d (\n  account TEXT,\n  trade_id TIMEUUID,\n  type TEXT,\n  symbol TEXT,\n  shares DECIMAL,\n  price DECIMAL,\n  amount DECIMAL,\n  PRIMARY KEY ((account),trade_id)\n) WITH CLUSTERING ORDER BY (trade_id DESC);\n\nCREATE TABLE IF NOT EXISTS trades_by_a_td (\n  account TEXT,\n  trade_id TIMEUUID,\n  type TEXT,\n  symbol TEXT,\n  shares DECIMAL,\n  price DECIMAL,\n  amount DECIMAL,\n  PRIMARY KEY ((account),type,trade_id)\n) WITH CLUSTERING ORDER BY (type ASC, trade_id DESC);\n\nCREATE TABLE IF NOT EXISTS trades_by_a_std (\n  account TEXT,\n  trade_id TIMEUUID,\n  type TEXT,\n  symbol TEXT,\n  shares DECIMAL,\n  price DECIMAL,\n  amount DECIMAL,\n  PRIMARY KEY ((account),symbol,type,trade_id)\n) WITH CLUSTERING ORDER BY (symbol ASC, type ASC, trade_id DESC);\n\nCREATE TABLE IF NOT EXISTS trades_by_a_sd (\n  account TEXT,\n  trade_id TIMEUUID,\n  type TEXT,\n  symbol TEXT,\n  shares DECIMAL,\n  price DECIMAL,\n  amount DECIMAL,\n  PRIMARY KEY ((account),symbol,trade_id)\n) WITH CLUSTERING ORDER BY (symbol ASC, trade_id DESC);\n\nDESCRIBE TABLES;\n")),(0,r.kt)("h3",{id:"populate-tables"},"Populate tables"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"SOURCE 'investment_data.cql'\n")),(0,r.kt)("p",null,"Retrieve some rows from tables:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT * FROM accounts_by_user;        \nSELECT * FROM positions_by_account;\nSELECT * FROM trades_by_a_d;                    \nSELECT * FROM trades_by_a_td;\nSELECT * FROM trades_by_a_std;       \nSELECT * FROM trades_by_a_sd;   \n")),(0,r.kt)("h3",{id:"design-query-q1"},"Design query Q1"),(0,r.kt)("p",null,"Find information about all investment accounts of a user with username joe:"),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Show me the Answer! "),"```sql SELECT * FROM accounts_by_user WHERE username = 'joe'; ```"),(0,r.kt)("br",null),(0,r.kt)("h3",{id:"design-query-q2"},"Design query Q2"),(0,r.kt)("p",null,"Find all positions in account joe001; order by instrument symbol (asc):"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT * \nFROM positions_by_account\nWHERE account = 'joe001'; \n")),(0,r.kt)("h3",{id:"design-query-q3"},"Design query Q3"),(0,r.kt)("p",null,"Find all trades for account joe001; order by trade date (desc):"),(0,r.kt)("details",null,(0,r.kt)("summary",null,"Show me the Answer! "),"```sql SELECT account, TODATE(DATEOF(trade_id)) AS date, trade_id, type, symbol, shares, price, amount FROM trades_by_a_d WHERE account = 'joe001'; ```"),(0,r.kt)("br",null),(0,r.kt)("h3",{id:"design-query-q4"},"Design query Q4"),(0,r.kt)("p",null,"Find all trades for account joe001 and date range 2020-09-07 - 2020-09-11; order by trade date (desc):"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT account, \n      TODATE(DATEOF(trade_id)) AS date, \n      trade_id, type, symbol,\n      shares, price, amount \nFROM trades_by_a_d\nWHERE account = 'joe001'\n  AND trade_id > maxTimeuuid('2020-09-07')\n  AND trade_id < minTimeuuid('2020-09-12');\n")),(0,r.kt)("h3",{id:"design-query-q5"},"Design query Q5"),(0,r.kt)("p",null,"Find all trades for account joe001, date range 2020-09-07 - 2020-09-11 and transaction type buy; order by trade date (desc):"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT account, \n      TODATE(DATEOF(trade_id)) AS date, \n      trade_id, type, symbol,\n      shares, price, amount \nFROM trades_by_a_td\nWHERE account = 'joe001'\n  AND type = 'buy'\n  AND trade_id > maxTimeuuid('2020-09-07')\n  AND trade_id < minTimeuuid('2020-09-12');\n")),(0,r.kt)("h3",{id:"design-query-q6"},"Design query Q6"),(0,r.kt)("p",null,"Find all trades for account joe001, date range 2020-09-07 - 2020-09-11, transaction type buy and instrument symbol AAPL; order by trade date (desc):"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT account, \n      TODATE(DATEOF(trade_id)) AS date, \n      trade_id, type, symbol,\n      shares, price, amount \nFROM trades_by_a_std\nWHERE account = 'joe001'\n  AND symbol = 'AAPL'\n  AND type = 'buy'\n  AND trade_id > maxTimeuuid('2020-09-07')\n  AND trade_id < minTimeuuid('2020-09-12');\n")),(0,r.kt)("h3",{id:"design-query-q7"},"Design query Q7"),(0,r.kt)("p",null,"Find all trades for account joe001, date range 2020-09-07 - 2020-09-11 and instrument symbol AAPL; order by trade date (desc):"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT account, \n      TODATE(DATEOF(trade_id)) AS date, \n      trade_id, type, symbol,\n      shares, price, amount \nFROM trades_by_a_sd\nWHERE account = 'joe001'\n  AND symbol = 'AAPL'\n  AND trade_id > maxTimeuuid('2020-09-07')\n  AND trade_id < minTimeuuid('2020-09-12');\n")))}u.isMDXComponent=!0}}]);