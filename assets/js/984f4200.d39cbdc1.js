"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[92988],{3905:(e,t,a)=>{a.d(t,{Zo:()=>d,kt:()=>c});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function l(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?l(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},l=Object.keys(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var s=n.createContext({}),u=function(e){var t=n.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},d=function(e){var t=u(e.components);return n.createElement(s.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,l=e.originalType,s=e.parentName,d=o(e,["components","mdxType","originalType","parentName"]),m=u(a),c=r,k=m["".concat(s,".").concat(c)]||m[c]||p[c]||l;return a?n.createElement(k,i(i({ref:t},d),{},{components:a})):n.createElement(k,i({ref:t},d))}));function c(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var l=a.length,i=new Array(l);i[0]=m;var o={};for(var s in t)hasOwnProperty.call(t,s)&&(o[s]=t[s]);o.originalType=e,o.mdxType="string"==typeof e?e:r,i[1]=o;for(var u=2;u<l;u++)i[u]=a[u];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}m.displayName="MDXCreateElement"},71860:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>p,frontMatter:()=>l,metadata:()=>o,toc:()=>u});var n=a(87462),r=(a(67294),a(3905));const l={},i="SQL vs NoSQL",o={unversionedId:"foundations/data-engineering-foundations/sql-vs-nosql",id:"foundations/data-engineering-foundations/sql-vs-nosql",title:"SQL vs NoSQL",description:"As you design large systems ( or even smaller ones), you need to decide the inflow-processing and outflow of data coming- and getting processed in the system.",source:"@site/docs/01-foundations/02-data-engineering-foundations/sql-vs-nosql.md",sourceDirName:"01-foundations/02-data-engineering-foundations",slug:"/foundations/data-engineering-foundations/sql-vs-nosql",permalink:"/docs/foundations/data-engineering-foundations/sql-vs-nosql",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Spark Quiz",permalink:"/docs/foundations/data-engineering-foundations/spark-quiz"},next:{title:"Real-Time Analytics",permalink:"/docs/foundations/data-engineering-foundations/stream-data-processing"}},s={},u=[{value:"Storage",id:"storage",level:3},{value:"Schema",id:"schema",level:3},{value:"Querying",id:"querying",level:3},{value:"Scalability",id:"scalability",level:3},{value:"ACID",id:"acid",level:3},{value:"Common types of NoSQL",id:"common-types-of-nosql",level:3},{value:"Key-value stores",id:"key-value-stores",level:4},{value:"Document databases",id:"document-databases",level:4},{value:"Wide-column / columnar databases",id:"wide-column--columnar-databases",level:4},{value:"Graph database",id:"graph-database",level:4}],d={toc:u};function p(e){let{components:t,...a}=e;return(0,r.kt)("wrapper",(0,n.Z)({},d,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"sql-vs-nosql"},"SQL vs NoSQL"),(0,r.kt)("p",null,"As you design large systems ( or even smaller ones), you need to decide the inflow-processing and outflow of data coming- and getting processed in the system."),(0,r.kt)("p",null,"Data is generally organized in tables as rows and columns where columns represents attributes and rows represent records and keys have logical relationships. The SQL db schema always shows relational, tabular data following the ACID properties."),(0,r.kt)("p",null,"SQL databases have predefined schema and the data is organized/displayed in the form of tables. These databases use SQL ( Structured Query Language) to define, manipulate, update the data."),(0,r.kt)("p",null,"Relational databases like MS SQL Server, PostgreSQL, Sybase, MySQL Database, Oracle, etc. use SQL."),(0,r.kt)("p",null,"NoSQL databases on the other side, have no predefined schema which adds to more flexibility to use the formats that best suits the data - Work with graphs, column-oriented data, key-value and documents etc. They are generally preferred for hierarchical data, graphs ( e.g. social network) and to work with large data."),(0,r.kt)("p",null,"Some examples - Wide-column use Cassandra and HBase, Graph use Neo4j, Document use MongoDB and CouchDB, Key-value use Redis and DynamoDB."),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/222883560-23c9b9d1-1105-4f34-acf4-d175ea41161e.png",alt:"sql-nosql"})),(0,r.kt)("table",null,(0,r.kt)("thead",{parentName:"table"},(0,r.kt)("tr",{parentName:"thead"},(0,r.kt)("th",{parentName:"tr",align:null}),(0,r.kt)("th",{parentName:"tr",align:null},"SQL"),(0,r.kt)("th",{parentName:"tr",align:null},"NoSQL"))),(0,r.kt)("tbody",{parentName:"table"},(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Definition"),(0,r.kt)("td",{parentName:"tr",align:null},"SQL databases are primarily called RDBMSs or relational databases."),(0,r.kt)("td",{parentName:"tr",align:null},"NoSQL databases are primarily called as non-relational or distributed databases.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Designed for"),(0,r.kt)("td",{parentName:"tr",align:null},"Traditional RDBMS uses SQL syntax and queries to analyze and get the data for further insights. They are used for OLAP systems."),(0,r.kt)("td",{parentName:"tr",align:null},"NoSQL database system consists of various kinds of database technologies. These databases were developed in response to the demands presented for the development of the modern application.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Query language"),(0,r.kt)("td",{parentName:"tr",align:null},"Structured Query Language (SQL)"),(0,r.kt)("td",{parentName:"tr",align:null},"No declarative query language")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Type"),(0,r.kt)("td",{parentName:"tr",align:null},"SQL databases are table-based databases."),(0,r.kt)("td",{parentName:"tr",align:null},"NoSQL databases can be document-based, key-value pair, graph databases.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Schema"),(0,r.kt)("td",{parentName:"tr",align:null},"SQL databases have a predefined schema."),(0,r.kt)("td",{parentName:"tr",align:null},"NoSQL databases use a dynamic schema for unstructured data.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Ability to scale"),(0,r.kt)("td",{parentName:"tr",align:null},"SQL databases are vertically scalable."),(0,r.kt)("td",{parentName:"tr",align:null},"NoSQL databases are horizontally scalable.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Examples"),(0,r.kt)("td",{parentName:"tr",align:null},"Oracle, Postgres, and MS SQL."),(0,r.kt)("td",{parentName:"tr",align:null},"MongoDB, Redis, Neo4j, Cassandra, HBase.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Best suited for"),(0,r.kt)("td",{parentName:"tr",align:null},"An ideal choice for the complex query-intensive environment."),(0,r.kt)("td",{parentName:"tr",align:null},"It is not a good fit for complex queries.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Hierarchical data\xa0storage"),(0,r.kt)("td",{parentName:"tr",align:null},"SQL databases are not suitable for hierarchical data storage."),(0,r.kt)("td",{parentName:"tr",align:null},"More suitable for the hierarchical data store as it supports key-value pair methods.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Variations"),(0,r.kt)("td",{parentName:"tr",align:null},"One type with minor variations."),(0,r.kt)("td",{parentName:"tr",align:null},"Many different types that include key-value stores, document databases, and graph databases.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Development year"),(0,r.kt)("td",{parentName:"tr",align:null},"It was developed in the 1970s to deal with issues with flat file storage."),(0,r.kt)("td",{parentName:"tr",align:null},"Developed in the late 2000s to overcome issues and limitations of SQL databases.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Consistency"),(0,r.kt)("td",{parentName:"tr",align:null},"It should be configured for strong consistency."),(0,r.kt)("td",{parentName:"tr",align:null},"It depends on DBMS as some offer strong consistency like MongoDB, whereas others offer only eventual consistency, like Cassandra.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Best used for"),(0,r.kt)("td",{parentName:"tr",align:null},"RDBMS is the right option for solving ACID problems."),(0,r.kt)("td",{parentName:"tr",align:null},"NoSQL is best used for solving data availability problems.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Importance"),(0,r.kt)("td",{parentName:"tr",align:null},"It should be used when data validity is super important."),(0,r.kt)("td",{parentName:"tr",align:null},"Use when it\u2019s more important to have fast data than correct data.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"Best option"),(0,r.kt)("td",{parentName:"tr",align:null},"When you need to support dynamic queries."),(0,r.kt)("td",{parentName:"tr",align:null},"Use when you need to scale based on changing requirements.")),(0,r.kt)("tr",{parentName:"tbody"},(0,r.kt)("td",{parentName:"tr",align:null},"ACID vs. BASE\xa0model"),(0,r.kt)("td",{parentName:"tr",align:null},"ACID (Atomicity, Consistency, Isolation, and Durability) is a standard for RDBMS."),(0,r.kt)("td",{parentName:"tr",align:null},"BASE (Basically Available, Soft state, Eventually consistent) is a model of many NoSQL systems.")))),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"SQL")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Ensure ACID compliance.",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Reduce anomalies."),(0,r.kt)("li",{parentName:"ul"},"Protect database integrity."))),(0,r.kt)("li",{parentName:"ul"},"Data is structured and unchanging.")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"NoSQL")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Data has little or no structure."),(0,r.kt)("li",{parentName:"ul"},"Make the most of cloud computing and storage.",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Cloud-based storage requires data to be easily spread across multiple servers to scale up."))),(0,r.kt)("li",{parentName:"ul"},"Rapid development.",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Frequent updates to the data structure.")))),(0,r.kt)("h3",{id:"storage"},"Storage"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"SQL: store data in tables."),(0,r.kt)("li",{parentName:"ul"},"NoSQL: have different data storage models.")),(0,r.kt)("h3",{id:"schema"},"Schema"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"SQL",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Each record conforms to a fixed schema."),(0,r.kt)("li",{parentName:"ul"},"Schema can be altered, but it requires modifying the whole database."))),(0,r.kt)("li",{parentName:"ul"},"NoSQL:",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Schemas are dynamic.")))),(0,r.kt)("h3",{id:"querying"},"Querying"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"SQL",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Use SQL (structured query language) for defining and manipulating the data."))),(0,r.kt)("li",{parentName:"ul"},"NoSQL",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Queries are focused on a collection of documents."),(0,r.kt)("li",{parentName:"ul"},"UnQL (unstructured query language)."),(0,r.kt)("li",{parentName:"ul"},"Different databases have different syntax.")))),(0,r.kt)("h3",{id:"scalability"},"Scalability"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"SQL",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Vertically scalable (by increasing the horsepower: memory, CPU, etc) and expensive."),(0,r.kt)("li",{parentName:"ul"},"Horizontally scalable (across multiple servers); but it can be challenging and time-consuming."))),(0,r.kt)("li",{parentName:"ul"},"NoSQL",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Horizontablly scalable (by adding more servers) and cheap.")))),(0,r.kt)("h3",{id:"acid"},"ACID"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Atomicity, consistency, isolation, durability"),(0,r.kt)("li",{parentName:"ul"},"SQL",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"ACID compliant"),(0,r.kt)("li",{parentName:"ul"},"Data reliability"),(0,r.kt)("li",{parentName:"ul"},"Gurantee of transactions"))),(0,r.kt)("li",{parentName:"ul"},"NoSQL",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Most sacrifice ACID compliance for performance and scalability.")))),(0,r.kt)("h3",{id:"common-types-of-nosql"},"Common types of NoSQL"),(0,r.kt)("h4",{id:"key-value-stores"},"Key-value stores"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},'Array of key-value pairs. The "key" is an attribute name.'),(0,r.kt)("li",{parentName:"ul"},"Redis, Vodemort, Dynamo.")),(0,r.kt)("h4",{id:"document-databases"},"Document databases"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Data is stored in documents."),(0,r.kt)("li",{parentName:"ul"},"Documents are grouped in collections."),(0,r.kt)("li",{parentName:"ul"},"Each document can have an entirely different structure."),(0,r.kt)("li",{parentName:"ul"},"CouchDB, MongoDB.")),(0,r.kt)("h4",{id:"wide-column--columnar-databases"},"Wide-column / columnar databases"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Column families - containers for rows."),(0,r.kt)("li",{parentName:"ul"},"No need to know all the columns up front."),(0,r.kt)("li",{parentName:"ul"},"Each row can have different number of columns."),(0,r.kt)("li",{parentName:"ul"},"Cassandra, HBase.")),(0,r.kt)("h4",{id:"graph-database"},"Graph database"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Data is stored in graph structures",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Nodes: entities"),(0,r.kt)("li",{parentName:"ul"},"Properties: information about the entities"),(0,r.kt)("li",{parentName:"ul"},"Lines: connections between the entities"))),(0,r.kt)("li",{parentName:"ul"},"Neo4J, InfiniteGraph")))}p.isMDXComponent=!0}}]);