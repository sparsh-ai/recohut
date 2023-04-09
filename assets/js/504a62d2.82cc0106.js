"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[42491],{3905:(e,t,r)=>{r.d(t,{Zo:()=>u,kt:()=>m});var a=r(67294);function n(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,a)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){n(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,a,n=function(e,t){if(null==e)return{};var r,a,n={},o=Object.keys(e);for(a=0;a<o.length;a++)r=o[a],t.indexOf(r)>=0||(n[r]=e[r]);return n}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)r=o[a],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var s=a.createContext({}),p=function(e){var t=a.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},u=function(e){var t=p(e.components);return a.createElement(s.Provider,{value:t},e.children)},c={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},d=a.forwardRef((function(e,t){var r=e.components,n=e.mdxType,o=e.originalType,s=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),d=p(r),m=n,h=d["".concat(s,".").concat(m)]||d[m]||c[m]||o;return r?a.createElement(h,i(i({ref:t},u),{},{components:r})):a.createElement(h,i({ref:t},u))}));function m(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var o=r.length,i=new Array(o);i[0]=d;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:n,i[1]=l;for(var p=2;p<o;p++)i[p]=r[p];return a.createElement.apply(null,i)}return a.createElement.apply(null,r)}d.displayName="MDXCreateElement"},28478:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>c,frontMatter:()=>o,metadata:()=>l,toc:()=>p});var a=r(87462),n=(r(67294),r(3905));const o={},i="Realtime Streaming analytics with Apache Kafka and Spark Streaming",l={unversionedId:"processing/lab-kafka-spark-streaming/README",id:"processing/lab-kafka-spark-streaming/README",title:"Realtime Streaming analytics with Apache Kafka and Spark Streaming",description:"Activity 1",source:"@site/docs/03-processing/lab-kafka-spark-streaming/README.md",sourceDirName:"03-processing/lab-kafka-spark-streaming",slug:"/processing/lab-kafka-spark-streaming/",permalink:"/docs/processing/lab-kafka-spark-streaming/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Getting started with Kafka and Python",permalink:"/docs/processing/lab-kafka-python/"},next:{title:"Stock Market Kafka Real Time",permalink:"/docs/processing/lab-kafka-stock-market/"}},s={},p=[{value:"Activity 1",id:"activity-1",level:2},{value:"Activity 2",id:"activity-2",level:2}],u={toc:p};function c(e){let{components:t,...r}=e;return(0,n.kt)("wrapper",(0,a.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"realtime-streaming-analytics-with-apache-kafka-and-spark-streaming"},"Realtime Streaming analytics with Apache Kafka and Spark Streaming"),(0,n.kt)("h2",{id:"activity-1"},"Activity 1"),(0,n.kt)("p",null,"Basketista is a retail company and they want to build a real-time analytics solution to get insights about their business orders and take decisions in near real-time environment."),(0,n.kt)("p",null,(0,n.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/211325959-dec2aa5c-93c5-403d-9dbe-bb5fe0b8d45f.svg",alt:null})),(0,n.kt)("p",null,"In this activity, you will:"),(0,n.kt)("ol",null,(0,n.kt)("li",{parentName:"ol"},"Setup the Environment - Postgres, Kafka, Spark Streaming applications"),(0,n.kt)("li",{parentName:"ol"},"Create Kafka Producer and send data to Kafka topic"),(0,n.kt)("li",{parentName:"ol"},"Build ETL logic in PySpark and integrate in Spark Stream"),(0,n.kt)("li",{parentName:"ol"},"Create Kafka Consumer and Store the procesed data in Postgres"),(0,n.kt)("li",{parentName:"ol"},"Connect to Postgres and validate the data load")),(0,n.kt)("h2",{id:"activity-2"},"Activity 2"),(0,n.kt)("p",null,"The objective is to analyze the \u201cretail_db\u201d dataset, provide reports on the total completed orders, and perform customer and product analytics. This activity is designed to help understand the retail database and generate reports on the completed orders. You should be able to analyze the dataset for this activity to create a report. You will be able to use PySpark, do analyses, and obtain the desired results."),(0,n.kt)("p",null,"Problem Statement: Customers can purchase products or services from Amazon for consumption and usage. Amazon usually sells products and services in-store. However, some may be sold online or over the phone and shipped to the customer. Clothing, medicine, supermarkets, and convenience stores are examples of their retail operations."),(0,n.kt)("p",null,"Perform the following tasks on the dataset provided using PySpark:"),(0,n.kt)("ol",null,(0,n.kt)("li",{parentName:"ol"},'Explore the customer records saved in the "customers-tab-delimited\u201c directory on HDFS',(0,n.kt)("ul",{parentName:"li"},(0,n.kt)("li",{parentName:"ul"},"Show the client information for those who live in California"),(0,n.kt)("li",{parentName:"ul"},"Save the results in the result/scenario1/solution folder"),(0,n.kt)("li",{parentName:"ul"},"Include the customer's entire name in the output"))),(0,n.kt)("li",{parentName:"ol"},"Explore the order records saved in the \u201corders parquet\u201d directory on HDFS",(0,n.kt)("ul",{parentName:"li"},(0,n.kt)("li",{parentName:"ul"},'Show all orders with the order status value "COMPLETE\u201c'),(0,n.kt)("li",{parentName:"ul"},'Save the data in the "result/scenario2/solution" directory on HDFS'),(0,n.kt)("li",{parentName:"ul"},"Include order number, order date, and current situation in the output"))),(0,n.kt)("li",{parentName:"ol"},'Explore the customer records saved in the "customers-tab- delimited\u201c directory on HDFS',(0,n.kt)("ul",{parentName:"li"},(0,n.kt)("li",{parentName:"ul"},'Produce a list of all consumers who live in the city of "Caguas"'),(0,n.kt)("li",{parentName:"ul"},"Save the results in the result/scenario3/solutionfolder"),(0,n.kt)("li",{parentName:"ul"},'The result should only contain records with the value "Caguas" for the customer city'))),(0,n.kt)("li",{parentName:"ol"},"Explore the order records saved in the \u201ccategories\u201d directory on HDFS",(0,n.kt)("ul",{parentName:"li"},(0,n.kt)("li",{parentName:"ul"},"Save the result files in CSV format"),(0,n.kt)("li",{parentName:"ul"},"Save the data in the result/scenario4/solution directory on HDFS"),(0,n.kt)("li",{parentName:"ul"},"Use lz4 compression to compress the output"))),(0,n.kt)("li",{parentName:"ol"},'Explore the customer records saved in the \u201cproducts_avro" directory on HDFS',(0,n.kt)("ul",{parentName:"li"},(0,n.kt)("li",{parentName:"ul"},"Include the products with a price of more than 1000.0 in the output"),(0,n.kt)("li",{parentName:"ul"},"Remove data from the table if the product price is greater than 1000.0"),(0,n.kt)("li",{parentName:"ul"},"Save the results in the result/scenario5/solution folder"))),(0,n.kt)("li",{parentName:"ol"},"Explore the order records saved in the \u201cproducts_avro\u201d directory on HDFS",(0,n.kt)("ul",{parentName:"li"},(0,n.kt)("li",{parentName:"ul"},"Only products with a price of more than 1000.0 should be in the output"),(0,n.kt)("li",{parentName:"ul"},'The pattern "Treadmill" appears in the product name'),(0,n.kt)("li",{parentName:"ul"},"Save the data in the result/scenario6/solution directory on HDFS"))),(0,n.kt)("li",{parentName:"ol"},'Explore the customer records saved in the \u201corders parquet" directory on HDFS',(0,n.kt)("ul",{parentName:"li"},(0,n.kt)("li",{parentName:"ul"},"Output all PENDING orders in July 2013"),(0,n.kt)("li",{parentName:"ul"},'Only entries with the order status value of "PENDING" should be included in the result'),(0,n.kt)("li",{parentName:"ul"},"Order date should be in the YYY-MM-DD format"),(0,n.kt)("li",{parentName:"ul"},"Save the results in the result/scenario7/solution folder")))))}c.isMDXComponent=!0}}]);