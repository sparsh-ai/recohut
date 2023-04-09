"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[84790],{3905:(e,t,a)=>{a.d(t,{Zo:()=>p,kt:()=>m});var n=a(67294);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function o(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?o(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):o(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function l(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},o=Object.keys(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var s=n.createContext({}),c=function(e){var t=n.useContext(s),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},p=function(e){var t=c(e.components);return n.createElement(s.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,o=e.originalType,s=e.parentName,p=l(e,["components","mdxType","originalType","parentName"]),u=c(a),m=r,f=u["".concat(s,".").concat(m)]||u[m]||d[m]||o;return a?n.createElement(f,i(i({ref:t},p),{},{components:a})):n.createElement(f,i({ref:t},p))}));function m(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var o=a.length,i=new Array(o);i[0]=u;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:r,i[1]=l;for(var c=2;c<o;c++)i[c]=a[c];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}u.displayName="MDXCreateElement"},83856:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>d,frontMatter:()=>o,metadata:()=>l,toc:()=>c});var n=a(87462),r=(a(67294),a(3905));const o={},i="AWS Kafka and DynamoDB for real time fraud detection",l={unversionedId:"capstones/redshield/README",id:"capstones/redshield/README",title:"AWS Kafka and DynamoDB for real time fraud detection",description:"Problem Statement",source:"@site/docs/12-capstones/redshield/README.md",sourceDirName:"12-capstones/redshield",slug:"/capstones/redshield/",permalink:"/docs/capstones/redshield/",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Reddit Submissions, Authors and Subreddits analysis",permalink:"/docs/capstones/reddit/"},next:{title:"Data Pipeline with dbt, Airflow and Great Expectations",permalink:"/docs/capstones/robust-data-pipeline/"}},s={},c=[{value:"Problem Statement",id:"problem-statement",level:2},{value:"Project Structure",id:"project-structure",level:2}],p={toc:c};function d(e){let{components:t,...a}=e;return(0,r.kt)("wrapper",(0,n.Z)({},p,a,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"aws-kafka-and-dynamodb-for-real-time-fraud-detection"},"AWS Kafka and DynamoDB for real time fraud detection"),(0,r.kt)("h2",{id:"problem-statement"},"Problem Statement"),(0,r.kt)("p",null,"Organizations need to move data in realtime and serve the data with minimal latency to their end users. Kafka is a real-time data pipeline used to move the data in real time. DynamoDB is a low-latency, high throughput data layer that can scale and handle extreme spikes in workload. These services work great together to enable use cases such as offloading mainframe banking data in real time to Kafka and ingesting the Kafka stream into DynamoDB. Once the data is in DynamoDB, it can be serve real-time requests from an API."),(0,r.kt)("p",null,"In this workshop, we add a Kinesis Data Analytics application to enable real-time fraud detection as this data is ingesting."),(0,r.kt)("p",null,"The environment for this lab consists of:"),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"An EC2 instance with kafdrop.",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Kafdrop is a web UI for viewing Kafka topics and browsing consumer groups. The tool displays information such as brokers, topics, partitions, consumers, and lets you view messages."))),(0,r.kt)("li",{parentName:"ul"},"In addition to the EC2 instance and networking components, the provided CloudFormation script creates the following AWS resources",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"A Managed Streaming for Kafka (MSK) cluster"),(0,r.kt)("li",{parentName:"ul"},"A Kinesis Data Anayltics application"),(0,r.kt)("li",{parentName:"ul"},"A DynamoDB fraud audit table")))),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Kafka Topics")),(0,r.kt)("ul",null,(0,r.kt)("li",{parentName:"ul"},"Demo_transactions.",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Topic to hold sample transactions (populated by Lambda SampleTransactionGenerator)"),(0,r.kt)("li",{parentName:"ul"},"This topic should have transaction as sample transaction lambda function was started by the cloud formation script"))),(0,r.kt)("li",{parentName:"ul"},"Flagged_accounts",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Topic to hold flagged account Ids (populated by Lambda FlagAccountGenerator)"),(0,r.kt)("li",{parentName:"ul"},"Initially, this topic will be empty as we need to manually run the lambda function to generate flagged acounts"))),(0,r.kt)("li",{parentName:"ul"},"Processed_topic",(0,r.kt)("ul",{parentName:"li"},(0,r.kt)("li",{parentName:"ul"},"Topic to hold flagged transactions (populated by flink application)"),(0,r.kt)("li",{parentName:"ul"},"Initially, this topic will also be empty but will become populated once the sample transaction can successfully join with Flagged Accounts")))),(0,r.kt)("p",null,"![arch]","(",(0,r.kt)("a",{parentName:"p",href:"https://user-images.githubusercontent.com/62965911/215308579-76b96550-f6a0-413a-b6bc-89f38e0874b6.png%5D"},"https://user-images.githubusercontent.com/62965911/215308579-76b96550-f6a0-413a-b6bc-89f38e0874b6.png]")),(0,r.kt)("h2",{id:"project-structure"},"Project Structure"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre"},".\n\u251c\u2500\u2500 [ 16K]  01-sa-kafka-dynamodb.ipynb\n\u251c\u2500\u2500 [2.0K]  assets\n\u2502   \u251c\u2500\u2500 [ 205]  download.sh\n\u2502   \u2514\u2500\u2500 [1.6K]  ee-default-keypair.pem\n\u251c\u2500\u2500 [ 52K]  cfn\n\u2502   \u2514\u2500\u2500 [ 51K]  fraud-detection-stack.json\n\u2514\u2500\u2500 [2.2K]  README.md\n\n 377K used in 2 directories, 5 files\n")))}d.isMDXComponent=!0}}]);