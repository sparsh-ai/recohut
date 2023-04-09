"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[9284],{3905:(e,t,a)=>{a.d(t,{Zo:()=>u,kt:()=>p});var n=a(67294);function i(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function r(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function o(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?r(Object(a),!0).forEach((function(t){i(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):r(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function l(e,t){if(null==e)return{};var a,n,i=function(e,t){if(null==e)return{};var a,n,i={},r=Object.keys(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||(i[a]=e[a]);return i}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(n=0;n<r.length;n++)a=r[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(i[a]=e[a])}return i}var s=n.createContext({}),d=function(e){var t=n.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):o(o({},t),e)),a},u=function(e){var t=d(e.components);return n.createElement(s.Provider,{value:t},e.children)},h={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var a=e.components,i=e.mdxType,r=e.originalType,s=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),m=d(a),p=i,c=m["".concat(s,".").concat(p)]||m[p]||h[p]||r;return a?n.createElement(c,o(o({ref:t},u),{},{components:a})):n.createElement(c,o({ref:t},u))}));function p(e,t){var a=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var r=a.length,o=new Array(r);o[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:i,o[1]=l;for(var d=2;d<r;d++)o[d]=a[d];return n.createElement.apply(null,o)}return n.createElement.apply(null,a)}m.displayName="MDXCreateElement"},79875:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>s,contentTitle:()=>o,default:()=>h,frontMatter:()=>r,metadata:()=>l,toc:()=>d});var n=a(87462),i=(a(67294),a(3905));const r={},o="Funflix",l={unversionedId:"capstones/funflix/README",id:"capstones/funflix/README",title:"Funflix",description:"You are working as a data engineer in an Australian media company Funflix. You got the following requirements and tasks to solve.",source:"@site/docs/12-capstones/funflix/README.md",sourceDirName:"12-capstones/funflix",slug:"/capstones/funflix/",permalink:"/docs/capstones/funflix/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Disaster Response Pipeline",permalink:"/docs/capstones/disaster-response/"},next:{title:"Datalake Schema Correction",permalink:"/docs/capstones/hmc/"}},s={},d=[{value:"Data Warehousing 1",id:"data-warehousing-1",level:2},{value:"Data Warehousing 2",id:"data-warehousing-2",level:2},{value:"Data Pipelining",id:"data-pipelining",level:2},{value:"Data Lake",id:"data-lake",level:2}],u={toc:d};function h(e){let{components:t,...a}=e;return(0,i.kt)("wrapper",(0,n.Z)({},u,a,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"funflix"},"Funflix"),(0,i.kt)("p",null,"You are working as a data engineer in an Australian media company Funflix. You got the following requirements and tasks to solve."),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Design the data warehouse for Funflix"),(0,i.kt)("li",{parentName:"ol"},"Build and deploy the data pipeline for Funflix's multi-region business"),(0,i.kt)("li",{parentName:"ol"},"Build a data lake")),(0,i.kt)("h2",{id:"data-warehousing-1"},"Data Warehousing 1"),(0,i.kt)("p",null,"Funflix recently acquired a medical company named Gluewell clinic which provided various medical therapies. The data engineering integration process is going on and you are part of the integration team."),(0,i.kt)("p",null,"Your analyst team is busy in some other part and needs your help in getting some insights, as it requires some bit of data modeling work, from Gluewell datasets. You have to perform the following steps:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"In Postgres database, create a schema named ",(0,i.kt)("inlineCode",{parentName:"li"},"funflix_datamodel"),"."),(0,i.kt)("li",{parentName:"ol"},"Upload the 4 raw files in this schema. Table names will be same as file names."),(0,i.kt)("li",{parentName:"ol"},"Create a star schema (Entity-Relation Diagram). Use ",(0,i.kt)("a",{parentName:"li",href:"https://dbdiagram.io/"},"https://dbdiagram.io/")," to create it. Once created, export the diagram as png and save it in your system."),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("table",{parentName:"li"},(0,i.kt)("thead",{parentName:"table"},(0,i.kt)("tr",{parentName:"thead"},(0,i.kt)("th",{parentName:"tr",align:null},"Write SQL queries to answer the following questions. For each of these queries, create a view in the same schema."),(0,i.kt)("th",{parentName:"tr",align:null},"Query"))),(0,i.kt)("tbody",{parentName:"table"},(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"How many customers visited the clinic in february 2022?"),(0,i.kt)("td",{parentName:"tr",align:null},"customer_feb22")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"What was the most booked service in march 2022?"),(0,i.kt)("td",{parentName:"tr",align:null},"service_mar22")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"Who were the top-5 customers who visited the most in Q1 2022 (i.e. Jan-Mar 2022)?"),(0,i.kt)("td",{parentName:"tr",align:null},"customer_top5_q122")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"What are the top-3 most booked services by the most visited customer?"),(0,i.kt)("td",{parentName:"tr",align:null},"service_top3")),(0,i.kt)("tr",{parentName:"tbody"},(0,i.kt)("td",{parentName:"tr",align:null},"Which therapist is most experienced in physiotherapy?"),(0,i.kt)("td",{parentName:"tr",align:null},"therapist_experience"))))),(0,i.kt)("li",{parentName:"ol"},"Generate a Markdown report of your work and submit it in your branch named ",(0,i.kt)("inlineCode",{parentName:"li"},"<your git username>/assignment-funflix"),". You need to put the report in ",(0,i.kt)("inlineCode",{parentName:"li"},"/assignments/funflix/modeling/your git username")," folder. Make sure to include schema diagram, explanations of your work and other key details in the report."),(0,i.kt)("li",{parentName:"ol"},"Create PR and notify the instructor for review.")),(0,i.kt)("h2",{id:"data-warehousing-2"},"Data Warehousing 2"),(0,i.kt)("p",null,"Customers comes to Funflix\u2019s platform and subscribe to become a subscribed user. Funflix content experts then hand picks a collection of movies as per user\u2019s taste and sends these recommendations to the user via email. Things are going well so far but Funflix\u2019s executive team do not see potential growth into future with the existing IT arrangements and asked you to innovate their company\u2019s IT processes to enable Funflix\u2019s future growth."),(0,i.kt)("p",null,"Ele is Funflix\u2019s IT expert and she knows all about the current systems and she is also your POC (point-of-contact) in this project. Here are the key points of the 1st meeting between you and Ele:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"You: I would like to know about the state of data. How it looks, where it is, Who does what?\n\nEle: We have a user data in which we store our subscribers\u2019 details, a movie data to store movie details and we also collect our user\u2019s feedback on movies. All the data is in 3 files that we maintain in MS-Excel on our local server.\n\nYou: How can I get access this data?\n\nEle: I can email you these 3 files or share them via pen-drive? The file size is not much.\n\nYou: Okay, you can email them then.\n")),(0,i.kt)("p",null,"You got the data via email (email is archived for you in the git repo) and now it\u2019s time to start the innovative work. You will perform the following steps:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},"Create a schema named ",(0,i.kt)("inlineCode",{parentName:"li"},"funflix_warehouse"),"."),(0,i.kt)("li",{parentName:"ol"},"Now, as you got 3 files in mail \u2014 for each file, do the following:",(0,i.kt)("ol",{parentName:"li"},(0,i.kt)("li",{parentName:"ol"},"Load into a dataframe (pandas or Pyspark dataframe e.g.)"),(0,i.kt)("li",{parentName:"ol"},"Add column names. You can find the list of columns here:",(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"cols",(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"['userid','age','gender','occupation',\"zipcode\"]"),(0,i.kt)("li",{parentName:"ul"},'["movieid", "movie_title", "release_date", "video_release_date", "imdb_url", "unknown", "action", "adventure", "animation", "children", "comedy", "crime", "documentary", "drama", "fantasy", "film_noir", "horror", "musical", "mystery", "romance", "scifi", "thriller", "war", "western"]'),(0,i.kt)("li",{parentName:"ul"},"['userid','itemid','rating','timestamp']"))))),(0,i.kt)("li",{parentName:"ol"},"Push the dataframe to database with correct schema."))),(0,i.kt)("li",{parentName:"ol"},"Go to RedShift query editor in AWS and verify if data has been updated corrrectly. e.g. In case of John Doe, it would look like this:\n",(0,i.kt)("img",{parentName:"li",src:"https://user-images.githubusercontent.com/62965911/215305042-35cd1b73-d793-42fe-a97e-44182ddf88ca.png",alt:"data-ingestion-redshift-example-1"})),(0,i.kt)("li",{parentName:"ol"},"Analyze the DDLs in Redshift and use this analysis to create a schema diagram (Entity-Relation Diagram). Use ",(0,i.kt)("a",{parentName:"li",href:"https://dbdiagram.io/"},"https://dbdiagram.io/")," to create it."),(0,i.kt)("li",{parentName:"ol"},"Generate a Markdown report of your work and submit it in your branch named ",(0,i.kt)("inlineCode",{parentName:"li"},"<your git username>/assignment-funflix"),". You need to put the report in ",(0,i.kt)("inlineCode",{parentName:"li"},"/assignments/funflix/warehousing/your git username")," folder. Make sure to include schema diagram, explanations of your work and other key details in the report."),(0,i.kt)("li",{parentName:"ol"},"Create PR and notify the instructor for review.")),(0,i.kt)("h2",{id:"data-pipelining"},"Data Pipelining"),(0,i.kt)("blockquote",null,(0,i.kt)("p",{parentName:"blockquote"},"An online retailer has a website where you can purchase widgets in a variety of colours. The website is backed by a relational database. Every transaction is stored in the database. How many blue widgets did the retailer sell in the last quarter?")),(0,i.kt)("p",null,"To answer this question, you could run a SQL query on the database. This doesn't rise to the level of needing a data engineer. But as the site grows, running queries on the production database is no longer practical. Furthermore, there may be more than one database that records transactions. There may be a database at different geographical locations \u2013 for example, the retailers in North America may have a different database than the retailers in Asia, Africa, and Europe."),(0,i.kt)("p",null,"Now you have entered the realm of data engineering. To answer the preceding question, a data engineer would create connections to all of the transactional databases for each region, extract the data, and load it into a data warehouse. From there, you could now count the number of all the blue widgets sold."),(0,i.kt)("p",null,"Rather than finding the number of blue widgets sold, companies would prefer to find the answer to the following questions:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"How do we find out which locations sell the most widgets?"),(0,i.kt)("li",{parentName:"ul"},"How do we find out the peak times for selling widgets?"),(0,i.kt)("li",{parentName:"ul"},"How many users put widgets in their carts and remove them later?"),(0,i.kt)("li",{parentName:"ul"},"How do we find out the combinations of widgets that are sold together?")),(0,i.kt)("p",null,"Answering these questions requires more than just extracting the data and loading it into a single system. There is a transformation required in between the extract and load. There is also the difference in times zones in different regions. For instance, the United States alone has four time zones. Because of this, you would need to transform time fields to a standard. You will also need a way to distinguish sales in each region. This could be accomplished by adding a location field to the data. Should this field be spatial \u2013 in coordinates or as well-known text \u2013 or will it just be text that could be transformed in a data engineering pipeline?"),(0,i.kt)("p",null,"Here, the data engineer would need to extract the data from each database, then transform the data by adding an additional field for the location. To compare the time zones, the data engineer would need to be familiar with data standards. For the time, the International Organization for Standardization (ISO) has a standard \u2013 ISO 8601."),(0,i.kt)("p",null,"Let's now answer the questions in the preceding list one by one:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Extract the data from each database."),(0,i.kt)("li",{parentName:"ul"},"Add a field to tag the location for each transaction in the data."),(0,i.kt)("li",{parentName:"ul"},"Transform the date from local time to ISO 8601."),(0,i.kt)("li",{parentName:"ul"},"Load the data into the data warehouse.")),(0,i.kt)("p",null,"The combination of extracting, loading, and transforming data is accomplished by the creation of a data pipeline. The data comes into the pipeline raw, or dirty in the sense that there may be missing data or typos in the data, which is then cleaned as it flows through the pipe. After that, it comes out the other side into a data warehouse, where it can be queried. The following diagram shows the pipeline required to accomplish the task:"),(0,i.kt)("p",null,(0,i.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/215305336-d033411c-ddf3-4ecd-a04f-fb1fc7f5ede1.png",alt:"data-pipe-example-1"})),(0,i.kt)("p",null,"Funflix runs its business globally in two regions - American and European. Mitch is the Sales Head of American region and Shiva is Sales Head of European region. Funflix needs your help in doing something similar to the above use case (the reading material) to collect their data from these regions and load them in their Warehouse. They also expecting to get some answers related to their overall sales that Mitch and Shiva can not answer at the moment because they don\u2019t have the global data. (\ud83d\udca1\xa0Data is in Silos!)."),(0,i.kt)("p",null,"Mitch shared the american region data."),(0,i.kt)("p",null,"Shiva on the other hand wants you to pull the data directly from the database. The credentials are in the AWS Secret Manager."),(0,i.kt)("p",null,"You got the data related information and now it\u2019s time to start the work. You will perform the following steps:"),(0,i.kt)("ol",null,(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Pull the data for both regions and store in your system.")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Create a schema in the database. Schema name should be like ",(0,i.kt)("inlineCode",{parentName:"p"},"funflix_pipeline"),".")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"It\u2019s time to follow the instructions that you read during the case study and apply them here. To summarize those again, this is what you need to do:"),(0,i.kt)("ol",{parentName:"li"},(0,i.kt)("li",{parentName:"ol"},"Read the data from raw layer for both regions in separate tables."),(0,i.kt)("li",{parentName:"ol"},"Add a field to tag the location for each transaction in the data."),(0,i.kt)("li",{parentName:"ol"},"Transform the date from local time to ISO 8601."),(0,i.kt)("li",{parentName:"ol"},"Merge the data into a single table named ",(0,i.kt)("inlineCode",{parentName:"li"},"sales"),"."),(0,i.kt)("li",{parentName:"ol"},"Load the data into the data warehouse.")),(0,i.kt)("p",{parentName:"li"},"The combination of extracting, loading, and transforming data is accomplished by the creation of a data pipeline. The data comes into the pipeline raw, or dirty in the sense that there may be missing data or typos in the data, which is then cleaned as it flows through the pipe. After that, it comes out the other side into a data warehouse, where it can be queried.")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Go to DBeaver, setup the warehouse connection and verify if data has been updated corrrectly.")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Generate a Markdown report of your work and submit it in your branch named ",(0,i.kt)("inlineCode",{parentName:"p"},"<your git username>/assignment-funflix"),". You need to put the report in ",(0,i.kt)("inlineCode",{parentName:"p"},"/assignments/funflix/pipeline/your git username")," folder. Make sure to include explanations of your work and other key details in the report.")),(0,i.kt)("li",{parentName:"ol"},(0,i.kt)("p",{parentName:"li"},"Create PR and notify the instructor for review."))),(0,i.kt)("h2",{id:"data-lake"},"Data Lake"),(0,i.kt)("p",null,"Your goal is to build a data lake pipeline with Python and AWS. Follow this architecture:"),(0,i.kt)("p",null,(0,i.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/215305348-4381282a-5770-4dbf-9d0d-36c719fadb38.svg",alt:"process_flow drawio"})))}h.isMDXComponent=!0}}]);