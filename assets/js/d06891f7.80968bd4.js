"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[86768],{3905:(t,e,a)=>{a.d(e,{Zo:()=>s,kt:()=>m});var n=a(67294);function i(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function r(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function o(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?r(Object(a),!0).forEach((function(e){i(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):r(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function l(t,e){if(null==t)return{};var a,n,i=function(t,e){if(null==t)return{};var a,n,i={},r=Object.keys(t);for(n=0;n<r.length;n++)a=r[n],e.indexOf(a)>=0||(i[a]=t[a]);return i}(t,e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(t);for(n=0;n<r.length;n++)a=r[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(i[a]=t[a])}return i}var c=n.createContext({}),u=function(t){var e=n.useContext(c),a=e;return t&&(a="function"==typeof t?t(e):o(o({},e),t)),a},s=function(t){var e=u(t.components);return n.createElement(c.Provider,{value:e},t.children)},p={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},d=n.forwardRef((function(t,e){var a=t.components,i=t.mdxType,r=t.originalType,c=t.parentName,s=l(t,["components","mdxType","originalType","parentName"]),d=u(a),m=i,h=d["".concat(c,".").concat(m)]||d[m]||p[m]||r;return a?n.createElement(h,o(o({ref:e},s),{},{components:a})):n.createElement(h,o({ref:e},s))}));function m(t,e){var a=arguments,i=e&&e.mdxType;if("string"==typeof t||i){var r=a.length,o=new Array(r);o[0]=d;var l={};for(var c in e)hasOwnProperty.call(e,c)&&(l[c]=e[c]);l.originalType=t,l.mdxType="string"==typeof t?t:i,o[1]=l;for(var u=2;u<r;u++)o[u]=a[u];return n.createElement.apply(null,o)}return n.createElement.apply(null,a)}d.displayName="MDXCreateElement"},10932:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>c,contentTitle:()=>o,default:()=>p,frontMatter:()=>r,metadata:()=>l,toc:()=>u});var n=a(87462),i=(a(67294),a(3905));const r={},o="Building End to end data pipeline in AWS",l={unversionedId:"capstones/cloudmaze/README",id:"capstones/cloudmaze/README",title:"Building End to end data pipeline in AWS",description:"Architecture Diagram",source:"@site/docs/12-capstones/cloudmaze/README.md",sourceDirName:"12-capstones/cloudmaze",slug:"/capstones/cloudmaze/",permalink:"/docs/capstones/cloudmaze/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Global Historical Climatology Network Daily Data Pipeline",permalink:"/docs/capstones/climate/"},next:{title:"README",permalink:"/docs/capstones/dbt-redshift/"}},c={},u=[{value:"Architecture Diagram",id:"architecture-diagram",level:2},{value:"Activity 1: Ingestion with DMS",id:"activity-1-ingestion-with-dms",level:2},{value:"Activity 2: Data Lake Hydration",id:"activity-2-data-lake-hydration",level:2},{value:"Activity 3: DMS Migration",id:"activity-3-dms-migration",level:2},{value:"Activity 4: Transforming data with Glue - Data Validation and ETL",id:"activity-4-transforming-data-with-glue---data-validation-and-etl",level:2},{value:"Activity 5: Query and Visualize",id:"activity-5-query-and-visualize",level:2},{value:"Project Structure",id:"project-structure",level:2}],s={toc:u};function p(t){let{components:e,...a}=t;return(0,i.kt)("wrapper",(0,n.Z)({},s,a,{components:e,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"building-end-to-end-data-pipeline-in-aws"},"Building End to end data pipeline in AWS"),(0,i.kt)("h2",{id:"architecture-diagram"},"Architecture Diagram"),(0,i.kt)("p",null,(0,i.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/211014268-7050505c-bafc-431d-b95a-a2d05081e528.png",alt:null})),(0,i.kt)("h2",{id:"activity-1-ingestion-with-dms"},"Activity 1: Ingestion with DMS"),(0,i.kt)("p",null,"In this activity, you will complete the following tasks using AWS CloudFormation template:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Create the source database environment."),(0,i.kt)("li",{parentName:"ol"},"Hydrate the source database environment."),(0,i.kt)("li",{parentName:"ol"},"Update the source database environment to demonstrate Change Data Capture (CDC) replication within DMS."),(0,i.kt)("li",{parentName:"ol"},"Create a Lambda function to trigger the CDC data to be replicated to Amazon S3 from the DMS CDC endpoint.")),(0,i.kt)("p",null,"Relevant information about this activity:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Expected setup time | 15 minutes"),(0,i.kt)("li",{parentName:"ul"},"Source database name | sportstickets"),(0,i.kt)("li",{parentName:"ul"},"Source schema name | dms_sample"),(0,i.kt)("li",{parentName:"ul"},"Database credentials: adminuser/admin123")),(0,i.kt)("h2",{id:"activity-2-data-lake-hydration"},"Activity 2: Data Lake Hydration"),(0,i.kt)("p",null,"In this activity, you will complete the following prerequisites using an AWS CloudFormation template:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Create required VPC for AWS DMS instance."),(0,i.kt)("li",{parentName:"ol"},"Create Amazon S3 bucket for destination endpoint configuration."),(0,i.kt)("li",{parentName:"ol"},"Create Amazon S3 buckets for Amazon Athena query result storage."),(0,i.kt)("li",{parentName:"ol"},"Create required Amazon S3 bucket policy to put data from the AWS DMS service."),(0,i.kt)("li",{parentName:"ol"},"Create AWS Glue Service Role to use in later section of project."),(0,i.kt)("li",{parentName:"ol"},"Create Amazon Athena workgroup users to use in the Athena project."),(0,i.kt)("li",{parentName:"ol"},"Create Amazon Lake formation users to use in the Lake Formation project.")),(0,i.kt)("h2",{id:"activity-3-dms-migration"},"Activity 3: DMS Migration"),(0,i.kt)("p",null,"You will migrate data from an existing Amazon Relational Database Service (Amazon RDS) Postgres database to an Amazon Simple Storage Service (Amazon S3) bucket that you create."),(0,i.kt)("p",null,"In this activity you will complete the following tasks:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Create a subnet group within the DMS activity VPC"),(0,i.kt)("li",{parentName:"ol"},"Create a DMS replication instance"),(0,i.kt)("li",{parentName:"ol"},"Create a source endpoint"),(0,i.kt)("li",{parentName:"ol"},"Create a target endpoint"),(0,i.kt)("li",{parentName:"ol"},"Create a task to perform the initial migration of the data."),(0,i.kt)("li",{parentName:"ol"},"Create target endpoint for CDC files to place these files in a separate location than the initial load files"),(0,i.kt)("li",{parentName:"ol"},"Create a task to perform the ongoing replication of data changes")),(0,i.kt)("h2",{id:"activity-4-transforming-data-with-glue---data-validation-and-etl"},"Activity 4: Transforming data with Glue - Data Validation and ETL"),(0,i.kt)("p",null,"In this activity, you will:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Create Glue Crawler for initial full load data"),(0,i.kt)("li",{parentName:"ol"},"Create Glue Crawler for Parquet Files"),(0,i.kt)("li",{parentName:"ol"},"Transforming data with Glue - Incremental Data Processing with Hudi"),(0,i.kt)("li",{parentName:"ol"},"Create glue job and create HUDI table"),(0,i.kt)("li",{parentName:"ol"},"Query the HUDI table in Athena"),(0,i.kt)("li",{parentName:"ol"},"Upsert Incremental Changes"),(0,i.kt)("li",{parentName:"ol"},"Run Incremental Queries using Spark SQL")),(0,i.kt)("h2",{id:"activity-5-query-and-visualize"},"Activity 5: Query and Visualize"),(0,i.kt)("p",null,"In this activity, you will:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Query the data with Amazon Athena"),(0,i.kt)("li",{parentName:"ol"},"Connect Athena to Quicksight"),(0,i.kt)("li",{parentName:"ol"},"Build Dashboard in Amazon Quicksight")),(0,i.kt)("h2",{id:"project-structure"},"Project Structure"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},".\n\u251c\u2500\u2500 [ 61K]  01-sa.ipynb\n\u251c\u2500\u2500 [ 32K]  cfn\n\u2502   \u251c\u2500\u2500 [ 14K]  dms.yml\n\u2502   \u2514\u2500\u2500 [ 18K]  hydration.yml\n\u251c\u2500\u2500 [708K]  img\n\u2502   \u251c\u2500\u2500 [297K]  arch-diagram.png\n\u2502   \u251c\u2500\u2500 [ 84K]  athena-federated.png\n\u2502   \u2514\u2500\u2500 [327K]  dashboard.png\n\u251c\u2500\u2500 [3.1K]  README.md\n\u2514\u2500\u2500 [ 14K]  src\n    \u251c\u2500\u2500 [ 11K]  glu_hdi_ticket_purchase_hist.py\n    \u2514\u2500\u2500 [3.2K]  glu_hdi_ticket_purchase_hist_incremental.py\n\n 818K used in 3 directories, 9 files\n")))}p.isMDXComponent=!0}}]);