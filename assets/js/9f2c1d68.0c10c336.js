"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[97475],{3905:(e,n,a)=>{a.d(n,{Zo:()=>c,kt:()=>p});var t=a(67294);function r(e,n,a){return n in e?Object.defineProperty(e,n,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[n]=a,e}function s(e,n){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);n&&(t=t.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),a.push.apply(a,t)}return a}function l(e){for(var n=1;n<arguments.length;n++){var a=null!=arguments[n]?arguments[n]:{};n%2?s(Object(a),!0).forEach((function(n){r(e,n,a[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):s(Object(a)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(a,n))}))}return e}function o(e,n){if(null==e)return{};var a,t,r=function(e,n){if(null==e)return{};var a,t,r={},s=Object.keys(e);for(t=0;t<s.length;t++)a=s[t],n.indexOf(a)>=0||(r[a]=e[a]);return r}(e,n);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(t=0;t<s.length;t++)a=s[t],n.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var i=t.createContext({}),u=function(e){var n=t.useContext(i),a=n;return e&&(a="function"==typeof e?e(n):l(l({},n),e)),a},c=function(e){var n=u(e.components);return t.createElement(i.Provider,{value:n},e.children)},m={inlineCode:"code",wrapper:function(e){var n=e.children;return t.createElement(t.Fragment,{},n)}},d=t.forwardRef((function(e,n){var a=e.components,r=e.mdxType,s=e.originalType,i=e.parentName,c=o(e,["components","mdxType","originalType","parentName"]),d=u(a),p=r,g=d["".concat(i,".").concat(p)]||d[p]||m[p]||s;return a?t.createElement(g,l(l({ref:n},c),{},{components:a})):t.createElement(g,l({ref:n},c))}));function p(e,n){var a=arguments,r=n&&n.mdxType;if("string"==typeof e||r){var s=a.length,l=new Array(s);l[0]=d;var o={};for(var i in n)hasOwnProperty.call(n,i)&&(o[i]=n[i]);o.originalType=e,o.mdxType="string"==typeof e?e:r,l[1]=o;for(var u=2;u<s;u++)l[u]=a[u];return t.createElement.apply(null,l)}return t.createElement.apply(null,a)}d.displayName="MDXCreateElement"},45823:(e,n,a)=>{a.r(n),a.d(n,{assets:()=>i,contentTitle:()=>l,default:()=>m,frontMatter:()=>s,metadata:()=>o,toc:()=>u});var t=a(87462),r=(a(67294),a(3905));const s={},l="Lab - MongoDB Basics",o={unversionedId:"storage/lab-mongodb-basics/README",id:"storage/lab-mongodb-basics/README",title:"Lab - MongoDB Basics",description:"Environment Setup",source:"@site/docs/02-storage/lab-mongodb-basics/README.md",sourceDirName:"02-storage/lab-mongodb-basics",slug:"/storage/lab-mongodb-basics/",permalink:"/docs/storage/lab-mongodb-basics/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Introduction to DynamoDB",permalink:"/docs/storage/lab-intro-to-dynamodb/"},next:{title:"MongoDB to CSV conversion",permalink:"/docs/storage/lab-mongodb-pandas/"}},i={},u=[{value:"Environment Setup",id:"environment-setup",level:2},{value:"MongoDB CRUD",id:"mongodb-crud",level:2},{value:"MongoDB Indexing",id:"mongodb-indexing",level:2},{value:"MongoDB Aggregation",id:"mongodb-aggregation",level:2},{value:"Assignment 1",id:"assignment-1",level:3},{value:"Assignment 2",id:"assignment-2",level:3}],c={toc:u};function m(e){let{components:n,...a}=e;return(0,r.kt)("wrapper",(0,t.Z)({},c,a,{components:n,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"lab---mongodb-basics"},"Lab - MongoDB Basics"),(0,r.kt)("h2",{id:"environment-setup"},"Environment Setup"),(0,r.kt)("p",null,"Connect to Atlas Cluster:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},'mongosh "mongodb+srv://cluster0.css32tr.mongodb.net/myFirstDatabase" --apiVersion 1 --username admin\n')),(0,r.kt)("h2",{id:"mongodb-crud"},"MongoDB CRUD"),(0,r.kt)("p",null,"Run the below code on mongo console. It will insert 5 documents, which will serve as sample data for the the assignment."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'use training\ndb.languages.insert({"name":"java","type":"object oriented"})\ndb.languages.insert({"name":"python","type":"general purpose"})\ndb.languages.insert({"name":"scala","type":"functional"})\ndb.languages.insert({"name":"c","type":"procedural"})\ndb.languages.insert({"name":"c++","type":"object oriented"})\n')),(0,r.kt)("p",null,"Task 1: Insert an entry for 'Haskell' programming language which is of type 'functional"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.languages.insert({"name":"Haskell","type":"functional"})\n')),(0,r.kt)("p",null,"Task 2: Query for all functional languages"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.languages.find({"type":"functional"})\n')),(0,r.kt)("p",null,"Task 3: Add \u2018Bjarne Stroustrup\u2019 as creator for c++"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.languages.updateMany({"name":"c++"},{$set:{"creator":"Bjarne Stroustrup"}})\n')),(0,r.kt)("p",null,"Task 4: Delete all functional programming languages"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.languages.remove({"type":"functional"})\n')),(0,r.kt)("p",null,"Task 5: Disconnect from the mongodb server"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"exit\n")),(0,r.kt)("h2",{id:"mongodb-indexing"},"MongoDB Indexing"),(0,r.kt)("p",null,"Task 1: Create a collection named bigdata"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.createCollection("bigdata")\n')),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Insert documents")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Let us insert a lot of documents into the newly created collection."),(0,r.kt)("li",{parentName:"ul"},"This should take around 3 minutes, so please be patient."),(0,r.kt)("li",{parentName:"ul"},"The code given below will insert 200000 documents into the 'bigdata' collection."),(0,r.kt)("li",{parentName:"ul"},"Each document would have a field named\xa0",(0,r.kt)("strong",{parentName:"li"},"account_no"),"\xa0which is a simple auto increment number."),(0,r.kt)("li",{parentName:"ul"},"And a field named\xa0",(0,r.kt)("strong",{parentName:"li"},"balance"),"\xa0which is a randomly generated number, to simulate the bank balance for the account.")),(0,r.kt)("p",null,"Copy the below code and paste it on the mongo client."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'use training\nfor (i=1;i<=200000;i++){print(i);db.bigdata.insert({"account_no":i,"balance":Math.round(Math.random()*1000000)})}\n')),(0,r.kt)("p",null,"Task 2: Verify that 200000 documents got inserted"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"db.bigdata.count()\n")),(0,r.kt)("p",null,"Task 3: Measure the time taken by a query"),(0,r.kt)("p",null,"Let us run a query and find out how much time it takes to complete."),(0,r.kt)("p",null,"Let us query for the details of account number 58982."),(0,r.kt)("p",null,"We will make use of the explain function to find the time taken to run the query in milliseconds."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.bigdata.find({"account_no":58982}).explain("executionStats").executionStats.executionTimeMillis\n')),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Working with indexes")),(0,r.kt)("p",null,"Before you create an index, choose the field you wish to create an index on. It is usually the field that you query most."),(0,r.kt)("p",null,"Run the below command to create an index on the field account_no."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.bigdata.createIndex({"account_no":1})\n')),(0,r.kt)("p",null,"Task 4: Get a list of indexes on the \u2018bigdata\u2019 collection."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"db.bigdata.getIndexes()\n")),(0,r.kt)("p",null,"Task 5: Find out how effective an index is"),(0,r.kt)("p",null,"Let us query for the details of account number 69271:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.bigdata.find({"account_no": 69271}).explain("executionStats").executionStats.executionTimeMillis\n')),(0,r.kt)("p",null,"Task 6: Delete the index we created earlier"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.bigdata.dropIndex({"account_no":1})\n')),(0,r.kt)("p",null,"Task 7: Create an index on the balance field"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.bigdata.createIndex({"balance":1})\n')),(0,r.kt)("p",null,"Task 8: Query for documents with a balance of 10000 and record the time taken"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.bigdata.find({"balance":10000}).explain("executionStats").executionStats.executionTimeMillis\n')),(0,r.kt)("p",null,"Task 9: Drop the index you have created"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.bigdata.dropIndex({"balance":1})\n')),(0,r.kt)("p",null,"Task 10: Query for documents with a balance of 10000 and record the time taken, and compare it with the previously recorded time"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.bigdata.find({"balance": 10000}).explain("executionStats").executionStats.executionTimeMillis\n')),(0,r.kt)("p",null,"Task 11: Disconnect from the mongodb server"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"exit\n")),(0,r.kt)("h2",{id:"mongodb-aggregation"},"MongoDB Aggregation"),(0,r.kt)("p",null,"Load sample data into the training database:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'use training\ndb.marks.insert({"name":"Ramesh","subject":"maths","marks":87})\ndb.marks.insert({"name":"Ramesh","subject":"english","marks":59})\ndb.marks.insert({"name":"Ramesh","subject":"science","marks":77})\ndb.marks.insert({"name":"Rav","subject":"maths","marks":62})\ndb.marks.insert({"name":"Rav","subject":"english","marks":83})\ndb.marks.insert({"name":"Rav","subject":"science","marks":71})\ndb.marks.insert({"name":"Alison","subject":"maths","marks":84})\ndb.marks.insert({"name":"Alison","subject":"english","marks":82})\ndb.marks.insert({"name":"Alison","subject":"science","marks":86})\ndb.marks.insert({"name":"Steve","subject":"maths","marks":81})\ndb.marks.insert({"name":"Steve","subject":"english","marks":89})\ndb.marks.insert({"name":"Steve","subject":"science","marks":77})\ndb.marks.insert({"name":"Jan","subject":"english","marks":0,"reason":"absent"})\n')),(0,r.kt)("h3",{id:"assignment-1"},"Assignment 1"),(0,r.kt)("p",null,"Task 1: Limiting the rows in the output - print only 2 documents from the marks collection"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'use training\ndb.marks.aggregate([{"$limit":2}])\n')),(0,r.kt)("p",null,"Task 2: Sorting based on a column - sorts the documents based on field marks in ascending/descending order"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'-- ascending\ndb.marks.aggregate([{"$sort":{"marks":1}}])\n\n--descending\ndb.marks.aggregate([{"$sort":{"marks":-1}}])\n')),(0,r.kt)("p",null,"Task 3: Sorting and limiting - create a two stage pipeline that answers the question ",(0,r.kt)("inlineCode",{parentName:"p"},"What are the top 2 marks?")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.marks.aggregate([\n{"$sort":{"marks":-1}},\n{"$limit":2}\n])\n')),(0,r.kt)("p",null,"Task 4: Group by - prints the average marks across all subjects"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.marks.aggregate([\n{\n    "$group":{\n        "_id":"$subject",\n        "average":{"$avg":"$marks"}\n        }\n}\n])\n')),(0,r.kt)("p",null,"Task 5: Write the SQL equivalent of the above query"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT subject, average(marks)\nFROM marks\nGROUP BY subject\n")),(0,r.kt)("p",null,"Task 6: Write a query to answer this question - ",(0,r.kt)("inlineCode",{parentName:"p"},"Who are the top 2 students by average marks?")),(0,r.kt)("p",null,"This involves:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"finding the average marks per student."),(0,r.kt)("li",{parentName:"ul"},"sorting the output based on average marks in descending order."),(0,r.kt)("li",{parentName:"ul"},"limiting the output to two documents.")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.marks.aggregate([\n{\n    "$group":{\n        "_id":"$name",\n        "average":{"$avg":"$marks"}\n        }\n},\n{\n    "$sort":{"average":-1}\n},\n{\n    "$limit":2\n}\n])\n')),(0,r.kt)("h3",{id:"assignment-2"},"Assignment 2"),(0,r.kt)("p",null,"Task 1: Find the total marks for each student across all subjects"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.marks.aggregate([\n    {\n        "$group":{"_id":"$name","total":{"$sum":"$marks"}}\n    }\n])\n')),(0,r.kt)("p",null,"Task 2: Find the maximum marks scored in each subject"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.marks.aggregate([\n    {\n        "$group":{"_id":"$subject","max_marks":{"$max":"$marks"}}\n    }\n])\n')),(0,r.kt)("p",null,"Task 3: Find the minimum marks scored by each student"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.marks.aggregate([\n    {\n        "$group":{"_id":"$name","min_marks":{"$min":"$marks"}}\n    }\n])\n')),(0,r.kt)("p",null,"Task 4: Find the top two subjects based on average marks"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},'db.marks.aggregate([\n{\n    "$group":{\n        "_id":"$subject",\n        "average":{"$avg":"$marks"}\n        }\n},\n{\n    "$sort":{"average":-1}\n},\n{\n    "$limit":2\n}\n])\n')),(0,r.kt)("p",null,"Task 5: Disconnect from the mongodb server"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"exit\n")))}m.isMDXComponent=!0}}]);