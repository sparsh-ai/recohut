"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[61521],{3905:(t,e,a)=>{a.d(e,{Zo:()=>d,kt:()=>m});var n=a(67294);function o(t,e,a){return e in t?Object.defineProperty(t,e,{value:a,enumerable:!0,configurable:!0,writable:!0}):t[e]=a,t}function r(t,e){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),a.push.apply(a,n)}return a}function i(t){for(var e=1;e<arguments.length;e++){var a=null!=arguments[e]?arguments[e]:{};e%2?r(Object(a),!0).forEach((function(e){o(t,e,a[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):r(Object(a)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(a,e))}))}return t}function s(t,e){if(null==t)return{};var a,n,o=function(t,e){if(null==t)return{};var a,n,o={},r=Object.keys(t);for(n=0;n<r.length;n++)a=r[n],e.indexOf(a)>=0||(o[a]=t[a]);return o}(t,e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(t);for(n=0;n<r.length;n++)a=r[n],e.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(t,a)&&(o[a]=t[a])}return o}var l=n.createContext({}),p=function(t){var e=n.useContext(l),a=e;return t&&(a="function"==typeof t?t(e):i(i({},e),t)),a},d=function(t){var e=p(t.components);return n.createElement(l.Provider,{value:e},t.children)},c={inlineCode:"code",wrapper:function(t){var e=t.children;return n.createElement(n.Fragment,{},e)}},u=n.forwardRef((function(t,e){var a=t.components,o=t.mdxType,r=t.originalType,l=t.parentName,d=s(t,["components","mdxType","originalType","parentName"]),u=p(a),m=o,h=u["".concat(l,".").concat(m)]||u[m]||c[m]||r;return a?n.createElement(h,i(i({ref:e},d),{},{components:a})):n.createElement(h,i({ref:e},d))}));function m(t,e){var a=arguments,o=e&&e.mdxType;if("string"==typeof t||o){var r=a.length,i=new Array(r);i[0]=u;var s={};for(var l in e)hasOwnProperty.call(e,l)&&(s[l]=e[l]);s.originalType=t,s.mdxType="string"==typeof t?t:o,i[1]=s;for(var p=2;p<r;p++)i[p]=a[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}u.displayName="MDXCreateElement"},56664:(t,e,a)=>{a.r(e),a.d(e,{assets:()=>l,contentTitle:()=>i,default:()=>c,frontMatter:()=>r,metadata:()=>s,toc:()=>p});var n=a(87462),o=(a(67294),a(3905));const r={},i="Data Pipeline with dbt, Airflow and Great Expectations",s={unversionedId:"capstones/robust-data-pipeline/README",id:"capstones/robust-data-pipeline/README",title:"Data Pipeline with dbt, Airflow and Great Expectations",description:"In this project, we will learn how to combine the functions of three open source tools - Airflow, dbt and Great expectations - to build, test, validate, document, and orchestrate an entire pipeline, end to end, from scratch. We are going to load the NYC Taxi data into Redshift warehouse and then transform + validate the data using dbt and great expectations.",source:"@site/docs/12-capstones/robust-data-pipeline/README.md",sourceDirName:"12-capstones/robust-data-pipeline",slug:"/capstones/robust-data-pipeline/",permalink:"/docs/capstones/robust-data-pipeline/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"AWS Kafka and DynamoDB for real time fraud detection",permalink:"/docs/capstones/redshield/"},next:{title:"Amazon Kinesis Data Streams",permalink:"/docs/capstones/smartcity/dataStream/"}},l={},p=[{value:"Project Structure",id:"project-structure",level:2}],d={toc:p};function c(t){let{components:e,...a}=t;return(0,o.kt)("wrapper",(0,n.Z)({},d,a,{components:e,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"data-pipeline-with-dbt-airflow-and-great-expectations"},"Data Pipeline with dbt, Airflow and Great Expectations"),(0,o.kt)("p",null,"In this project, we will learn how to combine the functions of three open source tools - Airflow, dbt and Great expectations - to build, test, validate, document, and orchestrate an entire pipeline, end to end, from scratch. We are going to load the NYC Taxi data into Redshift warehouse and then transform + validate the data using dbt and great expectations."),(0,o.kt)("p",null,"Data quality has become a much discussed topic in the fields of data engineering and data science, and it\u2019s become clear that data validation is crucial to ensuring the reliability of data products and insights produced by an organization\u2019s data pipelines. Apache Airflow and dbt (data build tool) are among the prominent open source tools in the data engineering ecosystem, and while dbt offers some data testing capabilities, another open source data tool, Great Expectations, enhances the pipeline with data validation and can add layers of robustness."),(0,o.kt)("p",null,(0,o.kt)("strong",{parentName:"p"},"By the end of this project, you\u2019ll understand:")),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"The basics of dbt, Airflow, and Great Expectations"),(0,o.kt)("li",{parentName:"ul"},"How to effectively combine these components to build a robust data pipeline"),(0,o.kt)("li",{parentName:"ul"},"When and how to implement data validation using these tools"),(0,o.kt)("li",{parentName:"ul"},"How to start developing a data quality strategy for your organization that goes beyond implementing data validation")),(0,o.kt)("p",null,(0,o.kt)("strong",{parentName:"p"},"And you\u2019ll be able to:")),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"Write and run Airflow, dbt, and Great Expectations code"),(0,o.kt)("li",{parentName:"ul"},"Design and implement a robust data pipeline"),(0,o.kt)("li",{parentName:"ul"},"Implement data validation and alerting across a data pipeline")),(0,o.kt)("p",null,(0,o.kt)("strong",{parentName:"p"},"This project is for you because\u2026")),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"You\u2019re a data engineer or analytics engineer who works with components of the dAG stack and wants to understand how to combine these tools."),(0,o.kt)("li",{parentName:"ul"},"You want to port existing data pipelines over to a modern data stack."),(0,o.kt)("li",{parentName:"ul"},"You\u2019re starting out in data engineering and want to better understand the types of tools used in the field.")),(0,o.kt)("p",null,(0,o.kt)("strong",{parentName:"p"},"Prerequisites")),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"Familiarity with Python and SQL (useful but not required)")),(0,o.kt)("p",null,(0,o.kt)("strong",{parentName:"p"},"Little bit of theory")),(0,o.kt)("p",null,"While there is a large number of data engineering frameworks have established themselves as leaders in the modern open-source data stack:"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"dbt (data build tool) is a framework that allows data teams to quickly iterate on building data transformation pipelines using templated SQL."),(0,o.kt)("li",{parentName:"ul"},"Apache Airflow is a workflow orchestration tool that enables users to define complex workflows as \u201cDAGs\u201d (directed acyclic graphs) made up of various tasks, as well as schedule and monitor execution."),(0,o.kt)("li",{parentName:"ul"},"Great Expectations is a python-based open-source data validation and documentation framework.")),(0,o.kt)("h2",{id:"project-structure"},"Project Structure"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre"},"\u251c\u2500\u2500 [6.6K]  01-sa-main.ipynb\n\u251c\u2500\u2500 [2.5K]  README.md\n\u251c\u2500\u2500 [ 48K]  airflow.cfg\n\u251c\u2500\u2500 [4.5K]  dags\n\u2502   \u251c\u2500\u2500 [1.5K]  dag1.py\n\u2502   \u251c\u2500\u2500 [1.3K]  dag2.py\n\u2502   \u2514\u2500\u2500 [1.5K]  dag3.py\n\u251c\u2500\u2500 [ 58K]  data.zip\n\u251c\u2500\u2500 [ 15K]  dbt\n\u2502   \u251c\u2500\u2500 [  96]  analysis\n\u2502   \u251c\u2500\u2500 [ 367]  dbt_project.yml\n\u2502   \u251c\u2500\u2500 [  96]  macros\n\u2502   \u251c\u2500\u2500 [2.7K]  models\n\u2502   \u2502   \u2514\u2500\u2500 [2.6K]  taxi\n\u2502   \u2502       \u251c\u2500\u2500 [ 362]  schema.yml\n\u2502   \u2502       \u251c\u2500\u2500 [1.7K]  staging\n\u2502   \u2502       \u2502   \u251c\u2500\u2500 [1.1K]  schema.yml\n\u2502   \u2502       \u2502   \u251c\u2500\u2500 [ 292]  taxi_trips_stage.sql\n\u2502   \u2502       \u2502   \u2514\u2500\u2500 [ 173]  taxi_zone_lookup_stage.sql\n\u2502   \u2502       \u2514\u2500\u2500 [ 396]  trips_with_borough_name.sql\n\u2502   \u251c\u2500\u2500 [ 233]  profiles.yml\n\u2502   \u251c\u2500\u2500 [ 497]  requirements.txt\n\u2502   \u251c\u2500\u2500 [ 10K]  seeds\n\u2502   \u2502   \u2514\u2500\u2500 [ 10K]  taxi_zone_lookup.csv\n\u2502   \u251c\u2500\u2500 [  96]  snapshots\n\u2502   \u2514\u2500\u2500 [  96]  tests\n\u251c\u2500\u2500 [   0]  download.sh\n\u251c\u2500\u2500 [ 18K]  great_expectations\n\u2502   \u251c\u2500\u2500 [1.9K]  checkpoints\n\u2502   \u2502   \u251c\u2500\u2500 [ 910]  yellow_tripdata_sample_2019_01.yml\n\u2502   \u2502   \u2514\u2500\u2500 [ 910]  yellow_tripdata_sample_2019_02.yml\n\u2502   \u251c\u2500\u2500 [2.2K]  expectations\n\u2502   \u2502   \u2514\u2500\u2500 [2.0K]  my_suite.json\n\u2502   \u251c\u2500\u2500 [4.2K]  great_expectations.yml\n\u2502   \u251c\u2500\u2500 [ 987]  plugins\n\u2502   \u2502   \u2514\u2500\u2500 [ 891]  custom_data_docs\n\u2502   \u2502       \u2514\u2500\u2500 [ 795]  styles\n\u2502   \u2502           \u2514\u2500\u2500 [ 699]  data_docs_custom_styles.css\n\u2502   \u2514\u2500\u2500 [8.8K]  scripts\n\u2502       \u251c\u2500\u2500 [ 581]  checkpoint_taxi_data_load_2019_3.py\n\u2502       \u251c\u2500\u2500 [ 919]  checkpoint_taxi_data_load_2019_3.yml\n\u2502       \u251c\u2500\u2500 [ 556]  create_checkpoint.py\n\u2502       \u251c\u2500\u2500 [ 556]  create_checkpoint_taxi_data_load_2019_1.py\n\u2502       \u251c\u2500\u2500 [ 765]  create_datasource.py\n\u2502       \u251c\u2500\u2500 [ 893]  my_checkpoint.yml\n\u2502       \u251c\u2500\u2500 [ 915]  my_checkpoint_taxi_data_load_2019_2.yml\n\u2502       \u251c\u2500\u2500 [ 915]  my_checkpoint_taxi_data_load_2019_3.yml\n\u2502       \u251c\u2500\u2500 [ 929]  sparsh_my_checkpoint_taxi_data_load_2019_3.yml\n\u2502       \u251c\u2500\u2500 [ 556]  taxi_data_load_2019_1.py\n\u2502       \u2514\u2500\u2500 [1.0K]  yellow_tripdata_taxi_checkpoints.py\n\u251c\u2500\u2500 [ 34K]  main.ipynb\n\u251c\u2500\u2500 [246K]  nbs\n\u2502   \u251c\u2500\u2500 [ 72K]  Data_Engineering_Lab___Airflow,_dbt_and_Great_Expectations.ipynb\n\u2502   \u251c\u2500\u2500 [ 54K]  Data_Engineering_Lab___Great_Expectations.ipynb\n\u2502   \u251c\u2500\u2500 [116K]  Data_Engineering_Lab___Transforming_Data_with_dbt.ipynb\n\u2502   \u2514\u2500\u2500 [4.8K]  session1.ipynb\n\u251c\u2500\u2500 [ 153]  requirements.txt\n\u2514\u2500\u2500 [ 545]  setup-simple.sh\n\n 435K used in 18 directories, 40 files\n")))}c.isMDXComponent=!0}}]);