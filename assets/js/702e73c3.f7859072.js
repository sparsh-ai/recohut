"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[11382],{3905:(e,t,a)=>{a.d(t,{Zo:()=>p,kt:()=>h});var n=a(67294);function i(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function o(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function r(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?o(Object(a),!0).forEach((function(t){i(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):o(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function l(e,t){if(null==e)return{};var a,n,i=function(e,t){if(null==e)return{};var a,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||(i[a]=e[a]);return i}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(i[a]=e[a])}return i}var s=n.createContext({}),u=function(e){var t=n.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):r(r({},t),e)),a},p=function(e){var t=u(e.components);return n.createElement(s.Provider,{value:t},e.children)},c={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},d=n.forwardRef((function(e,t){var a=e.components,i=e.mdxType,o=e.originalType,s=e.parentName,p=l(e,["components","mdxType","originalType","parentName"]),d=u(a),h=i,m=d["".concat(s,".").concat(h)]||d[h]||c[h]||o;return a?n.createElement(m,r(r({ref:t},p),{},{components:a})):n.createElement(m,r({ref:t},p))}));function h(e,t){var a=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var o=a.length,r=new Array(o);r[0]=d;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:i,r[1]=l;for(var u=2;u<o;u++)r[u]=a[u];return n.createElement.apply(null,r)}return n.createElement.apply(null,a)}d.displayName="MDXCreateElement"},37306:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>s,contentTitle:()=>r,default:()=>c,frontMatter:()=>o,metadata:()=>l,toc:()=>u});var n=a(87462),i=(a(67294),a(3905));const o={},r="Building and Executing a Pipeline Graph with Data Fusion",l={unversionedId:"orchestration/datafusion/lab-datafusion-pipeline/README",id:"orchestration/datafusion/lab-datafusion-pipeline/README",title:"Building and Executing a Pipeline Graph with Data Fusion",description:"Objective",source:"@site/docs/06-orchestration/datafusion/lab-datafusion-pipeline/README.md",sourceDirName:"06-orchestration/datafusion/lab-datafusion-pipeline",slug:"/orchestration/datafusion/lab-datafusion-pipeline/",permalink:"/docs/orchestration/datafusion/lab-datafusion-pipeline/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Cloud Data Fusion",permalink:"/docs/orchestration/datafusion/"},next:{title:"Modern Data Stack (MDS)",permalink:"/docs/orchestration/modern-data-stack/"}},s={},u=[{value:"Objective",id:"objective",level:2},{value:"Task 1. Creating a Cloud Data Fusion instance",id:"task-1-creating-a-cloud-data-fusion-instance",level:2},{value:"Task 2. Loading the data",id:"task-2-loading-the-data",level:2},{value:"Task 3. Cleaning the data",id:"task-3-cleaning-the-data",level:2},{value:"Task 4. Creating the pipeline",id:"task-4-creating-the-pipeline",level:2},{value:"Task 5. Adding a data source",id:"task-5-adding-a-data-source",level:2},{value:"Task 6. Joining two sources",id:"task-6-joining-two-sources",level:2},{value:"Task 7. Storing the output to BigQuery",id:"task-7-storing-the-output-to-bigquery",level:2},{value:"Task 8. Deploying and running the pipeline",id:"task-8-deploying-and-running-the-pipeline",level:2},{value:"Task 9. Viewing the results",id:"task-9-viewing-the-results",level:2}],p={toc:u};function c(e){let{components:t,...a}=e;return(0,i.kt)("wrapper",(0,n.Z)({},p,a,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"building-and-executing-a-pipeline-graph-with-data-fusion"},"Building and Executing a Pipeline Graph with Data Fusion"),(0,i.kt)("h2",{id:"objective"},"Objective"),(0,i.kt)("p",null,"This lab shows you how to use the Wrangler and Data Pipeline features in Cloud Data Fusion to clean, transform, and process taxi trip data for further analysis."),(0,i.kt)("p",null,"In this lab, you will:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Connect Cloud Data Fusion to a couple of data sources"),(0,i.kt)("li",{parentName:"ul"},"Apply basic transformations"),(0,i.kt)("li",{parentName:"ul"},"Join two data sources"),(0,i.kt)("li",{parentName:"ul"},"Write data to a sink")),(0,i.kt)("p",null,"Often times, data needs go through a number of pre-processing steps before analysts can leverage the data to glean insights. For example, data types may need to be adjusted, anomalies removed, and vague identifiers may need to be converted to more meaningful entries. Cloud Data Fusion is a service for efficiently building ETL/ELT data pipelines. Cloud Data Fusion uses Cloud Dataproc cluster to perform all transforms in the pipeline."),(0,i.kt)("p",null,"The use of Cloud Data Fusion will be exemplified in this tutorial by using a subset of the NYC TLC Taxi Trips dataset on BigQuery."),(0,i.kt)("h2",{id:"task-1-creating-a-cloud-data-fusion-instance"},"Task 1. Creating a Cloud Data Fusion instance"),(0,i.kt)("p",null,"Thorough directions for creating a Cloud Data Fusion instance can be found in the Creating a Cloud Data Fusion instance Guide. The essential steps are as follows:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"To ensure the training environment is properly configured you must first stop and restart the Cloud Data Fusion API. Run the command below in the Cloud Shell. It will take a few minutes to complete.")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"gcloud services disable datafusion.googleapis.com\ngcloud services enable datafusion.googleapis.com\n")),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"On the Navigation menu, select Data Fusion.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"To create a Cloud Data Fusion instance, click Create an Instance."),(0,i.kt)("ul",{parentName:"li"},(0,i.kt)("li",{parentName:"ul"},"Enter a name for your instance."),(0,i.kt)("li",{parentName:"ul"},"Select Basic for the Edition type."),(0,i.kt)("li",{parentName:"ul"},"Under Authorization section, click Grant Permission."),(0,i.kt)("li",{parentName:"ul"},"Leave all other fields as their defaults and click Create.")))),(0,i.kt)("p",null,"Note: Creation of the instance can take around 15 minutes."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Once the instance is created, you need one additional step to grant the service account associated with the instance permissions on your project. Navigate to the instance details page by clicking the instance name.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Copy the service account to your clipboard.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"In the GCP Console navigate to the IAM & Admin > IAM.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"On the IAM Permissions page, click +Grant Access add the service account you copied earlier as a new principals and grant the Cloud Data Fusion API Service Agent role.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Click Save."))),(0,i.kt)("h2",{id:"task-2-loading-the-data"},"Task 2. Loading the data"),(0,i.kt)("p",null,"Once the Cloud Data Fusion instance is up and running, you can start using Cloud Data Fusion. However, before Cloud Data Fusion can start ingesting data you have to take some preliminary steps."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"In this example, Cloud Data Fusion will read data out of a storage bucket. In the cloud shell console execute the following commands to create a new bucket and copy the relevant data into it:")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"export BUCKET=$GOOGLE_CLOUD_PROJECT\ngsutil mb gs://$BUCKET\ngsutil cp gs://cloud-training/OCBL017/ny-taxi-2018-sample.csv gs://$BUCKET\n")),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"In the command line, execute the following command to create a bucket for temporary storage items that Cloud data Fusion will create:")),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"gsutil mb gs://$BUCKET-temp\n")),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Click the View Instance link on the Data Fusion instances page, or the details page of an instance. Click username. If prompted to take a tour of the service click on No, Thanks. You should now be in the Cloud Data Fusion UI.")),(0,i.kt)("p",null,"Note: You may need to reload or refresh the Cloud Fusion UI pages to allow prompt loading of the page."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Wrangler is an interactive, visual tool that lets you see the effects of transformations on a small subset of your data before dispatching large, parallel-processing jobs on the entire dataset. On the Cloud Data Fusion UI, choose Wrangler. On the left side, there is a panel with the pre-configured connections to your data, including the Cloud Storage connection.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Under GCS, select Cloud Storage Default.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Click on the bucket corresponding to your project name.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Select ny-taxi-2018-sample.csv. The data is loaded into the Wrangler screen in row/column form.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"In the Parsing Options window, set Use First Row as Header as True. The data splits into multiple columns.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Click Confirm."))),(0,i.kt)("h2",{id:"task-3-cleaning-the-data"},"Task 3. Cleaning the data"),(0,i.kt)("p",null,"Now, you will perform some transformations to parse and clean the taxi data."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Click the Down arrow next to the trip_distance column, select Change data type and then click on Float. Repeat for the total_amount column.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Click the Down arrow next to the pickup_location_id column, select Change data type and then click on String.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"If you look at the data closely, you may find some anomalies, such as negative trip distances. You can avoid those negative values by filtering out in Wrangler. Click the Down arrow next to the trip_distance column and select Filter. Click if Custom condition and input >0.0")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Click on Apply."))),(0,i.kt)("p",null,(0,i.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214003271-cc4e8517-9deb-4dfb-977b-1e76025407aa.png",alt:null})),(0,i.kt)("h2",{id:"task-4-creating-the-pipeline"},"Task 4. Creating the pipeline"),(0,i.kt)("p",null,"Basic data cleansing is now complete and you've run transformations on a subset of your data. You can now create a batch pipeline to run transformations on all your data."),(0,i.kt)("p",null,"Cloud Data Fusion translates your visually built pipeline into an Apache Spark or MapReduce program that executes transformations on an ephemeral Cloud Dataproc cluster in parallel. This enables you to easily execute complex transformations over vast quantities of data in a scalable, reliable manner, without having to wrestle with infrastructure and technology."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"On the upper-right side of the Google Cloud Fusion UI, click Create a Pipeline.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"In the dialog that appears, select Batch pipeline.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"In the Data Pipelines UI, you will see a GCSFile source node connected to a Wrangler node. The Wrangler node contains all the transformations you applied in the Wrangler view captured as directive grammar. Hover over the Wrangler node and select Properties."))),(0,i.kt)("p",null,(0,i.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214003274-67c56282-204c-4504-ac20-811dcbbb0f55.png",alt:null})),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"At this stage, you can apply more transformations by clicking the Wrangle button. Delete the extra column by pressing the red trashcan icon beside its name. Click Validate on top right corner to check for any errors. To close the Wrangler tool click the X button in the top right corner.")),(0,i.kt)("h2",{id:"task-5-adding-a-data-source"},"Task 5. Adding a data source"),(0,i.kt)("p",null,"The taxi data contains several cryptic columns such as pickup_location_id, that aren't immediately transparent to an analyst. You are going to add a data source to the pipeline that maps the pickup_location_id column to a relevant location name. The mapping information will be stored in a BigQuery table."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"In a separate tab, open the BigQuery UI in the Cloud Console. Click Done on the 'Welcome to BigQuery in the Cloud Console' launch page.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"In the Explorer section of the BigQuery UI, click the three dots beside your GCP Project ID.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"On the menu that appears click the Create dataset link.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"In the Dataset ID field type in ",(0,i.kt)("inlineCode",{parentName:"p"},"trips"),".")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Click on Create dataset.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"To create the desired table in the newly created dataset, Go to editor window, navigate to More > Query Settings. This process will ensure you can access your table from Cloud Data Fusion.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Select the item for ",(0,i.kt)("inlineCode",{parentName:"p"},"Set a destination table for query results"),". For Dataset input ",(0,i.kt)("inlineCode",{parentName:"p"},"trips")," select from the dropdown. Table Id input ",(0,i.kt)("inlineCode",{parentName:"p"},"zone_id_mapping"),". Click Save.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Enter the following query in the Query Editor and then click Run:"))),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-sql"},"SELECT\n  zone_id,\n  zone_name,\n  borough\nFROM\n  `bigquery-public-data.new_york_taxi_trips.taxi_zone_geom`\n")),(0,i.kt)("p",null,(0,i.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214003169-24e75787-cf9a-4159-ac8c-949e30372d69.png",alt:null})),(0,i.kt)("p",null,"You can see that this table contains the mapping from zone_id to its name and borough."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Now, you will add a source in your pipeline to access this BigQuery table. Return to tab where you have Cloud Data Fusion open, from the Plugin palette on the left, select BigQuery from the Source section. A BigQuery source node appears on the canvas with the two other nodes.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Hover over the new BigQuery source node and click Properties.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"To configure the Reference Name, enter zone_mapping, which is used to identify this data source for lineage purposes.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"The BigQuery Dataset and Table configurations are the Dataset and Table you setup in BigQuery a few steps earlier: ",(0,i.kt)("inlineCode",{parentName:"p"},"trips")," and ",(0,i.kt)("inlineCode",{parentName:"p"},"zone_id_mapping"),'. For Temporary Bucket Name input the name of your project followed by "-temp", which corresponds to the bucket you created in Task 2.')),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"To populate the schema of this table from BigQuery, click Get Schema. The fields will appear on the right side of the wizard.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Click Validate on top right corner to check for any errors. To close the BigQuery Properties window click the X button in the top right corner."))),(0,i.kt)("h2",{id:"task-6-joining-two-sources"},"Task 6. Joining two sources"),(0,i.kt)("p",null,"Now you can join the two data sources\u2014taxi trip data and zone names\u2014to generate more meaningful output."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Under the Analytics section in the Plugin Palette, choose Joiner. A Joiner node appears on the canvas.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"To connect the Wrangler node and the BigQuery node to the Joiner node: Drag a connection arrow > on the right edge of the source node and drop on the destination node."))),(0,i.kt)("p",null,"To configure the Joiner node, which is similar to a SQL JOIN syntax:"),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},"Click Properties of Joiner."),(0,i.kt)("li",{parentName:"ul"},"Leave the label as Joiner."),(0,i.kt)("li",{parentName:"ul"},"Change the Join Type to Inner"),(0,i.kt)("li",{parentName:"ul"},"Set the Join Condition to join the pickup_location_id column in the Wrangler node to the zone_id column in the BigQuery node."),(0,i.kt)("li",{parentName:"ul"},"To generate the schema of the resultant join, click Get Schema."),(0,i.kt)("li",{parentName:"ul"},"In the Output Schema table on the right, remove the zone_id and pickup_location_id fields by hitting the red garbage can icon."),(0,i.kt)("li",{parentName:"ul"},"Click Validate on top right corner to check for any errors. Close the window by clicking the X button in the top right corner.")),(0,i.kt)("h2",{id:"task-7-storing-the-output-to-bigquery"},"Task 7. Storing the output to BigQuery"),(0,i.kt)("p",null,"You will store the result of the pipeline into a BigQuery table. Where you store your data is called a sink."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"In the Sink section of the Plugin Palette, choose BigQuery.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Connect the Joiner node to the BigQuery node. Drag a connection arrow > on the right edge of the source node and drop on the destination node.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},'Open the BigQuery2 node by hovering on it and then clicking Properties. You will use a configuration that\'s similar to the existing BigQuery source. Provide bq_insert for the Reference Name field and then use trips for the Dataset and the name of your project followed by "-temp" as Temporary Bucket Name. You will write to a new table that will be created for this pipeline execution. In Table field, enter trips_pickup_name.')),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Click Validate on top right corner to check for any errors. Close the window by clicking the X button in the top right corner."))),(0,i.kt)("h2",{id:"task-8-deploying-and-running-the-pipeline"},"Task 8. Deploying and running the pipeline"),(0,i.kt)("p",null,"At this point you have created your first pipeline and can deploy and run the pipeline."),(0,i.kt)("ul",null,(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Name your pipeline in the upper left corner of the Data Fusion UI and click Save.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"Now you will deploy the pipeline. In the upper-right corner of the page, click Deploy.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"On the next screen click Run to start processing data.")),(0,i.kt)("li",{parentName:"ul"},(0,i.kt)("p",{parentName:"li"},"When you run a pipeline, Cloud Data Fusion provisions an ephemeral Cloud Dataproc cluster, runs the pipeline, and then tears down the cluster. This could take a few minutes. You can observe the status of the pipeline transition from Provisioning to Starting and from Starting to Running to Succeeded during this time."))),(0,i.kt)("p",null,(0,i.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214003265-02ac63ea-b61c-46e7-bf5d-b1fc3c53b07d.png",alt:null})),(0,i.kt)("p",null,"Note: The pipeline transition may take 10-15 minutes to succeeded."),(0,i.kt)("p",null,(0,i.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214003268-0968dec2-638d-47c4-8c3e-9171b2cd2282.png",alt:null})),(0,i.kt)("h2",{id:"task-9-viewing-the-results"},"Task 9. Viewing the results"),(0,i.kt)("p",null,"To view the results after the pipeline runs:"),(0,i.kt)("p",null,"Return to the tab where you have BigQuery open. Run the query below to see the values in the trips_pickup_name table:"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"SELECT\n  *\nFROM\n  `trips.trips_pickup_name`\n")),(0,i.kt)("p",null,(0,i.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/214003172-c3b919d2-ca23-4098-a8e7-78eb9c358b7e.png",alt:null})),(0,i.kt)("p",null,"Congratulations!"))}c.isMDXComponent=!0}}]);