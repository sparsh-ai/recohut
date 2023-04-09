"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[62117],{3905:(e,t,a)=>{a.d(t,{Zo:()=>c,kt:()=>u});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function l(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function s(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?l(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function o(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},l=Object.keys(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var i=n.createContext({}),d=function(e){var t=n.useContext(i),a=t;return e&&(a="function"==typeof e?e(t):s(s({},t),e)),a},c=function(e){var t=d(e.components);return n.createElement(i.Provider,{value:t},e.children)},m={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},p=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,l=e.originalType,i=e.parentName,c=o(e,["components","mdxType","originalType","parentName"]),p=d(a),u=r,g=p["".concat(i,".").concat(u)]||p[u]||m[u]||l;return a?n.createElement(g,s(s({ref:t},c),{},{components:a})):n.createElement(g,s({ref:t},c))}));function u(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var l=a.length,s=new Array(l);s[0]=p;var o={};for(var i in t)hasOwnProperty.call(t,i)&&(o[i]=t[i]);o.originalType=e,o.mdxType="string"==typeof e?e:r,s[1]=o;for(var d=2;d<l;d++)s[d]=a[d];return n.createElement.apply(null,s)}return n.createElement.apply(null,a)}p.displayName="MDXCreateElement"},39311:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>i,contentTitle:()=>s,default:()=>m,frontMatter:()=>l,metadata:()=>o,toc:()=>d});var n=a(87462),r=(a(67294),a(3905));const l={},s="Postgres ELT Datamodel with PSQL",o={unversionedId:"data-modeling/lab-postgres-elt-datamodel/README",id:"data-modeling/lab-postgres-elt-datamodel/README",title:"Postgres ELT Datamodel with PSQL",description:"Create Fact and Dimension Tables from Denormalized Raw Data",source:"@site/docs/04-data-modeling/lab-postgres-elt-datamodel/README.md",sourceDirName:"04-data-modeling/lab-postgres-elt-datamodel",slug:"/data-modeling/lab-postgres-elt-datamodel/",permalink:"/docs/data-modeling/lab-postgres-elt-datamodel/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"lab-postgres-demographics-datamodel",permalink:"/docs/data-modeling/lab-postgres-demographics-datamodel"},next:{title:"Postgres ewallet Datamodel",permalink:"/docs/data-modeling/lab-postgres-ewallet-datamodel/"}},i={},d=[{value:"Login to Postgresql using psql",id:"login-to-postgresql-using-psql",level:2},{value:"Create Schema &amp; Rawdata table",id:"create-schema--rawdata-table",level:2},{value:"Import CSV data into Postgres table",id:"import-csv-data-into-postgres-table",level:2},{value:"Add a surrogate ID colum",id:"add-a-surrogate-id-colum",level:2},{value:"Identify the possible Dimensions",id:"identify-the-possible-dimensions",level:2},{value:"Build Fact table based on IDs from Dimension Table",id:"build-fact-table-based-on-ids-from-dimension-table",level:2}],c={toc:d};function m(e){let{components:t,...a}=e;return(0,r.kt)("wrapper",(0,n.Z)({},c,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"postgres-elt-datamodel-with-psql"},"Postgres ELT Datamodel with PSQL"),(0,r.kt)("blockquote",null,(0,r.kt)("p",{parentName:"blockquote"},"Create Fact and Dimension Tables from Denormalized Raw Data")),(0,r.kt)("p",null,"In data warehousing world there are occasions where developers have to reverse engineer model from flat csv files. We will understand this with simple example."),(0,r.kt)("h2",{id:"login-to-postgresql-using-psql"},"Login to Postgresql using psql"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"psql --host=database-1.cy8ltogyfgas.us-east-1.rds.amazonaws.com --port=5432 --username=postgres --password --dbname=sparsh\n")),(0,r.kt)("h2",{id:"create-schema--rawdata-table"},"Create Schema & Rawdata table"),(0,r.kt)("p",null,"This step is the dump the entire CSV into a ProstgreSQL table so its easier to clean or create Dimension tables."),(0,r.kt)("p",null,"Here we will be creating 3 schemas called landing, dim and fact. Schemas are very useful in grouping the tables logically."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"create schema elt_landing;\ncreate schema elt_dim;\ncreate schema elt_fact;\n")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"create table elt_landing.rawdata (\n    name varchar(100)\n    ,gender varchar(20)\n    ,profession varchar(50)\n    ,state varchar(2)\n    ,asofdate date\n    ,temperature float\n    ,pulse int\n);\n")),(0,r.kt)("p",null,"Verify the table & schema creation:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"\\dt elt_*.*\n")),(0,r.kt)("h2",{id:"import-csv-data-into-postgres-table"},"Import CSV data into Postgres table"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"\\COPY elt_landing.rawdata FROM 'data.csv' DELIMITER ',' CSV HEADER;\n")),(0,r.kt)("p",null,"Verify the data:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"select count(*) from elt_landing.rawdata;\nselect * from elt_landing.rawdata limit 10;\n")),(0,r.kt)("h2",{id:"add-a-surrogate-id-colum"},"Add a surrogate ID colum"),(0,r.kt)("blockquote",null,(0,r.kt)("p",{parentName:"blockquote"},"surrogate column means, column with sequence of numbers, generally auto generated.")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sh"},"alter table elt_landing.rawdata add id serial;\nselect * from elt_landing.rawdata limit 10;\n")),(0,r.kt)("h2",{id:"identify-the-possible-dimensions"},"Identify the possible Dimensions"),(0,r.kt)("p",null,"In this sample we can choose Gender, Name, State, Profession as possible dimensions."),(0,r.kt)("p",null,"Using select statement generate Dimension tables based on Distinct values."),(0,r.kt)("p",null,"Creating Gender dimension. Here the sub query returns the distinct genders and using the Windowing Function (row_number()) we are generating a unique ID for each gender."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"create table elt_dim.gender as \nselect \n    row_number() Over(order by gender) as genderid\n    ,gender \nfrom \n    (select distinct gender from elt_landing.rawdata) t;\n")),(0,r.kt)("p",null,"Similarly creating other Dimension tables:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"-- Second Query\n\ncreate table elt_dim.person as\nselect \n    row_number() Over(order by name) as personid\n   ,name \nfrom \n    (select distinct name from elt_landing.rawdata) t;\n\n-- Third Query\n\ncreate table elt_dim.profession as\nselect \n    row_number() Over(order by profession) as professionid\n    ,profession \nfrom \n    (select distinct profession from elt_landing.rawdata) t;\n\n-- Fourth Query\n\ncreate table elt_dim.state as \nselect \n    row_number() Over(order by state) as stateid\n    ,state \nfrom \n    (select distinct state from elt_landing.rawdata) t;\n")),(0,r.kt)("p",null,"Verify the Dimension tables:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"select * from elt_dim.person;\nselect * from elt_dim.profession;\nselect * from elt_dim.state;\nselect * from elt_dim.gender;\n")),(0,r.kt)("h2",{id:"build-fact-table-based-on-ids-from-dimension-table"},"Build Fact table based on IDs from Dimension Table"),(0,r.kt)("p",null,"This is the key step which will be generating the necessary Fact table. As the Dimensions are generated from landing data, JOIN will be used to build the fact table."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"create table elt_fact.user\nas\nselect\n    r.id\n    ,p.personid\n    ,g.genderid\n    ,pr.professionID\n    ,s.stateID\n    ,r.asofdate\n    ,r.temperature\n    ,r.pulse\nfrom\n    elt_landing.rawdata r\n    JOIN elt_dim.person as p on r.name = p.name\n    JOIN elt_dim.gender as g on r.gender = g.gender\n    JOIN elt_dim.profession as pr on r.profession = pr.profession\n    JOIN elt_dim.state as s on r.state = s.state;\n")),(0,r.kt)("p",null,"In the above query r.id is the Original Surrogate key from elt_landing.rawdata."),(0,r.kt)("p",null,"Compare and verify the data between elt_landing.rawdata and elt_fact.user table:"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"select * from elt_landing.rawdata where id = 1;\n")),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-sql"},"select * from elt_fact.user where id = 1;\nselect * from elt_dim.person where personid = 4;\n")),(0,r.kt)("p",null,"This is the basics, if needed the data can be normalized / modeled further."),(0,r.kt)("p",null,"Example : asofdate is used as part of Fact, if needed date can be normalized into Year, Month, Day for Snowflake Schema."))}m.isMDXComponent=!0}}]);