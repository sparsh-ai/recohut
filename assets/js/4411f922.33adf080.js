"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[78496],{3905:(e,t,a)=>{a.d(t,{Zo:()=>m,kt:()=>p});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function s(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},i=Object.keys(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var l=n.createContext({}),c=function(e){var t=n.useContext(l),a=t;return e&&(a="function"==typeof e?e(t):s(s({},t),e)),a},m=function(e){var t=c(e.components);return n.createElement(l.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,i=e.originalType,l=e.parentName,m=o(e,["components","mdxType","originalType","parentName"]),u=c(a),p=r,f=u["".concat(l,".").concat(p)]||u[p]||d[p]||i;return a?n.createElement(f,s(s({ref:t},m),{},{components:a})):n.createElement(f,s({ref:t},m))}));function p(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=a.length,s=new Array(i);s[0]=u;var o={};for(var l in t)hasOwnProperty.call(t,l)&&(o[l]=t[l]);o.originalType=e,o.mdxType="string"==typeof e?e:r,s[1]=o;for(var c=2;c<i;c++)s[c]=a[c];return n.createElement.apply(null,s)}return n.createElement.apply(null,a)}u.displayName="MDXCreateElement"},85268:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>l,contentTitle:()=>s,default:()=>d,frontMatter:()=>i,metadata:()=>o,toc:()=>c});var n=a(87462),r=(a(67294),a(3905));const i={},s="Batch and Stream Unified analytics for Sakila Music Company",o={unversionedId:"assignments/sakila/README",id:"assignments/sakila/README",title:"Batch and Stream Unified analytics for Sakila Music Company",description:"Problem Statement",source:"@site/docs/11-assignments/sakila/README.md",sourceDirName:"11-assignments/sakila",slug:"/assignments/sakila/",permalink:"/docs/assignments/sakila/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"OLX Data Engineering Challenge",permalink:"/docs/assignments/olx-python/"},next:{title:"Spiff Data Engineering Candidate Coding Exercises",permalink:"/docs/assignments/spiff-takehome/"}},l={},c=[{value:"Problem Statement",id:"problem-statement",level:2},{value:"Architecture Diagram",id:"architecture-diagram",level:2},{value:"References",id:"references",level:2}],m={toc:c};function d(e){let{components:t,...a}=e;return(0,r.kt)("wrapper",(0,n.Z)({},m,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"batch-and-stream-unified-analytics-for-sakila-music-company"},"Batch and Stream Unified analytics for Sakila Music Company"),(0,r.kt)("h2",{id:"problem-statement"},"Problem Statement"),(0,r.kt)("p",null,"The Sakila was a company that produced classic movies and rented those out of their DVD stores. The DVD rental stores went out of business years ago, but the owners have now made their classic movies available for purchase and rental through various streaming platforms."),(0,r.kt)("p",null,"The company receives information about their classic movies being streamed from their distribution partners in real time, in a standard format. Using KDG, we will simulate the streaming data that's received from partners, including the following:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Streaming timestamp"),(0,r.kt)("li",{parentName:"ul"},"Whether the customer rented, purchased, or watched the trailer"),(0,r.kt)("li",{parentName:"ul"},(0,r.kt)("strong",{parentName:"li"},"film_id"),"\xa0that matches the Sakila film database"),(0,r.kt)("li",{parentName:"ul"},"The distribution partner name"),(0,r.kt)("li",{parentName:"ul"},"Streaming platform"),(0,r.kt)("li",{parentName:"ul"},"The state that the movie was streamed in")),(0,r.kt)("p",null,"For Batch data - Load data into RDS Postgrs, Create AWS Data Migration Service Endpoints, Replication Instances and Tasks, Start the Task, Verify the Ingestion with Athena. For Stream data - Create Kinesis Firehose, Create Kinesis Data Generator and Push data to Firehose, Create and run Glue crawler on the streamed file in S3 and verify the ingestion with Athena."),(0,r.kt)("p",null,"NOTE"),(0,r.kt)("blockquote",null,(0,r.kt)("p",{parentName:"blockquote"},"The Sakila sample database is made available by MySQL and is licensed via the New BSD license. Sakila contains data for a fictitious movie rental company, and includes tables such as store, inventory, film, customer, and payment. While actual movie rental stores are largely a thing of the past, with a little imagination we could rebrand it as a movie-streaming company by ignoring the staff and address tables and renaming store to streaming_service.")),(0,r.kt)("h2",{id:"architecture-diagram"},"Architecture Diagram"),(0,r.kt)("p",null,"In most organizations, there are also likely to be multiple environments, such as a development environment, a test/",(0,r.kt)("strong",{parentName:"p"},"quality assurance"),"\xa0(",(0,r.kt)("strong",{parentName:"p"},"QA"),") environment, and a\xa0production environment. The data infrastructure and pipelines must be deployed and tested in the development environment first, and then any updates should be pushed to a test/QA environment for automated testing, before finally being approved for deployment in the production environment."),(0,r.kt)("p",null,"In the following diagram, we can see that there are multiple teams responsible for different aspects of data engineering resources. We can also see that the data engineering resources are duplicated across multiple different environments (which would generally be different AWS accounts), such as the development environment, test/QA environment, and production environment. Each organization may structure its teams and\xa0environments\xa0a little differently, but this is an example of the complexity of data engineering in real life:"),(0,r.kt)("p",null,(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/215260810-dfd352f1-b4aa-4809-8b53-3e8e29bd266f.png",alt:"batch-stream-aws"})),(0,r.kt)("p",null,"TIP"),(0,r.kt)("blockquote",null,(0,r.kt)("p",{parentName:"blockquote"},"It is a challenge to work in these kinds of complex environments, and an organized approach is required to be successful. Part of understanding the bigger picture of data analytics is to understand these types of challenges and how to overcome them.")),(0,r.kt)("h2",{id:"references"},"References"),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html"},"Using a MySQL-compatible database as a source for AWS DMS")),(0,r.kt)("li",{parentName:"ol"},(0,r.kt)("a",{parentName:"li",href:"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html"},"Using Amazon S3 as a target for AWS Database Migration Service"))))}d.isMDXComponent=!0}}]);